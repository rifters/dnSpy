# Namespace `dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor`

## Class `DbgBreakpointGlyphFormatter`

Writes breakpoints info used by breakpoint glyph margin code, eg. in tooltips. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor.DbgBreakpointGlyphFormatter and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor.DbgBreakpointGlyphFormatter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphFormatter.cs` (line 31)

### Methods

- `public abstract bool WriteLocation(IDbgTextWriter output, DbgCodeBreakpoint breakpoint, ITextView textView, SnapshotSpan span)`
  - Summary: Writes the text shown after "Location: " in tooltips when hovering over the breakpoint icon in the glyph margin. Returns true if something was written, and false if nothing was written.
  - Parameters:
    - `IDbgTextWriter output`: Output
    - `DbgCodeBreakpoint breakpoint`: Breakpoint
    - `ITextView textView`: Text view
    - `SnapshotSpan span`: Span of breakpoint marker in the document
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphFormatter.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLocation(output: /* IDbgTextWriter */, breakpoint: /* DbgCodeBreakpoint */, textView: /* ITextView */, span: /* SnapshotSpan */);
    ```

## Class `DbgBreakpointGlyphTextMarkerLocationProvider`

Creates s. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor.DbgBreakpointGlyphTextMarkerLocationProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor.DbgBreakpointGlyphTextMarkerLocationProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphTextMarkerLocationProvider.cs` (line 29)

### Methods

- `public abstract GlyphTextMarkerLocationInfo GetLocation(DbgCodeBreakpoint breakpoint)`
  - Summary: Gets the location of the breakpoint or null
  - Parameters:
    - `DbgCodeBreakpoint breakpoint`: Breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphTextMarkerLocationProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLocation(breakpoint: /* DbgCodeBreakpoint */);
    ```

## Class `ExportDbgBreakpointGlyphFormatterAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgBreakpointGlyphFormatterMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor.ExportDbgBreakpointGlyphFormatterAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphFormatter.cs` (line 52)

### Constructors

- `public ExportDbgBreakpointGlyphFormatterAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphFormatter.cs` (line 58)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphFormatter.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDbgBreakpointGlyphTextMarkerLocationProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgBreakpointGlyphTextMarkerLocationProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor.ExportDbgBreakpointGlyphTextMarkerLocationProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphTextMarkerLocationProvider.cs` (line 47)

### Constructors

- `public ExportDbgBreakpointGlyphTextMarkerLocationProviderAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphTextMarkerLocationProvider.cs` (line 53)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphTextMarkerLocationProvider.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDbgBreakpointGlyphFormatterMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor.IDbgBreakpointGlyphFormatterMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor.IDbgBreakpointGlyphFormatterMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphFormatter.cs` (line 44)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphFormatter.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDbgBreakpointGlyphTextMarkerLocationProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor.IDbgBreakpointGlyphTextMarkerLocationProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.TextEditor.IDbgBreakpointGlyphTextMarkerLocationProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphTextMarkerLocationProvider.cs` (line 39)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/TextEditor/DbgBreakpointGlyphTextMarkerLocationProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

