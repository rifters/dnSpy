# Namespace `dnSpy.Contracts.Images`

## Class `DsImage`

Image using to load the correct image depending on DPI, zoom and background color

**Inherits/Implements:** `Image`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Images.DsImage and call its members.
var instance = new dnSpy.Contracts.Images.DsImage(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 29)

### Methods

- `public static Brush GetBackgroundBrush(DependencyObject depo)`
  - Summary: Gets the background brush
  - Parameters:
    - `DependencyObject depo`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Images.DsImage.GetBackgroundBrush(depo: /* DependencyObject */);
    ```
- `public static Color? GetBackgroundColor(DependencyObject depo)`
  - Summary: Gets the background color
  - Parameters:
    - `DependencyObject depo`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Images.DsImage.GetBackgroundColor(depo: /* DependencyObject */);
    ```
- `public static double GetDpi(DependencyObject depo)`
  - Summary: Gets the dpi
  - Parameters:
    - `DependencyObject depo`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Images.DsImage.GetDpi(depo: /* DependencyObject */);
    ```
- `public static double GetZoom(DependencyObject depo)`
  - Summary: Gets the zoom (1.0 == 100%)
  - Parameters:
    - `DependencyObject depo`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Images.DsImage.GetZoom(depo: /* DependencyObject */);
    ```
- `public static void SetBackgroundBrush(DependencyObject depo, Brush value)`
  - Summary: Sets the background brush
  - Parameters:
    - `DependencyObject depo`: Object
    - `Brush value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Images.DsImage.SetBackgroundBrush(depo: /* DependencyObject */, value: /* Brush */);
    ```
- `public static void SetBackgroundColor(DependencyObject depo, Color? value)`
  - Summary: Sets the background color
  - Parameters:
    - `DependencyObject depo`: Object
    - `Color? value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Images.DsImage.SetBackgroundColor(depo: /* DependencyObject */, value: /* Color? */);
    ```
- `public static void SetDpi(DependencyObject depo, double value)`
  - Summary: Sets the dpi
  - Parameters:
    - `DependencyObject depo`: Object
    - `double value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Images.DsImage.SetDpi(depo: /* DependencyObject */, value: /* double */);
    ```
- `public static void SetZoom(DependencyObject depo, double value)`
  - Summary: Sets the zoom (1.0 == 100%)
  - Parameters:
    - `DependencyObject depo`: Object
    - `double value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Images.DsImage.SetZoom(depo: /* DependencyObject */, value: /* double */);
    ```

### Properties

- `public ImageReference ImageReference {
			get => (ImageReference)GetValue(ImageReferenceProperty);
			set => SetValue(ImageReferenceProperty, value);
		}`
  - Summary: Gets/sets the image reference, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageReference;
    ```

### Fields

- `public static readonly DependencyProperty BackgroundBrushProperty = DependencyProperty.RegisterAttached("BackgroundBrush", typeof(Brush), typeof(DsImage),
			new FrameworkPropertyMetadata(null, FrameworkPropertyMetadataOptions.Inherits))`
  - Summary: Background brush attached property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 72)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImage.BackgroundBrushProperty;
    ```
- `public static readonly DependencyProperty BackgroundColorProperty = DependencyProperty.RegisterAttached("BackgroundColor", typeof(Color?), typeof(DsImage),
			new FrameworkPropertyMetadata(null, FrameworkPropertyMetadataOptions.Inherits))`
  - Summary: Background color attached property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImage.BackgroundColorProperty;
    ```
- `public static readonly DependencyProperty DpiProperty = DependencyProperty.RegisterAttached("Dpi", typeof(double), typeof(DsImage),
			new FrameworkPropertyMetadata(0.0, FrameworkPropertyMetadataOptions.Inherits))`
  - Summary: Dpi attached property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 116)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImage.DpiProperty;
    ```
- `public static readonly DependencyProperty ImageReferenceProperty = DependencyProperty.Register(nameof(ImageReference), typeof(ImageReference), typeof(DsImage),
			new FrameworkPropertyMetadata(default(ImageReference)))`
  - Summary: dependency property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImage.ImageReferenceProperty;
    ```
- `public static readonly DependencyProperty ZoomProperty = DependencyProperty.RegisterAttached("Zoom", typeof(double), typeof(DsImage),
			new FrameworkPropertyMetadata(0.0, FrameworkPropertyMetadataOptions.Inherits))`
  - Summary: Zoom attached property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImage.cs` (line 94)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImage.ZoomProperty;
    ```

## Class `DsImages`

Image references to images used by dnSpy

**Example**

```csharp
// Access dnSpy.Contracts.Images.DsImages members directly without instantiation.
dnSpy.Contracts.Images.DsImages./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 26)

### Properties

- `public static ImageReference Add { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Add;
    ```
- `public static ImageReference AddReference { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.AddReference;
    ```
- `public static ImageReference AdvancedBreakpointDisabled { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.AdvancedBreakpointDisabled;
    ```
- `public static ImageReference AdvancedBreakpointEnabled { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.AdvancedBreakpointEnabled;
    ```
- `public static ImageReference AdvancedTracepointDisabled { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.AdvancedTracepointDisabled;
    ```
- `public static ImageReference AdvancedTracepointEnabled { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.AdvancedTracepointEnabled;
    ```
- `public static ImageReference Assembly { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Assembly;
    ```
- `public static ImageReference AssemblyError { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.AssemblyError;
    ```
- `public static ImageReference AssemblyExe { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.AssemblyExe;
    ```
- `public static ImageReference AutoSizeOptimize { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.AutoSizeOptimize;
    ```
- `public static ImageReference AutosWindow { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.AutosWindow;
    ```
- `public static ImageReference Backwards { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Backwards;
    ```
- `public static ImageReference Binary { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Binary;
    ```
- `public static ImageReference BinaryFile { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BinaryFile;
    ```
- `public static ImageReference Bookmark { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Bookmark;
    ```
- `public static ImageReference BookmarkDisabled { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BookmarkDisabled;
    ```
- `public static ImageReference BookmarkGroupDisabled { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BookmarkGroupDisabled;
    ```
- `public static ImageReference BookmarkMainMenuItem { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BookmarkMainMenuItem;
    ```
- `public static ImageReference BoundBreakpoint { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BoundBreakpoint;
    ```
- `public static ImageReference Branch { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Branch;
    ```
- `public static ImageReference BreakpointDisabled { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BreakpointDisabled;
    ```
- `public static ImageReference BreakpointEnabled { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BreakpointEnabled;
    ```
- `public static ImageReference BreakpointError { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BreakpointError;
    ```
- `public static ImageReference BreakpointWarning { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BreakpointWarning;
    ```
- `public static ImageReference BreakpointsWindow { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BreakpointsWindow;
    ```
- `public static ImageReference BuildSolution { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.BuildSolution;
    ```
- `public static ImageReference CSFileNode { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CSFileNode;
    ```
- `public static ImageReference CSInteractiveWindow { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CSInteractiveWindow;
    ```
- `public static ImageReference CSProjectNode { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CSProjectNode;
    ```
- `public static ImageReference CallReturnInstructionPointer { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CallReturnInstructionPointer;
    ```
- `public static ImageReference CallReturnInstructionPointerAlert { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CallReturnInstructionPointerAlert;
    ```
- `public static ImageReference CallStackWindow { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CallStackWindow;
    ```
- `public static ImageReference Cancel { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Cancel;
    ```
- `public static ImageReference CheckDot { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CheckDot;
    ```
- `public static ImageReference ClassInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ClassInternal;
    ```
- `public static ImageReference ClassPrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ClassPrivate;
    ```
- `public static ImageReference ClassProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ClassProtected;
    ```
- `public static ImageReference ClassPublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ClassPublic;
    ```
- `public static ImageReference ClassShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ClassShortcut;
    ```
- `public static ImageReference ClearBookmark { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ClearBookmark;
    ```
- `public static ImageReference ClearBreakpointGroup { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ClearBreakpointGroup;
    ```
- `public static ImageReference ClearWindowContent { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ClearWindowContent;
    ```
- `public static ImageReference CloseAll { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CloseAll;
    ```
- `public static ImageReference CloseDocumentGroup { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CloseDocumentGroup;
    ```
