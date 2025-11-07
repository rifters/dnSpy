# Namespace `dnSpy.Contracts.Hex`

## Class `HexBuffer`

Hex buffer

**Inherits/Implements:** `VSUTIL.IPropertyOwner`, `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBuffer(tags: /* HexTags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 29)

### Constructors

- `protected HexBuffer(HexTags tags)`
  - Summary: Constructor
  - Parameters:
    - `HexTags tags`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 33)

### Methods

- `protected virtual void DisposeCore()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 702)
  - Example:
    ```csharp
    // Example invocation
    instance.DisposeCore();
    ```
- `public HexSpan? GetNextValidSpan(HexPosition position, HexPosition upperBounds, bool fullSpan)`
  - Summary: Gets the next valid span or null if there's none left. This includes the input () if it happens to lie within this valid span. This method merges all consecutive valid spans.
  - Parameters:
    - `HexPosition position`: Start position to check
    - `HexPosition upperBounds`: End position
    - `bool fullSpan`: true if positions before should be included in the returned result. This could result in worse performance.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 134)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNextValidSpan(position: /* HexPosition */, upperBounds: /* HexPosition */, fullSpan: /* bool */);
    ```
- `public HexSpan? GetNextValidSpan(HexPosition position, bool fullSpan)`
  - Summary: Gets the next valid span or null if there's none left. This includes the input () if it happens to lie within this valid span. This method merges all consecutive valid spans.
  - Parameters:
    - `HexPosition position`: Start position to check
    - `bool fullSpan`: true if positions before should be included in the returned result. This could result in worse performance.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 122)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNextValidSpan(position: /* HexPosition */, fullSpan: /* bool */);
    ```
- `public HexSpan? GetPreviousValidSpan(HexPosition position, HexPosition lowerBounds, bool fullSpan)`
  - Summary: Gets the previous valid span or null if there's none left. This includes the input () if it happens to lie within this valid span. This method merges all consecutive valid spans.
  - Parameters:
    - `HexPosition position`: Start position to check
    - `HexPosition lowerBounds`: End position
    - `bool fullSpan`: true if positions after should be included in the returned result. This could result in worse performance.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 185)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPreviousValidSpan(position: /* HexPosition */, lowerBounds: /* HexPosition */, fullSpan: /* bool */);
    ```
- `public HexSpan? GetPreviousValidSpan(HexPosition position, bool fullSpan)`
  - Summary: Gets the previous valid span or null if there's none left. This includes the input () if it happens to lie within this valid span. This method merges all consecutive valid spans.
  - Parameters:
    - `HexPosition position`: Start position to check
    - `bool fullSpan`: true if positions after should be included in the returned result. This could result in worse performance.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 173)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPreviousValidSpan(position: /* HexPosition */, fullSpan: /* bool */);
    ```
- `public IEnumerable<HexSpan> GetValidSpans()`
  - Summary: Gets all valid spans. This could be empty if it's a 0-byte buffer stream. This method merges all consecutive valid spans.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 273)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValidSpans();
    ```
- `public IEnumerable<HexSpan> GetValidSpans(HexSpan span, bool fullSpan)`
  - Summary: Gets all valid spans overlapping . This method merges all consecutive valid spans.
  - Parameters:
    - `HexSpan span`: Span
    - `bool fullSpan`: true if positions before should be included in the returned result. This could result in worse performance.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 283)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValidSpans(span: /* HexSpan */, fullSpan: /* bool */);
    ```
- `public abstract HexBytes ReadHexBytes(HexPosition position, long length)`
  - Summary: Reads bytes
  - Parameters:
    - `HexPosition position`: Position
    - `long length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 651)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadHexBytes(position: /* HexPosition */, length: /* long */);
    ```
- `public abstract HexEdit CreateEdit()`
  - Summary: Creates a object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 299)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateEdit();
    ```
- `public abstract HexEdit CreateEdit(int? reiteratedVersionNumber, object editTag)`
  - Summary: Creates a object
  - Parameters:
    - `int? reiteratedVersionNumber`: Use by undo/redo to restore a previous version
    - `object editTag`: Edit tag, can be anything
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 307)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateEdit(reiteratedVersionNumber: /* int? */, editTag: /* object */);
    ```
- `public abstract HexSpanInfo GetSpanInfo(HexPosition position)`
  - Summary: Gets information about a position in the buffer. The returned info isn't normalized, there may be consecutive spans with the same flags. It's the responsibility of the caller to merge such spans.
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpanInfo(position: /* HexPosition */);
    ```
- `public abstract bool CheckEditAccess()`
  - Summary: Returns true if the current thread is allowed to modify the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.CheckEditAccess();
    ```
- `public abstract byte ReadByte(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 474)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadByte(position: /* HexPosition */);
    ```
- `public abstract byte[] ReadBytes(HexPosition position, long length)`
  - Summary: Reads bytes
  - Parameters:
    - `HexPosition position`: Position
    - `long length`: Number of bytes to read
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 608)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(position: /* HexPosition */, length: /* long */);
    ```
- `public abstract byte[] ReadBytes(HexPosition position, ulong length)`
  - Summary: Reads bytes
  - Parameters:
    - `HexPosition position`: Position
    - `ulong length`: Number of bytes to read
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 616)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(position: /* HexPosition */, length: /* ulong */);
    ```
- `public abstract byte[] ReadBytes(HexSpan span)`
  - Summary: Reads bytes
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 623)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(span: /* HexSpan */);
    ```
- `public abstract double ReadDouble(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 537)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadDouble(position: /* HexPosition */);
    ```
- `public abstract double ReadDoubleBigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 600)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadDoubleBigEndian(position: /* HexPosition */);
    ```
- `public abstract float ReadSingle(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 530)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadSingle(position: /* HexPosition */);
    ```
- `public abstract float ReadSingleBigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 593)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadSingleBigEndian(position: /* HexPosition */);
    ```
- `public abstract int ReadInt32(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 502)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt32(position: /* HexPosition */);
    ```
- `public abstract int ReadInt32BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 565)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt32BigEndian(position: /* HexPosition */);
    ```
- `public abstract int TryReadByte(HexPosition position)`
  - Summary: Tries to read a . If there's no data, a value less than 0 is returned.
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 460)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadByte(position: /* HexPosition */);
    ```
- `public abstract long ReadInt64(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 516)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt64(position: /* HexPosition */);
    ```
- `public abstract long ReadInt64BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 579)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt64BigEndian(position: /* HexPosition */);
    ```
- `public abstract sbyte ReadSByte(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 481)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadSByte(position: /* HexPosition */);
    ```
- `public abstract short ReadInt16(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 488)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt16(position: /* HexPosition */);
    ```
- `public abstract short ReadInt16BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 551)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt16BigEndian(position: /* HexPosition */);
    ```
- `public abstract uint ReadUInt32(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 509)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt32(position: /* HexPosition */);
    ```
- `public abstract uint ReadUInt32BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 572)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt32BigEndian(position: /* HexPosition */);
    ```
- `public abstract ulong ReadUInt64(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 523)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt64(position: /* HexPosition */);
    ```
- `public abstract ulong ReadUInt64BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 586)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt64BigEndian(position: /* HexPosition */);
    ```
- `public abstract ushort ReadUInt16(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 495)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt16(position: /* HexPosition */);
    ```
- `public abstract ushort ReadUInt16BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 558)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt16BigEndian(position: /* HexPosition */);
    ```
- `public abstract void ReadBytes(HexPosition position, byte[] destination, long destinationIndex, long length)`
  - Summary: Reads bytes
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] destination`: Destination array
    - `long destinationIndex`: Index
    - `long length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 643)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(position: /* HexPosition */, destination: /* byte[] */, destinationIndex: /* long */, length: /* long */);
    ```
- `public abstract void Refresh()`
  - Summary: Clears any read caches and raises if needed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.Refresh();
    ```
- `public abstract void TakeThreadOwnership()`
  - Summary: Claims ownership of this buffer for the current thread
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.TakeThreadOwnership();
    ```
- `public char ReadChar(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 467)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadChar(position: /* HexPosition */);
    ```
- `public char ReadCharBigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 544)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadCharBigEndian(position: /* HexPosition */);
    ```
- `public void Dispose()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 691)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```
- `public void ReadBytes(HexPosition position, byte[] destination)`
  - Summary: Reads bytes
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] destination`: Destination array
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 630)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(position: /* HexPosition */, destination: /* byte[] */);
    ```
- `public void Replace(HexPosition position, byte value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `byte value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 314)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* byte */);
    ```
- `public void Replace(HexPosition position, byte[] data)`
  - Summary: Replaces the data at with
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] data`: New data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 434)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, data: /* byte[] */);
    ```
- `public void Replace(HexPosition position, byte[] data, long index, long length)`
  - Summary: Replaces the data at with
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] data`: New data
    - `long index`: Index
    - `long length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 448)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, data: /* byte[] */, index: /* long */, length: /* long */);
    ```
- `public void Replace(HexPosition position, double value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `double value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 422)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* double */);
    ```
- `public void Replace(HexPosition position, float value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `float value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 410)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* float */);
    ```
- `public void Replace(HexPosition position, int value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `int value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 362)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* int */);
    ```
- `public void Replace(HexPosition position, long value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `long value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 386)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* long */);
    ```
- `public void Replace(HexPosition position, sbyte value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `sbyte value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 326)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* sbyte */);
    ```
- `public void Replace(HexPosition position, short value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `short value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 338)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* short */);
    ```
- `public void Replace(HexPosition position, uint value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `uint value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 374)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* uint */);
    ```
- `public void Replace(HexPosition position, ulong value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `ulong value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 398)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* ulong */);
    ```
- `public void Replace(HexPosition position, ushort value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `ushort value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 350)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* ushort */);
    ```

### Properties

- `public HexTags Tags { get; }`
  - Summary: Gets the tags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tags;
    ```
- `public VSUTIL.PropertyCollection Properties { get; }`
  - Summary: Gets all properties
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Properties;
    ```
- `public abstract HexSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public abstract HexVersion Version { get; }`
  - Summary: Gets the version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Version;
    ```
- `public abstract bool EditInProgress { get; }`
  - Summary: true if an edit is in progress
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EditInProgress;
    ```
- `public abstract bool IsReadOnly { get; }`
  - Summary: true if the buffer is read-only
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsReadOnly;
    ```
- `public abstract bool IsVolatile { get; }`
  - Summary: true if the content can change at any time
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsVolatile;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the name. This could be the filename if the data was read from a file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public bool IsDisposed { get; private set; }`
  - Summary: true if the instance has been disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 686)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDisposed;
    ```
- `public bool IsMemory => Tags.Contains(PredefinedHexBufferTags.Memory)`
  - Summary: true if the underlying stream reads data from some process' memory
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMemory;
    ```

### Events

- `public abstract event EventHandler PostChanged`
  - Summary: Raised after an edit operation has completed or after it has been canceled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 676)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PostChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<HexBufferSpanInvalidatedEventArgs> BufferSpanInvalidated`
  - Summary: Raised when a span of data got modified by other code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 76)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BufferSpanInvalidated += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<HexContentChangedEventArgs> Changed`
  - Summary: Raised when the buffer has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 666)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Changed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<HexContentChangedEventArgs> ChangedHighPriority`
  - Summary: Raised when the buffer has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 661)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ChangedHighPriority += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<HexContentChangedEventArgs> ChangedLowPriority`
  - Summary: Raised when the buffer has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 671)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ChangedLowPriority += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<HexContentChangingEventArgs> Changing`
  - Summary: Raised before the text buffer gets changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 656)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Changing += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public event EventHandler Disposed`
  - Summary: Raised after it is disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 681)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Disposed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexBufferCreatedEventArgs`

Hex buffer created event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferCreatedEventArgs(buffer: /* HexBuffer */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferCreatedEventArgs.cs` (line 26)

### Constructors

- `public HexBufferCreatedEventArgs(HexBuffer buffer)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferCreatedEventArgs.cs` (line 36)

### Properties

- `public HexBuffer Buffer { get; }`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferCreatedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```

## Class `HexBufferFactoryService`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferFactoryService.cs` (line 27)

### Constructors

- `protected HexBufferFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferFactoryService.cs` (line 31)

### Methods

- `public HexTags CreateTags(IEnumerable<string> tags)`
  - Summary: Creates a new instance
  - Parameters:
    - `IEnumerable<string> tags`: Tags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferFactoryService.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTags(tags: /* IEnumerable<string> */);
    ```
- `public abstract HexBuffer Create(HexBufferStream stream, HexTags tags, bool disposeStream)`
  - Summary: Creates a new
  - Parameters:
    - `HexBufferStream stream`: Stream to use
    - `HexTags tags`: Tags
    - `bool disposeStream`: true if the returned buffer owns and disposes it when the buffer gets disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferFactoryService.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(stream: /* HexBufferStream */, tags: /* HexTags */, disposeStream: /* bool */);
    ```
