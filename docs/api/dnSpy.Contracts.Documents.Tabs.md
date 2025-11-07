# Namespace `dnSpy.Contracts.Documents.Tabs`

## Class `AsyncDocumentTabContent`

that creates its output asynchronously in another thread

**Inherits/Implements:** `DocumentTabContent`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.AsyncDocumentTabContent and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.AsyncDocumentTabContent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/AsyncDocumentTabContent.cs` (line 26)

### Methods

- `public abstract Task CreateContentAsync(IAsyncShowContext ctx)`
  - Summary: Called in the worker thread
  - Parameters:
    - `IAsyncShowContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/AsyncDocumentTabContent.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateContentAsync(ctx: /* IAsyncShowContext */);
    ```
- `public abstract bool NeedAsyncWork(IShowContext ctx)`
  - Summary: Returns true if should be called
  - Parameters:
    - `IShowContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/AsyncDocumentTabContent.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.NeedAsyncWork(ctx: /* IShowContext */);
    ```
- `public abstract void OnShowAsync(IShowContext ctx, IAsyncShowResult result)`
  - Summary: Called in the main UI thread after the worker thread has exited or was interrupted
  - Parameters:
    - `IShowContext ctx`: Context
    - `IAsyncShowResult result`: Result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/AsyncDocumentTabContent.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.OnShowAsync(ctx: /* IShowContext */, result: /* IAsyncShowResult */);
    ```

## Class `DefaultDocumentTabContentProviderConstants`

constants

**Example**

```csharp
// Access dnSpy.Contracts.Documents.Tabs.DefaultDocumentTabContentProviderConstants members directly without instantiation.
dnSpy.Contracts.Documents.Tabs.DefaultDocumentTabContentProviderConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DefaultDocumentTabContentProviderConstants.cs` (line 24)

### Fields

- `public const double DEFAULT_HANDLER = 1000000`
  - Summary: Order of default instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DefaultDocumentTabContentProviderConstants.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DefaultDocumentTabContentProviderConstants.DEFAULT_HANDLER;
    ```

## Class `DocumentModifiedEventArgs`

Document modified event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocumentModifiedEventArgs(documents: /* IDsDocument[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentModifiedEventArgs.cs` (line 26)

### Constructors

- `public DocumentModifiedEventArgs(IDsDocument[] documents)`
  - Summary: Constructor
  - Parameters:
    - `IDsDocument[] documents`: Documents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentModifiedEventArgs.cs` (line 36)

### Properties

- `public IDsDocument[] Documents { get; }`
  - Summary: Gets the modified documents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentModifiedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Documents;
    ```

## Class `DocumentTabContent`

Contains the data used to generate the content shown in a tab. If it implements , it gets disposed when it's no longer in use.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocumentTabContent and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocumentTabContent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 29)

### Methods

- `public abstract DocumentTabContent Clone()`
  - Summary: Clones this instance. Can only be called if is true
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```
- `public abstract DocumentTabUIContext CreateUIContext(IDocumentTabUIContextLocator locator)`
  - Summary: Creates the instance needed by this instance. This instance will only be used in this tab.
  - Parameters:
    - `IDocumentTabUIContextLocator locator`: Can be used to get a per-tab shared instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateUIContext(locator: /* IDocumentTabUIContextLocator */);
    ```
- `public virtual void OnHide()`
  - Summary: Called when the content is hidden
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.OnHide();
    ```
- `public virtual void OnSelected()`
  - Summary: Called when its tab has been selected. Only called if this is the tab's active content.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.OnSelected();
    ```
- `public virtual void OnShow(IShowContext ctx)`
  - Summary: Called to show its content in the UI. Derive from to create the content in a worker thread.
  - Parameters:
    - `IShowContext ctx`: UI Context created by
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.OnShow(ctx: /* IShowContext */);
    ```
- `public virtual void OnUnselected()`
  - Summary: Called when its tab has been unselected. Only called if this is the tab's active content.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.OnUnselected();
    ```

### Properties

- `public IDocumentTab DocumentTab {
			get => documentTab;
			set {
				if (value == null)
					throw new ArgumentNullException(nameof(value));
				if (documentTab == null)
					documentTab = value;
				else if (documentTab != value)
					throw new InvalidOperationException();
			}
		}`
  - Summary: Written by the owner instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 90)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentTab;
    ```
- `public abstract string Title { get; }`
  - Summary: Gets the title
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Title;
    ```
