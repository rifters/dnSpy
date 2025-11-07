# Namespace `dnSpy.Contracts.Hex.Files.PE`

## Class `DataDirectoryData`

Data directory

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.DataDirectoryData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/DataDirectoryData.cs` (line 26)

### Constructors

- `public DataDirectoryData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/DataDirectoryData.cs` (line 57)
- `public DataDirectoryData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/DataDirectoryData.cs` (line 38)

### Properties

- `protected override BufferField[] Fields { get; }`
  - Summary: Gets the fields
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/DataDirectoryData.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public StructField<RvaData> VirtualAddress { get; }`
  - Summary: IMAGE_DATA_DIRECTORY.VirtualAddress
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/DataDirectoryData.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VirtualAddress;
    ```
- `public StructField<UInt32Data> Size { get; }`
  - Summary: IMAGE_DATA_DIRECTORY.Size
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/DataDirectoryData.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Size;
    ```

## Class `FileOffsetData`

32-bit file offset

**Inherits/Implements:** `UInt32Data`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.FileOffsetData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 109)

### Constructors

- `public FileOffsetData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 123)
- `public FileOffsetData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 114)

### Methods

- `public override HexSpan? GetFieldReferenceSpan(HexBufferFile file)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(file: /* HexBufferFile */);
    ```

## Class `PeDosHeaderData`

DOS header

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.PeDosHeaderData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 24)

### Constructors

- `protected PeDosHeaderData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 31)

### Properties

- `public abstract StructField<ArrayData<UInt16Data>> Res { get; }`
  - Summary: IMAGE_DOS_HEADER.e_res[4]
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Res;
    ```
- `public abstract StructField<ArrayData<UInt16Data>> Res2 { get; }`
  - Summary: IMAGE_DOS_HEADER.e_res2[10]
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Res2;
    ```
- `public abstract StructField<FileOffsetData> Lfanew { get; }`
  - Summary: IMAGE_DOS_HEADER.e_lfanew
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Lfanew;
    ```
- `public abstract StructField<UInt16Data> Cblp { get; }`
  - Summary: IMAGE_DOS_HEADER.e_cblp
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Cblp;
    ```
- `public abstract StructField<UInt16Data> Cp { get; }`
  - Summary: IMAGE_DOS_HEADER.e_cp
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Cp;
    ```
- `public abstract StructField<UInt16Data> Cparhdr { get; }`
  - Summary: IMAGE_DOS_HEADER.e_cparhdr
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Cparhdr;
    ```
- `public abstract StructField<UInt16Data> Crlc { get; }`
  - Summary: IMAGE_DOS_HEADER.e_crlc
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Crlc;
    ```
- `public abstract StructField<UInt16Data> Cs { get; }`
  - Summary: IMAGE_DOS_HEADER.e_cs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Cs;
    ```
- `public abstract StructField<UInt16Data> Csum { get; }`
  - Summary: IMAGE_DOS_HEADER.e_csum
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Csum;
    ```
- `public abstract StructField<UInt16Data> Ip { get; }`
  - Summary: IMAGE_DOS_HEADER.e_ip
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Ip;
    ```
- `public abstract StructField<UInt16Data> Lfarlc { get; }`
  - Summary: IMAGE_DOS_HEADER.e_lfarlc
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Lfarlc;
    ```
- `public abstract StructField<UInt16Data> Magic { get; }`
  - Summary: IMAGE_DOS_HEADER.e_magic
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Magic;
    ```
- `public abstract StructField<UInt16Data> Maxalloc { get; }`
  - Summary: IMAGE_DOS_HEADER.e_maxalloc
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Maxalloc;
    ```
- `public abstract StructField<UInt16Data> Minalloc { get; }`
  - Summary: IMAGE_DOS_HEADER.e_minalloc
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Minalloc;
    ```
- `public abstract StructField<UInt16Data> Oemid { get; }`
  - Summary: IMAGE_DOS_HEADER.e_oemid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Oemid;
    ```
