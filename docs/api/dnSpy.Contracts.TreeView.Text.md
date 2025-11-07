# Namespace `dnSpy.Contracts.TreeView.Text`

## Interface `ITreeViewNodeTextElementProvider`

Creates WPF text elements for treeview nodes

**Example**

```csharp
// Instantiate dnSpy.Contracts.TreeView.Text.ITreeViewNodeTextElementProvider and call its members.
var instance = new dnSpy.Contracts.TreeView.Text.ITreeViewNodeTextElementProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/ITreeViewNodeTextElementProvider.cs` (line 27)

### Methods

- `FrameworkElement CreateTextElement(TreeViewNodeClassifierContext context, string contentType, TextElementFlags flags)`
  - Summary: Creates a WPF text element
  - Parameters:
    - `TreeViewNodeClassifierContext context`: Context
    - `string contentType`: Treeview node content type, eg.
    - `TextElementFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/ITreeViewNodeTextElementProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextElement(context: /* TreeViewNodeClassifierContext */, contentType: /* string */, flags: /* TextElementFlags */);
    ```

## Class `TreeViewContentTypes`

Treeview content types

**Example**

```csharp
// Access dnSpy.Contracts.TreeView.Text.TreeViewContentTypes members directly without instantiation.
dnSpy.Contracts.TreeView.Text.TreeViewContentTypes./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/TreeViewContentTypes.cs` (line 24)

### Fields

- `public const string TreeViewNode = nameof(TreeViewNode)`
  - Summary: Treeview node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/TreeViewContentTypes.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.TreeView.Text.TreeViewContentTypes.TreeViewNode;
    ```
- `public const string TreeViewNodeAnalyzer = nameof(TreeViewNodeAnalyzer)`
  - Summary: Analyzer treeview node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/TreeViewContentTypes.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.TreeView.Text.TreeViewContentTypes.TreeViewNodeAnalyzer;
    ```
- `public const string TreeViewNodeAppSettings = nameof(TreeViewNodeAppSettings)`
  - Summary: Application settings treeview node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/TreeViewContentTypes.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.TreeView.Text.TreeViewContentTypes.TreeViewNodeAppSettings;
    ```
- `public const string TreeViewNodeAssemblyExplorer = nameof(TreeViewNodeAssemblyExplorer)`
  - Summary: Assembly Explorer treeview node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/TreeViewContentTypes.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.TreeView.Text.TreeViewContentTypes.TreeViewNodeAssemblyExplorer;
    ```

## Class `TreeViewNodeClassifierContext`

Treeview node classifier context passed to s that classify treeview nodes

**Inherits/Implements:** `TextClassifierContext`

**Example**

```csharp
var instance = new dnSpy.Contracts.TreeView.Text.TreeViewNodeClassifierContext(text: /* string */, treeView: /* ITreeView */, node: /* TreeNodeData */, isToolTip: /* bool */, colorize: /* bool */, colors: /* IReadOnlyCollection<SpanData<object>> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/TreeViewNodeClassifierContext.cs` (line 30)

### Constructors

- `public TreeViewNodeClassifierContext(string text, ITreeView treeView, TreeNodeData node, bool isToolTip, bool colorize, IReadOnlyCollection<SpanData<object>> colors = null)`
  - Summary: Constructor
  - Parameters:
    - `string text`: Text to classify
    - `ITreeView treeView`: Treeview
    - `TreeNodeData node`: Node to classify
    - `bool isToolTip`: true if the content will be shown in a tooltip
    - `bool colorize`: true if it should be colorized
    - `IReadOnlyCollection<SpanData<object>> colors` (default: `null`): Default colors or null. It doesn't have to be sorted and elements can overlap. The colors must be s or s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/TreeViewNodeClassifierContext.cs` (line 56)

### Properties

- `public ITreeView TreeView { get; }`
  - Summary: Gets the treeview
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/TreeViewNodeClassifierContext.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TreeView;
    ```
- `public TreeNodeData Node { get; }`
  - Summary: Gets the node to classify
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/TreeViewNodeClassifierContext.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Node;
    ```
- `public bool IsToolTip { get; }`
  - Summary: true if the content will be shown in a tooltip
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/Text/TreeViewNodeClassifierContext.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsToolTip;
    ```

