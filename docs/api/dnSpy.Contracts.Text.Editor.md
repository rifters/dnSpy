# Namespace `dnSpy.Contracts.Text.Editor`

## Enum `BlockStructureKind`

Block kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.BlockStructureKind and call its members.
var instance = new dnSpy.Contracts.Text.Editor.BlockStructureKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/BlockStructureKind.cs` (line 24)

### Members

- `None`: Not a block
- `Namespace`: Namespace
- `Type`: Reference type
- `Module`: Module
- `ValueType`: Value type
- `Interface`: Interface
- `Method`: Method
- `Accessor`: Accessor
- `AnonymousMethod`: Anonymous method
- `Constructor`: Constructor
- `Destructor`: Destructor
- `Operator`: Operator
- `Conditional`: Conditional
- `Loop`: Loop
- `Property`: Property
- `Event`: Event
- `Try`: Try
- `Catch`: Catch
- `Filter`: Catch filter
- `Finally`: Finally
- `Fault`: Fault
- `Lock`: Lock
- `Using`: Using
- `Fixed`: Fixed
- `Switch`: Switch
- `Case`: Case
- `LocalFunction`: Local function
- `Other`: Other block kind
- `Xml`: XML block
- `Xaml`: XAML block

## Enum `BlockStructureLineKind`

Block structure line kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.BlockStructureLineKind and call its members.
var instance = new dnSpy.Contracts.Text.Editor.BlockStructureLineKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/BlockStructureLineKind.cs` (line 24)

### Members

- `Solid`: Solid lines
- `Dashed_1_1`: Dashed lines (dash 1px, gap 1px)
- `Dashed_2_2`: Dashed lines (dash 2px, gap 2px)
- `Dashed_3_3`: Dashed lines (dash 3px, gap 3px)
- `Dashed_4_4`: Dashed lines (dash 4px, gap 4px)

## Class `CodeEditorOptions`

options

**Inherits/Implements:** `CommonTextEditorOptions`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.CodeEditorOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CodeEditorOptions.cs` (line 30)

### Constructors

- `public CodeEditorOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CodeEditorOptions.cs` (line 57)

### Methods

- `public new CodeEditorOptions Clone()`
  - Summary: Clones this
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CodeEditorOptions.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

### Properties

- `public HashSet<string> Roles { get; }`
  - Summary: All roles
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CodeEditorOptions.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Roles;
    ```
- `public ITextBuffer TextBuffer { get; set; }`
  - Summary: Text buffer to use or null. Use to create an instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CodeEditorOptions.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextBuffer;
    ```

## Class `CommonTextEditorOptions`

Common text editor options

**Inherits/Implements:** `TextViewCreatorOptions`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.CommonTextEditorOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CommonTextEditorOptions.cs` (line 26)

### Constructors

- `public CommonTextEditorOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CommonTextEditorOptions.cs` (line 40)

### Methods

- `public CommonTextEditorOptions CopyTo(CommonTextEditorOptions other)`
  - Summary: Copy this to
  - Parameters:
    - `CommonTextEditorOptions other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CommonTextEditorOptions.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* CommonTextEditorOptions */);
    ```
- `public new CommonTextEditorOptions Clone()`
  - Summary: Clones this
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CommonTextEditorOptions.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

### Properties

- `public IContentType ContentType { get; set; }`
  - Summary: Content type or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CommonTextEditorOptions.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentType;
    ```
- `public string ContentTypeString { get; set; }`
  - Summary: Content type string or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/CommonTextEditorOptions.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentTypeString;
    ```

## Class `CustomLineNumberMargin`

Custom line number margin. The must have the role and you must call . Option is used to show or hide it after creation.

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.CustomLineNumberMargin members directly without instantiation.
dnSpy.Contracts.Text.Editor.CustomLineNumberMargin./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICustomLineNumberMargin.cs` (line 34)

### Methods

- `public static void SetOwner(ITextView textView, ICustomLineNumberMarginOwner owner)`
  - Summary: Sets the owner and must only be called once
  - Parameters:
    - `ITextView textView`: Text view
    - `ICustomLineNumberMarginOwner owner`: Owner
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICustomLineNumberMargin.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.CustomLineNumberMargin.SetOwner(textView: /* ITextView */, owner: /* ICustomLineNumberMarginOwner */);
    ```

## Class `DefaultDsOptions`

