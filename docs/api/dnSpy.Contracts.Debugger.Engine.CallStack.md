# Namespace `dnSpy.Contracts.Debugger.Engine.CallStack`

## Class `DbgEngineStackFrame`

Stack frame implemented by a

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.CallStack.DbgEngineStackFrame and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.CallStack.DbgEngineStackFrame(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackFrame.cs` (line 32)

### Methods

- `public abstract void OnFrameCreated(DbgStackFrame frame)`
  - Summary: Called after the has been created
  - Parameters:
    - `DbgStackFrame frame`: Stack frame
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackFrame.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.OnFrameCreated(frame: /* DbgStackFrame */);
    ```
- `public virtual bool TryFormat(DbgEvaluationContext context, IDbgTextWriter output, DbgStackFrameFormatterOptions options, DbgValueFormatterOptions valueOptions, CultureInfo cultureInfo, CancellationToken cancellationToken)`
  - Summary: Formats the stack frame or returns false
  - Parameters:
    - `DbgEvaluationContext context`: Evaluation context
    - `IDbgTextWriter output`: Output
    - `DbgStackFrameFormatterOptions options`: Stack frame options
    - `DbgValueFormatterOptions valueOptions`: Value option
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackFrame.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.TryFormat(context: /* DbgEvaluationContext */, output: /* IDbgTextWriter */, options: /* DbgStackFrameFormatterOptions */, valueOptions: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */, cancellationToken: /* CancellationToken */);
    ```

### Properties

- `public abstract DbgCodeLocation Location { get; }`
  - Summary: Gets the location or null if none. Can be passed to
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackFrame.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Location;
    ```
- `public abstract DbgModule Module { get; }`
  - Summary: Gets the module or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackFrame.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public abstract DbgStackFrameFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackFrame.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public abstract uint FunctionOffset { get; }`
  - Summary: Gets the offset of the IP relative to the start of the function
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackFrame.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FunctionOffset;
    ```
- `public abstract uint FunctionToken { get; }`
  - Summary: Gets the function token or if it doesn't have a token.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackFrame.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FunctionToken;
    ```

### Fields

- `public const uint InvalidFunctionToken = uint.MaxValue`
  - Summary: Invalid function token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackFrame.cs` (line 61)
  - Example:
    ```csharp
    var value = instance.InvalidFunctionToken;
    ```

## Class `DbgEngineStackWalker`

Creates s

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.CallStack.DbgEngineStackWalker and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.CallStack.DbgEngineStackWalker(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackWalker.cs` (line 24)

### Methods

- `public abstract DbgEngineStackFrame[] GetNextStackFrames(int maxFrames)`
  - Summary: Gets the next frames or an empty list if there are no more frames
  - Parameters:
    - `int maxFrames`: Max number of frames to return
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/CallStack/DbgEngineStackWalker.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNextStackFrames(maxFrames: /* int */);
    ```

