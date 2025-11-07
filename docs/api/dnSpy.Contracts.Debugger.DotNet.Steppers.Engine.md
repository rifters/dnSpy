# Namespace `dnSpy.Contracts.Debugger.DotNet.Steppers.Engine`

## Class `DbgDotNetEngineStepper`

.NET stepper

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgDotNetEngineStepper and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgDotNetEngineStepper(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 28)

### Methods

- `public abstract DbgDotNetEngineStepperFrameInfo TryGetFrameInfo(DbgThread thread)`
  - Summary: Gets frame info or null if none is available
  - Parameters:
    - `DbgThread thread`: Thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetFrameInfo(thread: /* DbgThread */);
    ```
- `public abstract DbgDotNetStepperBreakpoint CreateBreakpoint(DbgThread thread, DbgModule module, uint token, uint offset)`
  - Summary: Creates a breakpoint
  - Parameters:
    - `DbgThread thread`: Thread or null to match any thread
    - `DbgModule module`: Module
    - `uint token`: Method token
    - `uint offset`: IL offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateBreakpoint(thread: /* DbgThread */, module: /* DbgModule */, token: /* uint */, offset: /* uint */);
    ```
- `public abstract SessionBase CreateSession(object tag)`
  - Summary: Creates a new
  - Parameters:
    - `object tag`: Tag
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateSession(tag: /* object */);
    ```
- `public abstract Task<DbgThread> StepIntoAsync(DbgDotNetEngineStepperFrameInfo frame, DbgCodeRange[] ranges)`
  - Summary: Steps into
  - Parameters:
    - `DbgDotNetEngineStepperFrameInfo frame`: Frame info
    - `DbgCodeRange[] ranges`: Statement ranges
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.StepIntoAsync(frame: /* DbgDotNetEngineStepperFrameInfo */, ranges: /* DbgCodeRange[] */);
    ```
- `public abstract Task<DbgThread> StepOutAsync(DbgDotNetEngineStepperFrameInfo frame)`
  - Summary: Steps out
  - Parameters:
    - `DbgDotNetEngineStepperFrameInfo frame`: Frame info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.StepOutAsync(frame: /* DbgDotNetEngineStepperFrameInfo */);
    ```
- `public abstract Task<DbgThread> StepOverAsync(DbgDotNetEngineStepperFrameInfo frame, DbgCodeRange[] ranges)`
  - Summary: Steps over
  - Parameters:
    - `DbgDotNetEngineStepperFrameInfo frame`: Frame info
    - `DbgCodeRange[] ranges`: Statement ranges
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.StepOverAsync(frame: /* DbgDotNetEngineStepperFrameInfo */, ranges: /* DbgCodeRange[] */);
    ```
- `public abstract bool IgnoreException(Exception exception)`
  - Summary: Returns true if the exception should be ignored eg. because the process has exited
  - Parameters:
    - `Exception exception`: Thrown exception
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 156)
  - Example:
    ```csharp
    // Example invocation
    instance.IgnoreException(exception: /* Exception */);
    ```
- `public abstract void CancelLastStep()`
  - Summary: Cancels last step operation
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 110)
  - Example:
    ```csharp
    // Example invocation
    instance.CancelLastStep();
    ```
- `public abstract void ClearReturnValues()`
  - Summary: Clears all return values
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 122)
  - Example:
    ```csharp
    // Example invocation
    instance.ClearReturnValues();
    ```
- `public abstract void Close(DbgDispatcher dispatcher)`
  - Summary: Cleans up
  - Parameters:
    - `DbgDispatcher dispatcher`: Dispatcher
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 162)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(dispatcher: /* DbgDispatcher */);
    ```
- `public abstract void CollectReturnValues(DbgDotNetEngineStepperFrameInfo frame, DbgILInstruction[][] statementInstructions)`
  - Summary: Prepares collecting return values
  - Parameters:
    - `DbgDotNetEngineStepperFrameInfo frame`: Frame info
    - `DbgILInstruction[][] statementInstructions`: Statement instructions
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.CollectReturnValues(frame: /* DbgDotNetEngineStepperFrameInfo */, statementInstructions: /* DbgILInstruction[][] */);
    ```
- `public abstract void Continue()`
  - Summary: Lets the process run
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.Continue();
    ```
- `public abstract void OnCanceled(SessionBase session)`
  - Summary: Called when it gets canceled
  - Parameters:
    - `SessionBase session`: Session
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 149)
  - Example:
    ```csharp
    // Example invocation
    instance.OnCanceled(session: /* SessionBase */);
    ```
- `public abstract void OnStepComplete()`
  - Summary: Called when the step is complete
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    instance.OnStepComplete();
    ```
