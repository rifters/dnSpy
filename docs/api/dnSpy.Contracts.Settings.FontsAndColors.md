# Namespace `dnSpy.Contracts.Settings.FontsAndColors`

## Class `FontAndColorOptions`

Font and color options

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.FontsAndColors.FontAndColorOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontAndColorOptions.cs` (line 26)

### Constructors

- `protected FontAndColorOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontAndColorOptions.cs` (line 30)

### Methods

- `public abstract void OnApply()`
  - Summary: Saves all settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontAndColorOptions.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.OnApply();
    ```
- `public virtual void OnClosed()`
  - Summary: Called after the dialog box is closed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontAndColorOptions.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.OnClosed();
    ```

### Properties

- `public abstract FontOption FontOption { get; }`
  - Summary: Font option
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontAndColorOptions.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontOption;
    ```
- `public abstract string DisplayName { get; }`
  - Summary: Name shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontAndColorOptions.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DisplayName;
    ```
- `public abstract string Name { get; }`
  - Summary: Unique name, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontAndColorOptions.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `FontAndColorOptionsProvider`

Creates used by the fonts settings page

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.FontsAndColors.FontAndColorOptionsProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontAndColorOptionsProvider.cs` (line 26)

### Constructors

- `protected FontAndColorOptionsProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontAndColorOptionsProvider.cs` (line 30)

### Methods

- `public abstract IEnumerable<FontAndColorOptions> GetFontAndColors()`
  - Summary: Creates instances
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontAndColorOptionsProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFontAndColors();
    ```

## Class `FontOption`

Font option

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.FontsAndColors.FontOption(fontType: /* FontType */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontOption.cs` (line 27)

### Constructors

- `public FontOption(FontType fontType)`
  - Summary: Constructor
  - Parameters:
    - `FontType fontType`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontOption.cs` (line 47)

### Properties

- `public FontFamily FontFamily { get; set; }`
  - Summary: Gets/sets the font family
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontOption.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontFamily;
    ```
- `public FontType FontType { get; }`
  - Summary: Font type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontOption.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontType;
    ```
- `public double FontSize { get; set; }`
  - Summary: Gets/sets the font size
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/FontsAndColors/FontOption.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontSize;
    ```

