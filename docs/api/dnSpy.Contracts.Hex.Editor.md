# Namespace `dnSpy.Contracts.Hex.Editor`

## Class `BufferLinesChangedEventArgs`

changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.BufferLinesChangedEventArgs(oldBufferLines: /* HexBufferLineFormatter */, newBufferLines: /* HexBufferLineFormatter */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 253)

### Constructors

- `public BufferLinesChangedEventArgs(HexBufferLineFormatter oldBufferLines, HexBufferLineFormatter newBufferLines)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferLineFormatter oldBufferLines`: Old instance
    - `HexBufferLineFormatter newBufferLines`: New instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 269)

### Properties

- `public HexBufferLineFormatter NewBufferLines { get; }`
  - Summary: Gets the new instance. This instance is never null.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 262)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewBufferLines;
    ```
- `public HexBufferLineFormatter OldBufferLines { get; }`
  - Summary: Gets the old instance. This value can be null.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 257)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldBufferLines;
    ```

## Class `DefaultHexViewHostOptions`

Default options

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions members directly without instantiation.
dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 26)

### Fields

- `public const string GlyphMarginName = "HexViewHost/GlyphMargin"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.GlyphMarginName;
    ```
- `public const string HorizontalScrollBarName = "HexViewHost/HorizontalScrollBar"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.HorizontalScrollBarName;
    ```
- `public const string IsInContrastModeName = "HexViewHost/IsInContrastMode"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.IsInContrastModeName;
    ```
- `public const string SelectionMarginName = "HexViewHost/SelectionMargin"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.SelectionMarginName;
    ```
- `public const string VerticalScrollBarName = "HexViewHost/VerticalScrollBar"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.VerticalScrollBarName;
    ```
- `public const string ZoomControlName = "HexViewHost/ZoomControl"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.ZoomControlName;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> GlyphMarginId = new VSTE.EditorOptionKey<bool>(GlyphMarginName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.GlyphMarginId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> HorizontalScrollBarId = new VSTE.EditorOptionKey<bool>(HorizontalScrollBarName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.HorizontalScrollBarId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> IsInContrastModeId = new VSTE.EditorOptionKey<bool>(IsInContrastModeName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.IsInContrastModeId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> SelectionMarginId = new VSTE.EditorOptionKey<bool>(SelectionMarginName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.SelectionMarginId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> VerticalScrollBarId = new VSTE.EditorOptionKey<bool>(VerticalScrollBarName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.VerticalScrollBarId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> ZoomControlId = new VSTE.EditorOptionKey<bool>(ZoomControlName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewHostOptions.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewHostOptions.ZoomControlId;
    ```

## Class `DefaultHexViewOptions`

Default options

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions members directly without instantiation.
dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 26)

### Fields

- `public const int DefaultHighlightCurrentValueDelayMilliSeconds = 100`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 83)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.DefaultHighlightCurrentValueDelayMilliSeconds;
    ```
- `public const int DefaultRefreshScreenOnChangeWaitMilliSeconds = 150`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 64)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.DefaultRefreshScreenOnChangeWaitMilliSeconds;
    ```
- `public const string BasePositionName = "HexView/BasePosition"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.BasePositionName;
    ```
- `public const string BytesPerLineName = "HexView/BytesPerLine"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.BytesPerLineName;
    ```
- `public const string ColumnGroupLine0Name = "HexView/ColumnGroupLine0"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ColumnGroupLine0Name;
    ```
- `public const string ColumnGroupLine1Name = "HexView/ColumnGroupLine1"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 75)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ColumnGroupLine1Name;
    ```
- `public const string ColumnLine0Name = "HexView/ColumnLine0"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 69)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ColumnLine0Name;
    ```
- `public const string ColumnLine1Name = "HexView/ColumnLine1"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 71)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ColumnLine1Name;
    ```
- `public const string EnableColorizationName = "HexView/EnableColorization"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.EnableColorizationName;
    ```
- `public const string EncodingCodePageName = "HexView/EncodingCodePage"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 84)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.EncodingCodePageName;
    ```
- `public const string EndPositionName = "HexView/EndPosition"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.EndPositionName;
    ```
- `public const string GroupSizeInBytesName = "HexView/GroupSizeInBytes"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 54)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.GroupSizeInBytesName;
    ```
- `public const string HexOffsetFormatName = "HexView/HexOffsetFormat"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HexOffsetFormatName;
    ```
- `public const string HexValuesDisplayFormatName = "HexView/HexValuesDisplayFormat"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HexValuesDisplayFormatName;
    ```
- `public const string HighlightActiveColumnName = "HexView/HighlightActiveColumn"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 77)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HighlightActiveColumnName;
    ```
- `public const string HighlightCurrentValueDelayMilliSecondsName = "HexView/HighlightCurrentValueDelayMilliSeconds"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 81)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HighlightCurrentValueDelayMilliSecondsName;
    ```
- `public const string HighlightCurrentValueName = "HexView/HighlightCurrentValue"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 79)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HighlightCurrentValueName;
    ```
- `public const string HighlightStructureUnderMouseCursorName = "HexView/HighlightStructureUnderMouseCursor"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 86)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HighlightStructureUnderMouseCursorName;
    ```
- `public const string OffsetBitSizeName = "HexView/OffsetBitSize"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.OffsetBitSizeName;
    ```
- `public const string OffsetLowerCaseHexName = "HexView/OffsetLowerCaseHex"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.OffsetLowerCaseHexName;
    ```
- `public const string RefreshScreenOnChangeName = "HexView/RefreshScreenOnChange"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 60)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.RefreshScreenOnChangeName;
    ```
- `public const string RefreshScreenOnChangeWaitMilliSecondsName = "HexView/RefreshScreenOnChangeWaitMilliSeconds"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 62)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.RefreshScreenOnChangeWaitMilliSecondsName;
    ```
- `public const string RemoveExtraTextLineVerticalPixelsName = "HexView/RemoveExtraTextLineVerticalPixels"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 65)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.RemoveExtraTextLineVerticalPixelsName;
    ```
- `public const string ShowAsciiColumnName = "HexView/ShowAsciiColumn"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ShowAsciiColumnName;
    ```
- `public const string ShowColumnLinesName = "HexView/ShowColumnLines"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 67)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ShowColumnLinesName;
    ```
- `public const string ShowOffsetColumnName = "HexView/ShowOffsetColumn"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ShowOffsetColumnName;
    ```
- `public const string ShowValuesColumnName = "HexView/ShowValuesColumn"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ShowValuesColumnName;
    ```
- `public const string StartPositionName = "HexView/StartPosition"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.StartPositionName;
    ```
- `public const string UseRelativePositionsName = "HexView/UseRelativePositions"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.UseRelativePositionsName;
    ```
- `public const string ValuesLowerCaseHexName = "HexView/ValuesLowerCaseHex"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ValuesLowerCaseHexName;
    ```
- `public const string ViewProhibitUserInputName = "HexView/ProhibitUserInput"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ViewProhibitUserInputName;
    ```
- `public static readonly VSTE.EditorOptionKey<HexColumnLineKind> ColumnGroupLine0Id = new VSTE.EditorOptionKey<HexColumnLineKind>(ColumnGroupLine0Name)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 74)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ColumnGroupLine0Id;
    ```
- `public static readonly VSTE.EditorOptionKey<HexColumnLineKind> ColumnGroupLine1Id = new VSTE.EditorOptionKey<HexColumnLineKind>(ColumnGroupLine1Name)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 76)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ColumnGroupLine1Id;
    ```
- `public static readonly VSTE.EditorOptionKey<HexColumnLineKind> ColumnLine0Id = new VSTE.EditorOptionKey<HexColumnLineKind>(ColumnLine0Name)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 70)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ColumnLine0Id;
    ```
- `public static readonly VSTE.EditorOptionKey<HexColumnLineKind> ColumnLine1Id = new VSTE.EditorOptionKey<HexColumnLineKind>(ColumnLine1Name)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 72)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ColumnLine1Id;
    ```
- `public static readonly VSTE.EditorOptionKey<HexOffsetFormat> HexOffsetFormatId = new VSTE.EditorOptionKey<HexOffsetFormat>(HexOffsetFormatName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HexOffsetFormatId;
    ```
- `public static readonly VSTE.EditorOptionKey<HexPosition> BasePositionId = new VSTE.EditorOptionKey<HexPosition>(BasePositionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.BasePositionId;
    ```
- `public static readonly VSTE.EditorOptionKey<HexPosition> EndPositionId = new VSTE.EditorOptionKey<HexPosition>(EndPositionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.EndPositionId;
    ```
- `public static readonly VSTE.EditorOptionKey<HexPosition> StartPositionId = new VSTE.EditorOptionKey<HexPosition>(StartPositionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.StartPositionId;
    ```
- `public static readonly VSTE.EditorOptionKey<HexValuesDisplayFormat> HexValuesDisplayFormatId = new VSTE.EditorOptionKey<HexValuesDisplayFormat>(HexValuesDisplayFormatName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 45)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HexValuesDisplayFormatId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> EnableColorizationId = new VSTE.EditorOptionKey<bool>(EnableColorizationName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 57)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.EnableColorizationId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> HighlightActiveColumnId = new VSTE.EditorOptionKey<bool>(HighlightActiveColumnName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 78)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HighlightActiveColumnId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> HighlightCurrentValueId = new VSTE.EditorOptionKey<bool>(HighlightCurrentValueName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 80)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HighlightCurrentValueId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> HighlightStructureUnderMouseCursorId = new VSTE.EditorOptionKey<bool>(HighlightStructureUnderMouseCursorName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 87)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HighlightStructureUnderMouseCursorId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> OffsetLowerCaseHexId = new VSTE.EditorOptionKey<bool>(OffsetLowerCaseHexName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 51)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.OffsetLowerCaseHexId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> RefreshScreenOnChangeId = new VSTE.EditorOptionKey<bool>(RefreshScreenOnChangeName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 61)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.RefreshScreenOnChangeId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> RemoveExtraTextLineVerticalPixelsId = new VSTE.EditorOptionKey<bool>(RemoveExtraTextLineVerticalPixelsName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 66)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.RemoveExtraTextLineVerticalPixelsId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> ShowAsciiColumnId = new VSTE.EditorOptionKey<bool>(ShowAsciiColumnName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ShowAsciiColumnId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> ShowColumnLinesId = new VSTE.EditorOptionKey<bool>(ShowColumnLinesName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ShowColumnLinesId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> ShowOffsetColumnId = new VSTE.EditorOptionKey<bool>(ShowOffsetColumnName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ShowOffsetColumnId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> ShowValuesColumnId = new VSTE.EditorOptionKey<bool>(ShowValuesColumnName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ShowValuesColumnId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> UseRelativePositionsId = new VSTE.EditorOptionKey<bool>(UseRelativePositionsName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.UseRelativePositionsId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> ValuesLowerCaseHexId = new VSTE.EditorOptionKey<bool>(ValuesLowerCaseHexName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ValuesLowerCaseHexId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> ViewProhibitUserInputId = new VSTE.EditorOptionKey<bool>(ViewProhibitUserInputName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 59)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.ViewProhibitUserInputId;
    ```
- `public static readonly VSTE.EditorOptionKey<int> BytesPerLineId = new VSTE.EditorOptionKey<int>(BytesPerLineName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.BytesPerLineId;
    ```
- `public static readonly VSTE.EditorOptionKey<int> EncodingCodePageId = new VSTE.EditorOptionKey<int>(EncodingCodePageName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 85)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.EncodingCodePageId;
    ```
- `public static readonly VSTE.EditorOptionKey<int> GroupSizeInBytesId = new VSTE.EditorOptionKey<int>(GroupSizeInBytesName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.GroupSizeInBytesId;
    ```
- `public static readonly VSTE.EditorOptionKey<int> HighlightCurrentValueDelayMilliSecondsId = new VSTE.EditorOptionKey<int>(HighlightCurrentValueDelayMilliSecondsName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 82)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.HighlightCurrentValueDelayMilliSecondsId;
    ```
- `public static readonly VSTE.EditorOptionKey<int> OffsetBitSizeId = new VSTE.EditorOptionKey<int>(OffsetBitSizeName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.OffsetBitSizeId;
    ```
- `public static readonly VSTE.EditorOptionKey<int> RefreshScreenOnChangeWaitMilliSecondsId = new VSTE.EditorOptionKey<int>(RefreshScreenOnChangeWaitMilliSecondsName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultHexViewOptions.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultHexViewOptions.RefreshScreenOnChangeWaitMilliSecondsId;
    ```

## Class `DefaultWpfHexViewOptions`

Default options

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions members directly without instantiation.
dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 26)

### Fields

- `public const string AppearanceCategoryName = "Appearance/Category"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.AppearanceCategoryName;
    ```
- `public const string EnableHighlightCurrentLineName = "WpfHexView/EnableHighlightCurrentLine"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.EnableHighlightCurrentLineName;
    ```
- `public const string EnableMouseWheelZoomName = "WpfHexView/MouseWheelZoom"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.EnableMouseWheelZoomName;
    ```
- `public const string EnableSimpleGraphicsName = "WpfHexView/Graphics/Simple/Enable"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.EnableSimpleGraphicsName;
    ```
- `public const string ForceClearTypeIfNeededName = "WpfHexView/ForceClearTypeIfNeeded"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.ForceClearTypeIfNeededName;
    ```
- `public const string UseReducedOpacityForHighContrastOptionName = "WpfHexView/UseReducedOpacityForHighContrast"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.UseReducedOpacityForHighContrastOptionName;
    ```
- `public const string ZoomLevelName = "WpfHexView/ZoomLevel"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.ZoomLevelName;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> EnableHighlightCurrentLineId = new VSTE.EditorOptionKey<bool>(EnableHighlightCurrentLineName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.EnableHighlightCurrentLineId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> EnableMouseWheelZoomId = new VSTE.EditorOptionKey<bool>(EnableMouseWheelZoomName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.EnableMouseWheelZoomId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> EnableSimpleGraphicsId = new VSTE.EditorOptionKey<bool>(EnableSimpleGraphicsName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.EnableSimpleGraphicsId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> ForceClearTypeIfNeededId = new VSTE.EditorOptionKey<bool>(ForceClearTypeIfNeededName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.ForceClearTypeIfNeededId;
    ```
- `public static readonly VSTE.EditorOptionKey<bool> UseReducedOpacityForHighContrastOptionId = new VSTE.EditorOptionKey<bool>(UseReducedOpacityForHighContrastOptionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.UseReducedOpacityForHighContrastOptionId;
    ```
- `public static readonly VSTE.EditorOptionKey<double> ZoomLevelId = new VSTE.EditorOptionKey<double>(ZoomLevelName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.ZoomLevelId;
    ```
- `public static readonly VSTE.EditorOptionKey<string> AppearanceCategoryId = new VSTE.EditorOptionKey<string>(AppearanceCategoryName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/DefaultWpfHexViewOptions.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.DefaultWpfHexViewOptions.AppearanceCategoryId;
    ```

## Enum `DisplayHexLineOptions`

Options passed to

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Editor.DisplayHexLineOptions and call its members.
var instance = new dnSpy.Contracts.Hex.Editor.DisplayHexLineOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 278)

### Members

- `None`: No bit is set
- `CanRecreateBufferLines` = `x00000001`: can be recreated immediately instead of delayed

## Class `HexAdornmentLayer`

Adornment layer

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexAdornmentLayer();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 29)

### Constructors

- `protected HexAdornmentLayer()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 33)

### Methods

- `public abstract bool AddAdornment(VSTE.AdornmentPositioningBehavior behavior, HexBufferSpan? visualSpan, object tag, UIElement adornment, VSTE.AdornmentRemovedCallback removedCallback)`
  - Summary: Adds an adornment. Returns true if the adornment was added.
  - Parameters:
    - `VSTE.AdornmentPositioningBehavior behavior`: Positioning behavior
    - `HexBufferSpan? visualSpan`: Span
    - `object tag`: Tag
    - `UIElement adornment`: Adornment
    - `VSTE.AdornmentRemovedCallback removedCallback`: Called when the adornment is removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 107)
  - Example:
    ```csharp
    // Example invocation
    instance.AddAdornment(behavior: /* VSTE.AdornmentPositioningBehavior */, visualSpan: /* HexBufferSpan? */, tag: /* object */, adornment: /* UIElement */, removedCallback: /* VSTE.AdornmentRemovedCallback */);
    ```
- `public abstract void RemoveAdornment(UIElement adornment)`
  - Summary: Removes an adornment
  - Parameters:
    - `UIElement adornment`: Adornment to remove
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAdornment(adornment: /* UIElement */);
    ```
