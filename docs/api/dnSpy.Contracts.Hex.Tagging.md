# Namespace `dnSpy.Contracts.Hex.Tagging`

## Class `HexBatchedTagsChangedEventArgs`

Batched tags changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexBatchedTagsChangedEventArgs(spans: /* IList<HexBufferSpan> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexBatchedTagsChangedEventArgs.cs` (line 28)

### Constructors

- `public HexBatchedTagsChangedEventArgs(IList<HexBufferSpan> spans)`
  - Summary: Constructor
  - Parameters:
    - `IList<HexBufferSpan> spans`: Spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexBatchedTagsChangedEventArgs.cs` (line 38)

### Properties

- `public ReadOnlyCollection<HexBufferSpan> Spans { get; }`
  - Summary: Gets the spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexBatchedTagsChangedEventArgs.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Spans;
    ```

## Class `HexBufferTagAggregatorFactoryService`

Hex buffer tag aggregator factory service

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexBufferTagAggregatorFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexBufferTagAggregatorFactoryService.cs` (line 24)

### Constructors

- `protected HexBufferTagAggregatorFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexBufferTagAggregatorFactoryService.cs` (line 28)

### Methods

- `public abstract HexTagAggregator<T> CreateTagAggregator<T>(HexBuffer buffer) where T : HexTag`
  - Summary: Creates a
  - Parameters:
    - `HexBuffer buffer`: Buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexBufferTagAggregatorFactoryService.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTagAggregator(buffer: /* HexBuffer */);
    ```

## Class `HexClassificationTag`

Classification tag

**Inherits/Implements:** `HexTag`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexClassificationTag(classificationType: /* VSTC.IClassificationType */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexClassificationTag.cs` (line 27)

### Constructors

- `public HexClassificationTag(VSTC.IClassificationType classificationType)`
  - Summary: Constructor
  - Parameters:
    - `VSTC.IClassificationType classificationType`: Classification type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexClassificationTag.cs` (line 37)

### Properties

- `public VSTC.IClassificationType ClassificationType { get; }`
  - Summary: Gets the classification type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexClassificationTag.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ClassificationType;
    ```

## Class `HexMarkerTag`

Hex marker tag used by

**Inherits/Implements:** `HexTag`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexMarkerTag(type: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexMarkerTag.cs` (line 27)

### Constructors

- `public HexMarkerTag(string type)`
  - Summary: Constructor
  - Parameters:
    - `string type`: Classification type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexMarkerTag.cs` (line 37)

### Properties

- `public string Type { get; }`
  - Summary: Gets the classification type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexMarkerTag.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```

## Class `HexSpaceNegotiatingAdornmentTag`

Space negotiating adornment tag

**Inherits/Implements:** `HexTag`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexSpaceNegotiatingAdornmentTag(width: /* double */, topSpace: /* double */, baseline: /* double */, textHeight: /* double */, bottomSpace: /* double */, affinity: /* VST.PositionAffinity */, identityTag: /* object */, providerTag: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexSpaceNegotiatingAdornmentTag.cs` (line 26)

### Constructors

- `public HexSpaceNegotiatingAdornmentTag(double width, double topSpace, double baseline, double textHeight, double bottomSpace, VST.PositionAffinity affinity, object identityTag, object providerTag)`
  - Summary: Constructor
  - Parameters:
    - `double width`: Width
    - `double topSpace`: Top space
    - `double baseline`: Base line
    - `double textHeight`: Text height
    - `double bottomSpace`: Bottom space
    - `VST.PositionAffinity affinity`: Affinity
    - `object identityTag`: Identity tag
    - `object providerTag`: Provider tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexSpaceNegotiatingAdornmentTag.cs` (line 78)

### Properties

- `public VST.PositionAffinity Affinity { get; }`
  - Summary: Gets the affinity
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexSpaceNegotiatingAdornmentTag.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Affinity;
    ```
- `public double Baseline { get; }`
  - Summary: Gets the base line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexSpaceNegotiatingAdornmentTag.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Baseline;
    ```
- `public double BottomSpace { get; }`
  - Summary: Gets the bottom space
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexSpaceNegotiatingAdornmentTag.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BottomSpace;
    ```
- `public double TextHeight { get; }`
  - Summary: Gets the text height
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexSpaceNegotiatingAdornmentTag.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextHeight;
    ```
- `public double TopSpace { get; }`
  - Summary: Gets the top space
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexSpaceNegotiatingAdornmentTag.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TopSpace;
    ```
- `public double Width { get; }`
  - Summary: Gets the width
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexSpaceNegotiatingAdornmentTag.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Width;
    ```
- `public object IdentityTag { get; }`
  - Summary: Gets the identity tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexSpaceNegotiatingAdornmentTag.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IdentityTag;
    ```
- `public object ProviderTag { get; }`
  - Summary: Gets the provider tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexSpaceNegotiatingAdornmentTag.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProviderTag;
    ```

## Class `HexTag`

Hex tag

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexTag();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTag.cs` (line 24)

### Constructors

- `protected HexTag()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTag.cs` (line 28)

## Class `HexTagAggregator<T>`

Tag aggregator

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexTagAggregator<T>();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 29)

