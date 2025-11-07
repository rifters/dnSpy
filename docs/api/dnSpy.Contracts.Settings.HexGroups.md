# Namespace `dnSpy.Contracts.Settings.HexGroups`

## Class `ExportHexViewOptionsGroupNameProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IHexViewOptionsGroupNameProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.HexGroups.ExportHexViewOptionsGroupNameProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupNameProvider.cs` (line 52)

### Constructors

- `public ExportHexViewOptionsGroupNameProviderAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order of this instanec
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupNameProvider.cs` (line 56)

### Properties

- `public double Order { get; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupNameProvider.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportTagOptionDefinitionProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `ITagOptionDefinitionProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.HexGroups.ExportTagOptionDefinitionProviderAttribute(group: /* string */, order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 61)

### Constructors

- `public ExportTagOptionDefinitionProviderAttribute(string group, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string group`: Group, eg.
    - `double order` (default: `double.MaxValue`): Order of this instanec
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 66)

### Properties

- `public double Order { get; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string Group { get; }`
  - Summary: Group, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Group;
    ```

## Class `HexViewOptionChangedEventArgs`

Hex view option changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.HexGroups.HexViewOptionChangedEventArgs(subGroup: /* string */, optionId: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionChangedEventArgs.cs` (line 27)

### Constructors

- `public HexViewOptionChangedEventArgs(string subGroup, string optionId)`
  - Summary: Constructor
  - Parameters:
    - `string subGroup`: Sub group
    - `string optionId`: Option id, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionChangedEventArgs.cs` (line 43)

### Properties

- `public string OptionId { get; }`
  - Summary: Option id, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionChangedEventArgs.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OptionId;
    ```
- `public string SubGroup { get; }`
  - Summary: Sub group, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionChangedEventArgs.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SubGroup;
    ```

## Class `HexViewOptionsGroup`

Contains a group of s that share a subset of all options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.HexGroups.HexViewOptionsGroup and call its members.
var instance = new dnSpy.Contracts.Settings.HexGroups.HexViewOptionsGroup(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroup.cs` (line 30)

### Methods

- `public abstract T GetOptionValue<T>(string tag, VSTE.EditorOptionKey<T> option)`
  - Summary: Gets the current value
  - Parameters:
    - `string tag`: Hex buffer tag, eg.
    - `VSTE.EditorOptionKey<T> option`: Option
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroup.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptionValue(tag: /* string */, option: /* VSTE.EditorOptionKey<T> */);
    ```
- `public abstract bool HasOption(string tag, string optionId)`
  - Summary: Returns true if the option is shared by all hex views in this group
  - Parameters:
    - `string tag`: Hex buffer tag, eg.
    - `string optionId`: Option name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroup.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.HasOption(tag: /* string */, optionId: /* string */);
    ```
- `public abstract bool HasOption<T>(string tag, VSTE.EditorOptionKey<T> option)`
  - Summary: Returns true if the option is shared by all hex views in this group
  - Parameters:
    - `string tag`: Hex buffer tag, eg.
    - `VSTE.EditorOptionKey<T> option`: Option
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroup.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.HasOption(tag: /* string */, option: /* VSTE.EditorOptionKey<T> */);
    ```
- `public abstract object GetOptionValue(string tag, string optionId)`
  - Summary: Gets the current value
  - Parameters:
    - `string tag`: Hex buffer tag, eg.
    - `string optionId`: Option name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroup.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptionValue(tag: /* string */, optionId: /* string */);
    ```
- `public abstract void SetOptionValue(string tag, string optionId, object value)`
  - Summary: Writes a new value
  - Parameters:
    - `string tag`: Hex buffer tag, eg.
    - `string optionId`: Option name
    - `object value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroup.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.SetOptionValue(tag: /* string */, optionId: /* string */, value: /* object */);
    ```
- `public abstract void SetOptionValue<T>(string tag, VSTE.EditorOptionKey<T> option, T value)`
  - Summary: Writes a new value
  - Parameters:
    - `string tag`: Hex buffer tag, eg.
    - `VSTE.EditorOptionKey<T> option`: Option
    - `T value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroup.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.SetOptionValue(tag: /* string */, option: /* VSTE.EditorOptionKey<T> */, value: /* T */);
    ```

### Properties

