# Namespace `dnSpy.Contracts.Hex.Files.DotNet`

## Class `Bit7EncodedInt32Data`

7-bit encoded integer

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.Bit7EncodedInt32Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/Bit7EncodedInt32Data.cs` (line 26)

### Constructors

- `public Bit7EncodedInt32Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span of data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/Bit7EncodedInt32Data.cs` (line 31)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/Bit7EncodedInt32Data.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `Bit7EncodedStringData`

7-bit encoded string (UTF-8)

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.Bit7EncodedStringData(buffer: /* HexBuffer */, lengthSpan: /* HexSpan */, stringSpan: /* HexSpan */, encoding: /* Encoding */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/Bit7EncodedStringData.cs` (line 27)

### Constructors

- `public Bit7EncodedStringData(HexBuffer buffer, HexSpan lengthSpan, HexSpan stringSpan, Encoding encoding)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexSpan lengthSpan`: Span of length
    - `HexSpan stringSpan`: Span of string data
    - `Encoding encoding`: Encoding
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/Bit7EncodedStringData.cs` (line 52)

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/Bit7EncodedStringData.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public StructField<Bit7EncodedInt32Data> Length { get; }`
  - Summary: Gets the length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/Bit7EncodedStringData.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public StructField<StringData> String { get; }`
  - Summary: Gets the string data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/Bit7EncodedStringData.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.String;
    ```

## Class `BlobEncodedUInt32Data`

Compressed integer stored in #Blob and #US heaps

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.BlobEncodedUInt32Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/BlobEncodedUInt32Data.cs` (line 26)

### Constructors

- `public BlobEncodedUInt32Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span of data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/BlobEncodedUInt32Data.cs` (line 31)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/BlobEncodedUInt32Data.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `BlobHeap`

.NET #Blob heap

**Inherits/Implements:** `DotNetHeap`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.BlobHeap(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 323)

### Constructors

- `protected BlobHeap(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Heap span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 328)

### Methods

- `public HexBufferSpan GetDataSpan(uint offset)`
  - Summary: Gets the span of data in this heap. The span doesn't include the compressed data length at . An empty span is returned if is invalid or 0.
  - Parameters:
    - `uint offset`: Offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 339)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDataSpan(offset: /* uint */);
    ```
- `public byte[] Read(uint offset)`
  - Summary: Reads data at . Returns an empty array if is invalid. The returned data doesn't include the compressed data length at .
  - Parameters:
    - `uint offset`: Offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 358)
  - Example:
    ```csharp
    // Example invocation
    instance.Read(offset: /* uint */);
    ```

## Class `BlobHeapData`

#Blob heap reference

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.BlobHeapData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 366)

### Constructors

- `protected BlobHeapData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 371)

### Methods

- `protected abstract uint ReadOffset()`
  - Summary: Reads the rid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 379)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadOffset();
    ```
- `public override HexSpan? GetFieldReferenceSpan(HexBufferFile file)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 386)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(file: /* HexBufferFile */);
    ```

## Class `BlobHeapData16`

16-bit #Blob heap reference

**Inherits/Implements:** `BlobHeapData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.BlobHeapData16(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 404)

### Constructors

- `public BlobHeapData16(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 420)
- `public BlobHeapData16(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 409)

### Methods

- `protected override uint ReadOffset()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 434)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadOffset();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 428)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `BlobHeapData32`

32-bit #Blob heap reference

**Inherits/Implements:** `BlobHeapData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.BlobHeapData32(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 440)

### Constructors

- `public BlobHeapData32(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 456)
- `public BlobHeapData32(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 445)

### Methods

- `protected override uint ReadOffset()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 470)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadOffset();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 464)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `BlobHeapRecordData`

#Blob heap record data

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.BlobHeapRecordData(buffer: /* HexBuffer */, span: /* HexSpan */, lengthSpan: /* HexSpan */, data: /* BufferData */, tokens: /* ReadOnlyCollection<uint> */, heap: /* BlobHeap */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 189)

### Constructors

- `public BlobHeapRecordData(HexBuffer buffer, HexSpan span, HexSpan lengthSpan, BufferData data, ReadOnlyCollection<uint> tokens, BlobHeap heap)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexSpan span`: Span
    - `HexSpan lengthSpan`: Span of length
    - `BufferData data`: Data
    - `ReadOnlyCollection<uint> tokens`: Tokens referencing this blob or an empty collection
    - `BlobHeap heap`: Owner heap
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 226)

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 215)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public BlobHeap Heap { get; }`
  - Summary: Gets the owner heap
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 195)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Heap;
    ```
- `public ReadOnlyCollection<uint> Tokens { get; }`
  - Summary: Gets the tokens referencing the blob or an empty collection if none (eg. referenced from data in the #Blob)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 200)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tokens;
    ```
- `public StructField<BlobEncodedUInt32Data> Length { get; }`
  - Summary: Gets the length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 205)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public StructField<BufferData> Data { get; }`
  - Summary: Gets the data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 210)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```

## Class `CodedToken`

Contains all possible coded token classes

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.CodedToken(bits: /* int */, tableTypes: /* Table[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 29)

### Constructors

- `public CodedToken(int bits, Table[] tableTypes)`
  - Summary: Constructor
  - Parameters:
    - `int bits`: Number of bits used to encode token type
    - `Table[] tableTypes`: All table types
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 129)

### Methods

- `public MDToken Decode2(uint codedToken)`
  - Summary: Decodes a coded token
  - Parameters:
    - `uint codedToken`: The coded token
  - Returns: Decoded token or 0 on failure
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    instance.Decode2(codedToken: /* uint */);
    ```
- `public bool Decode(uint codedToken, out MDToken token)`
  - Summary: Decodes a coded token
  - Parameters:
    - `uint codedToken`: The coded token
    - `out MDToken token`: Decoded token
  - Returns: true if successful
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 210)
  - Example:
    ```csharp
    // Example invocation
    instance.Decode(codedToken: /* uint */, token: /* MDToken */);
    ```
- `public bool Decode(uint codedToken, out uint token)`
  - Summary: Decodes a coded token
  - Parameters:
    - `uint codedToken`: The coded token
    - `out uint token`: Decoded token
  - Returns: true if successful
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 222)
  - Example:
    ```csharp
    // Example invocation
    instance.Decode(codedToken: /* uint */, token: /* uint */);
    ```
- `public bool Encode(MDToken token, out uint codedToken)`
  - Summary: Encodes a token
  - Parameters:
    - `MDToken token`: The token
    - `out uint codedToken`: Coded token
  - Returns: true if successful
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 162)
  - Example:
    ```csharp
    // Example invocation
    instance.Encode(token: /* MDToken */, codedToken: /* uint */);
    ```
- `public bool Encode(uint token, out uint codedToken)`
  - Summary: Encodes a token
  - Parameters:
    - `uint token`: The token
    - `out uint codedToken`: Coded token
  - Returns: true if successful
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 170)
  - Example:
    ```csharp
    // Example invocation
    instance.Encode(token: /* uint */, codedToken: /* uint */);
    ```
- `public uint Decode(uint codedToken)`
  - Summary: Decodes a coded token
  - Parameters:
    - `uint codedToken`: The coded token
  - Returns: Decoded token or 0 on failure
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.Decode(codedToken: /* uint */);
    ```
- `public uint Encode(MDToken token)`
  - Summary: Encodes a token
  - Parameters:
    - `MDToken token`: The token
  - Returns: Coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    instance.Encode(token: /* MDToken */);
    ```
- `public uint Encode(uint token)`
  - Summary: Encodes a token
  - Parameters:
    - `uint token`: The token
  - Returns: Coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 151)
  - Example:
    ```csharp
    // Example invocation
    instance.Encode(token: /* uint */);
    ```

### Properties

- `public ReadOnlyCollection<Table> TableTypes { get; }`
  - Summary: Returns all types of tables
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 117)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TableTypes;
    ```
- `public int Bits { get; }`
  - Summary: Returns the number of bits that is used to encode table type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 122)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Bits;
    ```

### Fields

- `public static readonly CodedToken CustomAttributeType = new CodedToken(3, new Table[4] {
			0, 0, Table.Method, Table.MemberRef,
		})`
  - Summary: CustomAttributeType coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 87)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.CustomAttributeType;
    ```
- `public static readonly CodedToken HasConstant = new CodedToken(2, new Table[3] {
			Table.Field, Table.Param, Table.Property,
		})`
  - Summary: HasConstant coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.HasConstant;
    ```
- `public static readonly CodedToken HasCustomAttribute = new CodedToken(5, new Table[24] {
			Table.Method, Table.Field, Table.TypeRef, Table.TypeDef,
			Table.Param, Table.InterfaceImpl, Table.MemberRef, Table.Module,
			Table.DeclSecurity, Table.Property, Table.Event, Table.StandAloneSig,
			Table.ModuleRef, Table.TypeSpec, Table.Assembly, Table.AssemblyRef,
			Table.File, Table.ExportedType, Table.ManifestResource, Table.GenericParam,
			Table.GenericParamConstraint, Table.MethodSpec, 0, 0,
		})`
  - Summary: HasCustomAttribute coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.HasCustomAttribute;
    ```
- `public static readonly CodedToken HasCustomDebugInformation = new CodedToken(5, new Table[27] {
			Table.Method, Table.Field, Table.TypeRef, Table.TypeDef,
			Table.Param, Table.InterfaceImpl, Table.MemberRef, Table.Module,
			Table.DeclSecurity, Table.Property, Table.Event, Table.StandAloneSig,
			Table.ModuleRef, Table.TypeSpec, Table.Assembly, Table.AssemblyRef,
			Table.File, Table.ExportedType, Table.ManifestResource, Table.GenericParam,
			Table.GenericParamConstraint, Table.MethodSpec, Table.Document, Table.LocalScope,
			Table.LocalVariable, Table.LocalConstant, Table.ImportScope,
		})`
  - Summary: HasCustomDebugInformation coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 102)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.HasCustomDebugInformation;
    ```
- `public static readonly CodedToken HasDeclSecurity = new CodedToken(2, new Table[3] {
			Table.TypeDef, Table.Method, Table.Assembly,
		})`
  - Summary: HasDeclSecurity coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.HasDeclSecurity;
    ```
- `public static readonly CodedToken HasFieldMarshal = new CodedToken(1, new Table[2] {
			Table.Field, Table.Param,
		})`
  - Summary: HasFieldMarshal coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 51)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.HasFieldMarshal;
    ```
- `public static readonly CodedToken HasSemantic = new CodedToken(1, new Table[2] {
			Table.Event, Table.Property,
		})`
  - Summary: HasSemantic coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 67)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.HasSemantic;
    ```
- `public static readonly CodedToken Implementation = new CodedToken(2, new Table[3] {
			Table.File, Table.AssemblyRef, Table.ExportedType,
		})`
  - Summary: Implementation coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 82)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.Implementation;
    ```
- `public static readonly CodedToken MemberForwarded = new CodedToken(1, new Table[2] {
			Table.Field, Table.Method,
		})`
  - Summary: MemberForwarded coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 77)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.MemberForwarded;
    ```
