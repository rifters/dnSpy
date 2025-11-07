#!/usr/bin/env python3
"""
Public API documentation generator for the dnSpy codebase.

This script scans all C# source files, extracts the publicly visible surface
area (types and members), and emits Markdown documentation grouped by
namespace. Where XML documentation comments exist, they are incorporated into
the output along with automatically synthesised usage snippets.
"""

from __future__ import annotations

import argparse
import dataclasses
import os
import re
import shutil
import sys
import textwrap
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from typing import Iterable, List, Optional

from tree_sitter import Node
from tree_sitter_languages import get_parser


# -----------------------------------------------------------------------------
# Data containers
# -----------------------------------------------------------------------------


@dataclasses.dataclass
class SourceLocation:
    path: Path
    line: int


@dataclasses.dataclass
class ParameterDoc:
    name: str
    type: str
    modifiers: List[str] = dataclasses.field(default_factory=list)
    default: Optional[str] = None
    summary: Optional[str] = None


@dataclasses.dataclass
class MemberDoc:
    name: str
    kind: str
    signature: str
    summary: Optional[str] = None
    remarks: Optional[str] = None
    returns: Optional[str] = None
    parameters: List[ParameterDoc] = dataclasses.field(default_factory=list)
    examples: List[str] = dataclasses.field(default_factory=list)
    modifiers: List[str] = dataclasses.field(default_factory=list)
    source: Optional[SourceLocation] = None


@dataclasses.dataclass
class EnumValueDoc:
    name: str
    value: Optional[str]
    summary: Optional[str]
    source: Optional[SourceLocation] = None


@dataclasses.dataclass
class TypeDoc:
    namespace: str
    full_name: str
    name: str
    kind: str
    modifiers: List[str]
    type_parameters: Optional[str]
    base_types: List[str] = dataclasses.field(default_factory=list)
    summary: Optional[str] = None
    remarks: Optional[str] = None
    examples: List[str] = dataclasses.field(default_factory=list)
    members: dict[str, List[MemberDoc]] = dataclasses.field(
        default_factory=lambda: defaultdict(list)
    )
    enum_values: List[EnumValueDoc] = dataclasses.field(default_factory=list)
    sources: List[SourceLocation] = dataclasses.field(default_factory=list)

    def add_member(self, category: str, member: MemberDoc) -> None:
        """Add a member doc, deduplicating by signature."""
        existing_signatures = {m.signature for m in self.members[category]}
        if member.signature not in existing_signatures:
            self.members[category].append(member)

    def add_enum_value(self, enum_value: EnumValueDoc) -> None:
        existing_names = {v.name for v in self.enum_values}
        if enum_value.name not in existing_names:
            self.enum_values.append(enum_value)


# -----------------------------------------------------------------------------
# Tree-sitter helpers
# -----------------------------------------------------------------------------


def node_text(source: bytes, node: Node) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8", errors="ignore")


def collect_modifiers(source: bytes, node: Node) -> List[str]:
    return [
        node_text(source, child)
        for child in node.children
        if child.type == "modifier"
    ]


def is_accessible(modifiers: Iterable[str], *, include_protected: bool = True) -> bool:
    mods = set(modifiers)
    if "public" in mods:
        return True
    protected_keywords = {"protected", "protected internal", "internal protected"}
    if include_protected and ("protected" in mods or any(k in " ".join(mods) for k in protected_keywords)):
        return True
    return False


def combine_namespace(current: str, addition: str) -> str:
    if not current:
        return addition or ""
    if not addition:
        return current
    return f"{current}.{addition}"


def sanitize_namespace(namespace: str) -> str:
    return namespace or "global"


def sanitize_filename(name: str) -> str:
    sanitized = re.sub(r"[<>:\"/\\\\|?*]", "_", name)
    sanitized = sanitized.replace("`", "_")
    return sanitized


