# Namespace `dnSpy.Contracts.Debugger.Disassembly`

## Enum `DbgNativeCodeOptions`

Native code options

**Inherits/Implements:** `uint`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Disassembly.DbgNativeCodeOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Disassembly.DbgNativeCodeOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 117)

### Members

- `None`: No option is enabled
- `ShowILCode` = `x00000001`: Show IL code, if available
- `ShowCode` = `x00000002`: Show source code or decompiled code, if available

## Class `DbgNativeCodeProvider`

Returns a method's native code

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Disassembly.DbgNativeCodeProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Disassembly.DbgNativeCodeProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 30)

### Methods

- `public abstract bool CanGetNativeCode(DbgBoundCodeBreakpoint boundBreakpoint)`
  - Summary: Checks if it's possible to get native code
  - Parameters:
    - `DbgBoundCodeBreakpoint boundBreakpoint`: A bound breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.CanGetNativeCode(boundBreakpoint: /* DbgBoundCodeBreakpoint */);
    ```
- `public abstract bool CanGetNativeCode(DbgRuntime runtime, DbgCodeLocation location)`
  - Summary: Checks if it's possible to get native code
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `DbgCodeLocation location`: Code location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.CanGetNativeCode(runtime: /* DbgRuntime */, location: /* DbgCodeLocation */);
    ```
- `public abstract bool CanGetNativeCode(DbgStackFrame frame)`
  - Summary: Checks if it's possible to get native code
  - Parameters:
    - `DbgStackFrame frame`: Stack frame
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.CanGetNativeCode(frame: /* DbgStackFrame */);
    ```
- `public abstract bool TryGetNativeCode(DbgBoundCodeBreakpoint boundBreakpoint, DbgNativeCodeOptions options, out GetNativeCodeResult result)`
  - Summary: Tries to get the native code
  - Parameters:
    - `DbgBoundCodeBreakpoint boundBreakpoint`: A bound breakpoint
    - `DbgNativeCodeOptions options`: Options
    - `out GetNativeCodeResult result`: Native code if successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetNativeCode(boundBreakpoint: /* DbgBoundCodeBreakpoint */, options: /* DbgNativeCodeOptions */, result: /* GetNativeCodeResult */);
    ```
- `public abstract bool TryGetNativeCode(DbgRuntime runtime, DbgCodeLocation location, DbgNativeCodeOptions options, out GetNativeCodeResult result)`
  - Summary: Tries to get the native code
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `DbgCodeLocation location`: Code location
    - `DbgNativeCodeOptions options`: Options
    - `out GetNativeCodeResult result`: Native code if successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetNativeCode(runtime: /* DbgRuntime */, location: /* DbgCodeLocation */, options: /* DbgNativeCodeOptions */, result: /* GetNativeCodeResult */);
    ```
- `public abstract bool TryGetNativeCode(DbgStackFrame frame, DbgNativeCodeOptions options, out GetNativeCodeResult result)`
  - Summary: Tries to get the native code
  - Parameters:
    - `DbgStackFrame frame`: Stack frame
    - `DbgNativeCodeOptions options`: Options
    - `out GetNativeCodeResult result`: Native code if successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetNativeCode(frame: /* DbgStackFrame */, options: /* DbgNativeCodeOptions */, result: /* GetNativeCodeResult */);
    ```

## Class `DbgRuntimeNativeCodeProvider`

Returns native method bodies. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Disassembly.DbgRuntimeNativeCodeProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Disassembly.DbgRuntimeNativeCodeProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 31)

### Methods

- `public abstract bool CanGetNativeCode(DbgBoundCodeBreakpoint boundBreakpoint)`
  - Summary: Checks if it's possible to get native code
  - Parameters:
    - `DbgBoundCodeBreakpoint boundBreakpoint`: A bound breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.CanGetNativeCode(boundBreakpoint: /* DbgBoundCodeBreakpoint */);
    ```
- `public abstract bool CanGetNativeCode(DbgRuntime runtime, DbgCodeLocation location)`
  - Summary: Checks if it's possible to get native code
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `DbgCodeLocation location`: Code location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.CanGetNativeCode(runtime: /* DbgRuntime */, location: /* DbgCodeLocation */);
    ```
