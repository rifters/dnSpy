# Namespace `dnSpy.Contracts.Documents.TreeView`

## Class `AssemblyDocumentNode`

A .NET assembly file

**Inherits/Implements:** `DsDocumentNode`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.AssemblyDocumentNode(document: /* IDsDotNetDocument */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/AssemblyDocumentNode.cs` (line 28)

### Constructors

- `protected AssemblyDocumentNode(IDsDotNetDocument document)`
  - Summary: Constructor
  - Parameters:
    - `IDsDotNetDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/AssemblyDocumentNode.cs` (line 45)

### Properties

- `public bool IsExe => (Document.ModuleDef.Characteristics & Characteristics.Dll) == 0`
  - Summary: true if it's an .exe file, false if it's a .dll or .netmodule
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/AssemblyDocumentNode.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsExe;
    ```
- `public new IDsDotNetDocument Document => (IDsDotNetDocument)base.Document`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/AssemblyDocumentNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Document;
    ```

## Class `AssemblyReferenceNode`

An assembly reference node

**Inherits/Implements:** `DocumentTreeNodeData`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.AssemblyReferenceNode();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/AssemblyReferenceNode.cs` (line 27)

### Constructors

- `protected AssemblyReferenceNode()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/AssemblyReferenceNode.cs` (line 36)

### Properties

- `public abstract AssemblyRef AssemblyRef { get; }`
  - Summary: Gets the assembly reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/AssemblyReferenceNode.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyRef;
    ```

## Class `BaseTypeFolderNode`

Contains the base type (if any) and all interfaces the type implements

**Inherits/Implements:** `DocumentTreeNodeData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.BaseTypeFolderNode();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/BaseTypeFolderNode.cs` (line 24)

### Constructors

- `protected BaseTypeFolderNode()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/BaseTypeFolderNode.cs` (line 28)

### Methods

- `public abstract void InvalidateChildren()`
  - Summary: Invalidates all children
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/BaseTypeFolderNode.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.InvalidateChildren();
    ```

## Class `BaseTypeNode`

A base type or implemented interface node

**Inherits/Implements:** `DocumentTreeNodeData`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.BaseTypeNode();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/BaseTypeNode.cs` (line 27)

### Constructors

- `protected BaseTypeNode()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/BaseTypeNode.cs` (line 38)

### Properties

- `public abstract ITypeDefOrRef TypeDefOrRef { get; }`
  - Summary: Gets the type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/BaseTypeNode.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeDefOrRef;
    ```

## Class `DerivedTypeNode`

A derived type

**Inherits/Implements:** `DocumentTreeNodeData`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.DerivedTypeNode();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DerivedTypeNode.cs` (line 27)

### Constructors

- `protected DerivedTypeNode()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DerivedTypeNode.cs` (line 38)

### Properties

- `public abstract TypeDef TypeDef { get; }`
  - Summary: Gets the type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DerivedTypeNode.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeDef;
    ```

## Class `DerivedTypesFolderNode`

Contains all derived types

**Inherits/Implements:** `DocumentTreeNodeData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.DerivedTypesFolderNode();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DerivedTypesFolderNode.cs` (line 24)

### Constructors

- `protected DerivedTypesFolderNode()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DerivedTypesFolderNode.cs` (line 28)

## Enum `DocumentFilterType`

Filter dragged documents to treeview

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.DocumentFilterType and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.DocumentFilterType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentFilterType.cs` (line 24)

### Members

- `All`: All
- `AllSupported`: Imports only supported files
- `DotNetOnly`: .NET only files

## Enum `DocumentNodeWriteOptions`

Options used when writing nodes

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.DocumentNodeWriteOptions and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.DocumentNodeWriteOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentNodeWriteOptions.cs` (line 26)

### Members

- `None`: No bit is set
- `Title` = `x00000001`: The text will be shown in a tab. Less important information such as metadata tokens should normally not be written.
- `ToolTip` = `x00000002`: The text will be shown in a tooltip

## Class `DocumentTreeNodeActivatedEventArgs`

activated event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeActivatedEventArgs(node: /* DocumentTreeNodeData */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeActivatedEventArgs.cs` (line 26)

### Constructors

- `public DocumentTreeNodeActivatedEventArgs(DocumentTreeNodeData node)`
  - Summary: Constructor
  - Parameters:
    - `DocumentTreeNodeData node`: Node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeActivatedEventArgs.cs` (line 41)

### Properties

- `public DocumentTreeNodeData Node { get; }`
  - Summary: Activated node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeActivatedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Node;
    ```
- `public bool Handled { get; set; }`
  - Summary: Set it to true if the event was handled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeActivatedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Handled;
    ```

## Class `DocumentTreeNodeData`

Document treenode data base class

**Inherits/Implements:** `TreeNodeData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeData();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 38)

### Constructors

- `protected DocumentTreeNodeData()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 166)

### Methods

- `protected abstract ImageReference GetIcon(IDotNetImageService dnImgMgr)`
  - Summary: Gets the icon
  - Parameters:
    - `IDotNetImageService dnImgMgr`: Image service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon(dnImgMgr: /* IDotNetImageService */);
    ```
- `protected abstract void WriteCore(ITextColorWriter output, IDecompiler decompiler, DocumentNodeWriteOptions options)`
  - Summary: Writes the contents
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `DocumentNodeWriteOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteCore(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, options: /* DocumentNodeWriteOptions */);
    ```
- `protected bool GetShowToken(DocumentNodeWriteOptions options)`
  - Summary: Returns true if should show tokens
  - Parameters:
    - `DocumentNodeWriteOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.GetShowToken(options: /* DocumentNodeWriteOptions */);
    ```
- `protected virtual ImageReference? GetExpandedIcon(IDotNetImageService dnImgMgr)`
  - Summary: Gets the icon shown when the node has been expanded
  - Parameters:
    - `IDotNetImageService dnImgMgr`: Image service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.GetExpandedIcon(dnImgMgr: /* IDotNetImageService */);
    ```
- `public override bool Activate()`
  - Summary: Called when the item gets activated, eg. double clicked. Returns true if it was handled, false otherwise.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 179)
  - Example:
    ```csharp
    // Example invocation
    instance.Activate();
    ```
- `public sealed override IDataObject Copy(TreeNodeData[] nodes)`
  - Summary: Copies nodes
  - Parameters:
    - `TreeNodeData[] nodes`: Nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 323)
  - Example:
    ```csharp
    // Example invocation
    instance.Copy(nodes: /* TreeNodeData[] */);
    ```
- `public sealed override bool CanDrag(TreeNodeData[] nodes)`
  - Summary: Returns true if the nodes can be dragged
  - Parameters:
    - `TreeNodeData[] nodes`: Nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 296)
  - Example:
    ```csharp
    // Example invocation
    instance.CanDrag(nodes: /* TreeNodeData[] */);
    ```
- `public sealed override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 141)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public sealed override void OnChildrenChanged(TreeNodeData[] added, TreeNodeData[] removed)`
  - Summary: Called when the children has changed
  - Parameters:
    - `TreeNodeData[] added`: Added nodes
    - `TreeNodeData[] removed`: Removed nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 250)
  - Example:
    ```csharp
    // Example invocation
    instance.OnChildrenChanged(added: /* TreeNodeData[] */, removed: /* TreeNodeData[] */);
    ```
- `public sealed override void OnEnsureChildrenLoaded()`
  - Summary: Called by
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 191)
  - Example:
    ```csharp
    // Example invocation
    instance.OnEnsureChildrenLoaded();
    ```
- `public sealed override void OnIsVisibleChanged()`
  - Summary: Called when has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 273)
  - Example:
    ```csharp
    // Example invocation
    instance.OnIsVisibleChanged();
    ```
- `public sealed override void OnRefreshUI()`
  - Summary: Called by before it invalidates all UI properties
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 172)
  - Example:
    ```csharp
    // Example invocation
    instance.OnRefreshUI();
    ```
- `public sealed override void StartDrag(DependencyObject dragSource, TreeNodeData[] nodes)`
  - Summary: Starts the drag and drop operation
  - Parameters:
    - `DependencyObject dragSource`: Drag source
    - `TreeNodeData[] nodes`: Nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 306)
  - Example:
    ```csharp
    // Example invocation
    instance.StartDrag(dragSource: /* DependencyObject */, nodes: /* TreeNodeData[] */);
    ```