### Constructors

- `protected HexTagAggregator()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 33)

### Methods

- `protected virtual void DisposeCore()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 122)
  - Example:
    ```csharp
    // Example invocation
    instance.DisposeCore();
    ```
- `public IEnumerable<IHexTagSpan<T>> GetTags(HexBufferSpan span)`
  - Summary: Returns all tags intersecting with
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(span: /* HexBufferSpan */);
    ```
- `public IEnumerable<IHexTagSpan<T>> GetTags(HexBufferSpan span, CancellationToken cancellationToken)`
  - Summary: Returns all tags intersecting with . This method is synchronous.
  - Parameters:
    - `HexBufferSpan span`: Span
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(span: /* HexBufferSpan */, cancellationToken: /* CancellationToken */);
    ```
- `public abstract IEnumerable<IHexTagSpan<T>> GetTags(NormalizedHexBufferSpanCollection spans)`
  - Summary: Returns all tags intersecting with
  - Parameters:
    - `NormalizedHexBufferSpanCollection spans`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(spans: /* NormalizedHexBufferSpanCollection */);
    ```
- `public abstract IEnumerable<IHexTagSpan<T>> GetTags(NormalizedHexBufferSpanCollection spans, CancellationToken cancellationToken)`
  - Summary: Returns all tags intersecting with . This method is synchronous.
  - Parameters:
    - `NormalizedHexBufferSpanCollection spans`: Span
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(spans: /* NormalizedHexBufferSpanCollection */, cancellationToken: /* CancellationToken */);
    ```
- `public abstract IEnumerable<IHexTextTagSpan<T>> GetAllTags(HexTaggerContext context)`
  - Summary: Gets all tags intersecting with the line. It merges all tags with all tags.
  - Parameters:
    - `HexTaggerContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAllTags(context: /* HexTaggerContext */);
    ```
- `public abstract IEnumerable<IHexTextTagSpan<T>> GetAllTags(HexTaggerContext context, CancellationToken cancellationToken)`
  - Summary: Gets all tags intersecting with the line. It merges all tags with all tags. This method is synchronous.
  - Parameters:
    - `HexTaggerContext context`: Context
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 112)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAllTags(context: /* HexTaggerContext */, cancellationToken: /* CancellationToken */);
    ```
- `public abstract IEnumerable<IHexTextTagSpan<T>> GetLineTags(HexTaggerContext context)`
  - Summary: Gets all tags intersecting with the line
  - Parameters:
    - `HexTaggerContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineTags(context: /* HexTaggerContext */);
    ```
- `public abstract IEnumerable<IHexTextTagSpan<T>> GetLineTags(HexTaggerContext context, CancellationToken cancellationToken)`
  - Summary: Gets all tags intersecting with the line. This method is synchronous.
  - Parameters:
    - `HexTaggerContext context`: Context
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineTags(context: /* HexTaggerContext */, cancellationToken: /* CancellationToken */);
    ```
- `public void Dispose()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Properties

- `public abstract HexBuffer Buffer { get; }`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```

### Events

