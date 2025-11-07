# Namespace `dnSpy.Contracts.Debugger.DotNet.Code`

## Class `DbgAsyncMethodDebugInfo`

Asynchronous method debug info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgAsyncMethodDebugInfo(stepInfos: /* DbgAsyncStepInfo[] */, builderField: /* FieldDef */, catchHandlerOffset: /* uint */, setResultOffset: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncMethodDebugInfo.cs` (line 27)

### Constructors

- `public DbgAsyncMethodDebugInfo(DbgAsyncStepInfo[] stepInfos, FieldDef builderField, uint catchHandlerOffset, uint setResultOffset)`
  - Summary: Constructor
  - Parameters:
    - `DbgAsyncStepInfo[] stepInfos`: Async step infos
    - `FieldDef builderField`: Async method builder field or null if it's unknown
    - `uint catchHandlerOffset`: Catch handler offset or . Only used if it's a async void method
    - `uint setResultOffset`: Offset of SetResult() call, or if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncMethodDebugInfo.cs` (line 55)

### Properties

- `public DbgAsyncStepInfo[] StepInfos { get; }`
  - Summary: Async step infos
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncMethodDebugInfo.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StepInfos;
    ```
- `public FieldDef BuilderFieldOrNull { get; }`
  - Summary: Async method builder field or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncMethodDebugInfo.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BuilderFieldOrNull;
    ```
- `public uint CatchHandlerOffset { get; }`
  - Summary: Catch handler offset or . Only used if it's an async void method
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncMethodDebugInfo.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CatchHandlerOffset;
    ```
- `public uint SetResultOffset { get; }`
  - Summary: Offset of SetResult() call, or if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncMethodDebugInfo.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SetResultOffset;
    ```

## Struct `DbgAsyncStepInfo`

Async method step info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgAsyncStepInfo(yieldOffset: /* uint */, resumeMethod: /* MethodDef */, resumeOffset: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncStepInfo.cs` (line 27)

### Constructors

- `public DbgAsyncStepInfo(uint yieldOffset, MethodDef resumeMethod, uint resumeOffset)`
  - Summary: Constructor
  - Parameters:
    - `uint yieldOffset`: Offset in where it starts waiting for the result
    - `MethodDef resumeMethod`: Resume method
    - `uint resumeOffset`: Offset in where it resumes after the result is available
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncStepInfo.cs` (line 49)

### Properties

- `public MethodDef ResumeMethod { get; }`
  - Summary: Resume method
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncStepInfo.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResumeMethod;
    ```
- `public uint ResumeOffset { get; }`
  - Summary: Offset in where it resumes after the result is available
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncStepInfo.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResumeOffset;
    ```
- `public uint YieldOffset { get; }`
  - Summary: Offset in method where it starts waiting for the result
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgAsyncStepInfo.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.YieldOffset;
    ```

## Struct `DbgCodeRange`

Code range

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgCodeRange(start: /* uint */, end: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgCodeRange.cs` (line 26)

### Constructors

- `public DbgCodeRange(uint start, uint end)`
  - Summary: Constructor
  - Parameters:
    - `uint start`: Start offset relative to the start of the method
    - `uint end`: End method offset (exclusive) relative to the start of the method
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgCodeRange.cs` (line 47)

### Methods

- `public bool Contains(uint offset)`
  - Summary: Checks whether is within this range
  - Parameters:
    - `uint offset`: Offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgCodeRange.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.Contains(offset: /* uint */);
    ```

### Properties

- `public uint End { get; }`
  - Summary: Gets the end method offset (exclusive) relative to the start of the method
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgCodeRange.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.End;
    ```
- `public uint Length => End - Start`
  - Summary: Gets the length of the range
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgCodeRange.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public uint Start { get; }`
  - Summary: Gets the start offset relative to the start of the method
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgCodeRange.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Start;
    ```

## Enum `DbgCompilerKind`

Compilers

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.DbgCompilerKind and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgCompilerKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgCompilerKind.cs` (line 24)

### Members

- `Unknown`: Unknown compiler
- `MicrosoftCSharp`: Microsoft C# compiler
- `MicrosoftVisualBasic`: Microsoft Visual Basic compiler
- `MonoCSharp`: Mono C# compiler

## Class `DbgDotNetCodeLocation`

.NET code location

**Inherits/Implements:** `DbgCodeLocation`, `IDbgDotNetCodeLocation`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetCodeLocation and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetCodeLocation(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetCodeLocation.cs` (line 27)

### Properties

- `public abstract DbgDotNetNativeFunctionAddress NativeAddress { get; }`
  - Summary: Gets the native address
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetCodeLocation.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NativeAddress;
    ```
- `public abstract DbgILOffsetMapping ILOffsetMapping { get; }`
  - Summary: Gets the IL offset mapping
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetCodeLocation.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ILOffsetMapping;
    ```
- `public abstract DbgModule DbgModule { get; }`
  - Summary: Gets the debugger module or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetCodeLocation.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DbgModule;
    ```
- `public abstract ModuleId Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetCodeLocation.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public abstract uint Offset { get; }`
  - Summary: Gets the IL offset within the method body
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetCodeLocation.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```
- `public abstract uint Token { get; }`
  - Summary: Gets the token of a method within the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetCodeLocation.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

## Class `DbgDotNetCodeLocationFactory`

Creates instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetCodeLocationFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetCodeLocationFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetCodeLocationFactory.cs` (line 26)

### Methods

- `public DbgDotNetCodeLocation Create(ModuleId module, uint token, uint offset)`
  - Summary: Creates a new instance
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a method within the module
    - `uint offset`: IL offset of the location within the method body
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetCodeLocationFactory.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleId */, token: /* uint */, offset: /* uint */);
    ```
- `public abstract DbgDotNetCodeLocation Create(ModuleId module, uint token, uint offset, DbgILOffsetMapping ilOffsetMapping)`
  - Summary: Creates a new instance
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a method within the module
    - `uint offset`: IL offset of the location within the method body
    - `DbgILOffsetMapping ilOffsetMapping`: IL offset mapping
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetCodeLocationFactory.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleId */, token: /* uint */, offset: /* uint */, ilOffsetMapping: /* DbgILOffsetMapping */);
    ```

## Class `DbgDotNetDecompilerGuidProvider`

Converts s to decompiler GUIDs. Use to export an instance

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetDecompilerGuidProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetDecompilerGuidProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetDecompilerGuidProvider.cs` (line 29)

### Methods

- `public abstract Guid? GetDecompilerGuid(DbgLanguage language)`
  - Summary: Gets the decompiler GUID or null
  - Parameters:
    - `DbgLanguage language`: Language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetDecompilerGuidProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDecompilerGuid(language: /* DbgLanguage */);
    ```

## Class `DbgDotNetDecompilerService`

Returns the decompiler that should be used by code that needs to use a decompiler to format methods. The decompiler gets updated when the gets changed.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetDecompilerService and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetDecompilerService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetDecompilerService.cs` (line 29)

### Properties

- `public abstract IDecompiler Decompiler { get; }`
  - Summary: Gets the decompiler
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetDecompilerService.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Decompiler;
    ```

### Events

- `public abstract event EventHandler<EventArgs> DecompilerChanged`
  - Summary: Raised after is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetDecompilerService.cs` (line 38)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.DecompilerChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DbgDotNetInstructionOffsetConstants`

Constants

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetInstructionOffsetConstants members directly without instantiation.
dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetInstructionOffsetConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetInstructionOffsetConstants.cs` (line 24)

### Fields

- `public const uint EPILOG = 0xFFFFFFFF`
  - Summary: The offset is in an epilog
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetInstructionOffsetConstants.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetInstructionOffsetConstants.EPILOG;
    ```
- `public const uint PROLOG = 0xFFFFFFFE`
  - Summary: The offset is in the prolog
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetInstructionOffsetConstants.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetInstructionOffsetConstants.PROLOG;
    ```

## Struct `DbgDotNetNativeFunctionAddress`

Native address info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetNativeFunctionAddress(address: /* ulong */, offset: /* ulong */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 61)

### Constructors

- `public DbgDotNetNativeFunctionAddress(ulong address, ulong offset)`
  - Summary: Constructor
  - Parameters:
    - `ulong address`: Address or 0 if it's not available
    - `ulong offset`: Offset relative to
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 87)

### Properties

- `public ulong Address { get; }`
  - Summary: Gets the address or 0 if it's not available
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```
- `public ulong IP => Address + Offset`
  - Summary: Gets the instruction pointer
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IP;
    ```
- `public ulong Offset { get; }`
  - Summary: Gets the offset relative to
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```

### Fields

- `public static readonly DbgDotNetNativeFunctionAddress None = default`
  - Summary: No address
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 65)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Code.DbgDotNetNativeFunctionAddress.None;
    ```

## Struct `DbgILInstruction`

IL instruction

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgILInstruction(offset: /* uint */, opCode: /* ushort */, operand: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILInstruction.cs` (line 24)

### Constructors

- `public DbgILInstruction(uint offset, ushort opCode, uint operand)`
  - Summary: Constructor
  - Parameters:
    - `uint offset`: Offset of instruction
    - `ushort opCode`: IL opcode
    - `uint operand`: Integer operand
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILInstruction.cs` (line 46)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILInstruction.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public uint Offset { get; }`
  - Summary: Gets the offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILInstruction.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```
- `public uint Operand { get; }`
  - Summary: Gets the operand
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILInstruction.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Operand;
    ```
- `public ushort OpCode { get; }`
  - Summary: Gets the opcode, 0x00XX or 0xFEXX
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILInstruction.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OpCode;
    ```

## Enum `DbgILOffsetMapping`

IL offset mapping result. This enum is similar to CorDebugMappingResult

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.DbgILOffsetMapping and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgILOffsetMapping(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILOffsetMapping.cs` (line 24)

### Members

- `Unknown`: Unknown
- `Prolog`: The native code is in the prolog
- `Epilog`: The native code is in an epilog
- `Exact`: Either the method maps exactly to MSIL code or the frame has been interpreted, so the value of the IP is accurate
- `Approximate`: The method was successfully mapped, but the value of the IP may be approximate
- `NoInfo`: No mapping information is available for the method
- `UnmappedAddress`: Although there is mapping information for the method, the current address cannot be mapped to Microsoft intermediate language (MSIL) code

## Struct `DbgILSpan`

IL span

**Inherits/Implements:** `IEquatable<DbgILSpan>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgILSpan(start: /* uint */, length: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 27)

### Constructors

- `public DbgILSpan(uint start, uint length)`
  - Summary: Constructor
  - Parameters:
    - `uint start`: Start offset
    - `uint length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 55)