- `public static readonly CodedToken MemberRefParent = new CodedToken(3, new Table[5] {
			Table.TypeDef, Table.TypeRef, Table.ModuleRef, Table.Method,
			Table.TypeSpec,
		})`
  - Summary: MemberRefParent coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 61)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.MemberRefParent;
    ```
- `public static readonly CodedToken MethodDefOrRef = new CodedToken(1, new Table[2] {
			Table.Method, Table.MemberRef,
		})`
  - Summary: MethodDefOrRef coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 72)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.MethodDefOrRef;
    ```
- `public static readonly CodedToken ResolutionScope = new CodedToken(2, new Table[4] {
			Table.Module, Table.ModuleRef, Table.AssemblyRef, Table.TypeRef,
		})`
  - Summary: ResolutionScope coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 92)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.ResolutionScope;
    ```
- `public static readonly CodedToken TypeDefOrRef = new CodedToken(2, new Table[3] {
			Table.TypeDef, Table.TypeRef, Table.TypeSpec,
		})`
  - Summary: TypeDefOrRef coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.TypeDefOrRef;
    ```
- `public static readonly CodedToken TypeOrMethodDef = new CodedToken(1, new Table[2] {
			Table.TypeDef, Table.Method,
		})`
  - Summary: TypeOrMethodDef coded token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/CodedToken.cs` (line 97)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.CodedToken.TypeOrMethodDef;
    ```

## Class `CodedToken16Data`

16-bit coded .NET metadata token

**Inherits/Implements:** `CodedTokenData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.CodedToken16Data(span: /* HexBufferSpan */, codedToken: /* CodedToken */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 140)

### Constructors

- `public CodedToken16Data(HexBuffer buffer, HexPosition position, CodedToken codedToken)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `CodedToken codedToken`: Coded token info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 158)
- `public CodedToken16Data(HexBufferSpan span, CodedToken codedToken)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `CodedToken codedToken`: Coded token info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 146)

### Methods

- `protected override uint ReadTokenValue()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 166)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadTokenValue();
    ```
- `protected override void WriteValueError(HexFieldFormatter formatter)`
  - Summary: Writes an error
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 172)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValueError(formatter: /* HexFieldFormatter */);
    ```

## Class `CodedToken32Data`

32-bit coded .NET metadata token

**Inherits/Implements:** `CodedTokenData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.CodedToken32Data(span: /* HexBufferSpan */, codedToken: /* CodedToken */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 178)

### Constructors

- `public CodedToken32Data(HexBuffer buffer, HexPosition position, CodedToken codedToken)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `CodedToken codedToken`: Coded token info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 196)
- `public CodedToken32Data(HexBufferSpan span, CodedToken codedToken)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `CodedToken codedToken`: Coded token info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 184)

### Methods

- `protected override uint ReadTokenValue()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 204)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadTokenValue();
    ```
- `protected override void WriteValueError(HexFieldFormatter formatter)`
  - Summary: Writes an error
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 210)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValueError(formatter: /* HexFieldFormatter */);
    ```

## Class `CodedTokenData`

Coded .NET metadata token

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.CodedTokenData(span: /* HexBufferSpan */, codedToken: /* CodedToken */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 75)

### Constructors

- `protected CodedTokenData(HexBufferSpan span, CodedToken codedToken)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `CodedToken codedToken`: Coded token info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 83)

### Methods

- `protected abstract uint ReadTokenValue()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadTokenValue();
    ```
- `protected abstract void WriteValueError(HexFieldFormatter formatter)`
  - Summary: Writes an error
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValueError(formatter: /* HexFieldFormatter */);
    ```
- `public override HexSpan? GetFieldReferenceSpan(HexBufferFile file)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(file: /* HexBufferFile */);
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `ColumnInfo`

Info about one column in a MD table

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.ColumnInfo(index: /* int */, name: /* string */, columnSize: /* ColumnSize */, offset: /* int */, size: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ColumnInfo.cs` (line 28)

### Constructors

- `public ColumnInfo(int index, string name, ColumnSize columnSize, int offset = 0, int size = 0)`
  - Summary: Constructor
  - Parameters:
    - `int index`: Column index
    - `string name`: The column name
    - `ColumnSize columnSize`: Column size
    - `int offset` (default: `0`): Offset of column
    - `int size` (default: `0`): Size of column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ColumnInfo.cs` (line 62)

### Properties

- `public ColumnSize ColumnSize { get; }`
  - Summary: Returns the ColumnSize enum value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ColumnInfo.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ColumnSize;
    ```
- `public int Index { get; }`
  - Summary: Gets the column index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ColumnInfo.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Index;
    ```
- `public int Offset { get; }`
  - Summary: Returns the column offset within the table row
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ColumnInfo.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```
- `public int Size { get; }`
  - Summary: Returns the column size
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ColumnInfo.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Size;
    ```
- `public string Name { get; }`
  - Summary: Returns the column name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ColumnInfo.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Enum `ColumnSize`

MD table column size

**Inherits/Implements:** `byte`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.DotNet.ColumnSize and call its members.
var instance = new dnSpy.Contracts.Hex.Files.DotNet.ColumnSize(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ColumnSize.cs` (line 26)

### Members

- `Module`: RID into Module table
- `TypeRef`: RID into TypeRef table
- `TypeDef`: RID into TypeDef table
- `FieldPtr`: RID into FieldPtr table
- `Field`: RID into Field table
- `MethodPtr`: RID into MethodPtr table
- `Method`: RID into Method table
- `ParamPtr`: RID into ParamPtr table
- `Param`: RID into Param table
- `InterfaceImpl`: RID into InterfaceImpl table
- `MemberRef`: RID into MemberRef table
- `Constant`: RID into Constant table
- `CustomAttribute`: RID into CustomAttribute table
- `FieldMarshal`: RID into FieldMarshal table
- `DeclSecurity`: RID into DeclSecurity table
- `ClassLayout`: RID into ClassLayout table
- `FieldLayout`: RID into FieldLayout table
- `StandAloneSig`: RID into StandAloneSig table
- `EventMap`: RID into EventMap table
- `EventPtr`: RID into EventPtr table
- `Event`: RID into Event table
- `PropertyMap`: RID into PropertyMap table
- `PropertyPtr`: RID into PropertyPtr table
- `Property`: RID into Property table
- `MethodSemantics`: RID into MethodSemantics table
- `MethodImpl`: RID into MethodImpl table
- `ModuleRef`: RID into ModuleRef table
- `TypeSpec`: RID into TypeSpec table
- `ImplMap`: RID into ImplMap table
- `FieldRVA`: RID into FieldRVA table
- `ENCLog`: RID into ENCLog table
- `ENCMap`: RID into ENCMap table
- `Assembly`: RID into Assembly table
- `AssemblyProcessor`: RID into AssemblyProcessor table
- `AssemblyOS`: RID into AssemblyOS table
- `AssemblyRef`: RID into AssemblyRef table
- `AssemblyRefProcessor`: RID into AssemblyRefProcessor table
- `AssemblyRefOS`: RID into AssemblyRefOS table
- `File`: RID into File table
- `ExportedType`: RID into ExportedType table
- `ManifestResource`: RID into ManifestResource table
- `NestedClass`: RID into NestedClass table
- `GenericParam`: RID into GenericParam table
- `MethodSpec`: RID into MethodSpec table
- `GenericParamConstraint`: RID into GenericParamConstraint table
- `Document` = `x30`: RID into Document table
- `MethodDebugInformation`: RID into MethodDebugInformation table
- `LocalScope`: RID into LocalScope table
- `LocalVariable`: RID into LocalVariable table
- `LocalConstant`: RID into LocalConstant table
- `ImportScope`: RID into ImportScope table
- `StateMachineMethod`: RID into StateMachineMethod table
- `CustomDebugInformation`: RID into CustomDebugInformation table
- `Byte` = `x40`: 8-bit byte
- `Int16`: 16-bit signed int
- `UInt16`: 16-bit unsigned int
- `Int32`: 32-bit signed int
- `UInt32`: 32-bit unsigned int
- `Strings`: Index into #Strings stream
- `GUID`: Index into #GUID stream
- `Blob`: Index into #Blob stream
- `TypeDefOrRef`: TypeDefOrRef encoded token
- `HasConstant`: HasConstant encoded token
- `HasCustomAttribute`: HasCustomAttribute encoded token
- `HasFieldMarshal`: HasFieldMarshal encoded token
- `HasDeclSecurity`: HasDeclSecurity encoded token
- `MemberRefParent`: MemberRefParent encoded token
- `HasSemantic`: HasSemantic encoded token
- `MethodDefOrRef`: MethodDefOrRef encoded token
- `MemberForwarded`: MemberForwarded encoded token
- `Implementation`: Implementation encoded token
- `CustomAttributeType`: CustomAttributeType encoded token
- `ResolutionScope`: ResolutionScope encoded token
- `TypeOrMethodDef`: TypeOrMethodDef encoded token
- `HasCustomDebugInformation`: HasCustomDebugInformation encoded token

## Class `DateTimeData`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DateTimeData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 27)

### Constructors

- `public DateTimeData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 43)
- `public DateTimeData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 32)

### Methods

- `public DateTime ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `DotNetCor20Data`

COR20 header

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetCor20Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 26)

### Constructors

- `protected DotNetCor20Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 33)

### Properties

- `public abstract StructField<DataDirectoryData> CodeManagerTable { get; }`
  - Summary: IMAGE_COR20_HEADER.CodeManagerTable
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CodeManagerTable;
    ```
- `public abstract StructField<DataDirectoryData> ExportAddressTableJumps { get; }`
  - Summary: IMAGE_COR20_HEADER.ExportAddressTableJumps
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExportAddressTableJumps;
    ```
- `public abstract StructField<DataDirectoryData> ManagedNativeHeader { get; }`
  - Summary: IMAGE_COR20_HEADER.ManagedNativeHeader
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ManagedNativeHeader;
    ```
- `public abstract StructField<DataDirectoryData> Metadata { get; }`
  - Summary: IMAGE_COR20_HEADER.MetaData
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Metadata;
    ```
- `public abstract StructField<DataDirectoryData> Resources { get; }`
  - Summary: IMAGE_COR20_HEADER.Resources
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Resources;
    ```
- `public abstract StructField<DataDirectoryData> StrongNameSignature { get; }`
  - Summary: IMAGE_COR20_HEADER.StrongNameSignature
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StrongNameSignature;
    ```
- `public abstract StructField<DataDirectoryData> VTableFixups { get; }`
  - Summary: IMAGE_COR20_HEADER.VTableFixups
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VTableFixups;
    ```
- `public abstract StructField<UInt16Data> MajorRuntimeVersion { get; }`
  - Summary: IMAGE_COR20_HEADER.MajorRuntimeVersion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MajorRuntimeVersion;
    ```
- `public abstract StructField<UInt16Data> MinorRuntimeVersion { get; }`
  - Summary: IMAGE_COR20_HEADER.MinorRuntimeVersion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MinorRuntimeVersion;
    ```
- `public abstract StructField<UInt32Data> Cb { get; }`
  - Summary: IMAGE_COR20_HEADER.cb
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Cb;
    ```