- `public abstract event EventHandler<HexBatchedTagsChangedEventArgs> BatchedTagsChanged`
  - Summary: Raised on the original thread after tags have changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 48)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BatchedTagsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<HexTagsChangedEventArgs> TagsChanged`
  - Summary: Raised after tags have changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagAggregator.cs` (line 43)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TagsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexTagSpan<T>`

Hex tag and span

**Inherits/Implements:** `IHexTagSpan<T>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexTagSpan<T>(span: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */, tag: /* T */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagSpan.cs` (line 48)

### Constructors

- `public HexTagSpan(HexBufferSpan span, HexSpanSelectionFlags flags, T tag)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
    - `HexSpanSelectionFlags flags`: Flags
    - `T tag`: Tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagSpan.cs` (line 70)

### Properties

- `public HexBufferSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagSpan.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public HexSpanSelectionFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagSpan.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public T Tag { get; }`
  - Summary: Gets the tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagSpan.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```

## Class `HexTagTypeAttribute`

Used by taggers to declare which tag types they support

**Inherits/Implements:** `VSUTIL.MultipleBaseMetadataAttribute`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexTagTypeAttribute(tagType: /* Type */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagTypeAttribute.cs` (line 27)

### Constructors

- `public HexTagTypeAttribute(Type tagType)`
  - Summary: Constructor
  - Parameters:
    - `Type tagType`: Tag type; it must derive from
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagTypeAttribute.cs` (line 37)

### Properties

- `public Type TagTypes { get; }`
  - Summary: Gets the tag type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagTypeAttribute.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TagTypes;
    ```

## Class `HexTagger<T>`

Tagger

**Inherits/Implements:** `IHexTagger<T>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexTagger<T>();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 69)

### Constructors

- `protected HexTagger()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 73)

### Methods

- `public abstract IEnumerable<IHexTagSpan<T>> GetTags(NormalizedHexBufferSpanCollection spans)`
  - Summary: Gets all tags intersecting with
  - Parameters:
    - `NormalizedHexBufferSpanCollection spans`: Spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(spans: /* NormalizedHexBufferSpanCollection */);
    ```
- `public abstract IEnumerable<IHexTextTagSpan<T>> GetTags(HexTaggerContext context)`
  - Summary: Gets all tags
  - Parameters:
    - `HexTaggerContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(context: /* HexTaggerContext */);
    ```
- `public virtual IEnumerable<IHexTagSpan<T>> GetTags(NormalizedHexBufferSpanCollection spans, CancellationToken cancellationToken)`
  - Summary: Gets all tags intersecting with . This method is synchronous.
  - Parameters:
    - `NormalizedHexBufferSpanCollection spans`: Spans
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(spans: /* NormalizedHexBufferSpanCollection */, cancellationToken: /* CancellationToken */);
    ```
- `public virtual IEnumerable<IHexTextTagSpan<T>> GetTags(HexTaggerContext context, CancellationToken cancellationToken)`
  - Summary: Gets all tags. This method is synchronous.
  - Parameters:
    - `HexTaggerContext context`: Context
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(context: /* HexTaggerContext */, cancellationToken: /* CancellationToken */);
    ```

### Events

- `public abstract event EventHandler<HexBufferSpanEventArgs> TagsChanged`
  - Summary: Raised after tags have changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 78)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TagsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `HexTaggerContext`

