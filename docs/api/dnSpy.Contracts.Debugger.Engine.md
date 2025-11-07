# Namespace `dnSpy.Contracts.Debugger.Engine`

## Struct `DbgBoundCodeBreakpointInfo<T>`

Bound breakpoint info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgBoundCodeBreakpointInfo<T>(location: /* DbgCodeLocation */, module: /* DbgModule */, address: /* ulong */, message: /* DbgEngineBoundCodeBreakpointMessage */, data: /* T */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 243)

### Constructors

- `public DbgBoundCodeBreakpointInfo(DbgCodeLocation location, DbgModule module, ulong address, DbgEngineBoundCodeBreakpointMessage message, T data)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeLocation location`: Location
    - `DbgModule module`: Module or null if none
    - `ulong address`: Address or if it's not known
    - `DbgEngineBoundCodeBreakpointMessage message`: Warning/error message or null if none
    - `T data`: Data to add to the or null if nothing gets added. If the data implements , it gets disposed when the bound breakpoint gets deleted.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 284)

### Properties

- `public DbgCodeLocation Location { get; }`
  - Summary: Gets the location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 252)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Location;
    ```
- `public DbgEngineBoundCodeBreakpointMessage Message { get; }`
  - Summary: Gets the warning/error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 267)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```
- `public DbgModule Module { get; }`
  - Summary: Gets the module or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 257)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public T Data { get; }`
  - Summary: Gets the data to add to the or null if nothing gets added. If the data implements , it gets disposed when the bound breakpoint gets deleted.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 273)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```
- `public ulong Address { get; }`
  - Summary: Gets the address or if it's not known
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 262)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```

### Fields

- `public const ulong NoAddress = DbgObjectFactory.BoundBreakpointNoAddress`
  - Summary: Value used when the bound breakpoint's address isn't known
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 247)
  - Example:
    ```csharp
    var value = instance.NoAddress;
    ```

## Class `DbgEngine`

A debug engine contains all the logic to control the debugged process

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngine and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngine(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 30)

### Methods

- `public abstract DbgEngineStackWalker CreateStackWalker(DbgThread thread)`
  - Summary: Creates a stack walker
  - Parameters:
    - `DbgThread thread`: Thread created by this engine
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateStackWalker(thread: /* DbgThread */);
    ```
- `public abstract DbgEngineStepper CreateStepper(DbgThread thread)`
  - Summary: Creates a stepper
  - Parameters:
    - `DbgThread thread`: Thread to step
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 164)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateStepper(thread: /* DbgThread */);
    ```
- `public abstract DbgInternalRuntime CreateInternalRuntime(DbgRuntime runtime)`
  - Summary: Creates a instance. It's called by the runtime constructor.
  - Parameters:
    - `DbgRuntime runtime`: Runtime instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInternalRuntime(runtime: /* DbgRuntime */);
    ```
- `public abstract bool CanSetIP(DbgThread thread, DbgCodeLocation location)`
  - Summary: Checks if can be called
  - Parameters:
    - `DbgThread thread`: Thread
    - `DbgCodeLocation location`: New location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 179)
  - Example:
    ```csharp
    // Example invocation
    instance.CanSetIP(thread: /* DbgThread */, location: /* DbgCodeLocation */);
    ```
- `public abstract void AddBreakpoints(DbgModule[] modules, DbgCodeLocation[] locations, bool includeNonModuleBreakpoints)`
  - Summary: Adds all breakpoints. To get notified when a bound breakpoint gets deleted, add custom data that implements when creating the bound breakpoint, see eg.
  - Parameters:
    - `DbgModule[] modules`: Modules
    - `DbgCodeLocation[] locations`: Breakpoint locations. The engine can ignore non-supported locations.
    - `bool includeNonModuleBreakpoints`: If false, add breakpoints that exist in , and if true, add breakpoints that exist in and all breakpoints not in a
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 150)
  - Example:
    ```csharp
    // Example invocation
    instance.AddBreakpoints(modules: /* DbgModule[] */, locations: /* DbgCodeLocation[] */, includeNonModuleBreakpoints: /* bool */);
    ```
- `public abstract void Break()`
  - Summary: Pauses the debugged program, if it's not already paused. This is an asynchronous method. Once the program is paused (even if it already was paused), message must be sent.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.Break();
    ```
- `public abstract void Detach()`
  - Summary: Detaches from the debugged program. If it's not possible, the program must be terminated. This is an asynchronous method. This method gets called when the user chooses Detach All from the Debug menu. When the program has been terminated or detached, message must be sent.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.Detach();
    ```
- `public abstract void Freeze(DbgThread thread)`
  - Summary: Freezes the thread
  - Parameters:
    - `DbgThread thread`: Thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 123)
  - Example:
    ```csharp
    // Example invocation
    instance.Freeze(thread: /* DbgThread */);
    ```
- `public abstract void OnConnected(DbgObjectFactory objectFactory, DbgRuntime runtime)`
  - Summary: Called when its connected message has been received by
  - Parameters:
    - `DbgObjectFactory objectFactory`: Object factory
    - `DbgRuntime runtime`: Runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.OnConnected(objectFactory: /* DbgObjectFactory */, runtime: /* DbgRuntime */);
    ```
- `public abstract void RemoveBreakpoints(DbgModule[] modules, DbgBoundCodeBreakpoint[] boundBreakpoints, bool includeNonModuleBreakpoints)`
  - Summary: Removes all breakpoints. There's no guarantee that this method will be called to delete all bound breakpoints. To always get notified when a bound breakpoint gets deleted, add custom data that implements when creating the bound breakpoint, see eg.
  - Parameters:
    - `DbgModule[] modules`: Modules
    - `DbgBoundCodeBreakpoint[] boundBreakpoints`: Bound breakpoints
    - `bool includeNonModuleBreakpoints`: If false, remove breakpoints that exist in , and if true, remove breakpoints that exist in and all breakpoints not in a
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveBreakpoints(modules: /* DbgModule[] */, boundBreakpoints: /* DbgBoundCodeBreakpoint[] */, includeNonModuleBreakpoints: /* bool */);
    ```
