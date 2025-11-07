# Namespace `dnSpy.Roslyn.Text`

## Class `RoslynMefHostServices`

Shared instance

**Example**

```csharp
// Instantiate dnSpy.Roslyn.Text.RoslynMefHostServices and call its members.
var instance = new dnSpy.Roslyn.Text.RoslynMefHostServices(/* arguments */);
```

*Defined in* `dnSpy/Roslyn/dnSpy.Roslyn/Text/RoslynMefHostServices.cs` (line 32)

### Properties

- `public static MefHostServices DefaultServices {
			get {
				if (defaultServices == null)
					Interlocked.CompareExchange(ref defaultServices, CreateDefaultServices(), null);
				return defaultServices;
			}
		}`
  - Summary: Gets the shared instance
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/RoslynMefHostServices.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Roslyn.Text.RoslynMefHostServices.DefaultServices;
    ```