- `public abstract StructField<UInt32Data> EntryPointTokenOrRVA { get; }`
  - Summary: IMAGE_COR20_HEADER.EntryPointToken / IMAGE_COR20_HEADER.EntryPointRVA
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EntryPointTokenOrRVA;
    ```
- `public abstract StructField<UInt32FlagsData> Flags { get; }`
  - Summary: IMAGE_COR20_HEADER.Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetCor20Data.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```

## Class `DotNetEmbeddedResource`

.NET embedded resource

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetEmbeddedResource(resourceProvider: /* DotNetResourceProvider */, span: /* HexBufferSpan */, token: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetEmbeddedResource.cs` (line 26)

### Constructors

- `protected DotNetEmbeddedResource(DotNetResourceProvider resourceProvider, HexBufferSpan span, uint token)`
  - Summary: Constructor
  - Parameters:
    - `DotNetResourceProvider resourceProvider`: Owner
    - `HexBufferSpan span`: Span
    - `uint token`: Token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetEmbeddedResource.cs` (line 45)

### Properties

- `public DotNetResourceProvider ResourceProvider { get; }`
  - Summary: Gets the owner instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetEmbeddedResource.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResourceProvider;
    ```
- `public MDToken Token { get; }`
  - Summary: Gets the token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetEmbeddedResource.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```
- `public abstract StructField<UInt32Data> Size { get; }`
  - Summary: Gets the size of the resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetEmbeddedResource.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Size;
    ```
- `public abstract StructField<VirtualArrayData<ByteData>> Content { get; }`
  - Summary: Gets the resource content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetEmbeddedResource.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Content;
    ```

## Class `DotNetHeaders`

.NET headers, present if the COR20 header exists in a PE file. The .NET metadata could still be null.

**Inherits/Implements:** `IBufferFileHeaders`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetHeaders();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeaders.cs` (line 26)

### Constructors

- `protected DotNetHeaders()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeaders.cs` (line 30)

### Properties

- `public abstract DotNetCor20Data Cor20 { get; }`
  - Summary: Gets the COR20 header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeaders.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Cor20;
    ```
- `public abstract DotNetMetadataHeaders MetadataHeaders { get; }`
  - Summary: Gets the .NET metadata-only headers or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeaders.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataHeaders;
    ```
- `public abstract DotNetMethodProvider MethodProvider { get; }`
  - Summary: Gets the method provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeaders.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MethodProvider;
    ```
- `public abstract DotNetResourceProvider ResourceProvider { get; }`
  - Summary: Gets the .NET resource provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeaders.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResourceProvider;
    ```
- `public abstract PeHeaders PeHeaders { get; }`
  - Summary: Gets the PE headers
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeaders.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PeHeaders;
    ```
- `public abstract VirtualArrayData<ByteData> StrongNameSignature { get; }`
  - Summary: Gets the strong name signature or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeaders.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StrongNameSignature;
    ```

## Class `DotNetHeap`

A .NET heap

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetHeap(span: /* HexBufferSpan */, heapKind: /* DotNetHeapKind */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 28)

### Constructors

- `protected DotNetHeap(HexBufferSpan span, DotNetHeapKind heapKind)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Heap span
    - `DotNetHeapKind heapKind`: Heap kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 34)

### Methods

- `protected int? ReadCompressedUInt32(ref HexPosition position)`
  - Summary: Reads a compressed and increments
  - Parameters:
    - `ref HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadCompressedUInt32(position: /* HexPosition */);
    ```
- `public virtual ComplexData GetStructure(HexPosition position)`
  - Summary: Gets a structure or null
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStructure(position: /* HexPosition */);
    ```
- `public virtual bool IsValidOffset(uint offset)`
  - Summary: Checks whether is valid. Note that some heaps treat as an index, eg. .
  - Parameters:
    - `uint offset`: Offset (or index if #GUID heap)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValidOffset(offset: /* uint */);
    ```

### Properties

- `public DotNetHeapKind HeapKind { get; }`
  - Summary: Gets the heap kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HeapKind;
    ```
- `public HexBufferSpan Span { get; }`
  - Summary: Gets the heap span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public abstract DotNetMetadataHeaders Metadata { get; }`
  - Summary: Gets the metadata headers
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Metadata;
    ```

## Enum `DotNetHeapKind`

.NET heap kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.DotNet.DotNetHeapKind and call its members.
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetHeapKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeapKind.cs` (line 24)

### Members

- `Unknown`: Unknown
- `Tables`: Tables heap (#~ or #-)
- `Strings`: #Strings
- `US`: #US
- `GUID`: #GUID
- `Blob`: #Blob
- `Hot`: #!
- `Pdb`: #Pdb

## Class `DotNetMetadataHeaderData`

.NET metadata header

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetMetadataHeaderData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 24)

### Constructors

- `protected DotNetMetadataHeaderData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 31)

### Properties

- `public abstract StructField<ByteData> Pad { get; }`
  - Summary: STORAGEHEADER.pad
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Pad;
    ```
- `public abstract StructField<ByteFlagsData> Flags { get; }`
  - Summary: STORAGEHEADER.fFlags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public abstract StructField<StringData> VersionString { get; }`
  - Summary: STORAGESIGNATURE.VersionString
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VersionString;
    ```
- `public abstract StructField<UInt16Data> MajorVersion { get; }`
  - Summary: STORAGESIGNATURE.iMajorVer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MajorVersion;
    ```
- `public abstract StructField<UInt16Data> MinorVersion { get; }`
  - Summary: STORAGESIGNATURE.iMinorVer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MinorVersion;
    ```
- `public abstract StructField<UInt16Data> StreamCount { get; }`
  - Summary: STORAGEHEADER.iStreams
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StreamCount;
    ```
- `public abstract StructField<UInt32Data> ExtraData { get; }`
  - Summary: STORAGESIGNATURE.iExtraData
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExtraData;
    ```
- `public abstract StructField<UInt32Data> Signature { get; }`
  - Summary: STORAGESIGNATURE.lSignature
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Signature;
    ```
- `public abstract StructField<UInt32Data> VersionStringCount { get; }`
  - Summary: STORAGESIGNATURE.iVersionString
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VersionStringCount;
    ```
- `public abstract StructField<VariableLengthArrayData<DotNetStorageStream>> StreamHeaders { get; }`
  - Summary: Streams following STORAGEHEADER.iStreams
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaderData.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StreamHeaders;
    ```

## Class `DotNetMetadataHeaders`

.NET metadata-only headers, present if the file is a .NET PE file or a .NET metadata only file (eg. portable pdb file)

**Inherits/Implements:** `IBufferFileHeaders`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetMetadataHeaders(metadataSpan: /* HexSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 26)

### Constructors

- `protected DotNetMetadataHeaders(HexSpan metadataSpan)`
  - Summary: Constructor
  - Parameters:
    - `HexSpan metadataSpan`: Metadata span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 31)

### Methods

- `public abstract ComplexData GetStructure(HexPosition position)`
  - Summary: Returns a structure at or null
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStructure(position: /* HexPosition */);
    ```

### Properties

- `public HexSpan MetadataSpan { get; }`
  - Summary: Gets the metadata span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataSpan;
    ```
- `public abstract BlobHeap BlobStream { get; }`
  - Summary: Gets the #Blob stream or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BlobStream;
    ```
- `public abstract DotNetMetadataHeaderData MetadataHeader { get; }`
  - Summary: Gets the metadata header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataHeader;
    ```
- `public abstract GUIDHeap GUIDStream { get; }`
  - Summary: Gets the #GUID stream or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GUIDStream;
    ```
- `public abstract PdbHeap PdbStream { get; }`
  - Summary: Gets the #Pdb stream or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PdbStream;
    ```
- `public abstract ReadOnlyCollection<DotNetHeap> Streams { get; }`
  - Summary: Gets all heaps
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Streams;
    ```
- `public abstract StringsHeap StringsStream { get; }`
  - Summary: Gets the #Strings stream or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StringsStream;
    ```
- `public abstract TablesHeap TablesStream { get; }`
  - Summary: Gets the tables stream (#~ or #-) or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TablesStream;
    ```
- `public abstract USHeap USStream { get; }`
  - Summary: Gets the #US stream or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMetadataHeaders.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.USStream;
    ```

## Class `DotNetMethodBody`

.NET method body

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetMethodBody(methodProvider: /* DotNetMethodProvider */, name: /* string */, span: /* HexBufferSpan */, tokens: /* ReadOnlyCollection<uint> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 47)

### Constructors

- `protected DotNetMethodBody(DotNetMethodProvider methodProvider, string name, HexBufferSpan span, ReadOnlyCollection<uint> tokens)`
  - Summary: Constructor
  - Parameters:
    - `DotNetMethodProvider methodProvider`: Owner
    - `string name`: Name
    - `HexBufferSpan span`: Span
    - `ReadOnlyCollection<uint> tokens`: Tokens of all methods that reference this method body
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 65)

### Properties

- `public DotNetMethodProvider MethodProvider { get; }`
  - Summary: Gets the owner instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MethodProvider;
    ```
- `public ReadOnlyCollection<uint> Tokens { get; }`
  - Summary: Gets tokens of all methods that reference this method body
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tokens;
    ```
- `public abstract DotNetMethodBodyKind Kind { get; }`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public abstract StructField<VirtualArrayData<ByteData>> Instructions { get; }`
  - Summary: Gets the instruction bytes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Instructions;
    ```

## Enum `DotNetMethodBodyKind`

kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.DotNet.DotNetMethodBodyKind and call its members.
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetMethodBodyKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 27)

### Members

- `Invalid`: Invalid method body ()
- `Tiny`: Tiny method body ()
- `Fat`: Fat method body ()

## Class `DotNetMethodProvider`

Provides instances

**Inherits/Implements:** `IBufferFileHeaders`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetMethodProvider(file: /* HexBufferFile */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodProvider.cs` (line 26)

### Constructors

- `protected DotNetMethodProvider(HexBufferFile file)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferFile file`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodProvider.cs` (line 30)

### Methods

- `public abstract DotNetMethodBody GetMethodBody(HexPosition position)`
  - Summary: Gets a method or null if isn't within a method body
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodProvider.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethodBody(position: /* HexPosition */);
    ```
- `public abstract bool IsMethodPosition(HexPosition position)`
  - Summary: Returns true if is probably within a method body
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodProvider.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.IsMethodPosition(position: /* HexPosition */);
    ```

### Properties

- `public HexBufferFile File { get; }`
  - Summary: Gets the file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodProvider.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.File;
    ```

## Class `DotNetMethodSection`

.NET method body section

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetMethodSection(name: /* string */, span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 181)

### Constructors

- `protected DotNetMethodSection(string name, HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 187)

### Properties

- `public abstract bool IsSmall { get; }`
  - Summary: Returns true if this is a small section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 194)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSmall;
    ```

## Class `DotNetMultiFileResourceHeaderData`

.NET multi-file resource header

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetMultiFileResourceHeaderData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 26)

### Constructors

