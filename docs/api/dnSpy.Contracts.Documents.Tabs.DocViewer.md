# Namespace `dnSpy.Contracts.Documents.Tabs.DocViewer`

## Class `DocumentViewerAddedEventArgs`

Document viewer added event args

**Inherits/Implements:** `DocumentViewerEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerAddedEventArgs(documentViewer: /* IDocumentViewer */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 137)

### Constructors

- `public DocumentViewerAddedEventArgs(IDocumentViewer documentViewer)`
  - Summary: Constructor
  - Parameters:
    - `IDocumentViewer documentViewer`: instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 147)

### Properties

- `public override DocumentViewerEvent EventType => DocumentViewerEvent.Added`
  - Summary: Returns the event type, which is
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 141)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EventType;
    ```

## Class `DocumentViewerContent`

content

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerContent and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerContent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContent.cs` (line 30)

### Methods

- `public TData GetCustomData<TData>(string id)`
  - Summary: Gets custom data
  - Parameters:
    - `string id`: Key, eg.,
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContent.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCustomData(id: /* string */);
    ```
- `public bool TryGetCustomData<TData>(string id, out TData data)`
  - Summary: Gets custom data. Returns false if it doesn't exist.
  - Parameters:
    - `string id`: Key, eg.,
    - `out TData data`: Updated with data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContent.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetCustomData(id: /* string */, data: /* TData */);
    ```

### Properties

- `public IReadOnlyList<MethodDebugInfo> MethodDebugInfos { get; }`
  - Summary: Gets the method debug info collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContent.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MethodDebugInfos;
    ```
- `public SpanDataCollection<ReferenceInfo> ReferenceCollection { get; }`
  - Summary: Gets the references
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContent.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReferenceCollection;
    ```
- `public string Text { get; }`
  - Summary: Gets the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContent.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Class `DocumentViewerContentDataIds`

Custom data IDs passed to eg.

**Example**

```csharp
// Access dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerContentDataIds members directly without instantiation.
dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerContentDataIds./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContentDataIds.cs` (line 28)

### Fields

- `public const string BlockStructure = "BlockStructure-Content"`
  - Summary: Block structure data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContentDataIds.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerContentDataIds.BlockStructure;
    ```
- `public const string BracePair = "BracePair-Content"`
  - Summary: Brace pair data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContentDataIds.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerContentDataIds.BracePair;
    ```
- `public const string DebugInfo = "DebugInfo-Content"`
  - Summary: Data is a collection ( elements)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContentDataIds.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerContentDataIds.DebugInfo;
    ```
- `public const string LineSeparator = "LineSeparator-Content"`
  - Summary: data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContentDataIds.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerContentDataIds.LineSeparator;
    ```
- `public const string SpanReference = "SpanReference-Content"`
  - Summary: Data is a ( elements)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerContentDataIds.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerContentDataIds.SpanReference;
    ```

## Enum `DocumentViewerEvent`

event

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerEvent and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerEvent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 92)

### Members

- `Added`: Raised when a new instance has been created
- `Removed`: Raised when a instance has been closed
- `GotNewContent`: Raised after the instance got new content (its method was called). It's only raised if the new content is different from the current content. I.e., calling it twice in a row with the same content won't raise this event the second time.

## Class `DocumentViewerEventArgs`

Document viewer event args base class

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerEventArgs(documentViewer: /* IDocumentViewer */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 116)

### Constructors

- `protected DocumentViewerEventArgs(IDocumentViewer documentViewer)`
  - Summary: Constructor
  - Parameters:
    - `IDocumentViewer documentViewer`: instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 131)

### Properties

- `public IDocumentViewer DocumentViewer { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 125)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentViewer;
    ```
- `public abstract DocumentViewerEvent EventType { get; }`
  - Summary: Gets the event type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 120)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EventType;
    ```

## Class `DocumentViewerExtensions`

Extensions

**Example**

```csharp
// Access dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerExtensions members directly without instantiation.
dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerExtensions.cs` (line 27)

### Methods

- `public static IDocumentViewer TryGetDocumentViewer(this ITextBuffer textBuffer)`
  - Summary: Returns a or null
  - Parameters:
    - `this ITextBuffer textBuffer`: Text buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerExtensions.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerExtensions.TryGetDocumentViewer(textBuffer: /* ITextBuffer */);
    ```