Default options

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.DefaultDsOptions members directly without instantiation.
dnSpy.Contracts.Text.Editor.DefaultDsOptions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsOptions.cs` (line 26)

### Fields

- `public const string IndentStyleOptionName = "Default/IndentStyle"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsOptions.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsOptions.IndentStyleOptionName;
    ```
- `public static readonly EditorOptionKey<IndentStyle> IndentStyleOptionId = new EditorOptionKey<IndentStyle>(IndentStyleOptionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsOptions.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsOptions.IndentStyleOptionId;
    ```

## Class `DefaultDsTextViewOptions`

Default options

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions members directly without instantiation.
dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 26)

### Fields

- `public const int DefaultRefreshScreenOnChangeWaitMilliSeconds = 150`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.DefaultRefreshScreenOnChangeWaitMilliSeconds;
    ```
- `public const string AllowBoxSelectionName = "ITextView/AllowBoxSelection"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.AllowBoxSelectionName;
    ```
- `public const string BlockStructureLineKindName = "ITextView/BlockStructureLineKind"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 57)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.BlockStructureLineKindName;
    ```
- `public const string BraceMatchingName = "ITextView/BraceMatching"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 45)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.BraceMatchingName;
    ```
- `public const string CanChangeOverwriteModeName = "ITextView/CanChangeOverwriteMode"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.CanChangeOverwriteModeName;
    ```
- `public const string CanChangeUseVisibleWhitespaceName = "ITextView/CanChangeUseVisibleWhitespace"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.CanChangeUseVisibleWhitespaceName;
    ```
- `public const string CanChangeWordWrapStyleName = "ITextView/CanChangeWordWrapStyle"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.CanChangeWordWrapStyleName;
    ```
- `public const string CompressEmptyOrWhitespaceLinesName = "ITextView/CompressEmptyOrWhitespaceLines"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 51)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.CompressEmptyOrWhitespaceLinesName;
    ```
- `public const string CompressNonLetterLinesName = "ITextView/CompressNonLetterLines"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.CompressNonLetterLinesName;
    ```
- `public const string EnableColorizationName = "ITextView/EnableColorization"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.EnableColorizationName;
    ```
- `public const string HighlightRelatedKeywordsName = "ITextView/HighlightRelatedKeywords"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.HighlightRelatedKeywordsName;
    ```
- `public const string LineSeparatorsName = "ITextView/LineSeparators"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.LineSeparatorsName;
    ```
- `public const string ReferenceHighlightingName = "ITextView/ReferenceHighlighting"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.ReferenceHighlightingName;
    ```
- `public const string RefreshScreenOnChangeName = "ITextView/RefreshScreenOnChange"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.RefreshScreenOnChangeName;
    ```
- `public const string RefreshScreenOnChangeWaitMilliSecondsName = "ITextView/RefreshScreenOnChangeWaitMilliSeconds"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.RefreshScreenOnChangeWaitMilliSecondsName;
    ```
- `public const string RemoveExtraTextLineVerticalPixelsName = "ITextView/RemoveExtraTextLineVerticalPixels"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.RemoveExtraTextLineVerticalPixelsName;
    ```
- `public static readonly EditorOptionKey<BlockStructureLineKind> BlockStructureLineKindId = new EditorOptionKey<BlockStructureLineKind>(BlockStructureLineKindName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.BlockStructureLineKindId;
    ```
- `public static readonly EditorOptionKey<bool> AllowBoxSelectionId = new EditorOptionKey<bool>(AllowBoxSelectionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.AllowBoxSelectionId;
    ```
- `public static readonly EditorOptionKey<bool> BraceMatchingId = new EditorOptionKey<bool>(BraceMatchingName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.BraceMatchingId;
    ```
- `public static readonly EditorOptionKey<bool> CanChangeOverwriteModeId = new EditorOptionKey<bool>(CanChangeOverwriteModeName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.CanChangeOverwriteModeId;
    ```
- `public static readonly EditorOptionKey<bool> CanChangeUseVisibleWhitespaceId = new EditorOptionKey<bool>(CanChangeUseVisibleWhitespaceName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.CanChangeUseVisibleWhitespaceId;
    ```
- `public static readonly EditorOptionKey<bool> CanChangeWordWrapStyleId = new EditorOptionKey<bool>(CanChangeWordWrapStyleName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.CanChangeWordWrapStyleId;
    ```
- `public static readonly EditorOptionKey<bool> CompressEmptyOrWhitespaceLinesId = new EditorOptionKey<bool>(CompressEmptyOrWhitespaceLinesName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.CompressEmptyOrWhitespaceLinesId;
    ```
- `public static readonly EditorOptionKey<bool> CompressNonLetterLinesId = new EditorOptionKey<bool>(CompressNonLetterLinesName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 54)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.CompressNonLetterLinesId;
    ```
- `public static readonly EditorOptionKey<bool> EnableColorizationId = new EditorOptionKey<bool>(EnableColorizationName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.EnableColorizationId;
    ```
- `public static readonly EditorOptionKey<bool> HighlightRelatedKeywordsId = new EditorOptionKey<bool>(HighlightRelatedKeywordsName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.HighlightRelatedKeywordsId;
    ```
- `public static readonly EditorOptionKey<bool> LineSeparatorsId = new EditorOptionKey<bool>(LineSeparatorsName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.LineSeparatorsId;
    ```
- `public static readonly EditorOptionKey<bool> ReferenceHighlightingId = new EditorOptionKey<bool>(ReferenceHighlightingName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.ReferenceHighlightingId;
    ```
- `public static readonly EditorOptionKey<bool> RefreshScreenOnChangeId = new EditorOptionKey<bool>(RefreshScreenOnChangeName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.RefreshScreenOnChangeId;
    ```
- `public static readonly EditorOptionKey<bool> RemoveExtraTextLineVerticalPixelsId = new EditorOptionKey<bool>(RemoveExtraTextLineVerticalPixelsName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.RemoveExtraTextLineVerticalPixelsId;
    ```
- `public static readonly EditorOptionKey<int> RefreshScreenOnChangeWaitMilliSecondsId = new EditorOptionKey<int>(RefreshScreenOnChangeWaitMilliSecondsName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsTextViewOptions.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsTextViewOptions.RefreshScreenOnChangeWaitMilliSecondsId;
    ```

## Class `DefaultDsWpfViewOptions`

Default options

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.DefaultDsWpfViewOptions members directly without instantiation.
dnSpy.Contracts.Text.Editor.DefaultDsWpfViewOptions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsWpfViewOptions.cs` (line 26)

### Fields

- `public const string ForceClearTypeIfNeededName = "IWpfTextView/ForceClearTypeIfNeeded"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsWpfViewOptions.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsWpfViewOptions.ForceClearTypeIfNeededName;
    ```
- `public static readonly EditorOptionKey<bool> ForceClearTypeIfNeededId = new EditorOptionKey<bool>(ForceClearTypeIfNeededName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultDsWpfViewOptions.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultDsWpfViewOptions.ForceClearTypeIfNeededId;
    ```

## Class `DefaultReplEditorOptions`

Default options

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.DefaultReplEditorOptions members directly without instantiation.
dnSpy.Contracts.Text.Editor.DefaultReplEditorOptions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultReplEditorOptions.cs` (line 26)

### Fields

- `public const int DefaultRefreshScreenOnChangeWaitMilliSeconds = DefaultDsTextViewOptions.DefaultRefreshScreenOnChangeWaitMilliSeconds`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultReplEditorOptions.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultReplEditorOptions.DefaultRefreshScreenOnChangeWaitMilliSeconds;
    ```
- `public const string RefreshScreenOnChangeName = "IReplEditor/RefreshScreenOnChange"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultReplEditorOptions.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultReplEditorOptions.RefreshScreenOnChangeName;
    ```
- `public const string RefreshScreenOnChangeWaitMilliSecondsName = "IReplEditor/RefreshScreenOnChangeWaitMilliSeconds"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultReplEditorOptions.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultReplEditorOptions.RefreshScreenOnChangeWaitMilliSecondsName;
    ```
- `public static readonly EditorOptionKey<bool> RefreshScreenOnChangeId = new EditorOptionKey<bool>(RefreshScreenOnChangeName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultReplEditorOptions.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultReplEditorOptions.RefreshScreenOnChangeId;
    ```
- `public static readonly EditorOptionKey<int> RefreshScreenOnChangeWaitMilliSecondsId = new EditorOptionKey<int>(RefreshScreenOnChangeWaitMilliSecondsName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/DefaultReplEditorOptions.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.DefaultReplEditorOptions.RefreshScreenOnChangeWaitMilliSecondsId;
    ```

## Class `DotNetMethodBodyGlyphTextMarkerLocationInfo`

Method text marker location info

**Inherits/Implements:** `GlyphTextMarkerLocationInfo`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.DotNetMethodBodyGlyphTextMarkerLocationInfo(module: /* ModuleId */, token: /* uint */, ilOffset: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 39)

### Constructors

- `public DotNetMethodBodyGlyphTextMarkerLocationInfo(ModuleId module, int token, uint ilOffset)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module
    - `int token`: Token of method
    - `uint ilOffset`: Method offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 73)
- `public DotNetMethodBodyGlyphTextMarkerLocationInfo(ModuleId module, uint token, uint ilOffset)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of method
    - `uint ilOffset`: Method offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 61)

### Properties

- `public ModuleId Module { get; }`
  - Summary: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public uint ILOffset { get; }`
  - Summary: Method offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ILOffset;
    ```
- `public uint Token { get; }`
  - Summary: Token of method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

## Class `DotNetTokenGlyphTextMarkerLocationInfo`

Method text marker location info

**Inherits/Implements:** `GlyphTextMarkerLocationInfo`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.DotNetTokenGlyphTextMarkerLocationInfo(module: /* ModuleId */, token: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 83)

### Constructors

- `public DotNetTokenGlyphTextMarkerLocationInfo(ModuleId module, int token)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module
    - `int token`: Token of definition (type, method, field, property, event)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 109)
- `public DotNetTokenGlyphTextMarkerLocationInfo(ModuleId module, uint token)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of definition (type, method, field, property, event)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 99)

### Properties

- `public ModuleId Module { get; }`
  - Summary: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public uint Token { get; }`
  - Summary: Token of definition (type, method, field, property, event)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

## Struct `GlyphTextMarkerAndSpan`

Marker and its span in a

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.GlyphTextMarkerAndSpan(marker: /* IGlyphTextMarker */, span: /* SnapshotSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 181)

### Constructors

- `public GlyphTextMarkerAndSpan(IGlyphTextMarker marker, SnapshotSpan span)`
  - Summary: Constructor
  - Parameters:
    - `IGlyphTextMarker marker`: Marker
    - `SnapshotSpan span`: Span of the marker in the
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 197)

### Properties

- `public IGlyphTextMarker Marker { get; }`
  - Summary: Gets the marker
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 185)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Marker;
    ```
- `public SnapshotSpan Span { get; }`
  - Summary: Gets the span of the marker in the
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 190)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Class `GlyphTextMarkerGlyphTag`

glyph tag

**Inherits/Implements:** `IGlyphTag`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.GlyphTextMarkerGlyphTag(imageReference: /* ImageReference */, zIndex: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 362)

### Constructors

- `public GlyphTextMarkerGlyphTag(ImageReference imageReference, int zIndex)`
  - Summary: Constructor
  - Parameters:
    - `ImageReference imageReference`: Image reference ()
    - `int zIndex`: Z-index ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 378)

### Properties

- `public ImageReference ImageReference { get; }`
  - Summary: Image reference ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 366)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageReference;
    ```
- `public int ZIndex { get; }`
  - Summary: Z-index ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 371)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ZIndex;
    ```

## Class `GlyphTextMarkerHandlerMouseProcessorBase`

Abstract class implementing

**Inherits/Implements:** `IGlyphTextMarkerHandlerMouseProcessor`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.GlyphTextMarkerHandlerMouseProcessorBase();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 206)

### Constructors

