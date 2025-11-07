# Namespace `dnSpy.Contracts.TreeView`

## Class `AsyncNodeProvider`

Creates nodes asynchronously

**Example**

```csharp
var instance = new dnSpy.Contracts.TreeView.AsyncNodeProvider(targetNode: /* TreeNodeData */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 30)

### Constructors

- `protected AsyncNodeProvider(TreeNodeData targetNode)`
  - Summary: Constructor
  - Parameters:
    - `TreeNodeData targetNode`: Target node that will be the parent of the new nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 45)

### Methods

- `protected abstract void ThreadMethod()`
  - Summary: Method that gets called in the worker thread
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 166)
  - Example:
    ```csharp
    // Example invocation
    instance.ThreadMethod();
    ```
- `protected virtual void OnCompleted()`
  - Summary: Called when the async code has stopped
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.OnCompleted();
    ```
- `protected void AddMessageNode(Func<TreeNodeData> create)`
  - Summary: Adds a node with a message
  - Parameters:
    - `Func<TreeNodeData> create`: Creates the message node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.AddMessageNode(create: /* Func<TreeNodeData> */);
    ```
- `protected void AddNode(TreeNodeData node)`
  - Summary: Adds a new node
  - Parameters:
    - `TreeNodeData node`: New node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.AddNode(node: /* TreeNodeData */);
    ```
- `protected void Start()`
  - Summary: Starts the thread
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    instance.Start();
    ```
- `public void Cancel()`
  - Summary: Cancels the async worker
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 171)
  - Example:
    ```csharp
    // Example invocation
    instance.Cancel();
    ```

### Properties

- `public bool CompletedSuccessfully { get; private set; }`
  - Summary: true if it completed successfully
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 140)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CompletedSuccessfully;
    ```
- `public bool IsRunning { get; private set; }`
  - Summary: true if it's still running
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 145)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRunning;
    ```

### Fields

- `protected readonly CancellationToken cancellationToken`
  - Summary: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/AsyncNodeProvider.cs` (line 34)
  - Example:
    ```csharp
    var value = instance.cancellationToken;
    ```

## Class `ExportTreeNodeDataProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `ITreeNodeDataProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.TreeView.ExportTreeNodeDataProviderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeDataProvider.cs` (line 49)

### Constructors

- `public ExportTreeNodeDataProviderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeDataProvider.cs` (line 52)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeDataProvider.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string Guid { get; set; }`
  - Summary: Guid of owner that will receive the new nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeDataProvider.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```

## Interface `IMDTokenNode`

Holds a reference with a token

**Example**

```csharp
// Instantiate dnSpy.Contracts.TreeView.IMDTokenNode and call its members.
var instance = new dnSpy.Contracts.TreeView.IMDTokenNode(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/IMDTokenNode.cs` (line 26)

### Properties

- `IMDTokenProvider Reference { get; }`
  - Summary: Gets the reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/IMDTokenNode.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reference;
    ```

## Interface `ITreeNode`

A tree node

**Example**

```csharp
// Instantiate dnSpy.Contracts.TreeView.ITreeNode and call its members.
var instance = new dnSpy.Contracts.TreeView.ITreeNode(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 26)

### Methods

- `IEnumerable<ITreeNode> Descendants()`
  - Summary: Gets all descendants
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.Descendants();
    ```
- `IEnumerable<ITreeNode> DescendantsAndSelf()`
  - Summary: Gets all descendants including itself
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.DescendantsAndSelf();
    ```
- `void AddChild(ITreeNode node)`
  - Summary: Adds a new node to
  - Parameters:
    - `ITreeNode node`: Node to insert
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.AddChild(node: /* ITreeNode */);
    ```
- `void EnsureChildrenLoaded()`
  - Summary: Forces loading of
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.EnsureChildrenLoaded();
    ```
- `void RefreshUI()`
  - Summary: Refreshes the UI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.RefreshUI();
    ```

### Properties

- `IEnumerable<TreeNodeData> DataChildren { get; }`
  - Summary: Gets all children in . See also
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DataChildren;
    ```
- `IList<ITreeNode> Children { get; }`
  - Summary: Gets all children or an empty list if is true. See also
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Children;
    ```
- `ITreeNode Parent { get; }`
  - Summary: Gets the parent or null if it is the root node or if it hasn't been inserted into the treeview yet.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Parent;
    ```
