# Namespace `dnSpy.Contracts.Resources`

## Class `ResourceHelper`

Converts strings to resource strings

**Example**

```csharp
// Access dnSpy.Contracts.Resources.ResourceHelper members directly without instantiation.
dnSpy.Contracts.Resources.ResourceHelper./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Resources/ResourceHelper.cs` (line 38)

### Methods

- `public static string GetString(object obj, string value)`
  - Summary: Converts to a string in the resources if it has been prefixed with "res:"
  - Parameters:
    - `object obj`: Can be any object in the assembly containing the resources or the assembly itself ().
    - `string value`: String
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Resources/ResourceHelper.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Resources.ResourceHelper.GetString(obj: /* object */, value: /* string */);
    ```