- `public abstract StructField<UInt16Data> Oeminfo { get; }`
  - Summary: IMAGE_DOS_HEADER.e_oeminfo
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Oeminfo;
    ```
- `public abstract StructField<UInt16Data> Ovno { get; }`
  - Summary: IMAGE_DOS_HEADER.e_ovno
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Ovno;
    ```
- `public abstract StructField<UInt16Data> Sp { get; }`
  - Summary: IMAGE_DOS_HEADER.e_sp
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Sp;
    ```
- `public abstract StructField<UInt16Data> Ss { get; }`
  - Summary: IMAGE_DOS_HEADER.e_ss
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeDosHeaderData.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Ss;
    ```

## Class `PeFileHeaderData`

File header

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.PeFileHeaderData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileHeaderData.cs` (line 24)

### Constructors

- `protected PeFileHeaderData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileHeaderData.cs` (line 31)

### Properties

- `public abstract StructField<FileOffsetData> PointerToSymbolTable { get; }`
  - Summary: IMAGE_FILE_HEADER.PointerToSymbolTable
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileHeaderData.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PointerToSymbolTable;
    ```
- `public abstract StructField<UInt16Data> NumberOfSections { get; }`
  - Summary: IMAGE_FILE_HEADER.NumberOfSections
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileHeaderData.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NumberOfSections;
    ```
- `public abstract StructField<UInt16Data> SizeOfOptionalHeader { get; }`
  - Summary: IMAGE_FILE_HEADER.SizeOfOptionalHeader
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileHeaderData.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfOptionalHeader;
    ```
- `public abstract StructField<UInt16EnumData> Machine { get; }`
  - Summary: IMAGE_FILE_HEADER.Machine
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileHeaderData.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Machine;
    ```
- `public abstract StructField<UInt16FlagsData> Characteristics { get; }`
  - Summary: IMAGE_FILE_HEADER.Characteristics
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileHeaderData.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Characteristics;
    ```
- `public abstract StructField<UInt32Data> NumberOfSymbols { get; }`
  - Summary: IMAGE_FILE_HEADER.NumberOfSymbols
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileHeaderData.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NumberOfSymbols;
    ```
- `public abstract StructField<UnixTime32Data> TimeDateStamp { get; }`
  - Summary: IMAGE_FILE_HEADER.TimeDateStamp
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileHeaderData.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TimeDateStamp;
    ```

## Enum `PeFileLayout`

PE file layout

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Files.PE.PeFileLayout and call its members.
var instance = new dnSpy.Contracts.Hex.Files.PE.PeFileLayout(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileLayoutProvider.cs` (line 44)

### Members

- `Unknown`: Unknown layout
- `File`: File layout
- `Memory`: Memory layout, the OS loader has loaded the file into memory

## Class `PeFileLayoutProvider`

Detects whether a PE file was loaded by the OS PE loader. Export an instance with a and an optional

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.PeFileLayoutProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileLayoutProvider.cs` (line 27)

### Constructors

- `protected PeFileLayoutProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileLayoutProvider.cs` (line 31)

### Methods

- `public abstract PeFileLayout GetLayout(HexBufferFile file)`
  - Summary: Gets the PE file layout
  - Parameters:
    - `HexBufferFile file`: File. This can be a nested file.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeFileLayoutProvider.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLayout(file: /* HexBufferFile */);
    ```

## Class `PeHeaders`

PE headers

**Inherits/Implements:** `IBufferFileHeaders`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.PeHeaders();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 24)

### Constructors

- `protected PeHeaders()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 28)

### Methods

- `public abstract HexPosition FilePositionToBufferPosition(ulong position)`
  - Summary: Converts a file position in the PE file to a buffer position. If the input is invalid, 0 is returned. This method uses data from cached section headers.
  - Parameters:
    - `ulong position`: File position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.FilePositionToBufferPosition(position: /* ulong */);
    ```
- `public abstract HexPosition RvaToBufferPosition(uint rva)`
  - Summary: Converts to a buffer position. This method uses data from cached section headers.
  - Parameters:
    - `uint rva`: RVA
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.RvaToBufferPosition(rva: /* uint */);
    ```