### Methods

- `public bool Equals(DbgILSpan other)`
  - Summary: Equals()
  - Parameters:
    - `DbgILSpan other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgILSpan */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 145)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static DbgILSpan FromBounds(uint start, uint end)`
  - Summary: Creates a new instance
  - Parameters:
    - `uint start`: Start offset
    - `uint end`: End offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgILSpan.FromBounds(start: /* uint */, end: /* uint */);
    ```

### Properties

- `public bool IsEmpty => end == start`
  - Summary: true if it's empty ( is 0)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public uint End => end`
  - Summary: End offset, exclusive
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.End;
    ```
- `public uint Length => end - start`
  - Summary: Length ( - )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public uint Start => start`
  - Summary: Start offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Start;
    ```

### Operators

- `public static bool operator !=(DbgILSpan left, DbgILSpan right) => !left.Equals(right);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 119)
- `public static bool operator ==(DbgILSpan left, DbgILSpan right) => left.Equals(right);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgILSpan.cs` (line 111)

## Struct `DbgImportInfo`

Import info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo(targetKind: /* DbgImportInfoKind */, target: /* string */, alias: /* string */, externAlias: /* string */, importScopeKind: /* DbgVBImportScopeKind */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 130)

### Constructors

- `public DbgImportInfo(DbgImportInfoKind targetKind, string target = null, string alias = null, string externAlias = null, DbgVBImportScopeKind importScopeKind = DbgVBImportScopeKind.None)`
  - Summary: Constructor
  - Parameters:
    - `DbgImportInfoKind targetKind`: Target kind
    - `string target` (default: `null`): Target string
    - `string alias` (default: `null`): Alias
    - `string externAlias` (default: `null`): Extern alias
    - `DbgVBImportScopeKind importScopeKind` (default: `DbgVBImportScopeKind.None`): VB import scope kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 164)