- `public abstract void RemoveAdornmentsByTag(object tag)`
  - Summary: Removes all adornments with the specified tag
  - Parameters:
    - `object tag`: Tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 119)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAdornmentsByTag(tag: /* object */);
    ```
- `public abstract void RemoveAllAdornments()`
  - Summary: Removes all adornments
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 166)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAllAdornments();
    ```
- `public abstract void RemoveMatchingAdornments(HexBufferSpan visualSpan, Predicate<HexAdornmentLayerElement> match)`
  - Summary: Removes all matching adornments
  - Parameters:
    - `HexBufferSpan visualSpan`: Span
    - `Predicate<HexAdornmentLayerElement> match`: Returns true if the adornment should be removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 161)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveMatchingAdornments(visualSpan: /* HexBufferSpan */, match: /* Predicate<HexAdornmentLayerElement> */);
    ```
- `public abstract void RemoveMatchingAdornments(Predicate<HexAdornmentLayerElement> match)`
  - Summary: Removes all matching adornments
  - Parameters:
    - `Predicate<HexAdornmentLayerElement> match`: Returns true if the adornment should be removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveMatchingAdornments(match: /* Predicate<HexAdornmentLayerElement> */);
    ```
- `public bool AddAdornment(HexBufferLine line, object tag, UIElement adornment)`
  - Summary: Adds an adornment. Returns true if the adornment was added.
  - Parameters:
    - `HexBufferLine line`: Line
    - `object tag`: Tag
    - `UIElement adornment`: Adornment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.AddAdornment(line: /* HexBufferLine */, tag: /* object */, adornment: /* UIElement */);
    ```
- `public bool AddAdornment(HexBufferSpan visualSpan, object tag, UIElement adornment)`
  - Summary: Adds an adornment. Returns true if the adornment was added.
  - Parameters:
    - `HexBufferSpan visualSpan`: Span
    - `object tag`: Tag
    - `UIElement adornment`: Adornment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.AddAdornment(visualSpan: /* HexBufferSpan */, tag: /* object */, adornment: /* UIElement */);
    ```
- `public bool AddAdornment(VSTE.AdornmentPositioningBehavior behavior, HexBufferLine line, object tag, UIElement adornment, VSTE.AdornmentRemovedCallback removedCallback)`
  - Summary: Adds an adornment. Returns true if the adornment was added.
  - Parameters:
    - `VSTE.AdornmentPositioningBehavior behavior`: Positioning behavior
    - `HexBufferLine line`: Line
    - `object tag`: Tag
    - `UIElement adornment`: Adornment
    - `VSTE.AdornmentRemovedCallback removedCallback`: Called when the adornment is removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.AddAdornment(behavior: /* VSTE.AdornmentPositioningBehavior */, line: /* HexBufferLine */, tag: /* object */, adornment: /* UIElement */, removedCallback: /* VSTE.AdornmentRemovedCallback */);
    ```
- `public void RemoveAdornmentsByVisualSpan(HexBufferLine line)`
  - Summary: Removes an adornment
  - Parameters:
    - `HexBufferLine line`: Line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 131)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAdornmentsByVisualSpan(line: /* HexBufferLine */);
    ```
- `public void RemoveAdornmentsByVisualSpan(HexBufferSpan visualSpan)`
  - Summary: Removes an adornment
  - Parameters:
    - `HexBufferSpan visualSpan`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 138)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAdornmentsByVisualSpan(visualSpan: /* HexBufferSpan */);
    ```
- `public void RemoveMatchingAdornments(HexBufferLine line, Predicate<HexAdornmentLayerElement> match)`
  - Summary: Removes all matching adornments
  - Parameters:
    - `HexBufferLine line`: Line
    - `Predicate<HexAdornmentLayerElement> match`: Returns true if the adornment should be removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 148)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveMatchingAdornments(line: /* HexBufferLine */, match: /* Predicate<HexAdornmentLayerElement> */);
    ```

### Properties

- `public abstract FrameworkElement VisualElement { get; }`
  - Summary: Gets the UI element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VisualElement;
    ```
- `public abstract ReadOnlyCollection<HexAdornmentLayerElement> Elements { get; }`
  - Summary: Gets all elements
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Elements;
    ```
- `public abstract WpfHexView HexView { get; }`
  - Summary: Gets the hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexView;
    ```
- `public abstract bool IsEmpty { get; }`
  - Summary: true if the layer is empty
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public virtual double Opacity {
			get => VisualElement.Opacity;
			set => VisualElement.Opacity = value;
		}`
  - Summary: Gets/sets the layer opacity
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayer.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Opacity;
    ```

## Class `HexAdornmentLayerDefinition`

Defines an adornment layer

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Editor.HexAdornmentLayerDefinition and call its members.
var instance = new dnSpy.Contracts.Hex.Editor.HexAdornmentLayerDefinition(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayerDefinition.cs` (line 24)

## Class `HexAdornmentLayerElement`

Adornment layer element

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexAdornmentLayerElement();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayerElement.cs` (line 27)

### Constructors

- `protected HexAdornmentLayerElement()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayerElement.cs` (line 31)

### Properties

- `public abstract HexBufferSpan? VisualSpan { get; }`
  - Summary: Buffer span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayerElement.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VisualSpan;
    ```
- `public abstract UIElement Adornment { get; }`
  - Summary: Gets the adornment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayerElement.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Adornment;
    ```
- `public abstract VSTE.AdornmentPositioningBehavior Behavior { get; }`
  - Summary: Gets the positioning behavior
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayerElement.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Behavior;
    ```
- `public abstract VSTE.AdornmentRemovedCallback RemovedCallback { get; }`
  - Summary: Called when the adornment is removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayerElement.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RemovedCallback;
    ```
- `public abstract object Tag { get; }`
  - Summary: Gets the tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexAdornmentLayerElement.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```

## Class `HexCaret`

Hex caret

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexCaret();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 27)

### Constructors

- `protected HexCaret()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 31)

### Methods

- `public HexCaretPosition MoveTo(HexBufferPoint position)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexBufferPoint position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 144)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(position: /* HexBufferPoint */);
    ```
- `public HexCaretPosition MoveTo(HexCellPosition position)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexCellPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 170)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(position: /* HexCellPosition */);
    ```
- `public HexCaretPosition MoveTo(HexColumnPosition position)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexColumnPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 186)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(position: /* HexColumnPosition */);
    ```
- `public HexCaretPosition MoveTo(HexColumnType column, HexBufferPoint position)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexColumnType column`: Column
    - `HexBufferPoint position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(column: /* HexColumnType */, position: /* HexBufferPoint */);
    ```
- `public abstract HexCaretPosition MoveTo(HexCellPosition position, HexMoveToFlags flags)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexCellPosition position`: Position
    - `HexMoveToFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 179)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(position: /* HexCellPosition */, flags: /* HexMoveToFlags */);
    ```
- `public abstract HexCaretPosition MoveTo(HexColumnPosition position, HexMoveToFlags flags)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexColumnPosition position`: Position
    - `HexMoveToFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 195)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(position: /* HexColumnPosition */, flags: /* HexMoveToFlags */);
    ```
- `public abstract HexCaretPosition MoveTo(HexColumnType column, HexBufferPoint position, HexMoveToFlags flags)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexColumnType column`: Column
    - `HexBufferPoint position`: Position
    - `HexMoveToFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 163)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(column: /* HexColumnType */, position: /* HexBufferPoint */, flags: /* HexMoveToFlags */);
    ```
- `public abstract HexCaretPosition MoveTo(HexViewLine hexLine)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexViewLine hexLine`: Line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 202)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(hexLine: /* HexViewLine */);
    ```
- `public abstract HexCaretPosition MoveTo(HexViewLine hexLine, HexMoveToFlags flags)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexViewLine hexLine`: Line
    - `HexMoveToFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 210)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(hexLine: /* HexViewLine */, flags: /* HexMoveToFlags */);
    ```
- `public abstract HexCaretPosition MoveTo(HexViewLine hexLine, double xCoordinate)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexViewLine hexLine`: Line
    - `double xCoordinate`: X coordinate
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 218)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(hexLine: /* HexViewLine */, xCoordinate: /* double */);
    ```
- `public abstract HexCaretPosition MoveTo(HexViewLine hexLine, double xCoordinate, HexMoveToFlags flags)`
  - Summary: Moves the caret to a new position
  - Parameters:
    - `HexViewLine hexLine`: Line
    - `double xCoordinate`: X coordinate
    - `HexMoveToFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 227)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(hexLine: /* HexViewLine */, xCoordinate: /* double */, flags: /* HexMoveToFlags */);
    ```
- `public abstract HexCaretPosition MoveToNextCaretPosition()`
  - Summary: Moves the caret to the next position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 239)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToNextCaretPosition();
    ```
- `public abstract HexCaretPosition MoveToPreferredCoordinates()`
  - Summary: Moves the caret to the preferred x and y coordinates
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 245)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToPreferredCoordinates();
    ```
- `public abstract HexCaretPosition MoveToPreviousCaretPosition()`
  - Summary: Moves the caret to the previous position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 233)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToPreviousCaretPosition();
    ```
- `public abstract HexCaretPosition ToggleActiveColumn()`
  - Summary: Toggles the active column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 137)
  - Example:
    ```csharp
    // Example invocation
    instance.ToggleActiveColumn();
    ```
- `public abstract void EnsureVisible()`
  - Summary: Brings the caret into view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 131)
  - Example:
    ```csharp
    // Example invocation
    instance.EnsureVisible();
    ```

### Properties

- `public abstract HexCaretPosition Position { get; }`
  - Summary: Gets the position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 121)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Position;
    ```
- `public abstract HexViewLine ContainingHexViewLine { get; }`
  - Summary: Gets the containing hex view line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContainingHexViewLine;
    ```
- `public abstract bool IsAsciiCaretPresent { get; }`
  - Summary: true if the caret in the ASCII column is present
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAsciiCaretPresent;
    ```
- `public abstract bool IsHidden { get; set; }`
  - Summary: true if the caret is hidden, false if it's visible
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsHidden;
    ```
- `public abstract bool IsValuesCaretPresent { get; }`
  - Summary: true if the caret in the values column is present
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsValuesCaretPresent;
    ```
- `public abstract bool OverwriteMode { get; }`
  - Summary: true if it's overwrite mode
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OverwriteMode;
    ```
- `public abstract double AsciiBottom { get; }`
  - Summary: Gets the position of the bottom edge of the caret in the ASCII column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsciiBottom;
    ```
- `public abstract double AsciiHeight { get; }`
  - Summary: Gets the height of the caret in the ASCII column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsciiHeight;
    ```
- `public abstract double AsciiLeft { get; }`
  - Summary: Gets the position of the left edge of the caret in the ASCII column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsciiLeft;
    ```
- `public abstract double AsciiRight { get; }`
  - Summary: Gets the position of the right edge of the caret in the ASCII column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsciiRight;
    ```
- `public abstract double AsciiTop { get; }`
  - Summary: Gets the position of the top edge of the caret in the ASCII column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsciiTop;
    ```
- `public abstract double AsciiWidth { get; }`
  - Summary: Gets the width of the caret in the ASCII column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsciiWidth;
    ```
- `public abstract double ValuesBottom { get; }`
  - Summary: Gets the position of the bottom edge of the caret in the values column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesBottom;
    ```
- `public abstract double ValuesHeight { get; }`
  - Summary: Gets the height of the caret in the values column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesHeight;
    ```
- `public abstract double ValuesLeft { get; }`
  - Summary: Gets the position of the left edge of the caret in the values column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesLeft;
    ```
- `public abstract double ValuesRight { get; }`
  - Summary: Gets the position of the right edge of the caret in the values column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesRight;
    ```
- `public abstract double ValuesTop { get; }`
  - Summary: Gets the position of the top edge of the caret in the values column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesTop;
    ```
- `public abstract double ValuesWidth { get; }`
  - Summary: Gets the width of the caret in the values column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValuesWidth;
    ```

### Events

- `public abstract event EventHandler<HexCaretPositionChangedEventArgs> PositionChanged`
  - Summary: Raised after the position is changed by calling one of the MoveTo methods
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 126)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PositionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `HexCaretPosition`

Caret position

**Inherits/Implements:** `IEquatable<HexCaretPosition>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexCaretPosition(position: /* HexColumnPosition */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaretPosition.cs` (line 26)

### Constructors

- `public HexCaretPosition(HexColumnPosition position)`
  - Summary: Constructor
  - Parameters:
    - `HexColumnPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaretPosition.cs` (line 41)

### Methods

- `public bool Equals(HexCaretPosition other)`
  - Summary: Equals()
  - Parameters:
    - `HexCaretPosition other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaretPosition.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* HexCaretPosition */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaretPosition.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaretPosition.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaretPosition.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public HexColumnPosition Position { get; }`
  - Summary: Gets the position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaretPosition.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Position;
    ```
- `public bool IsDefault => Position.IsDefault`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaretPosition.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```

### Operators

- `public static bool operator !=(HexCaretPosition a, HexCaretPosition b) => !a.Equals(b);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaretPosition.cs` (line 60)
- `public static bool operator ==(HexCaretPosition a, HexCaretPosition b) => a.Equals(b);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaretPosition.cs` (line 52)

## Class `HexCaretPositionChangedEventArgs`

Caret position changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexCaretPositionChangedEventArgs(hexView: /* HexView */, oldPosition: /* HexCaretPosition */, newPosition: /* HexCaretPosition */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 272)

### Constructors

- `public HexCaretPositionChangedEventArgs(HexView hexView, HexCaretPosition oldPosition, HexCaretPosition newPosition)`
  - Summary: Constructor
  - Parameters:
    - `HexView hexView`: Hex view
    - `HexCaretPosition oldPosition`: Old position
    - `HexCaretPosition newPosition`: New position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 294)

### Properties

- `public HexCaretPosition NewPosition { get; }`
  - Summary: Gets the new position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 286)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewPosition;
    ```
- `public HexCaretPosition OldPosition { get; }`
  - Summary: Gets the old position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 281)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldPosition;
    ```
- `public HexView HexView { get; }`
  - Summary: Gets the hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 276)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexView;
    ```

## Enum `HexColumnLineKind`

Column line kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Editor.HexColumnLineKind and call its members.
var instance = new dnSpy.Contracts.Hex.Editor.HexColumnLineKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexColumnLineKind.cs` (line 24)

### Members

- `None`: No line is shown (it's disabled)
- `Solid`: Solid lines
- `Dashed_1_1`: Dashed lines (dash 1px, gap 1px)
- `Dashed_2_2`: Dashed lines (dash 2px, gap 2px)
- `Dashed_3_3`: Dashed lines (dash 3px, gap 3px)
- `Dashed_4_4`: Dashed lines (dash 4px, gap 4px)

## Struct `HexCursorInfo`

Cursor info

**Inherits/Implements:** `IEquatable<HexCursorInfo>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexCursorInfo(cursor: /* Cursor */, priority: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 69)

### Constructors

- `public HexCursorInfo(Cursor cursor, double priority)`
  - Summary: Constructor
  - Parameters:
    - `Cursor cursor`: Cursor or null
    - `double priority`: Priority, eg. . The highest priority cursor is used
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 85)

### Methods

- `public bool Equals(HexCursorInfo other)`
  - Summary: Equals()
  - Parameters:
    - `HexCursorInfo other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* HexCursorInfo */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 107)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public Cursor Cursor { get; }`
  - Summary: Gets the cursor or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Cursor;
    ```
- `public double Priority { get; }`
  - Summary: Gets the priority, eg. . The highest priority cursor is used.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Priority;
    ```

### Operators

- `public static bool operator !=(HexCursorInfo left, HexCursorInfo right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 92)
- `public static bool operator ==(HexCursorInfo left, HexCursorInfo right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 91)

## Class `HexCursorProvider`

Hex editor provider

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexCursorProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 119)

### Constructors

- `protected HexCursorProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 123)

### Properties

- `public abstract HexCursorInfo CursorInfo { get; }`
  - Summary: Gets the cursor and priority
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 133)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CursorInfo;
    ```

### Events

- `public abstract event EventHandler CursorInfoChanged`
  - Summary: Raised after is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 128)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.CursorInfoChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexCursorProviderFactory`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexCursorProviderFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 27)