## Class `DocumentViewerGotNewContentEventArgs`

New content event args

**Inherits/Implements:** `DocumentViewerEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerGotNewContentEventArgs(documentViewer: /* IDocumentViewer */, content: /* DocumentViewerContent */, contentType: /* IContentType */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 173)

### Constructors

- `public DocumentViewerGotNewContentEventArgs(IDocumentViewer documentViewer, DocumentViewerContent content, IContentType contentType)`
  - Summary: Constructor
  - Parameters:
    - `IDocumentViewer documentViewer`: Document viewer
    - `DocumentViewerContent content`: New content
    - `IContentType contentType`: Content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 195)

### Properties

- `public DocumentViewerContent Content { get; }`
  - Summary: New content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 182)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Content;
    ```
- `public IContentType ContentType { get; }`
  - Summary: New content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 187)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentType;
    ```
- `public override DocumentViewerEvent EventType => DocumentViewerEvent.GotNewContent`
  - Summary: Returns the event type, which is
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 177)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EventType;
    ```

## Class `DocumentViewerListenerConstants`

constants

**Example**

```csharp
// Access dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerListenerConstants members directly without instantiation.
dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerListenerConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerListenerConstants.cs` (line 27)

### Fields

- `public const double ORDER_BLOCKSTRUCTURESERVICE = 5000`
  - Summary: Block structure service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerListenerConstants.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerListenerConstants.ORDER_BLOCKSTRUCTURESERVICE;
    ```
- `public const double ORDER_BRACEPAIRSERVICE = 4000`
  - Summary: Brace pair service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerListenerConstants.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerListenerConstants.ORDER_BRACEPAIRSERVICE;
    ```
- `public const double ORDER_DEBUGGER_METHODLOCALPROVIDER = ORDER_METHODDEBUGSERVICE + 1000`
  - Summary: Debugger: locals (MethodLocalProvider)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerListenerConstants.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerListenerConstants.ORDER_DEBUGGER_METHODLOCALPROVIDER;
    ```
- `public const double ORDER_DEFAULT = double.MaxValue`
  - Summary: Default order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerListenerConstants.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerListenerConstants.ORDER_DEFAULT;
    ```
- `public const double ORDER_GLYPHTEXTMARKERSERVICE = 1000`
  - Summary: Glyph text marker service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerListenerConstants.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerListenerConstants.ORDER_GLYPHTEXTMARKERSERVICE;
    ```
- `public const double ORDER_LINESEPARATORSERVICE = 6000`
  - Summary: Line separator service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerListenerConstants.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerListenerConstants.ORDER_LINESEPARATORSERVICE;
    ```
- `public const double ORDER_METHODDEBUGSERVICE = 2000`
  - Summary: create
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerListenerConstants.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerListenerConstants.ORDER_METHODDEBUGSERVICE;
    ```
- `public const double ORDER_UIELEMENTSERVICE = 7000`
  - Summary: service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/DocumentViewerListenerConstants.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerListenerConstants.ORDER_UIELEMENTSERVICE;
    ```

## Class `DocumentViewerRemovedEventArgs`

Document viewer removed event args

**Inherits/Implements:** `DocumentViewerEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.DocumentViewerRemovedEventArgs(documentViewer: /* IDocumentViewer */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 155)

### Constructors

- `public DocumentViewerRemovedEventArgs(IDocumentViewer documentViewer)`
  - Summary: Constructor
  - Parameters:
    - `IDocumentViewer documentViewer`: instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 165)

### Properties

- `public override DocumentViewerEvent EventType => DocumentViewerEvent.Removed`
  - Summary: Returns the event type, which is
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 159)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EventType;
    ```

## Class `ExportDecompileNodeAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDecompileNodeMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ExportDecompileNodeAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNode.cs` (line 49)

### Constructors