- `protected GlyphTextMarkerHandlerMouseProcessorBase()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 210)

### Methods

- `public virtual void OnMouseDown(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Default mouse down handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 218)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseDown(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```
- `public virtual void OnMouseLeftButtonDown(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Default mouse left button down handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 234)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeftButtonDown(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```
- `public virtual void OnMouseLeftButtonUp(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Default mouse left button up handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 242)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeftButtonUp(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```
- `public virtual void OnMouseMove(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseEventArgs e)`
  - Summary: Default mouse move handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 266)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseMove(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseEventArgs */);
    ```
- `public virtual void OnMouseRightButtonDown(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Default mouse right button down handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 250)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseRightButtonDown(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```
- `public virtual void OnMouseRightButtonUp(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Default mouse right button up handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 258)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseRightButtonUp(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```
- `public virtual void OnMouseUp(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Default mouse up handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 226)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseUp(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```

## Class `GlyphTextMarkerLocationInfo`

Text marker location base class

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.GlyphTextMarkerLocationInfo and call its members.
var instance = new dnSpy.Contracts.Text.Editor.GlyphTextMarkerLocationInfo(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 33)

## Class `GlyphTextMarkerMouseProcessorBase`

Abstract class implementing

**Inherits/Implements:** `IGlyphTextMarkerMouseProcessor`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.GlyphTextMarkerMouseProcessorBase();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 159)

### Constructors

- `protected GlyphTextMarkerMouseProcessorBase()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 163)

### Methods

- `public virtual IEnumerable<GuidObject> GetContextMenuObjects(IGlyphTextMarkerMouseProcessorContext context, Point marginRelativePoint)`
  - Summary: Creates context menu objects
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `Point marginRelativePoint`: Position of the mouse pointer relative to the glyph margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 171)
  - Example:
    ```csharp
    // Example invocation
    instance.GetContextMenuObjects(context: /* IGlyphTextMarkerMouseProcessorContext */, marginRelativePoint: /* Point */);
    ```
- `public virtual void OnMouseDown(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Default mouse down handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 180)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseDown(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```
- `public virtual void OnMouseEnter(IGlyphTextMarkerMouseProcessorContext context, MouseEventArgs e)`
  - Summary: Default mouse enter handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 229)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseEnter(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseEventArgs */);
    ```
- `public virtual void OnMouseLeave(IGlyphTextMarkerMouseProcessorContext context, MouseEventArgs e)`
  - Summary: Default mouse leave handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 236)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeave(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseEventArgs */);
    ```
- `public virtual void OnMouseLeftButtonDown(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Default mouse left button down handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 194)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeftButtonDown(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```
- `public virtual void OnMouseLeftButtonUp(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Default mouse left button up handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 201)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeftButtonUp(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```
- `public virtual void OnMouseMove(IGlyphTextMarkerMouseProcessorContext context, MouseEventArgs e)`
  - Summary: Default mouse move handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 222)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseMove(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseEventArgs */);
    ```
- `public virtual void OnMouseRightButtonDown(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Default mouse right button down handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 208)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseRightButtonDown(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```
- `public virtual void OnMouseRightButtonUp(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Default mouse right button up handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 215)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseRightButtonUp(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```
- `public virtual void OnMouseUp(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Default mouse up handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseUp(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```

## Class `GlyphTextMarkerServiceZIndexes`

Z-indexes

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes members directly without instantiation.
dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 24)

### Fields

- `public const int AdvancedBreakpointError = 2570`
  - Summary: (Debugger) Z-index of advanced breakpoints with errors
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.AdvancedBreakpointError;
    ```
- `public const int AdvancedBreakpointWarning = 2560`
  - Summary: (Debugger) Z-index of advanced breakpoints with warnings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.AdvancedBreakpointWarning;
    ```
- `public const int AdvancedTracepointError = 2670`
  - Summary: (Debugger) Z-index of advanced tracepoints with errors
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 113)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.AdvancedTracepointError;
    ```
- `public const int AdvancedTracepointWarning = 2660`
  - Summary: (Debugger) Z-index of advanced tracepoints with warnings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 108)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.AdvancedTracepointWarning;
    ```
- `public const int Bookmark = 1000`
  - Summary: Z-index of enabled bookmarks
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.Bookmark;
    ```
- `public const int BreakpointError = 2550`
  - Summary: (Debugger) Z-index of breakpoints with errors
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.BreakpointError;
    ```
- `public const int BreakpointWarning = 2540`
  - Summary: (Debugger) Z-index of breakpoints with warnings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.BreakpointWarning;
    ```
- `public const int CurrentStatement = 3000`
  - Summary: (Debugger) Z-index of current statement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 118)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.CurrentStatement;
    ```
- `public const int DisabledAdvancedBreakpoint = 2010`
  - Summary: (Debugger) Z-index of advanced disabled breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.DisabledAdvancedBreakpoint;
    ```
- `public const int DisabledAdvancedTracepoint = 2610`
  - Summary: (Debugger) Z-index of advanced disabled tracepoints
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 83)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.DisabledAdvancedTracepoint;
    ```
- `public const int DisabledBookmark = 990`
  - Summary: Z-index of disabled bookmarks
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.DisabledBookmark;
    ```
- `public const int DisabledBreakpoint = 2000`
  - Summary: (Debugger) Z-index of disabled breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.DisabledBreakpoint;
    ```
- `public const int DisabledTracepoint = 2600`
  - Summary: (Debugger) Z-index of disabled tracepionts
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 78)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.DisabledTracepoint;
    ```
- `public const int EnabledAdvancedBreakpoint = 2530`
  - Summary: (Debugger) Z-index of advanced enabled breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.EnabledAdvancedBreakpoint;
    ```
- `public const int EnabledAdvancedTracepoint = 2630`
  - Summary: (Debugger) Z-index of advanced enabled tracepoints
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 93)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.EnabledAdvancedTracepoint;
    ```
- `public const int EnabledBreakpoint = 2500`
  - Summary: (Debugger) Z-index of enabled breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.EnabledBreakpoint;
    ```
- `public const int EnabledTracepoint = 2620`
  - Summary: (Debugger) Z-index of enabled tracepoints
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.EnabledTracepoint;
    ```
- `public const int ReturnStatement = 4000`
  - Summary: (Debugger) Z-index of return statement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 123)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.ReturnStatement;
    ```
- `public const int TracepointError = 2650`
  - Summary: (Debugger) Z-index of tracepoints with errors
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 103)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.TracepointError;
    ```
- `public const int TracepointWarning = 2640`
  - Summary: (Debugger) Z-index of tracepoints with warnings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/GlyphTextMarkerServiceZIndexes.cs` (line 98)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.GlyphTextMarkerServiceZIndexes.TracepointWarning;
    ```

## Class `GlyphTextMarkerTag`

text marker tag

**Inherits/Implements:** `IGlyphTextMarkerTag`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.GlyphTextMarkerTag(markerTypeName: /* string */, selectedMarkerTypeName: /* string */, zIndex: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 315)

### Constructors

- `public GlyphTextMarkerTag(string markerTypeName, string selectedMarkerTypeName, int zIndex)`
  - Summary: Constructor
  - Parameters:
    - `string markerTypeName`: Name of a (or an ) ()
    - `string selectedMarkerTypeName`: Name of a (or an ) ()
    - `int zIndex`: Z-index of this text marker ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 337)

### Properties

- `public int ZIndex { get; }`
  - Summary: Gets the Z-index ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 329)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ZIndex;
    ```
- `public string MarkerTypeName { get; }`
  - Summary: Name of a (or an ) ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 319)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MarkerTypeName;
    ```
- `public string SelectedMarkerTypeName { get; }`
  - Summary: Gets the name of the marker format definition to use whenever the caret is inside the span; it can be null ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 324)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectedMarkerTypeName;
    ```

## Class `GlyphTextMarkerToolTip`

Contains the tooltip content and style that is shown when hovering over the glyph in the glyph margin

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.GlyphTextMarkerToolTip(content: /* string */, style: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 68)

### Constructors

- `public GlyphTextMarkerToolTip(object content, object style)`
  - Summary: Constructor
  - Parameters:
    - `object content`: Content to show in the tooltip
    - `object style`: Tooltip style or null. Can be the key of a style in the resources (eg. a ) or a instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 94)
- `public GlyphTextMarkerToolTip(string content, object style = null)`
  - Summary: Constructor
  - Parameters:
    - `string content`: Text content to show in the tooltip
    - `object style` (default: `null`): Tooltip style or null. Can be the key of a style in the resources (eg. a ) or a instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 84)

### Properties

- `public object Content { get; }`
  - Summary: Tooltip content, a or a UI element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Content;
    ```
- `public object Style { get; }`
  - Summary: Tooltip style or null. Can be the key of a style in the resources (eg. a ) or a instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Style;
    ```

## Interface `ICodeEditor`

Code text editor

**Inherits/Implements:** `IUIObjectProvider2`, `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.ICodeEditor and call its members.
var instance = new dnSpy.Contracts.Text.Editor.ICodeEditor(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICodeEditor.cs` (line 28)

### Properties

- `IDsWpfTextView TextView { get; }`
  - Summary: Gets the text view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICodeEditor.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextView;
    ```
- `IDsWpfTextViewHost TextViewHost { get; }`
  - Summary: Gets the text view host
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICodeEditor.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewHost;
    ```
- `ITextBuffer TextBuffer { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICodeEditor.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextBuffer;
    ```

## Interface `ICodeEditorProvider`

Creates instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.ICodeEditorProvider and call its members.
var instance = new dnSpy.Contracts.Text.Editor.ICodeEditorProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICodeEditorProvider.cs` (line 24)

### Methods

- `ICodeEditor Create(CodeEditorOptions options)`
  - Summary: Creates a new instance
  - Parameters:
    - `CodeEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICodeEditorProvider.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(options: /* CodeEditorOptions */);
    ```

## Interface `ICustomLineNumberMarginOwner`

Custom line number margin owner

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.ICustomLineNumberMarginOwner and call its members.
var instance = new dnSpy.Contracts.Text.Editor.ICustomLineNumberMarginOwner(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICustomLineNumberMargin.cs` (line 86)

### Methods

- `TextFormattingRunProperties GetDefaultTextFormattingRunProperties()`
  - Summary: Gets the default text formatting properties
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICustomLineNumberMargin.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDefaultTextFormattingRunProperties();
    ```
- `TextFormattingRunProperties GetLineNumberTextFormattingRunProperties(ITextViewLine viewLine, ITextSnapshotLine snapshotLine, int lineNumber, object state)`
  - Summary: Gets for the line number text
  - Parameters:
    - `ITextViewLine viewLine`: View line
    - `ITextSnapshotLine snapshotLine`: Snapshot line
    - `int lineNumber`: Line number returned by
    - `object state`: State, initialized by
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICustomLineNumberMargin.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineNumberTextFormattingRunProperties(viewLine: /* ITextViewLine */, snapshotLine: /* ITextSnapshotLine */, lineNumber: /* int */, state: /* object */);
    ```
