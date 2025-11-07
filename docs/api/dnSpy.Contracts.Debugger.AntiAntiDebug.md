# Namespace `dnSpy.Contracts.Debugger.AntiAntiDebug`

## Class `DbgHookedNativeFunction`

Hooked function. The owner can write their own code by calling

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.AntiAntiDebug.DbgHookedNativeFunction and call its members.
var instance = new dnSpy.Contracts.Debugger.AntiAntiDebug.DbgHookedNativeFunction(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunction.cs` (line 24)

### Methods

- `public abstract void WriteByte(byte value)`
  - Summary: Writes the next byte to the code section
  - Parameters:
    - `byte value`: Byte to write
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunction.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteByte(value: /* byte */);
    ```

### Properties

- `public abstract ulong CurrentAddress { get; }`
  - Summary: Gets the next address that will write to
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunction.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CurrentAddress;
    ```
- `public abstract ulong NewCodeAddress { get; }`
  - Summary: Gets the address of the new hooked function. The first written byte will be written to this location. The original function is patched to jump to this address.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunction.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewCodeAddress;
    ```
- `public abstract ulong NewFunctionAddress { get; }`
  - Summary: Gets the address of the original function after it has been moved. This address can be used to call the original function from the new code.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunction.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewFunctionAddress;
    ```
- `public abstract ulong OriginalFunctionAddress { get; }`
  - Summary: Gets the address of the function, which has been hooked by us. If you must call the real function from the new code, call and not this address.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunction.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OriginalFunctionAddress;
    ```

## Class `DbgHookedNativeFunctionProvider`

Finds exported functions in native dlls

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.AntiAntiDebug.DbgHookedNativeFunctionProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.AntiAntiDebug.DbgHookedNativeFunctionProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunctionProvider.cs` (line 24)

### Methods

- `public abstract DbgHookedNativeFunction GetFunction(string dllName, string funcName)`
  - Summary: Gets a function
  - Parameters:
    - `string dllName`: DLL name including the dll extension
    - `string funcName`: Name of function
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunctionProvider.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFunction(dllName: /* string */, funcName: /* string */);
    ```
- `public abstract DbgHookedNativeFunction GetFunction(string dllName, string funcName, ulong address)`
  - Summary: Creates a hooked function
  - Parameters:
    - `string dllName`: DLL name including the dll extension
    - `string funcName`: Name of function
    - `ulong address`: Address of function
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunctionProvider.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFunction(dllName: /* string */, funcName: /* string */, address: /* ulong */);
    ```
- `public abstract bool TryGetFunction(string dllName, string funcName, out ulong address)`
  - Summary: Gets the address of a function
  - Parameters:
    - `string dllName`: DLL name including the dll extension
    - `string funcName`: Name of function
    - `out ulong address`: Address of function
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunctionProvider.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetFunction(dllName: /* string */, funcName: /* string */, address: /* ulong */);
    ```
- `public abstract bool TryGetModuleAddress(string dllName, out ulong address, out ulong endAddress)`
  - Summary: Gets the address of a module
  - Parameters:
    - `string dllName`: DLL name including the dll extension
    - `out ulong address`: Start address of module
    - `out ulong endAddress`: End address of module (exclusive)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgHookedNativeFunctionProvider.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetModuleAddress(dllName: /* string */, address: /* ulong */, endAddress: /* ulong */);
    ```

## Class `DbgNativeFunctionHookContext`

Context used by a

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.AntiAntiDebug.DbgNativeFunctionHookContext and call its members.
var instance = new dnSpy.Contracts.Debugger.AntiAntiDebug.DbgNativeFunctionHookContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgNativeFunctionHookContext.cs` (line 24)

### Properties

- `public abstract DbgHookedNativeFunctionProvider FunctionProvider { get; }`
  - Summary: Finds exported functions in loaded native modules in the target process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgNativeFunctionHookContext.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FunctionProvider;
    ```
- `public abstract DbgProcess Process { get; }`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/DbgNativeFunctionHookContext.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```

## Class `ExportDbgNativeFunctionHookAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgNativeFunctionHookMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.AntiAntiDebug.ExportDbgNativeFunctionHookAttribute(dll: /* string */, function: /* string */, architecture: /* DbgArchitecture */, operatingSystem: /* DbgOperatingSystem */, order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 61)

### Constructors

- `public ExportDbgNativeFunctionHookAttribute(string dll, string function, DbgArchitecture architecture, DbgOperatingSystem operatingSystem, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string dll`: DLL name including dll extension, case sensitive. It can be any name, it's only used to make sure only one handler patches a function.
    - `string function`: Function name, case sensitive. It can be any name, it's only used to make sure only one handler patches a function.
    - `DbgArchitecture architecture`: Supported architecture
    - `DbgOperatingSystem operatingSystem`: Supported operating system
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 71)
- `public ExportDbgNativeFunctionHookAttribute(string dll, string function, DbgArchitecture[] architectures, DbgOperatingSystem[] operatingSystems, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string dll`: DLL name including dll extension, case sensitive. It can be any name, it's only used to make sure only one handler patches a function.
    - `string function`: Function name, case sensitive. It can be any name, it's only used to make sure only one handler patches a function.
    - `DbgArchitecture[] architectures`: Supported architectures or empty to support all available architectures
    - `DbgOperatingSystem[] operatingSystems`: Supported operating systems or empty to support all operating systems
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 83)

### Properties

- `public DbgArchitecture[] Architectures { get; }`
  - Summary: Supported architectures or empty to support all available architectures
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 105)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Architectures;
    ```
- `public DbgOperatingSystem[] OperatingSystems { get; }`
  - Summary: Supported operating systems or empty to support all operating systems
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 110)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OperatingSystems;
    ```
- `public double Order { get; }`
  - Summary: Gets the order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 115)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string Dll { get; }`
  - Summary: DLL name including dll extension, case sensitive. It can be any name, it's only used to make sure only one handler patches a function.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 95)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Dll;
    ```
- `public string Function { get; }`
  - Summary: Function name, case sensitive. It can be any name, it's only used to make sure only one handler patches a function.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 100)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Function;
    ```

## Interface `IDbgNativeFunctionHook`

Hooks native functions when the debugged process starts. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.AntiAntiDebug.IDbgNativeFunctionHook and call its members.
var instance = new dnSpy.Contracts.Debugger.AntiAntiDebug.IDbgNativeFunctionHook(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 28)

### Methods

- `bool IsEnabled(DbgNativeFunctionHookContext context)`
  - Summary: Returns true if it's enabled
  - Parameters:
    - `DbgNativeFunctionHookContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* DbgNativeFunctionHookContext */);
    ```
- `void Hook(DbgNativeFunctionHookContext context, out string errorMessage)`
  - Summary: Hooks the function
  - Parameters:
    - `DbgNativeFunctionHookContext context`: Context
    - `out string errorMessage`: Updated with an error message if it failed or null if it was successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.Hook(context: /* DbgNativeFunctionHookContext */, errorMessage: /* string */);
    ```

## Interface `IDbgNativeFunctionHookMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.AntiAntiDebug.IDbgNativeFunctionHookMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.AntiAntiDebug.IDbgNativeFunctionHookMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 45)

### Properties

- `DbgArchitecture[] Architectures { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Architectures;
    ```
- `DbgOperatingSystem[] OperatingSystems { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OperatingSystems;
    ```
- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string Dll { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Dll;
    ```
- `string Function { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AntiAntiDebug/IDbgNativeFunctionHook.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Function;
    ```

