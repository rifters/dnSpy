# Namespace `dnSpy.Text.Editor`

## Class `OptionsHelpers`

Options methods

**Example**

```csharp
// Access dnSpy.Text.Editor.OptionsHelpers members directly without instantiation.
dnSpy.Text.Editor.OptionsHelpers./* member */
```

*Defined in* `dnSpy/dnSpy/Text/Editor/OptionsHelpers.cs` (line 24)

### Methods

- `public static int FilterIndentSize(int indentSize)`
  - Summary: Filters so it's between and (inclusive)
  - Parameters:
    - `int indentSize`: Indent size
  - Defined in: `dnSpy/dnSpy/Text/Editor/OptionsHelpers.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Text.Editor.OptionsHelpers.FilterIndentSize(indentSize: /* int */);
    ```
- `public static int FilterTabSize(int tabSize)`
  - Summary: Filters so it's between and (inclusive)
  - Parameters:
    - `int tabSize`: Tab size
  - Defined in: `dnSpy/dnSpy/Text/Editor/OptionsHelpers.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Text.Editor.OptionsHelpers.FilterTabSize(tabSize: /* int */);
    ```

### Fields

- `public static readonly int MaximumIndentSize = 60`
  - Summary: Maximum indent size
  - Defined in: `dnSpy/dnSpy/Text/Editor/OptionsHelpers.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Text.Editor.OptionsHelpers.MaximumIndentSize;
    ```
- `public static readonly int MaximumTabSize = 60`
  - Summary: Maximum tab size
  - Defined in: `dnSpy/dnSpy/Text/Editor/OptionsHelpers.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Text.Editor.OptionsHelpers.MaximumTabSize;
    ```
- `public static readonly int MinimumIndentSize = 1`
  - Summary: Minimum indent size
  - Defined in: `dnSpy/dnSpy/Text/Editor/OptionsHelpers.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Text.Editor.OptionsHelpers.MinimumIndentSize;
    ```
- `public static readonly int MinimumTabSize = 1`
  - Summary: Minimum tab size
  - Defined in: `dnSpy/dnSpy/Text/Editor/OptionsHelpers.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Text.Editor.OptionsHelpers.MinimumTabSize;
    ```