- `int? GetLineNumber(ITextViewLine viewLine, ITextSnapshotLine snapshotLine, ref object state)`
  - Summary: Gets the line number or null to not print any line number. You should normally return null if 's is false.
  - Parameters:
    - `ITextViewLine viewLine`: View line
    - `ITextSnapshotLine snapshotLine`: Snapshot line
    - `ref object state`: State, initially null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICustomLineNumberMargin.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineNumber(viewLine: /* ITextViewLine */, snapshotLine: /* ITextSnapshotLine */, state: /* object */);
    ```
- `int? GetMaxLineNumberDigits()`
  - Summary: Gets maximum number of digits in a line number or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICustomLineNumberMargin.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMaxLineNumberDigits();
    ```
- `void OnInvisible()`
  - Summary: Called when the margin is hidden and when the margin gets disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICustomLineNumberMargin.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.OnInvisible();
    ```
- `void OnTextPropertiesChanged(IClassificationFormatMap classificationFormatMap)`
  - Summary: Gets called when text formatting properties have changed
  - Parameters:
    - `IClassificationFormatMap classificationFormatMap`: Classification format map
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICustomLineNumberMargin.cs` (line 123)
  - Example:
    ```csharp
    // Example invocation
    instance.OnTextPropertiesChanged(classificationFormatMap: /* IClassificationFormatMap */);
    ```
- `void OnVisible()`
  - Summary: Called when the margin is visible
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ICustomLineNumberMargin.cs` (line 128)
  - Example:
    ```csharp
    // Example invocation
    instance.OnVisible();
    ```

## Interface `IDotNetSpanMap`

Converts .NET tokens to spans

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IDotNetSpanMap and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IDotNetSpanMap(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 273)

### Methods

- `Span? ToSpan(ModuleId module, uint token)`
  - Summary: Converts a .NET module + token to a or returns null if the definition isn't present in the document
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of definition (type, method, field, property, event)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 289)
  - Example:
    ```csharp
    // Example invocation
    instance.ToSpan(module: /* ModuleId */, token: /* uint */);
    ```
- `Span? ToSpan(ModuleId module, uint token, uint ilOffset)`
  - Summary: Converts a method offset to a or returns null if the IL offset isn't present in the document
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of method
    - `uint ilOffset`: IL offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 281)
  - Example:
    ```csharp
    // Example invocation
    instance.ToSpan(module: /* ModuleId */, token: /* uint */, ilOffset: /* uint */);
    ```

## Interface `IDsTextEditorFactoryService`

dnSpy interface

**Inherits/Implements:** `ITextEditorFactoryService`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IDsTextEditorFactoryService and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IDsTextEditorFactoryService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextEditorFactoryService.cs` (line 27)

### Methods

- `IDsWpfTextView CreateTextView(ITextBuffer textBuffer, ITextViewRoleSet roles, IEditorOptions parentOptions, TextViewCreatorOptions options)`
  - Summary: Creates a new instance using
  - Parameters:
    - `ITextBuffer textBuffer`: Text buffer
    - `ITextViewRoleSet roles`: Roles
    - `IEditorOptions parentOptions`: Parent options
    - `TextViewCreatorOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextEditorFactoryService.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextView(textBuffer: /* ITextBuffer */, roles: /* ITextViewRoleSet */, parentOptions: /* IEditorOptions */, options: /* TextViewCreatorOptions */);
    ```
- `IDsWpfTextView CreateTextView(ITextBuffer textBuffer, ITextViewRoleSet roles, TextViewCreatorOptions options)`
  - Summary: Creates a new instance using
  - Parameters:
    - `ITextBuffer textBuffer`: Text buffer
    - `ITextViewRoleSet roles`: Roles
    - `TextViewCreatorOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextEditorFactoryService.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextView(textBuffer: /* ITextBuffer */, roles: /* ITextViewRoleSet */, options: /* TextViewCreatorOptions */);
    ```
- `IDsWpfTextView CreateTextView(ITextBuffer textBuffer, TextViewCreatorOptions options)`
  - Summary: Creates a new instance using
  - Parameters:
    - `ITextBuffer textBuffer`: Text buffer
    - `TextViewCreatorOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextEditorFactoryService.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextView(textBuffer: /* ITextBuffer */, options: /* TextViewCreatorOptions */);
    ```
- `IDsWpfTextView CreateTextView(ITextDataModel dataModel, ITextViewRoleSet roles, IEditorOptions parentOptions, TextViewCreatorOptions options)`
  - Summary: Creates a new instance using
  - Parameters:
    - `ITextDataModel dataModel`: Data model
    - `ITextViewRoleSet roles`: Roles
    - `IEditorOptions parentOptions`: Parent options
    - `TextViewCreatorOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextEditorFactoryService.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextView(dataModel: /* ITextDataModel */, roles: /* ITextViewRoleSet */, parentOptions: /* IEditorOptions */, options: /* TextViewCreatorOptions */);
    ```
- `IDsWpfTextView CreateTextView(ITextViewModel viewModel, ITextViewRoleSet roles, IEditorOptions parentOptions, TextViewCreatorOptions options)`
  - Summary: Creates a new instance using
  - Parameters:
    - `ITextViewModel viewModel`: View model
    - `ITextViewRoleSet roles`: Roles
    - `IEditorOptions parentOptions`: Parent options
    - `TextViewCreatorOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextEditorFactoryService.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextView(viewModel: /* ITextViewModel */, roles: /* ITextViewRoleSet */, parentOptions: /* IEditorOptions */, options: /* TextViewCreatorOptions */);
    ```
- `IDsWpfTextView CreateTextView(TextViewCreatorOptions options)`
  - Summary: Creates a new instance with content type text
  - Parameters:
    - `TextViewCreatorOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextEditorFactoryService.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextView(options: /* TextViewCreatorOptions */);
    ```
- `IDsWpfTextViewHost CreateTextViewHost(IDsWpfTextView wpfTextView, bool setFocus)`
  - Summary: Creates a new instance
  - Parameters:
    - `IDsWpfTextView wpfTextView`: Text view
    - `bool setFocus`: true to set focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextEditorFactoryService.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextViewHost(wpfTextView: /* IDsWpfTextView */, setFocus: /* bool */);
    ```

## Interface `IDsTextView`

dnSpy

**Inherits/Implements:** `ITextView`, `ICommandTargetCollectionProvider`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IDsTextView and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IDsTextView(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextView.cs` (line 27)

## Interface `IDsTextViewLine`

dnSpy

**Inherits/Implements:** `ITextViewLine`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IDsTextViewLine and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IDsTextViewLine(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextViewLine.cs` (line 26)

### Properties

- `bool HasAdornments { get; }`
  - Summary: true if there's at least one adornment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsTextViewLine.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasAdornments;
    ```

## Interface `IDsWpfTextView`

dnSpy

**Inherits/Implements:** `IWpfTextView`, `IDsTextView`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IDsWpfTextView and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IDsWpfTextView(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsWpfTextView.cs` (line 27)

### Methods

- `void InvalidateClassifications(SnapshotSpan span)`
  - Summary: Invalidates classifications
  - Parameters:
    - `SnapshotSpan span`: Span to invalidate
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsWpfTextView.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.InvalidateClassifications(span: /* SnapshotSpan */);
    ```

## Interface `IDsWpfTextViewHost`

dnSpy

**Inherits/Implements:** `IWpfTextViewHost`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IDsWpfTextViewHost and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IDsWpfTextViewHost(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IDsWpfTextViewHost.cs` (line 26)

## Interface `IGlyphTextDotNetTokenMarker`

A method marker created by

**Inherits/Implements:** `IGlyphTextMarker`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextDotNetTokenMarker and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextDotNetTokenMarker(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 258)

### Properties

- `ModuleId Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 262)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `uint Token { get; }`
  - Summary: Gets the token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 267)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

## Interface `IGlyphTextMarker`

A marker created by

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarker and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarker(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 208)

### Properties

- `IClassificationType ClassificationType { get; }`
  - Summary: Gets the classification type or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 227)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ClassificationType;
    ```
- `ImageReference? GlyphImageReference { get; }`
  - Summary: Gets the image reference shown in the glyph margin or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 212)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GlyphImageReference;
    ```
- `int ZIndex { get; }`
  - Summary: Gets the z-index of and , eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 232)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ZIndex;
    ```
- `object Tag { get; }`
  - Summary: Gets the user data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 237)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```
- `string MarkerTypeName { get; }`
  - Summary: Gets the name of the marker format definition or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 217)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MarkerTypeName;
    ```
- `string SelectedMarkerTypeName { get; }`
  - Summary: Gets the name of the marker format definition to use whenever the caret is inside the span; it can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 222)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectedMarkerTypeName;
    ```

## Interface `IGlyphTextMarkerGlyphTag`

glyph tag

**Inherits/Implements:** `IGlyphTag`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarkerGlyphTag and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarkerGlyphTag(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 347)

### Properties

- `ImageReference ImageReference { get; }`
  - Summary: Gets the image reference ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 351)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageReference;
    ```
- `int ZIndex { get; }`
  - Summary: Gets the Z-index ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 356)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ZIndex;
    ```

## Interface `IGlyphTextMarkerHandler`