- `protected DotNetMultiFileResourceHeaderData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 33)

### Properties

- `public abstract StructField<ArrayData<ByteData>> Alignment8 { get; }`
  - Summary: 8-byte alignment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Alignment8;
    ```
- `public abstract StructField<Bit7EncodedStringData> ReaderType { get; }`
  - Summary: Reader type or null if unknown header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReaderType;
    ```
- `public abstract StructField<Bit7EncodedStringData> ResourceSetType { get; }`
  - Summary: ResourceSet type or null if unknown header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResourceSetType;
    ```
- `public abstract StructField<FileOffsetData> DataSectionOffset { get; }`
  - Summary: DataSectionOffset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DataSectionOffset;
    ```
- `public abstract StructField<UInt32Data> HeaderSize { get; }`
  - Summary: Header size
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HeaderSize;
    ```
- `public abstract StructField<UInt32Data> MagicNum { get; }`
  - Summary: Magic number
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MagicNum;
    ```
- `public abstract StructField<UInt32Data> NumResources { get; }`
  - Summary: NumResources
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NumResources;
    ```
- `public abstract StructField<UInt32Data> NumTypes { get; }`
  - Summary: NumTypes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NumTypes;
    ```
- `public abstract StructField<UInt32Data> ResMgrHeaderVersion { get; }`
  - Summary: Header version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResMgrHeaderVersion;
    ```
- `public abstract StructField<UInt32Data> Version { get; }`
  - Summary: Version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Version;
    ```
- `public abstract StructField<VariableLengthArrayData<Bit7EncodedStringData>> TypeNames { get; }`
  - Summary: TypeNames
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeNames;
    ```
- `public abstract StructField<VirtualArrayData<ByteData>> UnknownHeader { get; }`
  - Summary: Unknown header or null if it's a known header (see and )
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UnknownHeader;
    ```
- `public abstract StructField<VirtualArrayData<UInt32Data>> NameHashes { get; }`
  - Summary: Name hashes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NameHashes;
    ```
- `public abstract StructField<VirtualArrayData<UInt32Data>> NamePositions { get; }`
  - Summary: Name positions
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResourceHeaderData.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NamePositions;
    ```

## Class `DotNetMultiFileResources`

Present if the file is a .NET multi-file resource file

**Inherits/Implements:** `IBufferFileHeaders`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetMultiFileResources(file: /* HexBufferFile */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResources.cs` (line 26)

### Constructors

- `protected DotNetMultiFileResources(HexBufferFile file)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResources.cs` (line 31)

### Methods

- `public abstract ComplexData GetStructure(HexPosition position)`
  - Summary: Returns a structure at or null
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResources.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStructure(position: /* HexPosition */);
    ```

### Properties

- `public HexBufferFile File { get; }`
  - Summary: Gets the file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResources.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.File;
    ```
- `public abstract DotNetMultiFileResourceHeaderData Header { get; }`
  - Summary: Gets the header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResources.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Header;
    ```
- `public abstract HexPosition DataSectionPosition { get; }`
  - Summary: Position of data section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMultiFileResources.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DataSectionPosition;
    ```

## Class `DotNetResourceProvider`

Provides instances

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetResourceProvider(file: /* HexBufferFile */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetResourceProvider.cs` (line 26)

### Constructors

- `protected DotNetResourceProvider(HexBufferFile file)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetResourceProvider.cs` (line 31)

### Methods

- `public abstract DotNetEmbeddedResource GetResource(HexPosition position)`
  - Summary: Gets a resource or null if isn't within a resource
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetResourceProvider.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResource(position: /* HexPosition */);
    ```
- `public abstract bool IsResourcePosition(HexPosition position)`
  - Summary: Returns true if is probably within a resource
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetResourceProvider.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.IsResourcePosition(position: /* HexPosition */);
    ```

### Properties

- `public HexBufferFile File { get; }`
  - Summary: Gets the file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetResourceProvider.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.File;
    ```
- `public abstract HexSpan ResourcesSpan { get; }`
  - Summary: Gets the span of the .NET resources or an empty span if there are no .NET resources
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetResourceProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResourcesSpan;
    ```

## Class `DotNetStorageStream`

.NET metadata header storage stream

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.DotNetStorageStream(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetStorageStream.cs` (line 24)

### Constructors

- `protected DotNetStorageStream(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetStorageStream.cs` (line 31)

### Properties

- `public abstract StructField<StringData> StreamName { get; }`
  - Summary: STORAGESTREAM.rcName
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetStorageStream.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StreamName;
    ```
- `public abstract StructField<UInt32Data> Offset { get; }`
  - Summary: STORAGESTREAM.iOffset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetStorageStream.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```
- `public abstract StructField<UInt32Data> Size { get; }`
  - Summary: STORAGESTREAM.iSize
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetStorageStream.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Size;
    ```

## Class `ExceptionClause`

Exception clause

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.ExceptionClause(name: /* string */, span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 330)

### Constructors

- `protected ExceptionClause(string name, HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 336)

### Properties

- `public abstract bool IsSmall { get; }`
  - Summary: true if it's a small exception clause
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 343)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSmall;
    ```

## Class `ExceptionHandlerTable`

Exception handler table

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.ExceptionHandlerTable(name: /* string */, span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 256)

### Constructors

- `protected ExceptionHandlerTable(string name, HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 262)

### Properties

- `public abstract bool IsSmall { get; }`
  - Summary: true if it's a small exception handler table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 269)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSmall;
    ```

## Class `FatExceptionClause`

Fat exception clause

**Inherits/Implements:** `ExceptionClause`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.FatExceptionClause(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 388)

### Constructors

- `protected FatExceptionClause(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 394)

### Properties

- `public abstract StructField<UInt32Data> ClassTokenOrFilterOffset { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT.ClassToken / FilterOffset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 421)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ClassTokenOrFilterOffset;
    ```
- `public abstract StructField<UInt32Data> HandlerLength { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT.HandlerLength
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 418)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HandlerLength;
    ```
- `public abstract StructField<UInt32Data> HandlerOffset { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT.HandlerOffset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 415)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HandlerOffset;
    ```
- `public abstract StructField<UInt32Data> TryLength { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT.TryLength
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 412)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TryLength;
    ```
- `public abstract StructField<UInt32Data> TryOffset { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT.TryOffset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 409)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TryOffset;
    ```
- `public abstract StructField<UInt32FlagsData> Flags { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_FAT.Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 406)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public override bool IsSmall => false`
  - Summary: Returns false since this is a fat exception clause
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 403)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSmall;
    ```

## Class `FatExceptionHandlerTable`

Fat exception handler table

**Inherits/Implements:** `ExceptionHandlerTable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.FatExceptionHandlerTable(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 304)

### Constructors

- `protected FatExceptionHandlerTable(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 311)

### Properties

- `public abstract StructField<ArrayData<FatExceptionClause>> Clauses { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_FAT.Clauses
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 324)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Clauses;
    ```
- `public abstract StructField<FatSection> SectFat { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_FAT.SectFat
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 321)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SectFat;
    ```
- `public override bool IsSmall => false`
  - Summary: Returns false since this is a fat exception handler table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 318)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSmall;
    ```

## Class `FatMethodBody`

Fat .NET method body

**Inherits/Implements:** `DotNetMethodBody`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.FatMethodBody(methodProvider: /* DotNetMethodProvider */, span: /* HexBufferSpan */, tokens: /* ReadOnlyCollection<uint> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 136)

### Constructors

- `protected FatMethodBody(DotNetMethodProvider methodProvider, HexBufferSpan span, ReadOnlyCollection<uint> tokens)`
  - Summary: Constructor
  - Parameters:
    - `DotNetMethodProvider methodProvider`: Owner
    - `HexBufferSpan span`: Span
    - `ReadOnlyCollection<uint> tokens`: Tokens of all methods that reference this method body
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 145)

### Properties

- `public abstract StructField<ExceptionHandlerTable> EHTable { get; }`
  - Summary: Gets the exception handler table or null if there's none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 175)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EHTable;
    ```
- `public abstract StructField<TokenData> LocalVarSigTok { get; }`
  - Summary: IMAGE_COR_ILMETHOD_FAT.LocalVarSigTok
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 164)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LocalVarSigTok;
    ```
- `public abstract StructField<UInt16Data> MaxStack { get; }`
  - Summary: IMAGE_COR_ILMETHOD_FAT.MaxStack
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 158)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MaxStack;
    ```
- `public abstract StructField<UInt16FlagsData> Flags_Size { get; }`
  - Summary: IMAGE_COR_ILMETHOD_FAT.Flags / Size
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 155)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags_Size;
    ```
- `public abstract StructField<UInt32Data> CodeSize { get; }`
  - Summary: IMAGE_COR_ILMETHOD_FAT.CodeSize
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 161)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CodeSize;
    ```
- `public abstract StructField<VirtualArrayData<ByteData>> Padding { get; }`
  - Summary: Padding between and . It's null if isn't present.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 170)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Padding;
    ```
- `public sealed override DotNetMethodBodyKind Kind => DotNetMethodBodyKind.Fat`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 152)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `FatSection`

Fat section

**Inherits/Implements:** `DotNetMethodSection`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.FatSection(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 228)

### Constructors

- `protected FatSection(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 235)

### Properties

- `public abstract StructField<ByteFlagsData> Kind { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_FAT.Kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 247)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public abstract StructField<UInt24Data> DataSize { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_FAT.DataSize
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 250)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DataSize;
    ```
- `public override bool IsSmall => false`
  - Summary: Returns false since this is a fat section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 244)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSmall;
    ```

## Class `GUIDHeap`

.NET #GUID heap

**Inherits/Implements:** `DotNetHeap`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.GUIDHeap(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 285)

### Constructors

- `protected GUIDHeap(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Heap span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 290)

### Methods

- `public Guid? Read(uint index)`
  - Summary: Reads a . Returns null if is 0 or invalid
  - Parameters:
    - `uint index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 313)
  - Example:
    ```csharp
    // Example invocation
    instance.Read(index: /* uint */);
    ```
- `public bool IsValidIndex(uint index)`
  - Summary: Checks whether is valid. This method is identical to
  - Parameters:
    - `uint index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 299)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValidIndex(index: /* uint */);
    ```
- `public override bool IsValidOffset(uint index)`
  - Summary: Checks whether is valid
  - Parameters:
    - `uint index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 306)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValidOffset(index: /* uint */);
    ```

## Class `GUIDHeapData`

#GUID heap reference

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.GUIDHeapData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 476)

### Constructors

- `protected GUIDHeapData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 481)

### Methods

- `protected abstract uint ReadIndex()`
  - Summary: Reads the rid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 489)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadIndex();
    ```
- `public override HexSpan? GetFieldReferenceSpan(HexBufferFile file)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 496)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(file: /* HexBufferFile */);
    ```

## Class `GUIDHeapData16`

16-bit #GUID heap reference

**Inherits/Implements:** `GUIDHeapData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.GUIDHeapData16(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 510)

### Constructors

- `public GUIDHeapData16(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 526)
- `public GUIDHeapData16(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 515)

### Methods

