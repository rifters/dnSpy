# Namespace `dnSpy.Contracts.Search`

## Class `ChainDocumentTreeNodeFilter`

Chain filter

**Inherits/Implements:** `IDocumentTreeNodeFilter`

**Example**

```csharp
var instance = new dnSpy.Contracts.Search.ChainDocumentTreeNodeFilter(filter: /* IDocumentTreeNodeFilter */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 30)

### Constructors

- `public ChainDocumentTreeNodeFilter(IDocumentTreeNodeFilter filter)`
  - Summary: Constructor
  - Parameters:
    - `IDocumentTreeNodeFilter filter`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 37)

### Methods

- `public virtual DocumentTreeNodeFilterResult GetResult(AssemblyDef asm)`
  - Parameters:
    - `AssemblyDef asm`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asm: /* AssemblyDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(AssemblyRef asmRef)`
  - Parameters:
    - `AssemblyRef asmRef`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asmRef: /* AssemblyRef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(BaseTypeFolderNode node)`
  - Parameters:
    - `BaseTypeFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* BaseTypeFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(BaseTypeNode node)`
  - Parameters:
    - `BaseTypeNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* BaseTypeNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(DerivedTypeNode node)`
  - Parameters:
    - `DerivedTypeNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* DerivedTypeNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(DerivedTypesFolderNode node)`
  - Parameters:
    - `DerivedTypesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* DerivedTypesFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(EventDef evt)`
  - Parameters:
    - `EventDef evt`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(evt: /* EventDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(FieldDef field)`
  - Parameters:
    - `FieldDef field`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(field: /* FieldDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(IDsDocument document)`
  - Parameters:
    - `IDsDocument document`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(document: /* IDsDocument */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(MethodDef method, Local local)`
  - Parameters:
    - `MethodDef method`: Description not provided.
    - `Local local`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */, local: /* Local */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(MethodDef method, ParamDef param)`
  - Parameters:
    - `MethodDef method`: Description not provided.
    - `ParamDef param`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */, param: /* ParamDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ModuleDef mod)`
  - Parameters:
    - `ModuleDef mod`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(mod: /* ModuleDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ModuleRef modRef)`
  - Parameters:
    - `ModuleRef modRef`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(modRef: /* ModuleRef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(PropertyDef prop)`
  - Parameters:
    - `PropertyDef prop`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(prop: /* PropertyDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ReferencesFolderNode node)`
  - Parameters:
    - `ReferencesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ReferencesFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ResourceElementNode node)`
  - Parameters:
    - `ResourceElementNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourceElementNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ResourceNode node)`
  - Parameters:
    - `ResourceNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourceNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ResourcesFolderNode node)`
  - Parameters:
    - `ResourcesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourcesFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(TypeDef type)`
  - Parameters:
    - `TypeDef type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(type: /* TypeDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(string ns, IDsDocument owner)`
  - Parameters:
    - `string ns`: Description not provided.
    - `IDsDocument owner`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(ns: /* string */, owner: /* IDsDocument */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultAttributes(IHasCustomAttribute hca)`
  - Parameters:
    - `IHasCustomAttribute hca`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultAttributes(hca: /* IHasCustomAttribute */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultBody(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultBody(method: /* MethodDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultLocals(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultLocals(method: /* MethodDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultOther(DocumentTreeNodeData node)`
  - Parameters:
    - `DocumentTreeNodeData node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultOther(node: /* DocumentTreeNodeData */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultParamDefs(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ChainDocumentTreeNodeFilter.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultParamDefs(method: /* MethodDef */);
    ```

## Class `DocumentTreeNodeFilterBase`

Filter base class

**Inherits/Implements:** `IDocumentTreeNodeFilter`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Search.DocumentTreeNodeFilterBase and call its members.
var instance = new dnSpy.Contracts.Search.DocumentTreeNodeFilterBase(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 30)

### Methods