- `public string ToString(DocumentNodeWriteOptions options = DocumentNodeWriteOptions.None)`
  - Summary: ToString()
  - Parameters:
    - `DocumentNodeWriteOptions options` (default: `DocumentNodeWriteOptions.None`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 148)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString(options: /* DocumentNodeWriteOptions */);
    ```
- `public string ToString(IDecompiler decompiler, DocumentNodeWriteOptions options = DocumentNodeWriteOptions.None)`
  - Summary: ToString()
  - Parameters:
    - `IDecompiler decompiler`: Decompiler
    - `DocumentNodeWriteOptions options` (default: `DocumentNodeWriteOptions.None`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString(decompiler: /* IDecompiler */, options: /* DocumentNodeWriteOptions */);
    ```
- `public virtual FilterType GetFilterType(IDocumentTreeNodeFilter filter)`
  - Summary: Gets the to filter this instance
  - Parameters:
    - `IDocumentTreeNodeFilter filter`: Filter to call
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 186)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFilterType(filter: /* IDocumentTreeNodeFilter */);
    ```
- `public void Refilter()`
  - Summary: Called when has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 281)
  - Example:
    ```csharp
    // Example invocation
    instance.Refilter();
    ```

### Properties

- `public IDocumentTreeNodeDataContext Context { get; set; }`
  - Summary: Gets the context. Should only be set by the owner
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Context;
    ```
- `public abstract NodePathName NodePathName { get; }`
  - Summary: Gets the node path name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NodePathName;
    ```
- `public int FilterVersion {
			get => filterVersion;
			set {
				if (filterVersion != value) {
					filterVersion = value;
					Refilter();
				}
			}
		}`
  - Summary: The class () should call when updating this value.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 204)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FilterVersion;
    ```
- `public override bool SingleClickExpandsChildren => Context.SingleClickExpandsChildren`
  - Summary: true if single clicking on a node expands all its children
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SingleClickExpandsChildren;
    ```
- `public sealed override ImageReference Icon => GetIcon(Context.DocumentTreeView.DotNetImageService)`
  - Summary: Icon
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Icon;
    ```
- `public sealed override ImageReference? ExpandedIcon => GetExpandedIcon(Context.DocumentTreeView.DotNetImageService)`
  - Summary: Expanded icon or null to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExpandedIcon;
    ```
- `public sealed override object Text {
			get {
				var cached = cachedText?.Target;
				if (cached != null)
					return cached;

				var writer = Cache.GetWriter();
				try {
					WriteCore(writer, Context.Decompiler, DocumentNodeWriteOptions.None);
					var classifierContext = new TreeViewNodeClassifierContext(writer.Text, Context.DocumentTreeView.TreeView, this, isToolTip: false, colorize: Context.SyntaxHighlight, colors: writer.Colors);
					var elem = Context.TreeViewNodeTextElementProvider.CreateTextElement(classifierContext, TreeViewContentTypes.TreeViewNodeAssemblyExplorer, TextElementFlags.FilterOutNewLines | (Context.UseNewRenderer ? TextElementFlags.NewFormatter : 0));
					cachedText = new WeakReference(elem);
					return elem;
				}
				finally {
					Cache.FreeWriter(writer);
				}
			}
		}`
  - Summary: Gets the data shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```
- `public sealed override object ToolTip {
			get {
				var writer = Cache.GetWriter();
				WriteCore(writer, Context.Decompiler, DocumentNodeWriteOptions.ToolTip);
				var classifierContext = new TreeViewNodeClassifierContext(writer.Text, Context.DocumentTreeView.TreeView, this, isToolTip: true, colorize: Context.SyntaxHighlight, colors: writer.Colors);
				var elem = Context.TreeViewNodeTextElementProvider.CreateTextElement(classifierContext, TreeViewContentTypes.TreeViewNodeAssemblyExplorer, Context.UseNewRenderer ? TextElementFlags.NewFormatter : 0);
				Cache.FreeWriter(writer);
				return elem;
			}
		}`
  - Summary: Gets the data shown in a tooltip
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 126)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTip;
    ```

## Class `DocumentTreeNodeDataExtensionMethods`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeDataExtensionMethods members directly without instantiation.
dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeDataExtensionMethods./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 341)

### Methods

- `public static AssemblyDocumentNode GetAssemblyNode(this TreeNodeData self)`
  - Summary: Gets the owner or null if none was found
  - Parameters:
    - `this TreeNodeData self`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 347)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeDataExtensionMethods.GetAssemblyNode(self: /* TreeNodeData */);
    ```
- `public static DsDocumentNode GetDocumentNode(this TreeNodeData self)`
  - Summary: Gets the first owner or null if none was found
  - Parameters:
    - `this TreeNodeData self`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 361)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeDataExtensionMethods.GetDocumentNode(self: /* TreeNodeData */);
    ```
- `public static DsDocumentNode GetTopNode(this TreeNodeData self)`
  - Summary: Gets the top node or null if none was found
  - Parameters:
    - `this TreeNodeData self`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 368)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeDataExtensionMethods.GetTopNode(self: /* TreeNodeData */);
    ```
- `public static ModuleDef GetModule(this TreeNodeData self)`
  - Summary: Gets the instance or null
  - Parameters:
    - `this TreeNodeData self`: This
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 389)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeDataExtensionMethods.GetModule(self: /* TreeNodeData */);
    ```
- `public static ModuleDocumentNode GetModuleNode(this TreeNodeData self)`
  - Summary: Gets the owner or null if none was found
  - Parameters:
    - `this TreeNodeData self`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeData.cs` (line 354)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeDataExtensionMethods.GetModuleNode(self: /* TreeNodeData */);
    ```

## Struct `DocumentTreeNodeFilterResult`

result

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeFilterResult(filterType: /* FilterType */, isMatch: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeFilterResult.cs` (line 24)

### Constructors

- `public DocumentTreeNodeFilterResult(FilterType filterType, bool isMatch)`
  - Summary: Constructor
  - Parameters:
    - `FilterType filterType`: Filter type
    - `bool isMatch`: True if it was a match
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeFilterResult.cs` (line 40)

### Fields

- `public readonly FilterType FilterType`
  - Summary: Filter type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeFilterResult.cs` (line 28)
  - Example:
    ```csharp
    var value = instance.FilterType;
    ```
- `public readonly bool IsMatch`
  - Summary: true if this is a node that can be returned as a result to the user
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeFilterResult.cs` (line 33)
  - Example:
    ```csharp
    var value = instance.IsMatch;
    ```

## Enum `DocumentTreeNodeGroupType`

Default instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeGroupType and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.DocumentTreeNodeGroupType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeNodeGroupType.cs` (line 26)

### Members

- `AssemblyRefTreeNodeGroupReferences`
- `AssemblyRefTreeNodeGroupAssemblyRef`
- `ModuleRefTreeNodeGroupReferences`
- `ReferencesFolderTreeNodeGroupModule`
- `ResourcesFolderTreeNodeGroupModule`
- `NamespaceTreeNodeGroupModule`
- `TypeTreeNodeGroupNamespace`
- `TypeTreeNodeGroupType`
- `BaseTypeFolderTreeNodeGroupType`
- `BaseTypeTreeNodeGroupBaseType`
- `InterfaceBaseTypeTreeNodeGroupBaseType`
- `DerivedTypesFolderTreeNodeGroupType`
- `MessageTreeNodeGroupDerivedTypes`
- `DerivedTypeTreeNodeGroupDerivedTypes`
- `MethodTreeNodeGroupType`
- `MethodTreeNodeGroupProperty`
- `MethodTreeNodeGroupEvent`
- `FieldTreeNodeGroupType`
- `EventTreeNodeGroupType`
- `PropertyTreeNodeGroupType`
- `ResourceTreeNodeGroup`
- `ResourceElementTreeNodeGroup`

## Class `DocumentTreeViewConstants`

Treeview constants

**Example**

```csharp
// Access dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants members directly without instantiation.
dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 26)

### Fields

- `public const double ORDER_ASSEMBLYREF_ASSEMBLYREF = 0`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 175)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_ASSEMBLYREF_ASSEMBLYREF;
    ```
- `public const double ORDER_BASETYPEFOLDER_BASETYPE = 0`
  - Summary: Order of base type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 208)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_BASETYPEFOLDER_BASETYPE;
    ```
- `public const double ORDER_BASETYPEFOLDER_INTERFACE = 100`
  - Summary: Order of interface s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 211)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_BASETYPEFOLDER_INTERFACE;
    ```
- `public const double ORDER_DERIVEDTYPES_TEXT = 0`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 214)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_DERIVEDTYPES_TEXT;
    ```
- `public const double ORDER_DERIVEDTYPES_TYPE = 100`
  - Summary: Order of interface s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 217)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_DERIVEDTYPES_TYPE;
    ```
- `public const double ORDER_EVENT_METHOD = 0`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 205)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_EVENT_METHOD;
    ```
- `public const double ORDER_MODULE_NAMESPACE = 300`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 166)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_MODULE_NAMESPACE;
    ```
