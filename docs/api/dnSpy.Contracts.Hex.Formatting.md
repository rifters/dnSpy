# Namespace `dnSpy.Contracts.Hex.Formatting`

## Class `FormattedHexSourceFactoryService`

Formatted hex source factory service

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.FormattedHexSourceFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/FormattedHexSourceFactoryService.cs` (line 27)

### Constructors

- `protected FormattedHexSourceFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/FormattedHexSourceFactoryService.cs` (line 31)

### Methods

- `public abstract HexFormattedLineSource Create(double baseIndent, bool useDisplayMode, HexClassifier aggregateClassifier, HexAndAdornmentSequencer sequencer, VSTC.IClassificationFormatMap classificationFormatMap)`
  - Summary: Creates a
  - Parameters:
    - `double baseIndent`: Base indentation
    - `bool useDisplayMode`: true to use display mode, false to use ideal mode
    - `HexClassifier aggregateClassifier`: Classifier
    - `HexAndAdornmentSequencer sequencer`: Sequencer
    - `VSTC.IClassificationFormatMap classificationFormatMap`: Classification format map
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/FormattedHexSourceFactoryService.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(baseIndent: /* double */, useDisplayMode: /* bool */, aggregateClassifier: /* HexClassifier */, sequencer: /* HexAndAdornmentSequencer */, classificationFormatMap: /* VSTC.IClassificationFormatMap */);
    ```
- `public virtual HexFormattedLineSource Create(double baseIndent, bool useDisplayMode, HexAndAdornmentSequencer sequencer, VSTC.IClassificationFormatMap classificationFormatMap)`
  - Summary: Creates a that doesn't classify anything
  - Parameters:
    - `double baseIndent`: Base indentation
    - `bool useDisplayMode`: true to use display mode, false to use ideal mode
    - `HexAndAdornmentSequencer sequencer`: Sequencer
    - `VSTC.IClassificationFormatMap classificationFormatMap`: Classification format map
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/FormattedHexSourceFactoryService.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(baseIndent: /* double */, useDisplayMode: /* bool */, sequencer: /* HexAndAdornmentSequencer */, classificationFormatMap: /* VSTC.IClassificationFormatMap */);
    ```

## Class `HexAdornmentElement`

Adornment sequence element

**Inherits/Implements:** `HexSequenceElement`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexAdornmentElement();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAdornmentElement.cs` (line 26)

### Constructors

- `protected HexAdornmentElement()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAdornmentElement.cs` (line 30)

### Properties

- `public abstract VST.PositionAffinity Affinity { get; }`
  - Summary: Gets the affinity
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAdornmentElement.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Affinity;
    ```
- `public abstract double Baseline { get; }`
  - Summary: Gets the base line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAdornmentElement.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Baseline;
    ```
- `public abstract double BottomSpace { get; }`
  - Summary: Gets the bottom space
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAdornmentElement.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BottomSpace;
    ```
- `public abstract double TextHeight { get; }`
  - Summary: Gets the text height
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAdornmentElement.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextHeight;
    ```
- `public abstract double TopSpace { get; }`
  - Summary: Gets the top space
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAdornmentElement.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TopSpace;
    ```
- `public abstract double Width { get; }`
  - Summary: Gets the width
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAdornmentElement.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Width;
    ```
- `public abstract object IdentityTag { get; }`
  - Summary: Gets the identity tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAdornmentElement.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IdentityTag;
    ```
- `public abstract object ProviderTag { get; }`
  - Summary: Gets the provider tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAdornmentElement.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProviderTag;
    ```

## Class `HexAndAdornmentCollection`

collection

**Inherits/Implements:** `IReadOnlyList<HexSequenceElement>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexAndAdornmentCollection();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentCollection.cs` (line 27)

### Constructors

- `protected HexAndAdornmentCollection()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentCollection.cs` (line 31)

### Methods

- `public IEnumerator<HexSequenceElement> GetEnumerator()`
  - Summary: Gets the enumerator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentCollection.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEnumerator();
    ```

### Properties

- `public abstract HexAndAdornmentSequencer Sequencer { get; }`
  - Summary: Gets the sequencer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentCollection.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Sequencer;
    ```