def collect_leading_doc_comment(source: bytes, node: Node) -> str:
    comments: List[str] = []
    current = node
    while True:
        prev = current.prev_named_sibling
        if prev is None:
            break
        if prev.type == "attribute_list":
            current = prev
            continue
        if prev.type != "comment":
            break
        text = node_text(source, prev).strip()
        if text.startswith("///") or text.startswith("/**"):
            comments.append(text)
            current = prev
            continue
        break
    comments.reverse()
    return "\n".join(comments)


def parse_xml_documentation(doc_comment: str) -> dict:
    if not doc_comment:
        return {}

    lines: List[str] = []
    for raw_line in doc_comment.splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("///"):
            content = stripped[3:]
            if content.startswith(" "):
                content = content[1:]
            lines.append(content)
        elif stripped.startswith("/**"):
            content = stripped.lstrip("/*").rstrip("*/").strip()
            lines.append(content)
        else:
            lines.append(stripped)

    xml_text = "\n".join(lines).strip()
    if not xml_text:
        return {}

    wrapped = f"<root>{xml_text}</root>"
    try:
        root = ET.fromstring(wrapped)
    except ET.ParseError:
        # Fall back to treating the summary as raw text.
        return {"summary": xml_text}

    def extract_text(tag: str) -> Optional[str]:
        elem = root.find(tag)
        if elem is None:
            return None
        text = "".join(elem.itertext()).strip()
        return " ".join(text.split()) if text else None

    data: dict = {
        "summary": extract_text("summary"),
        "remarks": extract_text("remarks"),
        "returns": extract_text("returns"),
        "examples": [
            textwrap.dedent("".join(example.itertext())).strip()
            for example in root.findall("example")
        ],
        "params": {},
        "typeparam": {},
    }

    for param in root.findall("param"):
        name = param.attrib.get("name")
        if not name:
            continue
        text = "".join(param.itertext()).strip()
        data["params"][name] = " ".join(text.split()) if text else None

    for tparam in root.findall("typeparam"):
        name = tparam.attrib.get("name")
        if not name:
            continue
        text = "".join(tparam.itertext()).strip()
        data["typeparam"][name] = " ".join(text.split()) if text else None

    if not data["examples"]:
        data.pop("examples")

    return data


# -----------------------------------------------------------------------------
# Extraction logic
# -----------------------------------------------------------------------------


TYPE_NODE_KINDS = {
    "class_declaration": "class",
    "struct_declaration": "struct",
    "interface_declaration": "interface",
    "enum_declaration": "enum",
    "delegate_declaration": "delegate",
    "record_declaration": "record",
    "record_struct_declaration": "record struct",
}


def extract_public_api(
    parser, source: bytes, file_path: Path, namespace: str, node: Node, types: dict
) -> None:
    """Traverse nodes to extract type and member metadata."""
    for child in node.children:
        if child.type == "namespace_declaration":
            name_node = child.child_by_field_name("name")
            new_namespace = combine_namespace(
                namespace, node_text(source, name_node).strip()
            )
            body = child.child_by_field_name("body")
            if body:
                extract_public_api(
                    parser, source, file_path, new_namespace, body, types
                )
            continue
        if child.type == "file_scoped_namespace_declaration":
            name_node = child.child_by_field_name("name")
            new_namespace = combine_namespace(
                namespace, node_text(source, name_node).strip()
            )
            # The remaining named children are declarations.
            remaining_children = [
                grandchild
                for grandchild in child.children
                if grandchild.type
                not in {"namespace", ";", "identifier", "qualified_name"}
            ]
            temp_node = DummyNode(remaining_children)
            extract_public_api(parser, source, file_path, new_namespace, temp_node, types)
            continue

        if child.type in TYPE_NODE_KINDS:
            process_type_declaration(
                source, file_path, namespace, child, types
            )
            continue

        if child.child_count:
            extract_public_api(parser, source, file_path, namespace, child, types)


class DummyNode:
    """Helper wrapper to allow iterating a synthetic node list."""

    def __init__(self, children: List[Node]):
        self.children = children