- `public const double ORDER_MODULE_PE = 0`
  - Summary: Order of PE node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 157)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_MODULE_PE;
    ```
- `public const double ORDER_MODULE_REFERENCES_FOLDER = 100`
  - Summary: Order of
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 160)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_MODULE_REFERENCES_FOLDER;
    ```
- `public const double ORDER_MODULE_RESOURCES_FOLDER = 200`
  - Summary: Order of
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 163)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_MODULE_RESOURCES_FOLDER;
    ```
- `public const double ORDER_NAMESPACE_TYPE = 0`
  - Summary: Order of non-nested s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 178)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_NAMESPACE_TYPE;
    ```
- `public const double ORDER_PROPERTY_METHOD = 0`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 202)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_PROPERTY_METHOD;
    ```
- `public const double ORDER_REFERENCES_ASSEMBLYREF = 0`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 169)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_REFERENCES_ASSEMBLYREF;
    ```
- `public const double ORDER_REFERENCES_MODULEREF = 100`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 172)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_REFERENCES_MODULEREF;
    ```
- `public const double ORDER_RESOURCE = 0`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 220)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_RESOURCE;
    ```
- `public const double ORDER_RESOURCE_ELEM = 0`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 223)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_RESOURCE_ELEM;
    ```
- `public const double ORDER_RSRCPROVIDER_BAML_NODE = 3000`
  - Summary: Order of BamlResourceElementNode provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 235)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_RSRCPROVIDER_BAML_NODE;
    ```
- `public const double ORDER_RSRCPROVIDER_IMAGE_RESOURCE_NODE = 1000`
  - Summary: Order of and provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 229)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_RSRCPROVIDER_IMAGE_RESOURCE_NODE;
    ```
- `public const double ORDER_RSRCPROVIDER_RSRCELEMSET = 0`
  - Summary: Order of provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 226)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_RSRCPROVIDER_RSRCELEMSET;
    ```
- `public const double ORDER_RSRCPROVIDER_SERIALIZED_IMAGE_LIST_STREAMER_RESOURCE_ELEMENT_NODE = 10000`
  - Summary: Order of provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 238)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_RSRCPROVIDER_SERIALIZED_IMAGE_LIST_STREAMER_RESOURCE_ELEMENT_NODE;
    ```
- `public const double ORDER_RSRCPROVIDER_SERIALIZED_IMAGE_RESOURCE_ELEMENT_NODE = 2000`
  - Summary: Order of provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 232)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_RSRCPROVIDER_SERIALIZED_IMAGE_RESOURCE_ELEMENT_NODE;
    ```
- `public const double ORDER_RSRCPROVIDER_UNKNOWNSERIALIZEDRSRCELEM = double.MaxValue`
  - Summary: Order of provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 241)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_RSRCPROVIDER_UNKNOWNSERIALIZEDRSRCELEM;
    ```
- `public const double ORDER_TYPE_BASE = 0`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 181)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_TYPE_BASE;
    ```
- `public const double ORDER_TYPE_DERIVED = 100`
  - Summary: Order of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 184)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_TYPE_DERIVED;
    ```
- `public const double ORDER_TYPE_EVENT = 400`
  - Summary: Order of nested s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 193)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_TYPE_EVENT;
    ```
- `public const double ORDER_TYPE_FIELD = 500`
  - Summary: Order of nested s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 196)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_TYPE_FIELD;
    ```
- `public const double ORDER_TYPE_METHOD = 200`
  - Summary: Order of nested s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 187)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_TYPE_METHOD;
    ```
- `public const double ORDER_TYPE_PROPERTY = 300`
  - Summary: Order of nested s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 190)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_TYPE_PROPERTY;
    ```
- `public const double ORDER_TYPE_TYPE = 600`
  - Summary: Order of nested s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 199)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ORDER_TYPE_TYPE;
    ```
- `public const string ASSEMBLYREF_NODE_GUID = "13151761-85EA-4A95-9C2D-4F7A6AC3A69D"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ASSEMBLYREF_NODE_GUID;
    ```
- `public const string ASSEMBLY_NODE_GUID = "AB10C139-2735-4595-9E47-2EE0EE247C6D"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ASSEMBLY_NODE_GUID;
    ```
- `public const string BAML_RESOURCE_ELEMENT_NODE_GUID = "2410E30D-D0D3-4BEA-8FA3-C2DBDDB25D56"`
  - Summary: BamlResourceElementNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 115)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.BAML_RESOURCE_ELEMENT_NODE_GUID;
    ```
- `public const string BASETYPEFOLDER_NODE_GUID = "5D8A8AF8-6604-4031-845F-755745DFB7A7"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 64)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.BASETYPEFOLDER_NODE_GUID;
    ```
- `public const string BASETYPE_NODE_GUID = "BB9DCFC7-3527-410A-A4DA-E12FDCAC351C"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 70)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.BASETYPE_NODE_GUID;
    ```
- `public const string BUILT_IN_RESOURCE_ELEMENT_NODE_GUID = "4C5C34F1-07F4-4367-91B5-F8EB06F3C224"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 100)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.BUILT_IN_RESOURCE_ELEMENT_NODE_GUID;
    ```
- `public const string DERIVEDTYPESFOLDER_NODE_GUID = "E40470B7-A638-4BCC-9426-8F696EC260D9"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 67)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.DERIVEDTYPESFOLDER_NODE_GUID;
    ```
- `public const string DERIVEDTYPE_NODE_GUID = "497D974B-53C0-453C-A8B4-026884B2E5D1"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.DERIVEDTYPE_NODE_GUID;
    ```
- `public const string EVENT_NODE_GUID = "CA3F5F2B-560C-43BD-A3E5-CF504E2184A0"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.EVENT_NODE_GUID;
    ```
- `public const string FIELD_NODE_GUID = "B4CB8C07-A684-4AF5-8FA2-561DC3E63110"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 79)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.FIELD_NODE_GUID;
    ```
- `public const string IMAGE_RESOURCE_ELEMENT_NODE_GUID = "17E968F8-3C66-4028-804A-1DDA6BC8AD60"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 106)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.IMAGE_RESOURCE_ELEMENT_NODE_GUID;
    ```
- `public const string IMAGE_RESOURCE_NODE_GUID = "E98B5242-9BB4-4895-B228-225612CBB73E"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 103)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.IMAGE_RESOURCE_NODE_GUID;
    ```
- `public const string IMGCOR20HEADER_NODE_GUID = "0B86A8A9-2C81-416D-B87F-4D5791471753"`
  - Summary: ImageCor20HeaderNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 121)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.IMGCOR20HEADER_NODE_GUID;
    ```
- `public const string IMGDOSHEADER_NODE_GUID = "30741351-D485-42D7-9463-2BD9FAE4A591"`
  - Summary: ImageDosHeaderNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 124)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.IMGDOSHEADER_NODE_GUID;
    ```
- `public const string IMGFILEHEADER_NODE_GUID = "EFB6A52C-FE1A-4C8B-803A-3163E952C8F7"`
  - Summary: ImageFileHeaderNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 127)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.IMGFILEHEADER_NODE_GUID;
    ```
- `public const string IMGOPTHEADER32_NODE_GUID = "CC55C6DC-80B9-4EF7-B12F-D208FFB68782"`
  - Summary: ImageOptionalHeader32Node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 130)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.IMGOPTHEADER32_NODE_GUID;
    ```
- `public const string IMGOPTHEADER64_NODE_GUID = "C35952E9-9886-4A71-A752-C359E3657198"`
  - Summary: ImageOptionalHeader64Node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 133)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.IMGOPTHEADER64_NODE_GUID;
    ```
- `public const string IMGSECTHEADER_NODE_GUID = "7CE7AA42-48FA-4C25-8AE8-FE07BDDFBF23"`
  - Summary: ImageSectionHeaderNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 136)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.IMGSECTHEADER_NODE_GUID;
    ```
- `public const string MDTBLREC_NODE_GUID = "ACAD28D4-699E-40F9-95D0-7ED34BA1558A"`
  - Summary: MetaDataTableRecordNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 142)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.MDTBLREC_NODE_GUID;
    ```
