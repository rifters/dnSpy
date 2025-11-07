# Namespace `dnSpy.Contracts.BackgroundImage`

## Class `BackgroundImageOptionDefinitionConstants`

constants

**Example**

```csharp
// Access dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants members directly without instantiation.
dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 27)

### Fields

- `public const double AttrOrder_CodeEditor = AttrOrder_Default + 3000`
  - Summary: Order of definition
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.AttrOrder_CodeEditor;
    ```
- `public const double AttrOrder_Default = 1000000`
  - Summary: Default order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.AttrOrder_Default;
    ```
- `public const double AttrOrder_DocumentViewer = AttrOrder_Default + 1000`
  - Summary: Order of definition
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.AttrOrder_DocumentViewer;
    ```
- `public const double AttrOrder_HexEditor = AttrOrder_Default + 100000000`
  - Summary: Order of hex editor definition
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.AttrOrder_HexEditor;
    ```
- `public const double AttrOrder_HexEditorDebuggerMemory = AttrOrder_Default + 5000`
  - Summary: Order of hex editor (Debugger / Process Memory) definition
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 61)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.AttrOrder_HexEditorDebuggerMemory;
    ```
- `public const double AttrOrder_Logger = AttrOrder_Default + 4000`
  - Summary: Order of definition
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 51)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.AttrOrder_Logger;
    ```
- `public const double AttrOrder_Repl = AttrOrder_Default + 2000`
  - Summary: Order of definition
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.AttrOrder_Repl;
    ```
- `public const double UIOrder_CodeEditor = 2000`
  - Summary: UI order of
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 76)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.UIOrder_CodeEditor;
    ```
- `public const double UIOrder_DocumentViewer = -1000`
  - Summary: UI order of
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 66)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.UIOrder_DocumentViewer;
    ```
- `public const double UIOrder_HexEditor = 4000`
  - Summary: UI order of hex editor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 86)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.UIOrder_HexEditor;
    ```
- `public const double UIOrder_HexEditorDebuggerMemory = 5000`
  - Summary: UI order of hex editor (Debugger / Process Memory)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 91)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.UIOrder_HexEditorDebuggerMemory;
    ```
- `public const double UIOrder_Logger = 3000`
  - Summary: UI order of
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 81)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.UIOrder_Logger;
    ```
- `public const double UIOrder_Repl = 1000`
  - Summary: UI order of
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/BackgroundImageOptionDefinitionConstants.cs` (line 71)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.BackgroundImage.BackgroundImageOptionDefinitionConstants.UIOrder_Repl;
    ```

## Class `DefaultImageSettings`

Default image settings

**Example**

```csharp
// Instantiate dnSpy.Contracts.BackgroundImage.DefaultImageSettings and call its members.
var instance = new dnSpy.Contracts.BackgroundImage.DefaultImageSettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 28)

### Properties

- `public ImagePlacement? ImagePlacement { get; set; }`
  - Summary: Image placement or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImagePlacement;
    ```
- `public Stretch? Stretch { get; set; }`
  - Summary: Stretch value or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Stretch;
    ```
- `public StretchDirection? StretchDirection { get; set; }`
  - Summary: Stretch direction value or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StretchDirection;
    ```
- `public TimeSpan? Interval { get; set; }`
  - Summary: Time interval until next image is shown or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 112)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Interval;
    ```
- `public bool? IsEnabled { get; set; }`
  - Summary: true if it's enabled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnabled;
    ```
- `public bool? IsRandom { get; set; }`
  - Summary: True if images are picked in random order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRandom;
    ```
- `public double? BottomMarginHeightPercent { get; }`
  - Summary: Bottom margin height (%) or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BottomMarginHeightPercent;
    ```
- `public double? HorizontalOffset { get; set; }`
  - Summary: Horizontal offset or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HorizontalOffset;
    ```
- `public double? LeftMarginWidthPercent { get; }`
  - Summary: Left margin width (%) or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LeftMarginWidthPercent;
    ```
- `public double? MaxHeight { get; set; }`
  - Summary: Max height or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MaxHeight;
    ```
- `public double? MaxWidth { get; set; }`
  - Summary: Max width or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MaxWidth;
    ```
- `public double? Opacity { get; set; }`
  - Summary: Opacity or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Opacity;
    ```
- `public double? RightMarginWidthPercent { get; }`
  - Summary: Right margin width (%) or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RightMarginWidthPercent;
    ```
- `public double? TopMarginHeightPercent { get; }`
  - Summary: Top margin height (%) or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TopMarginHeightPercent;
    ```
- `public double? VerticalOffset { get; set; }`
  - Summary: Vertical offset or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VerticalOffset;
    ```
- `public double? Zoom { get; set; }`
  - Summary: Zoom (%) or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Zoom;
    ```
- `public string[] Images { get; set; }`
  - Summary: All images or null to use the default value. This can be filenames, folders, or pack:// URIs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/DefaultImageSettings.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Images;
    ```

## Class `ExportBackgroundImageOptionDefinitionAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IBackgroundImageOptionDefinitionMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.BackgroundImage.ExportBackgroundImageOptionDefinitionAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 81)

### Constructors

- `public ExportBackgroundImageOptionDefinitionAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order of this instance, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 87)

### Properties

- `public double Order { get; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IBackgroundImageOptionDefinition`

Defines background image options. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.BackgroundImage.IBackgroundImageOptionDefinition and call its members.
var instance = new dnSpy.Contracts.BackgroundImage.IBackgroundImageOptionDefinition(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 30)

### Methods

- `DefaultImageSettings GetDefaultImageSettings()`
  - Summary: Gets the default settings or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDefaultImageSettings();
    ```
- `bool IsSupported(HexView hexView)`
  - Summary: Returns true if the hex view should use this instance's background image settings
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.IsSupported(hexView: /* HexView */);
    ```
- `bool IsSupported(ITextView textView)`
  - Summary: Returns true if the text view should use this instance's background image settings
  - Parameters:
    - `ITextView textView`: Text view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.IsSupported(textView: /* ITextView */);
    ```

### Properties

- `bool UserVisible { get; }`
  - Summary: true if the user can change the settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UserVisible;
    ```
- `double UIOrder { get; }`
  - Summary: Order of this option when shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIOrder;
    ```
- `string DisplayName { get; }`
  - Summary: Name shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DisplayName;
    ```
- `string Id { get; }`
  - Summary: Unique settings id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Interface `IBackgroundImageOptionDefinitionMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.BackgroundImage.IBackgroundImageOptionDefinitionMetadata and call its members.
var instance = new dnSpy.Contracts.BackgroundImage.IBackgroundImageOptionDefinitionMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 73)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/IBackgroundImageOptionDefinition.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Enum `ImagePlacement`

Image placement

**Example**

```csharp
// Instantiate dnSpy.Contracts.BackgroundImage.ImagePlacement and call its members.
var instance = new dnSpy.Contracts.BackgroundImage.ImagePlacement(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/BackgroundImage/ImagePlacement.cs` (line 24)

### Members

- `TopLeft`: Top left corner
- `TopRight`: Top right corner
- `BottomLeft`: Bottom left corner
- `BottomRight`: Bottom right corner
- `Top`: Top
- `Left`: Left
- `Right`: Right
- `Bottom`: Bottom
- `Center`: Center