- `public virtual IEnumerable<DocumentTreeNodeData> Nodes => Array.Empty<DocumentTreeNodeData>()`
  - Summary: Gets all nodes used to generate the content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Nodes;
    ```
- `public virtual bool CanClone => true`
  - Summary: true if can be called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanClone;
    ```
- `public virtual object ToolTip => null`
  - Summary: Gets the tooltip or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabContent.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTip;
    ```

## Class `DocumentTabExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Documents.Tabs.DocumentTabExtensions members directly without instantiation.
dnSpy.Contracts.Documents.Tabs.DocumentTabExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 141)

### Methods

- `public static IDocumentViewer TryGetDocumentViewer(this IDocumentTab tab)`
  - Summary: Returns the tab's or null if it's not visible
  - Parameters:
    - `this IDocumentTab tab`: Tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 147)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.Tabs.DocumentTabExtensions.TryGetDocumentViewer(tab: /* IDocumentTab */);
    ```

## Class `DocumentTabReferenceResult`

Created by

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocumentTabReferenceResult(documentTabContent: /* DocumentTabContent */, uiState: /* object */, onShownHandler: /* Action<ShowTabContentEventArgs> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabReferenceResult.cs` (line 26)

### Constructors

- `public DocumentTabReferenceResult(DocumentTabContent documentTabContent, object uiState = null, Action<ShowTabContentEventArgs> onShownHandler = null)`
  - Summary: Constructor
  - Parameters:
    - `DocumentTabContent documentTabContent`: New content
    - `object uiState` (default: `null`): UI state (passed to ) or null
    - `Action<ShowTabContentEventArgs> onShownHandler` (default: `null`): Handler or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabReferenceResult.cs` (line 48)

### Properties

- `public Action<ShowTabContentEventArgs> OnShownHandler { get; }`
  - Summary: Called when the output has been shown, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabReferenceResult.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OnShownHandler;
    ```
- `public DocumentTabContent DocumentTabContent { get; }`
  - Summary: New tab content, never null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabReferenceResult.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentTabContent;
    ```
- `public object UIState { get; }`
  - Summary: UI state (passed to ) or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabReferenceResult.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIState;
    ```

## Class `DocumentTabUIContext`

UI content shared by some instances, eg. it could contain the text editor. Only one instance per tab is allocated and stored in a . Implement to get called when the tab is removed (only called if this instance hasn't been GC'd)

**Inherits/Implements:** `IUIObjectProvider`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocumentTabUIContext and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocumentTabUIContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 32)

### Methods

- `public virtual object CreateUIState()`
  - Summary: Saves UI state, eg. line number, caret position, etc
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateUIState();
    ```
- `public virtual object DeserializeUIState(ISettingsSection section)`
  - Summary: Creates UI state from serialized data
  - Parameters:
    - `ISettingsSection section`: Serialized data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.DeserializeUIState(section: /* ISettingsSection */);
    ```
- `public virtual void OnHide()`
  - Summary: Called when another instance will be shown
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.OnHide();
    ```
- `public virtual void OnShow()`
  - Summary: Called when this instance will be shown in a tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.OnShow();
    ```
- `public virtual void RestoreUIState(object obj)`
  - Summary: Restores UI state. was created by but could also be null or an invalid value. The callee is responsible for verifying .
  - Parameters:
    - `object obj`: Serialized UI state
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.RestoreUIState(obj: /* object */);
    ```
- `public virtual void SerializeUIState(ISettingsSection section, object obj)`
  - Summary: Saves UI state to . was created by but should be verified by the callee.
  - Parameters:
    - `ISettingsSection section`: Destination
    - `object obj`: UI state, created by
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.SerializeUIState(section: /* ISettingsSection */, obj: /* object */);
    ```

### Properties

- `public IDocumentTab DocumentTab {
			get => documentTab;
			set {
				if (value == null)
					throw new ArgumentNullException(nameof(value));
				if (documentTab == null)
					documentTab = value;
				else if (documentTab != value)
					throw new InvalidOperationException();
			}
		}`
  - Summary: Gets the owner tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 90)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentTab;
    ```
- `public abstract FrameworkElement ZoomElement { get; }`
  - Summary: Gets the element that gets zoomed or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ZoomElement;
    ```
- `public abstract IInputElement FocusedElement { get; }`
  - Summary: Gets the element that gets focused or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FocusedElement;
    ```
- `public abstract object UIObject { get; }`
  - Summary: Gets the UI object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocumentTabUIContext.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIObject;
    ```

## Class `ExportDefaultDocumentTabContentProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDefaultDocumentTabContentProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.ExportDefaultDocumentTabContentProviderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDefaultDocumentTabContentProvider.cs` (line 46)

### Constructors

- `public ExportDefaultDocumentTabContentProviderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDefaultDocumentTabContentProvider.cs` (line 49)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDefaultDocumentTabContentProvider.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDocumentListListenerAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDocumentListListenerMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.ExportDocumentListListenerAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 70)

### Constructors

- `public ExportDocumentListListenerAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 73)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDocumentTabContentFactoryAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDocumentTabContentFactoryMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.ExportDocumentTabContentFactoryAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactory.cs` (line 66)

### Constructors

- `public ExportDocumentTabContentFactoryAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactory.cs` (line 69)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactory.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDocumentTabUIContextProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDocumentTabUIContextProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.ExportDocumentTabUIContextProviderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextProvider.cs` (line 49)

### Constructors

- `public ExportDocumentTabUIContextProviderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextProvider.cs` (line 52)

### Properties

- `public bool UseStrongReference { get; set; }`
  - Summary: true to store the created instance in a strong reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextProvider.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseStrongReference;
    ```
- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextProvider.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportReferenceDocumentTabContentProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IReferenceDocumentTabContentProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.ExportReferenceDocumentTabContentProviderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceDocumentTabContentProvider.cs` (line 49)

### Constructors

- `public ExportReferenceDocumentTabContentProviderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceDocumentTabContentProvider.cs` (line 52)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceDocumentTabContentProvider.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportReferenceHandlerAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IReferenceHandlerMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.ExportReferenceHandlerAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandler.cs` (line 46)

### Constructors

- `public ExportReferenceHandlerAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandler.cs` (line 50)

### Properties

- `public double Order { get; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandler.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportTabSaverProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `ITabSaverProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.ExportTabSaverProviderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaverProvider.cs` (line 46)

### Constructors

- `public ExportTabSaverProviderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaverProvider.cs` (line 49)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaverProvider.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IAsyncShowContext`

Passed to

**Inherits/Implements:** `IShowContext`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IAsyncShowContext and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IAsyncShowContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IAsyncShowContext.cs` (line 26)

### Methods

- `void Cancel()`
  - Summary: Cancels the operation
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IAsyncShowContext.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Cancel();
    ```

### Properties

- `CancellationToken CancellationToken { get; }`
  - Summary: Gets the cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IAsyncShowContext.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CancellationToken;
    ```

## Interface `IAsyncShowResult`

Result passed to

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IAsyncShowResult and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IAsyncShowResult(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IAsyncShowResult.cs` (line 26)

### Properties

- `Exception Exception { get; }`
  - Summary: The caught exception or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IAsyncShowResult.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Exception;
    ```
- `bool CanShowOutput { get; }`
  - Summary: true if it's still the visible tab and the UI context can be written to. It can be false if the asynchronous operation got canceled by the user.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IAsyncShowResult.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanShowOutput;
    ```
- `bool IsCanceled { get; }`
  - Summary: true if it was canceled (the cancellation token threw an exception)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IAsyncShowResult.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsCanceled;
    ```

## Interface `IDecompilerTabContent`

A that uses a to generate its content

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDecompilerTabContent and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDecompilerTabContent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDecompilerTabContent.cs` (line 26)

### Properties

- `IDecompiler Decompiler { get; set; }`
  - Summary: Gets/sets the language used to generate the content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDecompilerTabContent.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Decompiler;
    ```

## Interface `IDefaultDocumentTabContentProvider`

Creates default document tab content. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDefaultDocumentTabContentProvider and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDefaultDocumentTabContentProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDefaultDocumentTabContentProvider.cs` (line 28)

### Methods

- `DocumentTabContent Create(IDocumentTabService documentTabService)`
  - Summary: Creates default content or returns null
  - Parameters:
    - `IDocumentTabService documentTabService`: Owner
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDefaultDocumentTabContentProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(documentTabService: /* IDocumentTabService */);
    ```

## Interface `IDefaultDocumentTabContentProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDefaultDocumentTabContentProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDefaultDocumentTabContentProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDefaultDocumentTabContentProvider.cs` (line 38)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDefaultDocumentTabContentProvider.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDocumentListListener`

Can cancel loading document lists. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDocumentListListener and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDocumentListListener(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 28)

### Methods

