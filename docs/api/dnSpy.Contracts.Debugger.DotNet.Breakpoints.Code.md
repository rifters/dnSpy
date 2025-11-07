# Namespace `dnSpy.Contracts.Debugger.DotNet.Breakpoints.Code`

## Class `DbgDotNetBreakpointFactory`

Creates breakpoints and tracepoints

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Breakpoints.Code.DbgDotNetBreakpointFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Breakpoints.Code.DbgDotNetBreakpointFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 28)

### Methods

- `public DbgCodeBreakpoint Create(ModuleId module, uint token, uint offset)`
  - Summary: Creates an enabled breakpoint. If there's already a breakpoint at the location, null is returned.
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a method within the module
    - `uint offset`: IL offset of the breakpoint within the method body
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleId */, token: /* uint */, offset: /* uint */);
    ```
- `public DbgCodeBreakpoint Create(ModuleId module, uint token, uint offset, DbgCodeBreakpointSettings settings)`
  - Summary: Creates a breakpoint or a tracepoint. If there's already a breakpoint at the location, null is returned.
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a method within the module
    - `uint offset`: IL offset of the breakpoint within the method body
    - `DbgCodeBreakpointSettings settings`: Breakpoint settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleId */, token: /* uint */, offset: /* uint */, settings: /* DbgCodeBreakpointSettings */);
    ```
- `public DbgCodeBreakpoint CreateTracepoint(ModuleId module, uint token, uint offset, string message)`
  - Summary: Creates an enabled tracepoint. If there's already a breakpoint at the location, null is returned.
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a method within the module
    - `uint offset`: IL offset of the tracepoint within the method body
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTracepoint(module: /* ModuleId */, token: /* uint */, offset: /* uint */, message: /* string */);
    ```
- `public abstract DbgCodeBreakpoint TryGetBreakpoint(ModuleId module, uint token, uint offset)`
  - Summary: Returns an existing breakpoint or null if none exists
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a method within the module
    - `uint offset`: IL offset of the breakpoint within the method body
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetBreakpoint(module: /* ModuleId */, token: /* uint */, offset: /* uint */);
    ```
- `public abstract DbgCodeBreakpoint[] Create(DbgDotNetBreakpointInfo[] breakpoints)`
  - Summary: Creates breakpoints or tracepoints. Duplicate breakpoints are ignored.
  - Parameters:
    - `DbgDotNetBreakpointInfo[] breakpoints`: Breakpoint infos
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(breakpoints: /* DbgDotNetBreakpointInfo[] */);
    ```

## Struct `DbgDotNetBreakpointInfo`

Contains all required data to create a breakpoint

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Breakpoints.Code.DbgDotNetBreakpointInfo(module: /* ModuleId */, token: /* uint */, offset: /* uint */, settings: /* DbgCodeBreakpointSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 81)

### Constructors

- `public DbgDotNetBreakpointInfo(ModuleId module, uint token, uint offset, DbgCodeBreakpointSettings settings)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a method within the module
    - `uint offset`: IL offset of the breakpoint within the method body
    - `DbgCodeBreakpointSettings settings`: Breakpoint settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 109)

### Properties

- `public DbgCodeBreakpointSettings Settings { get; }`
  - Summary: Breakpoint settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 100)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```
- `public ModuleId Module { get; }`
  - Summary: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 85)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public uint Offset { get; }`
  - Summary: IL offset of the breakpoint within the method body
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 95)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```
- `public uint Token { get; }`
  - Summary: Token of a method within the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Breakpoints/Code/DbgDotNetBreakpointFactory.cs` (line 90)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