def process_type_declaration(
    source: bytes,
    file_path: Path,
    namespace: str,
    node: Node,
    types: dict[str, TypeDoc],
    type_stack: Optional[List[str]] = None,
) -> None:
    type_stack = type_stack or []

    modifiers = collect_modifiers(source, node)
    if not is_accessible(modifiers, include_protected=False):
        # Nested types inherit accessibility from their parents; we will only include
        # types explicitly marked public.
        return

    kind = TYPE_NODE_KINDS[node.type]
    name_node = node.child_by_field_name("name")
    if name_node is None:
        return
    name_text = node_text(source, name_node).strip()
    type_parameters_node = node.child_by_field_name("type_parameters")
    type_parameters = (
        node_text(source, type_parameters_node).strip()
        if type_parameters_node is not None
        else None
    )

    full_type_stack = [*type_stack, name_text + (type_parameters or "")]
    namespace_key = sanitize_namespace(namespace)
    full_name = ".".join(
        part for part in [namespace_key, *full_type_stack] if part
    )

    typedoc = types.get(full_name)
    if typedoc is None:
        typedoc = TypeDoc(
            namespace=namespace_key,
            full_name=full_name,
            name=name_text,
            kind=kind,
            modifiers=modifiers,
            type_parameters=type_parameters,
        )
        types[full_name] = typedoc

    typedoc.sources.append(
        SourceLocation(path=file_path, line=node.start_point[0] + 1)
    )

    base_list = None
    for child in node.children:
        if child.type == "base_list":
            base_list = node_text(source, child)
            break
    if base_list:
        typedoc.base_types = [
            part.strip()
            for part in base_list.split(":")[1].split(",")
            if part.strip()
        ]

    doc_comment = parse_xml_documentation(collect_leading_doc_comment(source, node))
    if doc_comment.get("summary") and not typedoc.summary:
        typedoc.summary = doc_comment.get("summary")
    if doc_comment.get("remarks"):
        typedoc.remarks = doc_comment.get("remarks")
    if doc_comment.get("examples"):
        typedoc.examples.extend(
            example for example in doc_comment["examples"] if example not in typedoc.examples
        )

    body = node.child_by_field_name("body")
    if body is None:
        return

    for child in body.children:
        if child.type in TYPE_NODE_KINDS:
            process_type_declaration(
                source,
                file_path,
                namespace,
                child,
                types,
                type_stack=full_type_stack,
            )
        else:
            process_member_declaration(
                source, file_path, namespace, typedoc, child
            )


def process_member_declaration(
    source: bytes,
    file_path: Path,
    namespace: str,
    typedoc: TypeDoc,
    node: Node,
) -> None:
    member_kind = node.type
    if member_kind not in {
        "constructor_declaration",
        "method_declaration",
        "property_declaration",
        "indexer_declaration",
        "field_declaration",
        "event_field_declaration",
        "event_declaration",
        "operator_declaration",
        "conversion_operator_declaration",
        "enum_member_declaration",
    }:
        return

    if member_kind == "enum_member_declaration":
        process_enum_member(source, file_path, typedoc, node)
        return

    modifiers = collect_modifiers(source, node)
    if not modifiers and typedoc.kind == "interface":
        # Interface members are implicitly public.
        accessible = True
    else:
        accessible = is_accessible(modifiers)
    if not accessible:
        return

    doc_comment = parse_xml_documentation(collect_leading_doc_comment(source, node))

    if member_kind == "constructor_declaration":
        name_node = node.child_by_field_name("name")
        name = node_text(source, name_node)
        parameters = extract_parameters(source, node.child_by_field_name("parameters"))
        signature = build_constructor_signature(source, node, name, parameters)
        member_doc = MemberDoc(
            name=name,
            kind="constructor",
            signature=signature,
            summary=doc_comment.get("summary"),
            remarks=doc_comment.get("remarks"),
            parameters=merge_parameter_summaries(parameters, doc_comment),
            examples=doc_comment.get("examples", []),
            modifiers=modifiers,
            source=SourceLocation(file_path, node.start_point[0] + 1),
        )
        typedoc.add_member("constructors", member_doc)
        return

    if member_kind == "method_declaration":
        process_method(source, file_path, typedoc, node, modifiers, doc_comment)
        return

    if member_kind == "property_declaration":
        process_property(source, file_path, typedoc, node, modifiers, doc_comment)
        return

    if member_kind == "indexer_declaration":
        process_indexer(source, file_path, typedoc, node, modifiers, doc_comment)
        return

    if member_kind in ("event_declaration", "event_field_declaration"):
        process_event(source, file_path, typedoc, node, modifiers, doc_comment)
        return

    if member_kind in ("field_declaration",):
        process_field(source, file_path, typedoc, node, modifiers, doc_comment)
        return

    if member_kind in ("operator_declaration", "conversion_operator_declaration"):
        process_operator(source, file_path, typedoc, node, modifiers, doc_comment)
        return