- `public abstract int Count { get; }`
  - Summary: Gets the number of elements in this collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentCollection.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Count;
    ```

### Indexers

- `public abstract HexSequenceElement this[int index]`
  - Summary: Gets an element
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentCollection.cs` (line 43)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

## Class `HexAndAdornmentSequenceChangedEventArgs`

Event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexAndAdornmentSequenceChangedEventArgs(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencer.cs` (line 60)

### Constructors

- `public HexAndAdornmentSequenceChangedEventArgs(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencer.cs` (line 70)

### Properties

- `public HexBufferSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencer.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Class `HexAndAdornmentSequencer`

Creates a sequence of text and adornment elements

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexAndAdornmentSequencer();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencer.cs` (line 26)

### Constructors

- `protected HexAndAdornmentSequencer()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencer.cs` (line 30)

### Methods

- `public abstract HexAndAdornmentCollection CreateHexAndAdornmentCollection(HexBufferLine line)`
  - Summary: Creates a
  - Parameters:
    - `HexBufferLine line`: Line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencer.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateHexAndAdornmentCollection(line: /* HexBufferLine */);
    ```
- `public abstract HexAndAdornmentCollection CreateHexAndAdornmentCollection(HexBufferPoint position)`
  - Summary: Creates a
  - Parameters:
    - `HexBufferPoint position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencer.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateHexAndAdornmentCollection(position: /* HexBufferPoint */);
    ```

### Properties

- `public abstract HexBuffer Buffer { get; }`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencer.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```

### Events

- `public abstract event EventHandler<HexAndAdornmentSequenceChangedEventArgs> SequenceChanged`
  - Summary: Raised after a sequence has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencer.cs` (line 40)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.SequenceChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexAndAdornmentSequencerFactoryService`

Creates instances

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexAndAdornmentSequencerFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencerFactoryService.cs` (line 26)

### Constructors

- `protected HexAndAdornmentSequencerFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencerFactoryService.cs` (line 30)

### Methods

- `public abstract HexAndAdornmentSequencer Create(HexView view)`
  - Summary: Creates a instance
  - Parameters:
    - `HexView view`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexAndAdornmentSequencerFactoryService.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(view: /* HexView */);
    ```

## Class `HexFormattedLine`

A formatted line

**Inherits/Implements:** `WpfHexViewLine`, `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexFormattedLine();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 29)

### Constructors

- `protected HexFormattedLine()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 33)

### Methods

- `protected virtual void DisposeCore()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.DisposeCore();
    ```
- `public abstract Visual GetOrCreateVisual()`
  - Summary: Gets or creates the visual
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateVisual();
    ```
- `public abstract void RemoveVisual()`
  - Summary: Removes the visual
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveVisual();
    ```
- `public abstract void SetChange(VSTF.TextViewLineChange change)`
  - Summary: Sets the change
  - Parameters:
    - `VSTF.TextViewLineChange change`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.SetChange(change: /* VSTF.TextViewLineChange */);
    ```
- `public abstract void SetDeltaY(double deltaY)`
  - Summary: Sets a new delta Y
  - Parameters:
    - `double deltaY`: New delta Y
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.SetDeltaY(deltaY: /* double */);
    ```
- `public abstract void SetLineTransform(VSTF.LineTransform transform)`
  - Summary: Sets a new line transform
  - Parameters:
    - `VSTF.LineTransform transform`: New line transform
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.SetLineTransform(transform: /* VSTF.LineTransform */);
    ```
- `public abstract void SetTop(double top)`
  - Summary: Sets a new top
  - Parameters:
    - `double top`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.SetTop(top: /* double */);
    ```
- `public abstract void SetVisibleArea(Rect visibleArea)`
  - Summary: Sets the visible area
  - Parameters:
    - `Rect visibleArea`: Visible area
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.SetVisibleArea(visibleArea: /* Rect */);
    ```
- `public void Dispose()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Properties

- `public abstract bool HasAdornments { get; }`
  - Summary: true if there's at least one adornment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLine.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasAdornments;
    ```

## Class `HexFormattedLineSource`

Formatted line source

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexFormattedLineSource();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 27)