- `public abstract HexBuffer Create(byte[] data, string name, HexTags tags = null)`
  - Summary: Creates a new
  - Parameters:
    - `byte[] data`: Data
    - `string name`: Name, can be anything and is usually the filename
    - `HexTags tags` (default: `null`): Tags or null to use the default file tags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferFactoryService.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(data: /* byte[] */, name: /* string */, tags: /* HexTags */);
    ```
- `public abstract HexBuffer Create(string filename, HexTags tags = null)`
  - Summary: Creates a new
  - Parameters:
    - `string filename`: Filename
    - `HexTags tags` (default: `null`): Tags or null to use the default file tags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferFactoryService.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(filename: /* string */, tags: /* HexTags */);
    ```

### Properties

- `public HexTags DefaultFileTags { get; }`
  - Summary: Default file / byte array tags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferFactoryService.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DefaultFileTags;
    ```
- `public HexTags DefaultMemoryTags { get; }`
  - Summary: Default memory tags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferFactoryService.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DefaultMemoryTags;
    ```
- `public HexTags EmptyTags { get; }`
  - Summary: Gets the empty tags collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferFactoryService.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EmptyTags;
    ```

### Events

- `public abstract event EventHandler<HexBufferCreatedEventArgs> HexBufferCreated`
  - Summary: Raised when a new has been created
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferFactoryService.cs` (line 70)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.HexBufferCreated += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexBufferLine`

Line information

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferLine();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 30)

### Constructors

- `protected HexBufferLine()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 34)

### Methods

- `public HexCellPosition? GetClosestCellPosition(HexLinePositionInfo position, bool onlyVisibleCells)`
  - Summary: Gets the closest cell position
  - Parameters:
    - `HexLinePositionInfo position`: Position
    - `bool onlyVisibleCells`: true to only return cells with data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 449)
  - Example:
    ```csharp
    // Example invocation
    instance.GetClosestCellPosition(position: /* HexLinePositionInfo */, onlyVisibleCells: /* bool */);
    ```
- `public HexCellPosition? GetClosestCellPosition(int linePosition, bool onlyVisibleCells)`
  - Summary: Gets the closest cell position
  - Parameters:
    - `int linePosition`: Line position
    - `bool onlyVisibleCells`: true to only return cells with data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 438)
  - Example:
    ```csharp
    // Example invocation
    instance.GetClosestCellPosition(linePosition: /* int */, onlyVisibleCells: /* bool */);
    ```
- `public HexLinePositionInfo GetLinePositionInfo(int linePosition)`
  - Summary: Creates a
  - Parameters:
    - `int linePosition`: Line position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 393)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLinePositionInfo(linePosition: /* int */);
    ```
- `public IEnumerable<TextAndHexSpan> GetAsciiSpans(HexBufferSpan span, HexSpanSelectionFlags flags)`
  - Summary: Gets ASCII spans
  - Parameters:
    - `HexBufferSpan span`: Buffer span
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 191)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAsciiSpans(span: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
    ```
- `public IEnumerable<TextAndHexSpan> GetAsciiSpans(HexBufferSpanSelection span)`
  - Summary: Gets ASCII spans
  - Parameters:
    - `HexBufferSpanSelection span`: Span and selection flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAsciiSpans(span: /* HexBufferSpanSelection */);
    ```
- `public IEnumerable<TextAndHexSpan> GetSpans(HexBufferSpan span, HexSpanSelectionFlags flags)`
  - Summary: Gets column spans in column order
  - Parameters:
    - `HexBufferSpan span`: Buffer span
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 208)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpans(span: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
    ```
- `public IEnumerable<TextAndHexSpan> GetSpans(HexBufferSpanSelection span)`
  - Summary: Gets column spans in column order
  - Parameters:
    - `HexBufferSpanSelection span`: Span and selection flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpans(span: /* HexBufferSpanSelection */);
    ```
- `public IEnumerable<TextAndHexSpan> GetValuesSpans(HexBufferSpan span, HexSpanSelectionFlags flags)`
  - Summary: Gets values spans
  - Parameters:
    - `HexBufferSpan span`: Buffer span
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 166)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValuesSpans(span: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
    ```
- `public IEnumerable<TextAndHexSpan> GetValuesSpans(HexBufferSpanSelection span)`
  - Summary: Gets values spans
  - Parameters:
    - `HexBufferSpanSelection span`: Span and selection flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValuesSpans(span: /* HexBufferSpanSelection */);
    ```
- `public VST.Span GetSpan(HexColumnType column, bool onlyVisibleCells)`
  - Summary: Gets the span of a column
  - Parameters:
    - `HexColumnType column`: Colum
    - `bool onlyVisibleCells`: true to only include visible values, false to include the full column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 129)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpan(column: /* HexColumnType */, onlyVisibleCells: /* bool */);
    ```
- `public abstract VST.Span GetAsciiSpan(bool onlyVisibleCells)`
  - Summary: Gets the span of the ASCII column. This can be an empty span if the ASCII column isn't shown.
  - Parameters:
    - `bool onlyVisibleCells`: true to only include visible characters, false to include the full column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAsciiSpan(onlyVisibleCells: /* bool */);
    ```
- `public abstract VST.Span GetOffsetSpan()`
  - Summary: Gets the span of the offset in . This can be an empty span if the offset column isn't shown.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOffsetSpan();
    ```
- `public abstract VST.Span GetValuesSpan(bool onlyVisibleCells)`
  - Summary: Gets the span of the values column
  - Parameters:
    - `bool onlyVisibleCells`: true to only include visible values, false to include the full column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 150)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValuesSpan(onlyVisibleCells: /* bool */);
    ```
- `public bool IsColumnPresent(HexColumnType column)`
  - Summary: Returns true if a column is present
  - Parameters:
    - `HexColumnType column`: Column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    instance.IsColumnPresent(column: /* HexColumnType */);
    ```
- `public int? GetLinePosition(HexCellPosition position)`
  - Summary: Gets a text line position or null
  - Parameters:
    - `HexCellPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 367)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLinePosition(position: /* HexCellPosition */);
    ```
- `public override string ToString()`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 627)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public string GetText(HexBufferSpan visibleBytes)`
  - Summary: Gets the text. All cells outside the input range are cleared.
  - Parameters:
    - `HexBufferSpan visibleBytes`: Visible bytes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 597)
  - Example:
    ```csharp
    // Example invocation
    instance.GetText(visibleBytes: /* HexBufferSpan */);
    ```

### Properties

- `public HexBuffer Buffer => LineProvider.Buffer`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public HexBufferPoint BufferEnd => BufferSpan.End`
  - Summary: Gets the end position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferEnd;
    ```
- `public HexBufferPoint BufferStart => BufferSpan.Start`
  - Summary: Gets the start position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferStart;
    ```
- `public VST.Span TextSpan => new VST.Span(0, Text.Length)`
  - Summary: Gets a span covering
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextSpan;
    ```
- `public abstract HexBufferLineFormatter LineProvider { get; }`
  - Summary: Gets the instance that created this line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LineProvider;
    ```
- `public abstract HexBufferSpan BufferSpan { get; }`
  - Summary: Buffer span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferSpan;
    ```
- `public abstract HexBytes HexBytes { get; }`
  - Summary: All raw bytes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexBytes;
    ```
- `public abstract HexCellCollection AsciiCells { get; }`
  - Summary: Gets the ASCII cell collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 255)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsciiCells;
    ```
- `public abstract HexCellCollection ValueCells { get; }`
  - Summary: Gets the value cell collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 250)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueCells;
    ```
- `public abstract HexPosition LineNumber { get; }`
  - Summary: Gets the line number
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LineNumber;
    ```
- `public abstract HexPosition LogicalOffset { get; }`
  - Summary: Gets the value of the offset shown in . The real offset is stored in
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 121)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LogicalOffset;
    ```
- `public abstract ReadOnlyCollection<HexColumnType> ColumnOrder { get; }`
  - Summary: Gets the column order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ColumnOrder;
    ```
- `public abstract bool IsAsciiColumnPresent { get; }`
  - Summary: true if the ASCII column is present
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAsciiColumnPresent;
    ```
- `public abstract bool IsOffsetColumnPresent { get; }`
  - Summary: true if the offset column is present
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOffsetColumnPresent;
    ```
- `public abstract bool IsValuesColumnPresent { get; }`
  - Summary: true if the values column is present
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsValuesColumnPresent;
    ```
- `public abstract string Text { get; }`
  - Summary: Text shown in the UI. The positions of the offset column, values column and ASCII column are not fixed, use one of the GetXXX methods to get the spans.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLine.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Class `HexBufferLineFormatter`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferLineFormatter();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 28)

### Constructors

- `protected HexBufferLineFormatter()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 32)

### Methods

- `public HexBufferPoint FilterAndVerify(HexBufferPoint position)`
  - Summary: Filters the position so it's less than if it equals . It will throw if returns false.
  - Parameters:
    - `HexBufferPoint position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 258)
  - Example:
    ```csharp
    // Example invocation
    instance.FilterAndVerify(position: /* HexBufferPoint */);
    ```
- `public VST.Span GetColumnSpan(HexColumnType column)`
  - Summary: Gets the span of a column. This is empty if the column isn't present.
  - Parameters:
    - `HexColumnType column`: Column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColumnSpan(column: /* HexColumnType */);
    ```
- `public abstract HexBufferLine GetLineFromLineNumber(HexPosition lineNumber)`
  - Summary: Returns a line
  - Parameters:
    - `HexPosition lineNumber`: Line number
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 207)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineFromLineNumber(lineNumber: /* HexPosition */);
    ```
- `public abstract HexBufferLine GetLineFromPosition(HexBufferPoint position)`
  - Summary: Creates a line
  - Parameters:
    - `HexBufferPoint position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 214)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineFromPosition(position: /* HexBufferPoint */);
    ```
- `public abstract HexBufferPoint GetBufferPositionFromLineNumber(HexPosition lineNumber)`
  - Summary: Gets the buffer position of a line
  - Parameters:
    - `HexPosition lineNumber`: Line number
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 200)
  - Example:
    ```csharp
    // Example invocation
    instance.GetBufferPositionFromLineNumber(lineNumber: /* HexPosition */);
    ```
- `public abstract HexBufferSpan GetValueBufferSpan(HexCell cell, int cellPosition)`
  - Summary: Gets a buffer span within a cell
  - Parameters:
    - `HexCell cell`: Cell
    - `int cellPosition`: Position within the cell
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 272)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValueBufferSpan(cell: /* HexCell */, cellPosition: /* int */);
    ```
- `public abstract HexPosition GetLineNumberFromPosition(HexBufferPoint position)`
  - Summary: Gets the line number
  - Parameters:
    - `HexBufferPoint position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 221)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineNumberFromPosition(position: /* HexBufferPoint */);
    ```
- `public abstract HexPosition ToLogicalPosition(HexPosition physicalPosition)`
  - Summary: Converts a physical (stream) position to a logical position
  - Parameters:
    - `HexPosition physicalPosition`: Physical (stream) position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 228)
  - Example:
    ```csharp
    // Example invocation
    instance.ToLogicalPosition(physicalPosition: /* HexPosition */);
    ```
- `public abstract HexPosition ToPhysicalPosition(HexPosition logicalPosition)`
  - Summary: Converts a logical position to a physical (stream) position
  - Parameters:
    - `HexPosition logicalPosition`: Logical position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 235)
  - Example:
    ```csharp
    // Example invocation
    instance.ToPhysicalPosition(logicalPosition: /* HexPosition */);
    ```
- `public abstract PositionAndData? EditValueCell(HexCell cell, int cellPosition, char c)`
  - Summary: Edits a value cell. Returns null if editing isn't supported or if the character isn't a valid input character (eg. it's not a hex digit character), else it returns the position in the buffer and new value.
  - Parameters:
    - `HexCell cell`: Cell
    - `int cellPosition`: Position within the cell
    - `char c`: Character
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 288)
  - Example:
    ```csharp
    // Example invocation
    instance.EditValueCell(cell: /* HexCell */, cellPosition: /* int */, c: /* char */);
    ```
- `public abstract int GetCharsPerCell(HexColumnType column)`
  - Summary: Gets the number of characters per cell value. This value doesn't include any cell separators
  - Parameters:
    - `HexColumnType column`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCharsPerCell(column: /* HexColumnType */);
    ```
- `public abstract int GetCharsPerCellIncludingSeparator(HexColumnType column)`
  - Summary: Gets the total number of characters per cell. This includes cell separators if any.
  - Parameters:
    - `HexColumnType column`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCharsPerCellIncludingSeparator(column: /* HexColumnType */);
    ```
- `public abstract string GetFormattedOffset(HexPosition position)`
  - Summary: Returns the offset as a string
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 295)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFormattedOffset(position: /* HexPosition */);
    ```
- `public bool IsValidPosition(HexBufferPoint position)`
  - Summary: Returns true if is a valid position that can be passed to methods expecting a (physical) position.
  - Parameters:
    - `HexBufferPoint position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 243)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValidPosition(position: /* HexBufferPoint */);
    ```

### Properties