def merge_parameter_summaries(parameters: List[ParameterDoc], doc_comment: dict) -> List[ParameterDoc]:
    param_docs = doc_comment.get("params", {})
    for param in parameters:
        if param.name in param_docs and param_docs[param.name]:
            param.summary = param_docs[param.name]
    return parameters


def extract_parameters(source: bytes, parameters_node: Optional[Node]) -> List[ParameterDoc]:
    if parameters_node is None:
        return []
    params: List[ParameterDoc] = []
    for child in parameters_node.children:
        if child.type != "parameter":
            continue
        modifiers = [
            node_text(source, c) for c in child.children if c.type == "parameter_modifier"
        ]
        type_node = child.child_by_field_name("type")
        name_node = child.child_by_field_name("name")
        default_value = None
        for c in child.children:
            if c.type == "equals_value_clause":
                text = node_text(source, c)
                if "=" in text:
                    default_value = text.split("=", 1)[1].strip()
                else:
                    default_value = text.strip()
        params.append(
            ParameterDoc(
                name=node_text(source, name_node) if name_node else "",
                type=node_text(source, type_node) if type_node else "",
                modifiers=modifiers,
                default=default_value,
            )
        )
    return params


def build_constructor_signature(
    source: bytes, node: Node, name: str, parameters: List[ParameterDoc]
) -> str:
    parameter_list_text = node_text(
        source, node.child_by_field_name("parameters")
    )
    initializer = node.child_by_field_name("constructor_initializer")
    initializer_text = f" {node_text(source, initializer).strip()}" if initializer else ""
    modifiers = " ".join(collect_modifiers(source, node))
    modifiers_prefix = f"{modifiers} " if modifiers else ""
    return f"{modifiers_prefix}{name}{parameter_list_text}{initializer_text}"


def process_method(
    source: bytes,
    file_path: Path,
    typedoc: TypeDoc,
    node: Node,
    modifiers: List[str],
    doc_comment: dict,
) -> None:
    return_type_node = node.child_by_field_name("type")
    return_type = node_text(source, return_type_node) if return_type_node else "void"
    name = node_text(source, node.child_by_field_name("name"))
    type_params_node = node.child_by_field_name("type_parameters")
    type_params = node_text(source, type_params_node) if type_params_node else ""
    params_node = node.child_by_field_name("parameters")
    parameters = extract_parameters(source, params_node)
    constraints = [
        node_text(source, child)
        for child in node.children
        if child.type == "type_parameter_constraints_clause"
    ]
    modifiers_prefix = " ".join(modifiers)
    signature_parts = []
    if modifiers_prefix:
        signature_parts.append(modifiers_prefix)
    signature_parts.append(return_type)
    signature_parts.append(f"{name}{type_params}{node_text(source, params_node) if params_node else '()'}")
    if constraints:
        signature_parts.extend(constraints)
    signature = " ".join(part for part in signature_parts if part)

    member_doc = MemberDoc(
        name=name,
        kind="method",
        signature=signature,
        summary=doc_comment.get("summary"),
        remarks=doc_comment.get("remarks"),
        returns=doc_comment.get("returns"),
        parameters=merge_parameter_summaries(parameters, doc_comment),
        examples=doc_comment.get("examples", []),
        modifiers=modifiers,
        source=SourceLocation(file_path, node.start_point[0] + 1),
    )
    typedoc.add_member("methods", member_doc)


