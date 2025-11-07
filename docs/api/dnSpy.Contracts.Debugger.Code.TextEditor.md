# Namespace `dnSpy.Contracts.Debugger.Code.TextEditor`

## Struct `DbgTextViewBreakpointLocationResult`

Text view locations

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Code.TextEditor.DbgTextViewBreakpointLocationResult(location: /* DbgCodeLocation */, span: /* SnapshotSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Code/TextEditor/DbgTextViewCodeLocationProvider.cs` (line 43)

### Constructors

- `public DbgTextViewBreakpointLocationResult(DbgCodeLocation location, SnapshotSpan span)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeLocation location`: Location
    - `SnapshotSpan span`: Text view span
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/TextEditor/DbgTextViewCodeLocationProvider.cs` (line 59)
- `public DbgTextViewBreakpointLocationResult(DbgCodeLocation location, VirtualSnapshotSpan span)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeLocation location`: Location
    - `VirtualSnapshotSpan span`: Text view span
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/TextEditor/DbgTextViewCodeLocationProvider.cs` (line 68)
- `public DbgTextViewBreakpointLocationResult(DbgCodeLocation[] locations, SnapshotSpan span)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeLocation[] locations`: Locations
    - `SnapshotSpan span`: Text view span
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/TextEditor/DbgTextViewCodeLocationProvider.cs` (line 80)
- `public DbgTextViewBreakpointLocationResult(DbgCodeLocation[] locations, VirtualSnapshotSpan span)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeLocation[] locations`: Locations
    - `VirtualSnapshotSpan span`: Text view span
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/TextEditor/DbgTextViewCodeLocationProvider.cs` (line 89)

### Properties

- `public DbgCodeLocation[] Locations { get; }`
  - Summary: Gets all locations
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/TextEditor/DbgTextViewCodeLocationProvider.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Locations;
    ```
- `public VirtualSnapshotSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/TextEditor/DbgTextViewCodeLocationProvider.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Class `DbgTextViewCodeLocationProvider`

Creates breakpoint locations in text views

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Code.TextEditor.DbgTextViewCodeLocationProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Code.TextEditor.DbgTextViewCodeLocationProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Code/TextEditor/DbgTextViewCodeLocationProvider.cs` (line 29)

### Methods

- `public abstract DbgTextViewBreakpointLocationResult? CreateLocation(IDocumentTab tab, ITextView textView, VirtualSnapshotPoint position)`
  - Summary: Creates a new instance whose text view span is >=
  - Parameters:
    - `IDocumentTab tab`: Tab
    - `ITextView textView`: Text view
    - `VirtualSnapshotPoint position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/TextEditor/DbgTextViewCodeLocationProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateLocation(tab: /* IDocumentTab */, textView: /* ITextView */, position: /* VirtualSnapshotPoint */);
    ```