- `public HexBufferPoint BufferEnd => BufferSpan.End`
  - Summary: Gets the end position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferEnd;
    ```
- `public HexBufferPoint BufferStart => BufferSpan.Start`
  - Summary: Gets the start position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferStart;
    ```
- `public abstract HexBuffer Buffer { get; }`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public abstract HexBufferSpan BufferSpan { get; }`
  - Summary: Gets the buffer span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferSpan;
    ```
- `public abstract HexOffsetFormat OffsetFormat { get; }`
  - Summary: Offset format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 126)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OffsetFormat;
    ```
- `public abstract HexPosition BasePosition { get; }`
  - Summary: Base position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 141)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BasePosition;
    ```
- `public abstract HexPosition EndPosition { get; }`
  - Summary: End position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 136)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EndPosition;
    ```
- `public abstract HexPosition LineCount { get; }`
  - Summary: Number of lines. There's always at least one line.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LineCount;
    ```
- `public abstract HexPosition StartPosition { get; }`
  - Summary: First position to show
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 131)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StartPosition;
    ```
- `public abstract HexValuesDisplayFormat ValuesFormat { get; }`
  - Summary: Values format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 166)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesFormat;
    ```
- `public abstract ReadOnlyCollection<HexColumnType> ColumnOrder { get; }`
  - Summary: Column order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 181)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ColumnOrder;
    ```
- `public abstract ReadOnlyCollection<HexGroupInformation> AsciiGroup { get; }`
  - Summary: ASCII group collection. It's empty if the ASCII column isn't present.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsciiGroup;
    ```
- `public abstract ReadOnlyCollection<HexGroupInformation> ValuesGroup { get; }`
  - Summary: Values group collection. It's empty if the values column isn't present.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesGroup;
    ```
- `public abstract VST.Span AsciiSpan { get; }`
  - Summary: Gets the span of the ASCII column. This is empty if the column isn't present.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsciiSpan;
    ```
- `public abstract VST.Span OffsetSpan { get; }`
  - Summary: Gets the span of the offset column. This is empty if the column isn't present.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OffsetSpan;
    ```
- `public abstract VST.Span ValuesSpan { get; }`
  - Summary: Gets the span of the values column. This is empty if the column isn't present.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesSpan;
    ```
- `public abstract bool CanEditValueCell { get; }`
  - Summary: true if can be called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 277)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanEditValueCell;
    ```
- `public abstract bool OffsetLowerCaseHex { get; }`
  - Summary: true to use lower case hex
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 121)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OffsetLowerCaseHex;
    ```
- `public abstract bool ShowAscii { get; }`
  - Summary: true to show ASCII chars
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 176)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowAscii;
    ```
- `public abstract bool ShowOffset { get; }`
  - Summary: true to show the offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowOffset;
    ```
- `public abstract bool ShowValues { get; }`
  - Summary: true to show the values
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 151)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowValues;
    ```
- `public abstract bool UseRelativePositions { get; }`
  - Summary: true if all visible positions are relative to
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 146)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseRelativePositions;
    ```
- `public abstract bool ValuesLowerCaseHex { get; }`
  - Summary: true to use lower case hex
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 156)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesLowerCaseHex;
    ```
- `public abstract int BytesPerLine { get; }`
  - Summary: Number of bytes per line or 0 to fit to width
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BytesPerLine;
    ```
- `public abstract int BytesPerValue { get; }`
  - Summary: Number of bytes per value in the values column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 171)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BytesPerValue;
    ```
- `public abstract int CharsPerLine { get; }`
  - Summary: Number of characters per line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CharsPerLine;
    ```
- `public abstract int GroupSizeInBytes { get; }`
  - Summary: Number of bytes per group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GroupSizeInBytes;
    ```
- `public abstract int OffsetBitSize { get; }`
  - Summary: Number of bits of the offset to show
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatter.cs` (line 161)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OffsetBitSize;
    ```

## Class `HexBufferLineFormatterFactoryService`

Creates instances

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferLineFormatterFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterFactoryService.cs` (line 24)

### Constructors

- `protected HexBufferLineFormatterFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterFactoryService.cs` (line 28)

### Methods

- `public abstract HexBufferLineFormatter Create(HexBuffer buffer, HexBufferLineFormatterOptions options)`
  - Summary: Creates a new instance
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexBufferLineFormatterOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterFactoryService.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(buffer: /* HexBuffer */, options: /* HexBufferLineFormatterOptions */);
    ```

## Class `HexBufferLineFormatterOptions`

Options passed to

**Inherits/Implements:** `IEquatable<HexBufferLineFormatterOptions>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.HexBufferLineFormatterOptions and call its members.
var instance = new dnSpy.Contracts.Hex.HexBufferLineFormatterOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 26)

### Methods

- `public bool Equals(HexBufferLineFormatterOptions other)`
  - Summary: Equals()
  - Parameters:
    - `HexBufferLineFormatterOptions other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 154)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* HexBufferLineFormatterOptions */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Other object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 191)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 197)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public HexColumnType[] ColumnOrder { get; set; }`
  - Summary: Column order or null to use the default order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ColumnOrder;
    ```
- `public HexOffsetFormat OffsetFormat { get; set; }`
  - Summary: Offset format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OffsetFormat;
    ```
- `public HexPosition BasePosition { get; set; }`
  - Summary: Base position. The real position is added to this value which is then shown in the offset column.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BasePosition;
    ```
- `public HexPosition EndPosition { get; set; }`
  - Summary: End position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EndPosition;
    ```
- `public HexPosition StartPosition { get; set; }`
  - Summary: First position to show
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StartPosition;
    ```
- `public HexValuesDisplayFormat ValuesFormat { get; set; }`
  - Summary: Values format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesFormat;
    ```
- `public bool OffsetLowerCaseHex { get; set; }`
  - Summary: true to use lower case hex
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OffsetLowerCaseHex;
    ```
- `public bool ShowAscii { get; set; }`
  - Summary: true to show ASCII chars
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowAscii;
    ```
- `public bool ShowOffset { get; set; }`
  - Summary: true to show the offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowOffset;
    ```
- `public bool ShowValues { get; set; }`
  - Summary: true to show the values
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowValues;
    ```
- `public bool UseRelativePositions { get; set; }`
  - Summary: true if all visible positions are relative to
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseRelativePositions;
    ```
- `public bool ValuesLowerCaseHex { get; set; }`
  - Summary: true to use lower case hex
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesLowerCaseHex;
    ```
- `public int BytesPerLine { get; set; }`
  - Summary: Number of bytes per line or 0 to fit to width
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BytesPerLine;
    ```
- `public int CharsPerLine { get; set; }`
  - Summary: Number of visible characters per line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CharsPerLine;
    ```
- `public int GroupSizeInBytes { get; set; }`
  - Summary: Size of a group in bytes or 0 to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GroupSizeInBytes;
    ```
- `public int OffsetBitSize { get; set; }`
  - Summary: Number of bits of the offset to show. Must be a multiple of 4. If it's 0, the default value is used.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OffsetBitSize;
    ```

### Fields

- `public const HexOffsetFormat HexOffsetFormat_First = HexOffsetFormat.Hex`
  - Summary: First valid value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 142)
  - Example:
    ```csharp
    var value = instance.HexOffsetFormat_First;
    ```
- `public const HexOffsetFormat HexOffsetFormat_Last = HexOffsetFormat.HexAssembly`
  - Summary: Last valid value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 147)
  - Example:
    ```csharp
    var value = instance.HexOffsetFormat_Last;
    ```
- `public const HexValuesDisplayFormat HexValuesDisplayFormat_First = HexValuesDisplayFormat.HexByte`
  - Summary: First valid value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 132)
  - Example:
    ```csharp
    var value = instance.HexValuesDisplayFormat_First;
    ```
- `public const HexValuesDisplayFormat HexValuesDisplayFormat_Last = HexValuesDisplayFormat.DoubleBigEndian`
  - Summary: Last valid value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 137)
  - Example:
    ```csharp
    var value = instance.HexValuesDisplayFormat_Last;
    ```
- `public static readonly int MaxBytesPerLine = 1024`
  - Summary: Max bytes per line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 127)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexBufferLineFormatterOptions.MaxBytesPerLine;
    ```
- `public static readonly int MaxOffsetBitSize = 64`
  - Summary: Maximum value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 117)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexBufferLineFormatterOptions.MaxOffsetBitSize;
    ```
- `public static readonly int MinBytesPerLine = 0`
  - Summary: Min bytes per line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 122)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexBufferLineFormatterOptions.MinBytesPerLine;
    ```
- `public static readonly int MinOffsetBitSize = 0`
  - Summary: Minimum value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferLineFormatterOptions.cs` (line 112)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexBufferLineFormatterOptions.MinOffsetBitSize;
    ```

## Struct `HexBufferPoint`

Contains a and a position

**Inherits/Implements:** `IEquatable<HexBufferPoint>`, `IComparable<HexBufferPoint>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferPoint(buffer: /* HexBuffer */, position: /* HexPosition */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 26)

### Constructors

- `public HexBufferPoint(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 47)

### Methods

- `public HexBufferPoint Add(HexPosition value)`
  - Summary: Add
  - Parameters:
    - `HexPosition value`: Value to add
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(value: /* HexPosition */);
    ```
- `public HexBufferPoint Subtract(HexPosition value)`
  - Summary: Subtract
  - Parameters:
    - `HexPosition value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.Subtract(value: /* HexPosition */);
    ```
- `public HexPosition Difference(HexBufferPoint other)`
  - Summary: Returns the difference of with this instance
  - Parameters:
    - `HexBufferPoint other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.Difference(other: /* HexBufferPoint */);
    ```
- `public bool Equals(HexBufferPoint other)`
  - Summary: Equals()
  - Parameters:
    - `HexBufferPoint other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* HexBufferPoint */);
    ```
- `public byte GetByte()`
  - Summary: Gets the byte
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.GetByte();
    ```
- `public int CompareTo(HexBufferPoint other)`
  - Summary: Compares this instance with
  - Parameters:
    - `HexBufferPoint other`: Ohter instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 110)
  - Example:
    ```csharp
    // Example invocation
    instance.CompareTo(other: /* HexBufferPoint */);
    ```
- `public int TryGetByte()`
  - Summary: Gets the or a value less than 0 if there's no data at
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetByte();
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 128)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 134)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public HexBuffer Buffer { get; }`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public HexPosition Position { get; }`
  - Summary: Gets the position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Position;
    ```
- `public bool IsDefault => Buffer == null`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```

### Operators

- `public static HexBufferPoint operator +(HexBufferPoint point, HexPosition value) => point.Add(value);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 96)
- `public static HexBufferPoint operator -(HexBufferPoint point, HexPosition value) => point.Subtract(value);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 95)
- `public static HexPosition operator -(HexBufferPoint left, HexBufferPoint right) => left.Position - right.Position;`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 94)
- `public static bool operator !=(HexBufferPoint a, HexBufferPoint b) => !a.Equals(b);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 98)
- `public static bool operator <(HexBufferPoint a, HexBufferPoint b) => a.CompareTo(b) < 0;`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 99)
- `public static bool operator <=(HexBufferPoint a, HexBufferPoint b) => a.CompareTo(b) <= 0;`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 100)
- `public static bool operator ==(HexBufferPoint a, HexBufferPoint b) => a.Equals(b);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 97)
- `public static bool operator >(HexBufferPoint a, HexBufferPoint b) => a.CompareTo(b) > 0;`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 101)
- `public static bool operator >=(HexBufferPoint a, HexBufferPoint b) => a.CompareTo(b) >= 0;`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 102)
- `public static implicit operator HexPosition(HexBufferPoint point) => point.Position;`
  - Summary: Converts to a
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferPoint.cs` (line 58)

## Struct `HexBufferSpan`

Contains a and a

**Inherits/Implements:** `IEquatable<HexBufferSpan>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferSpan(buffer: /* HexBuffer */, span: /* HexSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 27)

### Constructors

- `public HexBufferSpan(HexBuffer buffer, HexPosition start, ulong length)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition start`: Start point
    - `ulong length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 84)
- `public HexBufferSpan(HexBuffer buffer, HexSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 73)
- `public HexBufferSpan(HexBufferPoint start, HexBufferPoint end)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferPoint start`: Start position
    - `HexBufferPoint end`: End position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 94)
- `public HexBufferSpan(HexBufferPoint start, ulong length)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferPoint start`: Start point
    - `ulong length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 108)

### Methods

- `public HexBufferSpan? Intersection(HexBufferSpan span)`
  - Summary: Returns the intersection or null if there's none
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 249)
  - Example:
    ```csharp
    // Example invocation
    instance.Intersection(span: /* HexBufferSpan */);
    ```
- `public HexBufferSpan? Intersection(HexSpan span)`
  - Summary: Returns the intersection or null if there's none
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 237)
  - Example:
    ```csharp
    // Example invocation
    instance.Intersection(span: /* HexSpan */);
    ```