- `public abstract void Run()`
  - Summary: Lets the program run again. This is an asynchronous method. No message is sent.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.Run();
    ```
- `public abstract void SetIP(DbgThread thread, DbgCodeLocation location)`
  - Summary: Sets a new instruction pointer
  - Parameters:
    - `DbgThread thread`: Thread
    - `DbgCodeLocation location`: New location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 171)
  - Example:
    ```csharp
    // Example invocation
    instance.SetIP(thread: /* DbgThread */, location: /* DbgCodeLocation */);
    ```
- `public abstract void Start(DebugProgramOptions options)`
  - Summary: Called when the engine can start or attach to the debugged process. This method is called shortly after this instance gets created by a call to . It must send a message when it has connected to the program or if it failed.
  - Parameters:
    - `DebugProgramOptions options`: Same options that were passed to
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.Start(options: /* DebugProgramOptions */);
    ```
- `public abstract void Terminate()`
  - Summary: Terminates the debugged program. This is an asynchronous method. This method gets called when the user chooses Terminate All from the Debug menu When the program has been terminated or detached, message must be sent.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.Terminate();
    ```
- `public abstract void Thaw(DbgThread thread)`
  - Summary: Thaws the thread
  - Parameters:
    - `DbgThread thread`: Thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 129)
  - Example:
    ```csharp
    // Example invocation
    instance.Thaw(thread: /* DbgThread */);
    ```

### Properties

- `public abstract DbgEngineRuntimeInfo RuntimeInfo { get; }`
  - Summary: Contains properties used to create a . This property is called after the engine has connected and just before the instance is created.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeInfo;
    ```
- `public abstract DbgStartKind StartKind { get; }`
  - Summary: How was the debugged process started?
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StartKind;
    ```
- `public abstract bool CanDetach { get; }`
  - Summary: true if the engine can detach from the debugged program without terminating it.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanDetach;
    ```
- `public abstract string[] DebugTags { get; }`
  - Summary: Gets all debug tags, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DebugTags;
    ```
- `public abstract string[] Debugging { get; }`
  - Summary: What is being debugged. This is shown in the UI (eg. Processes window)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Debugging;
    ```

### Events

- `public abstract event EventHandler<DbgEngineMessage> Message`
  - Summary: Raised when there's a new message. It can be raised in any thread.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 65)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Message += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DbgEngineAppDomain`

A class that can update a

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineAppDomain and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineAppDomain(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineAppDomain.cs` (line 26)

### Methods

- `public abstract void Remove(DbgEngineMessageFlags messageFlags)`
  - Summary: Removes the app domain and disposes of it. The engine has paused the program.
  - Parameters:
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineAppDomain.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(messageFlags: /* DbgEngineMessageFlags */);
    ```
- `public abstract void Update(UpdateOptions options, string name = null, int id = 0)`
  - Summary: Updates properties
  - Parameters:
    - `UpdateOptions options`: Options
    - `string name` (default: `null`): New value
    - `int id` (default: `0`): New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineAppDomain.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Update(options: /* UpdateOptions */, name: /* string */, id: /* int */);
    ```
- `public void UpdateId(int id)`
  - Summary: Updates
  - Parameters:
    - `int id`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineAppDomain.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateId(id: /* int */);
    ```
- `public void UpdateName(string name)`
  - Summary: Updates
  - Parameters:
    - `string name`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineAppDomain.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateName(name: /* string */);
    ```

### Properties

- `public abstract DbgAppDomain AppDomain { get; }`
  - Summary: Gets the app domain
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineAppDomain.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```

## Enum `UpdateOptions`

Properties to update

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineAppDomain.UpdateOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineAppDomain.UpdateOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineAppDomain.cs` (line 41)

### Members

- `None`: No option is enabled
- `Name` = `x00000001`: Update
- `Id` = `x00000002`: Update

## Class `DbgEngineBoundCodeBreakpoint`

A class that can update a

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpoint and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpoint(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 27)

### Methods

- `public abstract void Remove()`
  - Summary: Removes this bound breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove();
    ```
- `public abstract void Remove(DbgEngineBoundCodeBreakpoint[] breakpoints)`
  - Summary: Removes bound breakpoints
  - Parameters:
    - `DbgEngineBoundCodeBreakpoint[] breakpoints`: Breakpoints to remove
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(breakpoints: /* DbgEngineBoundCodeBreakpoint[] */);
    ```
- `public abstract void Update(UpdateOptions options, DbgModule module = null, ulong address = 0, DbgEngineBoundCodeBreakpointMessage message = default)`
  - Summary: Updates properties
  - Parameters:
    - `UpdateOptions options`: Options
    - `DbgModule module` (default: `null`): New value
    - `ulong address` (default: `0`): New value
    - `DbgEngineBoundCodeBreakpointMessage message` (default: `default`): New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.Update(options: /* UpdateOptions */, module: /* DbgModule */, address: /* ulong */, message: /* DbgEngineBoundCodeBreakpointMessage */);
    ```
- `public void UpdateAddress(ulong address)`
  - Summary: Updates
  - Parameters:
    - `ulong address`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateAddress(address: /* ulong */);
    ```
- `public void UpdateMessage(DbgEngineBoundCodeBreakpointMessage message)`
  - Summary: Updates
  - Parameters:
    - `DbgEngineBoundCodeBreakpointMessage message`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateMessage(message: /* DbgEngineBoundCodeBreakpointMessage */);
    ```
- `public void UpdateModule(DbgModule module)`
  - Summary: Updates
  - Parameters:
    - `DbgModule module`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateModule(module: /* DbgModule */);
    ```

### Properties

- `public abstract DbgBoundCodeBreakpoint BoundCodeBreakpoint { get; }`
  - Summary: Gets the bound breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BoundCodeBreakpoint;
    ```

## Enum `UpdateOptions`

Properties to update

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpoint.UpdateOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpoint.UpdateOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 47)

