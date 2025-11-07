# Namespace `dnSpy.Contracts.Hex.Files`

## Class `ArrayData`

An array

**Inherits/Implements:** `ComplexData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ArrayData(name: /* string */, span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 222)

### Constructors

- `protected ArrayData(string name, HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 228)

### Methods

- `public override BufferField GetFieldByName(string name)`
  - Summary: Gets a field
  - Parameters:
    - `string name`: Name of field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 425)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByName(name: /* string */);
    ```
- `public override void WriteName(HexFieldFormatter formatter)`
  - Summary: Writes the name
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 440)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(formatter: /* HexFieldFormatter */);
    ```
- `public static ArrayData<ByteData> CreateByteArray(HexBuffer buffer, HexPosition position, int elements, string name = null)`
  - Summary: Creates a array
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `int elements`: Number of elements
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 276)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateByteArray(buffer: /* HexBuffer */, position: /* HexPosition */, elements: /* int */, name: /* string */);
    ```
- `public static ArrayData<Int16Data> CreateInt16Array(HexBuffer buffer, HexPosition position, int elements, string name = null)`
  - Summary: Creates a array
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `int elements`: Number of elements
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 371)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateInt16Array(buffer: /* HexBuffer */, position: /* HexPosition */, elements: /* int */, name: /* string */);
    ```
- `public static ArrayData<Int32Data> CreateInt32Array(HexBuffer buffer, HexPosition position, int elements, string name = null)`
  - Summary: Creates a array
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `int elements`: Number of elements
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 390)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateInt32Array(buffer: /* HexBuffer */, position: /* HexPosition */, elements: /* int */, name: /* string */);
    ```
- `public static ArrayData<Int64Data> CreateInt64Array(HexBuffer buffer, HexPosition position, int elements, string name = null)`
  - Summary: Creates a array
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `int elements`: Number of elements
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 409)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateInt64Array(buffer: /* HexBuffer */, position: /* HexPosition */, elements: /* int */, name: /* string */);
    ```
- `public static ArrayData<SByteData> CreateSByteArray(HexBuffer buffer, HexPosition position, int elements, string name = null)`
  - Summary: Creates a array
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `int elements`: Number of elements
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 352)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateSByteArray(buffer: /* HexBuffer */, position: /* HexPosition */, elements: /* int */, name: /* string */);
    ```
- `public static ArrayData<UInt16Data> CreateUInt16Array(HexBuffer buffer, HexPosition position, int elements, string name = null)`
  - Summary: Creates a array
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `int elements`: Number of elements
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 295)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateUInt16Array(buffer: /* HexBuffer */, position: /* HexPosition */, elements: /* int */, name: /* string */);
    ```
- `public static ArrayData<UInt32Data> CreateUInt32Array(HexBuffer buffer, HexPosition position, int elements, string name = null)`
  - Summary: Creates a array
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `int elements`: Number of elements
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 314)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateUInt32Array(buffer: /* HexBuffer */, position: /* HexPosition */, elements: /* int */, name: /* string */);
    ```
- `public static ArrayData<UInt64Data> CreateUInt64Array(HexBuffer buffer, HexPosition position, int elements, string name = null)`
  - Summary: Creates a array
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `int elements`: Number of elements
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 333)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateUInt64Array(buffer: /* HexBuffer */, position: /* HexPosition */, elements: /* int */, name: /* string */);
    ```
- `public static VirtualArrayData<ByteData> CreateVirtualByteArray(HexBufferSpan span, string name = null)`
  - Summary: Creates a virtual array
  - Parameters:
    - `HexBufferSpan span`: Span
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 238)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateVirtualByteArray(span: /* HexBufferSpan */, name: /* string */);
    ```
- `public static VirtualArrayData<UInt16Data> CreateVirtualUInt16Array(HexBufferSpan span, string name = null)`
  - Summary: Creates a virtual array
  - Parameters:
    - `HexBufferSpan span`: Span
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 248)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateVirtualUInt16Array(span: /* HexBufferSpan */, name: /* string */);
    ```
- `public static VirtualArrayData<UInt32Data> CreateVirtualUInt32Array(HexBufferSpan span, string name = null)`
  - Summary: Creates a virtual array
  - Parameters:
    - `HexBufferSpan span`: Span
    - `string name` (default: `null`): Array name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 261)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.ArrayData.CreateVirtualUInt32Array(span: /* HexBufferSpan */, name: /* string */);
    ```

## Class `ArrayData<TData>`

An array whose elements all have the same size

**Inherits/Implements:** `ArrayData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ArrayData<TData>(name: /* string */, span: /* HexBufferSpan */, fields: /* ArrayField<TData>[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 447)

### Constructors

- `public ArrayData(string name, HexBufferSpan span, ArrayField<TData>[] fields)`
  - Summary: Constructor, see eg.
  - Parameters:
    - `string name`: Name
    - `HexBufferSpan span`: Array span
    - `ArrayField<TData>[] fields`: Array elements
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 468)

### Methods

- `public override BufferField GetFieldByIndex(int index)`
  - Summary: Gets a field by index
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 492)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByIndex(index: /* int */);
    ```
- `public override BufferField GetFieldByPosition(HexPosition position)`
  - Summary: Gets a field by position
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 499)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByPosition(position: /* HexPosition */);
    ```

### Properties

- `public override int FieldCount => fields.Length`
  - Summary: Gets the field count
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 460)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FieldCount;
    ```

### Indexers

- `public new ArrayField<TData> this[int index]`
  - Summary: Gets the field at
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 455)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

## Class `ArrayField`

An array field

**Inherits/Implements:** `BufferField`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ArrayField(data: /* BufferData */, index: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 97)

### Constructors

- `public ArrayField(BufferData data, uint index)`
  - Summary: Constructor
  - Parameters:
    - `BufferData data`: Data type
    - `uint index`: Array index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 110)

### Methods

- `public sealed override void WriteName(HexFieldFormatter formatter)`
  - Summary: Writes the field name
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(formatter: /* HexFieldFormatter */);
    ```

### Properties

- `public sealed override string Name => index.ToString()`
  - Summary: Gets the name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 103)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `ArrayField<TData>`

An array field

**Inherits/Implements:** `ArrayField`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ArrayField<TData>(data: /* TData */, index: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 123)

### Constructors

- `public ArrayField(TData data, uint index)`
  - Summary: Constructor
  - Parameters:
    - `TData data`: Data type
    - `uint index`: Array index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 134)

### Properties

- `public new TData Data => (TData)base.Data`
  - Summary: Gets the data type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 127)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```

## Class `BooleanData`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.BooleanData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 28)

### Constructors

- `public BooleanData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 44)
- `public BooleanData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 33)

### Methods

- `public bool ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `BufferData`

Any data

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.BufferData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 27)

### Constructors

- `protected BufferData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 37)

### Properties

- `public HexBufferSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Class `BufferField`

A field

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.BufferField(data: /* BufferData */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 26)