- `protected override uint ReadIndex()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 540)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadIndex();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 534)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `GUIDHeapData32`

32-bit #GUID heap reference

**Inherits/Implements:** `GUIDHeapData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.GUIDHeapData32(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 546)

### Constructors

- `public GUIDHeapData32(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 562)
- `public GUIDHeapData32(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 551)

### Methods

- `protected override uint ReadIndex()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 576)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadIndex();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 570)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `GuidData`

A

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.GuidData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 26)

### Constructors

- `public GuidData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 98)
- `public GuidData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 61)

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public StructField<ByteData> D { get; }`
  - Summary: Guid.D
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.D;
    ```
- `public StructField<ByteData> E { get; }`
  - Summary: Guid.E
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.E;
    ```
- `public StructField<ByteData> F { get; }`
  - Summary: Guid.F
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.F;
    ```
- `public StructField<ByteData> G { get; }`
  - Summary: Guid.G
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.G;
    ```
- `public StructField<ByteData> H { get; }`
  - Summary: Guid.H
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.H;
    ```
- `public StructField<ByteData> I { get; }`
  - Summary: Guid.I
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.I;
    ```
- `public StructField<ByteData> J { get; }`
  - Summary: Guid.J
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.J;
    ```
- `public StructField<ByteData> K { get; }`
  - Summary: Guid.K
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.K;
    ```
- `public StructField<UInt16Data> B { get; }`
  - Summary: Guid.B
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.B;
    ```
- `public StructField<UInt16Data> C { get; }`
  - Summary: Guid.C
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.C;
    ```
- `public StructField<UInt32Data> A { get; }`
  - Summary: Guid.A
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/StructureData.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.A;
    ```

## Class `GuidHeapRecordData`

#GUID heap record data

**Inherits/Implements:** `GuidData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.GuidHeapRecordData(buffer: /* HexBuffer */, position: /* HexPosition */, heap: /* GUIDHeap */, index: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 28)

### Constructors

- `public GuidHeapRecordData(HexBuffer buffer, HexPosition position, GUIDHeap heap, uint index)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `GUIDHeap heap`: Owner heap
    - `uint index`: Guid index (1-based)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 46)

### Properties

- `public GUIDHeap Heap { get; }`
  - Summary: Gets the heap
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Heap;
    ```
- `public uint Index { get; }`
  - Summary: Gets the GUID index (1-based)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Index;
    ```

## Class `HotHeap`

.NET #! heap

**Inherits/Implements:** `DotNetHeap`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.HotHeap(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 364)

### Constructors

- `protected HotHeap(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Heap span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 369)

## Class `InvalidMethodBody`

Invalid .NET method body

**Inherits/Implements:** `DotNetMethodBody`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.InvalidMethodBody(methodProvider: /* DotNetMethodProvider */, span: /* HexBufferSpan */, tokens: /* ReadOnlyCollection<uint> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 89)

### Constructors

- `protected InvalidMethodBody(DotNetMethodProvider methodProvider, HexBufferSpan span, ReadOnlyCollection<uint> tokens)`
  - Summary: Constructor
  - Parameters:
    - `DotNetMethodProvider methodProvider`: Owner
    - `HexBufferSpan span`: Span
    - `ReadOnlyCollection<uint> tokens`: Tokens of all methods that reference this method body
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 98)

### Properties

- `public sealed override DotNetMethodBodyKind Kind => DotNetMethodBodyKind.Invalid`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 105)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `KnownResourceTypeCodeData`

Known data (not a user type)

**Inherits/Implements:** `ResourceTypeCodeData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.KnownResourceTypeCodeData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ResourceTypeCodeData.cs` (line 53)

### Constructors

- `public KnownResourceTypeCodeData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ResourceTypeCodeData.cs` (line 58)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ResourceTypeCodeData.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Enum `MDStreamFlags`

MDStream flags

**Inherits/Implements:** `byte`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.DotNet.MDStreamFlags and call its members.
var instance = new dnSpy.Contracts.Hex.Files.DotNet.MDStreamFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDStreamFlags.cs` (line 28)

### Members

- `BigStrings`: #Strings stream is big and requires 4 byte offsets
- `BigGUID`: #GUID stream is big and requires 4 byte offsets
- `BigBlob`: #Blob stream is big and requires 4 byte offsets
- `Padding`
- `DeltaOnly` = `x20`
- `ExtraData` = `x40`: Extra data follows the row counts
- `HasDelete` = `x80`: Set if certain tables can contain deleted rows. The name column (if present) is set to "_Deleted"

## Class `MDTable`

A MD table (eg. Method table)

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.MDTable(position: /* HexPosition */, table: /* Table */, rows: /* uint */, tableInfo: /* TableInfo */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 28)

### Constructors

- `public MDTable(HexPosition position, Table table, uint rows, TableInfo tableInfo)`
  - Summary: Constructor
  - Parameters:
    - `HexPosition position`: Start position
    - `Table table`: The table
    - `uint rows`: Number of rows in this table
    - `TableInfo tableInfo`: Info about this table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 76)

### Methods

- `public bool IsInvalidRID(uint rid)`
  - Summary: Checks whether the row does not exist
  - Parameters:
    - `uint rid`: Row ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.IsInvalidRID(rid: /* uint */);
    ```
- `public bool IsValidRID(uint rid)`
  - Summary: Checks whether the row exists
  - Parameters:
    - `uint rid`: Row ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValidRID(rid: /* uint */);
    ```

### Properties

- `public HexSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public ReadOnlyCollection<ColumnInfo> Columns => TableInfo.Columns`
  - Summary: Returns all the columns
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Columns;
    ```
- `public Table Table { get; }`
  - Summary: Gets the table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Table;
    ```
- `public TableInfo TableInfo { get; }`
  - Summary: Returns info about this table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TableInfo;
    ```
- `public bool IsEmpty => Rows == 0`
  - Summary: Returns true if there are no valid rows
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public string Name => TableInfo.Name`
  - Summary: Gets the name of this table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public uint RowSize => (uint)TableInfo.RowSize`
  - Summary: Gets the total size in bytes of one row in this table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RowSize;
    ```
- `public uint Rows { get; }`
  - Summary: Returns total number of rows
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDTable.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Rows;
    ```

## Struct `MDToken`

MetaData token

**Inherits/Implements:** `IEquatable<MDToken>`, `IComparable<MDToken>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.MDToken(token: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 28)

### Constructors

- `public MDToken(Table table, int rid)`
  - Summary: Constructor
  - Parameters:
    - `Table table`: The table type
    - `int rid`: Row id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 94)
- `public MDToken(Table table, uint rid)`
  - Summary: Constructor
  - Parameters:
    - `Table table`: The table type
    - `uint rid`: Row id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 85)
- `public MDToken(int token)`
  - Summary: Constructor
  - Parameters:
    - `int token`: Raw token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 76)
- `public MDToken(uint token)`
  - Summary: Constructor
  - Parameters:
    - `uint token`: Raw token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 70)

### Methods

- `public bool Equals(MDToken other)`
  - Parameters:
    - `MDToken other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 170)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* MDToken */);
    ```
- `public int CompareTo(MDToken other)`
  - Parameters:
    - `MDToken other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 167)
  - Example:
    ```csharp
    // Example invocation
    instance.CompareTo(other: /* MDToken */);
    ```
- `public int ToInt32()`
  - Summary: Gets the token as a raw 32-bit signed integer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 129)
  - Example:
    ```csharp
    // Example invocation
    instance.ToInt32();
    ```
- `public override bool Equals(object obj)`
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 173)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 180)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 183)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static Table ToTable(int token)`
  - Summary: Returns the table
  - Parameters:
    - `int token`: A raw metadata token
  - Returns: A metadata table index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 124)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.DotNet.MDToken.ToTable(token: /* int */);
    ```
- `public static Table ToTable(uint token)`
  - Summary: Returns the table
  - Parameters:
    - `uint token`: A raw metadata token
  - Returns: A metadata table index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.DotNet.MDToken.ToTable(token: /* uint */);
    ```
- `public static uint ToRID(int token)`
  - Summary: Returns the rid (row ID)
  - Parameters:
    - `int token`: A raw metadata token
  - Returns: A rid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 110)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.DotNet.MDToken.ToRID(token: /* int */);
    ```
- `public static uint ToRID(uint token)`
  - Summary: Returns the rid (row ID)
  - Parameters:
    - `uint token`: A raw metadata token
  - Returns: A rid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.DotNet.MDToken.ToRID(token: /* uint */);
    ```
- `public uint ToUInt32()`
  - Summary: Gets the token as a raw 32-bit unsigned integer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 134)
  - Example:
    ```csharp
    // Example invocation
    instance.ToUInt32();
    ```

### Properties

- `public Table Table => ToTable(token)`
  - Summary: Returns the table type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Table;
    ```
- `public bool IsNull => Rid == 0`
  - Summary: Returns true if it's a null token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNull;
    ```
- `public uint Raw => token`
  - Summary: Returns the raw token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Raw;
    ```
- `public uint Rid => ToRID(token)`
  - Summary: Returns the row id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Rid;
    ```

### Fields

- `public const int TABLE_SHIFT = 24`
  - Summary: Number of bits to right shift a raw metadata token to get the table index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 42)
  - Example:
    ```csharp
    var value = instance.TABLE_SHIFT;
    ```
- `public const uint RID_MASK = 0x00FFFFFF`
  - Summary: Mask to get the rid from a raw metadata token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 32)
  - Example:
    ```csharp
    var value = instance.RID_MASK;
    ```
- `public const uint RID_MAX = RID_MASK`
  - Summary: Max rid value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 37)
  - Example:
    ```csharp
    var value = instance.RID_MAX;
    ```

### Operators

- `public static bool operator !=(MDToken left, MDToken right)`
  - Summary: Overloaded operator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 142)
- `public static bool operator <(MDToken left, MDToken right)`
  - Summary: Overloaded operator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 147)
- `public static bool operator <=(MDToken left, MDToken right)`
  - Summary: Overloaded operator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 157)
- `public static bool operator ==(MDToken left, MDToken right)`
  - Summary: Overloaded operator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 137)
- `public static bool operator >(MDToken left, MDToken right)`
  - Summary: Overloaded operator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 152)
- `public static bool operator >=(MDToken left, MDToken right)`
  - Summary: Overloaded operator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MDToken.cs` (line 162)

## Class `MultiResourceArrayDataHeaderData`

Multi-file resource data header (byte arrays and streams)

**Inherits/Implements:** `MultiResourceDataHeaderData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.MultiResourceArrayDataHeaderData(resourceProvider: /* DotNetMultiFileResources */, resourceInfo: /* MultiResourceInfo */, span: /* HexBufferSpan */, lengthPosition: /* HexPosition */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 247)

### Constructors

- `public MultiResourceArrayDataHeaderData(DotNetMultiFileResources resourceProvider, MultiResourceInfo resourceInfo, HexBufferSpan span, HexPosition lengthPosition)`
  - Summary: Constructor
  - Parameters:
    - `DotNetMultiFileResources resourceProvider`: Owner
    - `MultiResourceInfo resourceInfo`: Resource info
    - `HexBufferSpan span`: Span
    - `HexPosition lengthPosition`: Position of 32-bit content length which immediately follows the 7-bit encoded type code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 267)

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 258)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public StructField<UInt32Data> ContentLength { get; }`
  - Summary: Content length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 251)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentLength;
    ```