- `ITreeView TreeView { get; }`
  - Summary: Gets the treeview
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TreeView;
    ```
- `TreeNodeData Data { get; }`
  - Summary: Tree node data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```
- `bool IsExpanded { get; set; }`
  - Summary: true if it's expanded
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsExpanded;
    ```
- `bool IsHidden { get; set; }`
  - Summary: true if it's hidden
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsHidden;
    ```
- `bool IsVisible { get; }`
  - Summary: true when this node is not hidden and all parent nodes are expanded and not hidden
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsVisible;
    ```
- `bool LazyLoading { get; set; }`
  - Summary: Gets/sets lazy loading of children. When true, will get called to load the children. Should only be used by
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNode.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LazyLoading;
    ```

## Interface `ITreeNodeDataProvider`

Creates . Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.TreeView.ITreeNodeDataProvider and call its members.
var instance = new dnSpy.Contracts.TreeView.ITreeNodeDataProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeDataProvider.cs` (line 29)

### Methods

- `IEnumerable<TreeNodeData> Create(TreeNodeDataProviderContext context)`
  - Summary: Creates new
  - Parameters:
    - `TreeNodeDataProviderContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeDataProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(context: /* TreeNodeDataProviderContext */);
    ```

## Interface `ITreeNodeDataProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.TreeView.ITreeNodeDataProviderMetadata and call its members.
var instance = new dnSpy.Contracts.TreeView.ITreeNodeDataProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeDataProvider.cs` (line 39)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeDataProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string Guid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeDataProvider.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```

## Interface `ITreeNodeGroup`

Tree node group

**Inherits/Implements:** `IComparer<TreeNodeData>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.TreeView.ITreeNodeGroup and call its members.
var instance = new dnSpy.Contracts.TreeView.ITreeNodeGroup(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeGroup.cs` (line 26)

### Properties

- `double Order { get; }`
  - Summary: Order of group relative to other groups
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeNodeGroup.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `ITreeView`

A treeview

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.TreeView.ITreeView and call its members.
var instance = new dnSpy.Contracts.TreeView.ITreeView(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 28)

### Methods

- `ITreeNode Create(TreeNodeData data)`
  - Summary: Creates a new instance that can be inserted into this, and only this, treeview.
  - Parameters:
    - `TreeNodeData data`: User data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(data: /* TreeNodeData */);
    ```
- `TreeNodeData FromImplNode(object selectedItem)`
  - Summary: Converts the selected item to a . Should rarely be called.
  - Parameters:
    - `object selectedItem`: Selected item
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    instance.FromImplNode(selectedItem: /* object */);
    ```
- `object ToImplNode(TreeNodeData node)`
  - Summary: Converts to the real tree node
  - Parameters:
    - `TreeNodeData node`: Node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.ToImplNode(node: /* TreeNodeData */);
    ```
- `void CollapseUnusedNodes()`
  - Summary: Collapses all unselected nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 120)
  - Example:
    ```csharp
    // Example invocation
    instance.CollapseUnusedNodes();
    ```
- `void Focus()`
  - Summary: Focuses the treeview, possibly getting keyboard focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.Focus();
    ```
- `void RefreshAllNodes()`
  - Summary: Calls all nodes' method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.RefreshAllNodes();
    ```
- `void ScrollIntoView()`
  - Summary: Scrolls the current node into view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollIntoView();
    ```
- `void SelectAll()`
  - Summary: Selects all visible items
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectAll();
    ```
- `void SelectItems(IEnumerable<TreeNodeData> items)`
  - Summary: Select items
  - Parameters:
    - `IEnumerable<TreeNodeData> items`: Items to select
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectItems(items: /* IEnumerable<TreeNodeData> */);
    ```

### Properties

- `Control UIObject { get; }`
  - Summary: Gets the treeview UI object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIObject;
    ```
- `Guid Guid { get; }`
  - Summary: Guid of this treeview
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `ITreeNode Root { get; }`
  - Summary: Gets the invisible root node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Root;
    ```
- `TreeNodeData SelectedItem { get; }`
  - Summary: Gets the selected node or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectedItem;
    ```
- `TreeNodeData[] SelectedItems { get; }`
  - Summary: Gets all selected items
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectedItems;
    ```