- `public ExportDecompileNodeAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNode.cs` (line 52)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNode.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDecompileNodeCollectionAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDecompileNodeCollectionMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ExportDecompileNodeCollectionAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeCollection.cs` (line 49)

### Constructors

- `public ExportDecompileNodeCollectionAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeCollection.cs` (line 52)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeCollection.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDocumentViewerCustomDataProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDocumentViewerCustomDataProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ExportDocumentViewerCustomDataProviderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataProvider.cs` (line 45)

### Constructors

- `public ExportDocumentViewerCustomDataProviderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataProvider.cs` (line 48)
- `public ExportDocumentViewerCustomDataProviderAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataProvider.cs` (line 54)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataProvider.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDocumentViewerListenerAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDocumentViewerListenerMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ExportDocumentViewerListenerAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 71)

### Constructors

- `public ExportDocumentViewerListenerAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 74)
- `public ExportDocumentViewerListenerAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order of this instance, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 80)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDocumentViewerPostProcessorAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDocumentViewerPostProcessorMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ExportDocumentViewerPostProcessorAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessor.cs` (line 48)

### Constructors

- `public ExportDocumentViewerPostProcessorAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessor.cs` (line 51)
- `public ExportDocumentViewerPostProcessorAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessor.cs` (line 57)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessor.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDocumentViewerReferenceEnablerProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDocumentViewerReferenceEnablerProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ExportDocumentViewerReferenceEnablerProviderAttribute(id: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerReferenceEnablerProvider.cs` (line 47)

### Constructors

- `public ExportDocumentViewerReferenceEnablerProviderAttribute(string id)`
  - Summary: Constructor
  - Parameters:
    - `string id`: Reference id, eg. . This id must equal an id stored in
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerReferenceEnablerProvider.cs` (line 52)

### Properties

- `public string Id { get; }`
  - Summary: Reference id, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerReferenceEnablerProvider.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Interface `IDecompileNode`

Decompiles instances. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileNode and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileNode(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNode.cs` (line 29)

### Methods

- `bool Decompile(IDecompileNodeContext context, DocumentTreeNodeData node)`
  - Summary: Decompiles or returns false if someone else should have a try. This method can be called in any thread.
  - Parameters:
    - `IDecompileNodeContext context`: Context
    - `DocumentTreeNodeData node`: Node to decompile
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNode.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(context: /* IDecompileNodeContext */, node: /* DocumentTreeNodeData */);
    ```

## Interface `IDecompileNodeCollection`

Decompiles instances. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileNodeCollection and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileNodeCollection(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeCollection.cs` (line 29)

### Methods

- `bool Decompile(IDecompileNodeContext context, DocumentTreeNodeData[] nodes)`
  - Summary: Decompiles or returns false if someone else should have a try. This method can be called in any thread
  - Parameters:
    - `IDecompileNodeContext context`: Context
    - `DocumentTreeNodeData[] nodes`: Nodes to decompile
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeCollection.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(context: /* IDecompileNodeContext */, nodes: /* DocumentTreeNodeData[] */);
    ```

## Interface `IDecompileNodeCollectionMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileNodeCollectionMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileNodeCollectionMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeCollection.cs` (line 41)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeCollection.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDecompileNodeContext`

context

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileNodeContext and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileNodeContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeContext.cs` (line 29)

### Methods

- `T UIThread<T>(Func<T> func)`
  - Summary: Executes in the UI thread and waits for it to complete, then returns the result to the caller. This can be used to load the node's property since it can only be loaded in the UI thread.
  - Parameters:
    - `Func<T> func`: Delegate to execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeContext.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.UIThread(func: /* Func<T> */);
    ```

### Properties

- `DecompilationContext DecompilationContext { get; }`
  - Summary: Gets the decompilation context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeContext.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DecompilationContext;
    ```
- `IContentType ContentType { get; set; }`
  - Summary: Sets the content type. See also
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeContext.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentType;
    ```
- `IDecompiler Decompiler { get; }`
  - Summary: Language to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeContext.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Decompiler;
    ```
- `IDecompilerOutput Output { get; }`
  - Summary: Output to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeContext.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Output;
    ```