- `public virtual DocumentTreeNodeFilterResult GetResult(AssemblyDef asm)`
  - Parameters:
    - `AssemblyDef asm`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asm: /* AssemblyDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(AssemblyRef asmRef)`
  - Parameters:
    - `AssemblyRef asmRef`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asmRef: /* AssemblyRef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(BaseTypeFolderNode node)`
  - Parameters:
    - `BaseTypeFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* BaseTypeFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(BaseTypeNode node)`
  - Parameters:
    - `BaseTypeNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* BaseTypeNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(DerivedTypeNode node)`
  - Parameters:
    - `DerivedTypeNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* DerivedTypeNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(DerivedTypesFolderNode node)`
  - Parameters:
    - `DerivedTypesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* DerivedTypesFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(EventDef evt)`
  - Parameters:
    - `EventDef evt`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(evt: /* EventDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(FieldDef field)`
  - Parameters:
    - `FieldDef field`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(field: /* FieldDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(IDsDocument document)`
  - Parameters:
    - `IDsDocument document`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(document: /* IDsDocument */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(MethodDef method, Local local)`
  - Parameters:
    - `MethodDef method`: Description not provided.
    - `Local local`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */, local: /* Local */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(MethodDef method, ParamDef param)`
  - Parameters:
    - `MethodDef method`: Description not provided.
    - `ParamDef param`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */, param: /* ParamDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ModuleDef mod)`
  - Parameters:
    - `ModuleDef mod`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(mod: /* ModuleDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ModuleRef modRef)`
  - Parameters:
    - `ModuleRef modRef`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(modRef: /* ModuleRef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(PropertyDef prop)`
  - Parameters:
    - `PropertyDef prop`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(prop: /* PropertyDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ReferencesFolderNode node)`
  - Parameters:
    - `ReferencesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ReferencesFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ResourceElementNode node)`
  - Parameters:
    - `ResourceElementNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourceElementNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ResourceNode node)`
  - Parameters:
    - `ResourceNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourceNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ResourcesFolderNode node)`
  - Parameters:
    - `ResourcesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourcesFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(TypeDef type)`
  - Parameters:
    - `TypeDef type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(type: /* TypeDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(string ns, IDsDocument owner)`
  - Parameters:
    - `string ns`: Description not provided.
    - `IDsDocument owner`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(ns: /* string */, owner: /* IDsDocument */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultAttributes(IHasCustomAttribute hca)`
  - Parameters:
    - `IHasCustomAttribute hca`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultAttributes(hca: /* IHasCustomAttribute */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultBody(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultBody(method: /* MethodDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultLocals(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultLocals(method: /* MethodDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultOther(DocumentTreeNodeData node)`
  - Parameters:
    - `DocumentTreeNodeData node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultOther(node: /* DocumentTreeNodeData */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultParamDefs(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/DocumentTreeNodeFilterBase.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultParamDefs(method: /* MethodDef */);
    ```

## Class `EntryPointDocumentTreeNodeFilter`

Entry point filter

**Inherits/Implements:** `ShowNothingDocumentTreeNodeFilterBase`

**Example**

```csharp
var instance = new dnSpy.Contracts.Search.EntryPointDocumentTreeNodeFilter(module: /* ModuleDef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Search/EntryPointDocumentTreeNodeFilter.cs` (line 28)

### Constructors

- `public EntryPointDocumentTreeNodeFilter(ModuleDef module)`
  - Summary: Constructor
  - Parameters:
    - `ModuleDef module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/EntryPointDocumentTreeNodeFilter.cs` (line 36)

### Methods

- `public override DocumentTreeNodeFilterResult GetResult(AssemblyDef asm)`
  - Parameters:
    - `AssemblyDef asm`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/EntryPointDocumentTreeNodeFilter.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asm: /* AssemblyDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(EventDef evt)`
  - Parameters:
    - `EventDef evt`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/EntryPointDocumentTreeNodeFilter.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(evt: /* EventDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/EntryPointDocumentTreeNodeFilter.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(ModuleDef mod)`
  - Parameters:
    - `ModuleDef mod`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/EntryPointDocumentTreeNodeFilter.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(mod: /* ModuleDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(PropertyDef prop)`
  - Parameters:
    - `PropertyDef prop`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/EntryPointDocumentTreeNodeFilter.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(prop: /* PropertyDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(TypeDef type)`
  - Parameters:
    - `TypeDef type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/EntryPointDocumentTreeNodeFilter.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(type: /* TypeDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(string ns, IDsDocument owner)`
  - Parameters:
    - `string ns`: Description not provided.
    - `IDsDocument owner`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/EntryPointDocumentTreeNodeFilter.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(ns: /* string */, owner: /* IDsDocument */);
    ```

## Class `FilterNothingDocumentTreeNodeFilter`

Filter nothing base class

**Inherits/Implements:** `DocumentTreeNodeFilterBase`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Search.FilterNothingDocumentTreeNodeFilter and call its members.
var instance = new dnSpy.Contracts.Search.FilterNothingDocumentTreeNodeFilter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Search/FilterNothingDocumentTreeNodeFilter.cs` (line 24)