### Constructors

- `protected BufferField(BufferData data)`
  - Summary: Constructor
  - Parameters:
    - `BufferData data`: Data type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 31)

### Methods

- `public abstract void WriteName(HexFieldFormatter formatter)`
  - Summary: Writes the field name
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(formatter: /* HexFieldFormatter */);
    ```

### Properties

- `public BufferData Data { get; }`
  - Summary: Gets the data type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `BufferFileHeadersProvider`

Provides headers

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.BufferFileHeadersProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileHeadersProvider.cs` (line 24)

### Constructors

- `protected BufferFileHeadersProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileHeadersProvider.cs` (line 28)

### Methods

- `public abstract THeader GetHeaders<THeader>() where THeader : class, IBufferFileHeaders`
  - Summary: Returns headers or null. This method is called after
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileHeadersProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHeaders();
    ```

## Class `BufferFileHeadersProviderFactory`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.BufferFileHeadersProviderFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileHeadersProviderFactory.cs` (line 24)

### Constructors

- `protected BufferFileHeadersProviderFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileHeadersProviderFactory.cs` (line 28)

### Methods

- `public abstract BufferFileHeadersProvider Create(HexBufferFile file)`
  - Summary: Creates a or returns null
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileHeadersProviderFactory.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(file: /* HexBufferFile */);
    ```

## Struct `BufferFileOptions`

options

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.BufferFileOptions(span: /* HexSpan */, name: /* string */, filename: /* string */, tags: /* string[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileOptions.cs` (line 26)

### Constructors

- `public BufferFileOptions(HexSpan span, string name, string filename, string[] tags)`
  - Summary: Constructor
  - Parameters:
    - `HexSpan span`: Span of file
    - `string name`: Name
    - `string filename`: Filename if possible, otherwise any name
    - `string[] tags`: Tags, see eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileOptions.cs` (line 59)

### Properties

- `public HexSpan Span { get; }`
  - Summary: Span of file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileOptions.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public bool IsDefault => Name == null`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileOptions.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```
- `public string Filename { get; }`
  - Summary: Filename if possible, otherwise any name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileOptions.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public string Name { get; }`
  - Summary: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileOptions.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public string[] Tags { get; }`
  - Summary: Tags, see eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFileOptions.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tags;
    ```

## Class `BufferFileServiceCreatedEventArgs`

created event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.BufferFileServiceCreatedEventArgs(bufferFileService: /* HexBufferFileService */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileServiceFactory.cs` (line 48)

### Constructors

- `public BufferFileServiceCreatedEventArgs(HexBufferFileService bufferFileService)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferFileService bufferFileService`: Created instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileServiceFactory.cs` (line 58)

### Properties

- `public HexBufferFileService BufferFileService { get; }`
  - Summary: Gets the created instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileServiceFactory.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferFileService;
    ```

## Class `BufferFilesAddedEventArgs`

s added event args

**Inherits/Implements:** `BufferFilesEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.BufferFilesAddedEventArgs(files: /* HexBufferFile[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFilesEventArgs.cs` (line 42)

### Constructors

- `public BufferFilesAddedEventArgs(HexBufferFile[] files)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferFile[] files`: Added files
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFilesEventArgs.cs` (line 47)

## Class `BufferFilesEventArgs`

Buffer files event args base class

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.BufferFilesEventArgs(files: /* HexBufferFile[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFilesEventArgs.cs` (line 26)

### Constructors

- `protected BufferFilesEventArgs(HexBufferFile[] files)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferFile[] files`: Files
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFilesEventArgs.cs` (line 36)

### Properties

- `public HexBufferFile[] Files { get; }`
  - Summary: Gets the files
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFilesEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Files;
    ```

## Class `BufferFilesRemovedEventArgs`

s removed event args

**Inherits/Implements:** `BufferFilesEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.BufferFilesRemovedEventArgs(files: /* HexBufferFile[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFilesEventArgs.cs` (line 55)

### Constructors

- `public BufferFilesRemovedEventArgs(HexBufferFile[] files)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferFile[] files`: Removed files
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferFilesEventArgs.cs` (line 60)

## Class `ByteData`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ByteData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 100)

### Constructors

- `public ByteData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 116)
- `public ByteData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 105)

### Methods

- `public byte ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 124)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `ByteEnumData`

A enum field

**Inherits/Implements:** `EnumData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ByteEnumData(span: /* HexBufferSpan */, enumFieldInfos: /* ReadOnlyCollection<EnumFieldInfo> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 735)

### Constructors

- `public ByteEnumData(HexBuffer buffer, HexPosition position, ReadOnlyCollection<EnumFieldInfo> enumFieldInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `ReadOnlyCollection<EnumFieldInfo> enumFieldInfos`: Enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 753)
- `public ByteEnumData(HexBufferSpan span, ReadOnlyCollection<EnumFieldInfo> enumFieldInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `ReadOnlyCollection<EnumFieldInfo> enumFieldInfos`: Enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 741)

### Methods

- `public byte ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 761)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 767)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `ByteFlagsData`

A flags field

**Inherits/Implements:** `FlagsData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ByteFlagsData(span: /* HexBufferSpan */, flagInfos: /* ReadOnlyCollection<FlagInfo> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 565)

### Constructors

- `public ByteFlagsData(HexBuffer buffer, HexPosition position, ReadOnlyCollection<FlagInfo> flagInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `ReadOnlyCollection<FlagInfo> flagInfos`: Flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 583)
- `public ByteFlagsData(HexBufferSpan span, ReadOnlyCollection<FlagInfo> flagInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `ReadOnlyCollection<FlagInfo> flagInfos`: Flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 571)

### Methods

- `public byte ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 591)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 597)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `CharData`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.CharData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 64)

### Constructors

- `public CharData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 80)
- `public CharData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 69)

### Methods

- `public char ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `ComplexData`

Base class of structures and arrays

**Inherits/Implements:** `BufferData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ComplexData(name: /* string */, span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 73)

### Constructors

- `protected ComplexData(string name, HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 84)

### Methods

- `public BufferField GetSimpleField(HexPosition position)`
  - Summary: Returns the first field (recursively) that contains a or null if none was found. This field could be contained in a nested instance.
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSimpleField(position: /* HexPosition */);
    ```
- `public abstract BufferField GetFieldByIndex(int index)`
  - Summary: Gets a field by index
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByIndex(index: /* int */);
    ```
- `public abstract BufferField GetFieldByName(string name)`
  - Summary: Gets a field
  - Parameters:
    - `string name`: Name of field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByName(name: /* string */);
    ```
- `public abstract BufferField GetFieldByPosition(HexPosition position)`
  - Summary: Gets a field by position
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 118)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByPosition(position: /* HexPosition */);
    ```
- `public abstract void WriteName(HexFieldFormatter formatter)`
  - Summary: Writes the name
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 131)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(formatter: /* HexFieldFormatter */);
    ```