### Constructors

- `protected HexCursorProviderFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 31)

### Methods

- `public abstract HexCursorProvider Create(WpfHexView wpfHexView)`
  - Summary: Creates a instance or returns null
  - Parameters:
    - `WpfHexView wpfHexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(wpfHexView: /* WpfHexView */);
    ```

## Class `HexEditorFactoryService`

Creates hex views and hosts

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexEditorFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 28)

### Constructors

- `protected HexEditorFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 32)

### Methods

- `public abstract VSTE.ITextViewRoleSet CreateTextViewRoleSet(IEnumerable<string> roles)`
  - Summary: Creates a role set
  - Parameters:
    - `IEnumerable<string> roles`: Roles
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 118)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextViewRoleSet(roles: /* IEnumerable<string> */);
    ```
- `public abstract VSTE.ITextViewRoleSet CreateTextViewRoleSet(params string[] roles)`
  - Summary: Creates a role set
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextViewRoleSet();
    ```
- `public abstract WpfHexView Create(HexBuffer buffer, HexViewCreatorOptions options)`
  - Summary: Creates a new
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `HexViewCreatorOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(buffer: /* HexBuffer */, options: /* HexViewCreatorOptions */);
    ```
- `public abstract WpfHexView Create(HexBuffer buffer, VSTE.ITextViewRoleSet roles, HexViewCreatorOptions options)`
  - Summary: Creates a new
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `VSTE.ITextViewRoleSet roles`: Roles
    - `HexViewCreatorOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(buffer: /* HexBuffer */, roles: /* VSTE.ITextViewRoleSet */, options: /* HexViewCreatorOptions */);
    ```
- `public abstract WpfHexView Create(HexBuffer buffer, VSTE.ITextViewRoleSet roles, VSTE.IEditorOptions parentOptions, HexViewCreatorOptions options)`
  - Summary: Creates a new
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `VSTE.ITextViewRoleSet roles`: Roles
    - `VSTE.IEditorOptions parentOptions`: Parent options
    - `HexViewCreatorOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(buffer: /* HexBuffer */, roles: /* VSTE.ITextViewRoleSet */, parentOptions: /* VSTE.IEditorOptions */, options: /* HexViewCreatorOptions */);
    ```
- `public abstract WpfHexViewHost CreateHost(WpfHexView wpfHexView, bool setFocus)`
  - Summary: Creates a new
  - Parameters:
    - `WpfHexView wpfHexView`: Hex view
    - `bool setFocus`: true to set focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateHost(wpfHexView: /* WpfHexView */, setFocus: /* bool */);
    ```
- `public virtual WpfHexView Create(HexBuffer buffer)`
  - Summary: Creates a new
  - Parameters:
    - `HexBuffer buffer`: Buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(buffer: /* HexBuffer */);
    ```
- `public virtual WpfHexView Create(HexBuffer buffer, VSTE.ITextViewRoleSet roles)`
  - Summary: Creates a new
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `VSTE.ITextViewRoleSet roles`: Roles
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(buffer: /* HexBuffer */, roles: /* VSTE.ITextViewRoleSet */);
    ```
- `public virtual WpfHexView Create(HexBuffer buffer, VSTE.ITextViewRoleSet roles, VSTE.IEditorOptions parentOptions)`
  - Summary: Creates a new
  - Parameters:
    - `HexBuffer buffer`: Buffer
    - `VSTE.ITextViewRoleSet roles`: Roles
    - `VSTE.IEditorOptions parentOptions`: Parent options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(buffer: /* HexBuffer */, roles: /* VSTE.ITextViewRoleSet */, parentOptions: /* VSTE.IEditorOptions */);
    ```

### Properties

- `public abstract VSTE.ITextViewRoleSet AllPredefinedRoles { get; }`
  - Summary: Gets all predefined hex view roles
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AllPredefinedRoles;
    ```
- `public abstract VSTE.ITextViewRoleSet DefaultRoles { get; }`
  - Summary: Gets the default hex view roles
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DefaultRoles;
    ```
- `public abstract VSTE.ITextViewRoleSet NoRoles { get; }`
  - Summary: Gets an empty role set
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NoRoles;
    ```

### Events

- `public abstract event EventHandler<HexViewCreatedEventArgs> HexViewCreated`
  - Summary: Raised when a new hex view is created
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryService.cs` (line 52)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.HexViewCreated += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexEditorFactoryServiceListener`

Gets notified when hex views get created, see also

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexEditorFactoryServiceListener();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryServiceListener.cs` (line 24)

### Constructors

- `protected HexEditorFactoryServiceListener()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryServiceListener.cs` (line 28)

### Methods

- `public abstract void HexViewCreated(WpfHexView hexView)`
  - Summary: Called after a hex view is created
  - Parameters:
    - `WpfHexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorFactoryServiceListener.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.HexViewCreated(hexView: /* WpfHexView */);
    ```

## Class `HexEditorOptionDefinition`

Hex editor option definition

**Inherits/Implements:** `VSTE.EditorOptionDefinition`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexEditorOptionDefinition();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 28)

### Constructors

- `protected HexEditorOptionDefinition()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 32)

## Class `HexEditorOptionDefinition<T>`

Hex editor option definition

**Inherits/Implements:** `HexEditorOptionDefinition`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexEditorOptionDefinition<T>();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 39)

### Constructors

- `protected HexEditorOptionDefinition()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 43)

### Methods

- `public sealed override bool IsValid(ref object proposedValue)`
  - Summary: Checks whether the new value is valid
  - Parameters:
    - `ref object proposedValue`: Proposed value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValid(proposedValue: /* object */);
    ```
- `public virtual bool IsValid(ref T proposedValue)`
  - Summary: Checks whether the new value is valid
  - Parameters:
    - `ref T proposedValue`: Proposed value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValid(proposedValue: /* T */);
    ```

### Properties

- `public abstract VSTE.EditorOptionKey<T> Key { get; }`
  - Summary: Gets the option key
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Key;
    ```
- `public sealed override Type ValueType => typeof(T)`
  - Summary: Gets the value type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueType;
    ```
- `public sealed override object DefaultValue => Default`
  - Summary: Gets the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DefaultValue;
    ```
- `public sealed override string Name => Key.Name`
  - Summary: Gets the name of the option
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public virtual T Default => default`
  - Summary: Gets the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Default;
    ```

## Class `HexEditorOptionsFactoryService`

Editor options factory service

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexEditorOptionsFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionsFactoryService.cs` (line 27)

### Constructors

- `protected HexEditorOptionsFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionsFactoryService.cs` (line 31)

### Methods

- `public abstract VSTE.IEditorOptions CreateOptions()`
  - Summary: Creates options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionsFactoryService.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateOptions();
    ```
- `public abstract VSTE.IEditorOptions GetOptions(VSUTIL.IPropertyOwner scope)`
  - Summary: Creates or returns existing options
  - Parameters:
    - `VSUTIL.IPropertyOwner scope`: Owner
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionsFactoryService.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptions(scope: /* VSUTIL.IPropertyOwner */);
    ```

### Properties

- `public abstract VSTE.IEditorOptions GlobalOptions { get; }`
  - Summary: Gets the global options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionsFactoryService.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GlobalOptions;
    ```

## Class `HexGlyphFactory`

Creates glyphs shown in glyph margins

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexGlyphFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphFactory.cs` (line 27)

### Constructors

- `protected HexGlyphFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphFactory.cs` (line 31)

### Methods

- `public abstract UIElement GenerateGlyph(WpfHexViewLine line, HexGlyphTag tag)`
  - Summary: Generates a glyph or returns null
  - Parameters:
    - `WpfHexViewLine line`: Line
    - `HexGlyphTag tag`: Tag
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphFactory.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.GenerateGlyph(line: /* WpfHexViewLine */, tag: /* HexGlyphTag */);
    ```

## Class `HexGlyphFactoryProvider`

Creates instances

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexGlyphFactoryProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphFactoryProvider.cs` (line 24)

### Constructors

- `protected HexGlyphFactoryProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphFactoryProvider.cs` (line 28)

### Methods

- `public abstract HexGlyphFactory GetGlyphFactory(WpfHexView view, WpfHexViewMargin margin)`
  - Summary: Creates a or returns null
  - Parameters:
    - `WpfHexView view`: Hex view
    - `WpfHexViewMargin margin`: Margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphFactoryProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGlyphFactory(view: /* WpfHexView */, margin: /* WpfHexViewMargin */);
    ```

## Class `HexGlyphMouseProcessorProvider`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexGlyphMouseProcessorProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphMouseProcessorProvider.cs` (line 24)

### Constructors

- `protected HexGlyphMouseProcessorProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphMouseProcessorProvider.cs` (line 28)

### Methods

- `public abstract HexMouseProcessor GetAssociatedMouseProcessor(WpfHexViewHost wpfHexViewHost, WpfHexViewMargin margin)`
  - Summary: Creates a mouse processor or returns null
  - Parameters:
    - `WpfHexViewHost wpfHexViewHost`: Hex view host
    - `WpfHexViewMargin margin`: Margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphMouseProcessorProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAssociatedMouseProcessor(wpfHexViewHost: /* WpfHexViewHost */, margin: /* WpfHexViewMargin */);
    ```

## Class `HexGlyphTag`

A glyph margin tag

**Inherits/Implements:** `HexTag`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexGlyphTag();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphTag.cs` (line 26)

### Constructors

- `protected HexGlyphTag()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexGlyphTag.cs` (line 30)

## Class `HexImageReferenceTag`

tag