- `public abstract IEnumerable<WpfHexView> HexViews { get; }`
  - Summary: Gets all hex views in this group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroup.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexViews;
    ```

### Events

- `public abstract event EventHandler<HexViewOptionChangedEventArgs> HexViewOptionChanged`
  - Summary: Raised when an option has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroup.cs` (line 39)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.HexViewOptionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexViewOptionsGroupNameProvider`

Provides group names. Use to export an instance.

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.HexGroups.HexViewOptionsGroupNameProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupNameProvider.cs` (line 29)

### Constructors

- `protected HexViewOptionsGroupNameProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupNameProvider.cs` (line 33)

### Methods

- `public abstract string TryGetGroupName(WpfHexView hexView)`
  - Summary: Returns a group name, eg. , or null
  - Parameters:
    - `WpfHexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupNameProvider.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetGroupName(hexView: /* WpfHexView */);
    ```

## Class `HexViewOptionsGroupService`

service

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.HexGroups.HexViewOptionsGroupService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupService.cs` (line 24)

### Constructors

- `protected HexViewOptionsGroupService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupService.cs` (line 28)

### Methods

- `public abstract HexViewOptionsGroup GetGroup(string name)`
  - Summary: Gets a group
  - Parameters:
    - `string name`: Group name, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupService.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGroup(name: /* string */);
    ```

## Interface `IHexViewOptionsGroupNameProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.HexGroups.IHexViewOptionsGroupNameProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Settings.HexGroups.IHexViewOptionsGroupNameProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupNameProvider.cs` (line 44)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/HexViewOptionsGroupNameProvider.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `ITagOptionDefinitionProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.HexGroups.ITagOptionDefinitionProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Settings.HexGroups.ITagOptionDefinitionProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 51)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string Group { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Group;
    ```

## Class `PredefinedHexViewGroupNames`

Hex view group names

**Example**

```csharp
// Access dnSpy.Contracts.Settings.HexGroups.PredefinedHexViewGroupNames members directly without instantiation.
dnSpy.Contracts.Settings.HexGroups.PredefinedHexViewGroupNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/PredefinedHexViewGroupNames.cs` (line 24)

### Fields

- `public const string HexEditor = nameof(HexEditor)`
  - Summary: Hex editor group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/PredefinedHexViewGroupNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Settings.HexGroups.PredefinedHexViewGroupNames.HexEditor;
    ```

## Class `TagOptionDefinition`

Option definition

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.HexGroups.TagOptionDefinition();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 28)

### Constructors

- `protected TagOptionDefinition()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 58)

### Properties

- `public Type Type { get; set; }`
  - Summary: Gets the type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public bool CanBeSaved { get; set; }`
  - Summary: true if the option can be saved
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanBeSaved;
    ```
- `public object DefaultValue { get; set; }`
  - Summary: Default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DefaultValue;
    ```
- `public string Name { get; set; }`
  - Summary: Hex view option name, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public string SubGroup { get; set; }`
  - Summary: Sub group, eg. . Use to add default options.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SubGroup;
    ```

## Class `TagOptionDefinition<T>`

Option definition

**Inherits/Implements:** `TagOptionDefinition`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.HexGroups.TagOptionDefinition<T>();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 64)

### Constructors

- `public TagOptionDefinition()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 68)
- `public TagOptionDefinition(VSTE.EditorOptionKey<T> option)`
  - Summary: Constructor
  - Parameters:
    - `VSTE.EditorOptionKey<T> option`: Name of option
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 77)
- `public TagOptionDefinition(string optionId)`
  - Summary: Constructor
  - Parameters:
    - `string optionId`: Name of option
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinition.cs` (line 84)

## Class `TagOptionDefinitionProvider`

Provides s. Use to export an instance.

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.HexGroups.TagOptionDefinitionProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 30)

### Constructors

- `protected TagOptionDefinitionProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 34)

### Methods

- `public abstract IEnumerable<TagOptionDefinition> GetOptions()`
  - Summary: Returns the options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptions();
    ```
- `public abstract string GetSubGroup(WpfHexView hexView)`
  - Summary: Gets the sub group (eg. ) to use or null
  - Parameters:
    - `WpfHexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/HexGroups/TagOptionDefinitionProvider.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSubGroup(hexView: /* WpfHexView */);
    ```