### Properties

- `public abstract int FieldCount { get; }`
  - Summary: Gets the field count
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 104)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FieldCount;
    ```
- `public string Name { get; }`
  - Summary: Gets the name or an empty string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

### Indexers

- `public BufferField this[int index]`
  - Summary: Gets a field
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 92)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```
- `public BufferField this[string name]`
  - Summary: Gets a field
  - Parameters:
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 99)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

## Class `DecimalData`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DecimalData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 496)

### Constructors

- `public DecimalData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 512)
- `public DecimalData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 501)

### Methods

- `public decimal ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 535)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 541)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `DoubleData`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DoubleData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 460)

### Constructors

- `public DoubleData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 476)
- `public DoubleData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 465)

### Methods

- `public double ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 484)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 490)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `EnumData`

Enum data

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.EnumData(span: /* HexBufferSpan */, enumFieldInfos: /* ReadOnlyCollection<EnumFieldInfo> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 717)

### Constructors

- `protected EnumData(HexBufferSpan span, ReadOnlyCollection<EnumFieldInfo> enumFieldInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `ReadOnlyCollection<EnumFieldInfo> enumFieldInfos`: Enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 728)

### Properties

- `public ReadOnlyCollection<EnumFieldInfo> EnumFieldInfos { get; }`
  - Summary: Gets all enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 721)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EnumFieldInfos;
    ```

## Struct `EnumFieldInfo`

Enum field info

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.EnumFieldInfo(value: /* ulong */, name: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/EnumFieldInfo.cs` (line 26)

### Constructors

- `public EnumFieldInfo(ulong value, string name)`
  - Summary: Enum field info
  - Parameters:
    - `ulong value`: Enum field value
    - `string name`: Enum field name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/EnumFieldInfo.cs` (line 42)

### Properties

- `public string Name { get; }`
  - Summary: Gets the enum field name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/EnumFieldInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public ulong Value { get; }`
  - Summary: Gets the enum field value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/EnumFieldInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```

## Struct `FileAndStructure`

File and structure

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.FileAndStructure(file: /* HexBufferFile */, structure: /* ComplexData */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 120)

### Constructors

- `public FileAndStructure(HexBufferFile file, ComplexData structure)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferFile file`: File
    - `ComplexData structure`: Structure
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 136)

### Properties

- `public ComplexData Structure { get; }`
  - Summary: Gets the structure
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Structure;
    ```
- `public HexBufferFile File { get; }`
  - Summary: Gets the file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 124)
  - Example:
    ```csharp
    // Read the property
    var value = instance.File;
    ```

## Struct `FlagInfo`

Flag info

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.FlagInfo(bitMask: /* ulong */, name: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/FlagInfo.cs` (line 26)

### Constructors

- `public FlagInfo(ulong bitMask, string name)`
  - Summary: Constructor
  - Parameters:
    - `ulong bitMask`: Bit mask
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/FlagInfo.cs` (line 71)
- `public FlagInfo(ulong mask, ulong value, string name)`
  - Summary: Constructor
  - Parameters:
    - `ulong mask`: Mask
    - `ulong value`: Value
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/FlagInfo.cs` (line 81)

### Methods

- `public static FlagInfo CreateEnumName(ulong mask, string name)`
  - Summary: Creates an instance that only holds the name of the embedded enum value
  - Parameters:
    - `ulong mask`: Enum mask
    - `string name`: Name of enum
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/FlagInfo.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.FlagInfo.CreateEnumName(mask: /* ulong */, name: /* string */);
    ```

### Properties

- `public bool IsEnumName => (Value & ~Mask) != 0 && Value == EnumNameValue`
  - Summary: true if it only stores the name of the enum and the enum mask. is not used and should be ignored.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/FlagInfo.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnumName;
    ```
- `public string Name { get; }`
  - Summary: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/FlagInfo.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public ulong Mask { get; }`
  - Summary: Mask
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/FlagInfo.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Mask;
    ```
- `public ulong Value { get; }`
  - Summary: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/FlagInfo.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```

## Class `FlagsData`

Flags data

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.FlagsData(span: /* HexBufferSpan */, flagInfos: /* ReadOnlyCollection<FlagInfo> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 547)

### Constructors

- `protected FlagsData(HexBufferSpan span, ReadOnlyCollection<FlagInfo> flagInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `ReadOnlyCollection<FlagInfo> flagInfos`: Flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 558)

### Properties

- `public ReadOnlyCollection<FlagInfo> FlagInfos { get; }`
  - Summary: Gets all flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 551)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FlagInfos;
    ```

## Class `HexBufferFile`

A file in a

**Inherits/Implements:** `VSUTIL.IPropertyOwner`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.HexBufferFile(buffer: /* HexBuffer */, span: /* HexSpan */, name: /* string */, filename: /* string */, tags: /* string[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 30)

### Constructors

- `protected HexBufferFile(HexBuffer buffer, HexSpan span, string name, string filename, string[] tags)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexSpan span`: Span of file
    - `string name`: Name
    - `string filename`: Filename if possible, otherwise any name
    - `string[] tags`: Tags, see eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 39)

### Methods

- `public ComplexData GetStructure(HexPosition position, bool checkNestedFiles = true)`
  - Summary: Gets a structure
  - Parameters:
    - `HexPosition position`: Position
    - `bool checkNestedFiles` (default: `true`): true to check nested files, false to only check this file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 150)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStructure(position: /* HexPosition */, checkNestedFiles: /* bool */);
    ```
- `public HexBufferFile CreateFile(HexSpan span)`
  - Summary: Creates a file. Overlapping files isn't supported.
  - Parameters:
    - `HexSpan span`: Span of file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateFile(span: /* HexSpan */);
    ```
- `public HexBufferFile CreateFile(HexSpan span, string name, string filename, string[] tags)`
  - Summary: Creates a file. Overlapping files isn't supported.
  - Parameters:
    - `HexSpan span`: Span of file
    - `string name`: Name
    - `string filename`: Filename if possible, otherwise any name
    - `string[] tags`: Tags, see eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateFile(span: /* HexSpan */, name: /* string */, filename: /* string */, tags: /* string[] */);
    ```
- `public HexPosition AlignUp(HexPosition position, uint alignment)`
  - Summary: Aligns up. The returned position is aligned relative to the start of the file, not relative to buffer position 0. I.e., if the file starts at position 2, is 3 and is 4, the returned value is 6, not 4.
  - Parameters:
    - `HexPosition position`: Position
    - `uint alignment`: Alignment, must be a power of 2
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 194)
  - Example:
    ```csharp
    // Example invocation
    instance.AlignUp(position: /* HexPosition */, alignment: /* uint */);
    ```
