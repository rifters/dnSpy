# Namespace `dnSpy.Contracts.Debugger.DotNet.Disassembly`

## Struct `DbgDotNetNativeCode`

Contains the code that will be disassembled

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Disassembly.DbgDotNetNativeCode(kind: /* NativeCodeKind */, optimization: /* NativeCodeOptimization */, blocks: /* DbgDotNetNativeCodeBlock[] */, codeInfo: /* NativeCodeInfo */, methodName: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCode.cs` (line 27)

### Constructors

- `public DbgDotNetNativeCode(NativeCodeKind kind, NativeCodeOptimization optimization, DbgDotNetNativeCodeBlock[] blocks, NativeCodeInfo codeInfo, string methodName)`
  - Summary: Constructor
  - Parameters:
    - `NativeCodeKind kind`: Code kind
    - `NativeCodeOptimization optimization`: Optimization kind
    - `DbgDotNetNativeCodeBlock[] blocks`: All blocks to disassemble
    - `NativeCodeInfo codeInfo`: Extra code info or null
    - `string methodName`: Method name or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCode.cs` (line 61)

### Properties

- `public DbgDotNetNativeCodeBlock[] Blocks { get; }`
  - Summary: All blocks to disassemble
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCode.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Blocks;
    ```
- `public NativeCodeInfo CodeInfo { get; }`
  - Summary: Extra optional info, or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCode.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CodeInfo;
    ```
- `public NativeCodeKind Kind { get; }`
  - Summary: Gets the code kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCode.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public NativeCodeOptimization Optimization { get; }`
  - Summary: Gets the optimization kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCode.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Optimization;
    ```
- `public string MethodName { get; }`
  - Summary: Method name or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCode.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MethodName;
    ```

## Struct `DbgDotNetNativeCodeBlock`

A block of native code

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Disassembly.DbgDotNetNativeCodeBlock(kind: /* NativeCodeBlockKind */, address: /* ulong */, code: /* ArraySegment<byte> */, ilOffset: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCodeBlock.cs` (line 27)

### Constructors

- `public DbgDotNetNativeCodeBlock(NativeCodeBlockKind kind, ulong address, ArraySegment<byte> code, int ilOffset)`
  - Summary: Constructor
  - Parameters:
    - `NativeCodeBlockKind kind`: Code kind
    - `ulong address`: Address of block
    - `ArraySegment<byte> code`: Raw code
    - `int ilOffset`: IL offset or -1 if unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCodeBlock.cs` (line 55)

### Properties

- `public ArraySegment<byte> Code { get; }`
  - Summary: Gets the raw code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCodeBlock.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Code;
    ```
- `public NativeCodeBlockKind Kind { get; }`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCodeBlock.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public int ILOffset { get; }`
  - Summary: IL offset or -1 if unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCodeBlock.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ILOffset;
    ```
- `public ulong Address { get; }`
  - Summary: Gets the address of the code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Disassembly/DbgDotNetNativeCodeBlock.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```