### Fields

- `public static readonly FilterNothingDocumentTreeNodeFilter Instance = new FilterNothingDocumentTreeNodeFilter()`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FilterNothingDocumentTreeNodeFilter.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Search.FilterNothingDocumentTreeNodeFilter.Instance;
    ```

## Class `FlagsDocumentTreeNodeFilter`

Filters nodes

**Inherits/Implements:** `DocumentTreeNodeFilterBase`

**Example**

```csharp
var instance = new dnSpy.Contracts.Search.FlagsDocumentTreeNodeFilter(flags: /* VisibleMembersFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 31)

### Constructors

- `public FlagsDocumentTreeNodeFilter(VisibleMembersFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `VisibleMembersFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 38)

### Methods

- `public override DocumentTreeNodeFilterResult GetResult(AssemblyDef asm)`
  - Parameters:
    - `AssemblyDef asm`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asm: /* AssemblyDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(AssemblyRef asmRef)`
  - Parameters:
    - `AssemblyRef asmRef`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asmRef: /* AssemblyRef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(BaseTypeFolderNode node)`
  - Parameters:
    - `BaseTypeFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* BaseTypeFolderNode */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(DerivedTypesFolderNode node)`
  - Parameters:
    - `DerivedTypesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* DerivedTypesFolderNode */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(EventDef evt)`
  - Parameters:
    - `EventDef evt`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(evt: /* EventDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(FieldDef field)`
  - Parameters:
    - `FieldDef field`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(field: /* FieldDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(IDsDocument document)`
  - Parameters:
    - `IDsDocument document`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(document: /* IDsDocument */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 136)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(MethodDef method, Local local)`
  - Parameters:
    - `MethodDef method`: Description not provided.
    - `Local local`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 348)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */, local: /* Local */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(MethodDef method, ParamDef param)`
  - Parameters:
    - `MethodDef method`: Description not provided.
    - `ParamDef param`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 328)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */, param: /* ParamDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(ModuleDef mod)`
  - Parameters:
    - `ModuleDef mod`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(mod: /* ModuleDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(ModuleRef modRef)`
  - Parameters:
    - `ModuleRef modRef`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 152)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(modRef: /* ModuleRef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(PropertyDef prop)`
  - Parameters:
    - `PropertyDef prop`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 176)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(prop: /* PropertyDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(ReferencesFolderNode node)`
  - Parameters:
    - `ReferencesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 189)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ReferencesFolderNode */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(ResourceElementNode node)`
  - Parameters:
    - `ResourceElementNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 219)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourceElementNode */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(ResourceNode node)`
  - Parameters:
    - `ResourceNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 208)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourceNode */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(ResourcesFolderNode node)`
  - Parameters:
    - `ResourcesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 197)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourcesFolderNode */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(TypeDef type)`
  - Parameters:
    - `TypeDef type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 233)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(type: /* TypeDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(string ns, IDsDocument owner)`
  - Parameters:
    - `string ns`: Description not provided.
    - `IDsDocument owner`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 159)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(ns: /* string */, owner: /* IDsDocument */);
    ```
- `public override DocumentTreeNodeFilterResult GetResultAttributes(IHasCustomAttribute hca)`
  - Parameters:
    - `IHasCustomAttribute hca`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 355)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultAttributes(hca: /* IHasCustomAttribute */);
    ```
- `public override DocumentTreeNodeFilterResult GetResultBody(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 310)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultBody(method: /* MethodDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResultLocals(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 338)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultLocals(method: /* MethodDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResultOther(DocumentTreeNodeData node)`
  - Parameters:
    - `DocumentTreeNodeData node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 226)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultOther(node: /* DocumentTreeNodeData */);
    ```