**Inherits/Implements:** `HexGlyphTag`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexImageReferenceTag(imageReference: /* ImageReference */, zIndex: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexImageReferenceTag.cs` (line 26)

### Constructors

- `public HexImageReferenceTag(ImageReference imageReference, int zIndex)`
  - Summary: Constructor
  - Parameters:
    - `ImageReference imageReference`: Image reference
    - `int zIndex`: Z-index, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexImageReferenceTag.cs` (line 42)

### Properties

- `public ImageReference ImageReference { get; }`
  - Summary: Gets the image reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexImageReferenceTag.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageReference;
    ```
- `public int ZIndex { get; }`
  - Summary: Gets the Z-index, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexImageReferenceTag.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ZIndex;
    ```

## Class `HexIntraTextAdornmentTag`

Intra text adornment tag

**Inherits/Implements:** `HexTag`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexIntraTextAdornmentTag(adornment: /* UIElement */, removalCallback: /* VSTE.AdornmentRemovedCallback */, topSpace: /* double? */, baseline: /* double? */, textHeight: /* double? */, bottomSpace: /* double? */, affinity: /* VST.PositionAffinity? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 30)

### Constructors

- `public HexIntraTextAdornmentTag(UIElement adornment, VSTE.AdornmentRemovedCallback removalCallback)`
  - Summary: Constructor
  - Parameters:
    - `UIElement adornment`: Adornment element
    - `VSTE.AdornmentRemovedCallback removalCallback`: Called when the adornment is removed, may be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 101)
- `public HexIntraTextAdornmentTag(UIElement adornment, VSTE.AdornmentRemovedCallback removalCallback, VST.PositionAffinity? affinity)`
  - Summary: Constructor
  - Parameters:
    - `UIElement adornment`: Adornment element
    - `VSTE.AdornmentRemovedCallback removalCallback`: Called when the adornment is removed, may be null
    - `VST.PositionAffinity? affinity`: Position affinity or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 92)
- `public HexIntraTextAdornmentTag(UIElement adornment, VSTE.AdornmentRemovedCallback removalCallback, double? topSpace, double? baseline, double? textHeight, double? bottomSpace, VST.PositionAffinity? affinity)`
  - Summary: Constructor
  - Parameters:
    - `UIElement adornment`: Adornment element
    - `VSTE.AdornmentRemovedCallback removalCallback`: Called when the adornment is removed, may be null
    - `double? topSpace`: Top space or null to use the default value
    - `double? baseline`: Base line or null to use the default value
    - `double? textHeight`: Text height or null to use the default value
    - `double? bottomSpace`: Bottom space or null to use the default value
    - `VST.PositionAffinity? affinity`: Position affinity or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 76)

### Properties

- `public UIElement Adornment { get; }`
  - Summary: Gets the adornment element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Adornment;
    ```
- `public VST.PositionAffinity? Affinity { get; }`
  - Summary: Gets the position affinity or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Affinity;
    ```
- `public VSTE.AdornmentRemovedCallback RemovalCallback { get; }`
  - Summary: Gets the removal callback or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RemovalCallback;
    ```
- `public double? Baseline { get; }`
  - Summary: Gets the base line or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Baseline;
    ```
- `public double? BottomSpace { get; }`
  - Summary: Gets the bottom space or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BottomSpace;
    ```
- `public double? TextHeight { get; }`
  - Summary: Gets the text height or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextHeight;
    ```
- `public double? TopSpace { get; }`
  - Summary: Gets the top space or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexIntraTextAdornmentTag.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TopSpace;
    ```

## Class `HexKeyProcessor`

Keyboard processor

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexKeyProcessor();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 26)

### Constructors

- `protected HexKeyProcessor()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 30)

### Methods

- `public virtual void KeyDown(KeyEventArgs args)`
  - Summary: Key down handler
  - Parameters:
    - `KeyEventArgs args`: Key event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.KeyDown(args: /* KeyEventArgs */);
    ```
- `public virtual void KeyUp(KeyEventArgs args)`
  - Summary: Key up handler
  - Parameters:
    - `KeyEventArgs args`: Key event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.KeyUp(args: /* KeyEventArgs */);
    ```
- `public virtual void PreviewKeyDown(KeyEventArgs args)`
  - Summary: Preview key down handler
  - Parameters:
    - `KeyEventArgs args`: Key event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.PreviewKeyDown(args: /* KeyEventArgs */);
    ```
- `public virtual void PreviewKeyUp(KeyEventArgs args)`
  - Summary: Preview key up handler
  - Parameters:
    - `KeyEventArgs args`: Key event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.PreviewKeyUp(args: /* KeyEventArgs */);
    ```
- `public virtual void PreviewTextInput(TextCompositionEventArgs args)`
  - Summary: Preview text input handler
  - Parameters:
    - `TextCompositionEventArgs args`: Key event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.PreviewTextInput(args: /* TextCompositionEventArgs */);
    ```
- `public virtual void PreviewTextInputStart(TextCompositionEventArgs args)`
  - Summary: Preview text input start handler
  - Parameters:
    - `TextCompositionEventArgs args`: Key event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.PreviewTextInputStart(args: /* TextCompositionEventArgs */);
    ```
- `public virtual void PreviewTextInputUpdate(TextCompositionEventArgs args)`
  - Summary: Preview text input update handler
  - Parameters:
    - `TextCompositionEventArgs args`: Key event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.PreviewTextInputUpdate(args: /* TextCompositionEventArgs */);
    ```
- `public virtual void TextInput(TextCompositionEventArgs args)`
  - Summary: Text input handler
  - Parameters:
    - `TextCompositionEventArgs args`: Key event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.TextInput(args: /* TextCompositionEventArgs */);
    ```
- `public virtual void TextInputStart(TextCompositionEventArgs args)`
  - Summary: Text input start handler
  - Parameters:
    - `TextCompositionEventArgs args`: Key event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.TextInputStart(args: /* TextCompositionEventArgs */);
    ```
- `public virtual void TextInputUpdate(TextCompositionEventArgs args)`
  - Summary: Text input update handler
  - Parameters:
    - `TextCompositionEventArgs args`: Key event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.TextInputUpdate(args: /* TextCompositionEventArgs */);
    ```

### Properties

- `public virtual bool IsInterestedInHandledEvents => false`
  - Summary: true if the instance is interested in handled events. Default value is false.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessor.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInterestedInHandledEvents;
    ```

## Class `HexKeyProcessorProvider`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexKeyProcessorProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessorProvider.cs` (line 24)

### Constructors

- `protected HexKeyProcessorProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessorProvider.cs` (line 28)

### Methods

- `public abstract HexKeyProcessor GetAssociatedProcessor(WpfHexView wpfHexView)`
  - Summary: Creates a or returns null
  - Parameters:
    - `WpfHexView wpfHexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexKeyProcessorProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAssociatedProcessor(wpfHexView: /* WpfHexView */);
    ```

## Enum `HexLayerKind`

Layer kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Editor.HexLayerKind and call its members.
var instance = new dnSpy.Contracts.Hex.Editor.HexLayerKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexLayerKind.cs` (line 24)

### Members

- `Normal`: Normal layer
- `Overlay`: Overlay layer. It's shown above all layers
- `Underlay`: Underlay layer. It's shown below all layers

## Class `HexLayerKindAttribute`

Adds a layer kind

**Inherits/Implements:** `VSUTIL.SingletonBaseMetadataAttribute`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexLayerKindAttribute(kind: /* HexLayerKind */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexLayerKindAttribute.cs` (line 26)

### Constructors

- `public HexLayerKindAttribute(HexLayerKind kind)`
  - Summary: Constructor
  - Parameters:
    - `HexLayerKind kind`: Kind of layer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexLayerKindAttribute.cs` (line 31)

### Properties

- `public HexLayerKind LayerKind { get; }`
  - Summary: Layer kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexLayerKindAttribute.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LayerKind;
    ```

## Class `HexMarginContextMenuHandlerProvider`

Creates s or returns null. You must this interface and add a with the name of the margin (eg. ). Optional attribute: .

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexMarginContextMenuHandlerProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginContextMenuHandlerProvider.cs` (line 32)

### Constructors

- `protected HexMarginContextMenuHandlerProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginContextMenuHandlerProvider.cs` (line 36)

### Methods

- `public abstract IHexMarginContextMenuHandler Create(WpfHexViewHost wpfHexViewHost, WpfHexViewMargin margin)`
  - Summary: Creates s or returns null
  - Parameters:
    - `WpfHexViewHost wpfHexViewHost`: Hex view host
    - `WpfHexViewMargin margin`: Margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginContextMenuHandlerProvider.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(wpfHexViewHost: /* WpfHexViewHost */, margin: /* WpfHexViewMargin */);
    ```

## Class `HexMarginContextMenuService`

Creates a that uses s to create objects.

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexMarginContextMenuService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginContextMenuService.cs` (line 27)

### Constructors

- `protected HexMarginContextMenuService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginContextMenuService.cs` (line 31)

### Methods

- `public abstract IGuidObjectsProvider Create(WpfHexViewHost wpfHexViewHost, WpfHexViewMargin margin, string marginName)`
  - Summary: Creates a
  - Parameters:
    - `WpfHexViewHost wpfHexViewHost`: Hex view host
    - `WpfHexViewMargin margin`: Margin
    - `string marginName`: Margin name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginContextMenuService.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(wpfHexViewHost: /* WpfHexViewHost */, margin: /* WpfHexViewMargin */, marginName: /* string */);
    ```

## Class `HexMarginNameAttribute`

Adds the name of a margin

**Inherits/Implements:** `VSUTIL.SingletonBaseMetadataAttribute`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexMarginNameAttribute(marginName: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginNameAttribute.cs` (line 27)

### Constructors

- `public HexMarginNameAttribute(string marginName)`
  - Summary: Constructor
  - Parameters:
    - `string marginName`: Name of margin, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginNameAttribute.cs` (line 32)

### Properties

- `public string MarginName { get; }`
  - Summary: Name of margin, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginNameAttribute.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MarginName;
    ```

## Class `HexMarkerServiceZIndexes`

Hex marker service Z-indexes. Markers with a negative z-index are placed in a marker layer below most other layers.

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.HexMarkerServiceZIndexes members directly without instantiation.
dnSpy.Contracts.Hex.Editor.HexMarkerServiceZIndexes./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarkerServiceZIndexes.cs` (line 25)

### Fields

- `public const int CurrentValue = 0`
  - Summary: Current value highlighter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarkerServiceZIndexes.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.HexMarkerServiceZIndexes.CurrentValue;
    ```
- `public const int FindMatch = 5000`
  - Summary: Find match
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarkerServiceZIndexes.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.HexMarkerServiceZIndexes.FindMatch;
    ```
- `public const int ToolTipCurrentField = 7000`
  - Summary: ToolTip current field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarkerServiceZIndexes.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.HexMarkerServiceZIndexes.ToolTipCurrentField;
    ```
- `public const int ToolTipField0 = 6000`
  - Summary: ToolTip field #0
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarkerServiceZIndexes.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.HexMarkerServiceZIndexes.ToolTipField0;
    ```
- `public const int ToolTipField1 = 6001`
  - Summary: ToolTip field #1
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarkerServiceZIndexes.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.HexMarkerServiceZIndexes.ToolTipField1;
    ```

## Class `HexMouseHoverAttribute`

Overrides mouse hover delay

**Inherits/Implements:** `Attribute`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexMouseHoverAttribute(delay: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseHoverAttribute.cs` (line 26)

### Constructors

- `public HexMouseHoverAttribute(int delay)`
  - Summary: Constructor
  - Parameters:
    - `int delay`: Delay in milliseconds
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseHoverAttribute.cs` (line 37)

### Properties

- `public int Delay { get; }`
  - Summary: Gets the delay in milliseconds
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseHoverAttribute.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Delay;
    ```

## Class `HexMouseHoverEventArgs`

Mouse hover event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexMouseHoverEventArgs(view: /* HexView */, line: /* HexBufferLine */, textPosition: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseHoverEventArgs.cs` (line 26)

### Constructors

- `public HexMouseHoverEventArgs(HexView view, HexBufferLine line, int textPosition)`
  - Summary: Constructor
  - Parameters:
    - `HexView view`: Hex view
    - `HexBufferLine line`: Line
    - `int textPosition`: Text position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseHoverEventArgs.cs` (line 48)

### Properties

- `public HexBufferLine Line { get; }`
  - Summary: Gets the line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseHoverEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Line;
    ```
- `public HexView View { get; }`
  - Summary: Gets the hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseHoverEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.View;
    ```
- `public int TextPosition { get; }`
  - Summary: Gets the text position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseHoverEventArgs.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextPosition;
    ```

## Class `HexMouseProcessor`

Mouse processor

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexMouseProcessor();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 27)

### Constructors

- `protected HexMouseProcessor()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 31)

### Methods

- `public virtual void PostprocessDragEnter(DragEventArgs e)`
  - Summary: Drag enter postprocess handler
  - Parameters:
    - `DragEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessDragEnter(e: /* DragEventArgs */);
    ```
- `public virtual void PostprocessDragLeave(DragEventArgs e)`
  - Summary: Drag leave postprocess handler
  - Parameters:
    - `DragEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 163)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessDragLeave(e: /* DragEventArgs */);
    ```
- `public virtual void PostprocessDragOver(DragEventArgs e)`
  - Summary: Drag over postprocess handler
  - Parameters:
    - `DragEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessDragOver(e: /* DragEventArgs */);
    ```
- `public virtual void PostprocessDrop(DragEventArgs e)`
  - Summary: Drop postprocess handler
  - Parameters:
    - `DragEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessDrop(e: /* DragEventArgs */);
    ```
- `public virtual void PostprocessGiveFeedback(GiveFeedbackEventArgs e)`
  - Summary: Give feedback postprocess handler
  - Parameters:
    - `GiveFeedbackEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 223)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessGiveFeedback(e: /* GiveFeedbackEventArgs */);
    ```
- `public virtual void PostprocessManipulationCompleted(ManipulationCompletedEventArgs e)`
  - Summary: Manipulation completed postprocess handler
  - Parameters:
    - `ManipulationCompletedEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 307)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessManipulationCompleted(e: /* ManipulationCompletedEventArgs */);
    ```
- `public virtual void PostprocessManipulationDelta(ManipulationDeltaEventArgs e)`
  - Summary: Manipulation delta postprocess handler
  - Parameters:
    - `ManipulationDeltaEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 295)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessManipulationDelta(e: /* ManipulationDeltaEventArgs */);
    ```
- `public virtual void PostprocessManipulationInertiaStarting(ManipulationInertiaStartingEventArgs e)`
  - Summary: Manipulation inertia starting postprocess handler
  - Parameters:
    - `ManipulationInertiaStartingEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 271)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessManipulationInertiaStarting(e: /* ManipulationInertiaStartingEventArgs */);
    ```
- `public virtual void PostprocessManipulationStarting(ManipulationStartingEventArgs e)`
  - Summary: Manipulation starting postprocess handler
  - Parameters:
    - `ManipulationStartingEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 283)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessManipulationStarting(e: /* ManipulationStartingEventArgs */);
    ```
- `public virtual void PostprocessMouseDown(MouseButtonEventArgs e)`
  - Summary: Mouse down postprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessMouseDown(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PostprocessMouseEnter(MouseEventArgs e)`
  - Summary: Mouse enter postprocess handler
  - Parameters:
    - `MouseEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessMouseEnter(e: /* MouseEventArgs */);
    ```
- `public virtual void PostprocessMouseLeave(MouseEventArgs e)`
  - Summary: Mouse leave postprocess handler
  - Parameters:
    - `MouseEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 151)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessMouseLeave(e: /* MouseEventArgs */);
    ```
- `public virtual void PostprocessMouseLeftButtonDown(MouseButtonEventArgs e)`
  - Summary: Mouse left button down postprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessMouseLeftButtonDown(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PostprocessMouseLeftButtonUp(MouseButtonEventArgs e)`
  - Summary: Mouse left button up postprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessMouseLeftButtonUp(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PostprocessMouseMove(MouseEventArgs e)`
  - Summary: Mouse move postprocess handler
  - Parameters:
    - `MouseEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessMouseMove(e: /* MouseEventArgs */);
    ```
- `public virtual void PostprocessMouseRightButtonDown(MouseButtonEventArgs e)`
  - Summary: Mouse right button down postprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessMouseRightButtonDown(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PostprocessMouseRightButtonUp(MouseButtonEventArgs e)`
  - Summary: Right button up postprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessMouseRightButtonUp(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PostprocessMouseUp(MouseButtonEventArgs e)`
  - Summary: Mouse up postprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessMouseUp(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PostprocessMouseWheel(MouseWheelEventArgs e)`
  - Summary: Mouse wheel postprocess handler
  - Parameters:
    - `MouseWheelEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 127)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessMouseWheel(e: /* MouseWheelEventArgs */);
    ```
- `public virtual void PostprocessQueryContinueDrag(QueryContinueDragEventArgs e)`
  - Summary: Query continue drag postprocess handler
  - Parameters:
    - `QueryContinueDragEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 211)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessQueryContinueDrag(e: /* QueryContinueDragEventArgs */);
    ```
- `public virtual void PostprocessStylusSystemGesture(StylusSystemGestureEventArgs e)`
  - Summary: Stylus system gesture postprocess handler
  - Parameters:
    - `StylusSystemGestureEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 259)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessStylusSystemGesture(e: /* StylusSystemGestureEventArgs */);
    ```
- `public virtual void PostprocessTouchDown(TouchEventArgs e)`
  - Summary: Touch down postprocess handler
  - Parameters:
    - `TouchEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 235)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessTouchDown(e: /* TouchEventArgs */);
    ```
- `public virtual void PostprocessTouchUp(TouchEventArgs e)`
  - Summary: Touch up postprocess handler
  - Parameters:
    - `TouchEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 247)
  - Example:
    ```csharp
    // Example invocation
    instance.PostprocessTouchUp(e: /* TouchEventArgs */);
    ```
- `public virtual void PreprocessDragEnter(DragEventArgs e)`
  - Summary: Drag enter preprocess handler
  - Parameters:
    - `DragEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessDragEnter(e: /* DragEventArgs */);
    ```
- `public virtual void PreprocessDragLeave(DragEventArgs e)`
  - Summary: Drag leave preprocess handler
  - Parameters:
    - `DragEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessDragLeave(e: /* DragEventArgs */);
    ```
- `public virtual void PreprocessDragOver(DragEventArgs e)`
  - Summary: Drag over preprocess handler
  - Parameters:
    - `DragEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 169)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessDragOver(e: /* DragEventArgs */);
    ```
- `public virtual void PreprocessDrop(DragEventArgs e)`
  - Summary: Drop preprocess handler
  - Parameters:
    - `DragEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessDrop(e: /* DragEventArgs */);
    ```
- `public virtual void PreprocessGiveFeedback(GiveFeedbackEventArgs e)`
  - Summary: Give feedback preprocess handler
  - Parameters:
    - `GiveFeedbackEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 217)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessGiveFeedback(e: /* GiveFeedbackEventArgs */);
    ```
- `public virtual void PreprocessManipulationCompleted(ManipulationCompletedEventArgs e)`
  - Summary: Manipulation completed preprocess handler
  - Parameters:
    - `ManipulationCompletedEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 301)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessManipulationCompleted(e: /* ManipulationCompletedEventArgs */);
    ```
- `public virtual void PreprocessManipulationDelta(ManipulationDeltaEventArgs e)`
  - Summary: Manipulation delta preprocess handler
  - Parameters:
    - `ManipulationDeltaEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 289)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessManipulationDelta(e: /* ManipulationDeltaEventArgs */);
    ```
- `public virtual void PreprocessManipulationInertiaStarting(ManipulationInertiaStartingEventArgs e)`
  - Summary: Manipulation inertia starting preprocess handler
  - Parameters:
    - `ManipulationInertiaStartingEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 265)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessManipulationInertiaStarting(e: /* ManipulationInertiaStartingEventArgs */);
    ```
- `public virtual void PreprocessManipulationStarting(ManipulationStartingEventArgs e)`
  - Summary: Manipulation starting preprocess handler
  - Parameters:
    - `ManipulationStartingEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 277)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessManipulationStarting(e: /* ManipulationStartingEventArgs */);
    ```
- `public virtual void PreprocessMouseDown(MouseButtonEventArgs e)`
  - Summary: Mouse down preprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessMouseDown(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PreprocessMouseEnter(MouseEventArgs e)`
  - Summary: Mouse enter preprocess handler
  - Parameters:
    - `MouseEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessMouseEnter(e: /* MouseEventArgs */);
    ```
- `public virtual void PreprocessMouseLeave(MouseEventArgs e)`
  - Summary: Mouse leave preprocess handler
  - Parameters:
    - `MouseEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 145)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessMouseLeave(e: /* MouseEventArgs */);
    ```