- `IDocumentWriterService DocumentWriterService { get; }`
  - Summary: Writes some known documents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeContext.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentWriterService;
    ```
- `string ContentTypeString { get; set; }`
  - Summary: Sets the content type. See also
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNodeContext.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentTypeString;
    ```

## Interface `IDecompileNodeMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileNodeMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileNodeMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNode.cs` (line 41)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileNode.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDecompileSelf`

Decompiles itself. Can be implemented by nodes.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileSelf and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDecompileSelf(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileSelf.cs` (line 26)

### Methods

- `bool Decompile(IDecompileNodeContext context)`
  - Summary: Decompiles itself or returns false if someone else should have a try. This method can be called in any thread.
  - Parameters:
    - `IDecompileNodeContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDecompileSelf.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(context: /* IDecompileNodeContext */);
    ```

## Interface `IDocumentViewer`

Document viewer, it also derives from

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewer and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewer(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 34)

### Methods

- `IEnumerable<SpanData<ReferenceInfo>> GetSelectedReferences()`
  - Summary: Gets all references intersecting with the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 122)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSelectedReferences();
    ```
- `bool RestoreReferencePosition(object obj)`
  - Summary: Restores location saved by
  - Parameters:
    - `object obj`: Saved position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 173)
  - Example:
    ```csharp
    // Example invocation
    instance.RestoreReferencePosition(obj: /* object */);
    ```
- `bool SetContent(DocumentViewerContent content, IContentType contentType)`
  - Summary: Sets new content. Returns true if the content got updated, false if the input was identical to the current content.
  - Parameters:
    - `DocumentViewerContent content`: New content
    - `IContentType contentType`: Content type or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.SetContent(content: /* DocumentViewerContent */, contentType: /* IContentType */);
    ```
- `object GetContentData(object key)`
  - Summary: Returns data added by or null if not found
  - Parameters:
    - `object key`: Key
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.GetContentData(key: /* object */);
    ```
- `object SaveReferencePosition()`
  - Summary: Saves current location relative to some reference in the code. Return value can be passed to
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 166)
  - Example:
    ```csharp
    // Example invocation
    instance.SaveReferencePosition();
    ```
- `void AddContentData(object key, object data)`
  - Summary: Adds data that is removed each time gets called with new content.
  - Parameters:
    - `object key`: Key
    - `object data`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.AddContentData(key: /* object */, data: /* object */);
    ```
- `void HideCancelButton()`
  - Summary: Hides the cancel button shown by
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.HideCancelButton();
    ```
- `void MoveCaretToPosition(int position, MoveCaretOptions options = MoveCaretOptions.Focus)`
  - Summary: Moves the caret to a position in the document
  - Parameters:
    - `int position`: Position
    - `MoveCaretOptions options` (default: `MoveCaretOptions.Focus`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 137)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveCaretToPosition(position: /* int */, options: /* MoveCaretOptions */);
    ```
- `void MoveCaretToReference(object @ref, MoveCaretOptions options = MoveCaretOptions.Select | MoveCaretOptions.Focus)`
  - Summary: Moves the caret to a reference, this can be a , or a . Anything else isn't currently supported.
  - Parameters:
    - `object @ref`: Description not provided.
    - `MoveCaretOptions options` (default: `MoveCaretOptions.Select | MoveCaretOptions.Focus`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveCaretToReference(@ref: /* object */, options: /* MoveCaretOptions */);
    ```
- `void MoveCaretToSpan(Span span, MoveCaretOptions options = MoveCaretOptions.Select | MoveCaretOptions.Focus)`
  - Summary: Moves the caret to a span in the document and selects it
  - Parameters:
    - `Span span`: Span
    - `MoveCaretOptions options` (default: `MoveCaretOptions.Select | MoveCaretOptions.Focus`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 152)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveCaretToSpan(span: /* Span */, options: /* MoveCaretOptions */);
    ```
- `void MoveCaretToSpan(SpanData<ReferenceInfo> refInfo, MoveCaretOptions options = MoveCaretOptions.Select | MoveCaretOptions.Focus)`
  - Summary: Moves the caret to a span in the document and selects it
  - Parameters:
    - `SpanData<ReferenceInfo> refInfo`: Reference and span
    - `MoveCaretOptions options` (default: `MoveCaretOptions.Select | MoveCaretOptions.Focus`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 159)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveCaretToSpan(refInfo: /* SpanData<ReferenceInfo> */, options: /* MoveCaretOptions */);
    ```