- `public const string MDTBL_NODE_GUID = "C8477B7C-7F93-4479-B286-CBBBFE6CC102"`
  - Summary: MetaDataTableNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 139)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.MDTBL_NODE_GUID;
    ```
- `public const string MESSAGE_NODE_GUID = "C6F57A88-A030-4E8F-BCBC-3F17A3EADE57"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.MESSAGE_NODE_GUID;
    ```
- `public const string METHOD_NODE_GUID = "8CBBC53F-74AB-46C9-B6CB-796225D5E58A"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 82)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.METHOD_NODE_GUID;
    ```
- `public const string MODULEREF_NODE_GUID = "E3883417-71E1-4E5A-AB16-A3FB874DA2D5"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 61)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.MODULEREF_NODE_GUID;
    ```
- `public const string MODULE_NODE_GUID = "597B3358-A6F5-47EA-B0D2-57EDD1208333"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.MODULE_NODE_GUID;
    ```
- `public const string NAMESPACE_NODE_GUID = "21FE74FA-4413-4F4F-964C-63DC966D66CC"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.NAMESPACE_NODE_GUID;
    ```
- `public const string PEDOCUMENT_NODE_GUID = "CBE3DD51-3C13-4E2D-92BB-6AAB6A64028A"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.PEDOCUMENT_NODE_GUID;
    ```
- `public const string PE_NODE_GUID = "44DCC53A-BC6D-41C4-B902-DE443A3FEA11"`
  - Summary: PENode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 118)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.PE_NODE_GUID;
    ```
- `public const string PROPERTY_NODE_GUID = "38247C2D-AD67-4664-8118-01D21644031E"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 85)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.PROPERTY_NODE_GUID;
    ```
- `public const string REFERENCES_FOLDER_NODE_GUID = "D2C27572-6874-4287-BE59-2D2A28C4D80B"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.REFERENCES_FOLDER_NODE_GUID;
    ```
- `public const string RESOURCES_FOLDER_NODE_GUID = "1DD75445-9DED-482F-B6EB-4FD13E4A2197"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.RESOURCES_FOLDER_NODE_GUID;
    ```
- `public const string RESOURCE_ELEMENT_SET_NODE_GUID = "1809FF98-C72F-49B7-9677-7208927E9981"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 94)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.RESOURCE_ELEMENT_SET_NODE_GUID;
    ```
- `public const string ROOT_NODE_GUID = "E0D1E8A9-4470-4CB8-8DD7-11708EA6ED44"`
  - Summary: Guid of root node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.ROOT_NODE_GUID;
    ```
- `public const string SERIALIZED_IMAGE_LIST_STREAMER_RESOURCE_ELEMENT_NODE_GUID = "20DFF130-CD6B-4D8A-A629-E82ED9B15D5A"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 109)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.SERIALIZED_IMAGE_LIST_STREAMER_RESOURCE_ELEMENT_NODE_GUID;
    ```
- `public const string SERIALIZED_IMAGE_RESOURCE_ELEMENT_NODE = "51AA3974-BD7A-4035-9D23-C2225776D965"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 112)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.SERIALIZED_IMAGE_RESOURCE_ELEMENT_NODE;
    ```
- `public const string STRGHEADER_NODE_GUID = "1B171FEC-C3DA-4390-BE7A-FA0A98C00D20"`
  - Summary: StorageHeaderNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 145)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.STRGHEADER_NODE_GUID;
    ```
- `public const string STRGSIG_NODE_GUID = "5DB376D9-9092-4625-82DC-DC8986EC6F89"`
  - Summary: StorageSignatureNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 148)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.STRGSIG_NODE_GUID;
    ```
- `public const string STRGSTREAM_NODE_GUID = "037F16E2-0BEA-4BEE-9EDE-8E7CD1732E8E"`
  - Summary: StorageStreamNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 151)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.STRGSTREAM_NODE_GUID;
    ```
- `public const string TBLSSTREAM_NODE_GUID = "8684B8BC-DFEB-4826-B078-A72F5CDFA4A7"`
  - Summary: TablesStreamNode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 154)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.TBLSSTREAM_NODE_GUID;
    ```
- `public const string TYPE_NODE_GUID = "EB18E75B-3627-405F-B7A0-B2F38FCDC071"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 76)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.TYPE_NODE_GUID;
    ```
- `public const string UNKNOWN_DOCUMENT_NODE_GUID = "3117F133-58FC-4BE3-ABA6-331D6C962701"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.UNKNOWN_DOCUMENT_NODE_GUID;
    ```
- `public const string UNKNOWN_RESOURCE_NODE_GUID = "69EA14DC-0C68-4956-8100-956CD29C4B79"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 91)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.UNKNOWN_RESOURCE_NODE_GUID;
    ```
- `public const string UNKNOWN_SERIALIZED_RESOURCE_ELEMENT_NODE_GUID = "7D98A4A3-DDA7-44F0-AD7C-A17CEBB254F8"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 97)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.UNKNOWN_SERIALIZED_RESOURCE_ELEMENT_NODE_GUID;
    ```
- `public static readonly string DATAFORMAT_COPIED_ROOT_NODES = "610D0A0F-ACDB-4B7B-AA03-8E08C834627D"`
  - Summary: Drag and drop nodes DataFormat. It's an [] of indexes of the nodes.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DocumentTreeViewConstants.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.TreeView.DocumentTreeViewConstants.DATAFORMAT_COPIED_ROOT_NODES;
    ```

## Class `DsDocumentNode`

A document node

**Inherits/Implements:** `DocumentTreeNodeData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.DsDocumentNode(document: /* IDsDocument */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DsDocumentNode.cs` (line 26)

### Constructors

- `protected DsDocumentNode(IDsDocument document)`
  - Summary: Constructor
  - Parameters:
    - `IDsDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DsDocumentNode.cs` (line 36)

### Methods

- `public override FilterType GetFilterType(IDocumentTreeNodeFilter filter)`
  - Summary: Gets the to filter this instance
  - Parameters:
    - `IDocumentTreeNodeFilter filter`: Filter to call
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DsDocumentNode.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFilterType(filter: /* IDocumentTreeNodeFilter */);
    ```

### Properties

- `public IDsDocument Document { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DsDocumentNode.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Document;
    ```
- `public sealed override NodePathName NodePathName => new NodePathName(Guid, (Document.Filename ?? string.Empty).ToUpperInvariant())`
  - Summary: Gets the node path name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/DsDocumentNode.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NodePathName;
    ```

## Class `EventNode`

An event node

**Inherits/Implements:** `DocumentTreeNodeData`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.EventNode(@event: /* EventDef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/EventNode.cs` (line 28)

### Constructors

- `protected EventNode(EventDef @event)`
  - Summary: Constructor
  - Parameters:
    - `EventDef @event`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/EventNode.cs` (line 40)

### Methods

- `public MethodNode Create(MethodDef method)`
  - Summary: Creates a , an adder, remover, invoker, or an other method
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/EventNode.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(method: /* MethodDef */);
    ```

### Properties

- `public EventDef EventDef { get; }`
  - Summary: Gets the event
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/EventNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EventDef;
    ```

## Class `ExportDocumentTreeNodeDataFinderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDocumentTreeNodeDataFinderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.ExportDocumentTreeNodeDataFinderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataFinder.cs` (line 47)

### Constructors

- `public ExportDocumentTreeNodeDataFinderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataFinder.cs` (line 50)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataFinder.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDsDocumentNodeProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDsDocumentNodeProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.ExportDsDocumentNodeProviderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDsDocumentNodeProvider.cs` (line 48)

### Constructors

- `public ExportDsDocumentNodeProviderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDsDocumentNodeProvider.cs` (line 51)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDsDocumentNodeProvider.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `FieldNode`

A field node

**Inherits/Implements:** `DocumentTreeNodeData`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.FieldNode(field: /* FieldDef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/FieldNode.cs` (line 28)

### Constructors

- `protected FieldNode(FieldDef field)`
  - Summary: Constructor
  - Parameters:
    - `FieldDef field`: Field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/FieldNode.cs` (line 40)

### Properties

- `public FieldDef FieldDef { get; }`
  - Summary: Gets the field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/FieldNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FieldDef;
    ```

## Enum `FilterType`

Filter type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.FilterType and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.FilterType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/FilterType.cs` (line 24)

### Members

- `Default`: The node itself decides what to do
- `Visible`: Node should be visible
- `Hide`: Node should be hidden
- `CheckChildren`: Node should be hidden if all its children are hidden, else visible

## Interface `IDocumentTreeNodeDataContext`

context

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeDataContext and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeDataContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 28)

### Properties

- `IDecompiler Decompiler { get; }`
  - Summary: Default language
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Decompiler;
    ```
- `IDocumentTreeNodeFilter Filter { get; }`
  - Summary: Gets the filter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filter;
    ```
- `IDocumentTreeView DocumentTreeView { get; }`
  - Summary: Owner
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentTreeView;
    ```
- `IResourceNodeFactory ResourceNodeFactory { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResourceNodeFactory;
    ```
- `ITreeViewNodeTextElementProvider TreeViewNodeTextElementProvider { get; }`
  - Summary: Gets the treeview node text element provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TreeViewNodeTextElementProvider;
    ```
- `bool CanDragAndDrop { get; }`
  - Summary: true if drag and drop is allowed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanDragAndDrop;
    ```
- `bool DeserializeResources { get; }`
  - Summary: true to deserialize resources
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DeserializeResources;
    ```
- `bool ShowAssemblyPublicKeyToken { get; }`
  - Summary: Show assembly public key token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowAssemblyPublicKeyToken;
    ```
- `bool ShowAssemblyVersion { get; }`
  - Summary: Show assembly version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowAssemblyVersion;
    ```
- `bool ShowToken { get; }`
  - Summary: Show MD token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowToken;
    ```
- `bool SingleClickExpandsChildren { get; }`
  - Summary: true if single clicks expand children
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SingleClickExpandsChildren;
    ```
- `bool SyntaxHighlight { get; }`
  - Summary: true if it should be syntax highlighted
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SyntaxHighlight;
    ```
- `bool UseNewRenderer { get; }`
  - Summary: true to use the new optimized renderer. It doesn't support all unicode chars or word wrapping
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseNewRenderer;
    ```
- `int FilterVersion { get; }`
  - Summary: Filter version, gets incremented each time gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataContext.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FilterVersion;
    ```

## Interface `IDocumentTreeNodeDataFinder`

Finds nodes. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeDataFinder and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeDataFinder(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataFinder.cs` (line 28)

### Methods

- `DocumentTreeNodeData FindNode(IDocumentTreeView documentTreeView, object @ref)`
  - Summary: Returns an existing node or null
  - Parameters:
    - `IDocumentTreeView documentTreeView`: Owner
    - `object @ref`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataFinder.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(documentTreeView: /* IDocumentTreeView */, @ref: /* object */);
    ```

## Interface `IDocumentTreeNodeDataFinderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeDataFinderMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeDataFinderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataFinder.cs` (line 39)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeDataFinder.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDocumentTreeNodeFilter`

Filters instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeFilter and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeFilter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 28)

### Methods

- `DocumentTreeNodeFilterResult GetResult(AssemblyDef asm)`
  - Summary: Returns a filter result. Called if it's a
  - Parameters:
    - `AssemblyDef asm`: Assembly
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asm: /* AssemblyDef */);
    ```
- `DocumentTreeNodeFilterResult GetResult(AssemblyRef asmRef)`
  - Summary: Returns a filter result. Called if it's a
  - Parameters:
    - `AssemblyRef asmRef`: Assembly reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 136)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(asmRef: /* AssemblyRef */);
    ```