- `TreeNodeData[] TopLevelSelection { get; }`
  - Summary: Gets the selected items which don't have any of their ancestors selected
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TopLevelSelection;
    ```

### Events

- `event EventHandler<TreeViewNodeRemovedEventArgs> NodeRemoved`
  - Summary: Raised when a node has been removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 71)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.NodeRemoved += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<TreeViewSelectionChangedEventArgs> SelectionChanged`
  - Summary: Raised when selection has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeView.cs` (line 66)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.SelectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `ITreeViewListener`

Gets notified by the

**Example**

```csharp
// Instantiate dnSpy.Contracts.TreeView.ITreeViewListener and call its members.
var instance = new dnSpy.Contracts.TreeView.ITreeViewListener(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeViewListener.cs` (line 24)

### Methods

- `void OnEvent(ITreeView treeView, TreeViewListenerEventArgs e)`
  - Summary: Called at various times
  - Parameters:
    - `ITreeView treeView`: Sender
    - `TreeViewListenerEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeViewListener.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.OnEvent(treeView: /* ITreeView */, e: /* TreeViewListenerEventArgs */);
    ```

## Interface `ITreeViewService`

Treeview manager

**Example**

```csharp
// Instantiate dnSpy.Contracts.TreeView.ITreeViewService and call its members.
var instance = new dnSpy.Contracts.TreeView.ITreeViewService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeViewService.cs` (line 26)

### Methods

- `ITreeView Create(Guid guid, TreeViewOptions options)`
  - Summary: Creates a instance. Its method must be called to destroy it.
  - Parameters:
    - `Guid guid`: Guid of treeview
    - `TreeViewOptions options`: Treeview options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/ITreeViewService.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(guid: /* Guid */, options: /* TreeViewOptions */);
    ```

## Class `TreeNodeData`

Treenode data base class

**Example**

```csharp
var instance = new dnSpy.Contracts.TreeView.TreeNodeData();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 30)

### Constructors

- `protected TreeNodeData()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 83)

### Methods

- `public abstract void OnRefreshUI()`
  - Summary: Called by before it invalidates all UI properties
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.OnRefreshUI();
    ```
- `public virtual IDataObject Copy(TreeNodeData[] nodes)`
  - Summary: Copies nodes
  - Parameters:
    - `TreeNodeData[] nodes`: Nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 160)
  - Example:
    ```csharp
    // Example invocation
    instance.Copy(nodes: /* TreeNodeData[] */);
    ```
- `public virtual IEnumerable<TreeNodeData> CreateChildren()`
  - Summary: Called when it's time to create its children
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateChildren();
    ```
- `public virtual bool Activate()`
  - Summary: Called when the item gets activated, eg. double clicked. Returns true if it was handled, false otherwise.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 116)
  - Example:
    ```csharp
    // Example invocation
    instance.Activate();
    ```
- `public virtual bool CanDrag(TreeNodeData[] nodes)`
  - Summary: Returns true if the nodes can be dragged
  - Parameters:
    - `TreeNodeData[] nodes`: Nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.CanDrag(nodes: /* TreeNodeData[] */);
    ```
- `public virtual bool CanDrop(DragEventArgs e, int index)`
  - Summary: Returns true if drop can execute
  - Parameters:
    - `DragEventArgs e`: Event args
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 168)
  - Example:
    ```csharp
    // Example invocation
    instance.CanDrop(e: /* DragEventArgs */, index: /* int */);
    ```
- `public virtual bool ShowExpander(bool defaultValue)`
  - Summary: Returns true if the expander should be shown
  - Parameters:
    - `bool defaultValue`: Default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowExpander(defaultValue: /* bool */);
    ```
- `public virtual void Drop(DragEventArgs e, int index)`
  - Summary: Drops data
  - Parameters:
    - `DragEventArgs e`: Event args
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.Drop(e: /* DragEventArgs */, index: /* int */);
    ```
- `public virtual void Initialize()`
  - Summary: Called after has been set.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    instance.Initialize();
    ```
- `public virtual void OnChildrenChanged(TreeNodeData[] added, TreeNodeData[] removed)`
  - Summary: Called when the children has changed
  - Parameters:
    - `TreeNodeData[] added`: Added nodes
    - `TreeNodeData[] removed`: Removed nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 128)
  - Example:
    ```csharp
    // Example invocation
    instance.OnChildrenChanged(added: /* TreeNodeData[] */, removed: /* TreeNodeData[] */);
    ```