- `public HexBufferSpan? Overlap(HexBufferSpan span)`
  - Summary: Gets the overlap with or null if there's none
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 205)
  - Example:
    ```csharp
    // Example invocation
    instance.Overlap(span: /* HexBufferSpan */);
    ```
- `public HexBufferSpan? Overlap(HexSpan span)`
  - Summary: Gets the overlap with or null if there's none
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.Overlap(span: /* HexSpan */);
    ```
- `public bool Contains(HexBufferPoint point)`
  - Summary: Returns true if lies within this span
  - Parameters:
    - `HexBufferPoint point`: Point
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.Contains(point: /* HexBufferPoint */);
    ```
- `public bool Contains(HexBufferSpan span)`
  - Summary: Returns true if lies within this span
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.Contains(span: /* HexBufferSpan */);
    ```
- `public bool Contains(HexPosition position)`
  - Summary: Returns true if lies within this span
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 168)
  - Example:
    ```csharp
    // Example invocation
    instance.Contains(position: /* HexPosition */);
    ```
- `public bool Contains(HexSpan span)`
  - Summary: Returns true if lies within this span
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 150)
  - Example:
    ```csharp
    // Example invocation
    instance.Contains(span: /* HexSpan */);
    ```
- `public bool Equals(HexBufferSpan other)`
  - Summary: Equals()
  - Parameters:
    - `HexBufferSpan other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 279)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* HexBufferSpan */);
    ```
- `public bool IntersectsWith(HexBufferSpan span)`
  - Summary: Returns true if intersects with this instance
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 226)
  - Example:
    ```csharp
    // Example invocation
    instance.IntersectsWith(span: /* HexBufferSpan */);
    ```
- `public bool IntersectsWith(HexSpan span)`
  - Summary: Returns true if intersects with this instance
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 219)
  - Example:
    ```csharp
    // Example invocation
    instance.IntersectsWith(span: /* HexSpan */);
    ```
- `public bool OverlapsWith(HexBufferSpan span)`
  - Summary: Returns true if this instances overlaps with
  - Parameters:
    - `HexBufferSpan span`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    instance.OverlapsWith(span: /* HexBufferSpan */);
    ```
- `public bool OverlapsWith(HexSpan span)`
  - Summary: Returns true if this instances overlaps with
  - Parameters:
    - `HexSpan span`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.OverlapsWith(span: /* HexSpan */);
    ```
- `public byte[] GetData()`
  - Summary: Gets the data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    instance.GetData();
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 286)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 292)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 298)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static HexBufferSpan FromBounds(HexBufferPoint start, HexBufferPoint end)`
  - Summary: Creates a new instance
  - Parameters:
    - `HexBufferPoint start`: Start point
    - `HexBufferPoint end`: End point
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 120)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexBufferSpan.FromBounds(start: /* HexBufferPoint */, end: /* HexBufferPoint */);
    ```

### Properties

- `public HexBuffer Buffer { get; }`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public HexBufferPoint End => new HexBufferPoint(Buffer, Span.End)`
  - Summary: Gets the end point. This can be 0 if the last byte is at position 2^64-1
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.End;
    ```
- `public HexBufferPoint Start => new HexBufferPoint(Buffer, Span.Start)`
  - Summary: Gets the start point
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Start;
    ```
- `public HexPosition Length => Span.Length`
  - Summary: Gets the length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public HexSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public bool IsDefault => Buffer == null`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```
- `public bool IsEmpty => Span.IsEmpty`
  - Summary: true if it's an empty span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public bool IsFull => Span.IsFull`
  - Summary: true if this span covers everything from 0 to 2^64-1, inclusive
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFull;
    ```

### Operators

- `public static bool operator !=(HexBufferSpan a, HexBufferSpan b) => !a.Equals(b);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 272)
- `public static bool operator ==(HexBufferSpan a, HexBufferSpan b) => a.Equals(b);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 264)
- `public static implicit operator HexSpan(HexBufferSpan hexBufferSpan) => hexBufferSpan.Span;`
  - Summary: Converts this instance to a
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpan.cs` (line 126)

## Class `HexBufferSpanEventArgs`

Hex buffer span event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferSpanEventArgs(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanEventArgs.cs` (line 26)

### Constructors

- `public HexBufferSpanEventArgs(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanEventArgs.cs` (line 36)

### Properties

- `public HexBufferSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Class `HexBufferSpanInvalidatedEventArgs`

Invalidated span event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferSpanInvalidatedEventArgs(span: /* HexSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 708)

### Constructors

- `public HexBufferSpanInvalidatedEventArgs(HexSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 718)

### Properties

- `public HexSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBuffer.cs` (line 712)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Struct `HexBufferSpanSelection`

Buffer span and selection flags

**Inherits/Implements:** `IEquatable<HexBufferSpanSelection>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferSpanSelection(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanSelection.cs` (line 26)

### Constructors

- `public HexBufferSpanSelection(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan bufferSpan`: Buffer span
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanSelection.cs` (line 47)

### Methods

- `public bool Equals(HexBufferSpanSelection other)`
  - Summary: Equals()
  - Parameters:
    - `HexBufferSpanSelection other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanSelection.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* HexBufferSpanSelection */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanSelection.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanSelection.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanSelection.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public HexBufferSpan BufferSpan { get; }`
  - Summary: Buffer span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanSelection.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferSpan;
    ```
- `public HexSpanSelectionFlags SelectionFlags { get; }`
  - Summary: Selection flags or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanSelection.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectionFlags;
    ```
- `public bool IsDefault => BufferSpan.IsDefault`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferSpanSelection.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```

## Class `HexBufferStream`

A stream used by a

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferStream();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 26)

### Constructors

- `protected HexBufferStream()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 30)

### Methods

- `protected HexSpanInfo GetSpanInfo(HexPosition position, HexSpan validSpan)`
  - Summary: Gets information about a position in the stream
  - Parameters:
    - `HexPosition position`: Position
    - `HexSpan validSpan`: Span of all valid data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpanInfo(position: /* HexPosition */, validSpan: /* HexSpan */);
    ```
- `protected virtual void DisposeCore()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 288)
  - Example:
    ```csharp
    // Example invocation
    instance.DisposeCore();
    ```
- `public abstract HexBytes ReadHexBytes(HexPosition position, long length)`
  - Summary: Reads bytes
  - Parameters:
    - `HexPosition position`: Position
    - `long length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 242)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadHexBytes(position: /* HexPosition */, length: /* long */);
    ```
- `public abstract HexSpanInfo GetSpanInfo(HexPosition position)`
  - Summary: Gets information about a position in the stream
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpanInfo(position: /* HexPosition */);
    ```
- `public abstract byte ReadByte(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadByte(position: /* HexPosition */);
    ```
- `public abstract byte[] ReadBytes(HexPosition position, long length)`
  - Summary: Reads bytes
  - Parameters:
    - `HexPosition position`: Position
    - `long length`: Number of bytes to read
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 225)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(position: /* HexPosition */, length: /* long */);
    ```
- `public abstract double ReadDouble(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 161)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadDouble(position: /* HexPosition */);
    ```
- `public abstract double ReadDoubleBigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 217)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadDoubleBigEndian(position: /* HexPosition */);
    ```
- `public abstract float ReadSingle(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 154)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadSingle(position: /* HexPosition */);
    ```
- `public abstract float ReadSingleBigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 210)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadSingleBigEndian(position: /* HexPosition */);
    ```
- `public abstract int ReadInt32(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt32(position: /* HexPosition */);
    ```
- `public abstract int ReadInt32BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt32BigEndian(position: /* HexPosition */);
    ```
- `public abstract int TryReadByte(HexPosition position)`
  - Summary: Tries to read a . If there's no data, a value less than 0 is returned.
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadByte(position: /* HexPosition */);
    ```
- `public abstract long ReadInt64(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt64(position: /* HexPosition */);
    ```
- `public abstract long ReadInt64BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 196)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt64BigEndian(position: /* HexPosition */);
    ```
- `public abstract sbyte ReadSByte(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadSByte(position: /* HexPosition */);
    ```
- `public abstract short ReadInt16(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 112)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt16(position: /* HexPosition */);
    ```
- `public abstract short ReadInt16BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 168)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt16BigEndian(position: /* HexPosition */);
    ```
- `public abstract uint ReadUInt32(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt32(position: /* HexPosition */);
    ```
- `public abstract uint ReadUInt32BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 189)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt32BigEndian(position: /* HexPosition */);
    ```
- `public abstract ulong ReadUInt64(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 147)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt64(position: /* HexPosition */);
    ```
- `public abstract ulong ReadUInt64BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 203)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt64BigEndian(position: /* HexPosition */);
    ```
- `public abstract ushort ReadUInt16(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 119)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt16(position: /* HexPosition */);
    ```
- `public abstract ushort ReadUInt16BigEndian(HexPosition position)`
  - Summary: Reads a
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt16BigEndian(position: /* HexPosition */);
    ```
- `public abstract void ReadBytes(HexPosition position, byte[] destination, long destinationIndex, long length)`
  - Summary: Reads bytes
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] destination`: Destination array
    - `long destinationIndex`: Index
    - `long length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 234)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(position: /* HexPosition */, destination: /* byte[] */, destinationIndex: /* long */, length: /* long */);
    ```
- `public abstract void Write(HexPosition position, byte[] source, long sourceIndex, long length)`
  - Summary: Writes bytes
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] source`: Data
    - `long sourceIndex`: Index
    - `long length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 262)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(position: /* HexPosition */, source: /* byte[] */, sourceIndex: /* long */, length: /* long */);
    ```
- `public virtual void ClearCache()`
  - Summary: Clears the cache if it uses a cache
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.ClearCache();
    ```
- `public void Dispose()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 277)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```
- `public void Write(HexPosition position, byte[] source)`
  - Summary: Writes bytes
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] source`: Data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 249)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(position: /* HexPosition */, source: /* byte[] */);
    ```

### Properties

- `public abstract HexSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public abstract bool IsReadOnly { get; }`
  - Summary: true if it's a read-only stream
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsReadOnly;
    ```
- `public abstract bool IsVolatile { get; }`
  - Summary: true if the content can change at any time
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsVolatile;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the name. This could be the filename if the data was read from a file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public bool IsDisposed { get; private set; }`
  - Summary: true if the instance has been disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 272)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDisposed;
    ```

### Events

- `public abstract event EventHandler<HexBufferStreamSpanInvalidatedEventArgs> BufferStreamSpanInvalidated`
  - Summary: Raised when a span of data got modified by other code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 55)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BufferStreamSpanInvalidated += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public event EventHandler Disposed`
  - Summary: Raised after it is disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 267)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Disposed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexBufferStreamFactoryService`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferStreamFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStreamFactoryService.cs` (line 27)

### Constructors

- `protected HexBufferStreamFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStreamFactoryService.cs` (line 31)

### Methods

- `public HexBufferStream Create(string filename)`
  - Summary: Creates a
  - Parameters:
    - `string filename`: Filename
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStreamFactoryService.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(filename: /* string */);
    ```
- `public HexCachedBufferStream CreateCachedProcessStream(IntPtr hProcess, string name = null, bool isReadOnly = false, bool isVolatile = true)`
  - Summary: Creates a process stream
  - Parameters:
    - `IntPtr hProcess`: Process handle
    - `string name` (default: `null`): Name or null to use the default name
    - `bool isReadOnly` (default: `false`): true if it's read only
    - `bool isVolatile` (default: `true`): true if the memory can be changed by other code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStreamFactoryService.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateCachedProcessStream(hProcess: /* IntPtr */, name: /* string */, isReadOnly: /* bool */, isVolatile: /* bool */);
    ```
- `public abstract HexBufferStream Create(byte[] data, string name)`
  - Summary: Creates a
  - Parameters:
    - `byte[] data`: Data
    - `string name`: Name, can be anything and is usually the filename
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStreamFactoryService.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(data: /* byte[] */, name: /* string */);
    ```
- `public abstract HexCachedBufferStream CreateCached(HexSimpleBufferStream simpleStream, bool disposeStream)`
  - Summary: Creates a
  - Parameters:
    - `HexSimpleBufferStream simpleStream`: Underlying stream
    - `bool disposeStream`: true if the returned stream owns and disposes it when the returned stream gets disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStreamFactoryService.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateCached(simpleStream: /* HexSimpleBufferStream */, disposeStream: /* bool */);
    ```
- `public abstract HexSimpleBufferStream CreateSimpleProcessStream(IntPtr hProcess, string name = null, bool isReadOnly = false, bool isVolatile = true)`
  - Summary: Creates a process stream
  - Parameters:
    - `IntPtr hProcess`: Process handle
    - `string name` (default: `null`): Name or null to use the default name
    - `bool isReadOnly` (default: `false`): true if it's read only
    - `bool isVolatile` (default: `true`): true if the memory can be changed by other code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStreamFactoryService.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateSimpleProcessStream(hProcess: /* IntPtr */, name: /* string */, isReadOnly: /* bool */, isVolatile: /* bool */);
    ```

## Class `HexBufferStreamSpanInvalidatedEventArgs`

Invalidated span event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBufferStreamSpanInvalidatedEventArgs(span: /* HexSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 294)

### Constructors

- `public HexBufferStreamSpanInvalidatedEventArgs(HexSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 304)