- `public abstract ComplexData GetStructure(string id)`
  - Summary: Gets a structure. Nested files aren't checked.
  - Parameters:
    - `string id`: Id, see eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 166)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStructure(id: /* string */);
    ```
- `public abstract FileAndStructure? GetFileAndStructure(HexPosition position, bool checkNestedFiles = true)`
  - Summary: Gets a structure
  - Parameters:
    - `HexPosition position`: Position
    - `bool checkNestedFiles` (default: `true`): true to check nested files, false to only check this file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 159)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFileAndStructure(position: /* HexPosition */, checkNestedFiles: /* bool */);
    ```
- `public abstract HexBufferFile GetFile(HexPosition position, bool checkNestedFiles)`
  - Summary: Finds a file
  - Parameters:
    - `HexPosition position`: Position
    - `bool checkNestedFiles`: true to check nested files
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFile(position: /* HexPosition */, checkNestedFiles: /* bool */);
    ```
- `public abstract HexBufferFile[] CreateFiles(params BufferFileOptions[] options)`
  - Summary: Creates files. Overlapping files isn't supported.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 119)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateFiles();
    ```
- `public abstract THeaders GetHeaders<THeaders>() where THeaders : class, IBufferFileHeaders`
  - Summary: Gets headers. Nested files aren't checked.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 183)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHeaders();
    ```

### Properties

- `public HexBuffer Buffer { get; }`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public HexSpan Span { get; }`
  - Summary: Gets the file span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public ReadOnlyCollection<string> Tags { get; }`
  - Summary: Gets all the tags, see eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tags;
    ```
- `public VSUTIL.PropertyCollection Properties { get; }`
  - Summary: Gets the properties
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Properties;
    ```
- `public abstract HexBufferFile ParentFile { get; }`
  - Summary: Parent file or null if it's not a nested file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ParentFile;
    ```
- `public abstract IEnumerable<HexBufferFile> Files { get; }`
  - Summary: Gets all nested files
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Files;
    ```
- `public abstract bool IsRemoved { get; }`
  - Summary: true if it has been removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 137)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRemoved;
    ```
- `public abstract bool IsStructuresInitialized { get; }`
  - Summary: true if has been raised
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 171)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsStructuresInitialized;
    ```
- `public bool IsNestedFile => ParentFile != null`
  - Summary: true if it's a nested file ( is not null)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNestedFile;
    ```
- `public string Filename { get; }`
  - Summary: Gets the filename if possible, otherwise it could be any name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public string Name { get; }`
  - Summary: Gets the name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

### Events

- `public abstract event EventHandler Removed`
  - Summary: Raised after it is removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 142)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Removed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler StructuresInitialized`
  - Summary: Raised after the default structures have been added
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 176)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.StructuresInitialized += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<BufferFilesAddedEventArgs> BufferFilesAdded`
  - Summary: Raised after files are added
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFile.cs` (line 124)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BufferFilesAdded += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexBufferFileService`

Creates and removes s from a

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.HexBufferFileService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 28)

### Constructors

- `protected HexBufferFileService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 32)

### Methods

- `public FileAndStructure? GetFileAndStructure(HexPosition position)`
  - Summary: Gets a and structure at or null if there's no structure
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFileAndStructure(position: /* HexPosition */);
    ```
- `public HexBufferFile CreateFile(HexSpan span, string name, string filename, string[] tags)`
  - Summary: Creates a file. Overlapping files isn't supported.
  - Parameters:
    - `HexSpan span`: Span of file
    - `string name`: Name
    - `string filename`: Filename if possible, otherwise any name
    - `string[] tags`: Tags, see eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateFile(span: /* HexSpan */, name: /* string */, filename: /* string */, tags: /* string[] */);
    ```
- `public abstract HexBufferFile GetFile(HexPosition position, bool checkNestedFiles)`
  - Summary: Finds a file
  - Parameters:
    - `HexPosition position`: Position
    - `bool checkNestedFiles`: true to check nested files
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFile(position: /* HexPosition */, checkNestedFiles: /* bool */);
    ```
- `public abstract HexBufferFile[] CreateFiles(params BufferFileOptions[] options)`
  - Summary: Creates files. Overlapping files isn't supported.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateFiles();
    ```
- `public abstract void RemoveFile(HexBufferFile file)`
  - Summary: Removes a file
  - Parameters:
    - `HexBufferFile file`: File to remove
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveFile(file: /* HexBufferFile */);
    ```
- `public abstract void RemoveFiles(HexSpan span)`
  - Summary: Removes all files overlapping with
  - Parameters:
    - `HexSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveFiles(span: /* HexSpan */);
    ```
- `public abstract void RemoveFiles(IEnumerable<HexBufferFile> files)`
  - Summary: Removes files
  - Parameters:
    - `IEnumerable<HexBufferFile> files`: Files to remove
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveFiles(files: /* IEnumerable<HexBufferFile> */);
    ```
- `public void RemoveAllFiles()`
  - Summary: Removes all files
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAllFiles();
    ```

### Properties

- `public abstract HexBuffer Buffer { get; }`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public abstract IEnumerable<HexBufferFile> Files { get; }`
  - Summary: Gets all files
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Files;
    ```

### Events

- `public abstract event EventHandler<BufferFilesAddedEventArgs> BufferFilesAdded`
  - Summary: Raised after files are added
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 88)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BufferFilesAdded += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<BufferFilesRemovedEventArgs> BufferFilesRemoved`
  - Summary: Raised after files are removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileService.cs` (line 93)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BufferFilesRemoved += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexBufferFileServiceFactory`

Creates instances

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.HexBufferFileServiceFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileServiceFactory.cs` (line 26)

### Constructors

- `protected HexBufferFileServiceFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileServiceFactory.cs` (line 30)

### Methods

- `public abstract HexBufferFileService Create(HexBuffer buffer)`
  - Summary: Gets or creates a
  - Parameters:
    - `HexBuffer buffer`: Buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileServiceFactory.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(buffer: /* HexBuffer */);
    ```

### Events

- `public abstract event EventHandler<BufferFileServiceCreatedEventArgs> BufferFileServiceCreated`
  - Summary: Raised after a new is created
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexBufferFileServiceFactory.cs` (line 42)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BufferFileServiceCreated += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexFieldFormatter`

Formats fields and values

**Inherits/Implements:** `HexTextWriter`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.HexFieldFormatter();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 27)

### Constructors

- `protected HexFieldFormatter()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 31)

### Methods

- `public abstract void WriteArrayField(uint index)`
  - Summary: Writes an array field
  - Parameters:
    - `uint index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteArrayField(index: /* uint */);
    ```
- `public abstract void WriteBoolean(bool value)`
  - Summary: Writes a value
  - Parameters:
    - `bool value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteBoolean(value: /* bool */);
    ```
- `public abstract void WriteByte(byte value)`
  - Summary: Writes a value
  - Parameters:
    - `byte value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteByte(value: /* byte */);
    ```
- `public abstract void WriteChar(char value)`
  - Summary: Writes a value
  - Parameters:
    - `char value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteChar(value: /* char */);
    ```
- `public abstract void WriteDecimal(decimal value)`
  - Summary: Writes a value
  - Parameters:
    - `decimal value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteDecimal(value: /* decimal */);
    ```
- `public abstract void WriteDouble(double value)`
  - Summary: Writes a value
  - Parameters:
    - `double value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 169)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteDouble(value: /* double */);
    ```
- `public abstract void WriteEnum(ulong value, ReadOnlyCollection<EnumFieldInfo> infos)`
  - Summary: Writes an enum value
  - Parameters:
    - `ulong value`: Value
    - `ReadOnlyCollection<EnumFieldInfo> infos`: Enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 195)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteEnum(value: /* ulong */, infos: /* ReadOnlyCollection<EnumFieldInfo> */);
    ```