- `void MoveCaretToSpan(int position, int length, MoveCaretOptions options = MoveCaretOptions.Select | MoveCaretOptions.Focus)`
  - Summary: Moves the caret to a span in the document and selects it
  - Parameters:
    - `int position`: Position
    - `int length`: Length of span
    - `MoveCaretOptions options` (default: `MoveCaretOptions.Select | MoveCaretOptions.Focus`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 145)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveCaretToSpan(position: /* int */, length: /* int */, options: /* MoveCaretOptions */);
    ```
- `void ShowCancelButton(string message, Action onCancel)`
  - Summary: Shows a cancel button. Can be used when decompiling in another thread
  - Parameters:
    - `string message`: Message to show to the user or null
    - `Action onCancel`: Called if the user clicks the cancel button
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowCancelButton(message: /* string */, onCancel: /* Action */);
    ```

### Properties

- `DocumentViewerContent Content { get; }`
  - Summary: Gets the current content (set by )
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Content;
    ```
- `FrameworkElement UIObject { get; }`
  - Summary: Gets the document viewer control
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIObject;
    ```
- `IDocumentTab DocumentTab { get; }`
  - Summary: Gets the owner tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentTab;
    ```
- `IDsWpfTextView TextView { get; }`
  - Summary: Gets the text view. Don't write to the text buffer directly, use to write new text.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextView;
    ```
- `IDsWpfTextViewHost TextViewHost { get; }`
  - Summary: Gets the text view host. Don't write to the text buffer directly, use to write new text.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 85)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewHost;
    ```
- `ITextCaret Caret { get; }`
  - Summary: Gets the caret
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Caret;
    ```
- `ITextSelection Selection { get; }`
  - Summary: Gets the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Selection;
    ```
- `SpanData<ReferenceInfo>? SelectedReference { get; }`
  - Summary: Gets the reference at the caret or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectedReference;
    ```
- `SpanDataCollection<ReferenceInfo> ReferenceCollection { get; }`
  - Summary: Gets the reference collection ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReferenceCollection;
    ```

### Events

- `event EventHandler<DocumentViewerGotNewContentEventArgs> GotNewContent`
  - Summary: Raised after this instance got new content (its method was called). It's only raised if the new content is different from the current content. I.e., calling it twice in a row with the same content won't raise this event the second time. This event is raised before
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 181)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.GotNewContent += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<DocumentViewerRemovedEventArgs> Removed`
  - Summary: Raised when this instance has been closed. This event is raised before
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewer.cs` (line 187)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Removed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IDocumentViewerCustomDataContext`

Context passed to

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerCustomDataContext and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerCustomDataContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataContext.cs` (line 27)

### Methods

- `TData[] GetData<TData>(string id)`
  - Summary: Gets data added by
  - Parameters:
    - `string id`: Key, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataContext.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetData(id: /* string */);
    ```
- `void AddCustomData(string id, object data)`
  - Summary: Adds data that gets stored in
  - Parameters:
    - `string id`: Key, eg.
    - `object data`: Data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataContext.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.AddCustomData(id: /* string */, data: /* object */);
    ```

### Properties

- `IContentType ContentType { get; }`
  - Summary: Gets the content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataContext.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentType;
    ```
- `IDocumentViewer DocumentViewer { get; }`
  - Summary: Gets the document viewer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataContext.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentViewer;
    ```
- `string Text { get; }`
  - Summary: Gets the new text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataContext.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Interface `IDocumentViewerCustomDataProvider`

Uses custom data created by the decompiler and transforms it to some other data. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerCustomDataProvider and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerCustomDataProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataProvider.cs` (line 28)

### Methods