def process_property(
    source: bytes,
    file_path: Path,
    typedoc: TypeDoc,
    node: Node,
    modifiers: List[str],
    doc_comment: dict,
) -> None:
    type_node = node.child_by_field_name("type")
    name_node = node.child_by_field_name("name")
    if name_node is None:
        return
    type_text = node_text(source, type_node) if type_node else ""
    name_text = node_text(source, name_node)
    accessors = [
        node_text(source, child).strip()
        for child in node.children
        if child.type in {"accessor_list", "arrow_expression_clause"}
    ]
    modifiers_prefix = " ".join(modifiers)
    signature = " ".join(
        part
        for part in [
            modifiers_prefix if modifiers_prefix else "",
            type_text,
            name_text,
            *accessors,
        ]
        if part
    )
    member_doc = MemberDoc(
        name=name_text,
        kind="property",
        signature=signature,
        summary=doc_comment.get("summary"),
        remarks=doc_comment.get("remarks"),
        parameters=[],
        examples=doc_comment.get("examples", []),
        modifiers=modifiers,
        source=SourceLocation(file_path, node.start_point[0] + 1),
    )
    typedoc.add_member("properties", member_doc)


def process_indexer(
    source: bytes,
    file_path: Path,
    typedoc: TypeDoc,
    node: Node,
    modifiers: List[str],
    doc_comment: dict,
) -> None:
    type_node = node.child_by_field_name("type")
    params_node = node.child_by_field_name("parameters")
    type_text = node_text(source, type_node) if type_node else ""
    params_text = node_text(source, params_node) if params_node else "[]"
    signature = " ".join(
        part
        for part in [
            " ".join(modifiers) if modifiers else "",
            type_text,
            f"this{params_text}",
        ]
        if part
    )
    member_doc = MemberDoc(
        name="this",
        kind="indexer",
        signature=signature,
        summary=doc_comment.get("summary"),
        remarks=doc_comment.get("remarks"),
        parameters=merge_parameter_summaries(
            extract_parameters(source, params_node), doc_comment
        ),
        examples=doc_comment.get("examples", []),
        modifiers=modifiers,
        source=SourceLocation(file_path, node.start_point[0] + 1),
    )
    typedoc.add_member("indexers", member_doc)


def process_event(
    source: bytes,
    file_path: Path,
    typedoc: TypeDoc,
    node: Node,
    modifiers: List[str],
    doc_comment: dict,
) -> None:
    if node.type == "event_field_declaration":
        declaration = next(
            (child for child in node.children if child.type == "variable_declaration"),
            None,
        )
        if declaration is None:
            return
        type_text = node_text(source, declaration.child_by_field_name("type"))
        for variable in declaration.children:
            if variable.type != "variable_declarator":
                continue
            name = node_text(
                source, next(ch for ch in variable.children if ch.type == "identifier")
            )
            signature = " ".join(
                part
                for part in [
                    " ".join(modifiers) if modifiers else "",
                    "event",
                    type_text,
                    name,
                ]
                if part
            )
            member_doc = MemberDoc(
                name=name,
                kind="event",
                signature=signature,
                summary=doc_comment.get("summary"),
                remarks=doc_comment.get("remarks"),
                examples=doc_comment.get("examples", []),
                modifiers=modifiers,
                source=SourceLocation(file_path, node.start_point[0] + 1),
            )
            typedoc.add_member("events", member_doc)
    else:
        handler_type = ""
        name = ""
        for child in node.children:
            if child.type == "identifier" and not name:
                handler_type = node_text(source, child)
            elif child.type == "identifier":
                name = node_text(source, child)
        signature = " ".join(
            part
            for part in [
                " ".join(modifiers) if modifiers else "",
                "event",
                handler_type,
                name,
            ]
            if part
        )
        member_doc = MemberDoc(
            name=name,
            kind="event",
            signature=signature,
            summary=doc_comment.get("summary"),
            remarks=doc_comment.get("remarks"),
            examples=doc_comment.get("examples", []),
            modifiers=modifiers,
            source=SourceLocation(file_path, node.start_point[0] + 1),
        )
        typedoc.add_member("events", member_doc)