### Properties

- `public HexSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBufferStream.cs` (line 298)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Struct `HexBytes`

Contains bytes and information about whether a byte exists in the stream

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexBytes(bytes: /* byte[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 27)

### Constructors

- `public HexBytes(byte[] bytes)`
  - Summary: Constructor
  - Parameters:
    - `byte[] bytes`: All bytes and all of them are valid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 57)
- `public HexBytes(byte[] bytes, BitArray validBytes)`
  - Summary: Constructor
  - Parameters:
    - `byte[] bytes`: All bytes. All invalid bytes should be cleared
    - `BitArray validBytes`: Valid bytes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 79)
- `public HexBytes(byte[] bytes, bool allValid)`
  - Summary: Constructor
  - Parameters:
    - `byte[] bytes`: All bytes
    - `bool allValid`: true if all bytes are valid, false if all bytes are invalid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 68)

### Methods

- `public bool IsValid(int index)`
  - Summary: Checks whether the byte at is valid
  - Parameters:
    - `int index`: Index of byte
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValid(index: /* int */);
    ```
- `public bool IsValid(long index)`
  - Summary: Checks whether the byte at is valid
  - Parameters:
    - `long index`: Index of byte
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 107)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValid(index: /* long */);
    ```
- `public int TryReadByte(int index)`
  - Summary: Returns the byte at or a value less than 0 if the byte is invalid
  - Parameters:
    - `int index`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 118)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadByte(index: /* int */);
    ```
- `public int TryReadByte(long index)`
  - Summary: Returns the at or a value less than 0 if the byte is invalid
  - Parameters:
    - `long index`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 129)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadByte(index: /* long */);
    ```
- `public int? TryReadInt32(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 207)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadInt32(index: /* long */);
    ```
- `public int? TryReadInt32BigEndian(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 331)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadInt32BigEndian(index: /* long */);
    ```
- `public long? TryReadInt64(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 242)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadInt64(index: /* long */);
    ```
- `public long? TryReadInt64BigEndian(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 366)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadInt64BigEndian(index: /* long */);
    ```
- `public sbyte? TryReadSByte(long index)`
  - Summary: Returns the at or null if the byte is invalid
  - Parameters:
    - `long index`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 154)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadSByte(index: /* long */);
    ```
- `public short? TryReadInt16(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 179)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadInt16(index: /* long */);
    ```
- `public short? TryReadInt16BigEndian(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 303)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadInt16BigEndian(index: /* long */);
    ```
- `public uint? TryReadUInt32(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadUInt32(index: /* long */);
    ```
- `public uint? TryReadUInt32BigEndian(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 317)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadUInt32BigEndian(index: /* long */);
    ```
- `public ulong? TryReadUInt64(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 221)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadUInt64(index: /* long */);
    ```
- `public ulong? TryReadUInt64BigEndian(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 345)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadUInt64BigEndian(index: /* long */);
    ```
- `public unsafe double? TryReadDouble(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 276)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadDouble(index: /* long */);
    ```
- `public unsafe double? TryReadDoubleBigEndian(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 400)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadDoubleBigEndian(index: /* long */);
    ```
- `public unsafe float? TryReadSingle(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 263)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadSingle(index: /* long */);
    ```
- `public unsafe float? TryReadSingleBigEndian(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 387)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadSingleBigEndian(index: /* long */);
    ```
- `public ushort? TryReadUInt16(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 165)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadUInt16(index: /* long */);
    ```
- `public ushort? TryReadUInt16BigEndian(long index)`
  - Summary: Returns the at or null if all bytes are invalid
  - Parameters:
    - `long index`: Index of value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 289)
  - Example:
    ```csharp
    // Example invocation
    instance.TryReadUInt16BigEndian(index: /* long */);
    ```
- `public void ReadBytes(long index, byte[] destination, long destinationIndex, long length)`
  - Summary: Reads bytes
  - Parameters:
    - `long index`: Index of data
    - `byte[] destination`: Destination array
    - `long destinationIndex`: Index in
    - `long length`: Number of bytes to copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 415)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(index: /* long */, destination: /* byte[] */, destinationIndex: /* long */, length: /* long */);
    ```

### Properties

- `public bool IsDefault => bytes == null`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```
- `public bool? AllValid => validBytes != null ? (bool?)null : allValid`
  - Summary: Returns true if all bytes are valid, false if all bytes are invalid, or null if it's not known (use )
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AllValid;
    ```
- `public int Length => bytes.Length`
  - Summary: Gets the length in bytes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```

### Indexers

- `public byte this[int index]`
  - Summary: Reads the byte at
  - Parameters:
    - `int index`: Index of byte
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 140)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```
- `public byte this[long index]`
  - Summary: Reads the byte at
  - Parameters:
    - `long index`: Index of byte
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 147)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

### Fields

- `public static readonly HexBytes Empty = new HexBytes(Array.Empty<byte>())`
  - Summary: Gets the empty instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexBytes.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexBytes.Empty;
    ```

## Class `HexCachedBufferStream`

A cached buffer stream

**Inherits/Implements:** `HexBufferStream`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexCachedBufferStream();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCachedBufferStream.cs` (line 24)

### Constructors

- `protected HexCachedBufferStream()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCachedBufferStream.cs` (line 28)

### Methods

- `public abstract void Invalidate(HexSpan span)`
  - Summary: Invalidates a region of memory
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCachedBufferStream.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Invalidate(span: /* HexSpan */);
    ```
- `public void InvalidateAll()`
  - Summary: Invalidates all memory
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCachedBufferStream.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.InvalidateAll();
    ```

## Class `HexCell`

Cell information

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexCell(index: /* int */, groupIndex: /* int */, bufferSpan: /* HexBufferSpan */, textSpan: /* VST.Span */, cellSpan: /* VST.Span */, separatorSpan: /* VST.Span */, fullSpan: /* VST.Span */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 27)

### Constructors

- `public HexCell(int index, int groupIndex, HexBufferSpan bufferSpan, VST.Span textSpan, VST.Span cellSpan, VST.Span separatorSpan, VST.Span fullSpan)`
  - Summary: Constructor
  - Parameters:
    - `int index`: Cell index
    - `int groupIndex`: Group index
    - `HexBufferSpan bufferSpan`: Buffer span or the default value if there's no data
    - `VST.Span textSpan`: Span of the text. This span doesn't include any whitespace before and after the text.
    - `VST.Span cellSpan`: Span of the cell, some of the span could be whitespace
    - `VST.Span separatorSpan`: Span of the cell separator
    - `VST.Span fullSpan`: Includes the whole cell and separator span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 88)

### Methods

- `public VST.Span GetSpan(HexSpanSelectionFlags flags)`
  - Summary: Gets a text span
  - Parameters:
    - `HexSpanSelectionFlags flags`: Flags, only and are checked
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpan(flags: /* HexSpanSelectionFlags */);
    ```

### Properties

- `public HexBufferPoint BufferEnd => BufferSpan.End`
  - Summary: Gets the end position. It's valid if is true
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferEnd;
    ```
- `public HexBufferPoint BufferStart => BufferSpan.Start`
  - Summary: Gets the start position. It's valid if is true
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferStart;
    ```
- `public HexBufferSpan BufferSpan { get; }`
  - Summary: Gets the buffer span. It's valid if is true
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferSpan;
    ```
- `public VST.Span CellSpan { get; }`
  - Summary: Span of the cell, some of the span could be whitespace
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CellSpan;
    ```
- `public VST.Span FullSpan { get; }`
  - Summary: Includes the whole cell and separator span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FullSpan;
    ```
- `public VST.Span SeparatorSpan { get; }`
  - Summary: Span of the cell separator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SeparatorSpan;
    ```
- `public VST.Span TextSpan { get; }`
  - Summary: Span of the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextSpan;
    ```
- `public bool HasData { get; }`
  - Summary: true if there's data in the cell even if there's no memory there; false if it's a blank cell
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasData;
    ```
- `public int GroupIndex { get; }`
  - Summary: Group index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GroupIndex;
    ```
- `public int Index { get; }`
  - Summary: Index in
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCell.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Index;
    ```

## Struct `HexCellCollection`

Hex cell collection

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexCellCollection(cells: /* HexCell[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 29)

### Constructors

- `public HexCellCollection(HexCell[] cells)`
  - Summary: Constructor
  - Parameters:
    - `HexCell[] cells`: All cells
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 64)

### Methods

- `public HexCell GetCell(HexBufferPoint point)`
  - Summary: Gets the cell that contains
  - Parameters:
    - `HexBufferPoint point`: Point
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCell(point: /* HexBufferPoint */);
    ```
- `public IEnumerable<HexCell> GetCells()`
  - Summary: Gets all cells, including unused cells
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCells();
    ```
- `public IEnumerable<HexCell> GetCells(HexBufferSpan span)`
  - Summary: Gets all cells that are contained in . The returned cells are ordered by index.
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCells(span: /* HexBufferSpan */);
    ```
- `public IEnumerable<HexCell> GetVisibleCells()`
  - Summary: Gets all visible cells
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 122)
  - Example:
    ```csharp
    // Example invocation
    instance.GetVisibleCells();
    ```

### Properties

- `public VST.Span HasDataSpan => VST.Span.FromBounds(validStart, validEnd)`
  - Summary: Gets the span of cells in the collection that have data ( is true)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasDataSpan;
    ```
- `public bool IsDefault => cells == null`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```
- `public int Count => cells.Length`
  - Summary: Gets the number of elements in this collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Count;
    ```

### Indexers

- `public HexCell this[int index]`
  - Summary: Gets a cell
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 58)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

### Fields

- `public static readonly HexCellCollection Empty = new HexCellCollection(Array.Empty<HexCell>())`
  - Summary: Gets the empty collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellCollection.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexCellCollection.Empty;
    ```

## Struct `HexCellPosition`

A position within a cell

**Inherits/Implements:** `IEquatable<HexCellPosition>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexCellPosition(column: /* HexColumnType */, bufferPosition: /* HexBufferPoint */, cellPosition: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 26)

### Constructors

- `public HexCellPosition(HexColumnType column, HexBufferPoint bufferPosition, int cellPosition)`
  - Summary: Constructor
  - Parameters:
    - `HexColumnType column`: Column
    - `HexBufferPoint bufferPosition`: Buffer position
    - `int cellPosition`: Position within the cell
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 53)

### Methods

- `public bool Equals(HexCellPosition other)`
  - Summary: Equals()
  - Parameters:
    - `HexCellPosition other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* HexCellPosition */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public HexBufferPoint BufferPosition { get; }`
  - Summary: Gets the buffer position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferPosition;
    ```
- `public HexColumnType Column { get; }`
  - Summary: Gets the column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Column;
    ```
- `public bool IsDefault => BufferPosition.IsDefault`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```
- `public int CellPosition { get; }`
  - Summary: Gets the position within the cell
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CellPosition;
    ```

### Operators

- `public static bool operator !=(HexCellPosition a, HexCellPosition b) => !a.Equals(b);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 79)
- `public static bool operator ==(HexCellPosition a, HexCellPosition b) => a.Equals(b);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexCellPosition.cs` (line 71)

## Class `HexChange`

A change

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexChange();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 24)

### Constructors

- `protected HexChange()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 28)

### Properties

- `public abstract HexPosition NewEnd { get; }`
  - Summary: Gets the new end position after the hex change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewEnd;
    ```
- `public abstract HexPosition NewLength { get; }`
  - Summary: Gets the new length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewLength;
    ```
- `public abstract HexPosition NewPosition { get; }`
  - Summary: Gets the new position after the hex change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewPosition;
    ```
- `public abstract HexPosition OldEnd { get; }`
  - Summary: Gets the old end position before the hex change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldEnd;
    ```
- `public abstract HexPosition OldLength { get; }`
  - Summary: Gets the old length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldLength;
    ```
- `public abstract HexPosition OldPosition { get; }`
  - Summary: Gets the old position before the hex change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldPosition;
    ```
- `public abstract HexSpan NewSpan { get; }`
  - Summary: Gets the span after the hex change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewSpan;
    ```
- `public abstract HexSpan OldSpan { get; }`
  - Summary: Gets the span before the hex change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldSpan;
    ```
- `public abstract byte[] NewData { get; }`
  - Summary: Gets the new data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewData;
    ```
- `public abstract byte[] OldData { get; }`
  - Summary: Gets the old data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldData;
    ```
- `public abstract long Delta { get; }`
  - Summary: Gets the difference in buffer length after the change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexChange.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Delta;
    ```

## Struct `HexColumnPosition`

A position in a hex column