- `public virtual void PreprocessMouseLeftButtonDown(MouseButtonEventArgs e)`
  - Summary: Mouse left button down preprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessMouseLeftButtonDown(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PreprocessMouseLeftButtonUp(MouseButtonEventArgs e)`
  - Summary: Mouse left button up preprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessMouseLeftButtonUp(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PreprocessMouseMove(MouseEventArgs e)`
  - Summary: Mouse move preprocess handler
  - Parameters:
    - `MouseEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessMouseMove(e: /* MouseEventArgs */);
    ```
- `public virtual void PreprocessMouseRightButtonDown(MouseButtonEventArgs e)`
  - Summary: Mouse right button down preprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessMouseRightButtonDown(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PreprocessMouseRightButtonUp(MouseButtonEventArgs e)`
  - Summary: Right button up preprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessMouseRightButtonUp(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PreprocessMouseUp(MouseButtonEventArgs e)`
  - Summary: Mouse up preprocess handler
  - Parameters:
    - `MouseButtonEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessMouseUp(e: /* MouseButtonEventArgs */);
    ```
- `public virtual void PreprocessMouseWheel(MouseWheelEventArgs e)`
  - Summary: Mouse wheel preprocess handler
  - Parameters:
    - `MouseWheelEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessMouseWheel(e: /* MouseWheelEventArgs */);
    ```
- `public virtual void PreprocessQueryContinueDrag(QueryContinueDragEventArgs e)`
  - Summary: Query continue drag preprocess handler
  - Parameters:
    - `QueryContinueDragEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 205)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessQueryContinueDrag(e: /* QueryContinueDragEventArgs */);
    ```
- `public virtual void PreprocessStylusSystemGesture(StylusSystemGestureEventArgs e)`
  - Summary: Stylus system gesture preprocess handler
  - Parameters:
    - `StylusSystemGestureEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 253)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessStylusSystemGesture(e: /* StylusSystemGestureEventArgs */);
    ```
- `public virtual void PreprocessTouchDown(TouchEventArgs e)`
  - Summary: Touch down preprocess handler
  - Parameters:
    - `TouchEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 229)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessTouchDown(e: /* TouchEventArgs */);
    ```
- `public virtual void PreprocessTouchUp(TouchEventArgs e)`
  - Summary: Touch up preprocess handler
  - Parameters:
    - `TouchEventArgs e`: Event args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessor.cs` (line 241)
  - Example:
    ```csharp
    // Example invocation
    instance.PreprocessTouchUp(e: /* TouchEventArgs */);
    ```

## Class `HexMouseProcessorProvider`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexMouseProcessorProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessorProvider.cs` (line 24)

### Constructors

- `protected HexMouseProcessorProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessorProvider.cs` (line 28)

### Methods

- `public abstract HexMouseProcessor GetAssociatedProcessor(WpfHexView wpfHexView)`
  - Summary: Creates a or returns null
  - Parameters:
    - `WpfHexView wpfHexView`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMouseProcessorProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAssociatedProcessor(wpfHexView: /* WpfHexView */);
    ```

## Enum `HexMoveToFlags`

Flags passed to eg.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Editor.HexMoveToFlags and call its members.
var instance = new dnSpy.Contracts.Hex.Editor.HexMoveToFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCaret.cs` (line 251)

### Members

- `None`: No bit is set
- `CaptureHorizontalPosition` = `x00000001`: Capture horizontal position
- `InsertionPosition` = `x00000002`: Get the character position by finding the character closest to the x coordinate

## Class `HexReferenceConverter`

Converts a reference

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexReferenceConverter();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexReferenceConverter.cs` (line 24)

### Constructors

- `protected HexReferenceConverter()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexReferenceConverter.cs` (line 28)

### Methods

- `public abstract object Convert(HexView hexView, object reference)`
  - Summary: Converts the reference to a new reference or returns the original value
  - Parameters:
    - `HexView hexView`: Hex view
    - `object reference`: Reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexReferenceConverter.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Convert(hexView: /* HexView */, reference: /* object */);
    ```

## Class `HexReferenceHandler`

Handles references created by . Export an instance with a , see .

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexReferenceHandler();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexReferenceHandler.cs` (line 28)

### Constructors

- `protected HexReferenceHandler()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexReferenceHandler.cs` (line 32)

### Methods

- `public abstract bool Handle(HexView hexView, object reference, IList<string> tags)`
  - Summary: Handles a reference
  - Parameters:
    - `HexView hexView`: Hex view
    - `object reference`: Reference created by eg.
    - `IList<string> tags`: Tags, see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexReferenceHandler.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.Handle(hexView: /* HexView */, reference: /* object */, tags: /* IList<string> */);
    ```

## Class `HexReferenceHandlerService`

Handles references created by

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexReferenceHandlerService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexReferenceHandlerService.cs` (line 26)

### Constructors

- `protected HexReferenceHandlerService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexReferenceHandlerService.cs` (line 30)

### Methods

- `public abstract bool Handle(HexView hexView, object reference, IList<string> tags = null)`
  - Summary: Handles a reference
  - Parameters:
    - `HexView hexView`: Hex view
    - `object reference`: Reference created by eg.
    - `IList<string> tags` (default: `null`): Tags or null, see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexReferenceHandlerService.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Handle(hexView: /* HexView */, reference: /* object */, tags: /* IList<string> */);
    ```

## Class `HexScrollMap`

Hex view scroll map

**Inherits/Implements:** `HexVerticalFractionMap`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexScrollMap();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexScrollMap.cs` (line 24)

### Constructors

- `protected HexScrollMap()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexScrollMap.cs` (line 28)

### Methods

- `public abstract HexBufferPoint GetBufferPositionAtCoordinate(double coordinate)`
  - Summary: Gets the buffer position that corresponds to a scrollmap coordinate
  - Parameters:
    - `double coordinate`: Scrollbar coordinate
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexScrollMap.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetBufferPositionAtCoordinate(coordinate: /* double */);
    ```
- `public abstract double GetCoordinateAtBufferPosition(HexBufferPoint bufferPosition)`
  - Summary: Gets the scrollmap coordinates of a buffer position
  - Parameters:
    - `HexBufferPoint bufferPosition`: Buffer position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexScrollMap.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCoordinateAtBufferPosition(bufferPosition: /* HexBufferPoint */);
    ```

### Properties

- `public abstract double End { get; }`
  - Summary: Gets the scrollmap coordinate of the end of the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexScrollMap.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.End;
    ```
- `public abstract double Start { get; }`
  - Summary: Gets the scrollmap coordinate of the start of the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexScrollMap.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Start;
    ```
- `public abstract double ThumbSize { get; }`
  - Summary: Gets the size of the text visible in the view (in scrollmap coordinates)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexScrollMap.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ThumbSize;
    ```

## Class `HexScrollMapFactoryService`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexScrollMapFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexScrollMapFactoryService.cs` (line 24)

### Constructors

- `protected HexScrollMapFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexScrollMapFactoryService.cs` (line 28)

### Methods

- `public abstract HexScrollMap Create(HexView hexView)`
  - Summary: Creates a instance
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexScrollMapFactoryService.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(hexView: /* HexView */);
    ```

## Class `HexSelection`

Hex selection

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexSelection();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 29)

### Constructors

- `protected HexSelection()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 33)

### Methods

- `public abstract IEnumerable<VST.Span> GetSelectionOnHexViewLine(HexViewLine line)`
  - Summary: Gets the slection on a line
  - Parameters:
    - `HexViewLine line`: Line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSelectionOnHexViewLine(line: /* HexViewLine */);
    ```
- `public abstract void Clear()`
  - Summary: Clears the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```
- `public abstract void Select(HexBufferPoint anchorPoint, HexBufferPoint activePoint, bool alignPoints)`
  - Summary: Select a span
  - Parameters:
    - `HexBufferPoint anchorPoint`: Anchor point
    - `HexBufferPoint activePoint`: Active point
    - `bool alignPoints`: true to align the span to include all bytes of the cells
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.Select(anchorPoint: /* HexBufferPoint */, activePoint: /* HexBufferPoint */, alignPoints: /* bool */);
    ```
- `public abstract void Select(HexBufferSpan selectionSpan, bool isReversed, bool alignPoints)`
  - Summary: Selects a span
  - Parameters:
    - `HexBufferSpan selectionSpan`: Span
    - `bool isReversed`: true if the anchor point is the end point of
    - `bool alignPoints`: true to align the span to include all bytes of the cells
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.Select(selectionSpan: /* HexBufferSpan */, isReversed: /* bool */, alignPoints: /* bool */);
    ```

### Properties

- `public HexBufferPoint End => AnchorPoint < ActivePoint ? ActivePoint : AnchorPoint`
  - Summary: Gets the end position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 121)
  - Example:
    ```csharp
    // Read the property
    var value = instance.End;
    ```
- `public HexBufferPoint Start => AnchorPoint < ActivePoint ? AnchorPoint : ActivePoint`
  - Summary: Gets the start position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Start;
    ```
- `public HexBufferSpan StreamSelectionSpan => new HexBufferSpan(Start, End)`
  - Summary: Gets the selected span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StreamSelectionSpan;
    ```
- `public abstract HexBufferPoint ActivePoint { get; }`
  - Summary: Gets the active point
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActivePoint;
    ```
- `public abstract HexBufferPoint AnchorPoint { get; }`
  - Summary: Gets the anchor point
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AnchorPoint;
    ```
- `public abstract HexView HexView { get; }`
  - Summary: Gets the hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexView;
    ```
- `public abstract NormalizedHexBufferSpanCollection SelectedSpans { get; }`
  - Summary: Gets all selected spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectedSpans;
    ```
- `public abstract bool ActivationTracksFocus { get; set; }`
  - Summary: true if gets updated when the hex view gets and loses focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActivationTracksFocus;
    ```
- `public abstract bool IsActive { get; set; }`
  - Summary: true if the selection is active, false if it's inactive
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsActive;
    ```
- `public bool IsEmpty => AnchorPoint == ActivePoint`
  - Summary: true if the selection is empty
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public bool IsReversed => ActivePoint < AnchorPoint`
  - Summary: true if the selection is reversed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsReversed;
    ```

### Events

- `public abstract event EventHandler SelectionChanged`
  - Summary: Raised when the selection is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSelection.cs` (line 101)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.SelectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexSpaceReservationAgent`

Space reservation agent

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexSpaceReservationAgent();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationAgent.cs` (line 27)

### Constructors

- `protected HexSpaceReservationAgent()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationAgent.cs` (line 31)

### Methods

- `public abstract Geometry PositionAndDisplay(Geometry reservedSpace)`
  - Summary: Positions and displays the adornment. Returns null if it should be removed.
  - Parameters:
    - `Geometry reservedSpace`: Reserved space
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationAgent.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.PositionAndDisplay(reservedSpace: /* Geometry */);
    ```
- `public abstract void Hide()`
  - Summary: Called to hide the adornment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationAgent.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.Hide();
    ```

### Properties

- `public abstract bool HasFocus { get; }`
  - Summary: true if its adornment has keyboard focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationAgent.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasFocus;
    ```
- `public abstract bool IsMouseOver { get; }`
  - Summary: true if the mouse is over its adornment
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationAgent.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMouseOver;
    ```

### Events

- `public abstract event EventHandler GotFocus`
  - Summary: Raised after its adornment got keyboard focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationAgent.cs` (line 46)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.GotFocus += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler LostFocus`
  - Summary: Raised after its adornment lost keyboard focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationAgent.cs` (line 51)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.LostFocus += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexSpaceReservationAgentChangedEventArgs`

Space reservation agent changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexSpaceReservationAgentChangedEventArgs(oldAgent: /* HexSpaceReservationAgent */, newAgent: /* HexSpaceReservationAgent */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 161)

### Constructors

- `public HexSpaceReservationAgentChangedEventArgs(HexSpaceReservationAgent oldAgent, HexSpaceReservationAgent newAgent)`
  - Summary: Constructor
  - Parameters:
    - `HexSpaceReservationAgent oldAgent`: Old agent or null
    - `HexSpaceReservationAgent newAgent`: New agent or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 177)

### Properties

- `public HexSpaceReservationAgent NewAgent { get; }`
  - Summary: Gets the new agent or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 165)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewAgent;
    ```
- `public HexSpaceReservationAgent OldAgent { get; }`
  - Summary: Gets the old agent or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 170)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldAgent;
    ```

## Class `HexSpaceReservationManager`

Space reservation manager

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexSpaceReservationManager();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 30)

### Constructors

- `protected HexSpaceReservationManager()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 34)

### Methods

- `public HexSpaceReservationAgent CreatePopupAgent(HexBufferLine line, VST.Span span, VSTA.PopupStyles style, UIElement content)`
  - Summary: Creates a popup agent
  - Parameters:
    - `HexBufferLine line`: Line
    - `VST.Span span`: Line span
    - `VSTA.PopupStyles style`: Popup style
    - `UIElement content`: Popup content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.CreatePopupAgent(line: /* HexBufferLine */, span: /* VST.Span */, style: /* VSTA.PopupStyles */, content: /* UIElement */);
    ```
- `public HexSpaceReservationAgent CreatePopupAgent(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags, VSTA.PopupStyles style, UIElement content)`
  - Summary: Creates a popup agent
  - Parameters:
    - `HexBufferSpan bufferSpan`: Buffer span
    - `HexSpanSelectionFlags flags`: Selection flags
    - `VSTA.PopupStyles style`: Popup style
    - `UIElement content`: Popup content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.CreatePopupAgent(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */, style: /* VSTA.PopupStyles */, content: /* UIElement */);
    ```
- `public HexSpaceReservationAgent CreatePopupAgent(HexBufferSpanSelection span, VSTA.PopupStyles style, UIElement content)`
  - Summary: Creates a popup agent
  - Parameters:
    - `HexBufferSpanSelection span`: Span and selection flags
    - `VSTA.PopupStyles style`: Popup style
    - `UIElement content`: Popup content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.CreatePopupAgent(span: /* HexBufferSpanSelection */, style: /* VSTA.PopupStyles */, content: /* UIElement */);
    ```
- `public abstract HexSpaceReservationAgent CreatePopupAgent(HexLineSpan lineSpan, VSTA.PopupStyles style, UIElement content)`
  - Summary: Creates a popup agent
  - Parameters:
    - `HexLineSpan lineSpan`: Line span
    - `VSTA.PopupStyles style`: Popup style
    - `UIElement content`: Popup content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.CreatePopupAgent(lineSpan: /* HexLineSpan */, style: /* VSTA.PopupStyles */, content: /* UIElement */);
    ```
- `public abstract bool RemoveAgent(HexSpaceReservationAgent agent)`
  - Summary: Removes an agent
  - Parameters:
    - `HexSpaceReservationAgent agent`: Agent to remove
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 118)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAgent(agent: /* HexSpaceReservationAgent */);
    ```
- `public abstract void AddAgent(HexSpaceReservationAgent agent)`
  - Summary: Adds an agent
  - Parameters:
    - `HexSpaceReservationAgent agent`: Agent to add
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.AddAgent(agent: /* HexSpaceReservationAgent */);
    ```
- `public abstract void UpdatePopupAgent(HexSpaceReservationAgent agent, HexLineSpan lineSpan, VSTA.PopupStyles styles)`
  - Summary: Updates a popup agent
  - Parameters:
    - `HexSpaceReservationAgent agent`: Popup agent created by
    - `HexLineSpan lineSpan`: New line span
    - `VSTA.PopupStyles styles`: New popup style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 155)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdatePopupAgent(agent: /* HexSpaceReservationAgent */, lineSpan: /* HexLineSpan */, styles: /* VSTA.PopupStyles */);
    ```
- `public void UpdatePopupAgent(HexSpaceReservationAgent agent, HexBufferLine line, VST.Span span, VSTA.PopupStyles styles)`
  - Summary: Updates a popup agent
  - Parameters:
    - `HexSpaceReservationAgent agent`: Popup agent created by
    - `HexBufferLine line`: Line
    - `VST.Span span`: Line span
    - `VSTA.PopupStyles styles`: New popup style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdatePopupAgent(agent: /* HexSpaceReservationAgent */, line: /* HexBufferLine */, span: /* VST.Span */, styles: /* VSTA.PopupStyles */);
    ```
- `public void UpdatePopupAgent(HexSpaceReservationAgent agent, HexBufferSpan bufferSpan, HexSpanSelectionFlags flags, VSTA.PopupStyles styles)`
  - Summary: Updates a popup agent
  - Parameters:
    - `HexSpaceReservationAgent agent`: Popup agent created by
    - `HexBufferSpan bufferSpan`: New buffer span
    - `HexSpanSelectionFlags flags`: New selection flags
    - `VSTA.PopupStyles styles`: New popup style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 136)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdatePopupAgent(agent: /* HexSpaceReservationAgent */, bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */, styles: /* VSTA.PopupStyles */);
    ```
- `public void UpdatePopupAgent(HexSpaceReservationAgent agent, HexBufferSpanSelection span, VSTA.PopupStyles styles)`
  - Summary: Updates a popup agent
  - Parameters:
    - `HexSpaceReservationAgent agent`: Popup agent created by
    - `HexBufferSpanSelection span`: Span and selection flags
    - `VSTA.PopupStyles styles`: New popup style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdatePopupAgent(agent: /* HexSpaceReservationAgent */, span: /* HexBufferSpanSelection */, styles: /* VSTA.PopupStyles */);
    ```

### Properties

- `public abstract ReadOnlyCollection<HexSpaceReservationAgent> Agents { get; }`
  - Summary: Gets all agents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Agents;
    ```
- `public abstract bool HasAggregateFocus { get; }`
  - Summary: true if any of the agents' adornments have keyboard focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasAggregateFocus;
    ```
- `public abstract bool IsMouseOver { get; }`
  - Summary: true if the mouse is over any of the agents' adornments
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMouseOver;
    ```

### Events

- `public abstract event EventHandler GotAggregateFocus`
  - Summary: Raised after it got aggregate focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 59)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.GotAggregateFocus += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler LostAggregateFocus`
  - Summary: Raised after it lost aggregate focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 64)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.LostAggregateFocus += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<HexSpaceReservationAgentChangedEventArgs> AgentChanged`
  - Summary: Raised after an agent has been added or removed from
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManager.cs` (line 54)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.AgentChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexSpaceReservationManagerDefinition`

Defines a space reservation manager

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Editor.HexSpaceReservationManagerDefinition and call its members.
var instance = new dnSpy.Contracts.Hex.Editor.HexSpaceReservationManagerDefinition(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexSpaceReservationManagerDefinition.cs` (line 24)

## Struct `HexStructureField`

Structure field

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexStructureField(bufferSpan: /* HexBufferSpan */, kind: /* HexStructureFieldKind */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 89)