- `public override DocumentTreeNodeFilterResult GetResultParamDefs(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/FlagsDocumentTreeNodeFilter.cs` (line 317)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultParamDefs(method: /* MethodDef */);
    ```

## Interface `ISearchResultReferenceProvider`

Provides a reference

**Example**

```csharp
// Instantiate dnSpy.Contracts.Search.ISearchResultReferenceProvider and call its members.
var instance = new dnSpy.Contracts.Search.ISearchResultReferenceProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Search/ISearchResult.cs` (line 29)

### Properties

- `object Reference { get; }`
  - Summary: Gets the reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ISearchResult.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reference;
    ```

## Class `SameAssemblyDocumentTreeNodeFilter`

Same assembly filter

**Inherits/Implements:** `ChainDocumentTreeNodeFilter`

**Example**

```csharp
var instance = new dnSpy.Contracts.Search.SameAssemblyDocumentTreeNodeFilter(allowedMod: /* ModuleDef */, filter: /* IDocumentTreeNodeFilter */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Search/SameAssemblyDocumentTreeNodeFilter.cs` (line 27)

### Constructors

- `public SameAssemblyDocumentTreeNodeFilter(ModuleDef allowedMod, IDocumentTreeNodeFilter filter)`
  - Summary: Constructor
  - Parameters:
    - `ModuleDef allowedMod`: Module
    - `IDocumentTreeNodeFilter filter`: Filter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/SameAssemblyDocumentTreeNodeFilter.cs` (line 36)

### Methods

- `public override DocumentTreeNodeFilterResult GetResult(AssemblyDef asm)`
  - Parameters:
    - `AssemblyDef asm`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/SameAssemblyDocumentTreeNodeFilter.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asm: /* AssemblyDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(ModuleDef mod)`
  - Parameters:
    - `ModuleDef mod`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/SameAssemblyDocumentTreeNodeFilter.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(mod: /* ModuleDef */);
    ```

## Class `SameModuleDocumentTreeNodeFilter`

Same module filter

**Inherits/Implements:** `ChainDocumentTreeNodeFilter`

**Example**

```csharp
var instance = new dnSpy.Contracts.Search.SameModuleDocumentTreeNodeFilter(allowedModule: /* ModuleDef */, filter: /* IDocumentTreeNodeFilter */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Search/SameModuleDocumentTreeNodeFilter.cs` (line 27)

### Constructors

- `public SameModuleDocumentTreeNodeFilter(ModuleDef allowedModule, IDocumentTreeNodeFilter filter)`
  - Summary: Constructor
  - Parameters:
    - `ModuleDef allowedModule`: Module
    - `IDocumentTreeNodeFilter filter`: Filter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/SameModuleDocumentTreeNodeFilter.cs` (line 35)

### Methods

- `public override DocumentTreeNodeFilterResult GetResult(AssemblyDef asm)`
  - Parameters:
    - `AssemblyDef asm`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/SameModuleDocumentTreeNodeFilter.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asm: /* AssemblyDef */);
    ```
- `public override DocumentTreeNodeFilterResult GetResult(ModuleDef mod)`
  - Parameters:
    - `ModuleDef mod`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/SameModuleDocumentTreeNodeFilter.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(mod: /* ModuleDef */);
    ```

## Class `ShowNothingDocumentTreeNodeFilterBase`

Show nothing filter base class

**Inherits/Implements:** `IDocumentTreeNodeFilter`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Search.ShowNothingDocumentTreeNodeFilterBase and call its members.
var instance = new dnSpy.Contracts.Search.ShowNothingDocumentTreeNodeFilterBase(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 30)

### Methods