**Inherits/Implements:** `IEquatable<HexColumnPosition>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexColumnPosition(activeColumn: /* HexColumnType */, valuePosition: /* HexCellPosition */, asciiPosition: /* HexCellPosition */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 26)

### Constructors

- `public HexColumnPosition(HexColumnType activeColumn, HexCellPosition valuePosition, HexCellPosition asciiPosition)`
  - Summary: Constructor
  - Parameters:
    - `HexColumnType activeColumn`: Active column
    - `HexCellPosition valuePosition`: Position in the values column
    - `HexCellPosition asciiPosition`: Position in the ASCII column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 68)

### Methods

- `public bool Equals(HexColumnPosition other)`
  - Summary: Equals()
  - Parameters:
    - `HexColumnPosition other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* HexColumnPosition */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 120)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public HexCellPosition ActivePosition {
			get {
				switch (ActiveColumn) {
				case HexColumnType.Values:	return ValuePosition;
				case HexColumnType.Ascii:	return AsciiPosition;
				case HexColumnType.Offset:
				default:
					throw new InvalidOperationException();
				}
			}
		}`
  - Summary: Gets the active position ( or )
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActivePosition;
    ```
- `public HexCellPosition AsciiPosition { get; }`
  - Summary: Position in the ASCII column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsciiPosition;
    ```
- `public HexCellPosition ValuePosition { get; }`
  - Summary: Position in the values column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuePosition;
    ```
- `public HexColumnType ActiveColumn { get; }`
  - Summary: Active column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveColumn;
    ```
- `public bool IsDefault => ValuePosition.IsDefault`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```

### Operators

- `public static bool operator !=(HexColumnPosition a, HexColumnPosition b) => !a.Equals(b);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 94)
- `public static bool operator ==(HexColumnPosition a, HexColumnPosition b) => a.Equals(b);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnPosition.cs` (line 86)

## Enum `HexColumnType`

Hex column

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.HexColumnType and call its members.
var instance = new dnSpy.Contracts.Hex.HexColumnType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexColumnType.cs` (line 24)

### Members

- `Offset`: Offset column
- `Values`: Values column
- `Ascii`: ASCII column

## Class `HexContentChangedEventArgs`

Hex content changed event args

**Inherits/Implements:** `HexVersionChangedEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexContentChangedEventArgs(beforeVersion: /* HexVersion */, afterVersion: /* HexVersion */, editTag: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexContentChangedEventArgs.cs` (line 24)

### Constructors

- `public HexContentChangedEventArgs(HexVersion beforeVersion, HexVersion afterVersion, object editTag)`
  - Summary: Constructor
  - Parameters:
    - `HexVersion beforeVersion`: Version before the change
    - `HexVersion afterVersion`: Version after the change
    - `object editTag`: Edit tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexContentChangedEventArgs.cs` (line 36)

### Properties

- `public NormalizedHexChangeCollection Changes => BeforeVersion.Changes`
  - Summary: Gets the changes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexContentChangedEventArgs.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Changes;
    ```

## Class `HexContentChangingEventArgs`

Hex content changing event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexContentChangingEventArgs(beforeVersion: /* HexVersion */, editTag: /* object */, cancelAction: /* Action<HexContentChangingEventArgs> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexContentChangingEventArgs.cs` (line 26)

### Constructors

- `public HexContentChangingEventArgs(HexVersion beforeVersion, object editTag, Action<HexContentChangingEventArgs> cancelAction)`
  - Summary: Constructor
  - Parameters:
    - `HexVersion beforeVersion`: Version before the change
    - `object editTag`: Edit tag
    - `Action<HexContentChangingEventArgs> cancelAction`: Called when gets called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexContentChangingEventArgs.cs` (line 50)

### Methods

- `public void Cancel()`
  - Summary: Cancels the edit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexContentChangingEventArgs.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.Cancel();
    ```

### Properties

- `public HexVersion BeforeVersion { get; }`
  - Summary: Version before the change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexContentChangingEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BeforeVersion;
    ```
- `public bool Canceled { get; private set; }`
  - Summary: true if has been called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexContentChangingEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Canceled;
    ```
- `public object EditTag { get; }`
  - Summary: Edit tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexContentChangingEventArgs.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EditTag;
    ```

## Class `HexEdit`

Edits a

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexEdit();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 26)

### Constructors

- `protected HexEdit()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 30)

### Methods

- `public abstract bool Replace(HexPosition position, byte value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `byte value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* byte */);
    ```
- `public abstract bool Replace(HexPosition position, byte[] data, long index, long length)`
  - Summary: Replaces the data at with
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] data`: New data
    - `long index`: Index
    - `long length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 152)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, data: /* byte[] */, index: /* long */, length: /* long */);
    ```
- `public abstract bool Replace(HexPosition position, double value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `double value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* double */);
    ```
- `public abstract bool Replace(HexPosition position, float value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `float value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 122)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* float */);
    ```
- `public abstract bool Replace(HexPosition position, int value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `int value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* int */);
    ```
- `public abstract bool Replace(HexPosition position, long value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `long value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* long */);
    ```
- `public abstract bool Replace(HexPosition position, sbyte value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `sbyte value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* sbyte */);
    ```
- `public abstract bool Replace(HexPosition position, short value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `short value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* short */);
    ```
- `public abstract bool Replace(HexPosition position, uint value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `uint value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* uint */);
    ```
- `public abstract bool Replace(HexPosition position, ulong value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `ulong value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* ulong */);
    ```
- `public abstract bool Replace(HexPosition position, ushort value)`
  - Summary: Replaces the at with
  - Parameters:
    - `HexPosition position`: Position
    - `ushort value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, value: /* ushort */);
    ```
- `public abstract void Apply()`
  - Summary: Commits all the modifications
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.Apply();
    ```
- `public abstract void Cancel()`
  - Summary: Cancels all modifications
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 162)
  - Example:
    ```csharp
    // Example invocation
    instance.Cancel();
    ```
- `public abstract void Dispose()`
  - Summary: Disposes this instance. If hasn't been called, the hex edit operation is canceled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 167)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```
- `public bool Replace(HexPosition position, byte[] data)`
  - Summary: Replaces the data at with
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] data`: New data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 138)
  - Example:
    ```csharp
    // Example invocation
    instance.Replace(position: /* HexPosition */, data: /* byte[] */);
    ```

### Properties

- `public abstract HexBuffer Buffer { get; }`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public abstract bool Canceled { get; }`
  - Summary: true if this edit has been canceled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Canceled;
    ```
- `public abstract bool HasEffectiveChanges { get; }`
  - Summary: true if the edit has changes in non-read-only regions
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasEffectiveChanges;
    ```
- `public abstract bool HasFailedChanges { get; }`
  - Summary: true if any changes failed to be added to this edit due to read-only regions
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexEdit.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasFailedChanges;
    ```

## Struct `HexGroupInformation`

Group information

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexGroupInformation(groupIndex: /* int */, fullSpan: /* VST.Span */, span: /* VST.Span */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexGroupInformation.cs` (line 27)

### Constructors

- `public HexGroupInformation(int groupIndex, VST.Span fullSpan, VST.Span span)`
  - Summary: Constructor
  - Parameters:
    - `int groupIndex`: Group index
    - `VST.Span fullSpan`: Full span including a possible separator at the end of the span
    - `VST.Span span`: Span without the separator at the end of the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexGroupInformation.cs` (line 49)

### Properties

- `public VST.Span FullSpan { get; }`
  - Summary: Gets the full span including a possible separator at the end of the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexGroupInformation.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FullSpan;
    ```
- `public VST.Span Span { get; }`
  - Summary: Gets the span without the separator at the end of the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexGroupInformation.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public int GroupIndex { get; }`
  - Summary: Group index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexGroupInformation.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GroupIndex;
    ```

## Struct `HexLinePositionInfo`

Line position info

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.HexLinePositionInfo and call its members.
var instance = new dnSpy.Contracts.Hex.HexLinePositionInfo(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 26)

### Methods

- `public static HexLinePositionInfo CreateAscii(int linePosition, HexCell cell)`
  - Summary: Creates a position within an ASCII cell
  - Parameters:
    - `int linePosition`: Line position
    - `HexCell cell`: Cell
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexLinePositionInfo.CreateAscii(linePosition: /* int */, cell: /* HexCell */);
    ```
- `public static HexLinePositionInfo CreateColumnSeparator(int linePosition)`
  - Summary: Creates a column separator position
  - Parameters:
    - `int linePosition`: Line position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 156)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexLinePositionInfo.CreateColumnSeparator(linePosition: /* int */);
    ```
- `public static HexLinePositionInfo CreateOffset(int linePosition, int offsetIndex)`
  - Summary: Creates a position within the offset column
  - Parameters:
    - `int linePosition`: Line position
    - `int offsetIndex`: Offset character index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexLinePositionInfo.CreateOffset(linePosition: /* int */, offsetIndex: /* int */);
    ```
- `public static HexLinePositionInfo CreateValue(int linePosition, HexCell cell)`
  - Summary: Creates a position within a value cell
  - Parameters:
    - `int linePosition`: Line position
    - `HexCell cell`: Cell
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexLinePositionInfo.CreateValue(linePosition: /* int */, cell: /* HexCell */);
    ```
- `public static HexLinePositionInfo CreateValueCellSeparator(int linePosition, HexCell cell)`
  - Summary: Creates a value cell separator position
  - Parameters:
    - `int linePosition`: Line position
    - `HexCell cell`: Cell
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 129)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexLinePositionInfo.CreateValueCellSeparator(linePosition: /* int */, cell: /* HexCell */);
    ```
- `public static HexLinePositionInfo CreateVirtualSpace(int linePosition, int lineLength)`
  - Summary: Creates a virtual space position
  - Parameters:
    - `int linePosition`: Line position
    - `int lineLength`: Length of line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 168)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexLinePositionInfo.CreateVirtualSpace(linePosition: /* int */, lineLength: /* int */);
    ```

### Properties

- `public HexCell Cell { get; }`
  - Summary: Gets the cell if any
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Cell;
    ```
- `public HexLinePositionInfoType Type { get; }`
  - Summary: Gets the type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public bool IsAsciiCell => Type == HexLinePositionInfoType.AsciiCell`
  - Summary: true if it's a position within an ASCII cell
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAsciiCell;
    ```
- `public bool IsColumnSeparator => Type == HexLinePositionInfoType.ColumnSeparator`
  - Summary: true if it's a position between two columns
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsColumnSeparator;
    ```
- `public bool IsOffset => Type == HexLinePositionInfoType.Offset`
  - Summary: true if it's a position within the offset column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOffset;
    ```
- `public bool IsValueCell => Type == HexLinePositionInfoType.ValueCell`
  - Summary: true if it's a position within a value cell
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsValueCell;
    ```
- `public bool IsValueCellSeparator => Type == HexLinePositionInfoType.ValueCellSeparator`
  - Summary: true if it's a value cell separator position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsValueCellSeparator;
    ```
- `public bool IsVirtualSpace => Type == HexLinePositionInfoType.VirtualSpace`
  - Summary: true if it's a position greater than or equal to the line length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsVirtualSpace;
    ```
- `public int CellPosition { get; }`
  - Summary: Gets the position within the cell, offset column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CellPosition;
    ```
- `public int Position { get; }`
  - Summary: Gets the line position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfo.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Position;
    ```

## Enum `HexLinePositionInfoType`

type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.HexLinePositionInfoType and call its members.
var instance = new dnSpy.Contracts.Hex.HexLinePositionInfoType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLinePositionInfoType.cs` (line 24)

### Members

- `Offset`: Offset column
- `ValueCell`: Value cell
- `ValueCellSeparator`: Value cell separator
- `AsciiCell`: ASCII cell
- `ColumnSeparator`: Column separator
- `VirtualSpace`: Virtual space (a position greater than or equal to the line length)

## Struct `HexLineSpan`

Hex line span

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexLineSpan(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLineSpan.cs` (line 27)

### Constructors

- `public HexLineSpan(HexBufferLine line, VST.Span textSpan)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferLine line`: Line
    - `VST.Span textSpan`: Text span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLineSpan.cs` (line 71)
- `public HexLineSpan(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan bufferSpan`: Buffer span
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLineSpan.cs` (line 58)

### Properties

- `public HexBufferSpan BufferSpan { get; }`
  - Summary: Buffer span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLineSpan.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferSpan;
    ```
- `public HexSpanSelectionFlags? SelectionFlags { get; }`
  - Summary: Selection flags or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLineSpan.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectionFlags;
    ```
- `public VST.Span? TextSpan { get; }`
  - Summary: Line span or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLineSpan.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextSpan;
    ```
- `public bool IsDefault => BufferSpan.IsDefault`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLineSpan.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```
- `public bool IsTextSpan => TextSpan != null`
  - Summary: true if it's a text span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexLineSpan.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsTextSpan;
    ```

## Enum `HexOffsetFormat`

Hex offset format

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.HexOffsetFormat and call its members.
var instance = new dnSpy.Contracts.Hex.HexOffsetFormat(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexOffsetFormat.cs` (line 24)

### Members

- `Hex`: Show just the hex digits
- `HexCSharp`: Use a 0x prefix
- `HexVisualBasic`: Use a &H prefix
- `HexAssembly`: Use a h suffix

## Struct `HexPosition`

A position in a

**Inherits/Implements:** `IEquatable<HexPosition>`, `IComparable<HexPosition>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexPosition(highValue: /* ulong */, lowValue: /* ulong */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 27)

### Constructors

- `public HexPosition(long value)`
  - Summary: Constructor
  - Parameters:
    - `long value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 77)