def process_field(
    source: bytes,
    file_path: Path,
    typedoc: TypeDoc,
    node: Node,
    modifiers: List[str],
    doc_comment: dict,
) -> None:
    declaration = next(
        (child for child in node.children if child.type == "variable_declaration"),
        None,
    )
    if declaration is None:
        return
    type_text = node_text(source, declaration.child_by_field_name("type"))
    for variable in declaration.children:
        if variable.type != "variable_declarator":
            continue
        identifier = next(
            (child for child in variable.children if child.type == "identifier"), None
        )
        if identifier is None:
            continue
        name = node_text(source, identifier)
        value_node = next(
            (child for child in variable.children if child.type == "equals_value_clause"),
            None,
        )
        value_text = ""
        if value_node:
            text = node_text(source, value_node)
            expr = text.split("=", 1)[1].strip() if "=" in text else text.strip()
            value_text = f" = {expr}"
        signature = " ".join(
            part
            for part in [
                " ".join(modifiers) if modifiers else "",
                type_text,
                f"{name}{value_text}",
            ]
            if part
        )
        member_doc = MemberDoc(
            name=name,
            kind="field",
            signature=signature,
            summary=doc_comment.get("summary"),
            remarks=doc_comment.get("remarks"),
            examples=doc_comment.get("examples", []),
            modifiers=modifiers,
            source=SourceLocation(file_path, node.start_point[0] + 1),
        )
        typedoc.add_member("fields", member_doc)


def process_operator(
    source: bytes,
    file_path: Path,
    typedoc: TypeDoc,
    node: Node,
    modifiers: List[str],
    doc_comment: dict,
) -> None:
    signature = node_text(source, node).split("{", 1)[0].strip()
    member_doc = MemberDoc(
        name=signature,
        kind="operator",
        signature=signature,
        summary=doc_comment.get("summary"),
        remarks=doc_comment.get("remarks"),
        returns=doc_comment.get("returns"),
        examples=doc_comment.get("examples", []),
        modifiers=modifiers,
        source=SourceLocation(file_path, node.start_point[0] + 1),
    )
    typedoc.add_member("operators", member_doc)


def process_enum_member(
    source: bytes,
    file_path: Path,
    typedoc: TypeDoc,
    node: Node,
) -> None:
    name_node = node.child_by_field_name("name")
    value_node = node.child_by_field_name("value")
    name = node_text(source, name_node) if name_node else ""
    value = node_text(source, value_node)[1:].strip() if value_node else None
    doc_comment = parse_xml_documentation(collect_leading_doc_comment(source, node))
    enum_value = EnumValueDoc(
        name=name,
        value=value,
        summary=doc_comment.get("summary"),
        source=SourceLocation(file_path, node.start_point[0] + 1),
    )
    typedoc.add_enum_value(enum_value)


# -----------------------------------------------------------------------------
# Documentation rendering
# -----------------------------------------------------------------------------