- `public abstract void WriteEquals()`
  - Summary: Writes an equals sign and optional spaces
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteEquals();
    ```
- `public abstract void WriteField(ComplexData structure, HexPosition position)`
  - Summary: Writes the field at
  - Parameters:
    - `ComplexData structure`: Owner structure
    - `HexPosition position`: Position of field within
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteField(structure: /* ComplexData */, position: /* HexPosition */);
    ```
- `public abstract void WriteField(string name)`
  - Summary: Writes a field name
  - Parameters:
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteField(name: /* string */);
    ```
- `public abstract void WriteFilename(string filename)`
  - Summary: Writes a filename which could contain path separators
  - Parameters:
    - `string filename`: Filename with or without path separators
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 201)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteFilename(filename: /* string */);
    ```
- `public abstract void WriteFlags(ulong value, ReadOnlyCollection<FlagInfo> infos)`
  - Summary: Writes flags
  - Parameters:
    - `ulong value`: Value
    - `ReadOnlyCollection<FlagInfo> infos`: Flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteFlags(value: /* ulong */, infos: /* ReadOnlyCollection<FlagInfo> */);
    ```
- `public abstract void WriteInt16(short value)`
  - Summary: Writes a value
  - Parameters:
    - `short value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 145)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteInt16(value: /* short */);
    ```
- `public abstract void WriteInt32(int value)`
  - Summary: Writes a value
  - Parameters:
    - `int value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 151)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteInt32(value: /* int */);
    ```
- `public abstract void WriteInt64(long value)`
  - Summary: Writes a value
  - Parameters:
    - `long value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteInt64(value: /* long */);
    ```
- `public abstract void WriteSByte(sbyte value)`
  - Summary: Writes a value
  - Parameters:
    - `sbyte value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteSByte(value: /* sbyte */);
    ```
- `public abstract void WriteSingle(float value)`
  - Summary: Writes a value
  - Parameters:
    - `float value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 163)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteSingle(value: /* float */);
    ```
- `public abstract void WriteString(string value)`
  - Summary: Writes a value
  - Parameters:
    - `string value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteString(value: /* string */);
    ```
- `public abstract void WriteToken(uint token)`
  - Summary: Writes a .NET metadata token
  - Parameters:
    - `uint token`: Token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteToken(token: /* uint */);
    ```
- `public abstract void WriteUInt16(ushort value)`
  - Summary: Writes a value
  - Parameters:
    - `ushort value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteUInt16(value: /* ushort */);
    ```
- `public abstract void WriteUInt24(uint value)`
  - Summary: Writes a 24-bit value
  - Parameters:
    - `uint value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteUInt24(value: /* uint */);
    ```
- `public abstract void WriteUInt32(uint value)`
  - Summary: Writes a value
  - Parameters:
    - `uint value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 127)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteUInt32(value: /* uint */);
    ```
- `public abstract void WriteUInt64(ulong value)`
  - Summary: Writes a value
  - Parameters:
    - `ulong value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteUInt64(value: /* ulong */);
    ```
- `public abstract void WriteUnknownValue()`
  - Summary: Writes an unknown value, eg. "???"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 206)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteUnknownValue();
    ```
- `public abstract void WriteValue(ComplexData structure, HexPosition position)`
  - Summary: Writes the field value
  - Parameters:
    - `ComplexData structure`: Owner structure
    - `HexPosition position`: Position of field within
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(structure: /* ComplexData */, position: /* HexPosition */);
    ```
- `public virtual void WriteFieldAndValue(ComplexData structure, HexPosition position)`
  - Summary: Writes the field and value
  - Parameters:
    - `ComplexData structure`: Owner structure
    - `HexPosition position`: Position of field within
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteFieldAndValue(structure: /* ComplexData */, position: /* HexPosition */);
    ```
- `public void WriteArray(string name)`
  - Summary: Writes an array name
  - Parameters:
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteArray(name: /* string */);
    ```
- `public void WriteStructure(string name)`
  - Summary: Writes a structure name
  - Parameters:
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatter.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteStructure(name: /* string */);
    ```

## Class `HexFieldFormatterFactory`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.HexFieldFormatterFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatterFactory.cs` (line 26)

### Constructors

- `protected HexFieldFormatterFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatterFactory.cs` (line 30)

### Methods

- `public HexFieldFormatter Create(HexTextWriter writer)`
  - Summary: Creates a formatter
  - Parameters:
    - `HexTextWriter writer`: Text writer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatterFactory.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(writer: /* HexTextWriter */);
    ```
- `public abstract HexFieldFormatter Create(HexTextWriter writer, HexFieldFormatterOptions options, HexNumberOptions arrayIndexOptions, HexNumberOptions valueNumberOptions)`
  - Summary: Creates a formatter
  - Parameters:
    - `HexTextWriter writer`: Text writer
    - `HexFieldFormatterOptions options`: Options
    - `HexNumberOptions arrayIndexOptions`: Array index options
    - `HexNumberOptions valueNumberOptions`: Value number options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatterFactory.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(writer: /* HexTextWriter */, options: /* HexFieldFormatterOptions */, arrayIndexOptions: /* HexNumberOptions */, valueNumberOptions: /* HexNumberOptions */);
    ```

## Enum `HexFieldFormatterOptions`

options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.HexFieldFormatterOptions and call its members.
var instance = new dnSpy.Contracts.Hex.Files.HexFieldFormatterOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFieldFormatterOptions.cs` (line 26)

### Members

- `None`: No bit is set
- `DontPrintDecimalValueInParens` = `x00000001`: Don't show the decimal value in parentheses
- `DontPrintFlagValueInParens` = `x00000002`: Don't show the value of the flag in parentheses
- `DontPrintEnumValueInParens` = `x00000004`: Don't show the value of the enum in parentheses

## Class `HexFileStructureInfoProvider`

Provides tooltips and references

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.HexFileStructureInfoProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 26)

### Constructors

- `protected HexFileStructureInfoProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 30)

### Methods