- `public virtual DocumentTreeNodeFilterResult GetResult(AssemblyDef asm)`
  - Parameters:
    - `AssemblyDef asm`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asm: /* AssemblyDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(AssemblyRef asmRef)`
  - Parameters:
    - `AssemblyRef asmRef`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asmRef: /* AssemblyRef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(BaseTypeFolderNode node)`
  - Parameters:
    - `BaseTypeFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* BaseTypeFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(BaseTypeNode node)`
  - Parameters:
    - `BaseTypeNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* BaseTypeNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(DerivedTypeNode node)`
  - Parameters:
    - `DerivedTypeNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* DerivedTypeNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(DerivedTypesFolderNode node)`
  - Parameters:
    - `DerivedTypesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* DerivedTypesFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(EventDef evt)`
  - Parameters:
    - `EventDef evt`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(evt: /* EventDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(FieldDef field)`
  - Parameters:
    - `FieldDef field`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(field: /* FieldDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(IDsDocument document)`
  - Parameters:
    - `IDsDocument document`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(document: /* IDsDocument */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(MethodDef method, Local local)`
  - Parameters:
    - `MethodDef method`: Description not provided.
    - `Local local`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */, local: /* Local */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(MethodDef method, ParamDef param)`
  - Parameters:
    - `MethodDef method`: Description not provided.
    - `ParamDef param`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */, param: /* ParamDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ModuleDef mod)`
  - Parameters:
    - `ModuleDef mod`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(mod: /* ModuleDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ModuleRef modRef)`
  - Parameters:
    - `ModuleRef modRef`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(modRef: /* ModuleRef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(PropertyDef prop)`
  - Parameters:
    - `PropertyDef prop`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(prop: /* PropertyDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ReferencesFolderNode node)`
  - Parameters:
    - `ReferencesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ReferencesFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ResourceElementNode node)`
  - Parameters:
    - `ResourceElementNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourceElementNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ResourceNode node)`
  - Parameters:
    - `ResourceNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourceNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(ResourcesFolderNode node)`
  - Parameters:
    - `ResourcesFolderNode node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourcesFolderNode */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(TypeDef type)`
  - Parameters:
    - `TypeDef type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(type: /* TypeDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResult(string ns, IDsDocument owner)`
  - Parameters:
    - `string ns`: Description not provided.
    - `IDsDocument owner`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(ns: /* string */, owner: /* IDsDocument */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultAttributes(IHasCustomAttribute hca)`
  - Parameters:
    - `IHasCustomAttribute hca`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultAttributes(hca: /* IHasCustomAttribute */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultBody(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultBody(method: /* MethodDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultLocals(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultLocals(method: /* MethodDef */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultOther(DocumentTreeNodeData node)`
  - Parameters:
    - `DocumentTreeNodeData node`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultOther(node: /* DocumentTreeNodeData */);
    ```
- `public virtual DocumentTreeNodeFilterResult GetResultParamDefs(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Search/ShowNothingDocumentTreeNodeFilterBase.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultParamDefs(method: /* MethodDef */);
    ```

## Enum `VisibleMembersFlags`

Filter flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Search.VisibleMembersFlags and call its members.
var instance = new dnSpy.Contracts.Search.VisibleMembersFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Search/VisibleMembersFlags.cs` (line 26)

### Members

- `AssemblyDef` = `x00000001`
- `ModuleDef` = `x00000002`
- `Namespace` = `x00000004`
- `TypeDef` = `x00000008`
- `FieldDef` = `x00000010`
- `MethodDef` = `x00000020`
- `PropertyDef` = `x00000040`
- `EventDef` = `x00000080`
- `AssemblyRef` = `x00000100`
- `BaseTypes` = `x00000200`
- `DerivedTypes` = `x00000400`
- `ModuleRef` = `x00000800`
- `ResourceList` = `x00001000`
- `NonNetFile` = `x00002000`
- `GenericTypeDef` = `x00004000`
- `NonGenericTypeDef` = `x00008000`
- `EnumTypeDef` = `x00010000`
- `InterfaceTypeDef` = `x00020000`
- `ClassTypeDef` = `x00040000`
- `StructTypeDef` = `x00080000`
- `DelegateTypeDef` = `x00100000`
- `MethodBody` = `x00200000`
- `InstanceConstructor` = `x00400000`
- `ParamDefs` = `x00800000`
- `ParamDef` = `x01000000`
- `Locals` = `x02000000`
- `Local` = `x04000000`
- `Resource` = `x08000000`
- `ResourceElement` = `x10000000`
- `Other` = `x20000000`
- `Attributes` = `x40000000`
- `TypeDefOther` = `enericTypeDef | NonGenericTypeDef | EnumTypeDef | InterfaceTypeDef | ClassTypeDef | StructTypeDef | DelegateTypeDef`
- `AnyTypeDef` = `ypeDef | TypeDefOther`
- `TreeViewAll` = `ssemblyDef | ModuleDef | Namespace | TypeDef |
						  FieldDef | MethodDef | PropertyDef | EventDef |
						  AssemblyRef | BaseTypes | DerivedTypes | ModuleRef |
						  ResourceList | NonNetFile | Resource | ResourceElement |
						  Other`