def generate_usage_example(typedoc: TypeDoc, member: Optional[MemberDoc] = None) -> Optional[str]:
    if member is None:
        if "static" in typedoc.modifiers:
            return textwrap.dedent(
                f"""
                ```csharp
                // Access {typedoc.full_name} members directly without instantiation.
                {typedoc.full_name}./* member */
                ```
                """
            ).strip()
        example_ctor = None
        constructors = typedoc.members.get("constructors", [])
        if constructors:
            example_ctor = constructors[0]
        if example_ctor:
            args = build_example_arguments(example_ctor.parameters)
            return textwrap.dedent(
                f"""
                ```csharp
                var instance = new {typedoc.full_name}({args});
                ```
                """
            ).strip()
        return textwrap.dedent(
            f"""
            ```csharp
            // Instantiate {typedoc.full_name} and call its members.
            var instance = new {typedoc.full_name}(/* arguments */);
            ```
            """
        ).strip()

    if member.kind == "method":
        args = build_example_arguments(member.parameters)
        target = (
            typedoc.full_name
            if "static" in member.modifiers or "static" in typedoc.modifiers
            else "instance"
        )
        invocation = (
            f"{typedoc.full_name}.{member.name}({args})"
            if target == typedoc.full_name
            else f"instance.{member.name}({args})"
        )
        return textwrap.dedent(
            f"""
            ```csharp
            // Example invocation
            {invocation};
            ```
            """
        ).strip()
    if member.kind == "property":
        target = (
            typedoc.full_name
            if "static" in member.modifiers or "static" in typedoc.modifiers
            else "instance"
        )
        access = (
            f"{typedoc.full_name}.{member.name}"
            if target == typedoc.full_name
            else f"instance.{member.name}"
        )
        return textwrap.dedent(
            f"""
            ```csharp
            // Read the property
            var value = {access};
            ```
            """
        ).strip()
    if member.kind == "event":
        target = (
            typedoc.full_name
            if "static" in member.modifiers or "static" in typedoc.modifiers
            else "instance"
        )
        access = (
            f"{typedoc.full_name}.{member.name}"
            if target == typedoc.full_name
            else f"instance.{member.name}"
        )
        return textwrap.dedent(
            f"""
            ```csharp
            // Subscribe to the event
            {access} += (sender, args) =>
            {{
                // TODO: handler logic
            }};
            ```
            """
        ).strip()
    if member.kind == "indexer":
        return textwrap.dedent(
            f"""
            ```csharp
            // Access via indexer
            var value = instance[/* index */];
            ```
            """
        ).strip()
    if member.kind == "field":
        target = (
            typedoc.full_name
            if "static" in member.modifiers or "static" in typedoc.modifiers
            else "instance"
        )
        access = (
            f"{typedoc.full_name}.{member.name}"
            if target == typedoc.full_name
            else f"instance.{member.name}"
        )
        return textwrap.dedent(
            f"""
            ```csharp
            var value = {access};
            ```
            """
        ).strip()
    return None


def build_example_arguments(parameters: List[ParameterDoc]) -> str:
    if not parameters:
        return ""
    args: List[str] = []
    for param in parameters:
        placeholder = f"{param.name}: /* {param.type or 'value'} */"
        args.append(placeholder)
    return ", ".join(args)


def render_markdown(types: dict[str, TypeDoc], output_dir: Path) -> None:
    namespaces: dict[str, List[TypeDoc]] = defaultdict(list)
    for typedoc in types.values():
        namespaces[typedoc.namespace].append(typedoc)

    for typedocs in namespaces.values():
        typedocs.sort(key=lambda t: t.full_name)

    output_dir.mkdir(parents=True, exist_ok=True)

    index_path = output_dir / "index.md"
    with index_path.open("w", encoding="utf-8") as index_file:
        index_file.write("# dnSpy Public API Documentation\n\n")
        index_file.write(
            "This documentation is generated automatically from the source code. "
            "Each namespace section links to a Markdown file describing all public "
            "types and members, incorporating existing XML documentation comments "
            "where available.\n\n"
        )
        for namespace in sorted(namespaces):
            filename = sanitize_filename(namespace) + ".md"
            relative = filename
            index_file.write(f"- [`{namespace}`]({relative})\n")

    for namespace, typedocs in sorted(namespaces.items()):
        filename = sanitize_filename(namespace) + ".md"
        namespace_path = output_dir / filename
        with namespace_path.open("w", encoding="utf-8") as f:
            f.write(f"# Namespace `{namespace}`\n\n")
            for typedoc in typedocs:
                render_type_section(f, typedoc)