- `bool CheckCanLoad(bool isReload)`
  - Summary: Returns true if the list can be loaded. It's called before and can be used to show a message box to the user. If false is returned, the list isn't loaded.
  - Parameters:
    - `bool isReload`: true if it's reload-list, false if it's load-list
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.CheckCanLoad(isReload: /* bool */);
    ```
- `void AfterLoad(bool isReload)`
  - Summary: Called after a new document list has been loaded
  - Parameters:
    - `bool isReload`: true if it's reload-list, false if it's load-list
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.AfterLoad(isReload: /* bool */);
    ```
- `void BeforeLoad(bool isReload)`
  - Summary: Called before a new document list is loaded
  - Parameters:
    - `bool isReload`: true if it's reload-list, false if it's load-list
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.BeforeLoad(isReload: /* bool */);
    ```

### Properties

- `bool CanLoad { get; }`
  - Summary: true if we can load a new document list
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanLoad;
    ```
- `bool CanReload { get; }`
  - Summary: true if we can reload the current document list
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanReload;
    ```

## Interface `IDocumentListListenerMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDocumentListListenerMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDocumentListListenerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 62)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentListListener.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDocumentTab`

A tab

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDocumentTab and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDocumentTab(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 29)

### Methods

- `void AsyncExec(Action<CancellationTokenSource> preExec, Action asyncAction, Action<IAsyncShowResult> postExec)`
  - Summary: Executes new code, cancelling any other started call
  - Parameters:
    - `Action<CancellationTokenSource> preExec`: Executed in the current thread before the async code has started
    - `Action asyncAction`: Executed in a new thread
    - `Action<IAsyncShowResult> postExec`: Executed in the current thread after has finished executing
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    instance.AsyncExec(preExec: /* Action<CancellationTokenSource> */, asyncAction: /* Action */, postExec: /* Action<IAsyncShowResult> */);
    ```
- `void Close()`
  - Summary: Closes this tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```
- `void DeserializeUI(ISettingsSection tabContentUI)`
  - Summary: Deserializes UI settings serialized by
  - Parameters:
    - `ISettingsSection tabContentUI`: Serialized data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.DeserializeUI(tabContentUI: /* ISettingsSection */);
    ```
- `void FollowReference(object @ref, DocumentTabContent sourceContent = null, Action<ShowTabContentEventArgs> onShown = null)`
  - Summary: Follows a reference
  - Parameters:
    - `object @ref`: Description not provided.
    - `DocumentTabContent sourceContent` (default: `null`): Source content or null
    - `Action<ShowTabContentEventArgs> onShown` (default: `null`): Called after the content has been shown. Can be null.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.FollowReference(@ref: /* object */, sourceContent: /* DocumentTabContent */, onShown: /* Action<ShowTabContentEventArgs> */);
    ```
- `void FollowReference(object @ref, bool newTab, Action<ShowTabContentEventArgs> onShown = null)`
  - Summary: Follows a reference
  - Parameters:
    - `object @ref`: Description not provided.
    - `bool newTab`: true to open a new tab
    - `Action<ShowTabContentEventArgs> onShown` (default: `null`): Called after the content has been shown. Can be null.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.FollowReference(@ref: /* object */, newTab: /* bool */, onShown: /* Action<ShowTabContentEventArgs> */);
    ```
- `void FollowReferenceNewTab(object @ref, Action<ShowTabContentEventArgs> onShown = null)`
  - Summary: Follows a reference in a new tab
  - Parameters:
    - `object @ref`: Description not provided.
    - `Action<ShowTabContentEventArgs> onShown` (default: `null`): Called after the content has been shown. Can be null.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.FollowReferenceNewTab(@ref: /* object */, onShown: /* Action<ShowTabContentEventArgs> */);
    ```
- `void NavigateBackward()`
  - Summary: Navigates backward in history
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.NavigateBackward();
    ```
- `void NavigateForward()`
  - Summary: Navigates forward in history
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.NavigateForward();
    ```
- `void SerializeUI(ISettingsSection tabContentUI)`
  - Summary: Serializes UI settings
  - Parameters:
    - `ISettingsSection tabContentUI`: Target section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.SerializeUI(tabContentUI: /* ISettingsSection */);
    ```
- `void Show(DocumentTabContent tabContent, object uiState, Action<ShowTabContentEventArgs> onShown)`
  - Summary: Shows the tab content
  - Parameters:
    - `DocumentTabContent tabContent`: Tab content
    - `object uiState`: UI state (passed to ) or null
    - `Action<ShowTabContentEventArgs> onShown`: Called after the output has been shown on the screen
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(tabContent: /* DocumentTabContent */, uiState: /* object */, onShown: /* Action<ShowTabContentEventArgs> */);
    ```
- `void TrySetFocus()`
  - Summary: Sets focus to the focused element if this is the active tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 116)
  - Example:
    ```csharp
    // Example invocation
    instance.TrySetFocus();
    ```

### Properties

- `DocumentTabContent Content { get; }`
  - Summary: Current instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Content;
    ```