- `public HexPosition(ulong highValue, ulong lowValue)`
  - Summary: Constructor
  - Parameters:
    - `ulong highValue`: High 64 bits of the value
    - `ulong lowValue`: Low 64 bits of the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 59)
- `public HexPosition(ulong value)`
  - Summary: Constructor
  - Parameters:
    - `ulong value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 68)

### Methods

- `public bool Equals(HexPosition other)`
  - Summary: Compares this instance with
  - Parameters:
    - `HexPosition other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 158)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* HexPosition */);
    ```
- `public int CompareTo(HexPosition other)`
  - Summary: Compares this instance with . Returns less than 0, 0, or greater than 0 depending on whether this instance is less than, equal to, or greather than .
  - Parameters:
    - `HexPosition other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 147)
  - Example:
    ```csharp
    // Example invocation
    instance.CompareTo(other: /* HexPosition */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Compares this instance with
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 165)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 171)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: Gets the value as a string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 177)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static HexPosition Max(HexPosition val1, HexPosition val2)`
  - Summary: Returns the larger of two values
  - Parameters:
    - `HexPosition val1`: First value
    - `HexPosition val2`: Second value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexPosition.Max(val1: /* HexPosition */, val2: /* HexPosition */);
    ```
- `public static HexPosition Min(HexPosition val1, HexPosition val2)`
  - Summary: Returns the smaller of two values
  - Parameters:
    - `HexPosition val1`: First value
    - `HexPosition val2`: Second value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexPosition.Min(val1: /* HexPosition */, val2: /* HexPosition */);
    ```
- `public static HexPosition Parse(string value)`
  - Summary: Parses a string and creates new
  - Parameters:
    - `string value`: String
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexPosition.Parse(value: /* string */);
    ```
- `public static bool TryParse(string value, out HexPosition result)`
  - Summary: Tries to parse a string and creates a
  - Parameters:
    - `string value`: String
    - `out HexPosition result`: Result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 202)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexPosition.TryParse(value: /* string */, result: /* HexPosition */);
    ```
- `public ulong ToUInt64()`
  - Summary: Converts the value to a , truncating the result if it doesn't fit in 64 bits.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.ToUInt64();
    ```

### Fields

- `public static readonly HexPosition MaxEndPosition = new HexPosition(1, 0)`
  - Summary: Max end position (2^64)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexPosition.MaxEndPosition;
    ```
- `public static readonly HexPosition MaxValue = new HexPosition(ulong.MaxValue, ulong.MaxValue)`
  - Summary: Gets the maximum value (2^128-1)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexPosition.MaxValue;
    ```
- `public static readonly HexPosition MinValue = new HexPosition(0)`
  - Summary: Gets the minimum value (0)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexPosition.MinValue;
    ```
- `public static readonly HexPosition Zero = new HexPosition(0)`
  - Summary: Gets the value 0
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexPosition.Zero;
    ```

### Operators

- `public static HexPosition operator +(HexPosition a, HexPosition b) => Add(a, b);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 117)
- `public static HexPosition operator ++(HexPosition a) => Add(a, One);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 120)
- `public static HexPosition operator -(HexPosition a) => Subtract(Zero, a);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 119)
- `public static HexPosition operator -(HexPosition a, HexPosition b) => Subtract(a, b);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 118)
- `public static HexPosition operator --(HexPosition a) => Subtract(a, One);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 121)
- `public static bool operator !=(HexPosition a, HexPosition b) => !a.Equals(b);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 115)
- `public static bool operator <(HexPosition a, HexPosition b) => a.CompareTo(b) < 0;`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 110)
- `public static bool operator <=(HexPosition a, HexPosition b) => a.CompareTo(b) <= 0;`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 111)
- `public static bool operator ==(HexPosition a, HexPosition b) => a.Equals(b);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 114)
- `public static bool operator >(HexPosition a, HexPosition b) => a.CompareTo(b) > 0;`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 112)
- `public static bool operator >=(HexPosition a, HexPosition b) => a.CompareTo(b) >= 0;`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 113)
- `public static implicit operator HexPosition(int value) => new HexPosition(value);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 108)
- `public static implicit operator HexPosition(long value) => new HexPosition(value);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 107)
- `public static implicit operator HexPosition(uint value) => new HexPosition((ulong)value);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 106)
- `public static implicit operator HexPosition(ulong value) => new HexPosition(value);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPosition.cs` (line 105)

## Class `HexPositionConverter`

converter

**Inherits/Implements:** `TypeConverter`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.HexPositionConverter and call its members.
var instance = new dnSpy.Contracts.Hex.HexPositionConverter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPositionConverter.cs` (line 28)

### Methods

- `public override bool CanConvertFrom(ITypeDescriptorContext context, Type sourceType)`
  - Parameters:
    - `ITypeDescriptorContext context`: Description not provided.
    - `Type sourceType`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPositionConverter.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.CanConvertFrom(context: /* ITypeDescriptorContext */, sourceType: /* Type */);
    ```
- `public override object ConvertFrom(ITypeDescriptorContext context, CultureInfo culture, object value)`
  - Parameters:
    - `ITypeDescriptorContext context`: Description not provided.
    - `CultureInfo culture`: Description not provided.
    - `object value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexPositionConverter.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertFrom(context: /* ITypeDescriptorContext */, culture: /* CultureInfo */, value: /* object */);
    ```

## Class `HexSimpleBufferStream`

A buffer stream with less methods

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexSimpleBufferStream();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 26)

### Constructors

- `protected HexSimpleBufferStream()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 30)

### Methods

- `protected HexSpanInfo GetSpanInfo(HexPosition position, HexSpan validSpan)`
  - Summary: Gets information about a position in the stream
  - Parameters:
    - `HexPosition position`: Position
    - `HexSpan validSpan`: Span of all valid data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpanInfo(position: /* HexPosition */, validSpan: /* HexSpan */);
    ```
- `protected virtual void DisposeCore()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    instance.DisposeCore();
    ```
- `public abstract HexPosition Read(HexPosition position, byte[] destination, long destinationIndex, long length)`
  - Summary: Reads bytes. Returns number of bytes read.
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] destination`: Destination array
    - `long destinationIndex`: Index
    - `long length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.Read(position: /* HexPosition */, destination: /* byte[] */, destinationIndex: /* long */, length: /* long */);
    ```
- `public abstract HexPosition Write(HexPosition position, byte[] source, long sourceIndex, long length)`
  - Summary: Writes bytes. Returns number of bytes written.
  - Parameters:
    - `HexPosition position`: Position
    - `byte[] source`: Data
    - `long sourceIndex`: Index
    - `long length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(position: /* HexPosition */, source: /* byte[] */, sourceIndex: /* long */, length: /* long */);
    ```
- `public abstract HexSpanInfo GetSpanInfo(HexPosition position)`
  - Summary: Gets information about a position in the stream
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpanInfo(position: /* HexPosition */);
    ```
- `public virtual void ClearCache()`
  - Summary: Clears the cache if it uses a cache
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.ClearCache();
    ```
- `public void Dispose()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Properties

- `public abstract HexSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public abstract bool IsReadOnly { get; }`
  - Summary: true if it's a read-only stream
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsReadOnly;
    ```
- `public abstract bool IsVolatile { get; }`
  - Summary: true if the content can change at any time
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsVolatile;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the name. This could be the filename if the data was read from a file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public bool IsDisposed { get; private set; }`
  - Summary: true if the instance has been disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDisposed;
    ```
- `public virtual ulong PageSize => 0`
  - Summary: Gets the page size of the underlying data store or 0 if it's unknown. Eg. if it's memory in some process, can be returned here. The returned value must be 0 or a power of 2.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PageSize;
    ```

### Events

- `public event EventHandler Disposed`
  - Summary: Raised after it is disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSimpleBufferStream.cs` (line 111)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Disposed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `HexSpan`

A span in a

**Inherits/Implements:** `IEquatable<HexSpan>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexSpan(start: /* HexPosition */, length: /* ulong */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 26)

### Constructors

- `public HexSpan(HexPosition start, ulong length)`
  - Summary: Constructor
  - Parameters:
    - `HexPosition start`: Position
    - `ulong length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 74)

### Methods

- `public HexSpan? Intersection(HexSpan span)`
  - Summary: Returns the intersection or null if there's none
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 112)
  - Example:
    ```csharp
    // Example invocation
    instance.Intersection(span: /* HexSpan */);
    ```
- `public HexSpan? Overlap(HexSpan span)`
  - Summary: Gets the overlap with or null if there's none
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.Overlap(span: /* HexSpan */);
    ```
- `public bool Contains(HexPosition position)`
  - Summary: Returns true if lies within this span
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    instance.Contains(position: /* HexPosition */);
    ```
- `public bool Contains(HexSpan span)`
  - Summary: Returns true if lies within this span
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.Contains(span: /* HexSpan */);
    ```
- `public bool Equals(HexSpan other)`
  - Summary: Equals()
  - Parameters:
    - `HexSpan other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 169)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* HexSpan */);
    ```
- `public bool IntersectsWith(HexSpan span)`
  - Summary: Returns true if intersects with this instance
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.IntersectsWith(span: /* HexSpan */);
    ```
- `public bool OverlapsWith(HexSpan span)`
  - Summary: Returns true if this instances overlaps with
  - Parameters:
    - `HexSpan span`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.OverlapsWith(span: /* HexSpan */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 176)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static HexSpan FromBounds(HexPosition start, HexPosition end)`
  - Summary: Creates a
  - Parameters:
    - `HexPosition start`: Start position
    - `HexPosition end`: End position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.HexSpan.FromBounds(start: /* HexPosition */, end: /* HexPosition */);
    ```

### Properties

- `public HexPosition End => end`
  - Summary: Gets the end of the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.End;
    ```
- `public HexPosition Length => end - start`
  - Summary: Gets the length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public HexPosition Start => start`
  - Summary: Gets the start of the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Start;
    ```
- `public bool IsEmpty => start == end`
  - Summary: true if it's an empty span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public bool IsFull => start == HexPosition.Zero && end == HexPosition.MaxEndPosition`
  - Summary: true if this span covers everything from 0 to 2^64-1, inclusive
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFull;
    ```

### Fields

- `public static readonly HexSpan FullSpan = new HexSpan(HexPosition.Zero, HexPosition.MaxEndPosition)`
  - Summary: Gets a instance that covers everything from 0 to 2^64-1, inclusive
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.HexSpan.FullSpan;
    ```

### Operators

- `public static bool operator !=(HexSpan left, HexSpan right) => !left.Equals(right);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 162)
- `public static bool operator ==(HexSpan left, HexSpan right) => left.Equals(right);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpan.cs` (line 154)

## Struct `HexSpanInfo`

Information about a span in a

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexSpanInfo(span: /* HexSpan */, flags: /* HexSpanInfoFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpanInfo.cs` (line 42)

### Constructors

- `public HexSpanInfo(HexSpan span, HexSpanInfoFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `HexSpan span`: Span
    - `HexSpanInfoFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpanInfo.cs` (line 63)

### Properties

- `public HexSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpanInfo.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public HexSpanInfoFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpanInfo.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public bool HasData => (Flags & HexSpanInfoFlags.HasData) != 0`
  - Summary: true if contains data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpanInfo.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasData;
    ```

## Enum `HexSpanInfoFlags`

flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.HexSpanInfoFlags and call its members.
var instance = new dnSpy.Contracts.Hex.HexSpanInfoFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpanInfo.cs` (line 26)

### Members

- `None`: No bit is set
- `HasData` = `x00000001`: Set if the span contains data, clear if the span doesn't contain any data

## Enum `HexSpanSelectionFlags`

Span selection flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.HexSpanSelectionFlags and call its members.
var instance = new dnSpy.Contracts.Hex.HexSpanSelectionFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexSpanSelectionFlags.cs` (line 26)

### Members

- `None`: No bit is set
- `Offset` = `x00000001`: Offset column
- `Values` = `x00000002`: Values column
- `Ascii` = `x00000004`: ASCII column
- `Group0` = `x00000008`: Cells in group #0
- `Group1` = `x00000010`: Cells in group #1
- `Cell` = `x00000020`: Select the full cell instead of only the text
- `Separator` = `x00000040`: Include the cell separator, if any
- `OneValue` = `x00000080`: One value at a time
- `AllCells` = `x00000100`: Select all cells in the values/ASCII column
- `AllVisibleCells` = `x00000200`: Select all visible cells in the values/ASCII column
- `Selection` = `alues | Ascii | Cell`: Same as selection, select full cells and cells in values and ASCII columns

## Class `HexTags`

Hex buffer tags

**Inherits/Implements:** `IEnumerable<string>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.HexTags and call its members.
var instance = new dnSpy.Contracts.Hex.HexTags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexTags.cs` (line 28)

### Methods