### Constructors

- `protected HexFormattedLineSource()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 31)

### Methods

- `public abstract HexFormattedLine FormatLineInVisualBuffer(HexBufferLine line)`
  - Summary: Formats a line
  - Parameters:
    - `HexBufferLine line`: Buffer line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatLineInVisualBuffer(line: /* HexBufferLine */);
    ```

### Properties

- `public abstract HexAndAdornmentSequencer HexAndAdornmentSequencer { get; }`
  - Summary: Gets the sequencer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexAndAdornmentSequencer;
    ```
- `public abstract TextRunProperties DefaultTextProperties { get; }`
  - Summary: Gets the default text properties
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DefaultTextProperties;
    ```
- `public abstract bool UseDisplayMode { get; }`
  - Summary: true to use mode, false to use mode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseDisplayMode;
    ```
- `public abstract double BaseIndentation { get; }`
  - Summary: Gets the base indentation
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BaseIndentation;
    ```
- `public abstract double ColumnWidth { get; }`
  - Summary: Gets the width of a column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ColumnWidth;
    ```
- `public abstract double LineHeight { get; }`
  - Summary: Gets the nominal line height
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LineHeight;
    ```
- `public abstract double TextHeightAboveBaseline { get; }`
  - Summary: Gets the nominal height of the text above the baseline
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextHeightAboveBaseline;
    ```
- `public abstract double TextHeightBelowBaseline { get; }`
  - Summary: Gets the nominal height of the text below the baseline
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexFormattedLineSource.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextHeightBelowBaseline;
    ```

## Class `HexHtmlBuilderService`

Creates HTML strings

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexHtmlBuilderService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexHtmlBuilderService.cs` (line 27)

### Constructors

- `protected HexHtmlBuilderService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexHtmlBuilderService.cs` (line 31)

### Methods

- `public abstract string GenerateHtmlFragment(NormalizedHexBufferSpanCollection spans, HexBufferLineFormatter bufferLines, string delimiter, CancellationToken cancellationToken)`
  - Summary: Creates an HTML fragment that can be copied to the clipboard
  - Parameters:
    - `NormalizedHexBufferSpanCollection spans`: Spans
    - `HexBufferLineFormatter bufferLines`: Buffer lines provider
    - `string delimiter`: Delimiter added between generated html strings
    - `CancellationToken cancellationToken`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexHtmlBuilderService.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.GenerateHtmlFragment(spans: /* NormalizedHexBufferSpanCollection */, bufferLines: /* HexBufferLineFormatter */, delimiter: /* string */, cancellationToken: /* CancellationToken */);
    ```
- `public abstract string GenerateHtmlFragment(NormalizedHexBufferSpanCollection spans, HexView hexView, string delimiter, CancellationToken cancellationToken)`
  - Summary: Creates an HTML fragment that can be copied to the clipboard
  - Parameters:
    - `NormalizedHexBufferSpanCollection spans`: Spans
    - `HexView hexView`: Hex view
    - `string delimiter`: Delimiter added between generated html strings
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexHtmlBuilderService.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.GenerateHtmlFragment(spans: /* NormalizedHexBufferSpanCollection */, hexView: /* HexView */, delimiter: /* string */, cancellationToken: /* CancellationToken */);
    ```
- `public string GenerateHtmlFragment(NormalizedHexBufferSpanCollection spans, HexBufferLineFormatter bufferLines, CancellationToken cancellationToken)`
  - Summary: Creates an HTML fragment that can be copied to the clipboard
  - Parameters:
    - `NormalizedHexBufferSpanCollection spans`: Spans
    - `HexBufferLineFormatter bufferLines`: Buffer lines provider
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexHtmlBuilderService.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GenerateHtmlFragment(spans: /* NormalizedHexBufferSpanCollection */, bufferLines: /* HexBufferLineFormatter */, cancellationToken: /* CancellationToken */);
    ```