Handles events

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarkerHandler and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarkerHandler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 32)

### Methods

- `FrameworkElement GetPopupContent(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker)`
  - Summary: Gets the popup content or null if the next handler should be checked. The popup content is shown above the line (eg. breakpoint toolbar settings popup)
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPopupContent(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */);
    ```
- `GlyphTextMarkerToolTip GetToolTipContent(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker)`
  - Summary: Gets the tool tip content or null if the next handler should be checked
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.GetToolTipContent(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */);
    ```
- `IEnumerable<GuidObject> GetContextMenuObjects(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, Point marginRelativePoint)`
  - Summary: Creates context menu objects
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `Point marginRelativePoint`: Position of the mouse pointer relative to the glyph margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetContextMenuObjects(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, marginRelativePoint: /* Point */);
    ```

### Properties

- `IGlyphTextMarkerHandlerMouseProcessor MouseProcessor { get; }`
  - Summary: Gets the mouse processor or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MouseProcessor;
    ```

## Interface `IGlyphTextMarkerHandlerContext`

context

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarkerHandlerContext and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarkerHandlerContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 115)

### Properties

- `IGlyphTextMarkerSpanProvider SpanProvider { get; }`
  - Summary: Gets the span provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 139)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SpanProvider;
    ```
- `IWpfTextView TextView { get; }`
  - Summary: Gets the text view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextView;
    ```
- `IWpfTextViewHost Host { get; }`
  - Summary: Gets the text view host
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 124)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Host;
    ```
- `IWpfTextViewLine Line { get; }`
  - Summary: Gets the line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Line;
    ```
- `IWpfTextViewMargin Margin { get; }`
  - Summary: Gets the glyph margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 119)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Margin;
    ```

## Interface `IGlyphTextMarkerHandlerMouseProcessor`

mouse processor (see also )

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarkerHandlerMouseProcessor and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarkerHandlerMouseProcessor(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 145)

### Methods

- `void OnMouseDown(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Mouse down handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 152)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseDown(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```
- `void OnMouseLeftButtonDown(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Mouse left button down handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 168)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeftButtonDown(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```
- `void OnMouseLeftButtonUp(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Mouse left button up handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 176)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeftButtonUp(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```
- `void OnMouseMove(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseEventArgs e)`
  - Summary: Mouse move handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 200)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseMove(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseEventArgs */);
    ```
- `void OnMouseRightButtonDown(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Mouse right button down handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 184)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseRightButtonDown(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```
- `void OnMouseRightButtonUp(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Mouse right button up handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 192)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseRightButtonUp(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```
- `void OnMouseUp(IGlyphTextMarkerHandlerContext context, IGlyphTextMarker marker, MouseButtonEventArgs e)`
  - Summary: Mouse up handler
  - Parameters:
    - `IGlyphTextMarkerHandlerContext context`: Context
    - `IGlyphTextMarker marker`: Marker
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 160)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseUp(context: /* IGlyphTextMarkerHandlerContext */, marker: /* IGlyphTextMarker */, e: /* MouseButtonEventArgs */);
    ```

## Interface `IGlyphTextMarkerMouseProcessor`

mouse processor (see also )

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarkerMouseProcessor and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarkerMouseProcessor(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 83)

### Methods

- `IEnumerable<GuidObject> GetContextMenuObjects(IGlyphTextMarkerMouseProcessorContext context, Point marginRelativePoint)`
  - Summary: Creates context menu objects
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `Point marginRelativePoint`: Position of the mouse pointer relative to the glyph margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.GetContextMenuObjects(context: /* IGlyphTextMarkerMouseProcessorContext */, marginRelativePoint: /* Point */);
    ```
- `void OnMouseDown(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Mouse down handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseDown(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```
- `void OnMouseEnter(IGlyphTextMarkerMouseProcessorContext context, MouseEventArgs e)`
  - Summary: Mouse enter handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseEnter(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseEventArgs */);
    ```
- `void OnMouseLeave(IGlyphTextMarkerMouseProcessorContext context, MouseEventArgs e)`
  - Summary: Mouse leave handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeave(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseEventArgs */);
    ```
- `void OnMouseLeftButtonDown(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Mouse left button down handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeftButtonDown(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```
- `void OnMouseLeftButtonUp(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Mouse left button up handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 118)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeftButtonUp(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```
- `void OnMouseMove(IGlyphTextMarkerMouseProcessorContext context, MouseEventArgs e)`
  - Summary: Mouse move handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseMove(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseEventArgs */);
    ```
- `void OnMouseRightButtonDown(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Mouse right button down handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseRightButtonDown(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```
- `void OnMouseRightButtonUp(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Mouse right button up handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseRightButtonUp(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```
- `void OnMouseUp(IGlyphTextMarkerMouseProcessorContext context, MouseButtonEventArgs e)`
  - Summary: Mouse up handler
  - Parameters:
    - `IGlyphTextMarkerMouseProcessorContext context`: Context
    - `MouseButtonEventArgs e`: Mouse event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseUp(context: /* IGlyphTextMarkerMouseProcessorContext */, e: /* MouseButtonEventArgs */);
    ```

## Interface `IGlyphTextMarkerMouseProcessorContext`

context

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarkerMouseProcessorContext and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarkerMouseProcessorContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 48)

### Properties

- `IGlyphTextMarkerSpanProvider SpanProvider { get; }`
  - Summary: Gets the span provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SpanProvider;
    ```
- `IGlyphTextMarker[] Markers { get; }`
  - Summary: Sorted markers shown in the glyph margin. The first marker is the top most marker.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Markers;
    ```
- `IWpfTextView TextView { get; }`
  - Summary: Gets the text view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextView;
    ```
- `IWpfTextViewHost Host { get; }`
  - Summary: Gets the text view host
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Host;
    ```
- `IWpfTextViewLine Line { get; }`
  - Summary: Gets the line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Line;
    ```
- `IWpfTextViewMargin Margin { get; }`
  - Summary: Gets the glyph margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Margin;
    ```

## Interface `IGlyphTextMarkerMouseProcessorProvider`

Creates s. You must this interface with a . Optional attributes: , .

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarkerMouseProcessorProvider and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarkerMouseProcessorProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 35)

### Methods

- `IGlyphTextMarkerMouseProcessor GetAssociatedMouseProcessor(IWpfTextViewHost wpfTextViewHost, IWpfTextViewMargin margin)`
  - Summary: Creates a or returns null
  - Parameters:
    - `IWpfTextViewHost wpfTextViewHost`: Text view host
    - `IWpfTextViewMargin margin`: Margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerMouseProcessor.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAssociatedMouseProcessor(wpfTextViewHost: /* IWpfTextViewHost */, margin: /* IWpfTextViewMargin */);
    ```

## Interface `IGlyphTextMarkerService`

Marks text and shows a glyph in the glyph margin

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarkerService and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarkerService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 118)

### Methods

- `GlyphTextMarkerAndSpan[] GetMarkers(ITextView textView, SnapshotSpan span)`
  - Summary: Gets markers
  - Parameters:
    - `ITextView textView`: Text view
    - `SnapshotSpan span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMarkers(textView: /* ITextView */, span: /* SnapshotSpan */);
    ```
- `IGlyphTextMarker AddMarker(GlyphTextMarkerLocationInfo location, ImageReference? glyphImage, string markerTypeName, string selectedMarkerTypeName, IClassificationType classificationType, int zIndex, object tag = null, IGlyphTextMarkerHandler handler = null, Func<ITextView, bool> textViewFilter = null)`
  - Summary: Adds a marker
  - Parameters:
    - `GlyphTextMarkerLocationInfo location`: Location
    - `ImageReference? glyphImage`: Image shown in the glyph margin or null if none
    - `string markerTypeName`: Name of a (or an ) or null. It should have a background color and an optional foreground color for the border
    - `string selectedMarkerTypeName`: Name of a or null. It's used whenever the caret is inside the text marker.
    - `IClassificationType classificationType`: Classification type or null. Only the foreground color is needed. If it has a background color, it will hide the text markers shown in the text marker layer (eg. search result, highlighted reference)
    - `int zIndex`: Z-index of and , eg.
    - `object tag` (default: `null`): User data
    - `IGlyphTextMarkerHandler handler` (default: `null`): Glyph handler or null
    - `Func<ITextView, bool> textViewFilter` (default: `null`): Filters out non-supported text views
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 155)
  - Example:
    ```csharp
    // Example invocation
    instance.AddMarker(location: /* GlyphTextMarkerLocationInfo */, glyphImage: /* ImageReference? */, markerTypeName: /* string */, selectedMarkerTypeName: /* string */, classificationType: /* IClassificationType */, zIndex: /* int */, tag: /* object */, handler: /* IGlyphTextMarkerHandler */, textViewFilter: /* Func<ITextView, bool> */);
    ```
- `IGlyphTextMethodMarker AddMarker(ModuleTokenId tokenId, uint ilOffset, ImageReference? glyphImage, string markerTypeName, string selectedMarkerTypeName, IClassificationType classificationType, int zIndex, object tag = null, IGlyphTextMarkerHandler handler = null, Func<ITextView, bool> textViewFilter = null)`
  - Summary: Adds a marker
  - Parameters:
    - `ModuleTokenId tokenId`: Method token
    - `uint ilOffset`: Method offset
    - `ImageReference? glyphImage`: Image shown in the glyph margin or null if none
    - `string markerTypeName`: Name of a (or an ) or null. It should have a background color and an optional foreground color for the border
    - `string selectedMarkerTypeName`: Name of a or null. It's used whenever the caret is inside the text marker.
    - `IClassificationType classificationType`: Classification type or null. Only the foreground color is needed. If it has a background color, it will hide the text markers shown in the text marker layer (eg. search result, highlighted reference)
    - `int zIndex`: Z-index of and , eg.
    - `object tag` (default: `null`): User data
    - `IGlyphTextMarkerHandler handler` (default: `null`): Glyph handler or null
    - `Func<ITextView, bool> textViewFilter` (default: `null`): Filters out non-supported text views
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    instance.AddMarker(tokenId: /* ModuleTokenId */, ilOffset: /* uint */, glyphImage: /* ImageReference? */, markerTypeName: /* string */, selectedMarkerTypeName: /* string */, classificationType: /* IClassificationType */, zIndex: /* int */, tag: /* object */, handler: /* IGlyphTextMarkerHandler */, textViewFilter: /* Func<ITextView, bool> */);
    ```
- `void Remove(IEnumerable<IGlyphTextMarker> markers)`
  - Summary: Removes markers
  - Parameters:
    - `IEnumerable<IGlyphTextMarker> markers`: Markers to remove
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 167)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(markers: /* IEnumerable<IGlyphTextMarker> */);
    ```
- `void Remove(IGlyphTextMarker marker)`
  - Summary: Removes a marker
  - Parameters:
    - `IGlyphTextMarker marker`: Marker to remove
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 161)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(marker: /* IGlyphTextMarker */);
    ```
- `void SetDotNetSpanMap(ITextView textView, IDotNetSpanMap map)`
  - Summary: Should be called whenever gets a new
  - Parameters:
    - `ITextView textView`: Text view
    - `IDotNetSpanMap map`: New map or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 124)
  - Example:
    ```csharp
    // Example invocation
    instance.SetDotNetSpanMap(textView: /* ITextView */, map: /* IDotNetSpanMap */);
    ```

## Interface `IGlyphTextMarkerSpanProvider`

Returns spans of markers

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarkerSpanProvider and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarkerSpanProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 103)

### Methods

- `SnapshotSpan GetSpan(IGlyphTextMarker marker)`
  - Summary: Gets the snapshot span of a marker
  - Parameters:
    - `IGlyphTextMarker marker`: Marker
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerHandler.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpan(marker: /* IGlyphTextMarker */);
    ```

## Interface `IGlyphTextMarkerTag`

text marker tag

**Inherits/Implements:** `ITag`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMarkerTag and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMarkerTag(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 295)

### Properties

- `int ZIndex { get; }`
  - Summary: Gets the Z-index ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 309)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ZIndex;
    ```
- `string MarkerTypeName { get; }`
  - Summary: Name of a (or an ) ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 299)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MarkerTypeName;
    ```
- `string SelectedMarkerTypeName { get; }`
  - Summary: Gets the name of the marker format definition to use whenever the caret is inside the span; it can be null ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 304)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectedMarkerTypeName;
    ```