- `public StructField<VirtualArrayData<ByteData>> Content { get; }`
  - Summary: Content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 253)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Content;
    ```
- `public override StructField<ResourceTypeCodeData> TypeCode { get; }`
  - Summary: Type code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 249)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeCode;
    ```

## Class `MultiResourceDataHeaderData`

Multi-file resource data header base class

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.MultiResourceDataHeaderData(resourceProvider: /* DotNetMultiFileResources */, resourceInfo: /* MultiResourceInfo */, span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 60)

### Constructors

- `protected MultiResourceDataHeaderData(DotNetMultiFileResources resourceProvider, MultiResourceInfo resourceInfo, HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `DotNetMultiFileResources resourceProvider`: Owner
    - `MultiResourceInfo resourceInfo`: Resource info
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 82)

### Properties

- `public DotNetMultiFileResources ResourceProvider { get; }`
  - Summary: Gets the owner instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResourceProvider;
    ```
- `public MultiResourceInfo ResourceInfo { get; }`
  - Summary: Gets resource info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResourceInfo;
    ```
- `public abstract StructField<ResourceTypeCodeData> TypeCode { get; }`
  - Summary: Type code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeCode;
    ```

## Struct `MultiResourceInfo`

Multi file resource element info

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.MultiResourceInfo(name: /* string */, typeCode: /* ResourceTypeCode */, userTypeName: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 28)

### Constructors

- `public MultiResourceInfo(string name, ResourceTypeCode typeCode, string userTypeName)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name of resource
    - `ResourceTypeCode typeCode`: Type code
    - `string userTypeName`: User type or null if it's not a
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 50)

### Properties

- `public ResourceTypeCode TypeCode { get; }`
  - Summary: Gets the type code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeCode;
    ```
- `public string Name { get; }`
  - Summary: Gets the resource name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public string UserTypeName { get; }`
  - Summary: Gets the user type name if is >=
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UserTypeName;
    ```

## Class `MultiResourceSimplDataHeaderData`

Multi-file resource data header (everything that's not a string, byte array, stream)

**Inherits/Implements:** `MultiResourceDataHeaderData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.MultiResourceSimplDataHeaderData(resourceProvider: /* DotNetMultiFileResources */, resourceInfo: /* MultiResourceInfo */, span: /* HexBufferSpan */, dataPosition: /* HexPosition */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 92)

### Constructors

- `public MultiResourceSimplDataHeaderData(DotNetMultiFileResources resourceProvider, MultiResourceInfo resourceInfo, HexBufferSpan span, HexPosition dataPosition)`
  - Summary: Constructor
  - Parameters:
    - `DotNetMultiFileResources resourceProvider`: Owner
    - `MultiResourceInfo resourceInfo`: Resource info
    - `HexBufferSpan span`: Span
    - `HexPosition dataPosition`: Position of data which immediately follows the 7-bit encoded type code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 110)

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public StructField Content { get; }`
  - Summary: Content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Content;
    ```
- `public override StructField<ResourceTypeCodeData> TypeCode { get; }`
  - Summary: Type code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeCode;
    ```

## Class `MultiResourceStringDataHeaderData`

Multi-file resource data header (strings)

**Inherits/Implements:** `MultiResourceDataHeaderData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.MultiResourceStringDataHeaderData(resourceProvider: /* DotNetMultiFileResources */, resourceInfo: /* MultiResourceInfo */, span: /* HexBufferSpan */, lengthSpan: /* HexSpan */, stringSpan: /* HexSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 207)

### Constructors

- `public MultiResourceStringDataHeaderData(DotNetMultiFileResources resourceProvider, MultiResourceInfo resourceInfo, HexBufferSpan span, HexSpan lengthSpan, HexSpan stringSpan)`
  - Summary: Constructor
  - Parameters:
    - `DotNetMultiFileResources resourceProvider`: Owner
    - `MultiResourceInfo resourceInfo`: Resource info
    - `HexBufferSpan span`: Span
    - `HexSpan lengthSpan`: Span of 7-bit encoded string length
    - `HexSpan stringSpan`: Span of string data (UTF-8)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 226)

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 216)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public StructField<Bit7EncodedStringData> Content { get; }`
  - Summary: Content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 211)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Content;
    ```
- `public override StructField<ResourceTypeCodeData> TypeCode { get; }`
  - Summary: Type code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceDataHeaderData.cs` (line 209)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeCode;
    ```

## Class `MultiResourceUnicodeNameAndOffsetData`

Multi-file .NET resource name and data offset

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.MultiResourceUnicodeNameAndOffsetData(resourceProvider: /* DotNetMultiFileResources */, buffer: /* HexBuffer */, lengthSpan: /* HexSpan */, stringSpan: /* HexSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceUnicodeNameAndOffsetData.cs` (line 27)

### Constructors

- `public MultiResourceUnicodeNameAndOffsetData(DotNetMultiFileResources resourceProvider, HexBuffer buffer, HexSpan lengthSpan, HexSpan stringSpan)`
  - Summary: Constructor
  - Parameters:
    - `DotNetMultiFileResources resourceProvider`: Owner
    - `HexBuffer buffer`: Buffer
    - `HexSpan lengthSpan`: Span of 7-bit encoded length
    - `HexSpan stringSpan`: Span of string data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceUnicodeNameAndOffsetData.cs` (line 52)

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceUnicodeNameAndOffsetData.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public DotNetMultiFileResources ResourceProvider { get; }`
  - Summary: Gets the owner instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceUnicodeNameAndOffsetData.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResourceProvider;
    ```
- `public StructField<Bit7EncodedStringData> ResourceName { get; }`
  - Summary: Gets the resource name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceUnicodeNameAndOffsetData.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResourceName;
    ```
- `public StructField<UInt32Data> DataOffset { get; }`
  - Summary: Gets the data offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/MultiResourceUnicodeNameAndOffsetData.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DataOffset;
    ```

## Class `PdbHeap`

.NET #Pdb heap

**Inherits/Implements:** `DotNetHeap`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.PdbHeap(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 377)

### Constructors

- `protected PdbHeap(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Heap span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 407)

### Properties

- `public abstract MDToken EntryPoint { get; }`
  - Summary: Gets the entry point, this value is cached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 391)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EntryPoint;
    ```
- `public abstract PdbStreamHeaderData Header { get; }`
  - Summary: Gets the header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 381)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Header;
    ```
- `public abstract ReadOnlyCollection<byte> PdbId { get; }`
  - Summary: Gets the PDB id, this value is cached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 386)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PdbId;
    ```
- `public abstract ReadOnlyCollection<uint> TypeSystemTableRows { get; }`
  - Summary: Gets the rows, this value is cached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 401)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeSystemTableRows;
    ```
- `public abstract ulong ReferencedTypeSystemTables { get; }`
  - Summary: Gets a bit mask of all referenced type system tables, this value is cached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 396)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReferencedTypeSystemTables;
    ```

## Class `PdbStreamHeaderData`

#Pdb heap header

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.PdbStreamHeaderData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PdbStreamHeaderData.cs` (line 24)

### Constructors

- `protected PdbStreamHeaderData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PdbStreamHeaderData.cs` (line 31)

### Properties

- `public abstract StructField<ArrayData<UInt32Data>> TypeSystemTableRows { get; }`
  - Summary: TypeSystemTableRows
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PdbStreamHeaderData.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeSystemTableRows;
    ```
- `public abstract StructField<PortablePdbIdData> PdbId { get; }`
  - Summary: PDB id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PdbStreamHeaderData.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PdbId;
    ```
- `public abstract StructField<TokenData> EntryPoint { get; }`
  - Summary: EntryPoint
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PdbStreamHeaderData.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EntryPoint;
    ```
- `public abstract StructField<UInt64FlagsData> ReferencedTypeSystemTables { get; }`
  - Summary: ReferencedTypeSystemTables
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PdbStreamHeaderData.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReferencedTypeSystemTables;
    ```

## Class `PortablePdbIdData`

Portable PDB Id (20 bytes)

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.PortablePdbIdData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 117)

### Constructors

- `public PortablePdbIdData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 133)
- `public PortablePdbIdData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 122)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 141)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `PredefinedDotNetDataIds`

Predefined .NET ids

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Files.DotNet.PredefinedDotNetDataIds members directly without instantiation.
dnSpy.Contracts.Hex.Files.DotNet.PredefinedDotNetDataIds./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PredefinedDotNetDataIds.cs` (line 24)

### Fields

- `public const string Cor20 = nameof(Cor20)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PredefinedDotNetDataIds.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.PredefinedDotNetDataIds.Cor20;
    ```
- `public const string MetadataHeader = nameof(MetadataHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PredefinedDotNetDataIds.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.PredefinedDotNetDataIds.MetadataHeader;
    ```
- `public const string MultiFileResource = nameof(MultiFileResource)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PredefinedDotNetDataIds.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.PredefinedDotNetDataIds.MultiFileResource;
    ```
- `public const string StrongNameSignature = nameof(StrongNameSignature)`
  - Summary: of bytes ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/PredefinedDotNetDataIds.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.DotNet.PredefinedDotNetDataIds.StrongNameSignature;
    ```

## Enum `ResourceTypeCode`

Type of resource

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.DotNet.ResourceTypeCode and call its members.
var instance = new dnSpy.Contracts.Hex.Files.DotNet.ResourceTypeCode(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ResourceTypeCode.cs` (line 26)

### Members

- `Null`: null
- `String`
- `Boolean`
- `Char`
- `Byte`
- `SByte`
- `Int16`
- `UInt16`
- `Int32`
- `UInt32`
- `Int64` = `x0A`
- `UInt64` = `x0B`
- `Single` = `x0C`
- `Double` = `x0D`
- `Decimal` = `x0E`
- `DateTime` = `x0F`
- `TimeSpan` = `x10`
- `ByteArray` = `x20`: array
- `Stream` = `x21`
- `UserTypes` = `x40`: Start of user types

## Class `ResourceTypeCodeData`

data

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.ResourceTypeCodeData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ResourceTypeCodeData.cs` (line 27)

### Constructors

- `protected ResourceTypeCodeData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ResourceTypeCodeData.cs` (line 32)

### Methods

- `public static ResourceTypeCodeData Create(HexBufferSpan span)`
  - Summary: Creates a
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ResourceTypeCodeData.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Hex.Files.DotNet.ResourceTypeCodeData.Create(span: /* HexBufferSpan */);
    ```

## Class `Rid16Data`

16-bit .NET table rid

**Inherits/Implements:** `RidData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.Rid16Data(span: /* HexBufferSpan */, table: /* Table */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 263)

### Constructors

- `public Rid16Data(HexBuffer buffer, HexPosition position, Table table)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `Table table`: Table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 281)
- `public Rid16Data(HexBufferSpan span, Table table)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `Table table`: Table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 269)

### Methods

- `protected override uint ReadRidValue()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 289)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadRidValue();
    ```

## Class `Rid32Data`

32-bit .NET table rid

**Inherits/Implements:** `RidData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.Rid32Data(span: /* HexBufferSpan */, table: /* Table */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 295)

### Constructors

- `public Rid32Data(HexBuffer buffer, HexPosition position, Table table)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
    - `Table table`: Table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 313)