- `public virtual void OnEnsureChildrenLoaded()`
  - Summary: Called by
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.OnEnsureChildrenLoaded();
    ```
- `public virtual void OnIsExpandedChanged(bool isExpanded)`
  - Summary: Called when has changed
  - Parameters:
    - `bool isExpanded`: Value of
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.OnIsExpandedChanged(isExpanded: /* bool */);
    ```
- `public virtual void OnIsVisibleChanged()`
  - Summary: Called when has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.OnIsVisibleChanged();
    ```
- `public virtual void StartDrag(DependencyObject dragSource, TreeNodeData[] nodes)`
  - Summary: Starts the drag and drop operation
  - Parameters:
    - `DependencyObject dragSource`: Drag source
    - `TreeNodeData[] nodes`: Nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.StartDrag(dragSource: /* DependencyObject */, nodes: /* TreeNodeData[] */);
    ```

### Properties

- `public ITreeNode TreeNode {
			get => treeNode;
			set {
				if (treeNode != null)
					throw new InvalidOperationException();
				treeNode = value ?? throw new ArgumentNullException(nameof(value));
			}
		}`
  - Summary: Gets the owner instance. Only the treeview may write to this property.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TreeNode;
    ```
- `public abstract Guid Guid { get; }`
  - Summary: Guid of this node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public abstract ImageReference Icon { get; }`
  - Summary: Icon
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Icon;
    ```
- `public abstract object Text { get; }`
  - Summary: Gets the data shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```
- `public abstract object ToolTip { get; }`
  - Summary: Gets the data shown in a tooltip
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTip;
    ```
- `public virtual ITreeNodeGroup TreeNodeGroup => null`
  - Summary: Group or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TreeNodeGroup;
    ```
- `public virtual ImageReference? ExpandedIcon => null`
  - Summary: Expanded icon or null to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExpandedIcon;
    ```
- `public virtual bool SingleClickExpandsChildren => false`
  - Summary: true if single clicking on a node expands all its children
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SingleClickExpandsChildren;
    ```

## Class `TreeNodeDataExtensionMethods`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.TreeView.TreeNodeDataExtensionMethods members directly without instantiation.
dnSpy.Contracts.TreeView.TreeNodeDataExtensionMethods./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 181)

### Methods

- `public static IEnumerable<TreeNodeData> Descendants(this TreeNodeData self)`
  - Summary: Gets all descendants
  - Parameters:
    - `this TreeNodeData self`: This
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.TreeView.TreeNodeDataExtensionMethods.Descendants(self: /* TreeNodeData */);
    ```
- `public static IEnumerable<TreeNodeData> DescendantsAndSelf(this TreeNodeData self)`
  - Summary: Gets all descendants including itself
  - Parameters:
    - `this TreeNodeData self`: This
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 194)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.TreeView.TreeNodeDataExtensionMethods.DescendantsAndSelf(self: /* TreeNodeData */);
    ```
- `public static T GetAncestorOrSelf<T>(this TreeNodeData self) where T : TreeNodeData`
  - Summary: Gets the ancestor of a certain type
  - Parameters:
    - `this TreeNodeData self`: This
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeData.cs` (line 202)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.TreeView.TreeNodeDataExtensionMethods.GetAncestorOrSelf(self: /* TreeNodeData */);
    ```

## Class `TreeNodeDataProviderContext`

context

**Example**

```csharp
var instance = new dnSpy.Contracts.TreeView.TreeNodeDataProviderContext(owner: /* ITreeNode */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeDataProviderContext.cs` (line 24)

### Constructors

- `public TreeNodeDataProviderContext(ITreeNode owner)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNode owner`: Owner
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeDataProviderContext.cs` (line 34)

### Properties

- `public ITreeNode Owner { get; }`
  - Summary: Owner of new
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeNodeDataProviderContext.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Owner;
    ```

## Class `TreeViewConstants`

Treeview constants

**Example**

```csharp
// Access dnSpy.Contracts.TreeView.TreeViewConstants members directly without instantiation.
dnSpy.Contracts.TreeView.TreeViewConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewConstants.cs` (line 24)

### Fields