- `public virtual HexIndexes[] GetSubStructureIndexes(HexBufferFile file, ComplexData structure, HexPosition position)`
  - Summary: Gets indexes of sub structures or null. The returned array must be sorted. If the array is empty, every field is a sub structure.
  - Parameters:
    - `HexBufferFile file`: File
    - `ComplexData structure`: Structure
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSubStructureIndexes(file: /* HexBufferFile */, structure: /* ComplexData */, position: /* HexPosition */);
    ```
- `public virtual HexSpan? GetFieldReferenceSpan(HexBufferFile file, ComplexData structure, HexPosition position)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexBufferFile file`: File
    - `ComplexData structure`: Structure
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(file: /* HexBufferFile */, structure: /* ComplexData */, position: /* HexPosition */);
    ```
- `public virtual object GetReference(HexBufferFile file, ComplexData structure, HexPosition position)`
  - Summary: Returns a reference or null
  - Parameters:
    - `HexBufferFile file`: File
    - `ComplexData structure`: Structure
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.GetReference(file: /* HexBufferFile */, structure: /* ComplexData */, position: /* HexPosition */);
    ```
- `public virtual object GetToolTip(HexBufferFile file, ComplexData structure, HexPosition position)`
  - Summary: Returns a tooltip or null
  - Parameters:
    - `HexBufferFile file`: File
    - `ComplexData structure`: Structure
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetToolTip(file: /* HexBufferFile */, structure: /* ComplexData */, position: /* HexPosition */);
    ```

## Class `HexFileStructureInfoProviderFactory`

Creates instances. Export an instance with a and an optional . See /

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.HexFileStructureInfoProviderFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProviderFactory.cs` (line 29)

### Constructors

- `protected HexFileStructureInfoProviderFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProviderFactory.cs` (line 33)

### Methods

- `public abstract HexFileStructureInfoProvider Create(HexView hexView)`
  - Summary: Creates a or returns null
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProviderFactory.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(hexView: /* HexView */);
    ```

## Class `HexFileStructureInfoService`

Provides tooltips and references

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.HexFileStructureInfoService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoService.cs` (line 24)

### Constructors

- `protected HexFileStructureInfoService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoService.cs` (line 28)

### Methods

- `public abstract HexIndexes[] GetSubStructureIndexes(HexPosition position)`
  - Summary: Gets indexes of sub structures or null. The returned array must be sorted. If the array is empty, every field is a sub structure.
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoService.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSubStructureIndexes(position: /* HexPosition */);
    ```
- `public abstract HexSpan? GetFieldReferenceSpan(HexPosition position)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoService.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(position: /* HexPosition */);
    ```
- `public abstract object GetReference(HexPosition position)`
  - Summary: Returns a reference or null
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoService.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.GetReference(position: /* HexPosition */);
    ```
- `public abstract object GetToolTip(HexPosition position)`
  - Summary: Returns a tooltip or null
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoService.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.GetToolTip(position: /* HexPosition */);
    ```

## Class `HexFileStructureInfoServiceFactory`

Creates instances

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.HexFileStructureInfoServiceFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoServiceFactory.cs` (line 26)

### Constructors

- `protected HexFileStructureInfoServiceFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoServiceFactory.cs` (line 30)

### Methods

- `public abstract HexFileStructureInfoService Create(HexView hexView)`
  - Summary: Creates a or returns an existing one
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoServiceFactory.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(hexView: /* HexView */);
    ```

## Struct `HexIndexes`

Indexes

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.HexIndexes(start: /* int */, length: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 73)

### Constructors

- `public HexIndexes(int start, int length)`
  - Summary: Constructor
  - Parameters:
    - `int start`: Start index
    - `int length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 94)

### Properties

- `public bool IsEmpty => Start == End`
  - Summary: true if it's empty
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public int End { get; }`
  - Summary: Gets the end index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.End;
    ```
- `public int Start { get; }`
  - Summary: Gets the start index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexFileStructureInfoProvider.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Start;
    ```

## Enum `HexNumberOptions`

Formatted number options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.HexNumberOptions and call its members.
var instance = new dnSpy.Contracts.Hex.Files.HexNumberOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/HexNumberOptions.cs` (line 26)

### Members

- `None`: No bit is set
- `HexCSharp` = `x00000000`: C# hex numbers (0x56789ABC)
- `HexVisualBasic` = `x00000001`: Visual Basic hex numbers (&H56789ABC)
- `HexAssembly` = `x00000002`: Assembly language hex numbers (56789ABCh)
- `Hex` = `x00000003`: Hex numbers (56789ABC)
- `Decimal` = `x00000004`: Decimal numbers
- `NumberBaseMask` = `x00000007`: Number base mask
- `LowerCaseHex` = `x40000000`: Lower case hex
- `MinimumDigits` = `nt.MinValue`: Use as few digits as possible

## Interface `IBufferFileHeaders`

Buffer file headers iface

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.IBufferFileHeaders and call its members.
var instance = new dnSpy.Contracts.Hex.Files.IBufferFileHeaders(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/IBufferFileHeaders.cs` (line 24)

## Class `Int16Data`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.Int16Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 316)

### Constructors

- `public Int16Data(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 332)
- `public Int16Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 321)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 346)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public short ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 340)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `Int32Data`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.Int32Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 352)

### Constructors

- `public Int32Data(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 368)
- `public Int32Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 357)

### Methods

- `public int ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 376)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 382)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `Int64Data`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.Int64Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 388)

### Constructors

- `public Int64Data(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 404)
- `public Int64Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 393)

### Methods

- `public long ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 412)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 418)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `PredefinedBufferFileTags`

Predefined tags

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Files.PredefinedBufferFileTags members directly without instantiation.
dnSpy.Contracts.Hex.Files.PredefinedBufferFileTags./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedBufferFileTags.cs` (line 24)

### Fields

- `public static readonly string DotNetMultiFileResource = nameof(DotNetMultiFileResource)`
  - Summary: This file is part of a multi-file .NET resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedBufferFileTags.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedBufferFileTags.DotNetMultiFileResource;
    ```
- `public static readonly string DotNetResources = nameof(DotNetResources)`
  - Summary: The file is part of .NET resources
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedBufferFileTags.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedBufferFileTags.DotNetResources;
    ```
- `public static readonly string FileLayout = nameof(FileLayout)`
  - Summary: Normal file layout, eg. a PE file on disk
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedBufferFileTags.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedBufferFileTags.FileLayout;
    ```
- `public static readonly string MemoryLayout = nameof(MemoryLayout)`
  - Summary: Memory layout, eg. a PE file loaded by the OS
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedBufferFileTags.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedBufferFileTags.MemoryLayout;
    ```
- `public static readonly string SerializedData = nameof(SerializedData)`
  - Summary: The content is serialized data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedBufferFileTags.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedBufferFileTags.SerializedData;
    ```

## Class `PredefinedHexFileStructureInfoProviderFactoryNames`

names

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Files.PredefinedHexFileStructureInfoProviderFactoryNames members directly without instantiation.
dnSpy.Contracts.Hex.Files.PredefinedHexFileStructureInfoProviderFactoryNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedHexFileStructureInfoProviderFactoryNames.cs` (line 24)

### Fields

- `public const string Default = nameof(Default)`
  - Summary: Default
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedHexFileStructureInfoProviderFactoryNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedHexFileStructureInfoProviderFactoryNames.Default;
    ```