Hex tagger context

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexTaggerContext(line: /* HexBufferLine */, lineSpan: /* VST.Span */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTaggerContext.cs` (line 27)

### Constructors

- `public HexTaggerContext(HexBufferLine line, VST.Span lineSpan)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferLine line`: Line info
    - `VST.Span lineSpan`: Line span to tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTaggerContext.cs` (line 48)

### Properties

- `public HexBufferLine Line { get; }`
  - Summary: Gets the line info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTaggerContext.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Line;
    ```
- `public VST.Span LineSpan { get; }`
  - Summary: Line span to tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTaggerContext.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LineSpan;
    ```
- `public bool IsDefault => Line == null`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTaggerContext.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```

## Class `HexTaggerProvider`

Hex tagger provider

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexTaggerProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTaggerProvider.cs` (line 24)

### Constructors

- `protected HexTaggerProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTaggerProvider.cs` (line 28)

### Methods

- `public abstract IHexTagger<T> CreateTagger<T>(HexBuffer buffer) where T : HexTag`
  - Summary: Creates a tagger or returns null
  - Parameters:
    - `HexBuffer buffer`: Hex buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTaggerProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTagger(buffer: /* HexBuffer */);
    ```

## Class `HexTagsChangedEventArgs`

Tags changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexTagsChangedEventArgs(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagsChangedEventArgs.cs` (line 26)

### Constructors

- `public HexTagsChangedEventArgs(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagsChangedEventArgs.cs` (line 36)

### Properties

- `public HexBufferSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagsChangedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Class `HexTextTagSpan<T>`

Text span and tag

**Inherits/Implements:** `IHexTextTagSpan<T>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexTextTagSpan<T>(span: /* VST.Span */, tag: /* T */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTextTagSpan.cs` (line 44)

### Constructors

- `public HexTextTagSpan(VST.Span span, T tag)`
  - Summary: Constructor
  - Parameters:
    - `VST.Span span`: Description not provided.
    - `T tag`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTextTagSpan.cs` (line 60)

### Properties

- `public T Tag { get; }`
  - Summary: Gets the tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTextTagSpan.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```
- `public VST.Span Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTextTagSpan.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Class `HexToolTipStructureSpanTag`

Hex tooltip structure tag, the tooltip is shown when hovering over a value in the hex view.

**Inherits/Implements:** `HexTag`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexToolTipStructureSpanTag(bufferSpan: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexToolTipStructureSpanTag.cs` (line 26)

### Constructors

- `public HexToolTipStructureSpanTag(HexBufferSpan bufferSpan)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span of field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexToolTipStructureSpanTag.cs` (line 46)
- `public HexToolTipStructureSpanTag(HexBufferSpan bufferSpan, object toolTip, object reference)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span of field
    - `object toolTip`: Tooltip to show or null
    - `object reference`: A reference to some high level object that represents the data or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexToolTipStructureSpanTag.cs` (line 56)

### Properties

- `public HexBufferSpan BufferSpan { get; }`
  - Summary: Span of data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexToolTipStructureSpanTag.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferSpan;
    ```
- `public object Reference { get; }`
  - Summary: A reference to some high level object that represents the data or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexToolTipStructureSpanTag.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reference;
    ```
- `public object ToolTip { get; }`
  - Summary: Tooltip to show or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexToolTipStructureSpanTag.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTip;
    ```

## Class `HexViewTagAggregatorFactoryService`

Hex view tag aggregator factory service

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexViewTagAggregatorFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexViewTagAggregatorFactoryService.cs` (line 26)

### Constructors

- `protected HexViewTagAggregatorFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexViewTagAggregatorFactoryService.cs` (line 30)

### Methods

- `public abstract HexTagAggregator<T> CreateTagAggregator<T>(HexView hexView) where T : HexTag`
  - Summary: Creates a
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexViewTagAggregatorFactoryService.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTagAggregator(hexView: /* HexView */);
    ```

## Class `HexViewTaggerProvider`

Hex view tag aggregator

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Tagging.HexViewTaggerProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexViewTaggerProvider.cs` (line 26)

### Constructors

- `protected HexViewTaggerProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexViewTaggerProvider.cs` (line 30)

### Methods

- `public abstract IHexTagger<T> CreateTagger<T>(HexView hexView, HexBuffer buffer) where T : HexTag`
  - Summary: Creates a tagger or returns null
  - Parameters:
    - `HexView hexView`: Hex view
    - `HexBuffer buffer`: Buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexViewTaggerProvider.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTagger(hexView: /* HexView */, buffer: /* HexBuffer */);
    ```

## Interface `IHexTagSpan<out T>`

Hex tag and span

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Tagging.IHexTagSpan<out T> and call its members.
var instance = new dnSpy.Contracts.Hex.Tagging.IHexTagSpan<out T>(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagSpan.cs` (line 27)

### Properties

- `HexBufferSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagSpan.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `HexSpanSelectionFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagSpan.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `T Tag { get; }`
  - Summary: Gets the tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagSpan.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```

## Interface `IHexTagger<out T>`

Tagger

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Tagging.IHexTagger<out T> and call its members.
var instance = new dnSpy.Contracts.Hex.Tagging.IHexTagger<out T>(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 29)

### Methods

- `IEnumerable<IHexTagSpan<T>> GetTags(NormalizedHexBufferSpanCollection spans)`
  - Summary: Gets all tags intersecting with
  - Parameters:
    - `NormalizedHexBufferSpanCollection spans`: Spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(spans: /* NormalizedHexBufferSpanCollection */);
    ```
- `IEnumerable<IHexTagSpan<T>> GetTags(NormalizedHexBufferSpanCollection spans, CancellationToken cancellationToken)`
  - Summary: Gets all tags intersecting with . This method is synchronous.
  - Parameters:
    - `NormalizedHexBufferSpanCollection spans`: Spans
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(spans: /* NormalizedHexBufferSpanCollection */, cancellationToken: /* CancellationToken */);
    ```
- `IEnumerable<IHexTextTagSpan<T>> GetTags(HexTaggerContext context)`
  - Summary: Gets all tags
  - Parameters:
    - `HexTaggerContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(context: /* HexTaggerContext */);
    ```
- `IEnumerable<IHexTextTagSpan<T>> GetTags(HexTaggerContext context, CancellationToken cancellationToken)`
  - Summary: Gets all tags. This method is synchronous.
  - Parameters:
    - `HexTaggerContext context`: Context
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(context: /* HexTaggerContext */, cancellationToken: /* CancellationToken */);
    ```

### Events

- `event EventHandler<HexBufferSpanEventArgs> TagsChanged`
  - Summary: Raised after tags have changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTagger.cs` (line 33)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TagsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IHexTextTagSpan<out T>`

Text span and tag

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Tagging.IHexTextTagSpan<out T> and call its members.
var instance = new dnSpy.Contracts.Hex.Tagging.IHexTextTagSpan<out T>(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTextTagSpan.cs` (line 28)

### Properties

- `T Tag { get; }`
  - Summary: Gets the tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTextTagSpan.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```
- `VST.Span Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Tagging/HexTextTagSpan.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

