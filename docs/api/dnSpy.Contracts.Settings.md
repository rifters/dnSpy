# Namespace `dnSpy.Contracts.Settings`

## Interface `ISettingsSection`

Settings section

**Inherits/Implements:** `ISettingsSectionProvider`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.ISettingsSection and call its members.
var instance = new dnSpy.Contracts.Settings.ISettingsSection(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSection.cs` (line 26)

### Methods

- `T Attribute<T>(string name)`
  - Summary: Gets the value of the attribute or the default value if it's not present
  - Parameters:
    - `string name`: Name of attribute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSection.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.Attribute(name: /* string */);
    ```
- `void Attribute<T>(string name, T value)`
  - Summary: Adds or overwrites an existing attribute with a new value
  - Parameters:
    - `string name`: Name of attribute
    - `T value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSection.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.Attribute(name: /* string */, value: /* T */);
    ```
- `void CopyFrom(ISettingsSection section)`
  - Summary: Copies to this instance
  - Parameters:
    - `ISettingsSection section`: Source section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSection.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyFrom(section: /* ISettingsSection */);
    ```
- `void RemoveAttribute(string name)`
  - Summary: Removes an attribute
  - Parameters:
    - `string name`: Name of attribute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSection.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAttribute(name: /* string */);
    ```

### Properties

- `Tuple<string, string>[] Attributes { get; }`
  - Summary: Gets all attributes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSection.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Attributes;
    ```
- `string Name { get; }`
  - Summary: Name of section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSection.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `ISettingsSectionProvider`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.ISettingsSectionProvider and call its members.
var instance = new dnSpy.Contracts.Settings.ISettingsSectionProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSectionProvider.cs` (line 24)

### Methods

- `ISettingsSection CreateSection(string name)`
  - Summary: Creates a new section, even if a section with the same name already exists
  - Parameters:
    - `string name`: Name of section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSectionProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateSection(name: /* string */);
    ```
- `ISettingsSection GetOrCreateSection(string name)`
  - Summary: Gets an existing section or creates a new one if one doesn't exist
  - Parameters:
    - `string name`: Name of section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSectionProvider.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateSection(name: /* string */);
    ```
- `ISettingsSection TryGetSection(string name)`
  - Summary: Gets a section or null if it doesn't exist
  - Parameters:
    - `string name`: Name of section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSectionProvider.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetSection(name: /* string */);
    ```
- `ISettingsSection[] SectionsWithName(string name)`
  - Summary: Gets all sections
  - Parameters:
    - `string name`: Name of section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSectionProvider.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.SectionsWithName(name: /* string */);
    ```
- `void RemoveSection(ISettingsSection section)`
  - Summary: Removes a section
  - Parameters:
    - `ISettingsSection section`: Section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSectionProvider.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveSection(section: /* ISettingsSection */);
    ```
- `void RemoveSection(string name)`
  - Summary: Removes a section
  - Parameters:
    - `string name`: Name of section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSectionProvider.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveSection(name: /* string */);
    ```

### Properties

- `ISettingsSection[] Sections { get; }`
  - Summary: Gets all sections
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsSectionProvider.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Sections;
    ```

## Interface `ISettingsService`

Adds/removes settings

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.ISettingsService and call its members.
var instance = new dnSpy.Contracts.Settings.ISettingsService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsService.cs` (line 26)

### Methods

- `ISettingsSection GetOrCreateSection(Guid guid)`
  - Summary: Gets an existing section or creates a new one if one doesn't exist
  - Parameters:
    - `Guid guid`: Guid of section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsService.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateSection(guid: /* Guid */);
    ```
- `ISettingsSection RecreateSection(Guid guid)`
  - Summary: Removes an existing section and re-creates it
  - Parameters:
    - `Guid guid`: Guid of section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsService.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.RecreateSection(guid: /* Guid */);
    ```
- `void RemoveSection(Guid guid)`
  - Summary: Removes a section
  - Parameters:
    - `Guid guid`: Guid of section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsService.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveSection(guid: /* Guid */);
    ```
- `void RemoveSection(ISettingsSection section)`
  - Summary: Removes a section
  - Parameters:
    - `ISettingsSection section`: Section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsService.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveSection(section: /* ISettingsSection */);
    ```

### Properties

- `ISettingsSection[] Sections { get; }`
  - Summary: Gets all sections
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsService.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Sections;
    ```

## Interface `ISettingsService2`

Adds/removes settings

**Inherits/Implements:** `ISettingsService`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.ISettingsService2 and call its members.
var instance = new dnSpy.Contracts.Settings.ISettingsService2(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsService2.cs` (line 24)

### Methods

- `void Open(string filename)`
  - Summary: Reads settings from a file. All current settings are removed
  - Parameters:
    - `string filename`: Filename of saved settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsService2.cs` (line 29)
  - Example:
    ```csharp
    // Example invocation
    instance.Open(filename: /* string */);
    ```
- `void Save(string filename)`
  - Summary: Saves current settings
  - Parameters:
    - `string filename`: Filename
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsService2.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Save(filename: /* string */);
    ```

## Interface `ISettingsServiceFactory`

Creates instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.ISettingsServiceFactory and call its members.
var instance = new dnSpy.Contracts.Settings.ISettingsServiceFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsServiceFactory.cs` (line 24)

### Methods

- `ISettingsService2 Create()`
  - Summary: Creates a settings service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/ISettingsServiceFactory.cs` (line 29)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