### Constructors

- `public HexStructureField(HexBufferSpan bufferSpan, HexStructureFieldKind kind)`
  - Summary: Constructor
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span of field
    - `HexStructureFieldKind kind`: Field kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 110)

### Properties

- `public HexBufferSpan BufferSpan { get; }`
  - Summary: Span of field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferSpan;
    ```
- `public HexStructureFieldKind Kind { get; }`
  - Summary: Field kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 98)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public bool IsCurrentField => Kind == HexStructureFieldKind.CurrentField`
  - Summary: true if it's the current field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 103)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsCurrentField;
    ```

## Enum `HexStructureFieldKind`

Field kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Editor.HexStructureFieldKind and call its members.
var instance = new dnSpy.Contracts.Hex.Editor.HexStructureFieldKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 59)

### Members

- `Other`: Some other kind
- `Structure`: Span is the full structure
- `SubStructure`: Span is a sub structure
- `Field`: Span is a field
- `CurrentField`: Span is the current field

## Class `HexStructureInfoAggregator`

Returns data from all s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexStructureInfoAggregator();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoAggregator.cs` (line 26)

### Constructors

- `protected HexStructureInfoAggregator()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoAggregator.cs` (line 30)

### Methods

- `public IEnumerable<HexStructureInfoProviderAndData<HexStructureField>> GetFields(HexPosition position)`
  - Summary: Gets all fields
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoAggregator.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFields(position: /* HexPosition */);
    ```
- `public IEnumerable<HexStructureInfoProviderAndData<object>> GetReferences(HexPosition position)`
  - Summary: Gets all references
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoAggregator.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.GetReferences(position: /* HexPosition */);
    ```
- `public IEnumerable<HexStructureInfoProviderAndData<object>> GetToolTips(HexPosition position)`
  - Summary: Gets all tooltips
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoAggregator.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetToolTips(position: /* HexPosition */);
    ```

### Properties

- `protected abstract IEnumerable<HexStructureInfoProvider> Providers { get; }`
  - Summary: Gets all providers
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoAggregator.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Providers;
    ```

## Class `HexStructureInfoAggregatorFactory`

Creates instances

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexStructureInfoAggregatorFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoAggregatorFactory.cs` (line 24)

### Constructors

- `protected HexStructureInfoAggregatorFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoAggregatorFactory.cs` (line 28)

### Methods

- `public abstract HexStructureInfoAggregator Create(HexView hexView)`
  - Summary: Creates a instance
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoAggregatorFactory.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(hexView: /* HexView */);
    ```

## Class `HexStructureInfoProvider`

Structure info provider

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexStructureInfoProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 26)

### Constructors

- `protected HexStructureInfoProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 30)

### Methods

- `public abstract IEnumerable<HexStructureField> GetFields(HexPosition position)`
  - Summary: Gets all related fields. It's enough to return the span of the current field at and the span of the full structure that contains the field.
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFields(position: /* HexPosition */);
    ```
- `public abstract object GetReference(HexPosition position)`
  - Summary: Gets a reference or null. The reference can be used to look up a high level representation of the data, eg. the C# statement in decompiled code.
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.GetReference(position: /* HexPosition */);
    ```
- `public abstract object GetToolTip(HexPosition position)`
  - Summary: Gets a tooltip or null
  - Parameters:
    - `HexPosition position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProvider.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetToolTip(position: /* HexPosition */);
    ```

## Struct `HexStructureInfoProviderAndData<TValue>`

Contains a and data

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexStructureInfoProviderAndData<TValue>(provider: /* HexStructureInfoProvider */, value: /* TValue */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProviderAndData.cs` (line 27)

### Constructors

- `public HexStructureInfoProviderAndData(HexStructureInfoProvider provider, TValue value)`
  - Summary: Constructor
  - Parameters:
    - `HexStructureInfoProvider provider`: Provider
    - `TValue value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProviderAndData.cs` (line 48)

### Properties

- `public HexStructureInfoProvider Provider { get; }`
  - Summary: Gets the provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProviderAndData.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Provider;
    ```
- `public TValue Value { get; }`
  - Summary: Gets the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProviderAndData.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public bool IsDefault => Provider == null`
  - Summary: true if this is a default instance that hasn't been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProviderAndData.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```

## Class `HexStructureInfoProviderFactory`

Creates instances. Export an instance with a and an optional . See .

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexStructureInfoProviderFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProviderFactory.cs` (line 28)

### Constructors

- `protected HexStructureInfoProviderFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProviderFactory.cs` (line 32)

### Methods

- `public abstract HexStructureInfoProvider Create(HexView hexView)`
  - Summary: Creates a instance
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexStructureInfoProviderFactory.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(hexView: /* HexView */);
    ```

## Class `HexVerticalFractionMap`

Maps between byte positions and fractions of the total vertical extent of a

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexVerticalFractionMap();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexVerticalFractionMap.cs` (line 26)

### Constructors

- `protected HexVerticalFractionMap()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexVerticalFractionMap.cs` (line 30)

### Methods

- `public abstract HexBufferPoint GetBufferPositionAtFraction(double fraction)`
  - Summary: Gets the buffer position that corresponds to a fraction of the vertical extent of the view, if it exists
  - Parameters:
    - `double fraction`: The fraction of the vertical extent of the view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexVerticalFractionMap.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetBufferPositionAtFraction(fraction: /* double */);
    ```
- `public abstract double GetFractionAtBufferPosition(HexBufferPoint bufferPosition)`
  - Summary: Gets the fraction of the vertical extent of the view that corresponds to the specified buffer position
  - Parameters:
    - `HexBufferPoint bufferPosition`: Buffer position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexVerticalFractionMap.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFractionAtBufferPosition(bufferPosition: /* HexBufferPoint */);
    ```

### Properties

- `public abstract HexView HexView { get; }`
  - Summary: Gets the hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexVerticalFractionMap.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexView;
    ```

### Events

- `public abstract event EventHandler MappingChanged`
  - Summary: Raised when the mapping is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexVerticalFractionMap.cs` (line 54)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.MappingChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexView`

Hex view

**Inherits/Implements:** `VSUTIL.IPropertyOwner`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexView();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 30)

### Constructors

- `protected HexView()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 194)

### Methods

- `public abstract HexViewLine GetHexViewLineContainingBufferPosition(HexBufferPoint bufferPosition)`
  - Summary: Gets a hex view line
  - Parameters:
    - `HexBufferPoint bufferPosition`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 237)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHexViewLineContainingBufferPosition(bufferPosition: /* HexBufferPoint */);
    ```
- `public abstract void Close()`
  - Summary: Closes the hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```
- `public abstract void DisplayHexLineContainingBufferPosition(HexBufferPoint bufferPosition, double verticalDistance, VSTE.ViewRelativePosition relativeTo, double? viewportWidthOverride, double? viewportHeightOverride, DisplayHexLineOptions options)`
  - Summary: Displays a line in the view
  - Parameters:
    - `HexBufferPoint bufferPosition`: Position
    - `double verticalDistance`: Distance relative to the top or bottom of the view
    - `VSTE.ViewRelativePosition relativeTo`: The
    - `double? viewportWidthOverride`: Overrides viewport width
    - `double? viewportHeightOverride`: Overrides viewport height
    - `DisplayHexLineOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 230)
  - Example:
    ```csharp
    // Example invocation
    instance.DisplayHexLineContainingBufferPosition(bufferPosition: /* HexBufferPoint */, verticalDistance: /* double */, relativeTo: /* VSTE.ViewRelativePosition */, viewportWidthOverride: /* double? */, viewportHeightOverride: /* double? */, options: /* DisplayHexLineOptions */);
    ```
- `public abstract void QueueSpaceReservationStackRefresh()`
  - Summary: Queues a space reservation stack refresh
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 242)
  - Example:
    ```csharp
    // Example invocation
    instance.QueueSpaceReservationStackRefresh();
    ```
- `public abstract void Refresh()`
  - Summary: Refreshes the screen and clears any read caches
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 247)
  - Example:
    ```csharp
    // Example invocation
    instance.Refresh();
    ```
- `public void DisplayHexLineContainingBufferPosition(HexBufferPoint bufferPosition, double verticalDistance, VSTE.ViewRelativePosition relativeTo)`
  - Summary: Displays a line in the view
  - Parameters:
    - `HexBufferPoint bufferPosition`: Position
    - `double verticalDistance`: Distance relative to the top or bottom of the view
    - `VSTE.ViewRelativePosition relativeTo`: The
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 207)
  - Example:
    ```csharp
    // Example invocation
    instance.DisplayHexLineContainingBufferPosition(bufferPosition: /* HexBufferPoint */, verticalDistance: /* double */, relativeTo: /* VSTE.ViewRelativePosition */);
    ```
- `public void DisplayHexLineContainingBufferPosition(HexBufferPoint bufferPosition, double verticalDistance, VSTE.ViewRelativePosition relativeTo, double? viewportWidthOverride, double? viewportHeightOverride)`
  - Summary: Displays a line in the view
  - Parameters:
    - `HexBufferPoint bufferPosition`: Position
    - `double verticalDistance`: Distance relative to the top or bottom of the view
    - `VSTE.ViewRelativePosition relativeTo`: The
    - `double? viewportWidthOverride`: Overrides viewport width
    - `double? viewportHeightOverride`: Overrides viewport height
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 218)
  - Example:
    ```csharp
    // Example invocation
    instance.DisplayHexLineContainingBufferPosition(bufferPosition: /* HexBufferPoint */, verticalDistance: /* double */, relativeTo: /* VSTE.ViewRelativePosition */, viewportWidthOverride: /* double? */, viewportHeightOverride: /* double? */);
    ```

### Properties

- `public VSUTIL.PropertyCollection Properties { get; }`
  - Summary: Gets all properties
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Properties;
    ```
- `public abstract HexBuffer Buffer { get; }`
  - Summary: Gets the hex buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 109)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public abstract HexBufferLineFormatter BufferLines { get; }`
  - Summary: Gets the hex buffer lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BufferLines;
    ```
- `public abstract HexBufferSpan? ProvisionalTextHighlight { get; set; }`
  - Summary: Gets the provisional text highlight
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 104)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProvisionalTextHighlight;
    ```
- `public abstract HexCaret Caret { get; }`
  - Summary: Gets the caret
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Caret;
    ```
- `public abstract HexSelection Selection { get; }`
  - Summary: Gets the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Selection;
    ```
- `public abstract HexViewLineCollection HexViewLines { get; }`
  - Summary: Gets the hex view lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 149)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexViewLines;
    ```
- `public abstract HexViewScroller ViewScroller { get; }`
  - Summary: Gets the view scroller
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 144)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewScroller;
    ```
- `public abstract ICommandTargetCollection CommandTarget { get; }`
  - Summary: Gets the command target
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CommandTarget;
    ```
- `public abstract VSTE.IEditorOptions Options { get; }`
  - Summary: Gets the editor options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```
- `public abstract VSTE.ITextViewRoleSet Roles { get; }`
  - Summary: Gets the hex view roles
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 99)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Roles;
    ```
- `public abstract bool HasAggregateFocus { get; }`
  - Summary: true if the hex view or any of its adornments has focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasAggregateFocus;
    ```
- `public abstract bool InLayout { get; }`
  - Summary: true if the view is in the process of being laid out
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InLayout;
    ```
- `public abstract bool IsClosed { get; }`
  - Summary: true if the view has closed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 89)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsClosed;
    ```
- `public abstract bool IsMouseOverViewOrAdornments { get; }`
  - Summary: true if the mouse is over the view or any of its adornments
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMouseOverViewOrAdornments;
    ```
- `public abstract double LineHeight { get; }`
  - Summary: Gets the nominal line height
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LineHeight;
    ```
- `public abstract double MaxTextRightCoordinate { get; }`
  - Summary: Gets the x coordinate of the maximum right edge of the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 79)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MaxTextRightCoordinate;
    ```
- `public abstract double ViewportBottom { get; }`
  - Summary: Gets viewport bottom
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 119)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportBottom;
    ```
- `public abstract double ViewportHeight { get; }`
  - Summary: Gets viewport height
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 139)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportHeight;
    ```
- `public abstract double ViewportLeft { get; set; }`
  - Summary: Gets/sets viewport left
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 124)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportLeft;
    ```
- `public abstract double ViewportRight { get; }`
  - Summary: Gets viewport right
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportRight;
    ```
- `public abstract double ViewportTop { get; }`
  - Summary: Gets viewport top
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 114)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportTop;
    ```
- `public abstract double ViewportWidth { get; }`
  - Summary: Gets viewport width
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportWidth;
    ```

### Events

- `public abstract event EventHandler Closed`
  - Summary: Raised after the view is closed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 154)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Closed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler GotAggregateFocus`
  - Summary: Raised when the view or one of its adornments got focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 159)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.GotAggregateFocus += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler LostAggregateFocus`
  - Summary: Raised when the view and all its adornments lost focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 164)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.LostAggregateFocus += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler ViewportHeightChanged`
  - Summary: Raised when viewport height is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 174)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ViewportHeightChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler ViewportLeftChanged`
  - Summary: Raised when viewport left is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 184)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ViewportLeftChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler ViewportWidthChanged`
  - Summary: Raised when viewport width is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 179)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ViewportWidthChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<BufferLinesChangedEventArgs> BufferLinesChanged`
  - Summary: Raised after is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 44)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BufferLinesChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<HexMouseHoverEventArgs> MouseHover`
  - Summary: Raised when the mouse has hovered long enough over something in the view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 189)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.MouseHover += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<HexViewLayoutChangedEventArgs> LayoutChanged`
  - Summary: Raised when the layout is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexView.cs` (line 169)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.LayoutChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexViewCreatedEventArgs`

Hex view created event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexViewCreatedEventArgs(hexView: /* HexView */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreatedEventArgs.cs` (line 26)

### Constructors

- `public HexViewCreatedEventArgs(HexView hexView)`
  - Summary: Constructor
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreatedEventArgs.cs` (line 36)

### Properties

- `public HexView HexView { get; }`
  - Summary: Gets the hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreatedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexView;
    ```

## Class `HexViewCreationListener`

Gets notified when hex views get created, see also

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexViewCreationListener();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreationListener.cs` (line 24)

### Constructors

- `protected HexViewCreationListener()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreationListener.cs` (line 28)

### Methods

- `public abstract void HexViewCreated(HexView hexView)`
  - Summary: Called after a hex view with the correct role is created
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreationListener.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.HexViewCreated(hexView: /* HexView */);
    ```

## Class `HexViewCreatorOptions`

creator options

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexViewCreatorOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreatorOptions.cs` (line 28)

### Constructors

- `public HexViewCreatorOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreatorOptions.cs` (line 48)

### Methods

- `public HexViewCreatorOptions Clone()`
  - Summary: Clones this
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreatorOptions.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```
- `public HexViewCreatorOptions CopyTo(HexViewCreatorOptions other)`
  - Summary: Copy this to
  - Parameters:
    - `HexViewCreatorOptions other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreatorOptions.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* HexViewCreatorOptions */);
    ```

### Properties

- `public Func<GuidObjectsProviderArgs, IEnumerable<GuidObject>> CreateGuidObjects { get; set; }`
  - Summary: Creates s, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreatorOptions.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CreateGuidObjects;
    ```
- `public Guid? MenuGuid { get; set; }`
  - Summary: Guid of context menu or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewCreatorOptions.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MenuGuid;
    ```

## Class `HexViewLayoutChangedEventArgs`