- `public static ImageReference CloseSolution { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CloseSolution;
    ```
- `public static ImageReference ConstantInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ConstantInternal;
    ```
- `public static ImageReference ConstantPrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ConstantPrivate;
    ```
- `public static ImageReference ConstantProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ConstantProtected;
    ```
- `public static ImageReference ConstantPublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ConstantPublic;
    ```
- `public static ImageReference ConstantSealed { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ConstantSealed;
    ```
- `public static ImageReference ConstantShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ConstantShortcut;
    ```
- `public static ImageReference Copy { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Copy;
    ```
- `public static ImageReference CopyItem { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 79)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CopyItem;
    ```
- `public static ImageReference CurrentInstructionPointer { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CurrentInstructionPointer;
    ```
- `public static ImageReference CurrentInstructionPointerPaused { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CurrentInstructionPointerPaused;
    ```
- `public static ImageReference CurrentInstructionPointerStopped { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 85)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.CurrentInstructionPointerStopped;
    ```
- `public static ImageReference Cursor { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Cursor;
    ```
- `public static ImageReference Cut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Cut;
    ```
- `public static ImageReference DelegateInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DelegateInternal;
    ```
- `public static ImageReference DelegatePrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 89)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DelegatePrivate;
    ```
- `public static ImageReference DelegateProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 90)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DelegateProtected;
    ```
- `public static ImageReference DelegatePublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DelegatePublic;
    ```
- `public static ImageReference DelegateShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DelegateShortcut;
    ```
- `public static ImageReference DeleteBreakpoint { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DeleteBreakpoint;
    ```
- `public static ImageReference DeleteWatch { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DeleteWatch;
    ```
- `public static ImageReference Dialog { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 95)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Dialog;
    ```
- `public static ImageReference DisableAllBreakpoints { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DisableAllBreakpoints;
    ```
- `public static ImageReference DisassemblyWindow { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DisassemblyWindow;
    ```
- `public static ImageReference DownloadNoColor { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 98)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DownloadNoColor;
    ```
- `public static ImageReference DraggedCurrentInstructionPointer { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 99)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DraggedCurrentInstructionPointer;
    ```
- `public static ImageReference DraggedInstructionPointerPaused { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 100)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.DraggedInstructionPointerPaused;
    ```
- `public static ImageReference Edit { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Edit;
    ```
- `public static ImageReference Editor { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Editor;
    ```
- `public static ImageReference EnableAllBreakpoints { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 103)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnableAllBreakpoints;
    ```
- `public static ImageReference EntryPoint { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 104)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EntryPoint;
    ```
- `public static ImageReference EnumerationInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 105)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationInternal;
    ```
- `public static ImageReference EnumerationItemInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationItemInternal;
    ```
- `public static ImageReference EnumerationItemPrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationItemPrivate;
    ```
- `public static ImageReference EnumerationItemProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 108)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationItemProtected;
    ```
- `public static ImageReference EnumerationItemPublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 109)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationItemPublic;
    ```
- `public static ImageReference EnumerationItemSealed { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 110)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationItemSealed;
    ```
- `public static ImageReference EnumerationItemShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationItemShortcut;
    ```
- `public static ImageReference EnumerationPrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 112)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationPrivate;
    ```
- `public static ImageReference EnumerationProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 113)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationProtected;
    ```
- `public static ImageReference EnumerationPublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 114)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationPublic;
    ```
- `public static ImageReference EnumerationShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 115)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EnumerationShortcut;
    ```
- `public static ImageReference EventInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EventInternal;
    ```
- `public static ImageReference EventPrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 117)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EventPrivate;
    ```
- `public static ImageReference EventProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 118)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EventProtected;
    ```
- `public static ImageReference EventPublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 119)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EventPublic;
    ```
- `public static ImageReference EventSealed { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 120)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EventSealed;
    ```
- `public static ImageReference EventShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 121)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.EventShortcut;
    ```
- `public static ImageReference ExceptionInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 122)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ExceptionInternal;
    ```
- `public static ImageReference ExceptionPrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 123)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ExceptionPrivate;
    ```
- `public static ImageReference ExceptionProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 124)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ExceptionProtected;
    ```
- `public static ImageReference ExceptionPublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 125)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ExceptionPublic;
    ```
- `public static ImageReference ExceptionSettings { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 126)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ExceptionSettings;
    ```
- `public static ImageReference ExceptionShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 127)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ExceptionShortcut;
    ```
- `public static ImageReference ExtensionMethod { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 128)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ExtensionMethod;
    ```
- `public static ImageReference FieldInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.FieldInternal;
    ```
- `public static ImageReference FieldPrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 130)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.FieldPrivate;
    ```
- `public static ImageReference FieldProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 131)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.FieldProtected;
    ```
- `public static ImageReference FieldPublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 132)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.FieldPublic;
    ```
- `public static ImageReference FieldSealed { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 133)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.FieldSealed;
    ```
- `public static ImageReference FieldShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.FieldShortcut;
    ```
- `public static ImageReference FileSystemWatcher { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 135)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.FileSystemWatcher;
    ```
- `public static ImageReference Fill { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 136)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Fill;
    ```
- `public static ImageReference Filter { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 137)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Filter;
    ```
- `public static ImageReference FolderClosed { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 138)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.FolderClosed;
    ```
- `public static ImageReference FolderOpened { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 139)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.FolderOpened;
    ```
- `public static ImageReference Forwards { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 140)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Forwards;
    ```
- `public static ImageReference GoToNext { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 141)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.GoToNext;
    ```
- `public static ImageReference GoToNextInList { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 142)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.GoToNextInList;
    ```
- `public static ImageReference GoToSourceCode { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 143)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.GoToSourceCode;
    ```
- `public static ImageReference Image { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 144)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Image;
    ```
- `public static ImageReference Import { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 145)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Import;
    ```
- `public static ImageReference IntellisenseKeyword { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 146)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.IntellisenseKeyword;
    ```
- `public static ImageReference InterfaceInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 147)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.InterfaceInternal;
    ```
- `public static ImageReference InterfacePrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 148)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.InterfacePrivate;
    ```
- `public static ImageReference InterfaceProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 149)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.InterfaceProtected;
    ```
- `public static ImageReference InterfacePublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 150)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.InterfacePublic;
    ```
- `public static ImageReference InterfaceShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 151)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.InterfaceShortcut;
    ```
- `public static ImageReference Label { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 152)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Label;
    ```
- `public static ImageReference Library { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 153)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Library;
    ```
- `public static ImageReference LocalVariable { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 155)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.LocalVariable;
    ```
- `public static ImageReference LocalsWindow { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 154)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.LocalsWindow;
    ```
- `public static ImageReference MarkupTag { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 156)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.MarkupTag;
    ```
- `public static ImageReference MemoryWindow { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 157)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.MemoryWindow;
    ```
- `public static ImageReference Metadata { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 158)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Metadata;
    ```
- `public static ImageReference MethodInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 159)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.MethodInternal;
    ```
- `public static ImageReference MethodPrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 160)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.MethodPrivate;
    ```
- `public static ImageReference MethodProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 161)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.MethodProtected;
    ```
- `public static ImageReference MethodPublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 162)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.MethodPublic;
    ```
- `public static ImageReference MethodSealed { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 163)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.MethodSealed;
    ```
- `public static ImageReference MethodShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 164)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.MethodShortcut;
    ```
- `public static ImageReference ModuleFile { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 165)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ModuleFile;
    ```
- `public static ImageReference ModuleInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 166)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ModuleInternal;
    ```
- `public static ImageReference ModulePrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 167)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ModulePrivate;
    ```
- `public static ImageReference ModuleProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 168)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ModuleProtected;
    ```
- `public static ImageReference ModulePublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 169)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ModulePublic;
    ```
- `public static ImageReference ModulesWindow { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 170)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ModulesWindow;
    ```
- `public static ImageReference MoveUp { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 171)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.MoveUp;
    ```
- `public static ImageReference Namespace { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 172)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Namespace;
    ```
- `public static ImageReference NewClass { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 173)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NewClass;
    ```
- `public static ImageReference NewDocument { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 174)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NewDocument;
    ```
