# Namespace `ConvertToNetstandardReferences`

## Class `ConvertToNetstandardReferences`

**Inherits/Implements:** `Task`

**Example**

```csharp
// Instantiate ConvertToNetstandardReferences.ConvertToNetstandardReferences and call its members.
var instance = new ConvertToNetstandardReferences.ConvertToNetstandardReferences(/* arguments */);
```

*Defined in* `Build/ConvertToNetstandardReferences/ConvertToNetstandardReferences.cs` (line 30)

### Methods

- `public override bool Execute()`
  - Defined in: `Build/ConvertToNetstandardReferences/ConvertToNetstandardReferences.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute();
    ```

### Properties

- `public ITaskItem[] OutputReferencePath { get; private set; }`
  - Defined in: `Build/ConvertToNetstandardReferences/ConvertToNetstandardReferences.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OutputReferencePath;
    ```
- `public ITaskItem[] ReferencePath { get; set; }`
  - Defined in: `Build/ConvertToNetstandardReferences/ConvertToNetstandardReferences.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReferencePath;
    ```
- `public string DestinationDirectory { get; set; }`
  - Defined in: `Build/ConvertToNetstandardReferences/ConvertToNetstandardReferences.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DestinationDirectory;
    ```