Hex view layout changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexViewLayoutChangedEventArgs(oldState: /* HexViewState */, newState: /* HexViewState */, newOrReformattedLines: /* IList<HexViewLine> */, translatedLines: /* IList<HexViewLine> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 29)

### Constructors

- `public HexViewLayoutChangedEventArgs(HexViewState oldState, HexViewState newState, IList<HexViewLine> newOrReformattedLines, IList<HexViewLine> translatedLines)`
  - Summary: Constructor
  - Parameters:
    - `HexViewState oldState`: Old view state
    - `HexViewState newState`: New view state
    - `IList<HexViewLine> newOrReformattedLines`: New or reformatted lines
    - `IList<HexViewLine> translatedLines`: Translated lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 100)

### Properties

- `public HexVersion NewVersion => NewViewState.Version`
  - Summary: Gets the new version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewVersion;
    ```
- `public HexVersion OldVersion => OldViewState.Version`
  - Summary: Gets the old version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldVersion;
    ```
- `public HexViewState NewViewState { get; }`
  - Summary: Gets the new view state
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewViewState;
    ```
- `public HexViewState OldViewState { get; }`
  - Summary: Gets the old view state
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldViewState;
    ```
- `public NormalizedHexBufferSpanCollection NewOrReformattedSpans => newOrReformattedSpans ?? (newOrReformattedSpans = CreateSpans(NewOrReformattedLines))`
  - Summary: Gets all new or reformatted spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewOrReformattedSpans;
    ```
- `public NormalizedHexBufferSpanCollection TranslatedSpans => translatedSpans ?? (translatedSpans = CreateSpans(TranslatedLines))`
  - Summary: Gets all translated spans
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 79)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TranslatedSpans;
    ```
- `public ReadOnlyCollection<HexViewLine> NewOrReformattedLines { get; }`
  - Summary: Gets all new or reformatted lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewOrReformattedLines;
    ```
- `public ReadOnlyCollection<HexViewLine> TranslatedLines { get; }`
  - Summary: Gets all translated lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TranslatedLines;
    ```
- `public bool HorizontalTranslation => OldViewState.ViewportLeft != NewViewState.ViewportLeft`
  - Summary: true if the layout was translated horizontally
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HorizontalTranslation;
    ```
- `public bool VerticalTranslation => OldViewState.ViewportTop != NewViewState.ViewportTop`
  - Summary: true if the layout was translated vertically
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLayoutChangedEventArgs.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VerticalTranslation;
    ```

## Class `HexViewLineCollection`

Hex view line collection

**Inherits/Implements:** `IReadOnlyList<HexViewLine>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexViewLineCollection();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 30)

### Constructors

- `protected HexViewLineCollection()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 34)

### Methods

- `public abstract Collection<HexViewLine> GetHexViewLinesIntersectingSpan(HexBufferSpan bufferSpan)`
  - Summary: Gets all lines intersecting with
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHexViewLinesIntersectingSpan(bufferSpan: /* HexBufferSpan */);
    ```
- `public abstract Collection<VSTF.TextBounds> GetNormalizedTextBounds(HexBufferSpan bufferPosition, HexSpanSelectionFlags flags)`
  - Summary: Gets normalized text bounds
  - Parameters:
    - `HexBufferSpan bufferPosition`: Position
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNormalizedTextBounds(bufferPosition: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
    ```
- `public abstract HexViewLine GetHexViewLineContainingBufferPosition(HexBufferPoint bufferPosition)`
  - Summary: Gets the line containing
  - Parameters:
    - `HexBufferPoint bufferPosition`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHexViewLineContainingBufferPosition(bufferPosition: /* HexBufferPoint */);
    ```
- `public abstract HexViewLine GetHexViewLineContainingYCoordinate(double y)`
  - Summary: Gets the line containing
  - Parameters:
    - `double y`: Y position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHexViewLineContainingYCoordinate(y: /* double */);
    ```
- `public abstract IEnumerator<HexViewLine> GetEnumerator()`
  - Summary: Gets the enumerator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEnumerator();
    ```
- `public abstract bool ContainsBufferPosition(HexBufferPoint bufferPosition)`
  - Summary: Returns true if this collection contains
  - Parameters:
    - `HexBufferPoint bufferPosition`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.ContainsBufferPosition(bufferPosition: /* HexBufferPoint */);
    ```
- `public abstract bool IntersectsBufferSpan(HexBufferSpan bufferSpan)`
  - Summary: Returns true if this collection intersects with
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.IntersectsBufferSpan(bufferSpan: /* HexBufferSpan */);
    ```

### Properties

- `public abstract HexBufferSpan FormattedSpan { get; }`
  - Summary: Gets the span of all lines in this collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FormattedSpan;
    ```
- `public abstract HexViewLine FirstVisibleLine { get; }`
  - Summary: Gets the first visible line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FirstVisibleLine;
    ```
- `public abstract HexViewLine LastVisibleLine { get; }`
  - Summary: Gets the last visible line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LastVisibleLine;
    ```
- `public abstract bool IsValid { get; }`
  - Summary: true if it's valid, false if it has been disposed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsValid;
    ```
- `public abstract int Count { get; }`
  - Summary: Gets the number of lines in this collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Count;
    ```

### Indexers

- `public abstract HexViewLine this[int index]`
  - Summary: Gets a line
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewLineCollection.cs` (line 51)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

## Class `HexViewMargin`

Hex view margin

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexViewMargin();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewMargin.cs` (line 26)

### Constructors

- `protected HexViewMargin()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewMargin.cs` (line 30)

### Methods

- `protected virtual void DisposeCore()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewMargin.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.DisposeCore();
    ```
- `public abstract HexViewMargin GetHexViewMargin(string marginName)`
  - Summary: Gets a or null if it's not this margin or a child of this margin
  - Parameters:
    - `string marginName`: Name of margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewMargin.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHexViewMargin(marginName: /* string */);
    ```
- `public void Dispose()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewMargin.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Properties

- `public abstract bool Enabled { get; }`
  - Summary: true if the margin is enabled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewMargin.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Enabled;
    ```
- `public abstract double MarginSize { get; }`
  - Summary: Gets the size of the margin (width or height depending on whether it's a vertical or horizontal margin)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewMargin.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MarginSize;
    ```

## Class `HexViewOptionDefinition<T>`

option definition

**Inherits/Implements:** `HexEditorOptionDefinition<T>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexViewOptionDefinition<T>();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 95)

### Constructors

- `protected HexViewOptionDefinition()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 99)

### Methods

- `public override bool IsApplicableToScope(VSUTIL.IPropertyOwner scope)`
  - Summary: Returns true if is a
  - Parameters:
    - `VSUTIL.IPropertyOwner scope`: Scope
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.IsApplicableToScope(scope: /* VSUTIL.IPropertyOwner */);
    ```

## Class `HexViewScroller`

View scroller

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexViewScroller();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 27)

### Constructors

- `protected HexViewScroller()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 31)

### Methods

- `public abstract bool ScrollViewportVerticallyByPage(VSTE.ScrollDirection direction)`
  - Summary: Scrolls the viewport one page up or down
  - Parameters:
    - `VSTE.ScrollDirection direction`: Direction
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollViewportVerticallyByPage(direction: /* VSTE.ScrollDirection */);
    ```
- `public abstract void EnsureSpanVisible(HexBufferLine line, VST.Span span, VSTE.EnsureSpanVisibleOptions options)`
  - Summary: Scrolls a line into view
  - Parameters:
    - `HexBufferLine line`: Line
    - `VST.Span span`: Line span
    - `VSTE.EnsureSpanVisibleOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.EnsureSpanVisible(line: /* HexBufferLine */, span: /* VST.Span */, options: /* VSTE.EnsureSpanVisibleOptions */);
    ```
- `public abstract void EnsureSpanVisible(HexBufferSpan span, HexSpanSelectionFlags flags, VSTE.EnsureSpanVisibleOptions options)`
  - Summary: Scrolls a span into view
  - Parameters:
    - `HexBufferSpan span`: Span
    - `HexSpanSelectionFlags flags`: Flags
    - `VSTE.EnsureSpanVisibleOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.EnsureSpanVisible(span: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */, options: /* VSTE.EnsureSpanVisibleOptions */);
    ```
- `public abstract void EnsureSpanVisible(HexLineSpan lineSpan, VSTE.EnsureSpanVisibleOptions options)`
  - Summary: Scrolls a span into view
  - Parameters:
    - `HexLineSpan lineSpan`: Line span
    - `VSTE.EnsureSpanVisibleOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.EnsureSpanVisible(lineSpan: /* HexLineSpan */, options: /* VSTE.EnsureSpanVisibleOptions */);
    ```
- `public abstract void ScrollViewportHorizontallyByPixels(double distanceToScroll)`
  - Summary: Scrolls the viewport horizontally
  - Parameters:
    - `double distanceToScroll`: Distance to scroll
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollViewportHorizontallyByPixels(distanceToScroll: /* double */);
    ```
- `public abstract void ScrollViewportVerticallyByLines(VSTE.ScrollDirection direction, int count)`
  - Summary: Scrolls the viewport by lines
  - Parameters:
    - `VSTE.ScrollDirection direction`: Direction
    - `int count`: Number of lines to scroll
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollViewportVerticallyByLines(direction: /* VSTE.ScrollDirection */, count: /* int */);
    ```
- `public abstract void ScrollViewportVerticallyByPixels(double distanceToScroll)`
  - Summary: Scrolls the viewport vertically
  - Parameters:
    - `double distanceToScroll`: Distance to scroll
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollViewportVerticallyByPixels(distanceToScroll: /* double */);
    ```
- `public void EnsureSpanVisible(HexBufferLine line, VST.Span span)`
  - Summary: Scrolls a line into view
  - Parameters:
    - `HexBufferLine line`: Line
    - `VST.Span span`: Line span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.EnsureSpanVisible(line: /* HexBufferLine */, span: /* VST.Span */);
    ```
- `public void EnsureSpanVisible(HexBufferSpan span, HexSpanSelectionFlags flags)`
  - Summary: Scrolls a span into view
  - Parameters:
    - `HexBufferSpan span`: Span
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.EnsureSpanVisible(span: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
    ```
- `public void EnsureSpanVisible(HexLineSpan lineSpan)`
  - Summary: Scrolls a span into view
  - Parameters:
    - `HexLineSpan lineSpan`: Line span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.EnsureSpanVisible(lineSpan: /* HexLineSpan */);
    ```
- `public void ScrollViewportVerticallyByLine(VSTE.ScrollDirection direction)`
  - Summary: Scrolls the viewport one line up or down
  - Parameters:
    - `VSTE.ScrollDirection direction`: Direction
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewScroller.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollViewportVerticallyByLine(direction: /* VSTE.ScrollDirection */);
    ```

## Class `HexViewState`

Hex view state

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.HexViewState(view: /* HexView */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 26)

### Constructors

- `public HexViewState(HexView view)`
  - Summary: Constructor
  - Parameters:
    - `HexView view`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 71)
- `public HexViewState(HexView view, double effectiveViewportWidth, double effectiveViewportHeight)`
  - Summary: Constructor
  - Parameters:
    - `HexView view`: Hex view
    - `double effectiveViewportWidth`: Viewport width
    - `double effectiveViewportHeight`: Viewport height
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 81)

### Properties

- `public HexBuffer Buffer { get; }`
  - Summary: Gets the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Buffer;
    ```
- `public HexVersion Version { get; }`
  - Summary: Gets the version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Version;
    ```
- `public double ViewportBottom => ViewportTop + ViewportHeight`
  - Summary: Gets viewport bottom
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportBottom;
    ```
- `public double ViewportHeight { get; }`
  - Summary: Gets viewport height
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportHeight;
    ```
- `public double ViewportLeft { get; }`
  - Summary: Gets viewport left
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportLeft;
    ```
- `public double ViewportRight => ViewportLeft + ViewportWidth`
  - Summary: Gets viewport right
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportRight;
    ```
- `public double ViewportTop { get; }`
  - Summary: Gets viewport top
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportTop;
    ```
- `public double ViewportWidth { get; }`
  - Summary: Gets viewport width
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexViewState.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ViewportWidth;
    ```

## Interface `IHexMarginContextMenuHandler`

Creates context menu objects

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Editor.IHexMarginContextMenuHandler and call its members.
var instance = new dnSpy.Contracts.Hex.Editor.IHexMarginContextMenuHandler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginContextMenuHandlerProvider.cs` (line 50)

### Methods

- `IEnumerable<GuidObject> GetContextMenuObjects(Point marginRelativePoint)`
  - Summary: Creates context menu objects
  - Parameters:
    - `Point marginRelativePoint`: Position of the mouse pointer relative to the glyph margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexMarginContextMenuHandlerProvider.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.GetContextMenuObjects(marginRelativePoint: /* Point */);
    ```

## Class `PredefinedHexAdornmentLayers`

Predefined hex adornment layer names

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers members directly without instantiation.
dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 24)

### Fields

- `public const string ActiveColumnHighlighter = prefix + nameof(ActiveColumnHighlighter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.ActiveColumnHighlighter;
    ```
- `public const string BackgroundImage = prefix + nameof(BackgroundImage)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.BackgroundImage;
    ```
- `public const string BottomLayer = prefix + nameof(BottomLayer)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.BottomLayer;
    ```
- `public const string Caret = prefix + nameof(Caret)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.Caret;
    ```
- `public const string ColumnLineSeparator = prefix + nameof(ColumnLineSeparator)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.ColumnLineSeparator;
    ```
- `public const string CurrentLineHighlighter = prefix + nameof(CurrentLineHighlighter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.CurrentLineHighlighter;
    ```
- `public const string GlyphTextMarker = prefix + nameof(GlyphTextMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.GlyphTextMarker;
    ```
- `public const string IntraTextAdornment = prefix + nameof(IntraTextAdornment)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.IntraTextAdornment;
    ```
- `public const string NegativeTextMarker = prefix + nameof(NegativeTextMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.NegativeTextMarker;
    ```
- `public const string Outlining = prefix + nameof(Outlining)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.Outlining;
    ```
- `public const string Search = prefix + nameof(Search)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.Search;
    ```
- `public const string Selection = prefix + nameof(Selection)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.Selection;
    ```
- `public const string Text = prefix + nameof(Text)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.Text;
    ```
- `public const string TextMarker = prefix + nameof(TextMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.TextMarker;
    ```
- `public const string TopLayer = prefix + nameof(TopLayer)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexAdornmentLayers.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexAdornmentLayers.TopLayer;
    ```

## Class `PredefinedHexCursorPriorities`

Cursor priorities

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.PredefinedHexCursorPriorities members directly without instantiation.
dnSpy.Contracts.Hex.Editor.PredefinedHexCursorPriorities./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 44)

### Fields

- `public static readonly double High = 100000`
  - Summary: High priority
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexCursorPriorities.High;
    ```
- `public static readonly double Low = -100000`
  - Summary: Low priority
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexCursorPriorities.Low;
    ```
- `public static readonly double Normal = 0`
  - Summary: Normal priority
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexCursorPriorities.Normal;
    ```
- `public static readonly double Offset = High`
  - Summary: Priority of the offset cursor (hand)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexCursorProvider.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexCursorPriorities.Offset;
    ```

## Class `PredefinedHexGlyphFactoryProviderNames`

names

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.PredefinedHexGlyphFactoryProviderNames members directly without instantiation.
dnSpy.Contracts.Hex.Editor.PredefinedHexGlyphFactoryProviderNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexGlyphFactoryProviderNames.cs` (line 24)

### Fields

- `public const string HexImageReference = prefix + nameof(HexImageReference)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexGlyphFactoryProviderNames.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexGlyphFactoryProviderNames.HexImageReference;
    ```

## Class `PredefinedHexMarginNames`

Predefined hex margin names

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames members directly without instantiation.
dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 24)

### Fields

- `public const string Bottom = prefix + nameof(Bottom)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.Bottom;
    ```
- `public const string BottomControl = prefix + nameof(BottomControl)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.BottomControl;
    ```
- `public const string BottomRightCorner = prefix + nameof(BottomRightCorner)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 45)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.BottomRightCorner;
    ```
- `public const string CustomLineNumber = prefix + nameof(CustomLineNumber)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.CustomLineNumber;
    ```
- `public const string Glyph = prefix + nameof(Glyph)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.Glyph;
    ```
- `public const string HorizontalScrollBar = prefix + nameof(HorizontalScrollBar)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.HorizontalScrollBar;
    ```
- `public const string HorizontalScrollBarContainer = prefix + nameof(HorizontalScrollBarContainer)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.HorizontalScrollBarContainer;
    ```
- `public const string Left = prefix + nameof(Left)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.Left;
    ```
- `public const string LeftSelection = prefix + nameof(LeftSelection)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.LeftSelection;
    ```
- `public const string LineNumber = prefix + nameof(LineNumber)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.LineNumber;
    ```
- `public const string Outlining = prefix + nameof(Outlining)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.Outlining;
    ```
- `public const string Right = prefix + nameof(Right)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.Right;
    ```
- `public const string RightControl = prefix + nameof(RightControl)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.RightControl;
    ```
- `public const string Spacer = prefix + nameof(Spacer)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.Spacer;
    ```
- `public const string Suggestion = prefix + nameof(Suggestion)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.Suggestion;
    ```
- `public const string Top = prefix + nameof(Top)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.Top;
    ```
- `public const string VerticalScrollBar = prefix + nameof(VerticalScrollBar)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.VerticalScrollBar;
    ```
- `public const string VerticalScrollBarContainer = prefix + nameof(VerticalScrollBarContainer)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.VerticalScrollBarContainer;
    ```
- `public const string ZoomControl = prefix + nameof(ZoomControl)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexMarginNames.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexMarginNames.ZoomControl;
    ```

## Class `PredefinedHexReferenceHandlerNames`

Predefined names

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.PredefinedHexReferenceHandlerNames members directly without instantiation.
dnSpy.Contracts.Hex.Editor.PredefinedHexReferenceHandlerNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexReferenceHandlerNames.cs` (line 24)