def render_type_section(f, typedoc: TypeDoc) -> None:
    display_name = typedoc.name + (typedoc.type_parameters or "")
    f.write(f"## {typedoc.kind.title()} `{display_name}`\n\n")
    if typedoc.summary:
        f.write(f"{typedoc.summary}\n\n")
    if typedoc.base_types:
        f.write(
            "**Inherits/Implements:** "
            + ", ".join(f"`{base}`" for base in typedoc.base_types)
            + "\n\n"
        )
    if typedoc.remarks:
        f.write(f"{typedoc.remarks}\n\n")
    type_example = generate_usage_example(typedoc)
    if type_example:
        f.write("**Example**\n\n")
        f.write(f"{type_example}\n\n")
    if typedoc.sources:
        first_source = typedoc.sources[0]
        f.write(
            f"*Defined in* `{first_source.path.as_posix()}` (line {first_source.line})\n\n"
        )

    sections_order = [
        ("constructors", "Constructors"),
        ("methods", "Methods"),
        ("properties", "Properties"),
        ("indexers", "Indexers"),
        ("fields", "Fields"),
        ("events", "Events"),
        ("operators", "Operators"),
    ]

    for key, heading in sections_order:
        members = typedoc.members.get(key)
        if not members:
            continue
        f.write(f"### {heading}\n\n")
        for member in sorted(members, key=lambda m: m.signature):
            render_member(f, typedoc, member)
        f.write("\n")

    if typedoc.enum_values:
        f.write("### Members\n\n")
        for value in typedoc.enum_values:
            f.write(f"- `{value.name}`")
            if value.value:
                f.write(f" = `{value.value}`")
            if value.summary:
                f.write(f": {value.summary}")
            f.write("\n")
        f.write("\n")


def render_member(f, typedoc: TypeDoc, member: MemberDoc) -> None:
    f.write(f"- `{member.signature}`\n")
    if member.summary:
        f.write(f"  - Summary: {member.summary}\n")
    if member.parameters:
        f.write("  - Parameters:\n")
        for param in member.parameters:
            param_desc = param.summary or "Description not provided."
            modifiers = " ".join(param.modifiers) + " " if param.modifiers else ""
            default = f" (default: `{param.default}`)" if param.default else ""
            f.write(
                f"    - `{modifiers}{param.type} {param.name}`{default}: {param_desc}\n"
            )
    if member.returns:
        f.write(f"  - Returns: {member.returns}\n")
    if member.source:
        f.write(
            f"  - Defined in: `{member.source.path.as_posix()}` (line {member.source.line})\n"
        )
    if member.examples:
        for example in member.examples:
            f.write("  - Example:\n")
            indented = textwrap.indent(example.strip(), "    ")
            f.write(f"{indented}\n")
    else:
        generated = generate_usage_example(typedoc, member)
        if generated:
            f.write("  - Example:\n")
            indented = textwrap.indent(generated, "    ")
            f.write(f"{indented}\n")


# -----------------------------------------------------------------------------
# Entry point
# -----------------------------------------------------------------------------


def collect_source_files(root: Path) -> List[Path]:
    ignore_dirs = {
        ".git",
        ".vs",
        "bin",
        "obj",
        "packages",
        "__pycache__",
        "Build/compiled",
    }
    cs_files: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        rel_parts = Path(dirpath).relative_to(root).parts
        if any(part in ignore_dirs for part in rel_parts):
            continue
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for filename in filenames:
            if filename.endswith(".cs"):
                cs_files.append(Path(dirpath) / filename)
    return cs_files


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Markdown documentation for the dnSpy public API."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Repository root containing C# sources.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "docs" / "api",
        help="Destination folder for generated Markdown files.",
    )
    args = parser.parse_args()

    root = args.root
    output_dir = args.output

    cs_files = collect_source_files(root)
    if not cs_files:
        print("No C# source files found.", file=sys.stderr)
        return 1

    parser_instance = get_parser("c_sharp")
    types: dict[str, TypeDoc] = {}

    for path in cs_files:
        try:
            source = path.read_bytes()
        except Exception as exc:  # pragma: no cover - filesystem errors
            print(f"Skipping {path}: {exc}", file=sys.stderr)
            continue
        tree = parser_instance.parse(source)
        extract_public_api(
            parser_instance,
            source,
            path.relative_to(root),
            "",
            tree.root_node,
            types,
        )

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    render_markdown(types, output_dir)

    print(f"Generated documentation for {len(types)} public types at {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