### Members

- `None`: No option is enabled
- `Module` = `x00000001`: Update
- `Address` = `x00000002`: Update
- `Message` = `x00000004`: Update

## Struct `DbgEngineBoundCodeBreakpointMessage`

Bound breakpoint message

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpointMessage and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpointMessage(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 131)

### Methods

- `public static DbgEngineBoundCodeBreakpointMessage CreateCouldNotCreateBreakpoint()`
  - Summary: Creates a could-not-create-breakpoint message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpointMessage.CreateCouldNotCreateBreakpoint();
    ```
- `public static DbgEngineBoundCodeBreakpointMessage CreateCustomError(string message)`
  - Summary: Creates a custom error message
  - Parameters:
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 167)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpointMessage.CreateCustomError(message: /* string */);
    ```
- `public static DbgEngineBoundCodeBreakpointMessage CreateCustomWarning(string message)`
  - Summary: Creates a custom warning message
  - Parameters:
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 159)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpointMessage.CreateCustomWarning(message: /* string */);
    ```
- `public static DbgEngineBoundCodeBreakpointMessage CreateFunctionNotFound(string function)`
  - Summary: Creates a function-not-found message
  - Parameters:
    - `string function`: Name of function
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpointMessage.CreateFunctionNotFound(function: /* string */);
    ```
- `public static DbgEngineBoundCodeBreakpointMessage CreateNoError()`
  - Summary: Creates a no-error message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 151)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpointMessage.CreateNoError();
    ```

### Properties

- `public DbgEngineBoundCodeBreakpointMessageKind Kind { get; }`
  - Summary: Message kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 135)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public string[] Arguments { get; }`
  - Summary: Arguments
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 140)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Arguments;
    ```

## Enum `DbgEngineBoundCodeBreakpointMessageKind`

Bound breakpoint message kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpointMessageKind and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineBoundCodeBreakpointMessageKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineBoundCodeBreakpoint.cs` (line 101)

### Members

- `None`: No warning or error, the breakpoint will break when hit
- `CustomWarning`: Custom warning message
- `CustomError`: Custom error message
- `FunctionNotFound`: Function wasn't found
- `CouldNotCreateBreakpoint`: A breakpoint could not be created

## Class `DbgEngineMessage`

Base class of messages created by a

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineMessage(messageFlags: /* DbgEngineMessageFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 27)

### Constructors

- `protected DbgEngineMessage(DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 42)

### Properties

- `public DbgEngineMessageFlags MessageFlags { get; }`
  - Summary: Gets the message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageFlags;
    ```
- `public abstract DbgEngineMessageKind MessageKind { get; }`
  - Summary: Gets the message kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```

## Enum `DbgEngineMessageFlags`

Message flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineMessageFlags and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineMessageFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessageFlags.cs` (line 26)

### Members

- `None`: No bit is set
- `Pause` = `x00000001`: Set if the process should be paused, false if other code gets to decide if it should pause
- `Continue` = `x00000002`: Set if the process should continue if possible, eg. it's a func-eval and an event occured.
- `Running` = `x00000004`: Set if the process is running

## Enum `DbgEngineMessageKind`

kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineMessageKind and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineMessageKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessageKind.cs` (line 24)

### Members

- `Connected`: The engine has connected to the debugged process. This message is the first message sent by the , even on failure. If the connection was successful, the program must be paused until gets called.
- `Disconnected`: The engine has been disconnected from the debugged process
- `Break`: The debugged executable is paused due to a call to or due to some other engine event.
- `EntryPointBreak`: Entry point has been reached. The engine has paused the program. This message is only sent if the user chose to break at the entry point.
- `ProgramMessage`: Log message written by the debugged program. The engine has paused the program.
- `Breakpoint`: A breakpoint has been hit. The engine has paused the program.
- `ProgramBreak`: The program paused itself by executing a break instruction or method
- `SetIPComplete`: SetIP() is complete
- `AsyncProgramMessage`: Message written by the debugged program. The program is still running. This message is sent when a GUI app writes to the console.

## Class `DbgEngineModule`

A class that can update a

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineModule and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineModule(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 26)

### Methods

- `public abstract void Remove(DbgEngineMessageFlags messageFlags)`
  - Summary: Removes the module and disposes of it. The engine has paused the program.
  - Parameters:
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(messageFlags: /* DbgEngineMessageFlags */);
    ```
- `public abstract void Update(UpdateOptions options, bool isExe = false, ulong address = 0, uint size = 0, DbgImageLayout imageLayout = 0, string name = null, string filename = null, bool isDynamic = false, bool isInMemory = false, bool? isOptimized = null, int order = 0, DateTime? timestamp = null, string version = null)`
  - Summary: Updates properties
  - Parameters:
    - `UpdateOptions options`: Options
    - `bool isExe` (default: `false`): New value
    - `ulong address` (default: `0`): New value
    - `uint size` (default: `0`): New value
    - `DbgImageLayout imageLayout` (default: `0`): New value
    - `string name` (default: `null`): New value
    - `string filename` (default: `null`): New value
    - `bool isDynamic` (default: `false`): New value
    - `bool isInMemory` (default: `false`): New value
    - `bool? isOptimized` (default: `null`): New value
    - `int order` (default: `0`): New value
    - `DateTime? timestamp` (default: `null`): New value
    - `string version` (default: `null`): New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 197)
  - Example:
    ```csharp
    // Example invocation
    instance.Update(options: /* UpdateOptions */, isExe: /* bool */, address: /* ulong */, size: /* uint */, imageLayout: /* DbgImageLayout */, name: /* string */, filename: /* string */, isDynamic: /* bool */, isInMemory: /* bool */, isOptimized: /* bool? */, order: /* int */, timestamp: /* DateTime? */, version: /* string */);
    ```
- `public void UpdateAddress(ulong address)`
  - Summary: Updates
  - Parameters:
    - `ulong address`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 119)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateAddress(address: /* ulong */);
    ```