### Methods

- `public static DbgImportInfo CreateAssembly(string externAlias)`
  - Parameters:
    - `string externAlias`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 179)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateAssembly(externAlias: /* string */);
    ```
- `public static DbgImportInfo CreateAssembly(string externAlias, string assembly)`
  - Parameters:
    - `string externAlias`: Description not provided.
    - `string assembly`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 180)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateAssembly(externAlias: /* string */, assembly: /* string */);
    ```
- `public static DbgImportInfo CreateCurrentNamespace()`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateCurrentNamespace();
    ```
- `public static DbgImportInfo CreateDefaultNamespace(string @namespace)`
  - Parameters:
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateDefaultNamespace(@namespace: /* string */);
    ```
- `public static DbgImportInfo CreateMethodToken(string token, DbgVBImportScopeKind importScopeKind)`
  - Parameters:
    - `string token`: Description not provided.
    - `DbgVBImportScopeKind importScopeKind`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 186)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateMethodToken(token: /* string */, importScopeKind: /* DbgVBImportScopeKind */);
    ```
- `public static DbgImportInfo CreateNamespace(string @namespace)`
  - Parameters:
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 173)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateNamespace(@namespace: /* string */);
    ```
- `public static DbgImportInfo CreateNamespace(string @namespace, DbgVBImportScopeKind importScopeKind)`
  - Parameters:
    - `string @namespace`: Description not provided.
    - `DbgVBImportScopeKind importScopeKind`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 185)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateNamespace(@namespace: /* string */, importScopeKind: /* DbgVBImportScopeKind */);
    ```
- `public static DbgImportInfo CreateNamespace(string @namespace, string externAlias)`
  - Parameters:
    - `string @namespace`: Description not provided.
    - `string externAlias`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 174)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateNamespace(@namespace: /* string */, externAlias: /* string */);
    ```