- `DocumentTabUIContext UIContext { get; }`
  - Summary: Current
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIContext;
    ```
- `IDocumentTabService DocumentTabService { get; }`
  - Summary: Gets the owner
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentTabService;
    ```
- `bool CanNavigateBackward { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanNavigateBackward;
    ```
- `bool CanNavigateForward { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanNavigateForward;
    ```
- `bool IsActiveTab { get; }`
  - Summary: true if this is the active tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsActiveTab;
    ```
- `bool IsAsyncExecInProgress { get; }`
  - Summary: true if hasn't finished executing
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTab.cs` (line 126)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAsyncExecInProgress;
    ```

## Interface `IDocumentTabContentFactory`

factory. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDocumentTabContentFactory and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDocumentTabContentFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactory.cs` (line 29)

### Methods

- `DocumentTabContent Create(IDocumentTabContentFactoryContext context)`
  - Summary: Creates a instance or returns null
  - Parameters:
    - `IDocumentTabContentFactoryContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactory.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(context: /* IDocumentTabContentFactoryContext */);
    ```
- `DocumentTabContent Deserialize(Guid guid, ISettingsSection section, IDocumentTabContentFactoryContext context)`
  - Summary: Deserializes a instance. Returns null if isn't supported.
  - Parameters:
    - `Guid guid`: Guid, this is the return value of
    - `ISettingsSection section`: Section with serialized content
    - `IDocumentTabContentFactoryContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactory.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.Deserialize(guid: /* Guid */, section: /* ISettingsSection */, context: /* IDocumentTabContentFactoryContext */);
    ```
- `Guid? Serialize(DocumentTabContent content, ISettingsSection section)`
  - Summary: Serializes a instance. Returns a unique guid if it was serialized, else null
  - Parameters:
    - `DocumentTabContent content`: Content
    - `ISettingsSection section`: Section to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactory.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.Serialize(content: /* DocumentTabContent */, section: /* ISettingsSection */);
    ```

## Interface `IDocumentTabContentFactoryContext`

context

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDocumentTabContentFactoryContext and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDocumentTabContentFactoryContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactoryContext.cs` (line 26)

### Properties

- `DocumentTreeNodeData[] Nodes { get; }`
  - Summary: Gets all nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactoryContext.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Nodes;
    ```

## Interface `IDocumentTabContentFactoryMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDocumentTabContentFactoryMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDocumentTabContentFactoryMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactory.cs` (line 58)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabContentFactory.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDocumentTabService`

Manages the document tabs and treeview

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDocumentTabService and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDocumentTabService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 29)

### Methods

- `DocumentTabContent TryCreateContent(DocumentTreeNodeData[] nodes)`
  - Summary: Creates a new instance. Returns null if it couldn't be created
  - Parameters:
    - `DocumentTreeNodeData[] nodes`: Nodes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.TryCreateContent(nodes: /* DocumentTreeNodeData[] */);
    ```
- `IDocumentTab GetOrCreateActiveTab()`
  - Summary: Gets the active tab or creates a new one if is null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateActiveTab();
    ```
- `IDocumentTab OpenEmptyTab()`
  - Summary: Opens a new empty tab and sets it as the active tab ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.OpenEmptyTab();
    ```
- `IDocumentTab TryGetDocumentTab(ITabContent content)`
  - Summary: Tries to get the
  - Parameters:
    - `ITabContent content`: Tab content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetDocumentTab(content: /* ITabContent */);
    ```
- `bool Owns(ITabGroup tabGroup)`
  - Summary: Returns true if is owned by this instance
  - Parameters:
    - `ITabGroup tabGroup`: Tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 112)
  - Example:
    ```csharp
    // Example invocation
    instance.Owns(tabGroup: /* ITabGroup */);
    ```
- `void Close(IDocumentTab tab)`
  - Summary: Closes the tab
  - Parameters:
    - `IDocumentTab tab`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 118)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(tab: /* IDocumentTab */);
    ```
- `void CloseAll()`
  - Summary: Closes all tabs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseAll();
    ```