- `public abstract uint BufferPositionToRva(HexPosition position)`
  - Summary: Converts a buffer position to an RVA. If the input is invalid, 0 is returned. This method uses data from cached section headers.
  - Parameters:
    - `HexPosition position`: Buffer position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.BufferPositionToRva(position: /* HexPosition */);
    ```
- `public abstract ulong BufferPositionToFilePosition(HexPosition position)`
  - Summary: Converts a buffer position to a file position in the PE file. If the input is invalid, 0 is returned. This method uses data from cached section headers.
  - Parameters:
    - `HexPosition position`: Buffer position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.BufferPositionToFilePosition(position: /* HexPosition */);
    ```

### Properties

- `public abstract PeDosHeaderData DosHeader { get; }`
  - Summary: Gets the DOS header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DosHeader;
    ```
- `public abstract PeFileHeaderData FileHeader { get; }`
  - Summary: Gets the file header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FileHeader;
    ```
- `public abstract PeOptionalHeaderData OptionalHeader { get; }`
  - Summary: Gets the optional header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OptionalHeader;
    ```
- `public abstract PeSectionsData Sections { get; }`
  - Summary: Gets the sections
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Sections;
    ```
- `public abstract bool IsFileLayout { get; }`
  - Summary: true if file layout, false if memory layout
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeHeaders.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFileLayout;
    ```

## Class `PeOptionalHeader32Data`

32-bit optional header

**Inherits/Implements:** `PeOptionalHeaderData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.PeOptionalHeader32Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 94)

### Constructors

- `protected PeOptionalHeader32Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 101)

### Properties

- `public abstract StructField<RvaData> BaseOfData { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER32.BaseOfData
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BaseOfData;
    ```
- `public abstract StructField<UInt32Data> ImageBase { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER32.ImageBase
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 113)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageBase;
    ```
- `public abstract StructField<UInt32Data> SizeOfHeapCommit { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER32.SizeOfHeapCommit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 121)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfHeapCommit;
    ```
- `public abstract StructField<UInt32Data> SizeOfHeapReserve { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER32.SizeOfHeapReserve
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 119)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfHeapReserve;
    ```
- `public abstract StructField<UInt32Data> SizeOfStackCommit { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER32.SizeOfStackCommit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 117)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfStackCommit;
    ```
- `public abstract StructField<UInt32Data> SizeOfStackReserve { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER32.SizeOfStackReserve
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 115)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfStackReserve;
    ```
- `public sealed override bool Is32Bit => true`
  - Summary: This is true, since it's a 32-bit optional header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 108)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Is32Bit;
    ```

## Class `PeOptionalHeader64Data`

64-bit optional header

**Inherits/Implements:** `PeOptionalHeaderData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.PeOptionalHeader64Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 127)

### Constructors

- `protected PeOptionalHeader64Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 134)

### Properties

- `public abstract StructField<UInt64Data> ImageBase { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER64.ImageBase
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 144)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageBase;
    ```
- `public abstract StructField<UInt64Data> SizeOfHeapCommit { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER64.SizeOfHeapCommit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 152)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfHeapCommit;
    ```
- `public abstract StructField<UInt64Data> SizeOfHeapReserve { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER64.SizeOfHeapReserve
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 150)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfHeapReserve;
    ```
- `public abstract StructField<UInt64Data> SizeOfStackCommit { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER64.SizeOfStackCommit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 148)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfStackCommit;
    ```
- `public abstract StructField<UInt64Data> SizeOfStackReserve { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER64.SizeOfStackReserve
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 146)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfStackReserve;
    ```
- `public sealed override bool Is32Bit => false`
  - Summary: This is false, since it's a 64-bit optional header
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 141)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Is32Bit;
    ```

## Class `PeOptionalHeaderData`

Optional header

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.PeOptionalHeaderData(name: /* string */, span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 24)

### Constructors

- `protected PeOptionalHeaderData(string name, HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Structure name
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 30)

### Properties

- `public abstract StructField<ArrayData<DataDirectoryData>> DataDirectory { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.DataDirectory
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DataDirectory;
    ```