## Interface `IGlyphTextMethodMarker`

A method marker created by

**Inherits/Implements:** `IGlyphTextMarker`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IGlyphTextMethodMarker and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IGlyphTextMethodMarker(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 243)

### Properties

- `ModuleTokenId Method { get; }`
  - Summary: Gets the method token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 247)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Method;
    ```
- `uint ILOffset { get; }`
  - Summary: Gets the IL offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IGlyphTextMarkerService.cs` (line 252)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ILOffset;
    ```

## Interface `ILineSeparatorTag`

Line separator tag

**Inherits/Implements:** `ITag`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.ILineSeparatorTag and call its members.
var instance = new dnSpy.Contracts.Text.Editor.ILineSeparatorTag(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILineSeparatorTag.cs` (line 26)

### Properties

- `bool IsPhysicalLine { get; }`
  - Summary: true to put the line separator after the real line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILineSeparatorTag.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPhysicalLine;
    ```

## Interface `ILogEditor`

A text control that allows appending text. Writing text is thread safe.

**Inherits/Implements:** `IUIObjectProvider2`, `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.ILogEditor and call its members.
var instance = new dnSpy.Contracts.Text.Editor.ILogEditor(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 29)

### Methods

- `string GetText()`
  - Summary: Gets all text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.GetText();
    ```
- `void Clear()`
  - Summary: Clears all text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```
- `void Write(IEnumerable<ColorAndText> text)`
  - Summary: Writes text
  - Parameters:
    - `IEnumerable<ColorAndText> text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* IEnumerable<ColorAndText> */);
    ```
- `void Write(string text, TextColor color)`
  - Summary: Writes text
  - Parameters:
    - `string text`: Text
    - `TextColor color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, color: /* TextColor */);
    ```
- `void Write(string text, object color)`
  - Summary: Writes text
  - Parameters:
    - `string text`: Text
    - `object color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, color: /* object */);
    ```
- `void WriteLine(string text, TextColor color)`
  - Summary: Writes text
  - Parameters:
    - `string text`: Text
    - `TextColor color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLine(text: /* string */, color: /* TextColor */);
    ```
- `void WriteLine(string text, object color)`
  - Summary: Writes text
  - Parameters:
    - `string text`: Text
    - `object color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLine(text: /* string */, color: /* object */);
    ```

### Properties

- `IDsWpfTextView TextView { get; }`
  - Summary: Gets the text view. It's not thread safe.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextView;
    ```
- `IDsWpfTextViewHost TextViewHost { get; }`
  - Summary: Gets the text view host. It's not thread safe.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewHost;
    ```
- `WordWrapStyles WordWrapStyle { get; set; }`
  - Summary: Enables/disables word wrapping
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.WordWrapStyle;
    ```
- `bool ShowLineNumbers { get; set; }`
  - Summary: true to show line numbers
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditor.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowLineNumbers;
    ```

## Interface `ILogEditorProvider`

Creates instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.ILogEditorProvider and call its members.
var instance = new dnSpy.Contracts.Text.Editor.ILogEditorProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditorProvider.cs` (line 24)

### Methods

- `ILogEditor Create(LogEditorOptions options)`
  - Summary: Creates a new instance
  - Parameters:
    - `LogEditorOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILogEditorProvider.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(options: /* LogEditorOptions */);
    ```

## Interface `IMarginContextMenuHandler`

Creates context menu objects

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IMarginContextMenuHandler and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IMarginContextMenuHandler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IMarginContextMenuHandler.cs` (line 45)

### Methods

- `IEnumerable<GuidObject> GetContextMenuObjects(Point marginRelativePoint)`
  - Summary: Creates context menu objects
  - Parameters:
    - `Point marginRelativePoint`: Position of the mouse pointer relative to the glyph margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IMarginContextMenuHandler.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.GetContextMenuObjects(marginRelativePoint: /* Point */);
    ```

## Interface `IMarginContextMenuHandlerProvider`

Creates s or returns null. You must this interface and add a with the name of the margin (eg. ). Optional attribute: .

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IMarginContextMenuHandlerProvider and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IMarginContextMenuHandlerProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IMarginContextMenuHandler.cs` (line 32)

### Methods

- `IMarginContextMenuHandler Create(IWpfTextViewHost wpfTextViewHost, IWpfTextViewMargin margin)`
  - Summary: Creates s or returns null
  - Parameters:
    - `IWpfTextViewHost wpfTextViewHost`: Text view host
    - `IWpfTextViewMargin margin`: Margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IMarginContextMenuHandler.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(wpfTextViewHost: /* IWpfTextViewHost */, margin: /* IWpfTextViewMargin */);
    ```

## Interface `IMarginContextMenuService`

Creates a that uses s to create objects.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IMarginContextMenuService and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IMarginContextMenuService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IMarginContextMenuHandlerProviderService.cs` (line 28)

### Methods

- `IGuidObjectsProvider Create(IWpfTextViewHost wpfTextViewHost, IWpfTextViewMargin margin, string marginName)`
  - Summary: Creates a
  - Parameters:
    - `IWpfTextViewHost wpfTextViewHost`: Text view host
    - `IWpfTextViewMargin margin`: Margin
    - `string marginName`: Margin name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IMarginContextMenuHandlerProviderService.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(wpfTextViewHost: /* IWpfTextViewHost */, margin: /* IWpfTextViewMargin */, marginName: /* string */);
    ```

## Interface `IReplaceListener`

Can cancel replaces (without having to create read-only regions)

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IReplaceListener and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IReplaceListener(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IReplaceListener.cs` (line 27)

### Methods

- `bool CanReplace(SnapshotSpan span, string newText)`
  - Summary: Returns true if can be modified and replaced with new content
  - Parameters:
    - `SnapshotSpan span`: Span to be replaced if all s return true. This is the latest textview snapshot ()
    - `string newText`: New text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IReplaceListener.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.CanReplace(span: /* SnapshotSpan */, newText: /* string */);
    ```

## Interface `IReplaceListenerProvider`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IReplaceListenerProvider and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IReplaceListenerProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IReplaceListenerProvider.cs` (line 26)