- `void FollowReference(object @ref, bool newTab = false, bool setFocus = true, Action<ShowTabContentEventArgs> onShown = null)`
  - Summary: Follows the reference in the active tab or a new tab
  - Parameters:
    - `object @ref`: Description not provided.
    - `bool newTab` (default: `false`): true to open a new tab
    - `bool setFocus` (default: `true`): true to give the tab keyboard focus
    - `Action<ShowTabContentEventArgs> onShown` (default: `null`): Called after the content has been shown. Can be null.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.FollowReference(@ref: /* object */, newTab: /* bool */, setFocus: /* bool */, onShown: /* Action<ShowTabContentEventArgs> */);
    ```
- `void Refresh(IEnumerable<IDocumentTab> tabs)`
  - Summary: Forces a refresh of the selected tabs
  - Parameters:
    - `IEnumerable<IDocumentTab> tabs`: Tabs to refresh
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Refresh(tabs: /* IEnumerable<IDocumentTab> */);
    ```
- `void Refresh(Predicate<DocumentTreeNodeData> pred)`
  - Summary: Refreshes all tabs that contain certain nodes
  - Parameters:
    - `Predicate<DocumentTreeNodeData> pred`: Returns true if the node should be included
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.Refresh(pred: /* Predicate<DocumentTreeNodeData> */);
    ```
- `void Refresh<T>() where T : DocumentTreeNodeData`
  - Summary: Refreshes all tabs that contain nodes of type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.Refresh();
    ```
- `void RefreshModifiedDocument(IDsDocument document)`
  - Summary: Refreshes all tabs that use
  - Parameters:
    - `IDsDocument document`: Modified document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.RefreshModifiedDocument(document: /* IDsDocument */);
    ```
- `void SetFocus(IDocumentTab tab)`
  - Summary: Gives keyboard focus
  - Parameters:
    - `IDocumentTab tab`: Tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.SetFocus(tab: /* IDocumentTab */);
    ```

### Properties