- `public abstract bool CanGetNativeCode(DbgStackFrame frame)`
  - Summary: Checks if it's possible to get native code
  - Parameters:
    - `DbgStackFrame frame`: Stack frame
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.CanGetNativeCode(frame: /* DbgStackFrame */);
    ```
- `public abstract bool TryGetNativeCode(DbgBoundCodeBreakpoint boundBreakpoint, DbgNativeCodeOptions options, out GetNativeCodeResult result)`
  - Summary: Tries to get the native code
  - Parameters:
    - `DbgBoundCodeBreakpoint boundBreakpoint`: A bound breakpoint
    - `DbgNativeCodeOptions options`: Options
    - `out GetNativeCodeResult result`: Native code if successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetNativeCode(boundBreakpoint: /* DbgBoundCodeBreakpoint */, options: /* DbgNativeCodeOptions */, result: /* GetNativeCodeResult */);
    ```
- `public abstract bool TryGetNativeCode(DbgRuntime runtime, DbgCodeLocation location, DbgNativeCodeOptions options, out GetNativeCodeResult result)`
  - Summary: Tries to get the native code
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `DbgCodeLocation location`: Code location
    - `DbgNativeCodeOptions options`: Options
    - `out GetNativeCodeResult result`: Native code if successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetNativeCode(runtime: /* DbgRuntime */, location: /* DbgCodeLocation */, options: /* DbgNativeCodeOptions */, result: /* GetNativeCodeResult */);
    ```
- `public abstract bool TryGetNativeCode(DbgStackFrame frame, DbgNativeCodeOptions options, out GetNativeCodeResult result)`
  - Summary: Tries to get the native code
  - Parameters:
    - `DbgStackFrame frame`: Stack frame
    - `DbgNativeCodeOptions options`: Options
    - `out GetNativeCodeResult result`: Native code if successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetNativeCode(frame: /* DbgStackFrame */, options: /* DbgNativeCodeOptions */, result: /* GetNativeCodeResult */);
    ```

## Class `ExportDbgRuntimeNativeCodeProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgRuntimeNativeCodeProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Disassembly.ExportDbgRuntimeNativeCodeProviderAttribute(guid: /* string */, runtimeKindGuid: /* string */, order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 96)

### Constructors

- `public ExportDbgRuntimeNativeCodeProviderAttribute(string guid, string runtimeKindGuid, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string guid`: Runtime GUID or null, see
    - `string runtimeKindGuid`: Runtime kind GUID or null, see
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 104)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 124)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string Guid { get; }`
  - Summary: Gets the runtime GUID or null, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 114)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public string RuntimeKindGuid { get; }`
  - Summary: Gets the runtime kind GUID or null, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 119)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeKindGuid;
    ```

## Struct `GetNativeCodeResult`

Native code result

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Disassembly.GetNativeCodeResult(code: /* NativeCode */, symbolResolver: /* ISymbolResolver */, header: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 85)

### Constructors

- `public GetNativeCodeResult(NativeCode code, ISymbolResolver symbolResolver, string header)`
  - Summary: Constructor
  - Parameters:
    - `NativeCode code`: Native code
    - `ISymbolResolver symbolResolver`: Symbol resolver or null
    - `string header`: Header or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 107)

### Properties

- `public ISymbolResolver SymbolResolver { get; }`
  - Summary: Symbol resolver or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SymbolResolver;
    ```
- `public NativeCode Code { get; }`
  - Summary: Native code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 89)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Code;
    ```
- `public string Header { get; }`
  - Summary: Header or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgNativeCodeProvider.cs` (line 99)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Header;
    ```

## Interface `IDbgRuntimeNativeCodeProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Disassembly.IDbgRuntimeNativeCodeProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Disassembly.IDbgRuntimeNativeCodeProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 84)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 90)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string Guid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `string RuntimeKindGuid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Disassembly/DbgRuntimeNativeCodeProvider.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeKindGuid;
    ```