- `public void UpdateFilename(string filename)`
  - Summary: Updates
  - Parameters:
    - `string filename`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateFilename(filename: /* string */);
    ```
- `public void UpdateImageLayout(DbgImageLayout imageLayout)`
  - Summary: Updates
  - Parameters:
    - `DbgImageLayout imageLayout`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 131)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateImageLayout(imageLayout: /* DbgImageLayout */);
    ```
- `public void UpdateIsDynamic(bool isDynamic)`
  - Summary: Updates
  - Parameters:
    - `bool isDynamic`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 149)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateIsDynamic(isDynamic: /* bool */);
    ```
- `public void UpdateIsExe(bool isExe)`
  - Summary: Updates
  - Parameters:
    - `bool isExe`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateIsExe(isExe: /* bool */);
    ```
- `public void UpdateIsInMemory(bool isInMemory)`
  - Summary: Updates
  - Parameters:
    - `bool isInMemory`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 155)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateIsInMemory(isInMemory: /* bool */);
    ```
- `public void UpdateIsOptimized(bool? isOptimized)`
  - Summary: Updates
  - Parameters:
    - `bool? isOptimized`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 161)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateIsOptimized(isOptimized: /* bool? */);
    ```
- `public void UpdateName(string name)`
  - Summary: Updates
  - Parameters:
    - `string name`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 137)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateName(name: /* string */);
    ```
- `public void UpdateOrder(int order)`
  - Summary: Updates
  - Parameters:
    - `int order`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 167)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateOrder(order: /* int */);
    ```
- `public void UpdateSize(uint size)`
  - Summary: Updates
  - Parameters:
    - `uint size`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateSize(size: /* uint */);
    ```
- `public void UpdateTimestamp(DateTime? timestamp)`
  - Summary: Updates
  - Parameters:
    - `DateTime? timestamp`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 173)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateTimestamp(timestamp: /* DateTime? */);
    ```
- `public void UpdateVersion(string version)`
  - Summary: Updates
  - Parameters:
    - `string version`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 179)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateVersion(version: /* string */);
    ```

### Properties

- `public abstract DbgModule Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```

## Enum `UpdateOptions`

Properties to update

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineModule.UpdateOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineModule.UpdateOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineModule.cs` (line 41)

### Members

- `None`: No option is enabled
- `IsExe` = `x00000001`: Update
- `Address` = `x00000002`: Update
- `Size` = `x00000004`: Update
- `ImageLayout` = `x00000008`: Update
- `Name` = `x00000010`: Update
- `Filename` = `x00000020`: Update
- `IsDynamic` = `x00000040`: Update
- `IsInMemory` = `x00000080`: Update
- `IsOptimized` = `x00000100`: Update
- `Order` = `x00000200`: Update
- `Timestamp` = `x00000400`: Update
- `Version` = `x00000800`: Update

## Class `DbgEngineProvider`

Creates instances. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineProvider.cs` (line 28)

### Methods

- `public abstract DbgEngine Create(DbgManager dbgManager, DebugProgramOptions options)`
  - Summary: Creates a or returns null if is unsupported
  - Parameters:
    - `DbgManager dbgManager`: Debug manager
    - `DebugProgramOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(dbgManager: /* DbgManager */, options: /* DebugProgramOptions */);
    ```

## Class `DbgEngineRuntimeInfo`

Created by a

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineRuntimeInfo(guid: /* Guid */, runtimeKindGuid: /* Guid */, name: /* string */, id: /* RuntimeId */, tags: /* ReadOnlyCollection<string> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineRuntimeInfo.cs` (line 27)

### Constructors

- `public DbgEngineRuntimeInfo(Guid guid, Guid runtimeKindGuid, string name, RuntimeId id, ReadOnlyCollection<string> tags)`
  - Summary: Constructor
  - Parameters:
    - `Guid guid`: GUID returned by
    - `Guid runtimeKindGuid`: GUID returned by
    - `string name`: Name returned by
    - `RuntimeId id`: Id returned by
    - `ReadOnlyCollection<string> tags`: Tags returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineRuntimeInfo.cs` (line 61)

### Properties

- `public Guid Guid { get; }`
  - Summary: GUID returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineRuntimeInfo.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public Guid RuntimeKindGuid { get; }`
  - Summary: GUID returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineRuntimeInfo.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeKindGuid;
    ```
- `public ReadOnlyCollection<string> Tags { get; }`
  - Summary: Tags returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineRuntimeInfo.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tags;
    ```
- `public RuntimeId Id { get; }`
  - Summary: Id returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineRuntimeInfo.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public string Name { get; }`
  - Summary: Name returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineRuntimeInfo.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `DbgEngineThread`

A class that can update a

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineThread and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineThread(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 27)

### Methods

- `public abstract void Remove(DbgEngineMessageFlags messageFlags)`
  - Summary: Removes the thread and disposes of it. The engine has paused the program.
  - Parameters:
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(messageFlags: /* DbgEngineMessageFlags */);
    ```