- `DocumentTreeNodeFilterResult GetResult(BaseTypeFolderNode node)`
  - Summary: Returns a filter result. The input can be null.
  - Parameters:
    - `BaseTypeFolderNode node`: Node, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* BaseTypeFolderNode */);
    ```
- `DocumentTreeNodeFilterResult GetResult(BaseTypeNode node)`
  - Summary: Returns a filter result. The input can be null.
  - Parameters:
    - `BaseTypeNode node`: Node, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 150)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* BaseTypeNode */);
    ```
- `DocumentTreeNodeFilterResult GetResult(DerivedTypeNode node)`
  - Summary: Returns a filter result. The input can be null.
  - Parameters:
    - `DerivedTypeNode node`: Node, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 164)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* DerivedTypeNode */);
    ```
- `DocumentTreeNodeFilterResult GetResult(DerivedTypesFolderNode node)`
  - Summary: Returns a filter result. The input can be null.
  - Parameters:
    - `DerivedTypesFolderNode node`: Node, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 171)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* DerivedTypesFolderNode */);
    ```
- `DocumentTreeNodeFilterResult GetResult(EventDef evt)`
  - Summary: Returns a filter result. Called if it's a
  - Parameters:
    - `EventDef evt`: Event
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 92)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(evt: /* EventDef */);
    ```
- `DocumentTreeNodeFilterResult GetResult(FieldDef field)`
  - Summary: Returns a filter result. Called if it's a
  - Parameters:
    - `FieldDef field`: Field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(field: /* FieldDef */);
    ```
- `DocumentTreeNodeFilterResult GetResult(IDsDocument document)`
  - Summary: Returns a filter result. Called if it's a but not a or a .
  - Parameters:
    - `IDsDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(document: /* IDsDocument */);
    ```
- `DocumentTreeNodeFilterResult GetResult(MethodDef method)`
  - Summary: Returns a filter result. Called if it's a
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */);
    ```
- `DocumentTreeNodeFilterResult GetResult(MethodDef method, Local local)`
  - Summary: Returns a filter result for a method's
  - Parameters:
    - `MethodDef method`: Method
    - `Local local`: Local
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 129)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */, local: /* Local */);
    ```
- `DocumentTreeNodeFilterResult GetResult(MethodDef method, ParamDef param)`
  - Summary: Returns a filter result for a method's
  - Parameters:
    - `MethodDef method`: Method
    - `ParamDef param`: Parameter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(method: /* MethodDef */, param: /* ParamDef */);
    ```
- `DocumentTreeNodeFilterResult GetResult(ModuleDef mod)`
  - Summary: Returns a filter result. Called if it's a
  - Parameters:
    - `ModuleDef mod`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(mod: /* ModuleDef */);
    ```
- `DocumentTreeNodeFilterResult GetResult(ModuleRef modRef)`
  - Summary: Returns a filter result. Called if it's a
  - Parameters:
    - `ModuleRef modRef`: Module reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(modRef: /* ModuleRef */);
    ```
- `DocumentTreeNodeFilterResult GetResult(PropertyDef prop)`
  - Summary: Returns a filter result. Called if it's a
  - Parameters:
    - `PropertyDef prop`: Property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(prop: /* PropertyDef */);
    ```
- `DocumentTreeNodeFilterResult GetResult(ReferencesFolderNode node)`
  - Summary: Returns a filter result. The input can be null.
  - Parameters:
    - `ReferencesFolderNode node`: Node, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 178)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ReferencesFolderNode */);
    ```
- `DocumentTreeNodeFilterResult GetResult(ResourceElementNode node)`
  - Summary: Returns a filter result. The input can be null.
  - Parameters:
    - `ResourceElementNode node`: Node, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourceElementNode */);
    ```
- `DocumentTreeNodeFilterResult GetResult(ResourceNode node)`
  - Summary: Returns a filter result. The input can be null.
  - Parameters:
    - `ResourceNode node`: Node, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 192)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourceNode */);
    ```
- `DocumentTreeNodeFilterResult GetResult(ResourcesFolderNode node)`
  - Summary: Returns a filter result. The input can be null.
  - Parameters:
    - `ResourcesFolderNode node`: Node, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 185)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(node: /* ResourcesFolderNode */);
    ```
- `DocumentTreeNodeFilterResult GetResult(TypeDef type)`
  - Summary: Returns a filter result. Called if it's a
  - Parameters:
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(type: /* TypeDef */);
    ```
- `DocumentTreeNodeFilterResult GetResult(string ns, IDsDocument owner)`
  - Summary: Returns a filter result. Called if it's a
  - Parameters:
    - `string ns`: Namespace
    - `IDsDocument owner`: Owner document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResult(ns: /* string */, owner: /* IDsDocument */);
    ```
- `DocumentTreeNodeFilterResult GetResultAttributes(IHasCustomAttribute hca)`
  - Summary: Returns a filter result
  - Parameters:
    - `IHasCustomAttribute hca`: Object with custom attributes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 213)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultAttributes(hca: /* IHasCustomAttribute */);
    ```
- `DocumentTreeNodeFilterResult GetResultBody(MethodDef method)`
  - Summary: Returns a filter result for a method's body
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultBody(method: /* MethodDef */);
    ```
- `DocumentTreeNodeFilterResult GetResultLocals(MethodDef method)`
  - Summary: Returns a filter result for a method's s
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultLocals(method: /* MethodDef */);
    ```
- `DocumentTreeNodeFilterResult GetResultOther(DocumentTreeNodeData node)`
  - Summary: Returns a filter result if it's any other instance
  - Parameters:
    - `DocumentTreeNodeData node`: Node, can't be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 206)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultOther(node: /* DocumentTreeNodeData */);
    ```
- `DocumentTreeNodeFilterResult GetResultParamDefs(MethodDef method)`
  - Summary: Returns a filter result for a method's s
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeFilter.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResultParamDefs(method: /* MethodDef */);
    ```

## Interface `IDocumentTreeNodeGroups`

Contains default instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeGroups and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeGroups(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeGroups.cs` (line 26)

### Methods