- `public static ImageReference NewEvent { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 175)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NewEvent;
    ```
- `public static ImageReference NewField { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 176)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NewField;
    ```
- `public static ImageReference NewImage { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 177)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NewImage;
    ```
- `public static ImageReference NewItem { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 178)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NewItem;
    ```
- `public static ImageReference NewMethod { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 179)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NewMethod;
    ```
- `public static ImageReference NewProperty { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 180)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NewProperty;
    ```
- `public static ImageReference NewWindow { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 181)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NewWindow;
    ```
- `public static ImageReference NextBookmark { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 182)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NextBookmark;
    ```
- `public static ImageReference NextBookmarkInFile { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 183)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NextBookmarkInFile;
    ```
- `public static ImageReference NextBookmarkInFolder { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 184)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NextBookmarkInFolder;
    ```
- `public static ImageReference NuGet { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 185)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.NuGet;
    ```
- `public static ImageReference OneLevelUp { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 186)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.OneLevelUp;
    ```
- `public static ImageReference Open { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 187)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Open;
    ```
- `public static ImageReference OpenFolder { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 188)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.OpenFolder;
    ```
- `public static ImageReference OperatorInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 189)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.OperatorInternal;
    ```
- `public static ImageReference OperatorPrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 190)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.OperatorPrivate;
    ```
- `public static ImageReference OperatorProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 191)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.OperatorProtected;
    ```
- `public static ImageReference OperatorPublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 192)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.OperatorPublic;
    ```
- `public static ImageReference OperatorSealed { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 193)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.OperatorSealed;
    ```
- `public static ImageReference OperatorShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 194)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.OperatorShortcut;
    ```
- `public static ImageReference Output { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 195)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Output;
    ```
- `public static ImageReference Parameter { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 196)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Parameter;
    ```
- `public static ImageReference Paste { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 197)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Paste;
    ```
- `public static ImageReference Pause { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 198)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Pause;
    ```
- `public static ImageReference PreviousBookmark { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 199)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.PreviousBookmark;
    ```
- `public static ImageReference PreviousBookmarkInFile { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 200)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.PreviousBookmarkInFile;
    ```
- `public static ImageReference PreviousBookmarkInFolder { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 201)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.PreviousBookmarkInFolder;
    ```
- `public static ImageReference Process { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 202)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Process;
    ```
- `public static ImageReference Property { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 203)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Property;
    ```
- `public static ImageReference PropertyInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 204)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.PropertyInternal;
    ```
- `public static ImageReference PropertyPrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 205)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.PropertyPrivate;
    ```
- `public static ImageReference PropertyProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 206)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.PropertyProtected;
    ```
- `public static ImageReference PropertySealed { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 207)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.PropertySealed;
    ```
- `public static ImageReference PropertyShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 208)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.PropertyShortcut;
    ```
- `public static ImageReference QuestionMark { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 209)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.QuestionMark;
    ```
- `public static ImageReference Redo { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 210)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Redo;
    ```
- `public static ImageReference Reference { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 211)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Reference;
    ```
- `public static ImageReference Refresh { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 212)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Refresh;
    ```
- `public static ImageReference RemoveCommand { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 213)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.RemoveCommand;
    ```
- `public static ImageReference Restart { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 214)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Restart;
    ```
- `public static ImageReference Run { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 215)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Run;
    ```
- `public static ImageReference RunOutline { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 216)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.RunOutline;
    ```
- `public static ImageReference Save { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 217)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Save;
    ```
- `public static ImageReference SaveAll { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 218)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.SaveAll;
    ```
- `public static ImageReference Search { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 219)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Search;
    ```
- `public static ImageReference Select { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 220)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Select;
    ```
- `public static ImageReference Settings { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 221)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Settings;
    ```
- `public static ImageReference Snippet { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 222)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Snippet;
    ```
- `public static ImageReference Solution { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 223)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Solution;
    ```
- `public static ImageReference SortAscending { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 224)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.SortAscending;
    ```
- `public static ImageReference SourceFileGroup { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 225)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.SourceFileGroup;
    ```
- `public static ImageReference SplitScreenHorizontally { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 226)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.SplitScreenHorizontally;
    ```
- `public static ImageReference SplitScreenVertically { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 227)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.SplitScreenVertically;
    ```
- `public static ImageReference StatusError { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 228)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StatusError;
    ```
- `public static ImageReference StatusHelp { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 229)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StatusHelp;
    ```
- `public static ImageReference StatusHidden { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 230)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StatusHidden;
    ```
- `public static ImageReference StatusInformation { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 231)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StatusInformation;
    ```
- `public static ImageReference StatusWarning { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 232)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StatusWarning;
    ```
- `public static ImageReference StepInto { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 233)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StepInto;
    ```
- `public static ImageReference StepOut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 234)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StepOut;
    ```
- `public static ImageReference StepOver { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 235)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StepOver;
    ```
- `public static ImageReference Stop { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 236)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Stop;
    ```
- `public static ImageReference String { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 237)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.String;
    ```
- `public static ImageReference StructureInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 238)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StructureInternal;
    ```
- `public static ImageReference StructurePrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 239)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StructurePrivate;
    ```
- `public static ImageReference StructureProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 240)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StructureProtected;
    ```
- `public static ImageReference StructurePublic { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 241)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StructurePublic;
    ```
- `public static ImageReference StructureShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 242)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.StructureShortcut;
    ```
- `public static ImageReference TableViewNameOnly { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 243)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TableViewNameOnly;
    ```
- `public static ImageReference Template { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 244)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Template;
    ```
- `public static ImageReference TemplateInternal { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 245)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TemplateInternal;
    ```
- `public static ImageReference TemplatePrivate { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 246)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TemplatePrivate;
    ```
- `public static ImageReference TemplateProtected { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 247)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TemplateProtected;
    ```
- `public static ImageReference TemplateShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 248)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TemplateShortcut;
    ```
- `public static ImageReference TerminateProcess { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 249)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TerminateProcess;
    ```
- `public static ImageReference TextFile { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 250)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TextFile;
    ```
- `public static ImageReference Thread { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 251)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Thread;
    ```
- `public static ImageReference ToggleAllBreakpoints { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 252)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ToggleAllBreakpoints;
    ```
- `public static ImageReference ToolstripPanelBottom { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 253)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ToolstripPanelBottom;
    ```
- `public static ImageReference ToolstripPanelLeft { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 254)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ToolstripPanelLeft;
    ```
- `public static ImageReference ToolstripPanelRight { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 255)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ToolstripPanelRight;
    ```
- `public static ImageReference ToolstripPanelTop { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 256)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.ToolstripPanelTop;
    ```
- `public static ImageReference TracepointDisabled { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 257)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TracepointDisabled;
    ```
- `public static ImageReference TracepointEnabled { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 258)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TracepointEnabled;
    ```
- `public static ImageReference TracepointError { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 259)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TracepointError;
    ```
- `public static ImageReference TracepointWarning { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 260)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.TracepointWarning;
    ```
- `public static ImageReference Type { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 261)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Type;
    ```
- `public static ImageReference Undo { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 262)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Undo;
    ```
- `public static ImageReference UndoCheckBoxList { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 263)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.UndoCheckBoxList;
    ```
- `public static ImageReference UserDefinedDataType { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 264)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.UserDefinedDataType;
    ```
- `public static ImageReference VBFileNode { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 265)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.VBFileNode;
    ```
- `public static ImageReference VBInteractiveWindow { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 266)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.VBInteractiveWindow;
    ```
- `public static ImageReference VBProjectNode { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 267)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.VBProjectNode;
    ```
- `public static ImageReference WPFFile { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 270)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.WPFFile;
    ```
- `public static ImageReference Watch { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 268)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.Watch;
    ```
- `public static ImageReference WordWrap { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 269)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.WordWrap;
    ```
- `public static ImageReference XMLFile { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 271)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.XMLFile;
    ```
- `public static ImageReference XMLSchema { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 272)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.XMLSchema;
    ```
- `public static ImageReference XSLTransform { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImages.cs` (line 273)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Images.DsImages.XSLTransform;
    ```

## Class `DsImagesAttribute`

Contains image reference strings that can be used in attributes, eg. menu item attributes

**Example**

```csharp
// Access dnSpy.Contracts.Images.DsImagesAttribute members directly without instantiation.
dnSpy.Contracts.Images.DsImagesAttribute./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 24)