- `void OnCustomData(IDocumentViewerCustomDataContext context)`
  - Summary: Gets called to create data that gets stored in an instance
  - Parameters:
    - `IDocumentViewerCustomDataContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataProvider.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.OnCustomData(context: /* IDocumentViewerCustomDataContext */);
    ```

## Interface `IDocumentViewerCustomDataProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerCustomDataProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerCustomDataProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataProvider.cs` (line 37)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerCustomDataProvider.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDocumentViewerListener`

Gets notified when a document viewer event occurs. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerListener and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerListener(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 54)

### Methods

- `void OnEvent(DocumentViewerEventArgs e)`
  - Summary: Raised when some event occurred
  - Parameters:
    - `DocumentViewerEventArgs e`: Event arguments
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.OnEvent(e: /* DocumentViewerEventArgs */);
    ```

## Interface `IDocumentViewerListenerMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerListenerMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerListenerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 63)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDocumentViewerOutput`

dnSpy text output

**Inherits/Implements:** `IDecompilerOutput`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerOutput and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerOutput(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerOutput.cs` (line 28)

### Methods

- `void AddButton(string buttonText, Action clickHandler)`
  - Summary: Adds a button
  - Parameters:
    - `string buttonText`: Button text
    - `Action clickHandler`: Button click handler
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerOutput.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.AddButton(buttonText: /* string */, clickHandler: /* Action */);
    ```
- `void AddUIElement(Func<UIElement> createElement)`
  - Summary: Adds a UI element
  - Parameters:
    - `Func<UIElement> createElement`: Creates the UI element. Only called on the UI thread
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerOutput.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.AddUIElement(createElement: /* Func<UIElement> */);
    ```
- `void DisableCaching()`
  - Summary: Called to disable caching of the result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerOutput.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.DisableCaching();
    ```

### Properties

- `bool CanBeCached { get; }`
  - Summary: true if the output can be cached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerOutput.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanBeCached;
    ```

## Interface `IDocumentViewerPostProcessor`

Gets a chance to add custom data before creating the content. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerPostProcessor and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerPostProcessor(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessor.cs` (line 29)

### Methods

- `void PostProcess(IDocumentViewerPostProcessorContext context)`
  - Summary: Gets called just before all instances get called. It's possible to call but not to add any text.
  - Parameters:
    - `IDocumentViewerPostProcessorContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessor.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.PostProcess(context: /* IDocumentViewerPostProcessorContext */);
    ```

## Interface `IDocumentViewerPostProcessorContext`

Context passed to

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerPostProcessorContext and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerPostProcessorContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessorContext.cs` (line 26)

### Properties

- `IContentType ContentType { get; }`
  - Summary: Gets the content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessorContext.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentType;
    ```
- `IDocumentViewer DocumentViewer { get; }`
  - Summary: Gets the document viewer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessorContext.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentViewer;
    ```
- `IDocumentViewerOutput DocumentViewerOutput { get; }`
  - Summary: Gets the output. It's not possible to write new text, but custom data can be added.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessorContext.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentViewerOutput;
    ```
- `string Text { get; }`
  - Summary: Gets the new text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessorContext.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Interface `IDocumentViewerPostProcessorMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerPostProcessorMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerPostProcessorMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessor.cs` (line 40)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerPostProcessor.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDocumentViewerReferenceEnabler`

Enables or disables highlighting of references

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerReferenceEnabler and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerReferenceEnabler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerReferenceEnablerProvider.cs` (line 64)

### Properties

- `bool IsEnabled { get; }`
  - Summary: true if the reference is enabled and can be highlighted, false if the reference is disabled and can't be highlighted.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerReferenceEnablerProvider.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnabled;
    ```

### Events

- `event EventHandler IsEnabledChanged`
  - Summary: Raised whenever has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerReferenceEnablerProvider.cs` (line 68)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.IsEnabledChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IDocumentViewerReferenceEnablerProvider`

Creates s. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerReferenceEnablerProvider and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerReferenceEnablerProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerReferenceEnablerProvider.cs` (line 29)

### Methods

- `IDocumentViewerReferenceEnabler Create(IDocumentViewer documentViewer)`
  - Summary: Creates a or returns null
  - Parameters:
    - `IDocumentViewer documentViewer`: Document viewer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerReferenceEnablerProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(documentViewer: /* IDocumentViewer */);
    ```

## Interface `IDocumentViewerReferenceEnablerProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerReferenceEnablerProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerReferenceEnablerProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerReferenceEnablerProvider.cs` (line 39)

### Properties

- `string Id { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerReferenceEnablerProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Interface `IDocumentViewerService`

Notifies listeners when certain events occur. You can manually import this instance and hook the events or you can export an

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerService and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentViewerService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 29)

### Events

- `event EventHandler<DocumentViewerAddedEventArgs> Added`
  - Summary: Raised when a new instance has been created
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 33)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Added += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<DocumentViewerGotNewContentEventArgs> GotNewContent`
  - Summary: Raised when the instance gets new content (its method was called). It's only raised if the new content is different from the current content. I.e., calling it twice in a row with the same content won't raise this event the second time.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 47)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.GotNewContent += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<DocumentViewerRemovedEventArgs> Removed`
  - Summary: Raised when a instance has been closed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentViewerService.cs` (line 38)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Removed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IDocumentWriter`

Writes documents

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentWriter and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentWriter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentWriter.cs` (line 26)