### Methods

- `IReplaceListener Create(ITextView textView)`
  - Summary: Creates a or returns null
  - Parameters:
    - `ITextView textView`: Text view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IReplaceListenerProvider.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(textView: /* ITextView */);
    ```

## Enum `IndentStyle`

Indent style

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.IndentStyle and call its members.
var instance = new dnSpy.Contracts.Text.Editor.IndentStyle(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IndentStyle.cs` (line 24)

### Members

- `None`: No indentation, always move caret to column 0
- `Block`: Block, use same indentation as the previous line (or first non-empty line)
- `Smart`: Use the language service to find the correct indentation

## Class `IsOverlayLayerAttribute`

Creates an adornment layer that is on top of all normal layers, see also

**Inherits/Implements:** `SingletonBaseMetadataAttribute`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.IsOverlayLayerAttribute(isOverlayLayer: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IsOverlayLayerAttribute.cs` (line 26)

### Constructors

- `public IsOverlayLayerAttribute(bool isOverlayLayer)`
  - Summary: Constructor
  - Parameters:
    - `bool isOverlayLayer`: true if it's an overlay layer, false if it's a normal layer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IsOverlayLayerAttribute.cs` (line 31)

### Properties

- `public bool IsOverlayLayer { get; }`
  - Summary: true if it's an overlay layer, false if it's a normal layer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/IsOverlayLayerAttribute.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOverlayLayer;
    ```

## Enum `LayerKind`

Layer kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.LayerKind and call its members.
var instance = new dnSpy.Contracts.Text.Editor.LayerKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/LayerKind.cs` (line 24)

### Members

- `Normal`: Normal layer
- `Overlay`: Overlay layer. It's shown above all layers
- `Underlay`: Underlay layer. It's shown below all layers

## Class `LayerKindAttribute`

Adds a layer kind

**Inherits/Implements:** `SingletonBaseMetadataAttribute`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.LayerKindAttribute(kind: /* LayerKind */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/LayerKindAttribute.cs` (line 26)

### Constructors

- `public LayerKindAttribute(LayerKind kind)`
  - Summary: Constructor
  - Parameters:
    - `LayerKind kind`: Kind of layer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/LayerKindAttribute.cs` (line 31)

### Properties

- `public LayerKind LayerKind { get; }`
  - Summary: Layer kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/LayerKindAttribute.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LayerKind;
    ```

## Class `LineSeparatorTag`

Line separator tag

**Inherits/Implements:** `ILineSeparatorTag`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.LineSeparatorTag(isPhysicalLine: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILineSeparatorTag.cs` (line 36)

### Constructors

- `public LineSeparatorTag(bool isPhysicalLine)`
  - Summary: Constructor
  - Parameters:
    - `bool isPhysicalLine`: true to put the line separator after the real line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILineSeparatorTag.cs` (line 46)

### Properties

- `public bool IsPhysicalLine { get; }`
  - Summary: true to put the line separator after the real line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/ILineSeparatorTag.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPhysicalLine;
    ```

## Class `LogEditorOptions`

options

**Inherits/Implements:** `CommonTextEditorOptions`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.LogEditorOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/LogEditorOptions.cs` (line 26)

### Constructors

- `public LogEditorOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/LogEditorOptions.cs` (line 35)

### Methods

- `public new LogEditorOptions Clone()`
  - Summary: Clones this
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/LogEditorOptions.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

### Properties

- `public List<string> ExtraRoles { get; }`
  - Summary: Extra text view roles
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/LogEditorOptions.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExtraRoles;
    ```

## Class `MarginNameAttribute`

Adds the name of a margin

**Inherits/Implements:** `SingletonBaseMetadataAttribute`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.MarginNameAttribute(marginName: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/MarginNameAttribute.cs` (line 28)

### Constructors

- `public MarginNameAttribute(string marginName)`
  - Summary: Constructor
  - Parameters:
    - `string marginName`: Name of margin, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/MarginNameAttribute.cs` (line 33)

### Properties

- `public string MarginName { get; }`
  - Summary: Name of margin, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/MarginNameAttribute.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MarginName;
    ```

## Class `PredefinedDsAdornmentLayers`

dnSpy adornment layers

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.PredefinedDsAdornmentLayers members directly without instantiation.
dnSpy.Contracts.Text.Editor.PredefinedDsAdornmentLayers./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsAdornmentLayers.cs` (line 24)

### Fields

- `public const string BackgroundImage = "dnSpy-" + nameof(BackgroundImage)`
  - Summary: Background image adornment layer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsAdornmentLayers.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsAdornmentLayers.BackgroundImage;
    ```
- `public const string BottomLayer = "dnSpy-" + nameof(BottomLayer)`
  - Summary: Bottom layer. All layers should normally be after this layer.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsAdornmentLayers.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsAdornmentLayers.BottomLayer;
    ```
- `public const string GlyphTextMarker = "dnSpy-" + nameof(GlyphTextMarker)`
  - Summary: 's adornment layer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsAdornmentLayers.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsAdornmentLayers.GlyphTextMarker;
    ```
- `public const string IntraTextAdornment = "Intra Text Adornment"`
  - Summary: Intra text adornment layer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsAdornmentLayers.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsAdornmentLayers.IntraTextAdornment;
    ```
- `public const string LineSeparator = "dnSpy-" + nameof(LineSeparator)`
  - Summary: Line separator adornment layer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsAdornmentLayers.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsAdornmentLayers.LineSeparator;
    ```
- `public const string NegativeTextMarkerLayer = "negativetextmarkerlayer"`
  - Summary: Text marker adornment layer for markers with a negative z-index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsAdornmentLayers.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsAdornmentLayers.NegativeTextMarkerLayer;
    ```
- `public const string Search = "dnSpy-" + nameof(Search)`
  - Summary: Search adornment layer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsAdornmentLayers.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsAdornmentLayers.Search;
    ```
- `public const string TopLayer = "dnSpy-" + nameof(TopLayer)`
  - Summary: Top layer. All layers should normally be before this layer.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsAdornmentLayers.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsAdornmentLayers.TopLayer;
    ```

## Class `PredefinedDsGlyphFactoryProviderNames`

dnSpy names

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.PredefinedDsGlyphFactoryProviderNames members directly without instantiation.
dnSpy.Contracts.Text.Editor.PredefinedDsGlyphFactoryProviderNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsGlyphFactoryProviderNames.cs` (line 26)

### Fields

- `public const string GlyphTextViewMarker = "dnSpy" + nameof(GlyphTextViewMarker)`
  - Summary: Glyph textview marker
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsGlyphFactoryProviderNames.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsGlyphFactoryProviderNames.GlyphTextViewMarker;
    ```

## Class `PredefinedDsGlyphMouseProcessorProviders`

Predefined dnSpy s

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.PredefinedDsGlyphMouseProcessorProviders members directly without instantiation.
dnSpy.Contracts.Text.Editor.PredefinedDsGlyphMouseProcessorProviders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsGlyphMouseProcessorProviders.cs` (line 26)

### Fields

- `public const string GlyphTextMarkerService = nameof(GlyphTextMarkerService)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsGlyphMouseProcessorProviders.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsGlyphMouseProcessorProviders.GlyphTextMarkerService;
    ```

## Class `PredefinedDsGlyphTextMarkerMouseProcessorProviderNames`

names

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.PredefinedDsGlyphTextMarkerMouseProcessorProviderNames members directly without instantiation.
dnSpy.Contracts.Text.Editor.PredefinedDsGlyphTextMarkerMouseProcessorProviderNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsGlyphTextMarkerMouseProcessorProviderNames.cs` (line 24)

### Fields

- `public const string DebuggerBreakpoints = nameof(DebuggerBreakpoints)`
  - Summary: Debugger breakpoints mouse processor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsGlyphTextMarkerMouseProcessorProviderNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsGlyphTextMarkerMouseProcessorProviderNames.DebuggerBreakpoints;
    ```

## Class `PredefinedDsMarginNames`

Predefined dnSpy margin names

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.PredefinedDsMarginNames members directly without instantiation.
dnSpy.Contracts.Text.Editor.PredefinedDsMarginNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsMarginNames.cs` (line 24)

### Fields

- `public const string CustomLineNumber = "dnSpy-" + nameof(CustomLineNumber)`
  - Summary: Custom line number margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsMarginNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsMarginNames.CustomLineNumber;
    ```

## Class `PredefinedDsMouseProcessorProviders`

Predefined dnSpy s

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.PredefinedDsMouseProcessorProviders members directly without instantiation.
dnSpy.Contracts.Text.Editor.PredefinedDsMouseProcessorProviders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsMouseProcessorProviders.cs` (line 28)

### Fields

- `public const string DocumentViewer = nameof(DocumentViewer)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsMouseProcessorProviders.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsMouseProcessorProviders.DocumentViewer;
    ```
- `public const string IntellisensePresenter = nameof(IntellisensePresenter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsMouseProcessorProviders.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsMouseProcessorProviders.IntellisensePresenter;
    ```
- `public const string Uri = nameof(Uri)`
  - Summary: URI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsMouseProcessorProviders.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsMouseProcessorProviders.Uri;
    ```

## Class `PredefinedDsTextViewRoles`

Predefined dnSpy textview roles

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles members directly without instantiation.
dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 28)

### Fields

- `public const string CSharpRepl = "dnSpy-" + nameof(CSharpRepl)`
  - Summary: C# REPL
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 57)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.CSharpRepl;
    ```
- `public const string CanHaveBackgroundImage = "dnSpy-" + nameof(CanHaveBackgroundImage)`
  - Summary: Allows background images to be used
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 117)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.CanHaveBackgroundImage;
    ```
- `public const string CanHaveCurrentLineHighlighter = "dnSpy-" + nameof(CanHaveCurrentLineHighlighter)`
  - Summary: Allows the current line highlighter to be used. Not needed if is already used.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 100)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.CanHaveCurrentLineHighlighter;
    ```
- `public const string CanHaveGlyphTextMarkerService = "dnSpy-" + nameof(CanHaveGlyphTextMarkerService)`
  - Summary: services can be used. Not needed if is already used.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 94)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.CanHaveGlyphTextMarkerService;
    ```
- `public const string CanHaveIntellisenseControllers = "dnSpy-" + nameof(CanHaveIntellisenseControllers)`
  - Summary: Allows intellisense controllers
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 127)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.CanHaveIntellisenseControllers;
    ```
- `public const string CanHaveLineCompressor = "dnSpy-" + nameof(CanHaveLineCompressor)`
  - Summary: Allows line compressor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 122)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.CanHaveLineCompressor;
    ```
- `public const string CanHaveLineNumberMargin = "dnSpy-" + nameof(CanHaveLineNumberMargin)`
  - Summary: Allows the line number margin to be used. Not needed if is already used.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 106)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.CanHaveLineNumberMargin;
    ```
