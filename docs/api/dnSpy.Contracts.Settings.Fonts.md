# Namespace `dnSpy.Contracts.Settings.Fonts`

## Class `ExportThemeFontSettingsDefinitionAttribute`

Exports a field

**Inherits/Implements:** `ExportAttribute`, `IThemeFontSettingsDefinitionMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.Fonts.ExportThemeFontSettingsDefinitionAttribute(name: /* string */, fontType: /* FontType */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsDefinition.cs` (line 42)

### Constructors

- `public ExportThemeFontSettingsDefinitionAttribute(string name, FontType fontType)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
    - `FontType fontType`: Font type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsDefinition.cs` (line 49)

### Properties

- `public FontType FontType { get; }`
  - Summary: Font type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsDefinition.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontType;
    ```
- `public string Name { get; }`
  - Summary: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsDefinition.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `FontSettings`

Font settings

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.Fonts.FontSettings();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/FontSettings.cs` (line 28)

### Constructors

- `protected FontSettings()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/FontSettings.cs` (line 32)

### Methods

- `protected void OnPropertyChanged(string propertyName)`
  - Summary: Raises
  - Parameters:
    - `string propertyName`: Property name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/FontSettings.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propertyName: /* string */);
    ```

### Properties

- `public FontType FontType => ThemeFontSettings.FontType`
  - Summary: Gets the font type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/FontSettings.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontType;
    ```
- `public abstract FontFamily FontFamily { get; set; }`
  - Summary: Gets/sets the font family
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/FontSettings.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontFamily;
    ```
- `public abstract Guid ThemeGuid { get; }`
  - Summary: Gets the theme guid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/FontSettings.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ThemeGuid;
    ```
- `public abstract ThemeFontSettings ThemeFontSettings { get; }`
  - Summary: Gets the owner
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/FontSettings.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ThemeFontSettings;
    ```
- `public abstract double FontSize { get; set; }`
  - Summary: Gets/sets the font size
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/FontSettings.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontSize;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised after a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/FontSettings.cs` (line 37)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Enum `FontType`

Font type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.Fonts.FontType and call its members.
var instance = new dnSpy.Contracts.Settings.Fonts.FontType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/FontType.cs` (line 24)

### Members

- `TextEditor`: Text editor font
- `HexEditor`: Hex editor font (monospaced font)
- `Monospaced`: Monospaced font
- `UI`: UI font

## Interface `IThemeFontSettingsDefinitionMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.Fonts.IThemeFontSettingsDefinitionMetadata and call its members.
var instance = new dnSpy.Contracts.Settings.Fonts.IThemeFontSettingsDefinitionMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsDefinition.cs` (line 32)

### Properties

- `FontType FontType { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsDefinition.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontType;
    ```
- `string Name { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsDefinition.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `ThemeFontSettings`

Theme font settings

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.Fonts.ThemeFontSettings();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettings.cs` (line 28)

### Constructors

- `protected ThemeFontSettings()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettings.cs` (line 32)

### Methods

- `protected void OnPropertyChanged(string propertyName)`
  - Summary: Raises
  - Parameters:
    - `string propertyName`: Property name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettings.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propertyName: /* string */);
    ```
- `public abstract FontSettings GetSettings(Guid themeGuid)`
  - Summary: Gets theme settings
  - Parameters:
    - `Guid themeGuid`: Guid of theme
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettings.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSettings(themeGuid: /* Guid */);
    ```

### Properties

- `public abstract FontSettings Active { get; }`
  - Summary: Gets the active instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettings.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Active;
    ```
- `public abstract FontType FontType { get; }`
  - Summary: Gets the font type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettings.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontType;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the name, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettings.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised after a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettings.cs` (line 37)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `ThemeFontSettingsDefinition`

Defines a font. Use to export a field.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.Fonts.ThemeFontSettingsDefinition and call its members.
var instance = new dnSpy.Contracts.Settings.Fonts.ThemeFontSettingsDefinition(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsDefinition.cs` (line 28)

## Class `ThemeFontSettingsService`

service

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.Fonts.ThemeFontSettingsService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsService.cs` (line 26)

### Constructors

- `protected ThemeFontSettingsService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsService.cs` (line 30)

### Methods

- `public abstract ThemeFontSettings GetSettings(string name)`
  - Summary: Gets a instance
  - Parameters:
    - `string name`: Name, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Fonts/ThemeFontSettingsService.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSettings(name: /* string */);
    ```