- `public abstract void Update(UpdateOptions options, DbgAppDomain appDomain = null, string kind = null, ulong id = 0, ulong? managedId = null, string name = null, int suspendedCount = 0, ReadOnlyCollection<DbgStateInfo> state = null)`
  - Summary: Updates properties
  - Parameters:
    - `UpdateOptions options`: Options
    - `DbgAppDomain appDomain` (default: `null`): New value
    - `string kind` (default: `null`): New value
    - `ulong id` (default: `0`): New value
    - `ulong? managedId` (default: `null`): New value
    - `string name` (default: `null`): New value
    - `int suspendedCount` (default: `0`): New value
    - `ReadOnlyCollection<DbgStateInfo> state` (default: `null`): New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 138)
  - Example:
    ```csharp
    // Example invocation
    instance.Update(options: /* UpdateOptions */, appDomain: /* DbgAppDomain */, kind: /* string */, id: /* ulong */, managedId: /* ulong? */, name: /* string */, suspendedCount: /* int */, state: /* ReadOnlyCollection<DbgStateInfo> */);
    ```
- `public void UpdateAppDomain(DbgAppDomain appDomain)`
  - Summary: Updates
  - Parameters:
    - `DbgAppDomain appDomain`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateAppDomain(appDomain: /* DbgAppDomain */);
    ```
- `public void UpdateId(ulong id)`
  - Summary: Updates
  - Parameters:
    - `ulong id`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateId(id: /* ulong */);
    ```
- `public void UpdateKind(string kind)`
  - Summary: Updates
  - Parameters:
    - `string kind`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateKind(kind: /* string */);
    ```
- `public void UpdateManagedId(ulong? managedId)`
  - Summary: Updates
  - Parameters:
    - `ulong? managedId`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 107)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateManagedId(managedId: /* ulong? */);
    ```
- `public void UpdateName(string name)`
  - Summary: Updates
  - Parameters:
    - `string name`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateName(name: /* string */);
    ```
- `public void UpdateState(ReadOnlyCollection<DbgStateInfo> state)`
  - Summary: Updates
  - Parameters:
    - `ReadOnlyCollection<DbgStateInfo> state`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateState(state: /* ReadOnlyCollection<DbgStateInfo> */);
    ```
- `public void UpdateSuspendedCount(int suspendedCount)`
  - Summary: Updates
  - Parameters:
    - `int suspendedCount`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 119)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateSuspendedCount(suspendedCount: /* int */);
    ```

### Properties

- `public abstract DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```

## Enum `UpdateOptions`

Properties to update

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgEngineThread.UpdateOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgEngineThread.UpdateOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineThread.cs` (line 42)

### Members

- `None`: No option is enabled
- `AppDomain` = `x00000001`: Update
- `Kind` = `x00000002`: Update
- `Id` = `x00000004`: Update
- `ManagedId` = `x00000008`: Update
- `Name` = `x00000010`: Update
- `SuspendedCount` = `x00000020`: Update
- `State` = `x00000040`: Update

## Class `DbgMessageAsyncProgramMessage`

event

**Inherits/Implements:** `DbgEngineMessage`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgMessageAsyncProgramMessage(source: /* AsyncProgramMessageSource */, message: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 289)

### Constructors

- `public DbgMessageAsyncProgramMessage(AsyncProgramMessageSource source, string message)`
  - Summary: Constructor
  - Parameters:
    - `AsyncProgramMessageSource source`: Source
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 310)

### Properties

- `public AsyncProgramMessageSource Source { get; }`
  - Summary: Gets the message source
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 298)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Source;
    ```
- `public override DbgEngineMessageKind MessageKind => DbgEngineMessageKind.AsyncProgramMessage`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 293)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```
- `public string Message { get; }`
  - Summary: Gets the message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 303)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```

## Class `DbgMessageBreak`

event

**Inherits/Implements:** `DbgEngineMessage`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgMessageBreak(thread: /* DbgThread */, messageFlags: /* DbgEngineMessageFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 107)

### Constructors

- `public DbgMessageBreak(DbgThread thread, DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread or null if it's not known
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 128)
- `public DbgMessageBreak(string errorMessage, DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `string errorMessage`: Error message
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 135)

### Properties

- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if it's not known
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 121)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public override DbgEngineMessageKind MessageKind => DbgEngineMessageKind.Break`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```
- `public string ErrorMessage { get; }`
  - Summary: The error message or null if there's no error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ErrorMessage;
    ```

## Class `DbgMessageBreakpoint`

event