- `public const string CanHaveLineSeparator = "dnSpy-" + nameof(CanHaveLineSeparator)`
  - Summary: Allows line separators to be used. Not needed if is already used.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 112)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.CanHaveLineSeparator;
    ```
- `public const string CodeEditor = "dnSpy-" + nameof(CodeEditor)`
  - Summary: text view role
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 67)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.CodeEditor;
    ```
- `public const string CustomLineNumberMargin = "dnSpy-" + nameof(CustomLineNumberMargin)`
  - Summary: Enables the custom line number margin, see documentation for more info.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.CustomLineNumberMargin;
    ```
- `public const string DocumentViewer = "dnSpy-" + nameof(DocumentViewer)`
  - Summary: text view role
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.DocumentViewer;
    ```
- `public const string LogEditor = "dnSpy-" + nameof(LogEditor)`
  - Summary: text view role
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.LogEditor;
    ```
- `public const string OutputTextPane = "dnSpy-" + nameof(OutputTextPane)`
  - Summary: text view role
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.OutputTextPane;
    ```
- `public const string ReplEditor = "dnSpy-" + nameof(ReplEditor)`
  - Summary: text view role
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.ReplEditor;
    ```
- `public const string RoslynCSharpCodeEditor = "dnSpy-" + nameof(RoslynCSharpCodeEditor)`
  - Summary: Roslyn code editor (C#)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 77)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.RoslynCSharpCodeEditor;
    ```
- `public const string RoslynCodeEditor = "dnSpy-" + nameof(RoslynCodeEditor)`
  - Summary: Roslyn code editor (any supported language, eg. C# and Visual Basic)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 72)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.RoslynCodeEditor;
    ```
- `public const string RoslynRepl = "dnSpy-" + nameof(RoslynRepl)`
  - Summary: Roslyn REPL (any supported language, eg. C# and Visual Basic)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.RoslynRepl;
    ```
- `public const string RoslynVisualBasicCodeEditor = "dnSpy-" + nameof(RoslynVisualBasicCodeEditor)`
  - Summary: Roslyn code editor (Visual Basic)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 82)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.RoslynVisualBasicCodeEditor;
    ```
- `public const string VisualBasicRepl = "dnSpy-" + nameof(VisualBasicRepl)`
  - Summary: Visual Basic REPL
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedDsTextViewRoles.cs` (line 62)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedDsTextViewRoles.VisualBasicRepl;
    ```

## Class `PredefinedSpaceReservationManagerNames`

Predefined names

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.PredefinedSpaceReservationManagerNames members directly without instantiation.
dnSpy.Contracts.Text.Editor.PredefinedSpaceReservationManagerNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedSpaceReservationManagerNames.cs` (line 27)

### Fields

- `public const string CurrentLine = "currentline"`
  - Summary: Current line space reservation manager name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedSpaceReservationManagerNames.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedSpaceReservationManagerNames.CurrentLine;
    ```
- `public const string ToolTip = "ToolTip"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/PredefinedSpaceReservationManagerNames.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.PredefinedSpaceReservationManagerNames.ToolTip;
    ```

## Class `TextMarkerServiceZIndexes`

Text marker service Z-indexes. Markers with a negative z-index are placed in a marker layer below most other layers.

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.TextMarkerServiceZIndexes members directly without instantiation.
dnSpy.Contracts.Text.Editor.TextMarkerServiceZIndexes./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextMarkerServiceZIndexes.cs` (line 25)

### Fields

- `public const int ActiveStatement = -1000`
  - Summary: (Debugger) Z-index of active statement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextMarkerServiceZIndexes.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.TextMarkerServiceZIndexes.ActiveStatement;
    ```
- `public const int FindMatch = 5000`
  - Summary: Find match
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextMarkerServiceZIndexes.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.TextMarkerServiceZIndexes.FindMatch;
    ```
- `public const int HighlightedDefinition = 0`
  - Summary: Highlighted definition
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextMarkerServiceZIndexes.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.TextMarkerServiceZIndexes.HighlightedDefinition;
    ```
- `public const int HighlightedReference = 0`
  - Summary: Highlighted reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextMarkerServiceZIndexes.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.TextMarkerServiceZIndexes.HighlightedReference;
    ```
- `public const int HighlightedWrittenReference = 0`
  - Summary: Highlighted written reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextMarkerServiceZIndexes.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.TextMarkerServiceZIndexes.HighlightedWrittenReference;
    ```

## Class `TextViewCreatorOptions`

creator options

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Editor.TextViewCreatorOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextViewCreatorOptions.cs` (line 29)

### Constructors

- `public TextViewCreatorOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextViewCreatorOptions.cs` (line 54)

### Methods

- `public TextViewCreatorOptions Clone()`
  - Summary: Clones this
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextViewCreatorOptions.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```
- `public TextViewCreatorOptions CopyTo(TextViewCreatorOptions other)`
  - Summary: Copy this to
  - Parameters:
    - `TextViewCreatorOptions other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextViewCreatorOptions.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* TextViewCreatorOptions */);
    ```

### Properties

- `public Func<GuidObjectsProviderArgs, IEnumerable<GuidObject>> CreateGuidObjects { get; set; }`
  - Summary: Creates s, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextViewCreatorOptions.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CreateGuidObjects;
    ```
- `public Guid? MenuGuid { get; set; }`
  - Summary: Guid of context menu or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextViewCreatorOptions.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MenuGuid;
    ```
- `public bool EnableUndoHistory { get; set; }`
  - Summary: true to enable undo/redo history. Default value is true
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextViewCreatorOptions.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EnableUndoHistory;
    ```

## Class `TextViewExtensions`

Text view extensions

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.TextViewExtensions members directly without instantiation.
dnSpy.Contracts.Text.Editor.TextViewExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextViewExtensions.cs` (line 28)

### Methods

- `public static void EnsureCaretVisible(this ITextView textView, bool center = false)`
  - Summary: Scrolls the view to make the caret visible. If it's not visible, it's centered.
  - Parameters:
    - `this ITextView textView`: Text view
    - `bool center` (default: `false`): true to center the caret
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/TextViewExtensions.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.TextViewExtensions.EnsureCaretVisible(textView: /* ITextView */, center: /* bool */);
    ```

## Class `WordWrapStylesConstants`

constants

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.WordWrapStylesConstants members directly without instantiation.
dnSpy.Contracts.Text.Editor.WordWrapStylesConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/WordWrapStylesConstants.cs` (line 26)

### Fields

- `public const WordWrapStyles DefaultDisabled = WordWrapStyles.None | WordWrapStyles.VisibleGlyphs | WordWrapStyles.AutoIndent`
  - Summary: Default disabled word wrap styles
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/WordWrapStylesConstants.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.WordWrapStylesConstants.DefaultDisabled;
    ```
- `public const WordWrapStyles DefaultEnabled = DefaultDisabled | WordWrapStyles.WordWrap`
  - Summary: Default enabled word wrap styles
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/WordWrapStylesConstants.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.WordWrapStylesConstants.DefaultEnabled;
    ```
- `public const WordWrapStyles DefaultValue = DefaultEnabled`
  - Summary: Default word wrap styles value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/WordWrapStylesConstants.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Editor.WordWrapStylesConstants.DefaultValue;
    ```