### Fields

- `public const string Add = Prefix + DsImageStrings.Add`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Add;
    ```
- `public const string AddReference = Prefix + DsImageStrings.AddReference`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.AddReference;
    ```
- `public const string AdvancedBreakpointDisabled = Prefix + DsImageStrings.AdvancedBreakpointDisabled`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.AdvancedBreakpointDisabled;
    ```
- `public const string AdvancedBreakpointEnabled = Prefix + DsImageStrings.AdvancedBreakpointEnabled`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.AdvancedBreakpointEnabled;
    ```
- `public const string AdvancedTracepointDisabled = Prefix + DsImageStrings.AdvancedTracepointDisabled`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.AdvancedTracepointDisabled;
    ```
- `public const string AdvancedTracepointEnabled = Prefix + DsImageStrings.AdvancedTracepointEnabled`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.AdvancedTracepointEnabled;
    ```
- `public const string Assembly = Prefix + DsImageStrings.Assembly`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Assembly;
    ```
- `public const string AssemblyError = Prefix + DsImageStrings.AssemblyError`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.AssemblyError;
    ```
- `public const string AssemblyExe = Prefix + DsImageStrings.AssemblyExe`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.AssemblyExe;
    ```
- `public const string AutoSizeOptimize = Prefix + DsImageStrings.AutoSizeOptimize`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.AutoSizeOptimize;
    ```
- `public const string AutosWindow = Prefix + DsImageStrings.AutosWindow`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.AutosWindow;
    ```
- `public const string Backwards = Prefix + DsImageStrings.Backwards`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Backwards;
    ```
- `public const string Binary = Prefix + DsImageStrings.Binary`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Binary;
    ```
- `public const string BinaryFile = Prefix + DsImageStrings.BinaryFile`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BinaryFile;
    ```
- `public const string Bookmark = Prefix + DsImageStrings.Bookmark`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Bookmark;
    ```
- `public const string BookmarkDisabled = Prefix + DsImageStrings.BookmarkDisabled`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BookmarkDisabled;
    ```
- `public const string BookmarkGroupDisabled = Prefix + DsImageStrings.BookmarkGroupDisabled`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BookmarkGroupDisabled;
    ```
- `public const string BookmarkMainMenuItem = Prefix + DsImageStrings.BookmarkMainMenuItem`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BookmarkMainMenuItem;
    ```
- `public const string BoundBreakpoint = Prefix + DsImageStrings.BoundBreakpoint`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 45)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BoundBreakpoint;
    ```
- `public const string Branch = Prefix + DsImageStrings.Branch`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Branch;
    ```
- `public const string BreakpointDisabled = Prefix + DsImageStrings.BreakpointDisabled`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BreakpointDisabled;
    ```
- `public const string BreakpointEnabled = Prefix + DsImageStrings.BreakpointEnabled`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BreakpointEnabled;
    ```
- `public const string BreakpointError = Prefix + DsImageStrings.BreakpointError`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BreakpointError;
    ```
- `public const string BreakpointWarning = Prefix + DsImageStrings.BreakpointWarning`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 51)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BreakpointWarning;
    ```
- `public const string BreakpointsWindow = Prefix + DsImageStrings.BreakpointsWindow`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BreakpointsWindow;
    ```
- `public const string BuildSolution = Prefix + DsImageStrings.BuildSolution`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.BuildSolution;
    ```
- `public const string CSFileNode = Prefix + DsImageStrings.CSFileNode`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 77)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CSFileNode;
    ```
- `public const string CSInteractiveWindow = Prefix + DsImageStrings.CSInteractiveWindow`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 78)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CSInteractiveWindow;
    ```
- `public const string CSProjectNode = Prefix + DsImageStrings.CSProjectNode`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 79)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CSProjectNode;
    ```
- `public const string CallReturnInstructionPointer = Prefix + DsImageStrings.CallReturnInstructionPointer`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CallReturnInstructionPointer;
    ```
- `public const string CallReturnInstructionPointerAlert = Prefix + DsImageStrings.CallReturnInstructionPointerAlert`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 54)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CallReturnInstructionPointerAlert;
    ```
- `public const string CallStackWindow = Prefix + DsImageStrings.CallStackWindow`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CallStackWindow;
    ```
- `public const string Cancel = Prefix + DsImageStrings.Cancel`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Cancel;
    ```
- `public const string CheckDot = Prefix + DsImageStrings.CheckDot`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 57)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CheckDot;
    ```
- `public const string ClassInternal = Prefix + DsImageStrings.ClassInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ClassInternal;
    ```
- `public const string ClassPrivate = Prefix + DsImageStrings.ClassPrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 59)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ClassPrivate;
    ```
- `public const string ClassProtected = Prefix + DsImageStrings.ClassProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 60)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ClassProtected;
    ```
- `public const string ClassPublic = Prefix + DsImageStrings.ClassPublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 61)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ClassPublic;
    ```
- `public const string ClassShortcut = Prefix + DsImageStrings.ClassShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 62)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ClassShortcut;
    ```
- `public const string ClearBookmark = Prefix + DsImageStrings.ClearBookmark`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ClearBookmark;
    ```
- `public const string ClearBreakpointGroup = Prefix + DsImageStrings.ClearBreakpointGroup`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 64)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ClearBreakpointGroup;
    ```
- `public const string ClearWindowContent = Prefix + DsImageStrings.ClearWindowContent`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 65)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ClearWindowContent;
    ```
- `public const string CloseAll = Prefix + DsImageStrings.CloseAll`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 66)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CloseAll;
    ```
- `public const string CloseDocumentGroup = Prefix + DsImageStrings.CloseDocumentGroup`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 67)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CloseDocumentGroup;
    ```
- `public const string CloseSolution = Prefix + DsImageStrings.CloseSolution`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CloseSolution;
    ```
- `public const string ConstantInternal = Prefix + DsImageStrings.ConstantInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 69)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ConstantInternal;
    ```
- `public const string ConstantPrivate = Prefix + DsImageStrings.ConstantPrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 70)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ConstantPrivate;
    ```
- `public const string ConstantProtected = Prefix + DsImageStrings.ConstantProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 71)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ConstantProtected;
    ```
- `public const string ConstantPublic = Prefix + DsImageStrings.ConstantPublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 72)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ConstantPublic;
    ```
- `public const string ConstantSealed = Prefix + DsImageStrings.ConstantSealed`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ConstantSealed;
    ```
- `public const string ConstantShortcut = Prefix + DsImageStrings.ConstantShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 74)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ConstantShortcut;
    ```
- `public const string Copy = Prefix + DsImageStrings.Copy`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 75)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Copy;
    ```
- `public const string CopyItem = Prefix + DsImageStrings.CopyItem`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 76)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CopyItem;
    ```
- `public const string CurrentInstructionPointer = Prefix + DsImageStrings.CurrentInstructionPointer`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 80)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CurrentInstructionPointer;
    ```
- `public const string CurrentInstructionPointerPaused = Prefix + DsImageStrings.CurrentInstructionPointerPaused`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 81)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CurrentInstructionPointerPaused;
    ```
- `public const string CurrentInstructionPointerStopped = Prefix + DsImageStrings.CurrentInstructionPointerStopped`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 82)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.CurrentInstructionPointerStopped;
    ```
- `public const string Cursor = Prefix + DsImageStrings.Cursor`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 83)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Cursor;
    ```
- `public const string Cut = Prefix + DsImageStrings.Cut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 84)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Cut;
    ```
- `public const string DelegateInternal = Prefix + DsImageStrings.DelegateInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 85)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DelegateInternal;
    ```
- `public const string DelegatePrivate = Prefix + DsImageStrings.DelegatePrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 86)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DelegatePrivate;
    ```
- `public const string DelegateProtected = Prefix + DsImageStrings.DelegateProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 87)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DelegateProtected;
    ```
- `public const string DelegatePublic = Prefix + DsImageStrings.DelegatePublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DelegatePublic;
    ```
- `public const string DelegateShortcut = Prefix + DsImageStrings.DelegateShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 89)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DelegateShortcut;
    ```
- `public const string DeleteBreakpoint = Prefix + DsImageStrings.DeleteBreakpoint`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 90)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DeleteBreakpoint;
    ```
