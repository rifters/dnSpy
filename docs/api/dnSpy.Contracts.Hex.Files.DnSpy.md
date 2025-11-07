# Namespace `dnSpy.Contracts.Hex.Files.DnSpy`

## Class `HexFileImageReferenceProvider`

Provides s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DnSpy.HexFileImageReferenceProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/HexFileImageReferenceProvider.cs` (line 26)

### Constructors

- `protected HexFileImageReferenceProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/HexFileImageReferenceProvider.cs` (line 30)

### Methods

- `public abstract ImageReference? GetImage(ComplexData structure, HexPosition position)`
  - Summary: Gets an image or null
  - Parameters:
    - `ComplexData structure`: Structure
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/HexFileImageReferenceProvider.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImage(structure: /* ComplexData */, position: /* HexPosition */);
    ```

## Class `ToolTipCreator`

Creates tooltips

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DnSpy.ToolTipCreator();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/ToolTipCreator.cs` (line 26)

### Constructors

- `protected ToolTipCreator()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/ToolTipCreator.cs` (line 30)

### Methods

- `public abstract object Create()`
  - Summary: Creates an object that can be added to a tooltip
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/ToolTipCreator.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

### Properties

- `public abstract HexToolTipContentCreator ToolTipContentCreator { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/ToolTipCreator.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTipContentCreator;
    ```

## Class `ToolTipCreatorFactory`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DnSpy.ToolTipCreatorFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/ToolTipCreatorFactory.cs` (line 24)

### Constructors

- `protected ToolTipCreatorFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/ToolTipCreatorFactory.cs` (line 28)

### Methods

- `public abstract ToolTipCreator Create()`
  - Summary: Creates a instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/ToolTipCreatorFactory.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

## Class `ToolTipObjectFactory`

Creates objects that can be shown in tooltips

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Files.DnSpy.ToolTipObjectFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/ToolTipObjectFactory.cs` (line 26)

### Constructors

- `protected ToolTipObjectFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/ToolTipObjectFactory.cs` (line 30)

### Methods

- `public abstract object Create(HexToolTipContent content)`
  - Summary: Creates an object that can be shown in a tooltip
  - Parameters:
    - `HexToolTipContent content`: Content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Files/DnSpy/ToolTipObjectFactory.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(content: /* HexToolTipContent */);
    ```

