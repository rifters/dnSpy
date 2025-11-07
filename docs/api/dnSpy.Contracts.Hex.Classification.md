# Namespace `dnSpy.Contracts.Hex.Classification`

## Class `HexClassificationChangedEventArgs`

Classification span changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Classification.HexClassificationChangedEventArgs(changeSpan: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationChangedEventArgs.cs` (line 26)

### Constructors

- `public HexClassificationChangedEventArgs(HexBufferSpan changeSpan)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan changeSpan`: The span that changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationChangedEventArgs.cs` (line 36)

### Properties

- `public HexBufferSpan ChangeSpan { get; }`
  - Summary: The span that changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationChangedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ChangeSpan;
    ```

## Struct `HexClassificationContext`

Hex classification context

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Classification.HexClassificationContext(line: /* HexBufferLine */, lineSpan: /* VST.Span */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationContext.cs` (line 27)

### Constructors

- `public HexClassificationContext(HexBufferLine line, VST.Span lineSpan)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferLine line`: Line info
    - `VST.Span lineSpan`: Line span to classify
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationContext.cs` (line 48)

### Properties

- `public HexBufferLine Line { get; }`
  - Summary: Gets the buffer line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationContext.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Line;
    ```
- `public VST.Span LineSpan { get; }`
  - Summary: Line span to classify
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationContext.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LineSpan;
    ```
- `public bool IsDefault => Line == null`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationContext.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```

## Class `HexClassificationFormatMapService`

Classification format map service

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Classification.HexClassificationFormatMapService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationFormatMapService.cs` (line 27)

### Constructors

- `protected HexClassificationFormatMapService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationFormatMapService.cs` (line 31)

### Methods

- `public abstract VSTC.IClassificationFormatMap GetClassificationFormatMap(HexView hexView)`
  - Summary: Gets a
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationFormatMapService.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetClassificationFormatMap(hexView: /* HexView */);
    ```
- `public abstract VSTC.IClassificationFormatMap GetClassificationFormatMap(string category)`
  - Summary: Gets a
  - Parameters:
    - `string category`: Appearance category
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationFormatMapService.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetClassificationFormatMap(category: /* string */);
    ```

## Struct `HexClassificationSpan`

Classification type and span

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Classification.HexClassificationSpan(span: /* VST.Span */, classification: /* VSTC.IClassificationType */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationSpan.cs` (line 28)

### Constructors

- `public HexClassificationSpan(VST.Span span, VSTC.IClassificationType classification)`
  - Summary: Constructor
  - Parameters:
    - `VST.Span span`: Span
    - `VSTC.IClassificationType classification`: Classification type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationSpan.cs` (line 44)

### Properties

- `public VST.Span Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationSpan.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public VSTC.IClassificationType ClassificationType { get; }`
  - Summary: Gets the classification type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassificationSpan.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ClassificationType;
    ```

## Class `HexClassifier`

Hex viewer classifier

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Classification.HexClassifier();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassifier.cs` (line 28)

### Constructors

- `protected HexClassifier()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassifier.cs` (line 32)

### Methods

- `protected virtual void DisposeCore()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassifier.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.DisposeCore();
    ```
- `public abstract void GetClassificationSpans(List<HexClassificationSpan> result, HexClassificationContext context)`
  - Summary: Classifies text
  - Parameters:
    - `List<HexClassificationSpan> result`: Updated with classifications
    - `HexClassificationContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassifier.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.GetClassificationSpans(result: /* List<HexClassificationSpan> */, context: /* HexClassificationContext */);
    ```
- `public virtual void GetClassificationSpans(List<HexClassificationSpan> result, HexClassificationContext context, CancellationToken cancellationToken)`
  - Summary: Classifies text synchronously
  - Parameters:
    - `List<HexClassificationSpan> result`: Updated with classifications
    - `HexClassificationContext context`: Context
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassifier.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.GetClassificationSpans(result: /* List<HexClassificationSpan> */, context: /* HexClassificationContext */, cancellationToken: /* CancellationToken */);
    ```
- `public void Dispose()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassifier.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Events

- `public abstract event EventHandler<HexClassificationChangedEventArgs> ClassificationChanged`
  - Summary: Raised when classification spans have changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassifier.cs` (line 37)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ClassificationChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexClassifierAggregatorService`

Hex buffer classifier aggregator service

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Classification.HexClassifierAggregatorService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassifierAggregatorService.cs` (line 24)

### Constructors

- `protected HexClassifierAggregatorService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassifierAggregatorService.cs` (line 28)

### Methods

- `public abstract HexClassifier GetClassifier(HexBuffer buffer)`
  - Summary: Creates a classifier aggregator
  - Parameters:
    - `HexBuffer buffer`: Buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexClassifierAggregatorService.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetClassifier(buffer: /* HexBuffer */);
    ```

## Class `HexEditorFormatMapService`

Hex editor format map service

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Classification.HexEditorFormatMapService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexEditorFormatMapService.cs` (line 27)

### Constructors

- `protected HexEditorFormatMapService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexEditorFormatMapService.cs` (line 31)

### Methods

- `public abstract VSTC.IEditorFormatMap GetEditorFormatMap(HexView view)`
  - Summary: Gets an
  - Parameters:
    - `HexView view`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexEditorFormatMapService.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEditorFormatMap(view: /* HexView */);
    ```
- `public abstract VSTC.IEditorFormatMap GetEditorFormatMap(string category)`
  - Summary: Gets an
  - Parameters:
    - `string category`: Appearance category
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexEditorFormatMapService.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEditorFormatMap(category: /* string */);
    ```

## Class `HexViewClassifierAggregatorService`

Hex view classifier aggregator service

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Classification.HexViewClassifierAggregatorService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexViewClassifierAggregatorService.cs` (line 26)

### Constructors

- `protected HexViewClassifierAggregatorService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexViewClassifierAggregatorService.cs` (line 30)

### Methods

- `public abstract HexClassifier GetClassifier(HexView hexView)`
  - Summary: Creates a classifier aggregator
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/HexViewClassifierAggregatorService.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetClassifier(hexView: /* HexView */);
    ```