- `public const string DotNet = nameof(DotNet)`
  - Summary: .NET
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedHexFileStructureInfoProviderFactoryNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedHexFileStructureInfoProviderFactoryNames.DotNet;
    ```
- `public const string PE = nameof(PE)`
  - Summary: PE
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedHexFileStructureInfoProviderFactoryNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedHexFileStructureInfoProviderFactoryNames.PE;
    ```

## Class `PredefinedStructureProviderFactoryNames`

names

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Files.PredefinedStructureProviderFactoryNames members directly without instantiation.
dnSpy.Contracts.Hex.Files.PredefinedStructureProviderFactoryNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedStructureProviderFactoryNames.cs` (line 24)

### Fields

- `public const string DotNet = nameof(DotNet)`
  - Summary: .NET file data provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedStructureProviderFactoryNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedStructureProviderFactoryNames.DotNet;
    ```
- `public const string DotNetMultiResource = nameof(DotNetMultiResource)`
  - Summary: .NET multi-file resource data provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedStructureProviderFactoryNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedStructureProviderFactoryNames.DotNetMultiResource;
    ```
- `public const string PE = nameof(PE)`
  - Summary: PE file data provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PredefinedStructureProviderFactoryNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PredefinedStructureProviderFactoryNames.PE;
    ```

## Class `SByteData`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.SByteData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 280)

### Constructors

- `public SByteData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 296)
- `public SByteData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 285)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 310)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public sbyte ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 304)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `SimpleData`

Simple data that contains no fields

**Inherits/Implements:** `BufferData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.SimpleData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 47)

### Constructors

- `protected SimpleData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 52)

### Methods

- `public abstract void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public virtual HexSpan? GetFieldReferenceSpan(HexBufferFile file)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(file: /* HexBufferFile */);
    ```

## Class `SingleData`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.SingleData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 424)

### Constructors

- `public SingleData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 440)
- `public SingleData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 429)

### Methods

- `public float ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 448)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 454)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `StringData`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.StringData(span: /* HexBufferSpan */, encoding: /* Encoding */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 887)

### Constructors

- `public StringData(HexBuffer buffer, HexPosition position, int byteLength, Encoding encoding)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `int byteLength`: String length in bytes
    - `Encoding encoding`: Encoding
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 908)
- `public StringData(HexBufferSpan span, Encoding encoding)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `Encoding encoding`: Encoding
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 898)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 922)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public string ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 916)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

### Properties

- `public Encoding Encoding { get; }`
  - Summary: Gets the encoding
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 891)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Encoding;
    ```

## Class `StructField`

A field in a structure

**Inherits/Implements:** `BufferField`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.StructField(name: /* string */, data: /* BufferData */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 53)

### Constructors

- `public StructField(string name, BufferData data)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
    - `BufferData data`: Data type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 65)

### Methods

- `public sealed override void WriteName(HexFieldFormatter formatter)`
  - Summary: Writes the field name
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(formatter: /* HexFieldFormatter */);
    ```

### Properties

- `public sealed override string Name => name`
  - Summary: Gets the field name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `StructField<TData>`

A field in a structure

**Inherits/Implements:** `StructField`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.StructField<TData>(name: /* string */, data: /* TData */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 78)

### Constructors

- `public StructField(string name, TData data)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
    - `TData data`: Data type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 89)

### Properties

- `public new TData Data => (TData)base.Data`
  - Summary: Gets the data type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferField.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```

## Class `StructureData`

A structure

**Inherits/Implements:** `ComplexData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.StructureData(name: /* string */, span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 157)

### Constructors

- `protected StructureData(string name, HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 163)

### Methods

- `public override BufferField GetFieldByName(string name)`
  - Summary: Gets a field
  - Parameters:
    - `string name`: Name of field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 202)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByName(name: /* string */);
    ```
- `public override void WriteName(HexFieldFormatter formatter)`
  - Summary: Writes the name
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 216)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(formatter: /* HexFieldFormatter */);
    ```
- `public sealed override BufferField GetFieldByIndex(int index)`
  - Summary: Gets a field by index
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByIndex(index: /* int */);
    ```
- `public sealed override BufferField GetFieldByPosition(HexPosition position)`
  - Summary: Gets a field by position
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 189)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByPosition(position: /* HexPosition */);
    ```

### Properties

- `protected abstract BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 170)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public sealed override int FieldCount => Fields.Length`
  - Summary: Gets the field count
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 175)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FieldCount;
    ```

## Class `StructureProvider`

Provides instances

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.StructureProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/StructureProvider.cs` (line 26)

### Constructors

- `protected StructureProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/StructureProvider.cs` (line 30)

### Methods

- `public abstract ComplexData GetStructure(HexPosition position)`
  - Summary: Returns a structure at or null
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/StructureProvider.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStructure(position: /* HexPosition */);
    ```
- `public abstract ComplexData GetStructure(string id)`
  - Summary: Returns a structure or null
  - Parameters:
    - `string id`: Id, see eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/StructureProvider.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStructure(id: /* string */);
    ```
- `public abstract bool Initialize()`
  - Summary: Called before any other method, but since this method is allowed to call , the other methods could get called before this instance's method has been called. The method returns false if this instance should be removed (eg. the file isn't supported). This method is allowed to call and but should make sure that any provider it depends on has already been initialized (eg. add a on your class)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/StructureProvider.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.Initialize();
    ```
- `public virtual THeader GetHeaders<THeader>() where THeader : class, IBufferFileHeaders`
  - Summary: Returns headers or null. This method is called before
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/StructureProvider.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHeaders();
    ```

## Class `StructureProviderFactory`

Creates s. Export an instance with a and a , see also

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.StructureProviderFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/StructureProviderFactory.cs` (line 28)

### Constructors

- `protected StructureProviderFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/StructureProviderFactory.cs` (line 32)

### Methods

- `public abstract StructureProvider Create(HexBufferFile file)`
  - Summary: Creates a or returns null
  - Parameters:
    - `HexBufferFile file`: Buffer file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/StructureProviderFactory.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(file: /* HexBufferFile */);
    ```

## Class `UInt16Data`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.UInt16Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 136)

### Constructors

- `public UInt16Data(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 152)
- `public UInt16Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 141)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 166)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public ushort ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 160)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `UInt16EnumData`

A enum field

