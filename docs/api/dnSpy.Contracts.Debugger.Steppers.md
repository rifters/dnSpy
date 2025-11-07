# Namespace `dnSpy.Contracts.Debugger.Steppers`

## Struct `DbgStepCompleteEventArgs`

Step complete event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Steppers.DbgStepCompleteEventArgs(thread: /* DbgThread */, error: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 79)

### Constructors

- `public DbgStepCompleteEventArgs(DbgThread thread, string error)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread
    - `string error`: Error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 100)

### Properties

- `public DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public bool HasError => Error != null`
  - Summary: true if there was an error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasError;
    ```
- `public string Error { get; }`
  - Summary: Gets the error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Enum `DbgStepKind`

Step kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Steppers.DbgStepKind and call its members.
var instance = new dnSpy.Contracts.Debugger.Steppers.DbgStepKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepKind.cs` (line 24)

### Members

- `StepInto`: Step into
- `StepOver`: Step over
- `StepOut`: Step out
- `StepIntoProcess`: Step into (only one process executes, the other ones aren't started)
- `StepOverProcess`: Step over (only one process executes, the other ones aren't started)
- `StepOutProcess`: Step out (only one process executes, the other ones aren't started)

## Class `DbgStepper`

Steps into, over or out of a method

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Steppers.DbgStepper and call its members.
var instance = new dnSpy.Contracts.Debugger.Steppers.DbgStepper(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 26)

### Methods

- `public abstract void Cancel()`
  - Summary: Cancels the step
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.Cancel();
    ```
- `public abstract void Close()`
  - Summary: Closes the stepper and cancels
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```
- `public abstract void Step(DbgStepKind step, bool autoClose = false)`
  - Summary: Steps once. This method can be called again once is raised. The method can only be called when its process is paused.
  - Parameters:
    - `DbgStepKind step`: Step kind
    - `bool autoClose` (default: `false`): true to call once is raised
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.Step(step: /* DbgStepKind */, autoClose: /* bool */);
    ```

### Properties

- `public DbgProcess Process => Thread.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public DbgRuntime Runtime => Thread.Runtime`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public abstract bool CanStep { get; }`
  - Summary: true if it's possible to call (eg. process must be paused)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanStep;
    ```
- `public abstract bool IsStepping { get; }`
  - Summary: true if has been called but hasn't been raised yet
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsStepping;
    ```

### Events

- `public abstract event EventHandler<DbgStepCompleteEventArgs> StepComplete`
  - Summary: Raised when the step is complete
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Steppers/DbgStepper.cs` (line 55)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.StepComplete += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