- `public Rid32Data(HexBufferSpan span, Table table)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `Table table`: Table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 301)

### Methods

- `protected override uint ReadRidValue()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 321)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadRidValue();
    ```

## Class `RidData`

.NET table rid

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.RidData(span: /* HexBufferSpan */, table: /* Table */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 216)

### Constructors

- `protected RidData(HexBufferSpan span, Table table)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
    - `Table table`: Table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 224)

### Methods

- `protected abstract uint ReadRidValue()`
  - Summary: Reads the rid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 231)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadRidValue();
    ```
- `public override HexSpan? GetFieldReferenceSpan(HexBufferFile file)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 246)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(file: /* HexBufferFile */);
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 239)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `SmallExceptionClause`

Small exception clause

**Inherits/Implements:** `ExceptionClause`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.SmallExceptionClause(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 349)

### Constructors

- `protected SmallExceptionClause(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 355)

### Properties

- `public abstract StructField<ByteData> HandlerLength { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL.HandlerLength
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 379)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HandlerLength;
    ```
- `public abstract StructField<ByteData> TryLength { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL.TryLength
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 373)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TryLength;
    ```
- `public abstract StructField<UInt16Data> HandlerOffset { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL.HandlerOffset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 376)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HandlerOffset;
    ```
- `public abstract StructField<UInt16Data> TryOffset { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL.TryOffset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 370)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TryOffset;
    ```
- `public abstract StructField<UInt16FlagsData> Flags { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL.Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 367)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public abstract StructField<UInt32Data> ClassTokenOrFilterOffset { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_CLAUSE_SMALL.ClassToken/FilterOffset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 382)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ClassTokenOrFilterOffset;
    ```
- `public override bool IsSmall => true`
  - Summary: Returns true since this is a small exception clause
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 364)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSmall;
    ```

## Class `SmallExceptionHandlerTable`

Small exception handler table

**Inherits/Implements:** `ExceptionHandlerTable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.SmallExceptionHandlerTable(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 275)

### Constructors

- `protected SmallExceptionHandlerTable(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 282)

### Properties

- `public abstract StructField<ArrayData<SmallExceptionClause>> Clauses { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_SMALL.Clauses
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 298)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Clauses;
    ```
- `public abstract StructField<SmallSection> SectSmall { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_SMALL.SectSmall
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 292)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SectSmall;
    ```
- `public abstract StructField<UInt16Data> Reserved { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_EH_SMALL.Reserved
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 295)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reserved;
    ```
- `public override bool IsSmall => true`
  - Summary: Returns true since this is a small exception handler table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 289)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSmall;
    ```

## Class `SmallSection`

Small section

**Inherits/Implements:** `DotNetMethodSection`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.SmallSection(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 200)

### Constructors

- `protected SmallSection(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 207)

### Properties

- `public abstract StructField<ByteData> DataSize { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_SMALL.DataSize
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 222)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DataSize;
    ```
- `public abstract StructField<ByteFlagsData> Kind { get; }`
  - Summary: IMAGE_COR_ILMETHOD_SECT_SMALL.Kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 219)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public override bool IsSmall => true`
  - Summary: Returns true since this is a small section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 216)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSmall;
    ```

## Class `StringsHeap`

.NET #Strings heap

**Inherits/Implements:** `DotNetHeap`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.StringsHeap(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 166)

### Constructors

- `protected StringsHeap(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Heap span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 171)

### Methods

- `public HexBufferSpan GetStringSpan(uint offset)`
  - Summary: Gets the span of the string, not including the terminating zero byte. Returns an empty span if is invalid.
  - Parameters:
    - `uint offset`: Offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStringSpan(offset: /* uint */);
    ```
- `public HexBufferSpan GetStringSpan(uint offset, int maxByteLength)`
  - Summary: Gets the span of the string, not including the terminating zero byte. Returns an empty span if is invalid.
  - Parameters:
    - `uint offset`: Offset
    - `int maxByteLength`: Maximum number of bytes to read
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 190)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStringSpan(offset: /* uint */, maxByteLength: /* int */);
    ```
- `public byte[] ReadBytes(uint offset)`
  - Summary: Reads string data which should be a UTF-8 encoded string. The array doesn't include the terminating zero. Returns an empty array if is invalid
  - Parameters:
    - `uint offset`: Offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 208)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(offset: /* uint */);
    ```
- `public byte[] ReadBytes(uint offset, int maxByteLength)`
  - Summary: Reads string data which should be a UTF-8 encoded string. The array doesn't include the terminating zero. Returns an empty array if is invalid
  - Parameters:
    - `uint offset`: Offset
    - `int maxByteLength`: Maximum number of bytes to read
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 217)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(offset: /* uint */, maxByteLength: /* int */);
    ```
- `public string Read(uint offset)`
  - Summary: Reads a string. Returns an empty string if is invalid
  - Parameters:
    - `uint offset`: Offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 224)
  - Example:
    ```csharp
    // Example invocation
    instance.Read(offset: /* uint */);
    ```
- `public string Read(uint offset, int maxByteLength)`
  - Summary: Reads a string. Returns an empty string if is invalid
  - Parameters:
    - `uint offset`: Offset
    - `int maxByteLength`: Maximum number of bytes to read
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 232)
  - Example:
    ```csharp
    // Example invocation
    instance.Read(offset: /* uint */, maxByteLength: /* int */);
    ```

## Class `StringsHeapData`

#Strings heap reference

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.StringsHeapData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 246)

### Constructors

- `protected StringsHeapData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 251)

### Methods

- `protected abstract uint ReadOffset()`
  - Summary: Reads the rid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 259)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadOffset();
    ```
- `public override HexSpan? GetFieldReferenceSpan(HexBufferFile file)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 266)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(file: /* HexBufferFile */);
    ```

## Class `StringsHeapData16`

16-bit #Strings heap reference

**Inherits/Implements:** `StringsHeapData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.StringsHeapData16(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 294)

### Constructors

- `public StringsHeapData16(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 310)
- `public StringsHeapData16(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 299)

### Methods

- `protected override uint ReadOffset()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 324)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadOffset();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 318)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `StringsHeapData32`

32-bit #Strings heap reference

**Inherits/Implements:** `StringsHeapData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.StringsHeapData32(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 330)

### Constructors

- `public StringsHeapData32(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 346)
- `public StringsHeapData32(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 335)

### Methods

- `protected override uint ReadOffset()`
  - Summary: Reads the token value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 360)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadOffset();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 354)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `StringsHeapRecordData`

#Strings heap record data

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.StringsHeapRecordData(buffer: /* HexBuffer */, stringSpan: /* HexSpan */, hasTerminatingZero: /* bool */, heap: /* StringsHeap */, tokens: /* uint[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 58)

### Constructors

- `public StringsHeapRecordData(HexBuffer buffer, HexSpan stringSpan, bool hasTerminatingZero, StringsHeap heap, uint[] tokens)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexSpan stringSpan`: Span of string, not including the terminating zero
    - `bool hasTerminatingZero`: true if there's a terminating zero, false if there's no terminating zero or if the string is too long
    - `StringsHeap heap`: Owner heap
    - `uint[] tokens`: Tokens of records referencing this string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 95)

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public ReadOnlyCollection<uint> Tokens { get; }`
  - Summary: Gets tokens of records referencing this string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tokens;
    ```
- `public StringsHeap Heap { get; }`
  - Summary: Gets the owner heap
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Heap;
    ```
- `public StructField<ByteData> Terminator { get; }`
  - Summary: Gets the terminator or null if there's none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 79)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Terminator;
    ```
- `public StructField<StringData> String { get; }`
  - Summary: Gets the string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.String;
    ```

## Enum `Table`

The metadata tables

**Inherits/Implements:** `byte`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.DotNet.Table and call its members.
var instance = new dnSpy.Contracts.Hex.Files.DotNet.Table(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/Table.cs` (line 26)

### Members

- `Module`: Module table (00h)
- `TypeRef`: TypeRef table (01h)
- `TypeDef`: TypeDef table (02h)
- `FieldPtr`: FieldPtr table (03h)
- `Field`: Field table (04h)
- `MethodPtr`: MethodPtr table (05h)
- `Method`: Method table (06h)
- `ParamPtr`: ParamPtr table (07h)
- `Param`: Param table (08h)
- `InterfaceImpl`: InterfaceImpl table (09h)
- `MemberRef`: MemberRef table (0Ah)
- `Constant`: Constant table (0Bh)
- `CustomAttribute`: CustomAttribute table (0Ch)
- `FieldMarshal`: FieldMarshal table (0Dh)
- `DeclSecurity`: DeclSecurity table (0Eh)
- `ClassLayout`: ClassLayout table (0Fh)
- `FieldLayout`: FieldLayout table (10h)
- `StandAloneSig`: StandAloneSig table (11h)
- `EventMap`: EventMap table (12h)
- `EventPtr`: EventPtr table (13h)
- `Event`: Event table (14h)
- `PropertyMap`: PropertyMap table (15h)
- `PropertyPtr`: PropertyPtr table (16h)
- `Property`: Property table (17h)
- `MethodSemantics`: MethodSemantics table (18h)
- `MethodImpl`: MethodImpl table (19h)
- `ModuleRef`: ModuleRef table (1Ah)
- `TypeSpec`: TypeSpec table (1Bh)
- `ImplMap`: ImplMap table (1Ch)
- `FieldRVA`: FieldRVA table (1Dh)
- `ENCLog`: ENCLog table (1Eh)
- `ENCMap`: ENCMap table (1Fh)
- `Assembly`: Assembly table (20h)
- `AssemblyProcessor`: AssemblyProcessor table (21h)
- `AssemblyOS`: AssemblyOS table (22h)
- `AssemblyRef`: AssemblyRef table (23h)
- `AssemblyRefProcessor`: AssemblyRefProcessor table (24h)
- `AssemblyRefOS`: AssemblyRefOS table (25h)
- `File`: File table (26h)
- `ExportedType`: ExportedType table (27h)
- `ManifestResource`: ManifestResource table (28h)
- `NestedClass`: NestedClass table (29h)
- `GenericParam`: GenericParam table (2Ah)
- `MethodSpec`: MethodSpec table (2Bh)
- `GenericParamConstraint`: GenericParamConstraint table (2Ch)
- `Document` = `x30`: (Portable PDB) Document table (30h)
- `MethodDebugInformation`: (Portable PDB) MethodDebugInformation table (31h)
- `LocalScope`: (Portable PDB) LocalScope table (32h)
- `LocalVariable`: (Portable PDB) LocalVariable table (33h)
- `LocalConstant`: (Portable PDB) LocalConstant table (34h)
- `ImportScope`: (Portable PDB) ImportScope table (35h)
- `StateMachineMethod`: (Portable PDB) StateMachineMethod table (36h)
- `CustomDebugInformation`: (Portable PDB) CustomDebugInformation table (37h)

## Class `TableInfo`

Info about one MD table

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.TableInfo(table: /* Table */, name: /* string */, columns: /* ColumnInfo[] */, rowSize: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableInfo.cs` (line 29)

### Constructors

- `public TableInfo(Table table, string name, ColumnInfo[] columns, int rowSize = 0)`
  - Summary: Constructor
  - Parameters:
    - `Table table`: Table type
    - `string name`: Table name
    - `ColumnInfo[] columns`: All columns
    - `int rowSize` (default: `0`): Row size
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableInfo.cs` (line 57)

### Properties

- `public ReadOnlyCollection<ColumnInfo> Columns { get; }`
  - Summary: Returns all the columns
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableInfo.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Columns;
    ```
- `public Table Table { get; }`
  - Summary: Returns the table type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableInfo.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Table;
    ```
- `public int RowSize { get; }`
  - Summary: Returns the total size of a row in bytes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableInfo.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RowSize;
    ```
- `public string Name { get; }`
  - Summary: Returns the name of the table
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableInfo.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `TableRecordData`

.NET table record

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.TableRecordData(tableName: /* string */, token: /* MDToken */, span: /* HexBufferSpan */, fields: /* BufferField[] */, tablesHeap: /* TablesHeap */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableRecordData.cs` (line 27)

### Constructors

- `public TableRecordData(string tableName, MDToken token, HexBufferSpan span, BufferField[] fields, TablesHeap tablesHeap)`
  - Summary: Constructor
  - Parameters:
    - `string tableName`: Name of table
    - `MDToken token`: Token
    - `HexBufferSpan span`: Span
    - `BufferField[] fields`: Fields
    - `TablesHeap tablesHeap`: Owner heap
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableRecordData.cs` (line 51)

### Methods

- `public override void WriteName(HexFieldFormatter formatter)`
  - Summary: Writes the name
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableRecordData.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(formatter: /* HexFieldFormatter */);
    ```
- `public uint ReadColumn(int index)`
  - Summary: Reads a column, treating the column value as an unsigned integer
  - Parameters:
    - `int index`: Index of column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableRecordData.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadColumn(index: /* int */);
    ```

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableRecordData.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public MDToken Token { get; }`
  - Summary: Gets the token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableRecordData.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```
- `public TablesHeap TablesHeap { get; }`
  - Summary: Gets the owner heap
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TableRecordData.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TablesHeap;
    ```

## Class `TablesHeaderData`

.NET tables stream header

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.TablesHeaderData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 24)

