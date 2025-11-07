# Namespace `dnSpy.Contracts.Hex.Editor.HexGroups`

## Class `HexEditorGroupFactoryService`

Creates hex views that are part of some hex view group

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexGroups.HexEditorGroupFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/HexEditorGroupFactoryService.cs` (line 26)

### Constructors

- `protected HexEditorGroupFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/HexEditorGroupFactoryService.cs` (line 30)

### Methods

- `public abstract LocalGroupOptions GetDefaultLocalOptions(HexView hexView)`
  - Summary: Gets the default local options
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/HexEditorGroupFactoryService.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDefaultLocalOptions(hexView: /* HexView */);
    ```
- `public abstract WpfHexViewHost Create(HexBuffer buffer, string group, string subGroup, Guid? menuGuid)`
  - Summary: Creates a hex view host
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `string group`: Group, eg.
    - `string subGroup`: Sub group, eg.
    - `Guid? menuGuid`: Menu guid or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/HexEditorGroupFactoryService.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(buffer: /* HexBuffer */, group: /* string */, subGroup: /* string */, menuGuid: /* Guid? */);
    ```

## Class `LocalGroupOptions`

Local group options

**Inherits/Implements:** `IEquatable<LocalGroupOptions>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexGroups.LocalGroupOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 26)

### Constructors

- `public LocalGroupOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 51)
- `public LocalGroupOptions(HexView hexView)`
  - Summary: Constructor
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 57)

### Methods

- `public LocalGroupOptions Clone()`
  - Summary: Clones this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 127)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```
- `public LocalGroupOptions CopyTo(LocalGroupOptions destination)`
  - Summary: Copies this instance to and returns
  - Parameters:
    - `LocalGroupOptions destination`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(destination: /* LocalGroupOptions */);
    ```
- `public LocalGroupOptions InitializeFrom(HexView hexView)`
  - Summary: Initializes this instance
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializeFrom(hexView: /* HexView */);
    ```
- `public LocalGroupOptions WriteTo(HexView hexView)`
  - Summary: Writes all options to
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteTo(hexView: /* HexView */);
    ```
- `public bool Equals(LocalGroupOptions other)`
  - Summary: Equals()
  - Parameters:
    - `LocalGroupOptions other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 134)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* LocalGroupOptions */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 152)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 158)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public HexPosition BasePosition { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BasePosition;
    ```
- `public HexPosition EndPosition { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EndPosition;
    ```
- `public HexPosition StartPosition { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StartPosition;
    ```
- `public HexValuesDisplayFormat HexValuesDisplayFormat { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexValuesDisplayFormat;
    ```
- `public bool ShowAsciiColumn { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowAsciiColumn;
    ```
- `public bool ShowOffsetColumn { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowOffsetColumn;
    ```
- `public bool ShowValuesColumn { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowValuesColumn;
    ```
- `public bool UseRelativePositions { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseRelativePositions;
    ```
- `public int BytesPerLine { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BytesPerLine;
    ```
- `public int OffsetBitSize { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGroups/LocalGroupOptions.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OffsetBitSize;
    ```