- `ITreeNodeGroup GetGroup(DocumentTreeNodeGroupType type)`
  - Summary: Gets a instance
  - Parameters:
    - `DocumentTreeNodeGroupType type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeGroups.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGroup(type: /* DocumentTreeNodeGroupType */);
    ```

## Interface `IDocumentTreeNodeProvider`

Creates

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeProvider and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDocumentTreeNodeProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 26)

### Methods

- `AssemblyDocumentNode CreateAssembly(IDsDotNetDocument asmDocument)`
  - Summary: Creates a
  - Parameters:
    - `IDsDotNetDocument asmDocument`: Assembly
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAssembly(asmDocument: /* IDsDotNetDocument */);
    ```
- `AssemblyReferenceNode Create(AssemblyRef asmRef, ModuleDef ownerModule)`
  - Summary: Creates a
  - Parameters:
    - `AssemblyRef asmRef`: Assembly reference
    - `ModuleDef ownerModule`: Owner module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(asmRef: /* AssemblyRef */, ownerModule: /* ModuleDef */);
    ```
- `EventNode Create(EventDef @event)`
  - Summary: Creates a
  - Parameters:
    - `EventDef @event`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 110)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(@event: /* EventDef */);
    ```
- `FieldNode Create(FieldDef field)`
  - Summary: Creates a
  - Parameters:
    - `FieldDef field`: Field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(field: /* FieldDef */);
    ```
- `MethodNode Create(MethodDef method)`
  - Summary: Creates a
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(method: /* MethodDef */);
    ```
- `MethodNode CreateEvent(MethodDef method)`
  - Summary: Creates an event
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateEvent(method: /* MethodDef */);
    ```
- `MethodNode CreateProperty(MethodDef method)`
  - Summary: Creates a property
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateProperty(method: /* MethodDef */);
    ```
- `ModuleDocumentNode CreateModule(IDsDotNetDocument modDocument)`
  - Summary: Creates a
  - Parameters:
    - `IDsDotNetDocument modDocument`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateModule(modDocument: /* IDsDotNetDocument */);
    ```
- `ModuleReferenceNode Create(ModuleRef modRef)`
  - Summary: Creates a
  - Parameters:
    - `ModuleRef modRef`: Module reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(modRef: /* ModuleRef */);
    ```
- `NamespaceNode Create(string name)`
  - Summary: Creates a
  - Parameters:
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(name: /* string */);
    ```
- `PropertyNode Create(PropertyDef property)`
  - Summary: Creates a
  - Parameters:
    - `PropertyDef property`: Property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(property: /* PropertyDef */);
    ```
- `TypeNode Create(TypeDef type)`
  - Summary: Creates a non-nested
  - Parameters:
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(type: /* TypeDef */);
    ```
- `TypeNode CreateNested(TypeDef type)`
  - Summary: Creates a nested
  - Parameters:
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeNodeProvider.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateNested(type: /* TypeDef */);
    ```

## Interface `IDocumentTreeView`

Document treeview

**Inherits/Implements:** `IDocumentTreeNodeProvider`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDocumentTreeView and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDocumentTreeView(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 32)

### Methods

- `AssemblyDocumentNode FindNode(AssemblyDef assembly)`
  - Summary: Returns a node or null if none could be found
  - Parameters:
    - `AssemblyDef assembly`: Assembly
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(assembly: /* AssemblyDef */);
    ```
- `DocumentTreeNodeData FindNode(object @ref)`
  - Summary: Returns a node or null if none could be found
  - Parameters:
    - `object @ref`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(@ref: /* object */);
    ```
- `DsDocumentNode CreateNode(DsDocumentNode owner, IDsDocument document)`
  - Summary: Creates a new instance. This will internally call all s it can find.
  - Parameters:
    - `DsDocumentNode owner`: Owner node or null if owner is the root node
    - `IDsDocument document`: New document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateNode(owner: /* DsDocumentNode */, document: /* IDsDocument */);
    ```
- `DsDocumentNode FindNode(IDsDocument document)`
  - Summary: Returns a node or null if none could be found
  - Parameters:
    - `IDsDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 107)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(document: /* IDsDocument */);
    ```
- `EventNode FindNode(EventDef @event)`
  - Summary: Returns a node or null if none could be found
  - Parameters:
    - `EventDef @event`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 156)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(@event: /* EventDef */);
    ```
- `FieldNode FindNode(FieldDef field)`
  - Summary: Returns a node or null if none could be found
  - Parameters:
    - `FieldDef field`: Field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 142)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(field: /* FieldDef */);
    ```
- `IEnumerable<DsDocumentNode> GetAllCreatedDocumentNodes()`
  - Summary: Gets all created s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAllCreatedDocumentNodes();
    ```
- `IEnumerable<ModuleDocumentNode> GetAllModuleNodes()`
  - Summary: Gets all s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAllModuleNodes();
    ```
- `MethodNode FindNode(MethodDef method)`
  - Summary: Returns a node or null if none could be found
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(method: /* MethodDef */);
    ```
- `ModuleDocumentNode FindNode(ModuleDef module)`
  - Summary: Returns a node or null if none could be found
  - Parameters:
    - `ModuleDef module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(module: /* ModuleDef */);
    ```
- `NamespaceNode FindNamespaceNode(IDsDocument module, string @namespace)`
  - Summary: Returns a node or null if none could be found
  - Parameters:
    - `IDsDocument module`: Owner module
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 164)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNamespaceNode(module: /* IDsDocument */, @namespace: /* string */);
    ```
- `PropertyNode FindNode(PropertyDef property)`
  - Summary: Returns a node or null if none could be found
  - Parameters:
    - `PropertyDef property`: Property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 149)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(property: /* PropertyDef */);
    ```
- `TypeNode FindNode(TypeDef type)`
  - Summary: Returns a node or null if none could be found
  - Parameters:
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 128)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(type: /* TypeDef */);
    ```
- `bool RaiseNodeActivated(DocumentTreeNodeData node)`
  - Summary: Should only be called by the node that gets activated. Returns true if someone handled it.
  - Parameters:
    - `DocumentTreeNodeData node`: The activated node (should be the caller)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.RaiseNodeActivated(node: /* DocumentTreeNodeData */);
    ```
- `void AddNode(DsDocumentNode documentNode, int index)`
  - Summary: Adds to the list
  - Parameters:
    - `DsDocumentNode documentNode`: Node
    - `int index`: Index or -1
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    instance.AddNode(documentNode: /* DsDocumentNode */, index: /* int */);
    ```