- `public string GenerateHtmlFragment(NormalizedHexBufferSpanCollection spans, HexView hexView, CancellationToken cancellationToken)`
  - Summary: Creates an HTML fragment that can be copied to the clipboard
  - Parameters:
    - `NormalizedHexBufferSpanCollection spans`: Spans
    - `HexView hexView`: Hex view
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexHtmlBuilderService.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.GenerateHtmlFragment(spans: /* NormalizedHexBufferSpanCollection */, hexView: /* HexView */, cancellationToken: /* CancellationToken */);
    ```

### Properties

- `public virtual string DefaultDelimiter => "<br/>"`
  - Summary: Gets the default delimiter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexHtmlBuilderService.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DefaultDelimiter;
    ```

## Class `HexLineTransformSource`

Line transform source

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexLineTransformSource();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexLineTransformSource.cs` (line 27)

### Constructors

- `protected HexLineTransformSource()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexLineTransformSource.cs` (line 31)

### Methods

- `public abstract VSTF.LineTransform GetLineTransform(HexViewLine line, double yPosition, VSTE.ViewRelativePosition placement)`
  - Summary: Calculates the line transform for a given line of formatted text
  - Parameters:
    - `HexViewLine line`: Line
    - `double yPosition`: Y position
    - `VSTE.ViewRelativePosition placement`: Placement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexLineTransformSource.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineTransform(line: /* HexViewLine */, yPosition: /* double */, placement: /* VSTE.ViewRelativePosition */);
    ```

## Class `HexLineTransformSourceProvider`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexLineTransformSourceProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexLineTransformSourceProvider.cs` (line 26)

### Constructors

- `protected HexLineTransformSourceProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexLineTransformSourceProvider.cs` (line 30)

### Methods

- `public abstract HexLineTransformSource Create(WpfHexView hexView)`
  - Summary: Creates a or returns null
  - Parameters:
    - `WpfHexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexLineTransformSourceProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(hexView: /* WpfHexView */);
    ```

## Class `HexSequenceElement`

Sequence element

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexSequenceElement();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexSequenceElement.cs` (line 26)

### Constructors

- `protected HexSequenceElement()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexSequenceElement.cs` (line 30)

### Properties

- `public abstract VST.Span Span { get; }`
  - Summary: Line span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexSequenceElement.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public abstract bool ShouldRenderText { get; }`
  - Summary: true to show the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexSequenceElement.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShouldRenderText;
    ```

## Class `HexViewLine`

Hex view line

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.HexViewLine();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 30)

### Constructors

- `protected HexViewLine()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 34)

### Methods

- `public Collection<VSTF.TextBounds> GetNormalizedTextBounds(HexBufferSpanSelection span)`
  - Summary: Gets normalized text bounds
  - Parameters:
    - `HexBufferSpanSelection span`: Span and selection flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 270)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNormalizedTextBounds(span: /* HexBufferSpanSelection */);
    ```
- `public Collection<VSTF.TextBounds> GetNormalizedTextBounds(HexLineSpan lineSpan)`
  - Summary: Gets normalized text bounds
  - Parameters:
    - `HexLineSpan lineSpan`: Line span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 250)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNormalizedTextBounds(lineSpan: /* HexLineSpan */);
    ```
- `public abstract Collection<VSTF.TextBounds> GetNormalizedTextBounds(HexBufferSpan bufferPosition, HexSpanSelectionFlags flags)`
  - Summary: Gets normalized text bounds
  - Parameters:
    - `HexBufferSpan bufferPosition`: Position
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 279)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNormalizedTextBounds(bufferPosition: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
    ```
- `public abstract Collection<VSTF.TextBounds> GetNormalizedTextBounds(VST.Span lineSpan)`
  - Summary: Gets normalized text bounds
  - Parameters:
    - `VST.Span lineSpan`: Line span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 263)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNormalizedTextBounds(lineSpan: /* VST.Span */);
    ```
- `public abstract ReadOnlyCollection<object> GetAdornmentTags(object providerTag)`
  - Summary: Gets all adornment tags
  - Parameters:
    - `object providerTag`: Provider tag ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 200)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAdornmentTags(providerTag: /* object */);
    ```
- `public abstract VST.Span GetTextElementSpan(int linePosition)`
  - Summary: Gets the span whose text element index corresponds to the given line position
  - Parameters:
    - `int linePosition`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 286)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTextElementSpan(linePosition: /* int */);
    ```
