# Namespace `dnSpy.Contracts.Hex.Files.ToolTips`

## Class `HexToolTipContent`

Contains data used to create a tooltip

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ToolTips.HexToolTipContent(text: /* HexClassifiedTextCollection[] */, image: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContent.cs` (line 27)

### Constructors

- `public HexToolTipContent(HexClassifiedTextCollection[] text, object image)`
  - Summary: Constructor
  - Parameters:
    - `HexClassifiedTextCollection[] text`: Text
    - `object image`: Image shown in the tooltip or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContent.cs` (line 43)

### Properties

- `public HexClassifiedTextCollection[] Text { get; }`
  - Summary: Gets all classified text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContent.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```
- `public object Image { get; }`
  - Summary: Image shown in the tooltip or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContent.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Image;
    ```

## Class `HexToolTipContentCreator`

Creates

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ToolTips.HexToolTipContentCreator();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContentCreator.cs` (line 24)

### Constructors

- `protected HexToolTipContentCreator()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContentCreator.cs` (line 28)

### Methods

- `public abstract HexFieldFormatter CreateNewWriter()`
  - Summary: Creates and returns a new writer. The created text is shown on a new line.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContentCreator.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateNewWriter();
    ```
- `public abstract HexToolTipContent Create()`
  - Summary: Creates the content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContentCreator.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

### Properties

- `public abstract HexFieldFormatter Writer { get; }`
  - Summary: Gets the current writer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContentCreator.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Writer;
    ```
- `public abstract object Image { get; set; }`
  - Summary: Image shown in the tooltip
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContentCreator.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Image;
    ```

## Class `HexToolTipContentCreatorFactory`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.ToolTips.HexToolTipContentCreatorFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContentCreatorFactory.cs` (line 24)

### Constructors

- `protected HexToolTipContentCreatorFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContentCreatorFactory.cs` (line 28)

### Methods

- `public abstract HexToolTipContentCreator Create()`
  - Summary: Creates a
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/ToolTips/HexToolTipContentCreatorFactory.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