- `public abstract StructField<ByteData> MajorLinkerVersion { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.MajorLinkerVersion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MajorLinkerVersion;
    ```
- `public abstract StructField<ByteData> MinorLinkerVersion { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.MinorLinkerVersion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MinorLinkerVersion;
    ```
- `public abstract StructField<RvaData> AddressOfEntryPoint { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.AddressOfEntryPoint
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AddressOfEntryPoint;
    ```
- `public abstract StructField<RvaData> BaseOfCode { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.BaseOfCode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BaseOfCode;
    ```
- `public abstract StructField<UInt16Data> Magic { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.Magic
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Magic;
    ```
- `public abstract StructField<UInt16Data> MajorImageVersion { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.MajorImageVersion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MajorImageVersion;
    ```
- `public abstract StructField<UInt16Data> MajorOperatingSystemVersion { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.MajorOperatingSystemVersion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MajorOperatingSystemVersion;
    ```
- `public abstract StructField<UInt16Data> MajorSubsystemVersion { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.MajorSubsystemVersion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MajorSubsystemVersion;
    ```
- `public abstract StructField<UInt16Data> MinorImageVersion { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.MinorImageVersion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MinorImageVersion;
    ```
- `public abstract StructField<UInt16Data> MinorOperatingSystemVersion { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.MinorOperatingSystemVersion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MinorOperatingSystemVersion;
    ```
- `public abstract StructField<UInt16Data> MinorSubsystemVersion { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.MinorSubsystemVersion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MinorSubsystemVersion;
    ```
- `public abstract StructField<UInt16EnumData> Subsystem { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.Subsystem
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Subsystem;
    ```
- `public abstract StructField<UInt16FlagsData> DllCharacteristics { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.DllCharacteristics
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DllCharacteristics;
    ```
- `public abstract StructField<UInt32Data> CheckSum { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.CheckSum
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CheckSum;
    ```
- `public abstract StructField<UInt32Data> FileAlignment { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.FileAlignment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FileAlignment;
    ```
- `public abstract StructField<UInt32Data> LoaderFlags { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.LoaderFlags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LoaderFlags;
    ```
- `public abstract StructField<UInt32Data> NumberOfRvaAndSizes { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.NumberOfRvaAndSizes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NumberOfRvaAndSizes;
    ```
- `public abstract StructField<UInt32Data> SectionAlignment { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.SectionAlignment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SectionAlignment;
    ```
- `public abstract StructField<UInt32Data> SizeOfCode { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.SizeOfCode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfCode;
    ```
- `public abstract StructField<UInt32Data> SizeOfHeaders { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.SizeOfHeaders
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfHeaders;
    ```
- `public abstract StructField<UInt32Data> SizeOfImage { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.SizeOfImage
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfImage;
    ```
- `public abstract StructField<UInt32Data> SizeOfInitializedData { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.SizeOfInitializedData
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfInitializedData;
    ```
- `public abstract StructField<UInt32Data> SizeOfUninitializedData { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.SizeOfUninitializedData
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfUninitializedData;
    ```
- `public abstract StructField<UInt32Data> Win32VersionValue { get; }`
  - Summary: IMAGE_OPTIONAL_HEADER.Win32VersionValue
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Win32VersionValue;
    ```
- `public abstract bool Is32Bit { get; }`
  - Summary: true if it's a , false if it's a
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeOptionalHeaderData.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Is32Bit;
    ```

## Class `PeSectionData`

Section header

**Inherits/Implements:** `StructureData`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.PeSectionData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 40)

### Constructors

- `protected PeSectionData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 47)

### Properties

- `public abstract StructField<FileOffsetData> PointerToLinenumbers { get; }`
  - Summary: IMAGE_SECTION_HEADER.PointerToLinenumbers
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PointerToLinenumbers;
    ```
- `public abstract StructField<FileOffsetData> PointerToRawData { get; }`
  - Summary: IMAGE_SECTION_HEADER.PointerToRawData
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PointerToRawData;
    ```
- `public abstract StructField<FileOffsetData> PointerToRelocations { get; }`
  - Summary: IMAGE_SECTION_HEADER.PointerToRelocations
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PointerToRelocations;
    ```
