# Namespace `dnSpy.Contracts.Debugger.DotNet.Metadata.Internal`

## Class `DbgRawMetadata`

Raw .NET metadata stored in some memory location

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Metadata.Internal.DbgRawMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Metadata.Internal.DbgRawMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadata.cs` (line 26)

### Methods

- `public abstract DbgRawMetadata AddRef()`
  - Summary: Increments the reference count and returns the same instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadata.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.AddRef();
    ```
- `public abstract void Release()`
  - Summary: Decrements the reference count
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadata.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.Release();
    ```
- `public abstract void UpdateMemory()`
  - Summary: Re-reads the memory if possible
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadata.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateMemory();
    ```

### Properties

- `public abstract IntPtr Address { get; }`
  - Summary: Gets the address of the data (first byte of the PE file)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadata.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```
- `public abstract IntPtr MetadataAddress { get; }`
  - Summary: Gets the address of the .NET metadata (BSJB header)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadata.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataAddress;
    ```
- `public abstract bool IsFileLayout { get; }`
  - Summary: true if it's file layout, false if it's memory layout
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadata.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFileLayout;
    ```
- `public abstract int MetadataSize { get; }`
  - Summary: Gets the size of the metadata
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadata.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataSize;
    ```
- `public abstract int Size { get; }`
  - Summary: Gets the size of the data (size of the PE file in memory)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadata.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Size;
    ```
- `public bool IsMemoryLayout => !IsFileLayout`
  - Summary: true if it's memory layout, false if it's file layout
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadata.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMemoryLayout;
    ```

## Class `DbgRawMetadataService`

Creates instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Metadata.Internal.DbgRawMetadataService and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Metadata.Internal.DbgRawMetadataService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadataService.cs` (line 24)

### Methods

- `public abstract DbgRawMetadata Create(DbgRuntime runtime, bool isFileLayout, byte[] moduleBytes)`
  - Summary: Creates a
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `bool isFileLayout`: true if it's file layout, false if it's memory layout
    - `byte[] moduleBytes`: Raw module bytes
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadataService.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(runtime: /* DbgRuntime */, isFileLayout: /* bool */, moduleBytes: /* byte[] */);
    ```
- `public abstract DbgRawMetadata Create(DbgRuntime runtime, bool isFileLayout, ulong moduleAddress, int moduleSize)`
  - Summary: Creates a
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `bool isFileLayout`: true if it's file layout, false if it's memory layout
    - `ulong moduleAddress`: Address of .NET module in the process' address space
    - `int moduleSize`: Size of module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/Internal/DbgRawMetadataService.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(runtime: /* DbgRuntime */, isFileLayout: /* bool */, moduleAddress: /* ulong */, moduleSize: /* int */);
    ```