- `IDocumentTab ActiveTab { get; set; }`
  - Summary: Gets the active tab or null if none, see also
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveTab;
    ```
- `IDocumentTreeView DocumentTreeView { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentTreeView;
    ```
- `IEnumerable<IDocumentTab> SortedTabs { get; }`
  - Summary: Gets all instances
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SortedTabs;
    ```
- `IEnumerable<IDocumentTab> VisibleFirstTabs { get; }`
  - Summary: Same as except that visible tabs are returned first
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VisibleFirstTabs;
    ```
- `ITabGroupService TabGroupService { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabGroupService;
    ```

### Events

- `event EventHandler<DocumentModifiedEventArgs> DocumentModified`
  - Summary: Raised when gets called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 100)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.DocumentModified += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<NotifyDocumentCollectionChangedEventArgs> DocumentCollectionChanged`
  - Summary: Notified when the document collection gets changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabService.cs` (line 105)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.DocumentCollectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IDocumentTabUIContextLocator`

Creates and caches instances. These are only used in a single tab.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDocumentTabUIContextLocator and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDocumentTabUIContextLocator(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextLocator.cs` (line 28)

### Methods

- `T Get<T>() where T : class`
  - Summary: Creates or returns an existing cached instance of a certain type. This instance is cached per tab and is stored in either a or a strong reference (see )
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextLocator.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Get();
    ```
- `T Get<T>(object key, Func<T> creator) where T : class`
  - Summary: Creates or returns an existing cached instance of a certain type. This instance is cached per tab and is stored in a .
  - Parameters:
    - `object key`: Key
    - `Func<T> creator`: Called if the value hasn't been cached or if it has been GC'd
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextLocator.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Get(key: /* object */, creator: /* Func<T> */);
    ```
- `T Get<T>(object key, bool useStrongReference, Func<T> creator) where T : class`
  - Summary: Creates or returns an existing cached instance of a certain type. This instance is cached per tab and is stored in a or a strong reference depending on the value of .
  - Parameters:
    - `object key`: Key
    - `bool useStrongReference`: true to store the result in a strong reference instead of a weak reference
    - `Func<T> creator`: Called if the value hasn't been cached or if it has been GC'd
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextLocator.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.Get(key: /* object */, useStrongReference: /* bool */, creator: /* Func<T> */);
    ```

## Interface `IDocumentTabUIContextProvider`

Creates instances. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDocumentTabUIContextProvider and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDocumentTabUIContextProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextProvider.cs` (line 28)

### Methods

- `DocumentTabUIContext Create<T>() where T : class`
  - Summary: Creates a new instance or returns null if someone else should create it.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

## Interface `IDocumentTabUIContextProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IDocumentTabUIContextProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IDocumentTabUIContextProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextProvider.cs` (line 39)

### Properties

- `bool UseStrongReference { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextProvider.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseStrongReference;
    ```
- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IDocumentTabUIContextProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IReferenceDocumentTabContentProvider`

Creates instances. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IReferenceDocumentTabContentProvider and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IReferenceDocumentTabContentProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceDocumentTabContentProvider.cs` (line 28)

### Methods

- `DocumentTabReferenceResult Create(IDocumentTabService documentTabService, DocumentTabContent sourceContent, object @ref)`
  - Summary: Creates a new or returns null
  - Parameters:
    - `IDocumentTabService documentTabService`: Owner
    - `DocumentTabContent sourceContent`: Source content or null. It's used when showing the reference in a new tab. This would then be the older tab's content.
    - `object @ref`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceDocumentTabContentProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(documentTabService: /* IDocumentTabService */, sourceContent: /* DocumentTabContent */, @ref: /* object */);
    ```

## Interface `IReferenceDocumentTabContentProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IReferenceDocumentTabContentProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IReferenceDocumentTabContentProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceDocumentTabContentProvider.cs` (line 41)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceDocumentTabContentProvider.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IReferenceHandler`

Called when a reference is followed in a tab. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IReferenceHandler and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IReferenceHandler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandler.cs` (line 28)

### Methods

- `bool OnFollowReference(IReferenceHandlerContext context)`
  - Summary: Called when a reference is followed. Returns true if it was handled, otherwise false.
  - Parameters:
    - `IReferenceHandlerContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandler.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.OnFollowReference(context: /* IReferenceHandlerContext */);
    ```

## Interface `IReferenceHandlerContext`

Context passed to

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IReferenceHandlerContext and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IReferenceHandlerContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandlerContext.cs` (line 24)

### Properties

- `DocumentTabContent Content { get; }`
  - Summary: Gets the tab content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandlerContext.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Content;
    ```
- `DocumentTabContent SourceContent { get; }`
  - Summary: Gets the source tab content or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandlerContext.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SourceContent;
    ```
- `object Reference { get; }`
  - Summary: Gets the reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandlerContext.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reference;
    ```

## Interface `IReferenceHandlerMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IReferenceHandlerMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IReferenceHandlerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandler.cs` (line 38)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IReferenceHandler.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `ISaveService`

Saves tabs

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.ISaveService and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.ISaveService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ISaveService.cs` (line 24)

### Methods

- `bool CanSave(IDocumentTab tab)`
  - Summary: Returns true if the tab can be saved
  - Parameters:
    - `IDocumentTab tab`: Tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ISaveService.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.CanSave(tab: /* IDocumentTab */);
    ```
- `string GetMenuHeader(IDocumentTab tab)`
  - Summary: Returns the menu header content, eg. "_Save..."
  - Parameters:
    - `IDocumentTab tab`: Tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ISaveService.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMenuHeader(tab: /* IDocumentTab */);
    ```
- `void Save(IDocumentTab tab)`
  - Summary: Saves the tab. See also
  - Parameters:
    - `IDocumentTab tab`: Tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ISaveService.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Save(tab: /* IDocumentTab */);
    ```

## Interface `IShowContext`

Passed to

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.IShowContext and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.IShowContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IShowContext.cs` (line 26)

### Properties

- `Action<ShowTabContentEventArgs> OnShown { get; set; }`
  - Summary: If non-null, gets called after the content has been shown
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IShowContext.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OnShown;
    ```
- `DocumentTabUIContext UIContext { get; }`
  - Summary: UI Context created by
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IShowContext.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIContext;
    ```
- `bool IsRefresh { get; }`
  - Summary: true if the view is being refreshed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IShowContext.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRefresh;
    ```
- `object Tag { get; set; }`
  - Summary: Can be initialized by the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/IShowContext.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```

## Interface `ITabSaver`

Saves tabs

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.ITabSaver and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.ITabSaver(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaver.cs` (line 24)

### Methods

- `void Save()`
  - Summary: Saves the tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaver.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.Save();
    ```

### Properties

- `bool CanSave { get; }`
  - Summary: true if it can be saved
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaver.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanSave;
    ```
- `string MenuHeader { get; }`
  - Summary: Gets the menu header, eg. "_Save..." or null to use the default "_Save..." string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaver.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MenuHeader;
    ```

## Interface `ITabSaverProvider`

Creates instances. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.ITabSaverProvider and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.ITabSaverProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaverProvider.cs` (line 28)

### Methods

- `ITabSaver Create(IDocumentTab tab)`
  - Summary: Creates a instance or returns null
  - Parameters:
    - `IDocumentTab tab`: Tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaverProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(tab: /* IDocumentTab */);
    ```

## Interface `ITabSaverProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.ITabSaverProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.ITabSaverProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaverProvider.cs` (line 38)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ITabSaverProvider.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ShowTabContentEventArgs`

Show tab content event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.ShowTabContentEventArgs(result: /* ShowTabContentResult */, tab: /* IDocumentTab */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ShowTabContentEventArgs.cs` (line 46)

### Constructors

- `public ShowTabContentEventArgs(ShowTabContentResult result, IDocumentTab tab)`
  - Summary: Constructor
  - Parameters:
    - `ShowTabContentResult result`: Result>
    - `IDocumentTab tab`: Tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ShowTabContentEventArgs.cs` (line 72)

### Properties

- `public IDocumentTab Tab { get; }`
  - Summary: Gets the tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ShowTabContentEventArgs.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tab;
    ```
- `public ShowTabContentResult Result { get; }`
  - Summary: Gets the result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ShowTabContentEventArgs.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Result;
    ```
- `public bool HasMovedCaret { get; set; }`
  - Summary: Set to true if the caret has been moved by a previous handler
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ShowTabContentEventArgs.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasMovedCaret;
    ```
- `public bool Success => Result == ShowTabContentResult.ShowedContent`
  - Summary: true if the content was shown
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ShowTabContentEventArgs.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Success;
    ```

## Enum `ShowTabContentResult`

Result

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.ShowTabContentResult and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.ShowTabContentResult(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/ShowTabContentEventArgs.cs` (line 26)

### Members

- `Failed`: The content failed to be shown, eg. an exception occurred
- `ShowedContent`: Content was shown
- `ReferenceHandler`: A handled it and no new content was shown

## Class `TabConstants`

Constants

**Example**

```csharp
// Access dnSpy.Contracts.Documents.Tabs.TabConstants members directly without instantiation.
dnSpy.Contracts.Documents.Tabs.TabConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 29)

### Fields

- `public const double ORDER_ASMED_HEXVIEWDOCUMENTTABCONTENTFACTORY = 11000`
  - Summary: Order of hex editor instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_ASMED_HEXVIEWDOCUMENTTABCONTENTFACTORY;
    ```
- `public const double ORDER_CONTENTPROVIDER_HEXADDRREF = 2000`
  - Summary: Order of hex instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_CONTENTPROVIDER_HEXADDRREF;
    ```
- `public const double ORDER_CONTENTPROVIDER_HEXTOKENREF = 1000`
  - Summary: Order of hex instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_CONTENTPROVIDER_HEXTOKENREF;
    ```
- `public const double ORDER_CONTENTPROVIDER_NODE = 20000`
  - Summary: Order of instance that creates content from nodes.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 84)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_CONTENTPROVIDER_NODE;
    ```
- `public const double ORDER_CONTENTPROVIDER_TEXTREF = 10000`
  - Summary: Order of default instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 78)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_CONTENTPROVIDER_TEXTREF;
    ```
- `public const double ORDER_DECOMPILEDOCUMENTTABCONTENTFACTORY = double.MaxValue`
  - Summary: Order of decompile instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_DECOMPILEDOCUMENTTABCONTENTFACTORY;
    ```
- `public const double ORDER_DEFAULTDECOMPILENODE = double.MaxValue`
  - Summary: Order of default instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_DEFAULTDECOMPILENODE;
    ```
- `public const double ORDER_DNLIBREFTOOLTIPCONTENTPROVIDER = double.MaxValue`
  - Summary: Order of dnlib reference instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_DNLIBREFTOOLTIPCONTENTPROVIDER;
    ```
- `public const double ORDER_DOCUMENTVIEWERPROVIDER = double.MaxValue`
  - Summary: Order of instance that creates instances
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_DOCUMENTVIEWERPROVIDER;
    ```
- `public const double ORDER_HEXDOCUMENTTABCONTENTFACTORY = 10000`
  - Summary: Order of hex instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_HEXDOCUMENTTABCONTENTFACTORY;
    ```
- `public const double ORDER_HEXTABSAVERPROVIDER = 2000`
  - Summary: Order of hex instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/TabConstants.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.TabConstants.ORDER_HEXTABSAVERPROVIDER;
    ```

