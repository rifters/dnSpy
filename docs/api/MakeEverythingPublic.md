# Namespace `MakeEverythingPublic`

## Class `MakeEverythingPublic`

**Inherits/Implements:** `Task`

**Example**

```csharp
// Instantiate MakeEverythingPublic.MakeEverythingPublic and call its members.
var instance = new MakeEverythingPublic.MakeEverythingPublic(/* arguments */);
```

*Defined in* `Build/MakeEverythingPublic/MakeEverythingPublic.cs` (line 31)

### Methods

- `public override bool Execute()`
  - Defined in: `Build/MakeEverythingPublic/MakeEverythingPublic.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute();
    ```

### Properties

- `public ITaskItem[] OutputReferencePath { get; private set; }`
  - Defined in: `Build/MakeEverythingPublic/MakeEverythingPublic.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OutputReferencePath;
    ```
- `public ITaskItem[] ReferencePath { get; set; }`
  - Defined in: `Build/MakeEverythingPublic/MakeEverythingPublic.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReferencePath;
    ```
- `public string AssembliesToMakePublic { get; set; }`
  - Defined in: `Build/MakeEverythingPublic/MakeEverythingPublic.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssembliesToMakePublic;
    ```
- `public string DestinationDirectory { get; set; }`
  - Defined in: `Build/MakeEverythingPublic/MakeEverythingPublic.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DestinationDirectory;
    ```
- `public string IVTString { get; set; }`
  - Defined in: `Build/MakeEverythingPublic/MakeEverythingPublic.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IVTString;
    ```