- `public IEnumerator<string> GetEnumerator()`
  - Summary: Gets all tags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexTags.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEnumerator();
    ```
- `public bool Contains(string tag)`
  - Summary: Checks whether exists in the collection
  - Parameters:
    - `string tag`: Tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexTags.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Contains(tag: /* string */);
    ```

## Enum `HexValuesDisplayFormat`

Hex bytes display format

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.HexValuesDisplayFormat and call its members.
var instance = new dnSpy.Contracts.Hex.HexValuesDisplayFormat(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexValuesDisplayFormat.cs` (line 24)

### Members

- `HexByte`: Hex,
- `HexUInt16`: Hex,
- `HexUInt32`: Hex,
- `HexUInt64`: Hex,
- `HexSByte`: Hex,
- `HexInt16`: Hex,
- `HexInt32`: Hex,
- `HexInt64`: Hex,
- `DecimalByte`: Decimal,
- `DecimalUInt16`: Decimal,
- `DecimalUInt32`: Decimal,
- `DecimalUInt64`: Decimal,
- `DecimalSByte`: Decimal,
- `DecimalInt16`: Decimal,
- `DecimalInt32`: Decimal,
- `DecimalInt64`: Decimal,
- `Single`
- `Double`
- `Bit8`: 8 bits
- `HexUInt16BigEndian`: Hex, , Big Endian
- `HexUInt32BigEndian`: Hex, , Big Endian
- `HexUInt64BigEndian`: Hex, , Big Endian
- `HexInt16BigEndian`: Hex, , Big Endian
- `HexInt32BigEndian`: Hex, , Big Endian
- `HexInt64BigEndian`: Hex, , Big Endian
- `DecimalUInt16BigEndian`: Decimal, , Big Endian
- `DecimalUInt32BigEndian`: Decimal, , Big Endian
- `DecimalUInt64BigEndian`: Decimal, , Big Endian
- `DecimalInt16BigEndian`: Decimal, , Big Endian
- `DecimalInt32BigEndian`: Decimal, , Big Endian
- `DecimalInt64BigEndian`: Decimal, , Big Endian
- `SingleBigEndian`: , Big Endian
- `DoubleBigEndian`: , Big Endian

## Class `HexVersion`

version

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexVersion();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersion.cs` (line 24)

### Constructors

- `protected HexVersion()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersion.cs` (line 28)

### Properties

- `public abstract HexBuffer Buffer { get; }`
  - Summary: Gets the
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersion.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public abstract HexVersion Next { get; }`
  - Summary: Next version or null if this is the latest version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersion.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Next;
    ```
- `public abstract NormalizedHexChangeCollection Changes { get; }`
  - Summary: Gets all hex changes or null if this is the latest version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersion.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Changes;
    ```
- `public abstract int ReiteratedVersionNumber { get; }`
  - Summary: Re-iterated version number used by undo/redo
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersion.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReiteratedVersionNumber;
    ```
- `public abstract int VersionNumber { get; }`
  - Summary: Version number
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersion.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VersionNumber;
    ```

## Class `HexVersionChangedEventArgs`

Hex version changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.HexVersionChangedEventArgs(beforeVersion: /* HexVersion */, afterVersion: /* HexVersion */, editTag: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersionChangedEventArgs.cs` (line 26)

### Constructors

- `protected HexVersionChangedEventArgs(HexVersion beforeVersion, HexVersion afterVersion, object editTag)`
  - Summary: Constructor
  - Parameters:
    - `HexVersion beforeVersion`: Version before the change
    - `HexVersion afterVersion`: Version after the change
    - `object editTag`: Edit tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersionChangedEventArgs.cs` (line 48)

### Properties

- `public HexVersion AfterVersion { get; }`
  - Summary: Version after the change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersionChangedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AfterVersion;
    ```
- `public HexVersion BeforeVersion { get; }`
  - Summary: Version before the change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersionChangedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BeforeVersion;
    ```
- `public object EditTag { get; }`
  - Summary: Edit tag passed to
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/HexVersionChangedEventArgs.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EditTag;
    ```

## Class `NormalizedHexBufferSpanCollection`

Normalized collection

**Inherits/Implements:** `IList<HexBufferSpan>`, `IList`, `IEquatable<NormalizedHexBufferSpanCollection>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.NormalizedHexBufferSpanCollection();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 28)

### Constructors

- `public NormalizedHexBufferSpanCollection()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 40)
- `public NormalizedHexBufferSpanCollection(HexBuffer buffer, HexSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 72)
- `public NormalizedHexBufferSpanCollection(HexBuffer buffer, IEnumerable<HexSpan> spans)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `IEnumerable<HexSpan> spans`: Spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 60)
- `public NormalizedHexBufferSpanCollection(HexBuffer buffer, NormalizedHexSpanCollection spans)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `NormalizedHexSpanCollection spans`: Spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 50)
- `public NormalizedHexBufferSpanCollection(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 81)
- `public NormalizedHexBufferSpanCollection(IEnumerable<HexBufferSpan> spans)`
  - Summary: Constructor
  - Parameters:
    - `IEnumerable<HexBufferSpan> spans`: Spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 92)

### Methods

- `public IEnumerator<HexBufferSpan> GetEnumerator()`
  - Summary: Gets the enumerator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 183)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEnumerator();
    ```
- `public bool Equals(NormalizedHexBufferSpanCollection other)`
  - Summary: Equals()
  - Parameters:
    - `NormalizedHexBufferSpanCollection other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 235)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* NormalizedHexBufferSpanCollection */);
    ```
- `public bool IntersectsWith(HexBufferSpan span)`
  - Summary: Returns true if any of the spans in this instance intersects with
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    instance.IntersectsWith(span: /* HexBufferSpan */);
    ```
- `public bool OverlapsWith(HexBufferSpan span)`
  - Summary: Returns true if any of the spans in this instance overlaps with
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 124)
  - Example:
    ```csharp
    // Example invocation
    instance.OverlapsWith(span: /* HexBufferSpan */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 254)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 260)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 271)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public int Count => coll.Count`
  - Summary: Gets the number of elements in the collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 169)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Count;
    ```

### Indexers

- `public HexBufferSpan this[int index]`
  - Summary: Gets the span at
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 156)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

### Fields

- `public static readonly NormalizedHexBufferSpanCollection Empty = new NormalizedHexBufferSpanCollection()`
  - Summary: An empty collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.NormalizedHexBufferSpanCollection.Empty;
    ```

### Operators

- `public static bool operator !=(NormalizedHexBufferSpanCollection left, NormalizedHexBufferSpanCollection right) => !(left == right);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 228)
- `public static bool operator ==(NormalizedHexBufferSpanCollection left, NormalizedHexBufferSpanCollection right)`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 214)
- `public static implicit operator NormalizedHexSpanCollection(NormalizedHexBufferSpanCollection spans)`
  - Summary: implicit operator NormalizedHexSpanCollection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexBufferSpanCollection.cs` (line 113)

## Class `NormalizedHexChangeCollection`

A normalized read-only collection

**Inherits/Implements:** `IList<HexChange>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.NormalizedHexChangeCollection and call its members.
var instance = new dnSpy.Contracts.Hex.NormalizedHexChangeCollection(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexChangeCollection.cs` (line 30)

### Methods

- `public IEnumerator<HexChange> GetEnumerator()`
  - Summary: Returns an enumerator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexChangeCollection.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEnumerator();
    ```
- `public bool Contains(HexChange item)`
  - Summary: Returns true if is a part of this collection
  - Parameters:
    - `HexChange item`: Item
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexChangeCollection.cs` (line 131)
  - Example:
    ```csharp
    // Example invocation
    instance.Contains(item: /* HexChange */);
    ```
- `public int IndexOf(HexChange item)`
  - Summary: Returns the index of in this collection or a value less than 0 if it's not a part of this collection
  - Parameters:
    - `HexChange item`: Item
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexChangeCollection.cs` (line 138)
  - Example:
    ```csharp
    // Example invocation
    instance.IndexOf(item: /* HexChange */);
    ```
- `public static NormalizedHexChangeCollection Create(HexChange change)`
  - Summary: Creates an instance
  - Parameters:
    - `HexChange change`: Change
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexChangeCollection.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.NormalizedHexChangeCollection.Create(change: /* HexChange */);
    ```
- `public static NormalizedHexChangeCollection Create(IList<HexChange> changes)`
  - Summary: Creates an instance
  - Parameters:
    - `IList<HexChange> changes`: Changes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexChangeCollection.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.NormalizedHexChangeCollection.Create(changes: /* IList<HexChange> */);
    ```
- `public void CopyTo(HexChange[] array, int arrayIndex)`
  - Summary: Copies this collection to an array
  - Parameters:
    - `HexChange[] array`: Destination array
    - `int arrayIndex`: Destination array index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexChangeCollection.cs` (line 145)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(array: /* HexChange[] */, arrayIndex: /* int */);
    ```

### Properties

- `public int Count => changes.Length`
  - Summary: Gets the number of elements in this collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexChangeCollection.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Count;
    ```

### Indexers

- `public HexChange this[int index]`
  - Summary: Gets
  - Parameters:
    - `int index`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexChangeCollection.cs` (line 36)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

## Class `NormalizedHexSpanCollection`

Normalized collection

**Inherits/Implements:** `ReadOnlyCollection<HexSpan>`, `IEquatable<NormalizedHexSpanCollection>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.NormalizedHexSpanCollection();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 29)

### Constructors

- `public NormalizedHexSpanCollection()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 38)
- `public NormalizedHexSpanCollection(HexSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 46)
- `public NormalizedHexSpanCollection(IEnumerable<HexSpan> spans)`
  - Summary: Constructor
  - Parameters:
    - `IEnumerable<HexSpan> spans`: Spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 54)

### Methods

- `public bool Equals(NormalizedHexSpanCollection other)`
  - Summary: Equals()
  - Parameters:
    - `NormalizedHexSpanCollection other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 142)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* NormalizedHexSpanCollection */);
    ```
- `public bool IntersectsWith(HexSpan span)`
  - Summary: Returns true if any of the spans in this instance intersects with
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 107)
  - Example:
    ```csharp
    // Example invocation
    instance.IntersectsWith(span: /* HexSpan */);
    ```
- `public bool OverlapsWith(HexSpan span)`
  - Summary: Returns true if any of the spans in this instance overlaps with
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.OverlapsWith(span: /* HexSpan */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 159)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 165)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 176)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Fields

- `public static readonly NormalizedHexSpanCollection Empty = new NormalizedHexSpanCollection()`
  - Summary: An empty collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.NormalizedHexSpanCollection.Empty;
    ```

### Operators

- `public static bool operator !=(NormalizedHexSpanCollection left, NormalizedHexSpanCollection right) => !(left == right);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 135)
- `public static bool operator ==(NormalizedHexSpanCollection left, NormalizedHexSpanCollection right)`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/NormalizedHexSpanCollection.cs` (line 121)

## Struct `PositionAndData`

Position and data

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.PositionAndData(position: /* HexBufferPoint */, data: /* byte[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/PositionAndData.cs` (line 26)

### Constructors

- `public PositionAndData(HexBufferPoint position, byte[] data)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferPoint position`: Position
    - `byte[] data`: Data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/PositionAndData.cs` (line 47)

### Properties

- `public HexBufferPoint Position { get; }`
  - Summary: Gets the position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/PositionAndData.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Position;
    ```
- `public bool IsDefault => Data == null`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/PositionAndData.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```
- `public byte[] Data { get; }`
  - Summary: Gets the data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/PositionAndData.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```

## Class `PredefinedHexBufferTags`

Predefined tags

**Example**

```csharp
// Access dnSpy.Contracts.Hex.PredefinedHexBufferTags members directly without instantiation.
dnSpy.Contracts.Hex.PredefinedHexBufferTags./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/PredefinedHexBufferTags.cs` (line 24)

### Fields

- `public const string File = nameof(File)`
  - Summary: The underlying stream is a file or a byte array stream
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/PredefinedHexBufferTags.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.PredefinedHexBufferTags.File;
    ```
- `public const string Memory = nameof(Memory)`
  - Summary: The underlying stream is a memory stream
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/PredefinedHexBufferTags.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.PredefinedHexBufferTags.Memory;
    ```

## Struct `TextAndHexSpan`

Text span and hex span

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.TextAndHexSpan(textSpan: /* VST.Span */, bufferSpan: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/TextAndHexSpan.cs` (line 26)

### Constructors

- `public TextAndHexSpan(VST.Span textSpan, HexBufferSpan bufferSpan)`
  - Summary: Constructor
  - Parameters:
    - `VST.Span textSpan`: Text span
    - `HexBufferSpan bufferSpan`: Buffer span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/TextAndHexSpan.cs` (line 42)

### Properties

- `public HexBufferSpan BufferSpan { get; }`
  - Summary: Gets the buffer span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/TextAndHexSpan.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferSpan;
    ```
- `public VST.Span TextSpan { get; }`
  - Summary: Gets the text span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/TextAndHexSpan.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextSpan;
    ```