**Inherits/Implements:** `DbgEngineMessage`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgMessageBreakpoint(boundBreakpoint: /* DbgBoundCodeBreakpoint */, thread: /* DbgThread */, messageFlags: /* DbgEngineMessageFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 195)

### Constructors

- `public DbgMessageBreakpoint(DbgBoundCodeBreakpoint boundBreakpoint, DbgThread thread, DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `DbgBoundCodeBreakpoint boundBreakpoint`: Breakpoint
    - `DbgThread thread`: Thread or null if it's not known
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 217)

### Properties

- `public DbgBoundCodeBreakpoint BoundBreakpoint { get; }`
  - Summary: Gets the breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 204)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BoundBreakpoint;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if it's not known
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 209)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public override DbgEngineMessageKind MessageKind => DbgEngineMessageKind.Breakpoint`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 199)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```

## Class `DbgMessageConnected`

event. Should be the first event sent by the debug engine. If it couldn't connect, no more messages need to be sent after this message is sent.

**Inherits/Implements:** `DbgEngineMessage`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgMessageConnected(processId: /* int */, messageFlags: /* DbgEngineMessageFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 50)

### Constructors

- `public DbgMessageConnected(int processId, DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `int processId`: Process id
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 71)
- `public DbgMessageConnected(string errorMessage, DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `string errorMessage`: Error message
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 78)

### Properties

- `public int ProcessId { get; }`
  - Summary: Gets the process id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessId;
    ```
- `public override DbgEngineMessageKind MessageKind => DbgEngineMessageKind.Connected`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```
- `public string ErrorMessage { get; }`
  - Summary: The error message or null if there's no error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ErrorMessage;
    ```

## Class `DbgMessageDisconnected`

event

**Inherits/Implements:** `DbgEngineMessage`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgMessageDisconnected(exitCode: /* int */, messageFlags: /* DbgEngineMessageFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 85)

### Constructors

- `public DbgMessageDisconnected(int exitCode, DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `int exitCode`: Exit code
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 101)

### Properties

- `public int ExitCode { get; }`
  - Summary: Gets the exit code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExitCode;
    ```
- `public override DbgEngineMessageKind MessageKind => DbgEngineMessageKind.Disconnected`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 89)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```

## Class `DbgMessageEntryPointBreak`

event

**Inherits/Implements:** `DbgEngineMessage`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgMessageEntryPointBreak(thread: /* DbgThread */, messageFlags: /* DbgEngineMessageFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 141)

### Constructors

- `public DbgMessageEntryPointBreak(DbgThread thread, DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread or null if it's not known
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 157)

### Properties

- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if it's not known
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 150)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public override DbgEngineMessageKind MessageKind => DbgEngineMessageKind.EntryPointBreak`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 145)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```

## Class `DbgMessageProgramBreak`

event

**Inherits/Implements:** `DbgEngineMessage`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgMessageProgramBreak(thread: /* DbgThread */, messageFlags: /* DbgEngineMessageFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 227)

### Constructors

- `public DbgMessageProgramBreak(DbgThread thread, DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread or null if it's not known
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 243)

### Properties

- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if it's not known
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 236)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public override DbgEngineMessageKind MessageKind => DbgEngineMessageKind.ProgramBreak`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 231)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```

## Class `DbgMessageProgramMessage`

event

**Inherits/Implements:** `DbgEngineMessage`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgMessageProgramMessage(message: /* string */, thread: /* DbgThread */, messageFlags: /* DbgEngineMessageFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 163)

### Constructors

- `public DbgMessageProgramMessage(string message, DbgThread thread, DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
    - `DbgThread thread`: Thread or null if it's not known
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 185)

### Properties

- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if it's not known
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 177)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public override DbgEngineMessageKind MessageKind => DbgEngineMessageKind.ProgramMessage`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 167)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```
- `public string Message { get; }`
  - Summary: Gets the message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 172)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```

## Class `DbgMessageSetIPComplete`

event

**Inherits/Implements:** `DbgEngineMessage`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.DbgMessageSetIPComplete(thread: /* DbgThread */, framesInvalidated: /* bool */, error: /* string */, messageFlags: /* DbgEngineMessageFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 250)

### Constructors

- `public DbgMessageSetIPComplete(DbgThread thread, bool framesInvalidated, string error, DbgEngineMessageFlags messageFlags)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread or null if it's not known
    - `bool framesInvalidated`: true if all frames in the thread have been invalidated
    - `string error`: Error string or null if none
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 278)

### Properties

- `public DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 259)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public bool FramesInvalidated { get; }`
  - Summary: true if all frames in the thread have been invalidated
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 264)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FramesInvalidated;
    ```
- `public override DbgEngineMessageKind MessageKind => DbgEngineMessageKind.SetIPComplete`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 254)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```
- `public string Error { get; }`
  - Summary: Gets the error string or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineMessage.cs` (line 269)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Class `DbgObjectFactory`

Used by a to create new modules, threads, etc.

The engines don't need to worry about locks, or raising events in the correct thread, or updating collections in the right thread, or closing dbg objects, etc... It's taken care of by dnSpy.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgObjectFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgObjectFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 37)

### Methods

- `public DbgEngineAppDomain CreateAppDomain(DbgInternalAppDomain internalAppDomain, string name, int id, DbgEngineMessageFlags messageFlags)`
  - Summary: Creates an app domain. The engine has paused the program.
  - Parameters:
    - `DbgInternalAppDomain internalAppDomain`: App domain object created by the debug engine
    - `string name`: New value
    - `int id`: New value
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAppDomain(internalAppDomain: /* DbgInternalAppDomain */, name: /* string */, id: /* int */, messageFlags: /* DbgEngineMessageFlags */);
    ```
- `public DbgEngineBoundCodeBreakpoint Create(DbgCodeLocation location, DbgModule module, ulong address, DbgEngineBoundCodeBreakpointMessage message)`
  - Summary: Creates a bound breakpoint. This method returns null if there was no breakpoint matching . To get notified when a bound breakpoint gets deleted, add custom data that implements .
  - Parameters:
    - `DbgCodeLocation location`: Breakpoint location
    - `DbgModule module`: Module or null if none
    - `ulong address`: Address or if unknown
    - `DbgEngineBoundCodeBreakpointMessage message`: Warning/error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 198)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(location: /* DbgCodeLocation */, module: /* DbgModule */, address: /* ulong */, message: /* DbgEngineBoundCodeBreakpointMessage */);
    ```
