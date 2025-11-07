# Namespace `dnSpy.Decompiler.Settings`

## Class `DecompilerOption<T>`

**Inherits/Implements:** `IDecompilerOption`

**Example**

```csharp
var instance = new dnSpy.Decompiler.Settings.DecompilerOption<T>(guid: /* Guid */, getter: /* Func<T> */, setter: /* Action<T> */);
```

*Defined in* `dnSpy/dnSpy.Decompiler/Settings/DecompilerOption.cs` (line 24)

### Constructors

- `public DecompilerOption(Guid guid, Func<T> getter, Action<T> setter)`
  - Parameters:
    - `Guid guid`: Description not provided.
    - `Func<T> getter`: Description not provided.
    - `Action<T> setter`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/Settings/DecompilerOption.cs` (line 37)

### Properties

- `public Guid Guid { get; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/Settings/DecompilerOption.cs` (line 27)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public Type Type => typeof(T)`
  - Defined in: `dnSpy/dnSpy.Decompiler/Settings/DecompilerOption.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public object Value {
			get { return getter(); }
			set { setter((T)value); }
		}`
  - Defined in: `dnSpy/dnSpy.Decompiler/Settings/DecompilerOption.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public string Description { get; set; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/Settings/DecompilerOption.cs` (line 25)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Description;
    ```
- `public string Name { get; set; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/Settings/DecompilerOption.cs` (line 26)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