### Methods

- `void Write(IDecompilerOutput output, string text)`
  - Summary: Writes text
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentWriter.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* IDecompilerOutput */, text: /* string */);
    ```

## Interface `IDocumentWriterProvider`

Creates s. Export an instance with at least one , a and optional s.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentWriterProvider and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentWriterProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentWriterProvider.cs` (line 28)

### Methods

- `IDocumentWriter Create(IContentType contentType)`
  - Summary: Creates a or returns null
  - Parameters:
    - `IContentType contentType`: Content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentWriterProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(contentType: /* IContentType */);
    ```

## Interface `IDocumentWriterService`

Writes text

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentWriterService and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.IDocumentWriterService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentWriterService.cs` (line 27)

### Methods

- `void Write(IDecompilerOutput output, string text, string contentType)`
  - Summary: Writes text
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `string text`: Text
    - `string contentType`: Content type, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/IDocumentWriterService.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* IDecompilerOutput */, text: /* string */, contentType: /* string */);
    ```

## Enum `MoveCaretOptions`

Move caret options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.MoveCaretOptions and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.MoveCaretOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/MoveCaretOptions.cs` (line 26)

### Members

- `None`: No bit is set
- `Select` = `x00000001`: Select the span
- `Focus` = `x00000002`: Give the text viewer focus
- `Center` = `x00000004`: Always center the caret in the view

## Class `PredefinedDocumentWriterProviderNames`

Predefined names

**Example**

```csharp
// Access dnSpy.Contracts.Documents.Tabs.DocViewer.PredefinedDocumentWriterProviderNames members directly without instantiation.
dnSpy.Contracts.Documents.Tabs.DocViewer.PredefinedDocumentWriterProviderNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/PredefinedDocumentWriterProviderNames.cs` (line 24)

### Fields

- `public const string DefaultXmlXaml = nameof(DefaultXmlXaml)`
  - Summary: Default XML/XAML writer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/PredefinedDocumentWriterProviderNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.Tabs.DocViewer.PredefinedDocumentWriterProviderNames.DefaultXmlXaml;
    ```

## Struct `ReferenceAndId`

Reference and id. Created from a

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ReferenceAndId(reference: /* object */, id: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceAndId.cs` (line 26)

### Constructors

- `public ReferenceAndId(object reference, string id)`
  - Summary: Constructor
  - Parameters:
    - `object reference`: Reference
    - `string id`: Reference id or null, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceAndId.cs` (line 43)

### Properties

- `public object Reference { get; }`
  - Summary: Gets the reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceAndId.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reference;
    ```
- `public string Id { get; }`
  - Summary: Id or null (eg. ). This is used to enable or disable the reference. If null, it's always enabled.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceAndId.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Struct `ReferenceInfo`

Reference info