### Fields

- `public const string DefaultApplicationHandler = nameof(DefaultApplicationHandler)`
  - Summary: Default handler used by the application, and should be last
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexReferenceHandlerNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexReferenceHandlerNames.DefaultApplicationHandler;
    ```

## Class `PredefinedHexReferenceHandlerTags`

Tags passed to

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.PredefinedHexReferenceHandlerTags members directly without instantiation.
dnSpy.Contracts.Hex.Editor.PredefinedHexReferenceHandlerTags./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexReferenceHandlerTags.cs` (line 24)

### Fields

- `public static readonly string NewTab = nameof(NewTab)`
  - Summary: Open the reference in a new tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexReferenceHandlerTags.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexReferenceHandlerTags.NewTab;
    ```

## Class `PredefinedHexSpaceReservationManagerNames`

Predefined names

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.PredefinedHexSpaceReservationManagerNames members directly without instantiation.
dnSpy.Contracts.Hex.Editor.PredefinedHexSpaceReservationManagerNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexSpaceReservationManagerNames.cs` (line 26)

### Fields

- `public const string ToolTip = "ToolTip"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexSpaceReservationManagerNames.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexSpaceReservationManagerNames.ToolTip;
    ```

## Class `PredefinedHexStructureInfoProviderFactoryNames`

names

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.PredefinedHexStructureInfoProviderFactoryNames members directly without instantiation.
dnSpy.Contracts.Hex.Editor.PredefinedHexStructureInfoProviderFactoryNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexStructureInfoProviderFactoryNames.cs` (line 26)

### Fields

- `public const string DefaultHexFileStructure = nameof(DefaultHexFileStructure)`
  - Summary: Name of provider that uses s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexStructureInfoProviderFactoryNames.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexStructureInfoProviderFactoryNames.DefaultHexFileStructure;
    ```

## Class `PredefinedHexViewRoles`

Predefined hex view roles

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles members directly without instantiation.
dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 24)

### Fields

- `public const string Analyzable = prefix + nameof(Analyzable)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.Analyzable;
    ```
- `public const string CanHaveBackgroundImage = prefix + nameof(CanHaveBackgroundImage)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.CanHaveBackgroundImage;
    ```
- `public const string CanHaveColumnLineSeparator = prefix + nameof(CanHaveColumnLineSeparator)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.CanHaveColumnLineSeparator;
    ```
- `public const string CanHaveCurrentLineHighlighter = prefix + nameof(CanHaveCurrentLineHighlighter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.CanHaveCurrentLineHighlighter;
    ```
- `public const string CanHaveGlyphMargin = prefix + nameof(CanHaveGlyphMargin)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.CanHaveGlyphMargin;
    ```
- `public const string CanHaveIntellisenseControllers = prefix + nameof(CanHaveIntellisenseControllers)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.CanHaveIntellisenseControllers;
    ```
- `public const string CanHighlightActiveColumn = prefix + nameof(CanHighlightActiveColumn)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.CanHighlightActiveColumn;
    ```
- `public const string Debuggable = prefix + nameof(Debuggable)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.Debuggable;
    ```
- `public const string Document = prefix + nameof(Document)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.Document;
    ```
- `public const string Editable = prefix + nameof(Editable)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.Editable;
    ```
- `public const string EmbeddedPeekHexView = prefix + nameof(EmbeddedPeekHexView)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.EmbeddedPeekHexView;
    ```
- `public const string HexEditorGroup = prefix + nameof(HexEditorGroup)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.HexEditorGroup;
    ```
- `public const string HexEditorGroupDebuggerMemory = prefix + nameof(HexEditorGroupDebuggerMemory)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.HexEditorGroupDebuggerMemory;
    ```
- `public const string HexEditorGroupDefault = prefix + nameof(HexEditorGroupDefault)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 45)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.HexEditorGroupDefault;
    ```
- `public const string Interactive = prefix + nameof(Interactive)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.Interactive;
    ```
- `public const string PreviewHexView = prefix + nameof(PreviewHexView)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.PreviewHexView;
    ```
- `public const string PrimaryDocument = prefix + nameof(PrimaryDocument)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.PrimaryDocument;
    ```
- `public const string Printable = prefix + nameof(Printable)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.Printable;
    ```
- `public const string Structured = prefix + nameof(Structured)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.Structured;
    ```
- `public const string Zoomable = prefix + nameof(Zoomable)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/PredefinedHexViewRoles.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Editor.PredefinedHexViewRoles.Zoomable;
    ```

## Class `WpfHexView`

WPF hex view

**Inherits/Implements:** `HexView`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.WpfHexView();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 30)

### Constructors

- `protected WpfHexView()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 34)

### Methods

- `public abstract HexAdornmentLayer GetAdornmentLayer(string name)`
  - Summary: Gets an adornment layer
  - Parameters:
    - `string name`: Name of adornment layer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAdornmentLayer(name: /* string */);
    ```
- `public abstract HexSpaceReservationManager GetSpaceReservationManager(string name)`
  - Summary: Gets the space reservation manager
  - Parameters:
    - `string name`: Name of space reservation manager
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSpaceReservationManager(name: /* string */);
    ```
- `public abstract WpfHexViewLine GetWpfHexViewLineContainingBufferPosition(HexBufferPoint bufferPosition)`
  - Summary: Gets the line that contains the position
  - Parameters:
    - `HexBufferPoint bufferPosition`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.GetWpfHexViewLineContainingBufferPosition(bufferPosition: /* HexBufferPoint */);
    ```

### Properties

- `public abstract Brush Background { get; set; }`
  - Summary: Gets/sets the background brush
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Background;
    ```
- `public abstract FrameworkElement VisualElement { get; }`
  - Summary: Gets the UI element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VisualElement;
    ```
- `public abstract HexFormattedLineSource FormattedLineSource { get; }`
  - Summary: Gets the formatted line source
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FormattedLineSource;
    ```
- `public abstract HexLineTransformSource LineTransformSource { get; }`
  - Summary: Gets the line transform source
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LineTransformSource;
    ```
- `public abstract WpfHexViewLineCollection WpfHexViewLines { get; }`
  - Summary: Gets the WPF hex view lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.WpfHexViewLines;
    ```
- `public abstract double ZoomLevel { get; set; }`
  - Summary: Gets/sets the zoom level between 20% to 400%
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ZoomLevel;
    ```

### Events

- `public abstract event EventHandler<VSTE.BackgroundBrushChangedEventArgs> BackgroundBrushChanged`
  - Summary: Raised when the background property has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 49)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BackgroundBrushChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<VSTE.ZoomLevelChangedEventArgs> ZoomLevelChanged`
  - Summary: Raised when the zoom level has changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexView.cs` (line 59)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ZoomLevelChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `WpfHexViewCreationListener`

Gets notified when hex views get created, see also

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.WpfHexViewCreationListener();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewCreationListener.cs` (line 24)

### Constructors

- `protected WpfHexViewCreationListener()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewCreationListener.cs` (line 28)

### Methods

- `public abstract void HexViewCreated(WpfHexView hexView)`
  - Summary: Called after a hex view with the correct role is created
  - Parameters:
    - `WpfHexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewCreationListener.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.HexViewCreated(hexView: /* WpfHexView */);
    ```

## Class `WpfHexViewHost`

WPF hex view host

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.WpfHexViewHost();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewHost.cs` (line 27)

### Constructors

- `protected WpfHexViewHost()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewHost.cs` (line 31)

### Methods

- `public abstract WpfHexViewMargin GetHexViewMargin(string marginName)`
  - Summary: Gets a margin or null if it doesn't exist
  - Parameters:
    - `string marginName`: Name of margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewHost.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHexViewMargin(marginName: /* string */);
    ```
- `public abstract void Close()`
  - Summary: Closes this host and its hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewHost.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```

### Properties

- `public abstract Control HostControl { get; }`
  - Summary: Gets the UI element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewHost.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HostControl;
    ```
- `public abstract WpfHexView HexView { get; }`
  - Summary: Gets the hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewHost.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexView;
    ```
- `public abstract bool IsClosed { get; }`
  - Summary: true if the host has been closed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewHost.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsClosed;
    ```

### Events

- `public abstract event EventHandler Closed`
  - Summary: Raised when it is closed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewHost.cs` (line 46)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Closed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `WpfHexViewLineCollection`

WPF hex view line collection

**Inherits/Implements:** `HexViewLineCollection`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.WpfHexViewLineCollection();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 30)

### Constructors

- `protected WpfHexViewLineCollection()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 34)

### Methods

- `public abstract Geometry GetLineMarkerGeometry(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags)`
  - Summary: Gets a line marker geometry
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineMarkerGeometry(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
    ```
- `public abstract Geometry GetLineMarkerGeometry(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags, bool clipToViewport, Thickness padding)`
  - Summary: Gets a line marker geometry
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span
    - `HexSpanSelectionFlags flags`: Flags
    - `bool clipToViewport`: true to clip the geometry to the viewport
    - `Thickness padding`: Padding to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 127)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineMarkerGeometry(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */, clipToViewport: /* bool */, padding: /* Thickness */);
    ```
- `public abstract Geometry GetLineMarkerGeometry(WpfHexViewLine line, VST.Span span)`
  - Summary: Gets a line marker geometry
  - Parameters:
    - `WpfHexViewLine line`: A line in this collection
    - `VST.Span span`: Text span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineMarkerGeometry(line: /* WpfHexViewLine */, span: /* VST.Span */);
    ```
- `public abstract Geometry GetLineMarkerGeometry(WpfHexViewLine line, VST.Span span, bool clipToViewport, Thickness padding)`
  - Summary: Gets a line marker geometry
  - Parameters:
    - `WpfHexViewLine line`: A line in this collection
    - `VST.Span span`: Text span
    - `bool clipToViewport`: true to clip the geometry to the viewport
    - `Thickness padding`: Padding to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLineMarkerGeometry(line: /* WpfHexViewLine */, span: /* VST.Span */, clipToViewport: /* bool */, padding: /* Thickness */);
    ```
- `public abstract Geometry GetMarkerGeometry(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags)`
  - Summary: Gets a marker geometry
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMarkerGeometry(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
    ```
- `public abstract Geometry GetMarkerGeometry(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags, bool clipToViewport, Thickness padding)`
  - Summary: Gets a marker geometry
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span
    - `HexSpanSelectionFlags flags`: Flags
    - `bool clipToViewport`: true to clip the geometry to the viewport
    - `Thickness padding`: Padding to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 145)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMarkerGeometry(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */, clipToViewport: /* bool */, padding: /* Thickness */);
    ```
- `public abstract Geometry GetTextMarkerGeometry(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags)`
  - Summary: Gets a text marker geometry
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span
    - `HexSpanSelectionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTextMarkerGeometry(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */);
    ```
- `public abstract Geometry GetTextMarkerGeometry(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags, bool clipToViewport, Thickness padding)`
  - Summary: Gets a text marker geometry
  - Parameters:
    - `HexBufferSpan bufferSpan`: Span
    - `HexSpanSelectionFlags flags`: Flags
    - `bool clipToViewport`: true to clip the geometry to the viewport
    - `Thickness padding`: Padding to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 163)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTextMarkerGeometry(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */, clipToViewport: /* bool */, padding: /* Thickness */);
    ```
- `public abstract Geometry GetTextMarkerGeometry(WpfHexViewLine line, VST.Span span)`
  - Summary: Gets a text marker geometry
  - Parameters:
    - `WpfHexViewLine line`: A line in this collection
    - `VST.Span span`: Text span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTextMarkerGeometry(line: /* WpfHexViewLine */, span: /* VST.Span */);
    ```
- `public abstract Geometry GetTextMarkerGeometry(WpfHexViewLine line, VST.Span span, bool clipToViewport, Thickness padding)`
  - Summary: Gets a text marker geometry
  - Parameters:
    - `WpfHexViewLine line`: A line in this collection
    - `VST.Span span`: Text span
    - `bool clipToViewport`: true to clip the geometry to the viewport
    - `Thickness padding`: Padding to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTextMarkerGeometry(line: /* WpfHexViewLine */, span: /* VST.Span */, clipToViewport: /* bool */, padding: /* Thickness */);
    ```
- `public abstract WpfHexViewLine GetWpfHexViewLine(int index)`
  - Summary: Gets a line
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.GetWpfHexViewLine(index: /* int */);
    ```
- `public abstract WpfHexViewLine GetWpfHexViewLineContainingBufferPosition(HexBufferPoint bufferPosition)`
  - Summary: Gets the line containing
  - Parameters:
    - `HexBufferPoint bufferPosition`: Buffer position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 170)
  - Example:
    ```csharp
    // Example invocation
    instance.GetWpfHexViewLineContainingBufferPosition(bufferPosition: /* HexBufferPoint */);
    ```

### Properties

- `public abstract ReadOnlyCollection<WpfHexViewLine> WpfHexViewLines { get; }`
  - Summary: Gets all the lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.WpfHexViewLines;
    ```
- `public abstract WpfHexViewLine FirstVisibleWpfLine { get; }`
  - Summary: Gets the first visible line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FirstVisibleWpfLine;
    ```
- `public abstract WpfHexViewLine LastVisibleWpfLine { get; }`
  - Summary: Gets the last visible line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LastVisibleWpfLine;
    ```
- `public override HexViewLine FirstVisibleLine => FirstVisibleWpfLine`
  - Summary: Gets the first visible line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FirstVisibleLine;
    ```
- `public override HexViewLine LastVisibleLine => LastVisibleWpfLine`
  - Summary: Gets the last visible line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LastVisibleLine;
    ```

### Indexers

- `public override HexViewLine this[int index]`
  - Summary: Gets a line
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewLineCollection.cs` (line 48)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

## Class `WpfHexViewMargin`

WPF hex view margin

**Inherits/Implements:** `HexViewMargin`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.WpfHexViewMargin();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewMargin.cs` (line 26)

### Constructors

- `protected WpfHexViewMargin()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewMargin.cs` (line 30)

### Properties

- `public abstract FrameworkElement VisualElement { get; }`
  - Summary: Gets the UI element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewMargin.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VisualElement;
    ```

## Class `WpfHexViewMarginProvider`

Creates s

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.WpfHexViewMarginProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewMarginProvider.cs` (line 24)

### Constructors

- `protected WpfHexViewMarginProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewMarginProvider.cs` (line 28)

### Methods

- `public abstract WpfHexViewMargin CreateMargin(WpfHexViewHost wpfHexViewHost, WpfHexViewMargin marginContainer)`
  - Summary: Creates a margin or returns null
  - Parameters:
    - `WpfHexViewHost wpfHexViewHost`: WPF hex view host
    - `WpfHexViewMargin marginContainer`: Margin container
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/WpfHexViewMarginProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateMargin(wpfHexViewHost: /* WpfHexViewHost */, marginContainer: /* WpfHexViewMargin */);
    ```

## Class `WpfHexViewOptionDefinition<T>`

option definition

**Inherits/Implements:** `HexEditorOptionDefinition<T>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Editor.WpfHexViewOptionDefinition<T>();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 112)

### Constructors

- `protected WpfHexViewOptionDefinition()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 116)

### Methods

- `public override bool IsApplicableToScope(VSUTIL.IPropertyOwner scope)`
  - Summary: Returns true if is a
  - Parameters:
    - `VSUTIL.IPropertyOwner scope`: Scope
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Editor/HexEditorOptionDefinition.cs` (line 123)
  - Example:
    ```csharp
    // Example invocation
    instance.IsApplicableToScope(scope: /* VSUTIL.IPropertyOwner */);
    ```

