# Namespace `dnSpy.Contracts.Extension`

## Enum `AutoLoadedLoadType`

load type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Extension.AutoLoadedLoadType and call its members.
var instance = new dnSpy.Contracts.Extension.AutoLoadedLoadType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Extension/IAutoLoaded.cs` (line 34)

### Members

- `BeforeExtensions`: Loaded before extensions are created
- `AfterExtensions`: Loaded after extensions have been created
- `AfterExtensionsLoaded`: Loaded after all extensions have been created and loaded
- `AppLoaded`: Loaded when the app has been loaded

## Class `ExportAutoLoadedAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IAutoLoadedMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Extension.ExportAutoLoadedAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Extension/IAutoLoaded.cs` (line 67)

### Constructors

- `public ExportAutoLoadedAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IAutoLoaded.cs` (line 70)

### Properties

- `public AutoLoadedLoadType LoadType { get; set; }`
  - Summary: Default is
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IAutoLoaded.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LoadType;
    ```
- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IAutoLoaded.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportExtensionAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IExtensionMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Extension.ExportExtensionAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Extension/IExtension.cs` (line 57)

### Constructors

- `public ExportExtensionAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IExtension.cs` (line 60)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IExtension.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Enum `ExtensionEvent`

Extension event

**Example**

```csharp
// Instantiate dnSpy.Contracts.Extension.ExtensionEvent and call its members.
var instance = new dnSpy.Contracts.Extension.ExtensionEvent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Extension/ExtensionEvent.cs` (line 24)

### Members

- `Loaded`: All extensions have been loaded
- `AppLoaded`: The app has been loaded
- `AppExit`: The app is closing

## Class `ExtensionInfo`

Extension information

**Example**

```csharp
// Instantiate dnSpy.Contracts.Extension.ExtensionInfo and call its members.
var instance = new dnSpy.Contracts.Extension.ExtensionInfo(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Extension/ExtensionInfo.cs` (line 26)

### Properties

- `public string Copyright { get; set; }`
  - Summary: Copyright message or null to get it from the assembly's
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/ExtensionInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Copyright;
    ```
- `public string ShortDescription { get; set; }`
  - Summary: Short description or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/ExtensionInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShortDescription;
    ```

## Interface `IAutoLoaded`

All classes that export this type automatically get loaded at startup. Use to export it.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Extension.IAutoLoaded and call its members.
var instance = new dnSpy.Contracts.Extension.IAutoLoaded(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Extension/IAutoLoaded.cs` (line 28)

## Interface `IAutoLoadedMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Extension.IAutoLoadedMetadata and call its members.
var instance = new dnSpy.Contracts.Extension.IAutoLoadedMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Extension/IAutoLoaded.cs` (line 57)

### Properties

- `AutoLoadedLoadType LoadType { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IAutoLoaded.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LoadType;
    ```
- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IAutoLoaded.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IExtension`

All extensions should export exactly one type that implements this interface. Use to export a extension.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Extension.IExtension and call its members.
var instance = new dnSpy.Contracts.Extension.IExtension(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Extension/IExtension.cs` (line 29)

### Methods

- `void OnEvent(ExtensionEvent @event, object obj)`
  - Summary: Called at various times
  - Parameters:
    - `ExtensionEvent @event`: Description not provided.
    - `object obj`: Data, see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IExtension.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.OnEvent(@event: /* ExtensionEvent */, obj: /* object */);
    ```

### Properties

- `ExtensionInfo ExtensionInfo { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IExtension.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExtensionInfo;
    ```
- `IEnumerable<string> MergedResourceDictionaries { get; }`
  - Summary: Gets relative paths of all resource dictionaries that will be added to the app's resources
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IExtension.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MergedResourceDictionaries;
    ```

## Interface `IExtensionMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Extension.IExtensionMetadata and call its members.
var instance = new dnSpy.Contracts.Extension.IExtensionMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Extension/IExtension.cs` (line 49)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Extension/IExtension.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