**Inherits/Implements:** `EnumData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.UInt16EnumData(span: /* HexBufferSpan */, enumFieldInfos: /* ReadOnlyCollection<EnumFieldInfo> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 773)

### Constructors

- `public UInt16EnumData(HexBuffer buffer, HexPosition position, ReadOnlyCollection<EnumFieldInfo> enumFieldInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `ReadOnlyCollection<EnumFieldInfo> enumFieldInfos`: Enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 791)
- `public UInt16EnumData(HexBufferSpan span, ReadOnlyCollection<EnumFieldInfo> enumFieldInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `ReadOnlyCollection<EnumFieldInfo> enumFieldInfos`: Enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 779)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 805)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public ushort ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 799)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `UInt16FlagsData`

A flags field

**Inherits/Implements:** `FlagsData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.UInt16FlagsData(span: /* HexBufferSpan */, flagInfos: /* ReadOnlyCollection<FlagInfo> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 603)

### Constructors

- `public UInt16FlagsData(HexBuffer buffer, HexPosition position, ReadOnlyCollection<FlagInfo> flagInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `ReadOnlyCollection<FlagInfo> flagInfos`: Flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 621)
- `public UInt16FlagsData(HexBufferSpan span, ReadOnlyCollection<FlagInfo> flagInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `ReadOnlyCollection<FlagInfo> flagInfos`: Flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 609)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 635)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public ushort ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 629)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `UInt24Data`

A 24-bit

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.UInt24Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 172)

### Constructors

- `public UInt24Data(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 188)
- `public UInt24Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 177)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 202)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public uint ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 196)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `UInt32Data`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.UInt32Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 208)

### Constructors

- `public UInt32Data(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 224)
- `public UInt32Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 213)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 238)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public uint ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 232)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `UInt32EnumData`

A enum field

**Inherits/Implements:** `EnumData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.UInt32EnumData(span: /* HexBufferSpan */, enumFieldInfos: /* ReadOnlyCollection<EnumFieldInfo> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 811)

### Constructors

- `public UInt32EnumData(HexBuffer buffer, HexPosition position, ReadOnlyCollection<EnumFieldInfo> enumFieldInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `ReadOnlyCollection<EnumFieldInfo> enumFieldInfos`: Enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 829)
- `public UInt32EnumData(HexBufferSpan span, ReadOnlyCollection<EnumFieldInfo> enumFieldInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `ReadOnlyCollection<EnumFieldInfo> enumFieldInfos`: Enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 817)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 843)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public uint ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 837)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `UInt32FlagsData`

A flags field

**Inherits/Implements:** `FlagsData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.UInt32FlagsData(span: /* HexBufferSpan */, flagInfos: /* ReadOnlyCollection<FlagInfo> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 641)

### Constructors

- `public UInt32FlagsData(HexBuffer buffer, HexPosition position, ReadOnlyCollection<FlagInfo> flagInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `ReadOnlyCollection<FlagInfo> flagInfos`: Flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 659)
- `public UInt32FlagsData(HexBufferSpan span, ReadOnlyCollection<FlagInfo> flagInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `ReadOnlyCollection<FlagInfo> flagInfos`: Flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 647)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 673)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public uint ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 667)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `UInt64Data`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.UInt64Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 244)

### Constructors

- `public UInt64Data(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 260)
- `public UInt64Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 249)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 274)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public ulong ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 268)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `UInt64EnumData`

A enum field

**Inherits/Implements:** `EnumData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.UInt64EnumData(span: /* HexBufferSpan */, enumFieldInfos: /* ReadOnlyCollection<EnumFieldInfo> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 849)

### Constructors

- `public UInt64EnumData(HexBuffer buffer, HexPosition position, ReadOnlyCollection<EnumFieldInfo> enumFieldInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `ReadOnlyCollection<EnumFieldInfo> enumFieldInfos`: Enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 867)
- `public UInt64EnumData(HexBufferSpan span, ReadOnlyCollection<EnumFieldInfo> enumFieldInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `ReadOnlyCollection<EnumFieldInfo> enumFieldInfos`: Enum field infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 855)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 881)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public ulong ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 875)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `UInt64FlagsData`

A flags field

**Inherits/Implements:** `FlagsData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.UInt64FlagsData(span: /* HexBufferSpan */, flagInfos: /* ReadOnlyCollection<FlagInfo> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 679)

### Constructors

- `public UInt64FlagsData(HexBuffer buffer, HexPosition position, ReadOnlyCollection<FlagInfo> flagInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `ReadOnlyCollection<FlagInfo> flagInfos`: Flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 697)
- `public UInt64FlagsData(HexBufferSpan span, ReadOnlyCollection<FlagInfo> flagInfos)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `ReadOnlyCollection<FlagInfo> flagInfos`: Flag infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 685)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 711)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```
- `public ulong ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BasicData.cs` (line 705)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```

## Class `VariableLengthArrayData<TData>`

An array whose elements have different sizes

**Inherits/Implements:** `ArrayData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.VariableLengthArrayData<TData>(name: /* string */, span: /* HexBufferSpan */, fields: /* ArrayField<TData>[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 511)

### Constructors

- `public VariableLengthArrayData(string name, HexBufferSpan span, ArrayField<TData>[] fields)`
  - Summary: Constructor, see eg.
  - Parameters:
    - `string name`: Name
    - `HexBufferSpan span`: Array span
    - `ArrayField<TData>[] fields`: Array elements
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 532)

### Methods

- `public override BufferField GetFieldByIndex(int index)`
  - Summary: Gets a field by index
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 540)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByIndex(index: /* int */);
    ```
- `public override BufferField GetFieldByPosition(HexPosition position)`
  - Summary: Gets a field by position
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 547)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByPosition(position: /* HexPosition */);
    ```

### Properties

- `public override int FieldCount => fields.Length`
  - Summary: Gets the field count
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 524)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FieldCount;
    ```

### Indexers

- `public new ArrayField<TData> this[int index]`
  - Summary: Gets the field at
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 519)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

## Class `VirtualArrayData<TData>`

An array whose elements all have the same size and where each element is only created when needed. The elements aren't cached so calling eg. multiple times with the same input will always return new instances.

**Inherits/Implements:** `ArrayData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.VirtualArrayData<TData>(name: /* string */, span: /* HexBufferSpan */, elementLength: /* ulong */, createElement: /* Func<HexBufferPoint, TData> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 564)

### Constructors

- `public VirtualArrayData(string name, HexBufferSpan span, ulong elementLength, Func<HexBufferPoint, TData> createElement)`
  - Summary: Constructor, see eg.
  - Parameters:
    - `string name`: Name
    - `HexBufferSpan span`: Array span
    - `ulong elementLength`: Size of each element in bytes
    - `Func<HexBufferPoint, TData> createElement`: Creates new elements; input parameter is the position of the data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 593)

### Methods

- `public override BufferField GetFieldByIndex(int index)`
  - Summary: Gets a field by index
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 612)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByIndex(index: /* int */);
    ```
- `public override BufferField GetFieldByPosition(HexPosition position)`
  - Summary: Gets a field by position
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 619)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldByPosition(position: /* HexPosition */);
    ```

### Properties

- `public override int FieldCount { get; }`
  - Summary: Gets the field count
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 581)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FieldCount;
    ```

### Indexers

- `public new ArrayField<TData> this[int index]`
  - Summary: Gets the field at
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/BufferData.cs` (line 570)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