- `public abstract VSTF.TextBounds GetCharacterBounds(int linePosition)`
  - Summary: Gets character bounds
  - Parameters:
    - `int linePosition`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 222)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCharacterBounds(linePosition: /* int */);
    ```
- `public abstract VSTF.TextBounds GetExtendedCharacterBounds(int linePosition)`
  - Summary: Gets extended character bounds, including any adornments
  - Parameters:
    - `int linePosition`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 229)
  - Example:
    ```csharp
    // Example invocation
    instance.GetExtendedCharacterBounds(linePosition: /* int */);
    ```
- `public abstract VSTF.TextBounds? GetAdornmentBounds(object identityTag)`
  - Summary: Gets the bounds of an adornment
  - Parameters:
    - `object identityTag`: Identity tag ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAdornmentBounds(identityTag: /* object */);
    ```
- `public abstract bool ContainsBufferPosition(HexBufferPoint bufferPosition)`
  - Summary: Returns true if lies within this line
  - Parameters:
    - `HexBufferPoint bufferPosition`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 186)
  - Example:
    ```csharp
    // Example invocation
    instance.ContainsBufferPosition(bufferPosition: /* HexBufferPoint */);
    ```
- `public abstract bool IntersectsBufferSpan(HexBufferSpan bufferSpan)`
  - Summary: Returns true if the line intersects with
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 293)
  - Example:
    ```csharp
    // Example invocation
    instance.IntersectsBufferSpan(bufferSpan: /* HexBufferSpan */);
    ```
- `public abstract int GetInsertionLinePositionFromXCoordinate(double xCoordinate)`
  - Summary: Gets the insertion line position
  - Parameters:
    - `double xCoordinate`: x coordinate
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 243)
  - Example:
    ```csharp
    // Example invocation
    instance.GetInsertionLinePositionFromXCoordinate(xCoordinate: /* double */);
    ```
- `public abstract int GetVirtualLinePositionFromXCoordinate(double xCoordinate)`
  - Summary: Gets the line position
  - Parameters:
    - `double xCoordinate`: x coordinate
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 236)
  - Example:
    ```csharp
    // Example invocation
    instance.GetVirtualLinePositionFromXCoordinate(xCoordinate: /* double */);
    ```
- `public abstract int? GetLinePositionFromXCoordinate(double xCoordinate)`
  - Summary: Gets the line position
  - Parameters:
    - `double xCoordinate`: x coordinate
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 207)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLinePositionFromXCoordinate(xCoordinate: /* double */);
    ```
- `public abstract int? GetLinePositionFromXCoordinate(double xCoordinate, bool textOnly)`
  - Summary: Gets the line position
  - Parameters:
    - `double xCoordinate`: x coordinate
    - `bool textOnly`: true to return null if it's over an adornment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 215)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLinePositionFromXCoordinate(xCoordinate: /* double */, textOnly: /* bool */);
    ```

### Properties

- `public HexBuffer Buffer => BufferLine.Buffer`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 149)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public HexBufferPoint BufferEnd => BufferSpan.End`
  - Summary: Gets the end position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 179)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferEnd;
    ```
- `public HexBufferPoint BufferStart => BufferSpan.Start`
  - Summary: Gets the start position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 174)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferStart;
    ```
- `public HexBufferSpan BufferSpan => BufferLine.BufferSpan`
  - Summary: Gets the buffer span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 169)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferSpan;
    ```
