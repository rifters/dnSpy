# Namespace `dnSpy.Contracts.Debugger.CallStack.TextEditor`

## Class `DbgStackFrameGlyphTextMarkerLocationInfoProvider`

Converts s to s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.CallStack.TextEditor.DbgStackFrameGlyphTextMarkerLocationInfoProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.CallStack.TextEditor.DbgStackFrameGlyphTextMarkerLocationInfoProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/CallStack/TextEditor/DbgStackFrameGlyphTextMarkerLocationInfoProvider.cs` (line 26)

### Methods

- `public abstract GlyphTextMarkerLocationInfo Create(DbgStackFrame frame)`
  - Summary: Creates a or returns null
  - Parameters:
    - `DbgStackFrame frame`: Frame
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/TextEditor/DbgStackFrameGlyphTextMarkerLocationInfoProvider.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(frame: /* DbgStackFrame */);
    ```

## Class `DbgStackFrameTextViewMarker`

Creates stack frame spans in s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.CallStack.TextEditor.DbgStackFrameTextViewMarker and call its members.
var instance = new dnSpy.Contracts.Debugger.CallStack.TextEditor.DbgStackFrameTextViewMarker(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/CallStack/TextEditor/DbgStackFrameTextViewMarker.cs` (line 29)

### Methods

- `public abstract IEnumerable<SnapshotSpan> GetFrameSpans(ITextView textView, NormalizedSnapshotSpanCollection spans)`
  - Summary: Returns spans of the active statements set by . It shouldn't return duplicate spans. The first frame (if it exists) should not be marked by this class.
  - Parameters:
    - `ITextView textView`: Text view
    - `NormalizedSnapshotSpanCollection spans`: Spans
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/TextEditor/DbgStackFrameTextViewMarker.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFrameSpans(textView: /* ITextView */, spans: /* NormalizedSnapshotSpanCollection */);
    ```
- `public abstract void OnNewFrames(ReadOnlyCollection<DbgStackFrame> frames)`
  - Summary: Called when there's new frames. It's always called before . The first frame (if it exists) should not be marked by this class.
  - Parameters:
    - `ReadOnlyCollection<DbgStackFrame> frames`: New frames. These frames are owned by the caller and should not be closed by the callee.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/TextEditor/DbgStackFrameTextViewMarker.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewFrames(frames: /* ReadOnlyCollection<DbgStackFrame> */);
    ```

