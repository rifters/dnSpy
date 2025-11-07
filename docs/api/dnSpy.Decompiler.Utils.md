# Namespace `dnSpy.Decompiler.Utils`

## Class `StateMachineHelpers`

**Example**

```csharp
// Access dnSpy.Decompiler.Utils.StateMachineHelpers members directly without instantiation.
dnSpy.Decompiler.Utils.StateMachineHelpers./* member */
```

*Defined in* `dnSpy/dnSpy.Decompiler/Utils/StateMachineHelpers.cs` (line 24)

### Methods

- `public static TypeDef GetStateMachineType(MethodDef method)`
  - Parameters:
    - `MethodDef method`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/Utils/StateMachineHelpers.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Decompiler.Utils.StateMachineHelpers.GetStateMachineType(method: /* MethodDef */);
    ```
- `public static bool TryGetKickoffMethod(MethodDef method, out MethodDef kickoffMethod)`
  - Summary: Gets the state machine kickoff method. It's the original async/iterator method that the compiler moves to the MoveNext method
  - Parameters:
    - `MethodDef method`: A possible state machine MoveNext method
    - `out MethodDef kickoffMethod`: Updated with kickoff method on success
  - Defined in: `dnSpy/dnSpy.Decompiler/Utils/StateMachineHelpers.cs` (line 208)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Decompiler.Utils.StateMachineHelpers.TryGetKickoffMethod(method: /* MethodDef */, kickoffMethod: /* MethodDef */);
    ```