- `public const string DeleteWatch = Prefix + DsImageStrings.DeleteWatch`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 91)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DeleteWatch;
    ```
- `public const string Dialog = Prefix + DsImageStrings.Dialog`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 92)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Dialog;
    ```
- `public const string DisableAllBreakpoints = Prefix + DsImageStrings.DisableAllBreakpoints`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 93)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DisableAllBreakpoints;
    ```
- `public const string DisassemblyWindow = Prefix + DsImageStrings.DisassemblyWindow`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 94)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DisassemblyWindow;
    ```
- `public const string DownloadNoColor = Prefix + DsImageStrings.DownloadNoColor`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 95)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DownloadNoColor;
    ```
- `public const string DraggedCurrentInstructionPointer = Prefix + DsImageStrings.DraggedCurrentInstructionPointer`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 96)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DraggedCurrentInstructionPointer;
    ```
- `public const string DraggedInstructionPointerPaused = Prefix + DsImageStrings.DraggedInstructionPointerPaused`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 97)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.DraggedInstructionPointerPaused;
    ```
- `public const string Edit = Prefix + DsImageStrings.Edit`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 98)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Edit;
    ```
- `public const string Editor = Prefix + DsImageStrings.Editor`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 99)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Editor;
    ```
- `public const string EnableAllBreakpoints = Prefix + DsImageStrings.EnableAllBreakpoints`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 100)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnableAllBreakpoints;
    ```
- `public const string EntryPoint = Prefix + DsImageStrings.EntryPoint`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 101)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EntryPoint;
    ```
- `public const string EnumerationInternal = Prefix + DsImageStrings.EnumerationInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 102)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationInternal;
    ```
- `public const string EnumerationItemInternal = Prefix + DsImageStrings.EnumerationItemInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 103)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationItemInternal;
    ```
- `public const string EnumerationItemPrivate = Prefix + DsImageStrings.EnumerationItemPrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 104)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationItemPrivate;
    ```
- `public const string EnumerationItemProtected = Prefix + DsImageStrings.EnumerationItemProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 105)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationItemProtected;
    ```
- `public const string EnumerationItemPublic = Prefix + DsImageStrings.EnumerationItemPublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 106)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationItemPublic;
    ```
- `public const string EnumerationItemSealed = Prefix + DsImageStrings.EnumerationItemSealed`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 107)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationItemSealed;
    ```
- `public const string EnumerationItemShortcut = Prefix + DsImageStrings.EnumerationItemShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 108)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationItemShortcut;
    ```
- `public const string EnumerationPrivate = Prefix + DsImageStrings.EnumerationPrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 109)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationPrivate;
    ```
- `public const string EnumerationProtected = Prefix + DsImageStrings.EnumerationProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 110)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationProtected;
    ```
- `public const string EnumerationPublic = Prefix + DsImageStrings.EnumerationPublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 111)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationPublic;
    ```
- `public const string EnumerationShortcut = Prefix + DsImageStrings.EnumerationShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 112)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EnumerationShortcut;
    ```
- `public const string EventInternal = Prefix + DsImageStrings.EventInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 113)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EventInternal;
    ```
- `public const string EventPrivate = Prefix + DsImageStrings.EventPrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 114)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EventPrivate;
    ```
- `public const string EventProtected = Prefix + DsImageStrings.EventProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 115)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EventProtected;
    ```
- `public const string EventPublic = Prefix + DsImageStrings.EventPublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 116)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EventPublic;
    ```
- `public const string EventSealed = Prefix + DsImageStrings.EventSealed`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 117)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EventSealed;
    ```
- `public const string EventShortcut = Prefix + DsImageStrings.EventShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 118)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.EventShortcut;
    ```
- `public const string ExceptionInternal = Prefix + DsImageStrings.ExceptionInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 119)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ExceptionInternal;
    ```
- `public const string ExceptionPrivate = Prefix + DsImageStrings.ExceptionPrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 120)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ExceptionPrivate;
    ```
- `public const string ExceptionProtected = Prefix + DsImageStrings.ExceptionProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 121)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ExceptionProtected;
    ```
- `public const string ExceptionPublic = Prefix + DsImageStrings.ExceptionPublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 122)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ExceptionPublic;
    ```
- `public const string ExceptionSettings = Prefix + DsImageStrings.ExceptionSettings`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 123)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ExceptionSettings;
    ```
- `public const string ExceptionShortcut = Prefix + DsImageStrings.ExceptionShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 124)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ExceptionShortcut;
    ```
- `public const string ExtensionMethod = Prefix + DsImageStrings.ExtensionMethod`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 125)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ExtensionMethod;
    ```
- `public const string FieldInternal = Prefix + DsImageStrings.FieldInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 126)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.FieldInternal;
    ```
- `public const string FieldPrivate = Prefix + DsImageStrings.FieldPrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 127)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.FieldPrivate;
    ```
- `public const string FieldProtected = Prefix + DsImageStrings.FieldProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 128)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.FieldProtected;
    ```
- `public const string FieldPublic = Prefix + DsImageStrings.FieldPublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 129)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.FieldPublic;
    ```
- `public const string FieldSealed = Prefix + DsImageStrings.FieldSealed`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 130)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.FieldSealed;
    ```
- `public const string FieldShortcut = Prefix + DsImageStrings.FieldShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 131)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.FieldShortcut;
    ```
- `public const string FileSystemWatcher = Prefix + DsImageStrings.FileSystemWatcher`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 132)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.FileSystemWatcher;
    ```
- `public const string Fill = Prefix + DsImageStrings.Fill`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 133)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Fill;
    ```
- `public const string Filter = Prefix + DsImageStrings.Filter`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 134)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Filter;
    ```
- `public const string FolderClosed = Prefix + DsImageStrings.FolderClosed`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 135)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.FolderClosed;
    ```
- `public const string FolderOpened = Prefix + DsImageStrings.FolderOpened`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 136)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.FolderOpened;
    ```
- `public const string Forwards = Prefix + DsImageStrings.Forwards`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 137)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Forwards;
    ```
- `public const string GoToNext = Prefix + DsImageStrings.GoToNext`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 138)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.GoToNext;
    ```
- `public const string GoToNextInList = Prefix + DsImageStrings.GoToNextInList`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 139)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.GoToNextInList;
    ```
- `public const string GoToSourceCode = Prefix + DsImageStrings.GoToSourceCode`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 140)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.GoToSourceCode;
    ```
- `public const string Image = Prefix + DsImageStrings.Image`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 141)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Image;
    ```
- `public const string Import = Prefix + DsImageStrings.Import`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 142)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Import;
    ```
- `public const string IntellisenseKeyword = Prefix + DsImageStrings.IntellisenseKeyword`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 143)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.IntellisenseKeyword;
    ```
- `public const string InterfaceInternal = Prefix + DsImageStrings.InterfaceInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 144)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.InterfaceInternal;
    ```
- `public const string InterfacePrivate = Prefix + DsImageStrings.InterfacePrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 145)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.InterfacePrivate;
    ```
- `public const string InterfaceProtected = Prefix + DsImageStrings.InterfaceProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 146)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.InterfaceProtected;
    ```
- `public const string InterfacePublic = Prefix + DsImageStrings.InterfacePublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 147)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.InterfacePublic;
    ```
- `public const string InterfaceShortcut = Prefix + DsImageStrings.InterfaceShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 148)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.InterfaceShortcut;
    ```
- `public const string Label = Prefix + DsImageStrings.Label`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 149)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Label;
    ```
- `public const string Library = Prefix + DsImageStrings.Library`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 150)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Library;
    ```
- `public const string LocalVariable = Prefix + DsImageStrings.LocalVariable`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 152)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.LocalVariable;
    ```
- `public const string LocalsWindow = Prefix + DsImageStrings.LocalsWindow`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 151)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.LocalsWindow;
    ```
- `public const string MarkupTag = Prefix + DsImageStrings.MarkupTag`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 153)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.MarkupTag;
    ```
- `public const string MemoryWindow = Prefix + DsImageStrings.MemoryWindow`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 154)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.MemoryWindow;
    ```