- `public DbgEngineBoundCodeBreakpoint Create<T>(DbgCodeLocation location, DbgModule module, ulong address, DbgEngineBoundCodeBreakpointMessage message, T data) where T : class`
  - Summary: Creates a bound breakpoint. This method returns null if there was no breakpoint matching . To get notified when a bound breakpoint gets deleted, add custom data that implements .
  - Parameters:
    - `DbgCodeLocation location`: Breakpoint location
    - `DbgModule module`: Module or null if none
    - `ulong address`: Address or if unknown
    - `DbgEngineBoundCodeBreakpointMessage message`: Warning/error message or null if none
    - `T data`: Data to add to the or null if nothing gets added
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 213)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(location: /* DbgCodeLocation */, module: /* DbgModule */, address: /* ulong */, message: /* DbgEngineBoundCodeBreakpointMessage */, data: /* T */);
    ```
- `public DbgEngineModule CreateModule(DbgAppDomain appDomain, DbgInternalModule internalModule, bool isExe, ulong address, uint size, DbgImageLayout imageLayout, string name, string filename, bool isDynamic, bool isInMemory, bool? isOptimized, int order, DateTime? timestamp, string version, DbgEngineMessageFlags messageFlags)`
  - Summary: Creates a module. The engine has paused the program.
  - Parameters:
    - `DbgAppDomain appDomain`: New value
    - `DbgInternalModule internalModule`: Module object created by the debug engine
    - `bool isExe`: New value
    - `ulong address`: New value
    - `uint size`: New value
    - `DbgImageLayout imageLayout`: New value
    - `string name`: New value
    - `string filename`: New value
    - `bool isDynamic`: New value
    - `bool isInMemory`: New value
    - `bool? isOptimized`: New value
    - `int order`: New value
    - `DateTime? timestamp`: New value
    - `string version`: New value
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateModule(appDomain: /* DbgAppDomain */, internalModule: /* DbgInternalModule */, isExe: /* bool */, address: /* ulong */, size: /* uint */, imageLayout: /* DbgImageLayout */, name: /* string */, filename: /* string */, isDynamic: /* bool */, isInMemory: /* bool */, isOptimized: /* bool? */, order: /* int */, timestamp: /* DateTime? */, version: /* string */, messageFlags: /* DbgEngineMessageFlags */);
    ```
- `public DbgEngineThread CreateThread(DbgAppDomain appDomain, string kind, ulong id, ulong? managedId, string name, int suspendedCount, ReadOnlyCollection<DbgStateInfo> state, DbgEngineMessageFlags messageFlags)`
  - Summary: Creates a thread. The engine has paused the program.
  - Parameters:
    - `DbgAppDomain appDomain`: New value
    - `string kind`: New value
    - `ulong id`: New value
    - `ulong? managedId`: New value
    - `string name`: New value
    - `int suspendedCount`: New value
    - `ReadOnlyCollection<DbgStateInfo> state`: New value
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateThread(appDomain: /* DbgAppDomain */, kind: /* string */, id: /* ulong */, managedId: /* ulong? */, name: /* string */, suspendedCount: /* int */, state: /* ReadOnlyCollection<DbgStateInfo> */, messageFlags: /* DbgEngineMessageFlags */);
    ```
- `public DbgException CreateException(DbgExceptionId id, DbgExceptionEventFlags flags, string message, DbgThread thread, DbgModule module, DbgEngineMessageFlags messageFlags)`
  - Summary: Creates an exception. The engine has paused the program.
  - Parameters:
    - `DbgExceptionId id`: Exception id
    - `DbgExceptionEventFlags flags`: Exception event flags
    - `string message`: Exception message or null if it's not available
    - `DbgThread thread`: Thread where exception was thrown or null if it's unknown
    - `DbgModule module`: Module where exception was thrown or null if it's unknown
    - `DbgEngineMessageFlags messageFlags`: Message flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 165)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateException(id: /* DbgExceptionId */, flags: /* DbgExceptionEventFlags */, message: /* string */, thread: /* DbgThread */, module: /* DbgModule */, messageFlags: /* DbgEngineMessageFlags */);
    ```
- `public abstract DbgEngineAppDomain CreateAppDomain<T>(DbgInternalAppDomain internalAppDomain, string name, int id, DbgEngineMessageFlags messageFlags, T data, Action<DbgEngineAppDomain> onCreated = null) where T : class`
  - Summary: Creates an app domain. The engine has paused the program.
  - Parameters:
    - `DbgInternalAppDomain internalAppDomain`: App domain object created by the debug engine
    - `string name`: New value
    - `int id`: New value
    - `DbgEngineMessageFlags messageFlags`: Message flags
    - `T data`: Data to add to the or null if nothing gets added
    - `Action<DbgEngineAppDomain> onCreated` (default: `null`): Called right after creating the app domain but before adding it to internal data structures. This can be null.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAppDomain(internalAppDomain: /* DbgInternalAppDomain */, name: /* string */, id: /* int */, messageFlags: /* DbgEngineMessageFlags */, data: /* T */, onCreated: /* Action<DbgEngineAppDomain> */);
    ```
- `public abstract DbgEngineBoundCodeBreakpoint[] Create<T>(DbgBoundCodeBreakpointInfo<T>[] infos) where T : class`
  - Summary: Creates bound breakpoints. Locations that don't match an existing breakpoint are ignored, and all user data are disposed if they implement . To get notified when a bound breakpoint gets deleted, add custom data that implements .
  - Parameters:
    - `DbgBoundCodeBreakpointInfo<T>[] infos`: Bound breakpoints to create
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 225)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(infos: /* DbgBoundCodeBreakpointInfo<T>[] */);
    ```