### Constructors

- `protected TablesHeaderData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 31)

### Properties

- `public abstract StructField<ArrayData<UInt32Data>> Rows { get; }`
  - Summary: Rows
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Rows;
    ```
- `public abstract StructField<ByteData> Log2Rid { get; }`
  - Summary: m_rid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Log2Rid;
    ```
- `public abstract StructField<ByteData> MajorVersion { get; }`
  - Summary: m_major
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MajorVersion;
    ```
- `public abstract StructField<ByteData> MinorVersion { get; }`
  - Summary: m_minor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MinorVersion;
    ```
- `public abstract StructField<ByteFlagsData> Flags { get; }`
  - Summary: m_heaps
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public abstract StructField<UInt32Data> ExtraData { get; }`
  - Summary: Extra data or null if there was no extra data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExtraData;
    ```
- `public abstract StructField<UInt32Data> Reserved { get; }`
  - Summary: m_ulReserved
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reserved;
    ```
- `public abstract StructField<UInt64FlagsData> SortedMask { get; }`
  - Summary: m_sorted
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SortedMask;
    ```
- `public abstract StructField<UInt64FlagsData> ValidMask { get; }`
  - Summary: m_maskvalid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValidMask;
    ```
- `public bool HasExtraData => ExtraData != null`
  - Summary: true if field exists in header and isn't null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeaderData.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasExtraData;
    ```

## Class `TablesHeap`

.NET tables (#~ or #-) heap

**Inherits/Implements:** `DotNetHeap`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.TablesHeap(span: /* HexBufferSpan */, tablesHeapType: /* TablesHeapType */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 89)

### Constructors

- `protected TablesHeap(HexBufferSpan span, TablesHeapType tablesHeapType)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Heap span
    - `TablesHeapType tablesHeapType`: Tables heap type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 145)

### Methods

- `public TableRecordData GetRecord(uint token)`
  - Summary: Gets a record or null if is invalid
  - Parameters:
    - `uint token`: Token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRecord(token: /* uint */);
    ```
- `public abstract TableRecordData GetRecord(MDToken token)`
  - Summary: Gets a record or null if is invalid
  - Parameters:
    - `MDToken token`: Token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 160)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRecord(token: /* MDToken */);
    ```

### Properties

- `public TablesHeapType TablesHeapType { get; }`
  - Summary: Gets the metadata type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TablesHeapType;
    ```
- `public abstract HexSpan HeaderSpan { get; }`
  - Summary: Span of header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 103)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HeaderSpan;
    ```
- `public abstract HexSpan TablesSpan { get; }`
  - Summary: Span of all tables
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 108)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TablesSpan;
    ```
- `public abstract MDStreamFlags Flags { get; }`
  - Summary: Gets the flags, this value is cached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 128)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public abstract ReadOnlyCollection<MDTable> MDTables { get; }`
  - Summary: Gets all metadata table infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 98)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MDTables;
    ```
- `public abstract TablesHeaderData Header { get; }`
  - Summary: Gets the header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 113)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Header;
    ```
- `public abstract byte MajorVersion { get; }`
  - Summary: Gets the major version, this value is cached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 118)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MajorVersion;
    ```
- `public abstract byte MinorVersion { get; }`
  - Summary: Gets the minor version, this value is cached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 123)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MinorVersion;
    ```
- `public abstract ulong SortedMask { get; }`
  - Summary: Gets the sorted mask, this value is cached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 138)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SortedMask;
    ```
- `public abstract ulong ValidMask { get; }`
  - Summary: Gets the valid mask, this value is cached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 133)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValidMask;
    ```

## Enum `TablesHeapType`

Metadata tables type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.DotNet.TablesHeapType and call its members.
var instance = new dnSpy.Contracts.Hex.Files.DotNet.TablesHeapType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TablesHeapType.cs` (line 24)

### Members

- `Compressed`: Compressed (#~)
- `ENC`: Edit n' Continue (#-)

## Class `TimeSpanData`

A

**Inherits/Implements:** `SimpleData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.TimeSpanData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 72)

### Constructors

- `public TimeSpanData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 88)
- `public TimeSpanData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 77)

### Methods

- `public TimeSpan ReadValue()`
  - Summary: Reads the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadValue();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/SimpleData.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `TinyMethodBody`

Tiny .NET method body

**Inherits/Implements:** `DotNetMethodBody`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.TinyMethodBody(methodProvider: /* DotNetMethodProvider */, span: /* HexBufferSpan */, tokens: /* ReadOnlyCollection<uint> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 111)

### Constructors

- `protected TinyMethodBody(DotNetMethodProvider methodProvider, HexBufferSpan span, ReadOnlyCollection<uint> tokens)`
  - Summary: Constructor
  - Parameters:
    - `DotNetMethodProvider methodProvider`: Owner
    - `HexBufferSpan span`: Span
    - `ReadOnlyCollection<uint> tokens`: Tokens of all methods that reference this method body
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 120)

### Properties

- `public abstract StructField<ByteFlagsData> Flags_CodeSize { get; }`
  - Summary: IMAGE_COR_ILMETHOD_TINY.Flags_CodeSize
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 130)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags_CodeSize;
    ```
- `public sealed override DotNetMethodBodyKind Kind => DotNetMethodBodyKind.Tiny`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetMethodBodyData.cs` (line 127)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `TokenData`

.NET metadata token

**Inherits/Implements:** `UInt32Data`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.TokenData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 26)

### Constructors

- `public TokenData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 40)
- `public TokenData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 31)

### Methods

- `public override HexSpan? GetFieldReferenceSpan(HexBufferFile file)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(file: /* HexBufferFile */);
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/TokenData.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

## Class `USHeap`

.NET #US heap

**Inherits/Implements:** `DotNetHeap`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.USHeap(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 238)

### Constructors

- `protected USHeap(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Heap span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 243)

### Methods

- `public HexBufferSpan GetStringSpan(uint offset)`
  - Summary: Returns the span of the string data or an empty span if is 0 or invalid.
  - Parameters:
    - `uint offset`: Offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 252)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStringSpan(offset: /* uint */);
    ```
- `public byte[] ReadData(uint offset)`
  - Summary: Reads data at . Returns an empty array if is invalid. The returned data doesn't include the compressed data length at .
  - Parameters:
    - `uint offset`: Offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 271)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadData(offset: /* uint */);
    ```
- `public string Read(uint offset)`
  - Summary: Reads the string at . Returns an empty string if is 0 or invalid.
  - Parameters:
    - `uint offset`: Offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 279)
  - Example:
    ```csharp
    // Example invocation
    instance.Read(offset: /* uint */);
    ```

## Class `USHeapRecordData`

#US heap record data

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.USHeapRecordData(buffer: /* HexBuffer */, lengthSpan: /* HexSpan */, stringSpan: /* HexSpan */, terminalByteSpan: /* HexSpan */, heap: /* USHeap */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 121)

### Constructors

- `public USHeapRecordData(HexBuffer buffer, HexSpan lengthSpan, HexSpan stringSpan, HexSpan terminalByteSpan, USHeap heap)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexSpan lengthSpan`: Span of length
    - `HexSpan stringSpan`: Span of string data
    - `HexSpan terminalByteSpan`: Span of terminal byte (0 or 1 byte)
    - `USHeap heap`: Owner heap
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 157)

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 147)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public StructField<BlobEncodedUInt32Data> Length { get; }`
  - Summary: Gets the length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 132)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public StructField<ByteData> TerminalByte { get; }`
  - Summary: Gets the terminal byte or null if none exists
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 142)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TerminalByte;
    ```
- `public StructField<StringData> String { get; }`
  - Summary: Gets the string data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 137)
  - Example:
    ```csharp
    // Read the property
    var value = instance.String;
    ```
- `public USHeap Heap { get; }`
  - Summary: Gets the owner heap
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/HeapData.cs` (line 127)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Heap;
    ```

## Class `UnknownHeap`

Unknown .NET heap

**Inherits/Implements:** `DotNetHeap`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.UnknownHeap(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 415)

### Constructors

- `protected UnknownHeap(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Heap span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/DotNetHeap.cs` (line 420)

## Class `UserTypeResourceTypeCodeData`

data

**Inherits/Implements:** `ResourceTypeCodeData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DotNet.UserTypeResourceTypeCodeData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ResourceTypeCodeData.cs` (line 101)

### Constructors

- `public UserTypeResourceTypeCodeData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ResourceTypeCodeData.cs` (line 106)

### Methods

- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DotNet/ResourceTypeCodeData.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