- `public const string Metadata = Prefix + DsImageStrings.Metadata`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 155)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Metadata;
    ```
- `public const string MethodInternal = Prefix + DsImageStrings.MethodInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 156)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.MethodInternal;
    ```
- `public const string MethodPrivate = Prefix + DsImageStrings.MethodPrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 157)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.MethodPrivate;
    ```
- `public const string MethodProtected = Prefix + DsImageStrings.MethodProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 158)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.MethodProtected;
    ```
- `public const string MethodPublic = Prefix + DsImageStrings.MethodPublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 159)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.MethodPublic;
    ```
- `public const string MethodSealed = Prefix + DsImageStrings.MethodSealed`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 160)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.MethodSealed;
    ```
- `public const string MethodShortcut = Prefix + DsImageStrings.MethodShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 161)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.MethodShortcut;
    ```
- `public const string ModuleFile = Prefix + DsImageStrings.ModuleFile`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 162)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ModuleFile;
    ```
- `public const string ModuleInternal = Prefix + DsImageStrings.ModuleInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 163)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ModuleInternal;
    ```
- `public const string ModulePrivate = Prefix + DsImageStrings.ModulePrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 164)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ModulePrivate;
    ```
- `public const string ModuleProtected = Prefix + DsImageStrings.ModuleProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 165)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ModuleProtected;
    ```
- `public const string ModulePublic = Prefix + DsImageStrings.ModulePublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 166)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ModulePublic;
    ```
- `public const string ModulesWindow = Prefix + DsImageStrings.ModulesWindow`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 167)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ModulesWindow;
    ```
- `public const string MoveUp = Prefix + DsImageStrings.MoveUp`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 168)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.MoveUp;
    ```
- `public const string Namespace = Prefix + DsImageStrings.Namespace`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 169)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Namespace;
    ```
- `public const string NewClass = Prefix + DsImageStrings.NewClass`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 170)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NewClass;
    ```
- `public const string NewDocument = Prefix + DsImageStrings.NewDocument`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 171)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NewDocument;
    ```
- `public const string NewEvent = Prefix + DsImageStrings.NewEvent`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 172)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NewEvent;
    ```
- `public const string NewField = Prefix + DsImageStrings.NewField`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 173)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NewField;
    ```
- `public const string NewImage = Prefix + DsImageStrings.NewImage`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 174)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NewImage;
    ```
- `public const string NewItem = Prefix + DsImageStrings.NewItem`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 175)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NewItem;
    ```
- `public const string NewMethod = Prefix + DsImageStrings.NewMethod`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 176)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NewMethod;
    ```
- `public const string NewProperty = Prefix + DsImageStrings.NewProperty`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 177)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NewProperty;
    ```
- `public const string NewWindow = Prefix + DsImageStrings.NewWindow`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 178)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NewWindow;
    ```
- `public const string NextBookmark = Prefix + DsImageStrings.NextBookmark`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 179)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NextBookmark;
    ```
- `public const string NextBookmarkInFile = Prefix + DsImageStrings.NextBookmarkInFile`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 180)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NextBookmarkInFile;
    ```
- `public const string NextBookmarkInFolder = Prefix + DsImageStrings.NextBookmarkInFolder`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 181)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NextBookmarkInFolder;
    ```
- `public const string NuGet = Prefix + DsImageStrings.NuGet`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 182)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.NuGet;
    ```
- `public const string OneLevelUp = Prefix + DsImageStrings.OneLevelUp`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 183)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.OneLevelUp;
    ```
- `public const string Open = Prefix + DsImageStrings.Open`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 184)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Open;
    ```
- `public const string OpenFolder = Prefix + DsImageStrings.OpenFolder`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 185)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.OpenFolder;
    ```
- `public const string OperatorInternal = Prefix + DsImageStrings.OperatorInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 186)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.OperatorInternal;
    ```
- `public const string OperatorPrivate = Prefix + DsImageStrings.OperatorPrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 187)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.OperatorPrivate;
    ```
- `public const string OperatorProtected = Prefix + DsImageStrings.OperatorProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 188)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.OperatorProtected;
    ```
- `public const string OperatorPublic = Prefix + DsImageStrings.OperatorPublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 189)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.OperatorPublic;
    ```
- `public const string OperatorSealed = Prefix + DsImageStrings.OperatorSealed`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 190)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.OperatorSealed;
    ```
- `public const string OperatorShortcut = Prefix + DsImageStrings.OperatorShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 191)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.OperatorShortcut;
    ```
- `public const string Output = Prefix + DsImageStrings.Output`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 192)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Output;
    ```
- `public const string Parameter = Prefix + DsImageStrings.Parameter`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 193)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Parameter;
    ```
- `public const string Paste = Prefix + DsImageStrings.Paste`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 194)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Paste;
    ```
- `public const string Pause = Prefix + DsImageStrings.Pause`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 195)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Pause;
    ```
- `public const string PreviousBookmark = Prefix + DsImageStrings.PreviousBookmark`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 196)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.PreviousBookmark;
    ```
- `public const string PreviousBookmarkInFile = Prefix + DsImageStrings.PreviousBookmarkInFile`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 197)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.PreviousBookmarkInFile;
    ```
- `public const string PreviousBookmarkInFolder = Prefix + DsImageStrings.PreviousBookmarkInFolder`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 198)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.PreviousBookmarkInFolder;
    ```
- `public const string Process = Prefix + DsImageStrings.Process`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 199)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Process;
    ```
- `public const string Property = Prefix + DsImageStrings.Property`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 200)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Property;
    ```
- `public const string PropertyInternal = Prefix + DsImageStrings.PropertyInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 201)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.PropertyInternal;
    ```
- `public const string PropertyPrivate = Prefix + DsImageStrings.PropertyPrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 202)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.PropertyPrivate;
    ```
- `public const string PropertyProtected = Prefix + DsImageStrings.PropertyProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 203)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.PropertyProtected;
    ```
- `public const string PropertySealed = Prefix + DsImageStrings.PropertySealed`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 204)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.PropertySealed;
    ```
- `public const string PropertyShortcut = Prefix + DsImageStrings.PropertyShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 205)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.PropertyShortcut;
    ```
- `public const string QuestionMark = Prefix + DsImageStrings.QuestionMark`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 206)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.QuestionMark;
    ```
- `public const string Redo = Prefix + DsImageStrings.Redo`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 207)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Redo;
    ```
- `public const string Reference = Prefix + DsImageStrings.Reference`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 208)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Reference;
    ```
- `public const string Refresh = Prefix + DsImageStrings.Refresh`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 209)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Refresh;
    ```
- `public const string RemoveCommand = Prefix + DsImageStrings.RemoveCommand`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 210)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.RemoveCommand;
    ```
- `public const string Restart = Prefix + DsImageStrings.Restart`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 211)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Restart;
    ```
- `public const string Run = Prefix + DsImageStrings.Run`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 212)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Run;
    ```
- `public const string RunOutline = Prefix + DsImageStrings.RunOutline`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 213)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.RunOutline;
    ```
- `public const string Save = Prefix + DsImageStrings.Save`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 214)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Save;
    ```
- `public const string SaveAll = Prefix + DsImageStrings.SaveAll`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 215)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.SaveAll;
    ```
- `public const string Search = Prefix + DsImageStrings.Search`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 216)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Search;
    ```
- `public const string Select = Prefix + DsImageStrings.Select`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 217)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Select;
    ```
- `public const string Settings = Prefix + DsImageStrings.Settings`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 218)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Settings;
    ```
- `public const string Snippet = Prefix + DsImageStrings.Snippet`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 219)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Snippet;
    ```
- `public const string Solution = Prefix + DsImageStrings.Solution`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 220)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Solution;
    ```
- `public const string SortAscending = Prefix + DsImageStrings.SortAscending`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 221)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.SortAscending;
    ```
- `public const string SourceFileGroup = Prefix + DsImageStrings.SourceFileGroup`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 222)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.SourceFileGroup;
    ```
- `public const string SplitScreenHorizontally = Prefix + DsImageStrings.SplitScreenHorizontally`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 223)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.SplitScreenHorizontally;
    ```
- `public const string SplitScreenVertically = Prefix + DsImageStrings.SplitScreenVertically`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 224)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.SplitScreenVertically;
    ```