- `public abstract DbgEngineModule CreateModule<T>(DbgAppDomain appDomain, DbgInternalModule internalModule, bool isExe, ulong address, uint size, DbgImageLayout imageLayout, string name, string filename, bool isDynamic, bool isInMemory, bool? isOptimized, int order, DateTime? timestamp, string version, DbgEngineMessageFlags messageFlags, T data, Action<DbgEngineModule> onCreated = null) where T : class`
  - Summary: Creates a module. The engine has paused the program.
  - Parameters:
    - `DbgAppDomain appDomain`: New value
    - `DbgInternalModule internalModule`: Module object created by the debug engine
    - `bool isExe`: New value
    - `ulong address`: New value
    - `uint size`: New value
    - `DbgImageLayout imageLayout`: New value
    - `string name`: New value
    - `string filename`: New value
    - `bool isDynamic`: New value
    - `bool isInMemory`: New value
    - `bool? isOptimized`: New value
    - `int order`: New value
    - `DateTime? timestamp`: New value
    - `string version`: New value
    - `DbgEngineMessageFlags messageFlags`: Message flags
    - `T data`: Data to add to the or null if nothing gets added
    - `Action<DbgEngineModule> onCreated` (default: `null`): Called right after creating the module but before adding it to internal data structures. This can be null.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateModule(appDomain: /* DbgAppDomain */, internalModule: /* DbgInternalModule */, isExe: /* bool */, address: /* ulong */, size: /* uint */, imageLayout: /* DbgImageLayout */, name: /* string */, filename: /* string */, isDynamic: /* bool */, isInMemory: /* bool */, isOptimized: /* bool? */, order: /* int */, timestamp: /* DateTime? */, version: /* string */, messageFlags: /* DbgEngineMessageFlags */, data: /* T */, onCreated: /* Action<DbgEngineModule> */);
    ```
- `public abstract DbgEngineStackFrame CreateSpecialStackFrame(string name, DbgCodeLocation location = null, DbgModule module = null, uint functionOffset = 0, uint functionToken = DbgEngineStackFrame.InvalidFunctionToken)`
  - Summary: Creates a special stack frame that's displayed as [name], eg. [Managed to Native Transition]
  - Parameters:
    - `string name`: Name, eg. "Managed to Native Transition"
    - `DbgCodeLocation location` (default: `null`): Location or null
    - `DbgModule module` (default: `null`): Module or null
    - `uint functionOffset` (default: `0`): Function offset
    - `uint functionToken` (default: `DbgEngineStackFrame.InvalidFunctionToken`): Function token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 236)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateSpecialStackFrame(name: /* string */, location: /* DbgCodeLocation */, module: /* DbgModule */, functionOffset: /* uint */, functionToken: /* uint */);
    ```
- `public abstract DbgEngineThread CreateThread<T>(DbgAppDomain appDomain, string kind, ulong id, ulong? managedId, string name, int suspendedCount, ReadOnlyCollection<DbgStateInfo> state, DbgEngineMessageFlags messageFlags, T data, Action<DbgEngineThread> onCreated = null) where T : class`
  - Summary: Creates a thread. The engine has paused the program.
  - Parameters:
    - `DbgAppDomain appDomain`: New value
    - `string kind`: New value
    - `ulong id`: New value
    - `ulong? managedId`: New value
    - `string name`: New value
    - `int suspendedCount`: New value
    - `ReadOnlyCollection<DbgStateInfo> state`: New value
    - `DbgEngineMessageFlags messageFlags`: Message flags
    - `T data`: Data to add to the or null if nothing gets added
    - `Action<DbgEngineThread> onCreated` (default: `null`): Called right after creating the thread but before adding it to internal data structures. This can be null.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateThread(appDomain: /* DbgAppDomain */, kind: /* string */, id: /* ulong */, managedId: /* ulong? */, name: /* string */, suspendedCount: /* int */, state: /* ReadOnlyCollection<DbgStateInfo> */, messageFlags: /* DbgEngineMessageFlags */, data: /* T */, onCreated: /* Action<DbgEngineThread> */);
    ```
- `public abstract DbgException CreateException<T>(DbgExceptionId id, DbgExceptionEventFlags flags, string message, DbgThread thread, DbgModule module, DbgEngineMessageFlags messageFlags, T data, Action<DbgException> onCreated = null) where T : class`
  - Summary: Creates an exception. The engine has paused the program.
  - Parameters:
    - `DbgExceptionId id`: Exception id
    - `DbgExceptionEventFlags flags`: Exception event flags
    - `string message`: Exception message or null if it's not available
    - `DbgThread thread`: Thread where exception was thrown or null if it's unknown
    - `DbgModule module`: Module where exception was thrown or null if it's unknown
    - `DbgEngineMessageFlags messageFlags`: Message flags
    - `T data`: Data to add to the or null if nothing gets added
    - `Action<DbgException> onCreated` (default: `null`): Called right after creating the exception but before adding it to internal data structures. This can be null.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateException(id: /* DbgExceptionId */, flags: /* DbgExceptionEventFlags */, message: /* string */, thread: /* DbgThread */, module: /* DbgModule */, messageFlags: /* DbgEngineMessageFlags */, data: /* T */, onCreated: /* Action<DbgException> */);
    ```

### Properties

- `public DbgProcess Process => Runtime.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DbgManager DbgManager { get; }`
  - Summary: Gets the debug manager
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DbgManager;
    ```
- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```

### Fields

- `public const ulong BoundBreakpointNoAddress = ulong.MaxValue`
  - Summary: Value used when the bound breakpoint's address isn't known
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgObjectFactory.cs` (line 186)
  - Example:
    ```csharp
    var value = instance.BoundBreakpointNoAddress;
    ```

## Enum `DbgStartKind`

Start kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.DbgStartKind and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.DbgStartKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngine.cs` (line 185)

### Members

- `Start`: The program was started by the debugger
- `Attach`: The debugger attached to the program after it was started by someone else

## Class `ExportDbgEngineProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgEngineProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.ExportDbgEngineProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineProvider.cs` (line 47)

### Constructors

- `public ExportDbgEngineProviderAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineProvider.cs` (line 53)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineProvider.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDbgEngineProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.IDbgEngineProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.IDbgEngineProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineProvider.cs` (line 39)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/DbgEngineProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