- `void Dispose()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```
- `void Remove(IEnumerable<DsDocumentNode> nodes)`
  - Summary: Removes . They must be top nodes (eg. s)
  - Parameters:
    - `IEnumerable<DsDocumentNode> nodes`: Nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(nodes: /* IEnumerable<DsDocumentNode> */);
    ```
- `void SetDecompiler(IDecompiler decompiler)`
  - Summary: Sets decompiler
  - Parameters:
    - `IDecompiler decompiler`: Decompiler
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 194)
  - Example:
    ```csharp
    // Example invocation
    instance.SetDecompiler(decompiler: /* IDecompiler */);
    ```
- `void SortTopNodes()`
  - Summary: Sorts all documents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 204)
  - Example:
    ```csharp
    // Example invocation
    instance.SortTopNodes();
    ```

### Properties

- `IDocumentTreeNodeGroups DocumentTreeNodeGroups { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 169)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentTreeNodeGroups;
    ```
- `IDotNetImageService DotNetImageService { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DotNetImageService;
    ```
- `IDsDocumentService DocumentService { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentService;
    ```
- `ITreeView TreeView { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TreeView;
    ```
- `IWpfCommands WpfCommands { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.WpfCommands;
    ```
- `bool CanSortTopNodes { get; }`
  - Summary: true if can be called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 209)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanSortTopNodes;
    ```

### Events

- `event EventHandler<DocumentTreeNodeActivatedEventArgs> NodeActivated`
  - Summary: Raised when a node gets activated (eg. double clicked)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 66)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.NodeActivated += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<EventArgs> NodesTextChanged`
  - Summary: Raised when the node's text has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 61)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.NodesTextChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<NotifyDocumentTreeViewCollectionChangedEventArgs> CollectionChanged`
  - Summary: Raised when the collection gets changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 56)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.CollectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<TreeViewSelectionChangedEventArgs> SelectionChanged`
  - Summary: Raised when selection has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeView.cs` (line 71)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.SelectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IDocumentTreeViewProvider`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDocumentTreeViewProvider and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDocumentTreeViewProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewProvider.cs` (line 24)

### Methods

- `IDocumentTreeView Create(IDocumentTreeNodeFilter filter)`
  - Summary: Creates a new instance
  - Parameters:
    - `IDocumentTreeNodeFilter filter`: Filter or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewProvider.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(filter: /* IDocumentTreeNodeFilter */);
    ```

## Interface `IDocumentTreeViewSettings`

settings

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDocumentTreeViewSettings and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDocumentTreeViewSettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 26)

### Properties

- `DocumentFilterType FilterDraggedItems { get; }`
  - Summary: How to filter dragged items
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FilterDraggedItems;
    ```
- `MemberKind MemberKind0 { get; }`
  - Summary: Gets 0th member
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberKind0;
    ```
- `MemberKind MemberKind1 { get; }`
  - Summary: Gets 1st member
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberKind1;
    ```
- `MemberKind MemberKind2 { get; }`
  - Summary: Gets 2nd member
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberKind2;
    ```
- `MemberKind MemberKind3 { get; }`
  - Summary: Gets 3rd member
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberKind3;
    ```
- `MemberKind MemberKind4 { get; }`
  - Summary: Gets 4th member
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberKind4;
    ```
- `bool DeserializeResources { get; }`
  - Summary: true to deserialize resources
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DeserializeResources;
    ```
- `bool ShowAssemblyPublicKeyToken { get; }`
  - Summary: true to show assembly public key token when printing assembly nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowAssemblyPublicKeyToken;
    ```
- `bool ShowAssemblyVersion { get; }`
  - Summary: true to show assembly version when printing assembly nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowAssemblyVersion;
    ```
- `bool ShowToken { get; }`
  - Summary: true to show tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowToken;
    ```
- `bool SingleClickExpandsTreeViewChildren { get; }`
  - Summary: true causes single clicks to expand children, false requires a double click
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SingleClickExpandsTreeViewChildren;
    ```
- `bool SyntaxHighlight { get; }`
  - Summary: true to syntax highlight the treeview
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDocumentTreeViewSettings.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SyntaxHighlight;
    ```

## Interface `IDsDocumentNodeProvider`

Creates s. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDsDocumentNodeProvider and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDsDocumentNodeProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDsDocumentNodeProvider.cs` (line 28)

### Methods

- `DsDocumentNode Create(IDocumentTreeView documentTreeView, DsDocumentNode owner, IDsDocument document)`
  - Summary: Creates a new instance or returns null
  - Parameters:
    - `IDocumentTreeView documentTreeView`: Document treeview
    - `DsDocumentNode owner`: Owner node or null if owner is the root node
    - `IDsDocument document`: New document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDsDocumentNodeProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(documentTreeView: /* IDocumentTreeView */, owner: /* DsDocumentNode */, document: /* IDsDocument */);
    ```

## Interface `IDsDocumentNodeProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.IDsDocumentNodeProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.IDsDocumentNodeProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDsDocumentNodeProvider.cs` (line 40)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/IDsDocumentNodeProvider.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Enum `MemberKind`

Order of members in the treeview

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.MemberKind and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.MemberKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/MemberKind.cs` (line 24)

### Members

- `NestedTypes`: Nested types
- `Fields`: Fields
- `Events`: Events
- `Properties`: Properties
- `Methods`: Methods

## Class `MessageNode`

A message node

**Inherits/Implements:** `DocumentTreeNodeData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.MessageNode();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/MessageNode.cs` (line 24)

### Constructors

- `protected MessageNode()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/MessageNode.cs` (line 33)

### Properties

- `public abstract string Message { get; }`
  - Summary: Gets the message
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/MessageNode.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```

## Class `MethodNode`

A method node

**Inherits/Implements:** `DocumentTreeNodeData`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.MethodNode(method: /* MethodDef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/MethodNode.cs` (line 28)

### Constructors

- `protected MethodNode(MethodDef method)`
  - Summary: Constructor
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/MethodNode.cs` (line 40)

### Properties

- `public MethodDef MethodDef { get; }`
  - Summary: Gets the method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/MethodNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MethodDef;
    ```

## Class `ModuleDocumentNode`

A .NET module file

**Inherits/Implements:** `DsDocumentNode`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.ModuleDocumentNode(document: /* IDsDotNetDocument */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ModuleDocumentNode.cs` (line 28)

### Constructors

- `protected ModuleDocumentNode(IDsDotNetDocument document)`
  - Summary: Constructor
  - Parameters:
    - `IDsDotNetDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ModuleDocumentNode.cs` (line 40)

### Methods

- `public NamespaceNode Create(string name)`
  - Summary: Creates a
  - Parameters:
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ModuleDocumentNode.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(name: /* string */);
    ```
- `public abstract NamespaceNode FindNode(string ns)`
  - Summary: Returns an existing instance or null
  - Parameters:
    - `string ns`: Namespace
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ModuleDocumentNode.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.FindNode(ns: /* string */);
    ```

### Properties

- `public new IDsDotNetDocument Document => (IDsDotNetDocument)base.Document`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ModuleDocumentNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Document;
    ```

## Class `ModuleReferenceNode`

A module reference node

**Inherits/Implements:** `DocumentTreeNodeData`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.ModuleReferenceNode(moduleRef: /* ModuleRef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ModuleReferenceNode.cs` (line 28)

### Constructors

- `protected ModuleReferenceNode(ModuleRef moduleRef)`
  - Summary: Constructor
  - Parameters:
    - `ModuleRef moduleRef`: Module reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ModuleReferenceNode.cs` (line 40)

### Properties

- `public ModuleRef ModuleRef { get; }`
  - Summary: Gets the module reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ModuleReferenceNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleRef;
    ```

## Class `NamespaceNode`

A namespace node

**Inherits/Implements:** `DocumentTreeNodeData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.NamespaceNode(name: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NamespaceNode.cs` (line 26)

### Constructors

- `protected NamespaceNode(string name)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NamespaceNode.cs` (line 36)

### Methods

- `public TypeNode Create(TypeDef type)`
  - Summary: Creates a
  - Parameters:
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NamespaceNode.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(type: /* TypeDef */);
    ```

### Properties

- `public string Name { get; set; }`
  - Summary: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NamespaceNode.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Struct `NodePathName`

Node path name

**Inherits/Implements:** `IEquatable<NodePathName>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.NodePathName(guid: /* Guid */, name: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePathName.cs` (line 28)

### Constructors

- `public NodePathName(Guid guid, string name = null)`
  - Summary: Constructor
  - Parameters:
    - `Guid guid`: Guid of node ()
    - `string name` (default: `null`): Extra data if needed or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePathName.cs` (line 44)

### Methods

- `public bool Equals(NodePathName other)`
  - Summary: Equals()
  - Parameters:
    - `NodePathName other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePathName.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* NodePathName */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePathName.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePathName.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePathName.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public Guid Guid { get; }`
  - Summary: Gets the guid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePathName.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public string Name { get; }`
  - Summary: Gets the name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePathName.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Struct `NodePrinter`

Node printer

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.NodePrinter and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.NodePrinter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 31)

### Methods

- `public void Write(ITextColorWriter output, IDecompiler decompiler, AssemblyDef asm, bool showToken, bool showAssemblyVersion, bool showAssemblyPublicKeyToken)`
  - Summary: Writes an assembly
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `AssemblyDef asm`: Assembly
    - `bool showToken`: true to write tokens
    - `bool showAssemblyVersion`: true to write version
    - `bool showAssemblyPublicKeyToken`: true to write public key token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, asm: /* AssemblyDef */, showToken: /* bool */, showAssemblyVersion: /* bool */, showAssemblyPublicKeyToken: /* bool */);
    ```
- `public void Write(ITextColorWriter output, IDecompiler decompiler, AssemblyRef asmRef, bool showToken)`
  - Summary: Writes an assembly reference
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `AssemblyRef asmRef`: Assembly reference
    - `bool showToken`: true to write tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 149)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, asmRef: /* AssemblyRef */, showToken: /* bool */);
    ```
- `public void Write(ITextColorWriter output, IDecompiler decompiler, EventDef @event, bool showToken)`
  - Summary: Writes an event
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `EventDef @event`: Description not provided.
    - `bool showToken`: true to write tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 197)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, @event: /* EventDef */, showToken: /* bool */);
    ```
- `public void Write(ITextColorWriter output, IDecompiler decompiler, FieldDef field, bool showToken)`
  - Summary: Writes a field
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `FieldDef field`: Field
    - `bool showToken`: true to write tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 230)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, field: /* FieldDef */, showToken: /* bool */);
    ```
- `public void Write(ITextColorWriter output, IDecompiler decompiler, IDsDocument document)`
  - Summary: Writes a file
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `IDsDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, document: /* IDsDocument */);
    ```
- `public void Write(ITextColorWriter output, IDecompiler decompiler, ITypeDefOrRef type, bool showToken)`
  - Summary: Writes a type
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `ITypeDefOrRef type`: Type
    - `bool showToken`: true to write tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 185)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, type: /* ITypeDefOrRef */, showToken: /* bool */);
    ```