- `public abstract StructField<RvaData> VirtualAddress { get; }`
  - Summary: IMAGE_SECTION_HEADER.VirtualAddress
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VirtualAddress;
    ```
- `public abstract StructField<StringData> SectionName { get; }`
  - Summary: IMAGE_SECTION_HEADER.Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SectionName;
    ```
- `public abstract StructField<UInt16Data> NumberOfLinenumbers { get; }`
  - Summary: IMAGE_SECTION_HEADER.NumberOfLinenumbers
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NumberOfLinenumbers;
    ```
- `public abstract StructField<UInt16Data> NumberOfRelocations { get; }`
  - Summary: IMAGE_SECTION_HEADER.NumberOfRelocations
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NumberOfRelocations;
    ```
- `public abstract StructField<UInt32Data> SizeOfRawData { get; }`
  - Summary: IMAGE_SECTION_HEADER.SizeOfRawData
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SizeOfRawData;
    ```
- `public abstract StructField<UInt32Data> VirtualSize { get; }`
  - Summary: IMAGE_SECTION_HEADER.VirtualSize
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VirtualSize;
    ```
- `public abstract StructField<UInt32FlagsData> Characteristics { get; }`
  - Summary: IMAGE_SECTION_HEADER.Characteristics
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Characteristics;
    ```

## Class `PeSectionsData`

Sections array

**Inherits/Implements:** `ArrayData<PeSectionData>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.PeSectionsData(span: /* HexBufferSpan */, fields: /* ArrayField<PeSectionData>[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 24)

### Constructors

- `public PeSectionsData(HexBufferSpan span, ArrayField<PeSectionData>[] fields)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Span
    - `ArrayField<PeSectionData>[] fields`: Array elements
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PeSectionsData.cs` (line 32)

## Class `PredefinedPeDataIds`

Predefined PE ids

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Files.PE.PredefinedPeDataIds members directly without instantiation.
dnSpy.Contracts.Hex.Files.PE.PredefinedPeDataIds./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PredefinedPeDataIds.cs` (line 24)

### Fields

- `public const string PeDosHeader = nameof(PeDosHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PredefinedPeDataIds.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PE.PredefinedPeDataIds.PeDosHeader;
    ```
- `public const string PeFileHeader = nameof(PeFileHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PredefinedPeDataIds.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PE.PredefinedPeDataIds.PeFileHeader;
    ```
- `public const string PeOptionalHeader = nameof(PeOptionalHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PredefinedPeDataIds.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PE.PredefinedPeDataIds.PeOptionalHeader;
    ```
- `public const string PeSections = nameof(PeSections)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/PredefinedPeDataIds.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Files.PE.PredefinedPeDataIds.PeSections;
    ```

## Class `RvaData`

RVA data

**Inherits/Implements:** `UInt32Data`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.RvaData(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 72)

### Constructors

- `public RvaData(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 86)
- `public RvaData(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 77)

### Methods

- `public override HexSpan? GetFieldReferenceSpan(HexBufferFile file)`
  - Summary: Returns the span the field value references or null. The span can be empty.
  - Parameters:
    - `HexBufferFile file`: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFieldReferenceSpan(file: /* HexBufferFile */);
    ```

## Class `UnixTime32Data`

32-bit Unix (epoch) time

**Inherits/Implements:** `UInt32Data`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.PE.UnixTime32Data(span: /* HexBufferSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 28)

### Constructors

- `public UnixTime32Data(HexBuffer buffer, HexPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 44)
- `public UnixTime32Data(HexBufferSpan span)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan span`: Data span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 33)

### Methods

- `public DateTime ReadDateTime()`
  - Summary: Reads the value as a
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadDateTime();
    ```
- `public override void WriteValue(HexFieldFormatter formatter)`
  - Summary: Writes the value
  - Parameters:
    - `HexFieldFormatter formatter`: Formatter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/PE/SimpleData.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteValue(formatter: /* HexFieldFormatter */);
    ```