- `public abstract void RemoveBreakpoints(DbgDotNetStepperBreakpoint[] breakpoints)`
  - Summary: Removes breakpoints
  - Parameters:
    - `DbgDotNetStepperBreakpoint[] breakpoints`: Breakpoints to remove
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 138)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveBreakpoints(breakpoints: /* DbgDotNetStepperBreakpoint[] */);
    ```

### Properties

- `public abstract SessionBase Session { get; set; }`
  - Summary: Gets/sets the session. It's null if there's no step operation in progress.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Session;
    ```
- `public abstract bool IsRuntimePaused { get; }`
  - Summary: true if the runtime is paused
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRuntimePaused;
    ```
- `public abstract uint ContinueCounter { get; }`
  - Summary: Gets the countinue counter. It's incremented each time the process is continued.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContinueCounter;
    ```

### Fields

- `protected static readonly int maxReturnValues = 100`
  - Summary: Max number of return values to save
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgDotNetEngineStepper.maxReturnValues;
    ```

## Class `SessionBase`

Session

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgDotNetEngineStepper.SessionBase(tag: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 37)

### Constructors

- `protected SessionBase(object tag)`
  - Summary: Constructor
  - Parameters:
    - `object tag`: Tag
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 47)

### Properties

- `public object Tag { get; }`
  - Summary: Gets the tag
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```

## Class `DbgDotNetEngineStepperFrameInfo`

Frame info needed by the stepper

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgDotNetEngineStepperFrameInfo and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgDotNetEngineStepperFrameInfo(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepperFrameInfo.cs` (line 24)

### Methods

- `public abstract bool Equals(DbgDotNetEngineStepperFrameInfo other)`
  - Summary: Checks if this frame is the same as another frame
  - Parameters:
    - `DbgDotNetEngineStepperFrameInfo other`: Other frame
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepperFrameInfo.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgDotNetEngineStepperFrameInfo */);
    ```
- `public abstract bool TryGetLocation(out DbgModule module, out uint token, out uint offset)`
  - Summary: Gets the location
  - Parameters:
    - `out DbgModule module`: Module
    - `out uint token`: Method token
    - `out uint offset`: IL offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepperFrameInfo.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetLocation(module: /* DbgModule */, token: /* uint */, offset: /* uint */);
    ```

### Properties

- `public abstract DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepperFrameInfo.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public abstract bool SupportsReturnValues { get; }`
  - Summary: true if return values are supported
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepperFrameInfo.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SupportsReturnValues;
    ```

## Class `DbgDotNetStepperBreakpoint`

A code breakpoint used by the .NET stepper

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgDotNetStepperBreakpoint and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgDotNetStepperBreakpoint(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 168)

### Events

- `public abstract event EventHandler<DbgDotNetStepperBreakpointEventArgs> Hit`
  - Summary: Raised when the breakpoint is hit
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 172)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Hit += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DbgDotNetStepperBreakpointEventArgs`

Stepper breakpoint event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgDotNetStepperBreakpointEventArgs(thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 178)

### Constructors

- `public DbgDotNetStepperBreakpointEventArgs(DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Current thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 193)

### Properties

- `public DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 182)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public bool Pause { get; set; }`
  - Summary: Set to true by the event handler to pause the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgDotNetEngineStepper.cs` (line 187)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Pause;
    ```

## Class `DbgEngineStepperFactory`

Creates a .NET stepper

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgEngineStepperFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.DbgEngineStepperFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgEngineStepperFactory.cs` (line 27)

### Methods

- `public abstract DbgEngineStepper Create(IDbgDotNetRuntime runtime, DbgDotNetEngineStepper stepper, DbgThread thread)`
  - Summary: Creates a .NET stepper
  - Parameters:
    - `IDbgDotNetRuntime runtime`: Runtime
    - `DbgDotNetEngineStepper stepper`: Stepper
    - `DbgThread thread`: Thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/DbgEngineStepperFactory.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(runtime: /* IDbgDotNetRuntime */, stepper: /* DbgDotNetEngineStepper */, thread: /* DbgThread */);
    ```

## Class `ForciblyCanceledException`

Thrown when the stepper was forcibly canceled

**Inherits/Implements:** `Exception`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.ForciblyCanceledException(message: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/Exceptions.cs` (line 37)

### Constructors

- `public ForciblyCanceledException(string message)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/Exceptions.cs` (line 42)

## Class `StepErrorException`

Thrown when there was an error stepping

**Inherits/Implements:** `Exception`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Steppers.Engine.StepErrorException(message: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/Exceptions.cs` (line 26)

### Constructors

- `public StepErrorException(string message)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Steppers/Engine/Exceptions.cs` (line 31)