- `public void Write(ITextColorWriter output, IDecompiler decompiler, MethodDef method, bool showToken)`
  - Summary: Writes a method
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `MethodDef method`: Method
    - `bool showToken`: true to write tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 246)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, method: /* MethodDef */, showToken: /* bool */);
    ```
- `public void Write(ITextColorWriter output, IDecompiler decompiler, ModuleDef module, bool showToken)`
  - Summary: Writes a module
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `ModuleDef module`: Module
    - `bool showToken`: true to write tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 123)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, module: /* ModuleDef */, showToken: /* bool */);
    ```
- `public void Write(ITextColorWriter output, IDecompiler decompiler, ModuleRef modRef, bool showToken)`
  - Summary: Writes a module reference
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `ModuleRef modRef`: Module reference
    - `bool showToken`: true to write tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 161)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, modRef: /* ModuleRef */, showToken: /* bool */);
    ```
- `public void Write(ITextColorWriter output, IDecompiler decompiler, PropertyDef property, bool showToken, bool? isIndexer)`
  - Summary: Writes a property
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `PropertyDef property`: Property
    - `bool showToken`: true to write tokens
    - `bool? isIndexer`: true if it's an indexer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 214)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, property: /* PropertyDef */, showToken: /* bool */, isIndexer: /* bool? */);
    ```
- `public void Write(ITextColorWriter output, IDecompiler decompiler, TypeDef type, bool showToken)`
  - Summary: Writes a type
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `TypeDef type`: Type
    - `bool showToken`: true to write tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 173)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, type: /* TypeDef */, showToken: /* bool */);
    ```
- `public void WriteNamespace(ITextColorWriter output, IDecompiler decompiler, string @namespace)`
  - Summary: Writes a namespace
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NodePrinter.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteNamespace(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, @namespace: /* string */);
    ```

## Enum `NotifyDocumentTreeViewCollection`

Event type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.NotifyDocumentTreeViewCollection and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.NotifyDocumentTreeViewCollection(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NotifyDocumentTreeViewCollection.cs` (line 24)

### Members

- `Clear`: All document nodes have been cleared
- `Add`: A new document node was added
- `Remove`: A document node was removed

## Class `NotifyDocumentTreeViewCollectionChangedEventArgs`

Event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.NotifyDocumentTreeViewCollectionChangedEventArgs and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.NotifyDocumentTreeViewCollectionChangedEventArgs(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NotifyDocumentTreeViewCollectionChangedEventArgs.cs` (line 27)

### Methods

- `public static NotifyDocumentTreeViewCollectionChangedEventArgs CreateAdd(DsDocumentNode document)`
  - Summary: Creates a instance
  - Parameters:
    - `DsDocumentNode document`: Added document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NotifyDocumentTreeViewCollectionChangedEventArgs.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.NotifyDocumentTreeViewCollectionChangedEventArgs.CreateAdd(document: /* DsDocumentNode */);
    ```
- `public static NotifyDocumentTreeViewCollectionChangedEventArgs CreateClear(DsDocumentNode[] clearedDocuments)`
  - Summary: Creates a instance
  - Parameters:
    - `DsDocumentNode[] clearedDocuments`: All cleared documents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NotifyDocumentTreeViewCollectionChangedEventArgs.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.NotifyDocumentTreeViewCollectionChangedEventArgs.CreateClear(clearedDocuments: /* DsDocumentNode[] */);
    ```
- `public static NotifyDocumentTreeViewCollectionChangedEventArgs CreateRemove(DsDocumentNode[] documents)`
  - Summary: Creates a instance
  - Parameters:
    - `DsDocumentNode[] documents`: Removed documents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NotifyDocumentTreeViewCollectionChangedEventArgs.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.NotifyDocumentTreeViewCollectionChangedEventArgs.CreateRemove(documents: /* DsDocumentNode[] */);
    ```

### Properties

- `public DsDocumentNode[] Nodes { get; private set; }`
  - Summary: All document nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NotifyDocumentTreeViewCollectionChangedEventArgs.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Nodes;
    ```
- `public NotifyDocumentTreeViewCollection Type { get; private set; }`
  - Summary: Event type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/NotifyDocumentTreeViewCollectionChangedEventArgs.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```

## Class `PEDocumentNode`

A PE file (but not a .NET file)

**Inherits/Implements:** `DsDocumentNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.PEDocumentNode(document: /* IDsDocument */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/PEDocumentNode.cs` (line 27)

### Constructors

- `protected PEDocumentNode(IDsDocument document)`
  - Summary: Constructor
  - Parameters:
    - `IDsDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/PEDocumentNode.cs` (line 37)

### Properties

- `public bool IsExe => (Document.PEImage.ImageNTHeaders.FileHeader.Characteristics & Characteristics.Dll) == 0`
  - Summary: true if it's an .exe file, false if it's a .dll file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/PEDocumentNode.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsExe;
    ```

## Class `PropertyNode`

A property node

**Inherits/Implements:** `DocumentTreeNodeData`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.PropertyNode(property: /* PropertyDef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/PropertyNode.cs` (line 28)

### Constructors

- `protected PropertyNode(PropertyDef property)`
  - Summary: Constructor
  - Parameters:
    - `PropertyDef property`: Property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/PropertyNode.cs` (line 40)

### Methods

- `public MethodNode Create(MethodDef method)`
  - Summary: Creates a , a getter, setter, or an other property method
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/PropertyNode.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(method: /* MethodDef */);
    ```

### Properties

- `public PropertyDef PropertyDef { get; }`
  - Summary: Gets the property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/PropertyNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PropertyDef;
    ```

## Class `ReferencesFolderNode`

References node

**Inherits/Implements:** `DocumentTreeNodeData`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.ReferencesFolderNode and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.ReferencesFolderNode(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ReferencesFolderNode.cs` (line 26)

### Methods

- `public ModuleReferenceNode Create(ModuleRef modRef)`
  - Summary: Creates a
  - Parameters:
    - `ModuleRef modRef`: Module reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ReferencesFolderNode.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(modRef: /* ModuleRef */);
    ```
- `public abstract AssemblyReferenceNode Create(AssemblyRef asmRef)`
  - Summary: Creates a
  - Parameters:
    - `AssemblyRef asmRef`: Assembly reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ReferencesFolderNode.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(asmRef: /* AssemblyRef */);
    ```

## Class `ResourcesFolderNode`

Resources node

**Inherits/Implements:** `DocumentTreeNodeData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.ResourcesFolderNode();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ResourcesFolderNode.cs` (line 24)

### Constructors

- `protected ResourcesFolderNode()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/ResourcesFolderNode.cs` (line 28)

## Class `TypeNode`

A type node

**Inherits/Implements:** `DocumentTreeNodeData`, `IMDTokenNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.TypeNode(type: /* TypeDef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/TypeNode.cs` (line 28)

### Constructors

- `protected TypeNode(TypeDef type)`
  - Summary: Constructor
  - Parameters:
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/TypeNode.cs` (line 40)

### Methods

- `public EventNode Create(EventDef @event)`
  - Summary: Creates a
  - Parameters:
    - `EventDef @event`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/TypeNode.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(@event: /* EventDef */);
    ```
- `public FieldNode Create(FieldDef field)`
  - Summary: Creates a
  - Parameters:
    - `FieldDef field`: Field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/TypeNode.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(field: /* FieldDef */);
    ```
- `public MethodNode Create(MethodDef method)`
  - Summary: Creates a
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/TypeNode.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(method: /* MethodDef */);
    ```
- `public PropertyNode Create(PropertyDef property)`
  - Summary: Creates a
  - Parameters:
    - `PropertyDef property`: Property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/TypeNode.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(property: /* PropertyDef */);
    ```
- `public TypeNode Create(TypeDef type)`
  - Summary: Creates a
  - Parameters:
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/TypeNode.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(type: /* TypeDef */);
    ```

### Properties

- `public TypeDef TypeDef { get; }`
  - Summary: Gets the type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/TypeNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeDef;
    ```

## Class `UnknownDocumentNode`

Unknown file (not a PE or .NET file)

**Inherits/Implements:** `DsDocumentNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.UnknownDocumentNode(document: /* IDsDocument */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/UnknownDocumentNode.cs` (line 26)

### Constructors

- `protected UnknownDocumentNode(IDsDocument document)`
  - Summary: Constructor
  - Parameters:
    - `IDsDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/UnknownDocumentNode.cs` (line 31)

