# Namespace `dnSpy.Contracts.Debugger.Engine.Evaluation.Internal`

## Interface `IPredefinedEvaluationErrorMessagesHelper`

Converts values to localized strings

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.Internal.IPredefinedEvaluationErrorMessagesHelper and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.Internal.IPredefinedEvaluationErrorMessagesHelper(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 97)

### Methods

- `string GetErrorMessage(string error)`
  - Summary: Gets a message
  - Parameters:
    - `string error`: An error message (eg. one in )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.GetErrorMessage(error: /* string */);
    ```