- `public static readonly string DOCUMENT_TREEVIEW_GUID = "47F487E1-64D1-4D63-87C6-B4C4F89461A3"`
  - Summary: Guid of documents treeview
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewConstants.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.TreeView.TreeViewConstants.DOCUMENT_TREEVIEW_GUID;
    ```

## Enum `TreeViewListenerEvent`

event

**Example**

```csharp
// Instantiate dnSpy.Contracts.TreeView.TreeViewListenerEvent and call its members.
var instance = new dnSpy.Contracts.TreeView.TreeViewListenerEvent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewListenerEvent.cs` (line 24)

### Members

- `NodeCreated`: A new node was created. is a

## Class `TreeViewListenerEventArgs`

event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.TreeView.TreeViewListenerEventArgs(@event: /* TreeViewListenerEvent */, arg: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewListenerEventArgs.cs` (line 26)

### Constructors

- `public TreeViewListenerEventArgs(TreeViewListenerEvent @event, object arg)`
  - Summary: Constructor
  - Parameters:
    - `TreeViewListenerEvent @event`: Description not provided.
    - `object arg`: Argument
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewListenerEventArgs.cs` (line 42)

### Properties

- `public TreeViewListenerEvent Event { get; }`
  - Summary: Event type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewListenerEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Event;
    ```
- `public object Argument { get; }`
  - Summary: Argument, see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewListenerEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Argument;
    ```

## Class `TreeViewNodeRemovedEventArgs`

Node removed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.TreeView.TreeViewNodeRemovedEventArgs(node: /* TreeNodeData */, removed: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewNodeRemovedEventArgs.cs` (line 26)

### Constructors

- `public TreeViewNodeRemovedEventArgs(TreeNodeData node, bool removed)`
  - Summary: Constructor
  - Parameters:
    - `TreeNodeData node`: Node
    - `bool removed`: true if it was removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewNodeRemovedEventArgs.cs` (line 42)

### Properties

- `public TreeNodeData Node { get; }`
  - Summary: The node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewNodeRemovedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Node;
    ```
- `public bool Removed { get; }`
  - Summary: true if was removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewNodeRemovedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Removed;
    ```

## Class `TreeViewOptions`

Treeview options

**Example**

```csharp
var instance = new dnSpy.Contracts.TreeView.TreeViewOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 27)

### Constructors

- `public TreeViewOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 76)

### Properties

- `public ITreeViewListener TreeViewListener { get; set; }`
  - Summary: listener
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TreeViewListener;
    ```
- `public SelectionMode SelectionMode { get; set; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectionMode;
    ```
- `public TreeNodeData RootNode { get; set; }`
  - Summary: The root node or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RootNode;
    ```
- `public VirtualizationMode VirtualizationMode { get; set; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VirtualizationMode;
    ```
- `public bool AllowDrop { get; set; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AllowDrop;
    ```
- `public bool CanDragAndDrop { get; set; }`
  - Summary: true if drag and drop is possible
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanDragAndDrop;
    ```
- `public bool IsGridView { get; set; }`
  - Summary: true if it's a grid view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsGridView;
    ```
- `public bool IsVirtualizing { get; set; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsVirtualizing;
    ```
- `public object ForegroundBrushResourceKey { get; set; }`
  - Summary: Foreground brush resource key or null to use the default color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewOptions.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ForegroundBrushResourceKey;
    ```

## Class `TreeViewSelectionChangedEventArgs`

Selection changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.TreeView.TreeViewSelectionChangedEventArgs(added: /* TreeNodeData[] */, removed: /* TreeNodeData[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewSelectionChangedEventArgs.cs` (line 26)

### Constructors

- `public TreeViewSelectionChangedEventArgs(TreeNodeData[] added, TreeNodeData[] removed)`
  - Summary: Constructor
  - Parameters:
    - `TreeNodeData[] added`: Added nodes or null
    - `TreeNodeData[] removed`: Removed nodes or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewSelectionChangedEventArgs.cs` (line 42)

### Properties

- `public TreeNodeData[] Added { get; }`
  - Summary: Added nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewSelectionChangedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Added;
    ```
- `public TreeNodeData[] Removed { get; }`
  - Summary: Removed nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/TreeView/TreeViewSelectionChangedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Removed;
    ```