**Inherits/Implements:** `IEquatable<ReferenceInfo>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ReferenceInfo(reference: /* object */, flags: /* DecompilerReferenceFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 29)

### Constructors

- `public ReferenceInfo(object reference, DecompilerReferenceFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `object reference`: Reference or null
    - `DecompilerReferenceFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 65)

### Methods

- `public TextReference ToTextReference()`
  - Summary: Creates a instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.ToTextReference();
    ```
- `public TextReference ToTextReference(Span span)`
  - Summary: Creates a instance
  - Parameters:
    - `Span span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.ToTextReference(span: /* Span */);
    ```
- `public bool Equals(ReferenceInfo other)`
  - Summary: Equals()
  - Parameters:
    - `ReferenceInfo other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* ReferenceInfo */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public DecompilerReferenceFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public bool IsDefinition => (Flags & DecompilerReferenceFlags.Definition) != 0`
  - Summary: true if it's a definition
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefinition;
    ```
- `public bool IsHidden => (Flags & DecompilerReferenceFlags.Hidden) != 0`
  - Summary: true if reference shouldn't be highlighted
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsHidden;
    ```
- `public bool IsLocal => (Flags & DecompilerReferenceFlags.Local) != 0`
  - Summary: true if it's a local, parameter, or label
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsLocal;
    ```
- `public bool IsWrite => (Flags & DecompilerReferenceFlags.IsWrite) != 0`
  - Summary: true if it's a write to a reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsWrite;
    ```
- `public object Reference { get; }`
  - Summary: Gets the reference or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reference;
    ```

### Operators

- `public static bool operator !=(ReferenceInfo a, ReferenceInfo b) => !a.Equals(b);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 97)
- `public static bool operator ==(ReferenceInfo a, ReferenceInfo b) => a.Equals(b);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 89)

## Class `SpanDataReferenceInfoExtensions`

extensions

**Example**

```csharp
// Access dnSpy.Contracts.Documents.Tabs.DocViewer.SpanDataReferenceInfoExtensions members directly without instantiation.
dnSpy.Contracts.Documents.Tabs.DocViewer.SpanDataReferenceInfoExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 123)

### Methods

- `public static TextReference ToTextReference(this SpanData<ReferenceInfo> spanData)`
  - Summary: Creates a
  - Parameters:
    - `this SpanData<ReferenceInfo> spanData`: Instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ReferenceInfo.cs` (line 129)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.Tabs.DocViewer.SpanDataReferenceInfoExtensions.ToTextReference(spanData: /* SpanData<ReferenceInfo> */);
    ```

## Class `TextReference`

A reference in the text

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.TextReference(reference: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 27)

### Constructors

- `public TextReference(object reference)`
  - Summary: Constructor
  - Parameters:
    - `object reference`: Reference or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 67)
- `public TextReference(object reference, DecompilerReferenceFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `object reference`: Reference or null
    - `DecompilerReferenceFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 85)
- `public TextReference(object reference, DecompilerReferenceFlags flags, Span span)`
  - Summary: Constructor
  - Parameters:
    - `object reference`: Reference or null
    - `DecompilerReferenceFlags flags`: Flags
    - `Span span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 97)
- `public TextReference(object reference, Span span)`
  - Summary: Constructor
  - Parameters:
    - `object reference`: Reference or null
    - `Span span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 76)

### Properties

- `public DecompilerReferenceFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public Span? Span { get; }`
  - Summary: Gets the span or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public bool IsDefinition => (Flags & DecompilerReferenceFlags.Definition) != 0`
  - Summary: true if it's a definition
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefinition;
    ```
- `public bool IsHidden => (Flags & DecompilerReferenceFlags.Hidden) != 0`
  - Summary: true if reference shouldn't be highlighted
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsHidden;
    ```
- `public bool IsLocal => (Flags & DecompilerReferenceFlags.Local) != 0`
  - Summary: true if it's a local, parameter, or label
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsLocal;
    ```
- `public bool IsWrite => (Flags & DecompilerReferenceFlags.IsWrite) != 0`
  - Summary: true if it's a write to a reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsWrite;
    ```
- `public object Reference { get; }`
  - Summary: Gets the reference or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/TextReference.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reference;
    ```

