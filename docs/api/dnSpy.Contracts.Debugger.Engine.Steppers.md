# Namespace `dnSpy.Contracts.Debugger.Engine.Steppers`

## Struct `DbgEngineStepCompleteEventArgs`

Step complete event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.Steppers.DbgEngineStepCompleteEventArgs(thread: /* DbgThread */, tag: /* object */, error: /* string */, forciblyCanceled: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepper.cs` (line 50)

### Constructors

- `public DbgEngineStepCompleteEventArgs(DbgThread thread, object tag, string error, bool forciblyCanceled)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread or null to use the default thread that was used to create the stepper
    - `object tag`: Same value that was passed to
    - `string error`: Error message or null if none
    - `bool forciblyCanceled`: true if the stepper was canceled by the engine
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepper.cs` (line 78)

### Properties

- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null to use the default thread that was used to create the stepper
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepper.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public bool ForciblyCanceled { get; }`
  - Summary: true if the stepper was canceled by the engine
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepper.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ForciblyCanceled;
    ```
- `public object Tag { get; }`
  - Summary: Gets the tag
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepper.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```
- `public string Error { get; }`
  - Summary: Gets the error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepper.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Enum `DbgEngineStepKind`

Step kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Steppers.DbgEngineStepKind and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Steppers.DbgEngineStepKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepKind.cs` (line 24)

### Members

- `StepInto`: Step into
- `StepOver`: Step over
- `StepOut`: Step out

## Class `DbgEngineStepper`

Steps into, over or out of a method. When closed, any non-completed call must be canceled.

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Steppers.DbgEngineStepper and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Steppers.DbgEngineStepper(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepper.cs` (line 26)

### Methods

- `public abstract void Cancel(object tag)`
  - Summary: Cancels the step, but does not raise
  - Parameters:
    - `object tag`: Same value that was passed to
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepper.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.Cancel(tag: /* object */);
    ```
- `public abstract void Step(object tag, DbgEngineStepKind step)`
  - Summary: Steps once. This method can be called again once is raised. This method is only called if the engine is paused.
  - Parameters:
    - `object tag`: This value must be used when raising
    - `DbgEngineStepKind step`: Step kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepper.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.Step(tag: /* object */, step: /* DbgEngineStepKind */);
    ```

### Events

- `public abstract event EventHandler<DbgEngineStepCompleteEventArgs> StepComplete`
  - Summary: Raised when the step is complete
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Steppers/DbgEngineStepper.cs` (line 30)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.StepComplete += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