- `public const string StatusError = Prefix + DsImageStrings.StatusError`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 225)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StatusError;
    ```
- `public const string StatusHelp = Prefix + DsImageStrings.StatusHelp`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 226)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StatusHelp;
    ```
- `public const string StatusHidden = Prefix + DsImageStrings.StatusHidden`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 227)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StatusHidden;
    ```
- `public const string StatusInformation = Prefix + DsImageStrings.StatusInformation`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 228)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StatusInformation;
    ```
- `public const string StatusWarning = Prefix + DsImageStrings.StatusWarning`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 229)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StatusWarning;
    ```
- `public const string StepInto = Prefix + DsImageStrings.StepInto`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 230)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StepInto;
    ```
- `public const string StepOut = Prefix + DsImageStrings.StepOut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 231)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StepOut;
    ```
- `public const string StepOver = Prefix + DsImageStrings.StepOver`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 232)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StepOver;
    ```
- `public const string Stop = Prefix + DsImageStrings.Stop`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 233)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Stop;
    ```
- `public const string String = Prefix + DsImageStrings.String`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 234)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.String;
    ```
- `public const string StructureInternal = Prefix + DsImageStrings.StructureInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 235)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StructureInternal;
    ```
- `public const string StructurePrivate = Prefix + DsImageStrings.StructurePrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 236)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StructurePrivate;
    ```
- `public const string StructureProtected = Prefix + DsImageStrings.StructureProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 237)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StructureProtected;
    ```
- `public const string StructurePublic = Prefix + DsImageStrings.StructurePublic`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 238)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StructurePublic;
    ```
- `public const string StructureShortcut = Prefix + DsImageStrings.StructureShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 239)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.StructureShortcut;
    ```
- `public const string TableViewNameOnly = Prefix + DsImageStrings.TableViewNameOnly`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 240)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TableViewNameOnly;
    ```
- `public const string Template = Prefix + DsImageStrings.Template`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 241)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Template;
    ```
- `public const string TemplateInternal = Prefix + DsImageStrings.TemplateInternal`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 242)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TemplateInternal;
    ```
- `public const string TemplatePrivate = Prefix + DsImageStrings.TemplatePrivate`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 243)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TemplatePrivate;
    ```
- `public const string TemplateProtected = Prefix + DsImageStrings.TemplateProtected`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 244)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TemplateProtected;
    ```
- `public const string TemplateShortcut = Prefix + DsImageStrings.TemplateShortcut`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 245)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TemplateShortcut;
    ```
- `public const string TerminateProcess = Prefix + DsImageStrings.TerminateProcess`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 246)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TerminateProcess;
    ```
- `public const string TextFile = Prefix + DsImageStrings.TextFile`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 247)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TextFile;
    ```
- `public const string Thread = Prefix + DsImageStrings.Thread`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 248)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Thread;
    ```
- `public const string ToggleAllBreakpoints = Prefix + DsImageStrings.ToggleAllBreakpoints`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 249)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ToggleAllBreakpoints;
    ```
- `public const string ToolstripPanelBottom = Prefix + DsImageStrings.ToolstripPanelBottom`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 250)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ToolstripPanelBottom;
    ```
- `public const string ToolstripPanelLeft = Prefix + DsImageStrings.ToolstripPanelLeft`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 251)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ToolstripPanelLeft;
    ```
- `public const string ToolstripPanelRight = Prefix + DsImageStrings.ToolstripPanelRight`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 252)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ToolstripPanelRight;
    ```
- `public const string ToolstripPanelTop = Prefix + DsImageStrings.ToolstripPanelTop`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 253)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.ToolstripPanelTop;
    ```
- `public const string TracepointDisabled = Prefix + DsImageStrings.TracepointDisabled`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 254)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TracepointDisabled;
    ```
- `public const string TracepointEnabled = Prefix + DsImageStrings.TracepointEnabled`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 255)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TracepointEnabled;
    ```
- `public const string TracepointError = Prefix + DsImageStrings.TracepointError`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 256)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TracepointError;
    ```
- `public const string TracepointWarning = Prefix + DsImageStrings.TracepointWarning`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 257)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.TracepointWarning;
    ```
- `public const string Type = Prefix + DsImageStrings.Type`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 258)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Type;
    ```
- `public const string Undo = Prefix + DsImageStrings.Undo`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 259)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Undo;
    ```
- `public const string UndoCheckBoxList = Prefix + DsImageStrings.UndoCheckBoxList`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 260)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.UndoCheckBoxList;
    ```
- `public const string UserDefinedDataType = Prefix + DsImageStrings.UserDefinedDataType`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 261)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.UserDefinedDataType;
    ```
- `public const string VBFileNode = Prefix + DsImageStrings.VBFileNode`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 262)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.VBFileNode;
    ```
- `public const string VBInteractiveWindow = Prefix + DsImageStrings.VBInteractiveWindow`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 263)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.VBInteractiveWindow;
    ```
- `public const string VBProjectNode = Prefix + DsImageStrings.VBProjectNode`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 264)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.VBProjectNode;
    ```
- `public const string WPFFile = Prefix + DsImageStrings.WPFFile`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 267)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.WPFFile;
    ```
- `public const string Watch = Prefix + DsImageStrings.Watch`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 265)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.Watch;
    ```
- `public const string WordWrap = Prefix + DsImageStrings.WordWrap`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 266)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.WordWrap;
    ```
- `public const string XMLFile = Prefix + DsImageStrings.XMLFile`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 268)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.XMLFile;
    ```
- `public const string XMLSchema = Prefix + DsImageStrings.XMLSchema`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 269)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.XMLSchema;
    ```
- `public const string XSLTransform = Prefix + DsImageStrings.XSLTransform`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/DsImagesAttribute.cs` (line 270)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.DsImagesAttribute.XSLTransform;
    ```

## Class `ExportImageSourceInfoProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IImageSourceInfoProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Images.ExportImageSourceInfoProviderAttribute(type: /* Type */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageSourceInfoProvider.cs` (line 51)

### Constructors

- `public ExportImageSourceInfoProviderAttribute(Type type)`
  - Summary: Constructor
  - Parameters:
    - `Type type`: Some type in the assembly, eg. this type itself
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageSourceInfoProvider.cs` (line 55)
- `public ExportImageSourceInfoProviderAttribute(Type type, double order)`
  - Summary: Constructor
  - Parameters:
    - `Type type`: Some type in the assembly, eg. this type itself
    - `double order`: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageSourceInfoProvider.cs` (line 62)

### Properties

- `public Type Type { get; }`
  - Summary: Gets the type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageSourceInfoProvider.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public double Order { get; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageSourceInfoProvider.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDotNetImageService`

Image manager for .NET fields, types, etc

**Example**

```csharp
// Instantiate dnSpy.Contracts.Images.IDotNetImageService and call its members.
var instance = new dnSpy.Contracts.Images.IDotNetImageService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 27)

### Methods

- `ImageReference GetImageReference(AssemblyDef assembly)`
  - Summary: Gets an image
  - Parameters:
    - `AssemblyDef assembly`: Assembly
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReference(assembly: /* AssemblyDef */);
    ```
- `ImageReference GetImageReference(EventDef @event)`
  - Summary: Gets an image
  - Parameters:
    - `EventDef @event`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReference(@event: /* EventDef */);
    ```
- `ImageReference GetImageReference(FieldDef field)`
  - Summary: Gets an image
  - Parameters:
    - `FieldDef field`: Field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReference(field: /* FieldDef */);
    ```
- `ImageReference GetImageReference(IPEImage peImage)`
  - Summary: Gets an image
  - Parameters:
    - `IPEImage peImage`: PE image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReference(peImage: /* IPEImage */);
    ```
- `ImageReference GetImageReference(MethodDef method)`
  - Summary: Gets an image
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReference(method: /* MethodDef */);
    ```
- `ImageReference GetImageReference(ModuleDef module)`
  - Summary: Gets an image
  - Parameters:
    - `ModuleDef module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReference(module: /* ModuleDef */);
    ```
- `ImageReference GetImageReference(PropertyDef property)`
  - Summary: Gets an image
  - Parameters:
    - `PropertyDef property`: Property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReference(property: /* PropertyDef */);
    ```
