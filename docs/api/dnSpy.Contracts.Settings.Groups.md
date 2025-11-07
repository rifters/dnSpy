# Namespace `dnSpy.Contracts.Settings.Groups`

## Class `ContentTypeOptionDefinition`

Option definition

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.Groups.ContentTypeOptionDefinition();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 28)

### Constructors

- `protected ContentTypeOptionDefinition()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 58)

### Properties

- `public Type Type { get; set; }`
  - Summary: Gets the type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public bool CanBeSaved { get; set; }`
  - Summary: true if the option can be saved
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanBeSaved;
    ```
- `public object DefaultValue { get; set; }`
  - Summary: Default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DefaultValue;
    ```
- `public string ContentType { get; set; }`
  - Summary: Content type, eg. . Use to add default options.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentType;
    ```
- `public string Name { get; set; }`
  - Summary: Text view option name, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `ContentTypeOptionDefinition<T>`

Option definition

**Inherits/Implements:** `ContentTypeOptionDefinition`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.Groups.ContentTypeOptionDefinition<T>();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 64)

### Constructors

- `public ContentTypeOptionDefinition()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 68)
- `public ContentTypeOptionDefinition(EditorOptionKey<T> option)`
  - Summary: Constructor
  - Parameters:
    - `EditorOptionKey<T> option`: Name of option
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 77)
- `public ContentTypeOptionDefinition(string optionId)`
  - Summary: Constructor
  - Parameters:
    - `string optionId`: Name of option
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ContentTypeOptionDefinition.cs` (line 84)

## Class `ExportContentTypeOptionDefinitionProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IContentTypeOptionDefinitionProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.Groups.ExportContentTypeOptionDefinitionProviderAttribute(group: /* string */, order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/IContentTypeOptionDefinitionProvider.cs` (line 48)

### Constructors

- `public ExportContentTypeOptionDefinitionProviderAttribute(string group, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string group`: Group, eg.
    - `double order` (default: `double.MaxValue`): Order of this instanec
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/IContentTypeOptionDefinitionProvider.cs` (line 53)

### Properties

- `public double Order { get; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/IContentTypeOptionDefinitionProvider.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string Group { get; }`
  - Summary: Group, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/IContentTypeOptionDefinitionProvider.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Group;
    ```

## Class `ExportTextViewOptionsGroupNameProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `ITextViewOptionsGroupNameProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.Groups.ExportTextViewOptionsGroupNameProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroupNameProvider.cs` (line 47)

### Constructors

- `public ExportTextViewOptionsGroupNameProviderAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order of this instanec
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroupNameProvider.cs` (line 51)

### Properties

- `public double Order { get; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroupNameProvider.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IContentTypeOptionDefinitionProvider`

Provides s. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.Groups.IContentTypeOptionDefinitionProvider and call its members.
var instance = new dnSpy.Contracts.Settings.Groups.IContentTypeOptionDefinitionProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/IContentTypeOptionDefinitionProvider.cs` (line 29)

### Methods

- `IEnumerable<ContentTypeOptionDefinition> GetOptions()`
  - Summary: Returns the options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/IContentTypeOptionDefinitionProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptions();
    ```

## Interface `IContentTypeOptionDefinitionProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.Groups.IContentTypeOptionDefinitionProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Settings.Groups.IContentTypeOptionDefinitionProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/IContentTypeOptionDefinitionProvider.cs` (line 38)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/IContentTypeOptionDefinitionProvider.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string Group { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/IContentTypeOptionDefinitionProvider.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Group;
    ```

## Interface `ITextViewOptionsGroup`

Contains a group of s that share a subset of all options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.Groups.ITextViewOptionsGroup and call its members.
var instance = new dnSpy.Contracts.Settings.Groups.ITextViewOptionsGroup(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroup.cs` (line 29)

### Methods

- `T GetOptionValue<T>(string contentType, EditorOptionKey<T> option)`
  - Summary: Gets the current value
  - Parameters:
    - `string contentType`: Content type, eg.
    - `EditorOptionKey<T> option`: Option
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroup.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptionValue(contentType: /* string */, option: /* EditorOptionKey<T> */);
    ```
- `bool HasOption(string contentType, string optionId)`
  - Summary: Returns true if the option is shared by all text views in this group
  - Parameters:
    - `string contentType`: Content type, eg.
    - `string optionId`: Option name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroup.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.HasOption(contentType: /* string */, optionId: /* string */);
    ```
- `bool HasOption<T>(string contentType, EditorOptionKey<T> option)`
  - Summary: Returns true if the option is shared by all text views in this group
  - Parameters:
    - `string contentType`: Content type, eg.
    - `EditorOptionKey<T> option`: Option
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroup.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.HasOption(contentType: /* string */, option: /* EditorOptionKey<T> */);
    ```
- `object GetOptionValue(string contentType, string optionId)`
  - Summary: Gets the current value
  - Parameters:
    - `string contentType`: Content type, eg.
    - `string optionId`: Option name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroup.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptionValue(contentType: /* string */, optionId: /* string */);
    ```
- `void SetOptionValue(string contentType, string optionId, object value)`
  - Summary: Writes a new value
  - Parameters:
    - `string contentType`: Content type, eg.
    - `string optionId`: Option name
    - `object value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroup.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.SetOptionValue(contentType: /* string */, optionId: /* string */, value: /* object */);
    ```
- `void SetOptionValue<T>(string contentType, EditorOptionKey<T> option, T value)`
  - Summary: Writes a new value
  - Parameters:
    - `string contentType`: Content type, eg.
    - `EditorOptionKey<T> option`: Option
    - `T value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroup.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.SetOptionValue(contentType: /* string */, option: /* EditorOptionKey<T> */, value: /* T */);
    ```

### Properties

- `IEnumerable<IWpfTextView> TextViews { get; }`
  - Summary: Gets all text views in this group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroup.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViews;
    ```

### Events

- `event EventHandler<TextViewOptionChangedEventArgs> TextViewOptionChanged`
  - Summary: Raised when an option has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroup.cs` (line 38)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TextViewOptionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `ITextViewOptionsGroupNameProvider`

Provides group names. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.Groups.ITextViewOptionsGroupNameProvider and call its members.
var instance = new dnSpy.Contracts.Settings.Groups.ITextViewOptionsGroupNameProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroupNameProvider.cs` (line 29)

### Methods

- `string TryGetGroupName(IWpfTextView textView)`
  - Summary: Returns a group name, eg. , or null
  - Parameters:
    - `IWpfTextView textView`: Text view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroupNameProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetGroupName(textView: /* IWpfTextView */);
    ```

## Interface `ITextViewOptionsGroupNameProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.Groups.ITextViewOptionsGroupNameProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Settings.Groups.ITextViewOptionsGroupNameProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroupNameProvider.cs` (line 39)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroupNameProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `ITextViewOptionsGroupService`

service

**Example**

```csharp
// Instantiate dnSpy.Contracts.Settings.Groups.ITextViewOptionsGroupService and call its members.
var instance = new dnSpy.Contracts.Settings.Groups.ITextViewOptionsGroupService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroupService.cs` (line 24)

### Methods

- `ITextViewOptionsGroup GetGroup(string name)`
  - Summary: Gets a group
  - Parameters:
    - `string name`: Group name, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/ITextViewOptionsGroupService.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGroup(name: /* string */);
    ```

## Class `PredefinedTextViewGroupNames`

Text view group names

**Example**

```csharp
// Access dnSpy.Contracts.Settings.Groups.PredefinedTextViewGroupNames members directly without instantiation.
dnSpy.Contracts.Settings.Groups.PredefinedTextViewGroupNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/PredefinedTextViewGroupNames.cs` (line 24)

### Fields

- `public const string CodeEditor = nameof(CodeEditor)`
  - Summary: Code editor group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/PredefinedTextViewGroupNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Settings.Groups.PredefinedTextViewGroupNames.CodeEditor;
    ```
- `public const string DocumentViewer = nameof(DocumentViewer)`
  - Summary: Text viewer group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/PredefinedTextViewGroupNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Settings.Groups.PredefinedTextViewGroupNames.DocumentViewer;
    ```
- `public const string OutputWindow = nameof(OutputWindow)`
  - Summary: Output window group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/PredefinedTextViewGroupNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Settings.Groups.PredefinedTextViewGroupNames.OutputWindow;
    ```
- `public const string REPL = nameof(REPL)`
  - Summary: REPL group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/PredefinedTextViewGroupNames.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Settings.Groups.PredefinedTextViewGroupNames.REPL;
    ```

## Class `TextViewOptionChangedEventArgs`

Text view option changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Settings.Groups.TextViewOptionChangedEventArgs(contentType: /* string */, optionId: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/TextViewOptionChangedEventArgs.cs` (line 27)

### Constructors

- `public TextViewOptionChangedEventArgs(string contentType, string optionId)`
  - Summary: Constructor
  - Parameters:
    - `string contentType`: Content type
    - `string optionId`: Option id, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/TextViewOptionChangedEventArgs.cs` (line 43)

### Properties

- `public string ContentType { get; }`
  - Summary: Content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/TextViewOptionChangedEventArgs.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentType;
    ```
- `public string OptionId { get; }`
  - Summary: Option id, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Settings/Groups/TextViewOptionChangedEventArgs.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OptionId;
    ```

