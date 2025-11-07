# Namespace `dnSpy.Contracts.Debugger.DotNet.CorDebug.Code`

## Class `DbgDotNetNativeCodeLocation`

A .NET method body location including an exact native address

**Inherits/Implements:** `DbgCodeLocation`, `IDbgDotNetCodeLocation`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.CorDebug.Code.DbgDotNetNativeCodeLocation and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.CorDebug.Code.DbgDotNetNativeCodeLocation(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/Code/DbgDotNetNativeCodeLocation.cs` (line 28)

### Properties

- `public abstract DbgDotNetNativeFunctionAddress NativeAddress { get; }`
  - Summary: Gets the native address
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/Code/DbgDotNetNativeCodeLocation.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NativeAddress;
    ```
- `public abstract DbgILOffsetMapping ILOffsetMapping { get; }`
  - Summary: Gets the IL offset mapping
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/Code/DbgDotNetNativeCodeLocation.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ILOffsetMapping;
    ```
- `public abstract DbgModule DbgModule { get; }`
  - Summary: Gets the debugger module or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/Code/DbgDotNetNativeCodeLocation.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DbgModule;
    ```
- `public abstract ModuleId Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/Code/DbgDotNetNativeCodeLocation.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public abstract uint Offset { get; }`
  - Summary: Gets the IL offset within the method body
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/Code/DbgDotNetNativeCodeLocation.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```
- `public abstract uint Token { get; }`
  - Summary: Gets the token of a method within the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/Code/DbgDotNetNativeCodeLocation.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