- `public static DbgImportInfo CreateNamespaceAlias(string @namespace, string alias)`
  - Parameters:
    - `string @namespace`: Description not provided.
    - `string alias`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 176)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateNamespaceAlias(@namespace: /* string */, alias: /* string */);
    ```
- `public static DbgImportInfo CreateNamespaceAlias(string @namespace, string alias, string externAlias)`
  - Parameters:
    - `string @namespace`: Description not provided.
    - `string alias`: Description not provided.
    - `string externAlias`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 178)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateNamespaceAlias(@namespace: /* string */, alias: /* string */, externAlias: /* string */);
    ```
- `public static DbgImportInfo CreateNamespaceOrType(string namespaceOrType, string alias, DbgVBImportScopeKind importScopeKind)`
  - Parameters:
    - `string namespaceOrType`: Description not provided.
    - `string alias`: Description not provided.
    - `DbgVBImportScopeKind importScopeKind`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateNamespaceOrType(namespaceOrType: /* string */, alias: /* string */, importScopeKind: /* DbgVBImportScopeKind */);
    ```
- `public static DbgImportInfo CreateType(string type)`
  - Parameters:
    - `string type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateType(type: /* string */);
    ```
- `public static DbgImportInfo CreateType(string type, DbgVBImportScopeKind importScopeKind)`
  - Parameters:
    - `string type`: Description not provided.
    - `DbgVBImportScopeKind importScopeKind`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 184)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateType(type: /* string */, importScopeKind: /* DbgVBImportScopeKind */);
    ```
- `public static DbgImportInfo CreateTypeAlias(string type, string alias)`
  - Parameters:
    - `string type`: Description not provided.
    - `string alias`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 177)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateTypeAlias(type: /* string */, alias: /* string */);
    ```
- `public static DbgImportInfo CreateXmlNamespace(string xmlNamespace, string alias, DbgVBImportScopeKind importScopeKind)`
  - Parameters:
    - `string xmlNamespace`: Description not provided.
    - `string alias`: Description not provided.
    - `DbgVBImportScopeKind importScopeKind`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 183)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfo.CreateXmlNamespace(xmlNamespace: /* string */, alias: /* string */, importScopeKind: /* DbgVBImportScopeKind */);
    ```