- `ImageReference GetImageReference(TypeDef type)`
  - Summary: Gets an image
  - Parameters:
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReference(type: /* TypeDef */);
    ```
- `ImageReference GetImageReferenceAssemblyRef()`
  - Summary: Gets an assembly reference image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReferenceAssemblyRef();
    ```
- `ImageReference GetImageReferenceField()`
  - Summary: Gets a field image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 123)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReferenceField();
    ```
- `ImageReference GetImageReferenceGenericParameter()`
  - Summary: Gets a generic parameter image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReferenceGenericParameter();
    ```
- `ImageReference GetImageReferenceLocal()`
  - Summary: Gets a local image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReferenceLocal();
    ```
- `ImageReference GetImageReferenceMethod()`
  - Summary: Gets a method image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReferenceMethod();
    ```
- `ImageReference GetImageReferenceModuleRef()`
  - Summary: Gets a module reference image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReferenceModuleRef();
    ```
- `ImageReference GetImageReferenceParameter()`
  - Summary: Gets a parameter image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReferenceParameter();
    ```
- `ImageReference GetImageReferenceType()`
  - Summary: Gets a type image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReferenceType();
    ```
- `ImageReference GetNamespaceImageReference()`
  - Summary: Gets a namespace image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IDotNetImageService.cs` (line 136)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNamespaceImageReference();
    ```

## Interface `IImageService`

Image service

**Example**

```csharp
// Instantiate dnSpy.Contracts.Images.IImageService and call its members.
var instance = new dnSpy.Contracts.Images.IImageService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageService.cs` (line 26)

### Methods

- `BitmapSource GetImage(ImageReference imageReference, ImageOptions options)`
  - Summary: Returns an image
  - Parameters:
    - `ImageReference imageReference`: Image reference
    - `ImageOptions options`: Image options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageService.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImage(imageReference: /* ImageReference */, options: /* ImageOptions */);
    ```

## Interface `IImageSourceInfoProvider`

Converts s to s. Use to export an instance. There's usually no need to export an instance since the default implementation is usually enough.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Images.IImageSourceInfoProvider and call its members.
var instance = new dnSpy.Contracts.Images.IImageSourceInfoProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageSourceInfoProvider.cs` (line 30)

### Methods

- `ImageSourceInfo[] GetImageSourceInfos(string name)`
  - Summary: Returns all s or null if the next (or default) instance should be asked.
  - Parameters:
    - `string name`: Name from but with any options removed from the string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageSourceInfoProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageSourceInfos(name: /* string */);
    ```

## Interface `IImageSourceInfoProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Images.IImageSourceInfoProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Images.IImageSourceInfoProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageSourceInfoProvider.cs` (line 41)

### Properties

- `Type Type { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageSourceInfoProvider.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/IImageSourceInfoProvider.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ImageOptions`

Image options

**Example**

```csharp
var instance = new dnSpy.Contracts.Images.ImageOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageOptions.cs` (line 30)

### Constructors

- `public ImageOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageOptions.cs` (line 65)
- `public ImageOptions(ITextView textView)`
  - Summary: Constructor
  - Parameters:
    - `ITextView textView`: Text view with which to initialize and
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageOptions.cs` (line 71)

### Properties

- `public Brush BackgroundBrush { get; set; }`
  - Summary: Background brush or null. Only and brushes are supported.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageOptions.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BackgroundBrush;
    ```
- `public Color? BackgroundColor { get; set; }`
  - Summary: Background color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageOptions.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BackgroundColor;
    ```
- `public DependencyObject DpiObject { get; set; }`
  - Summary: If initialized, the DPI of its containing window will be used and doesn't have to be initialized.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageOptions.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DpiObject;
    ```
- `public Size Dpi { get; set; }`
  - Summary: DPI or (0,0) to use the default DPI (DPI of main window)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageOptions.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Dpi;
    ```
- `public Size LogicalSize { get; set; }`
  - Summary: Image size in logical pixels. 16x16 is used if this is 0x0
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageOptions.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LogicalSize;
    ```
- `public Size Zoom { get; set; }`
  - Summary: Total zoom applied to the element containing the image or (0,0) if the property shouldn't be used. 1.0 == 100%
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageOptions.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Zoom;
    ```

## Struct `ImageReference`

Image reference

**Example**

```csharp
var instance = new dnSpy.Contracts.Images.ImageReference(assembly: /* Assembly */, name: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReference.cs` (line 28)

### Constructors

- `public ImageReference(Assembly assembly, string name)`
  - Summary: Constructor
  - Parameters:
    - `Assembly assembly`: Assembly of image or null if is a pack: URI
    - `string name`: Name of image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReference.cs` (line 55)

### Methods

- `public override string ToString()`
  - Summary: Converts this instance to a string that can be passed to
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReference.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static bool TryParse(string value, out ImageReference result)`
  - Summary: Parses a string and tries to create an
  - Parameters:
    - `string value`: String to parse
    - `out ImageReference result`: Result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReference.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Images.ImageReference.TryParse(value: /* string */, result: /* ImageReference */);
    ```

### Properties

- `public Assembly Assembly { get; }`
  - Summary: Assembly of image or null if is a URI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReference.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Assembly;
    ```
- `public bool IsDefault => Assembly == null && Name == null`
  - Summary: true if it's the default instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReference.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```
- `public string Name { get; }`
  - Summary: Name of image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReference.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

### Fields

- `public static readonly ImageReference None = default`
  - Summary: Gets an which isn't referencing any image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReference.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.ImageReference.None;
    ```

## Class `ImageReferenceConverter`

Converts a to an or vice versa

**Inherits/Implements:** `TypeConverter`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Images.ImageReferenceConverter and call its members.
var instance = new dnSpy.Contracts.Images.ImageReferenceConverter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReferenceConverter.cs` (line 28)

### Methods

- `public override bool CanConvertFrom(ITypeDescriptorContext context, Type sourceType)`
  - Parameters:
    - `ITypeDescriptorContext context`: Description not provided.
    - `Type sourceType`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReferenceConverter.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.CanConvertFrom(context: /* ITypeDescriptorContext */, sourceType: /* Type */);
    ```
- `public override bool CanConvertTo(ITypeDescriptorContext context, Type destinationType)`
  - Parameters:
    - `ITypeDescriptorContext context`: Description not provided.
    - `Type destinationType`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReferenceConverter.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.CanConvertTo(context: /* ITypeDescriptorContext */, destinationType: /* Type */);
    ```
- `public override object ConvertFrom(ITypeDescriptorContext context, CultureInfo culture, object value)`
  - Parameters:
    - `ITypeDescriptorContext context`: Description not provided.
    - `CultureInfo culture`: Description not provided.
    - `object value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReferenceConverter.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertFrom(context: /* ITypeDescriptorContext */, culture: /* CultureInfo */, value: /* object */);
    ```
- `public override object ConvertTo(ITypeDescriptorContext context, CultureInfo culture, object value, Type destinationType)`
  - Parameters:
    - `ITypeDescriptorContext context`: Description not provided.
    - `CultureInfo culture`: Description not provided.
    - `object value`: Description not provided.
    - `Type destinationType`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageReferenceConverter.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertTo(context: /* ITypeDescriptorContext */, culture: /* CultureInfo */, value: /* object */, destinationType: /* Type */);
    ```

## Struct `ImageSourceInfo`

Image source info

**Example**

```csharp
// Instantiate dnSpy.Contracts.Images.ImageSourceInfo and call its members.
var instance = new dnSpy.Contracts.Images.ImageSourceInfo(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageSourceInfo.cs` (line 26)

### Properties

- `public Size Size { get; set; }`
  - Summary: Size of image in pixels or
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageSourceInfo.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Size;
    ```
- `public string Uri { get; set; }`
  - Summary: URI of image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageSourceInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Uri;
    ```

### Fields

- `public static readonly Size AnySize = new Size(0, 0)`
  - Summary: Any size
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Images/ImageSourceInfo.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Images.ImageSourceInfo.AnySize;
    ```