- `public VST.Span TextSpan => BufferLine.TextSpan`
  - Summary: Gets the text span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 164)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextSpan;
    ```
- `public abstract HexBufferLine BufferLine { get; }`
  - Summary: Gets the buffer line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 154)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferLine;
    ```
- `public abstract VSTF.LineTransform DefaultLineTransform { get; }`
  - Summary: Gets the default line transform
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 139)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DefaultLineTransform;
    ```
- `public abstract VSTF.LineTransform LineTransform { get; }`
  - Summary: Gets the line transform
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 144)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LineTransform;
    ```
- `public abstract VSTF.TextViewLineChange Change { get; }`
  - Summary: Gets the change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Change;
    ```
- `public abstract VSTF.VisibilityState VisibilityState { get; }`
  - Summary: Gets the visibility
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VisibilityState;
    ```
- `public abstract bool IsValid { get; }`
  - Summary: true if this line is valid, false if it has been disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsValid;
    ```
- `public abstract double Baseline { get; }`
  - Summary: Gets the base line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Baseline;
    ```
- `public abstract double Bottom { get; }`
  - Summary: Gets the position of the bottom edge of this line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Bottom;
    ```
- `public abstract double DeltaY { get; }`
  - Summary: Gets the delta Y between current layout and previous layout
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 119)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DeltaY;
    ```
- `public abstract double EndOfLineWidth { get; }`
  - Summary: Gets the width of the end of line character
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 124)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EndOfLineWidth;
    ```
- `public abstract double Height { get; }`
  - Summary: Gets the height of the line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 79)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Height;
    ```
- `public abstract double Left { get; }`
  - Summary: Gets the position of the left edge of this line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Left;
    ```
- `public abstract double Right { get; }`
  - Summary: Gets the position of the right edge of this line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Right;
    ```
- `public abstract double TextBottom { get; }`
  - Summary: Gets the position of the bottom edge of the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 89)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextBottom;
    ```
- `public abstract double TextHeight { get; }`
  - Summary: Gets the text height
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 109)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextHeight;
    ```
- `public abstract double TextLeft { get; }`
  - Summary: Gets the position of the left edge of the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextLeft;
    ```
- `public abstract double TextRight { get; }`
  - Summary: Gets the position of the right edge of the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 99)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextRight;
    ```
- `public abstract double TextTop { get; }`
  - Summary: Gets the position of the top edge of the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextTop;
    ```
- `public abstract double TextWidth { get; }`
  - Summary: Gets the text width
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 104)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextWidth;
    ```
- `public abstract double Top { get; }`
  - Summary: Gets the position of the top edge of this line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Top;
    ```
- `public abstract double VirtualSpaceWidth { get; }`
  - Summary: Get the width of the virtual spaces at the end of this line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 114)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VirtualSpaceWidth;
    ```
- `public abstract double Width { get; }`
  - Summary: Gets the width of the line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Width;
    ```
- `public abstract object IdentityTag { get; }`
  - Summary: Gets a tag that can be used to track the instance across layouts
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IdentityTag;
    ```
- `public string Text => BufferLine.Text`
  - Summary: Gets the text shown in this line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/HexViewLine.cs` (line 159)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Class `WpfHexViewLine`

WPF hex view line

**Inherits/Implements:** `HexViewLine`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Formatting.WpfHexViewLine();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/WpfHexViewLine.cs` (line 28)

### Constructors

- `protected WpfHexViewLine()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/WpfHexViewLine.cs` (line 32)

### Methods

- `public abstract TextRunProperties GetCharacterFormatting(int linePosition)`
  - Summary: Gets the character formatting
  - Parameters:
    - `int linePosition`: Line position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/WpfHexViewLine.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCharacterFormatting(linePosition: /* int */);
    ```

### Properties

- `public abstract ReadOnlyCollection<TextLine> TextLines { get; }`
  - Summary: Gets all text lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/WpfHexViewLine.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextLines;
    ```
- `public abstract Rect VisibleArea { get; }`
  - Summary: Gets the visible area
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Formatting/WpfHexViewLine.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VisibleArea;
    ```