### Properties

- `public DbgImportInfoKind TargetKind { get; }`
  - Summary: Target kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TargetKind;
    ```
- `public DbgVBImportScopeKind VBImportScopeKind { get; }`
  - Summary: Gets the VB import scope kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 139)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VBImportScopeKind;
    ```
- `public string Alias { get; }`
  - Summary: Alias
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 149)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Alias;
    ```
- `public string ExternAlias { get; }`
  - Summary: Extern alias
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 154)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExternAlias;
    ```
- `public string Target { get; }`
  - Summary: Target
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 144)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Target;
    ```

## Enum `DbgImportInfoKind`

Import kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfoKind and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgImportInfoKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 65)

### Members

- `Namespace`: Namespace import
- `Type`: Type import
- `NamespaceOrType`: Namespace or type import
- `Assembly`: C#: extern alias
- `XmlNamespace`: VB: XML import
- `MethodToken`: VB: token of method with imports
- `CurrentNamespace`: VB: containing namespace
- `DefaultNamespace`: VB: root namespace

## Struct `DbgLocal`

Method local info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgLocal(index: /* int */, name: /* string */, hoistedField: /* FieldDef */, flags: /* DbgLocalFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgLocal.cs` (line 27)

### Constructors

- `public DbgLocal(int index, string name, FieldDef hoistedField, DbgLocalFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `int index`: Index of local or < 0 if it's not in the metadata
    - `string name`: Name of the local
    - `FieldDef hoistedField`: Hoisted field or null if it's not a hoisted local/parameter
    - `DbgLocalFlags flags`: Local flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgLocal.cs` (line 65)

### Properties

- `public DbgLocalFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgLocal.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public FieldDef HoistedField { get; }`
  - Summary: Gets the hoisted field or null if it's not a hoisted local
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgLocal.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HoistedField;
    ```
- `public bool IsDebuggerHidden => (Flags & DbgLocalFlags.DebuggerHidden) != 0`
  - Summary: true if this is a debugger hidden local
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgLocal.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDebuggerHidden;
    ```
- `public bool IsDecompilerGenerated => (Flags & DbgLocalFlags.DecompilerGenerated) != 0`
  - Summary: true if this is a decompiler generated local
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgLocal.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDecompilerGenerated;
    ```
- `public int Index { get; }`
  - Summary: Gets the local index or < 0 if it's not in the metadata
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgLocal.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Index;
    ```
- `public string Name { get; }`
  - Summary: Gets the name of the local
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgLocal.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Enum `DbgLocalFlags`

Locals flags

**Inherits/Implements:** `uint`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.DbgLocalFlags and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgLocalFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgLocal.cs` (line 76)

### Members

- `None`: No bit is set
- `DecompilerGenerated` = `x00000001`: Decompiler generated local
- `DebuggerHidden` = `x00000002`: Debugger hidden local

## Class `DbgMethodDebugInfo`

Method debug info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgMethodDebugInfo(compiler: /* DbgCompilerKind */, debugInfoVersion: /* int */, method: /* MethodDef */, parameters: /* DbgParameter[] */, statements: /* DbgSourceStatement[] */, scope: /* DbgMethodDebugScope */, asyncMethodDebugInfo: /* DbgAsyncMethodDebugInfo */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 31)

### Constructors

- `public DbgMethodDebugInfo(DbgCompilerKind compiler, int debugInfoVersion, MethodDef method, DbgParameter[] parameters, DbgSourceStatement[] statements, DbgMethodDebugScope scope, DbgAsyncMethodDebugInfo asyncMethodDebugInfo)`
  - Summary: Constructor
  - Parameters:
    - `DbgCompilerKind compiler`: Compiler
    - `int debugInfoVersion`: Debug info version
    - `MethodDef method`: Method
    - `DbgParameter[] parameters`: Parameters or null
    - `DbgSourceStatement[] statements`: Statements
    - `DbgMethodDebugScope scope`: Root scope
    - `DbgAsyncMethodDebugInfo asyncMethodDebugInfo`: Async info or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 78)

### Methods

- `public DbgILSpan[] GetILSpansOfStatement(DbgTextSpan statementSpan)`
  - Summary: Gets all ILSpans of a statement
  - Parameters:
    - `DbgTextSpan statementSpan`: Statement span
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 169)
  - Example:
    ```csharp
    // Example invocation
    instance.GetILSpansOfStatement(statementSpan: /* DbgTextSpan */);
    ```
- `public DbgILSpan[] GetRanges(DbgILSpan[] sourceILSpans)`
  - Summary: Gets step ranges
  - Parameters:
    - `DbgILSpan[] sourceILSpans`: Source statement spans
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRanges(sourceILSpans: /* DbgILSpan[] */);
    ```
- `public DbgILSpan[] GetUnusedRanges()`
  - Summary: Gets unused step ranges
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    instance.GetUnusedRanges();
    ```
- `public DbgSourceStatement? GetSourceStatementByCodeOffset(uint ilOffset)`
  - Summary: Gets a
  - Parameters:
    - `uint ilOffset`: IL offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 156)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSourceStatementByCodeOffset(ilOffset: /* uint */);
    ```

### Properties

- `public DbgAsyncMethodDebugInfo AsyncInfo { get; }`
  - Summary: Gets the async method debug info or null if it's not an async method
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsyncInfo;
    ```
- `public DbgCompilerKind Compiler { get; }`
  - Summary: Compiler used to compile the code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Compiler;
    ```
- `public DbgMethodDebugScope Scope { get; }`
  - Summary: Gets the root scope
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Scope;
    ```
- `public DbgParameter[] Parameters { get; }`
  - Summary: Gets the parameters. There could be missing parameters, in which case use . This array isn't sorted.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Parameters;
    ```
- `public DbgSourceStatement[] Statements { get; }`
  - Summary: Gets all statements, sorted by
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Statements;
    ```
- `public MethodDef Method { get; }`
  - Summary: Gets the method
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Method;
    ```
- `public int DebugInfoVersion { get; }`
  - Summary: Version number of this method debug info. If it gets incremented, any older instances with a different version should not be used again.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugInfo.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DebugInfoVersion;
    ```

## Class `DbgMethodDebugScope`

Method scope

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgMethodDebugScope(span: /* DbgILSpan */, scopes: /* DbgMethodDebugScope[] */, locals: /* DbgLocal[] */, imports: /* DbgImportInfo[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 26)

### Constructors

- `public DbgMethodDebugScope(DbgILSpan span, DbgMethodDebugScope[] scopes, DbgLocal[] locals, DbgImportInfo[] imports)`
  - Summary: Constructor
  - Parameters:
    - `DbgILSpan span`: Scope span
    - `DbgMethodDebugScope[] scopes`: Child scopes
    - `DbgLocal[] locals`: Locals
    - `DbgImportInfo[] imports`: Imports
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 54)

### Properties

- `public DbgILSpan Span { get; }`
  - Summary: Gets the span of this scope
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public DbgImportInfo[] Imports { get; }`
  - Summary: Gets all new imports in the scope
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Imports;
    ```
- `public DbgLocal[] Locals { get; }`
  - Summary: Gets all new locals in the scope
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Locals;
    ```
- `public DbgMethodDebugScope[] Scopes { get; }`
  - Summary: Gets all child scopes
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Scopes;
    ```

## Struct `DbgParameter`

Method parameter info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgParameter(index: /* int */, name: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgParameter.cs` (line 26)

### Constructors

- `public DbgParameter(int index, string name)`
  - Summary: Constructor
  - Parameters:
    - `int index`: Parameter index
    - `string name`: Parameter name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgParameter.cs` (line 42)

### Properties

- `public int Index { get; }`
  - Summary: Gets the parameter index
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgParameter.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Index;
    ```
- `public string Name { get; }`
  - Summary: Gets the parameter name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgParameter.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Struct `DbgSourceStatement`

Source statement

**Inherits/Implements:** `IEquatable<DbgSourceStatement>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgSourceStatement(ilSpan: /* DbgILSpan */, textSpan: /* DbgTextSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgSourceStatement.cs` (line 27)

### Constructors

- `public DbgSourceStatement(DbgILSpan ilSpan, DbgTextSpan textSpan)`
  - Summary: Constructor
  - Parameters:
    - `DbgILSpan ilSpan`: IL span
    - `DbgTextSpan textSpan`: Text span
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgSourceStatement.cs` (line 51)

### Methods

- `public bool Equals(DbgSourceStatement other)`
  - Summary: Equals()
  - Parameters:
    - `DbgSourceStatement other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgSourceStatement.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgSourceStatement */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgSourceStatement.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgSourceStatement.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgSourceStatement.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DbgILSpan ILSpan => ilSpan`
  - Summary: IL span
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgSourceStatement.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ILSpan;
    ```
- `public DbgTextSpan TextSpan => textSpan`
  - Summary: Text span
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgSourceStatement.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextSpan;
    ```

### Operators

- `public static bool operator !=(DbgSourceStatement left, DbgSourceStatement right) => !left.Equals(right);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgSourceStatement.cs` (line 70)
- `public static bool operator ==(DbgSourceStatement left, DbgSourceStatement right) => left.Equals(right);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgSourceStatement.cs` (line 62)

## Struct `DbgTextSpan`

Text span

**Inherits/Implements:** `IEquatable<DbgTextSpan>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgTextSpan(start: /* int */, length: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 26)

### Constructors

- `public DbgTextSpan(int start, int length)`
  - Summary: Constructor
  - Parameters:
    - `int start`: Start offset
    - `int length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 54)

### Methods

- `public bool Equals(DbgTextSpan other)`
  - Summary: Equals()
  - Parameters:
    - `DbgTextSpan other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 92)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgTextSpan */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static DbgTextSpan FromBounds(int start, int end)`
  - Summary: Creates a new instance
  - Parameters:
    - `int start`: Start offset
    - `int end`: End offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Code.DbgTextSpan.FromBounds(start: /* int */, end: /* int */);
    ```

### Properties

- `public bool IsEmpty => end == start`
  - Summary: true if it's empty ( is 0)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public int End => end`
  - Summary: End offset, exclusive
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.End;
    ```
- `public int Length => end - start`
  - Summary: Length ( - )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public int Start => start`
  - Summary: Start offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Start;
    ```

### Operators

- `public static bool operator !=(DbgTextSpan left, DbgTextSpan right) => !left.Equals(right);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 85)
- `public static bool operator ==(DbgTextSpan left, DbgTextSpan right) => left.Equals(right);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgTextSpan.cs` (line 77)

## Enum `DbgVBImportScopeKind`

Visual Basic import scope kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.DbgVBImportScopeKind and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.DbgVBImportScopeKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgMethodDebugScope.cs` (line 110)

### Members

- `None`: Unspecified scope
- `File`: File scope
- `Project`: Project scope

## Class `ExportDbgDotNetDecompilerGuidProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgDotNetDecompilerGuidProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.ExportDbgDotNetDecompilerGuidProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetDecompilerGuidProvider.cs` (line 47)

### Constructors

- `public ExportDbgDotNetDecompilerGuidProviderAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetDecompilerGuidProvider.cs` (line 53)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetDecompilerGuidProvider.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDbgDotNetCodeLocation`

.NET code location

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.IDbgDotNetCodeLocation and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.IDbgDotNetCodeLocation(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 26)

### Properties

- `DbgDotNetNativeFunctionAddress NativeAddress { get; }`
  - Summary: Gets the native address
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NativeAddress;
    ```
- `DbgILOffsetMapping ILOffsetMapping { get; }`
  - Summary: Gets the IL offset mapping
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ILOffsetMapping;
    ```
- `DbgModule DbgModule { get; }`
  - Summary: Gets the debugger module or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DbgModule;
    ```
- `ModuleId Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `uint Offset { get; }`
  - Summary: Gets the IL offset within the method body
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```
- `uint Token { get; }`
  - Summary: Gets the token of a method within the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/IDbgDotNetCodeLocation.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

## Interface `IDbgDotNetDecompilerGuidProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Code.IDbgDotNetDecompilerGuidProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Code.IDbgDotNetDecompilerGuidProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetDecompilerGuidProvider.cs` (line 39)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Code/DbgDotNetDecompilerGuidProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

