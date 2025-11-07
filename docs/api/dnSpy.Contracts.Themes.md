# Namespace `dnSpy.Contracts.Themes`

## Enum `ColorType`

Color type

**Inherits/Implements:** `uint`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Themes.ColorType and call its members.
var instance = new dnSpy.Contracts.Themes.ColorType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Themes/ColorType.cs` (line 24)

### Members

- `Text` = `x00004000`
- `FirstNR` = `ext`
- `Operator`
- `Punctuation`
- `Number`
- `Comment`
- `Keyword`
- `String`
- `VerbatimString`
- `Char`
- `Namespace`
- `Type`
- `SealedType`
- `StaticType`
- `Delegate`
- `Enum`
- `Interface`
- `ValueType`
- `Module`
- `TypeGenericParameter`
- `MethodGenericParameter`
- `InstanceMethod`
- `StaticMethod`
- `ExtensionMethod`
- `InstanceField`
- `EnumField`
- `LiteralField`
- `StaticField`
- `InstanceEvent`
- `StaticEvent`
- `InstanceProperty`
- `StaticProperty`
- `Local`
- `Parameter`
- `PreprocessorKeyword`
- `PreprocessorText`
- `Label`
- `OpCode`
- `ILDirective`
- `ILModule`
- `ExcludedCode`
- `XmlDocCommentAttributeName`
- `XmlDocCommentAttributeQuotes`
- `XmlDocCommentAttributeValue`
- `XmlDocCommentCDataSection`
- `XmlDocCommentComment`
- `XmlDocCommentDelimiter`
- `XmlDocCommentEntityReference`
- `XmlDocCommentName`
- `XmlDocCommentProcessingInstruction`
- `XmlDocCommentText`
- `XmlLiteralAttributeName`
- `XmlLiteralAttributeQuotes`
- `XmlLiteralAttributeValue`
- `XmlLiteralCDataSection`
- `XmlLiteralComment`
- `XmlLiteralDelimiter`
- `XmlLiteralEmbeddedExpression`
- `XmlLiteralEntityReference`
- `XmlLiteralName`
- `XmlLiteralProcessingInstruction`
- `XmlLiteralText`
- `XmlAttribute`
- `XmlAttributeQuotes`
- `XmlAttributeValue`
- `XmlCDataSection`
- `XmlComment`
- `XmlDelimiter`
- `XmlKeyword`
- `XmlName`
- `XmlProcessingInstruction`
- `XmlText`
- `XamlAttribute`
- `XamlAttributeQuotes`
- `XamlAttributeValue`
- `XamlCDataSection`
- `XamlComment`
- `XamlDelimiter`
- `XamlKeyword`
- `XamlMarkupExtensionClass`
- `XamlMarkupExtensionParameterName`
- `XamlMarkupExtensionParameterValue`
- `XamlName`
- `XamlProcessingInstruction`
- `XamlText`
- `XmlDocToolTipHeader`
- `Assembly`
- `AssemblyExe`
- `AssemblyModule`
- `DirectoryPart`
- `FileNameNoExtension`
- `FileExtension`
- `Error`
- `ToStringEval`
- `ReplPrompt1`
- `ReplPrompt2`
- `ReplOutputText`
- `ReplScriptOutputText`
- `Black`
- `Blue`
- `Cyan`
- `DarkBlue`
- `DarkCyan`
- `DarkGray`
- `DarkGreen`
- `DarkMagenta`
- `DarkRed`
- `DarkYellow`
- `Gray`
- `Green`
- `Magenta`
- `Red`
- `White`
- `Yellow`
- `InvBlack`
- `InvBlue`
- `InvCyan`
- `InvDarkBlue`
- `InvDarkCyan`
- `InvDarkGray`
- `InvDarkGreen`
- `InvDarkMagenta`
- `InvDarkRed`
- `InvDarkYellow`
- `InvGray`
- `InvGreen`
- `InvMagenta`
- `InvRed`
- `InvWhite`
- `InvYellow`
- `DebugLogExceptionHandled`
- `DebugLogExceptionUnhandled`
- `DebugLogStepFiltering`
- `DebugLogLoadModule`
- `DebugLogUnloadModule`
- `DebugLogExitProcess`
- `DebugLogExitThread`
- `DebugLogProgramOutput`
- `DebugLogMDA`
- `DebugLogTimestamp`
- `LineNumber`
- `ReplLineNumberInput1`
- `ReplLineNumberInput2`
- `ReplLineNumberOutput`
- `VisibleWhitespace`
- `SelectedText`
- `InactiveSelectedText`
- `HighlightedReference`
- `HighlightedWrittenReference`
- `HighlightedDefinition`
- `CurrentStatement`
- `CurrentStatementMarker`
- `CallReturn`
- `CallReturnMarker`
- `ActiveStatementMarker`
- `BreakpointStatement`
- `BreakpointStatementMarker`
- `SelectedBreakpointStatementMarker`
- `DisabledBreakpointStatementMarker`
- `CurrentLine`
- `CurrentLineNoFocus`
- `HexText`
- `HexOffset`
- `HexByte0`
- `HexByte1`
- `HexByteError`
- `HexAscii`
- `HexCaret`
- `HexInactiveCaret`
- `HexSelection`
- `GlyphMargin`
- `BraceMatching`
- `LineSeparator`
- `FindMatchHighlightMarker`
- `BlockStructureNamespace`
- `BlockStructureType`
- `BlockStructureModule`
- `BlockStructureValueType`
- `BlockStructureInterface`
- `BlockStructureMethod`
- `BlockStructureAccessor`
- `BlockStructureAnonymousMethod`
- `BlockStructureConstructor`
- `BlockStructureDestructor`
- `BlockStructureOperator`
- `BlockStructureConditional`
- `BlockStructureLoop`
- `BlockStructureProperty`
- `BlockStructureEvent`
- `BlockStructureTry`
- `BlockStructureCatch`
- `BlockStructureFilter`
- `BlockStructureFinally`
- `BlockStructureFault`
- `BlockStructureLock`
- `BlockStructureUsing`
- `BlockStructureFixed`
- `BlockStructureSwitch`
- `BlockStructureCase`
- `BlockStructureLocalFunction`
- `BlockStructureOther`
- `BlockStructureXml`
- `BlockStructureXaml`
- `CompletionMatchHighlight`
- `CompletionSuffix`
- `SignatureHelpDocumentation`
- `SignatureHelpCurrentParameter`
- `SignatureHelpParameter`
- `SignatureHelpParameterDocumentation`
- `Url`
- `HexPeDosHeader`
- `HexPeFileHeader`
- `HexPeOptionalHeader32`
- `HexPeOptionalHeader64`
- `HexPeSection`
- `HexPeSectionName`
- `HexCor20Header`
- `HexStorageSignature`
- `HexStorageHeader`
- `HexStorageStream`
- `HexStorageStreamName`
- `HexStorageStreamNameInvalid`
- `HexTablesStream`
- `HexTableName`
- `DocumentListMatchHighlight`
- `GacMatchHighlight`
- `AppSettingsTreeViewNodeMatchHighlight`
- `AppSettingsTextMatchHighlight`
- `HexCurrentLine`
- `HexCurrentLineNoFocus`
- `HexInactiveSelectedText`
- `HexColumnLine0`
- `HexColumnLine1`
- `HexColumnLineGroup0`
- `HexColumnLineGroup1`
- `HexHighlightedValuesColumn`
- `HexHighlightedAsciiColumn`
- `HexGlyphMargin`
- `HexCurrentValueCell`
- `HexCurrentAsciiCell`
- `OutputWindowText`
- `HexFindMatchHighlightMarker`
- `HexToolTipServiceField0`
- `HexToolTipServiceField1`
- `HexToolTipServiceCurrentField`
- `ListFindMatchHighlight`
- `AdvancedBreakpointStatement`
- `AdvancedBreakpointStatementMarker`
- `SelectedAdvancedBreakpointStatementMarker`
- `DisabledAdvancedBreakpointStatement`
- `DisabledAdvancedBreakpointStatementMarker`
- `SelectedDisabledAdvancedBreakpointStatementMarker`
- `BreakpointWarningStatement`
- `BreakpointWarningStatementMarker`
- `SelectedBreakpointWarningStatementMarker`
- `BreakpointErrorStatement`
- `BreakpointErrorStatementMarker`
- `SelectedBreakpointErrorStatementMarker`
- `AdvancedBreakpointWarningStatement`
- `AdvancedBreakpointWarningStatementMarker`
- `SelectedAdvancedBreakpointWarningStatementMarker`
- `AdvancedBreakpointErrorStatement`
- `AdvancedBreakpointErrorStatementMarker`
- `SelectedAdvancedBreakpointErrorStatementMarker`
- `TracepointStatement`
- `TracepointStatementMarker`
- `SelectedTracepointStatementMarker`
- `DisabledTracepointStatement`
- `DisabledTracepointStatementMarker`
- `SelectedDisabledTracepointStatementMarker`
- `AdvancedTracepointStatement`
- `AdvancedTracepointStatementMarker`
- `SelectedAdvancedTracepointStatementMarker`
- `DisabledAdvancedTracepointStatement`
- `DisabledAdvancedTracepointStatementMarker`
- `SelectedDisabledAdvancedTracepointStatementMarker`
- `TracepointWarningStatement`
- `TracepointWarningStatementMarker`
- `SelectedTracepointWarningStatementMarker`
- `TracepointErrorStatement`
- `TracepointErrorStatementMarker`
- `SelectedTracepointErrorStatementMarker`
- `AdvancedTracepointWarningStatement`
- `AdvancedTracepointWarningStatementMarker`
- `SelectedAdvancedTracepointWarningStatementMarker`
- `AdvancedTracepointErrorStatement`
- `AdvancedTracepointErrorStatementMarker`
- `SelectedAdvancedTracepointErrorStatementMarker`
- `BookmarkName`
- `ActiveBookmarkName`
- `DebugLogTrace`
- `DebugLogExtensionMessage`
- `DebuggerValueChangedHighlight`
- `DebugExceptionName`
- `DebugStowedExceptionName`
- `DebugReturnValueName`
- `DebugVariableName`
- `DebugObjectIdName`
- `DebuggerDisplayAttributeEval`
- `DebuggerNoStringQuotesEval`
- `DebugViewPropertyName`
- `AsmComment`
- `AsmDirective`
- `AsmPrefix`
- `AsmMnemonic`
- `AsmKeyword`
- `AsmOperator`
- `AsmPunctuation`
- `AsmNumber`
- `AsmRegister`
- `AsmSelectorValue`
- `AsmLabelAddress`
- `AsmFunctionAddress`
- `AsmLabel`
- `AsmFunction`
- `AsmData`
- `AsmAddress`
- `AsmHexBytes`
- `LastNR`
- `DefaultText` = `x00100000`
- `FirstUI` = `efaultText`
- `SystemColorsControl`
- `SystemColorsControlDark`
- `SystemColorsControlDarkDark`
- `SystemColorsControlLight`
- `SystemColorsControlLightLight`
- `SystemColorsControlText`
- `SystemColorsGrayText`
- `SystemColorsHighlight`
- `SystemColorsHighlightText`
- `SystemColorsInactiveCaption`
- `SystemColorsInactiveCaptionText`
- `SystemColorsInactiveSelectionHighlight`
- `SystemColorsInactiveSelectionHighlightText`
- `SystemColorsMenuText`
- `SystemColorsWindow`
- `SystemColorsWindowText`
- `PEHex`
- `PEHexBorder`
- `DialogWindow`
- `DialogWindowActiveCaption`
- `DialogWindowActiveDebuggingBorder`
- `DialogWindowActiveDefaultBorder`
- `DialogWindowButtonHoverInactive`
- `DialogWindowButtonHoverInactiveBorder`
- `DialogWindowButtonHoverInactiveGlyph`
- `DialogWindowButtonInactiveBorder`
- `DialogWindowButtonInactiveGlyph`
- `DialogWindowInactiveBorder`
- `DialogWindowInactiveCaption`
- `EnvironmentBackgroundBrush`
- `EnvironmentBackground`
- `EnvironmentForeground`
- `EnvironmentMainWindowActiveCaption`
- `EnvironmentMainWindowActiveDebuggingBorder`
- `EnvironmentMainWindowActiveDefaultBorder`
- `EnvironmentMainWindowButtonActiveBorder`
- `EnvironmentMainWindowButtonActiveGlyph`
- `EnvironmentMainWindowButtonDown`
- `EnvironmentMainWindowButtonDownBorder`
- `EnvironmentMainWindowButtonDownGlyph`
- `EnvironmentMainWindowButtonHoverActive`
- `EnvironmentMainWindowButtonHoverActiveBorder`
- `EnvironmentMainWindowButtonHoverActiveGlyph`
- `EnvironmentMainWindowButtonHoverInactive`
- `EnvironmentMainWindowButtonHoverInactiveBorder`
- `EnvironmentMainWindowButtonHoverInactiveGlyph`
- `EnvironmentMainWindowButtonInactiveBorder`
- `EnvironmentMainWindowButtonInactiveGlyph`
- `EnvironmentMainWindowInactiveBorder`
- `EnvironmentMainWindowInactiveCaption`
- `ControlShadow`
- `GridSplitterPreviewFill`
- `GroupBoxBorderBrush`
- `TopLevelMenuHeaderHoverBorder`
- `TopLevelMenuHeaderHover`
- `MenuItemSeparatorFillTop`
- `MenuItemSeparatorFillBottom`
- `MenuItemGlyphPanelBorderBrush`
- `MenuItemHighlightedInnerBorder`
- `MenuItemDisabledForeground`
- `MenuItemDisabledGlyphPanelBackground`
- `MenuItemDisabledGlyphFill`
- `ToolBarButtonPressed`
- `ToolBarSeparatorFill`
- `ToolBarButtonHover`
- `ToolBarButtonHoverBorder`
- `ToolBarButtonPressedBorder`
- `ToolBarMenuBorder`
- `ToolBarSubMenuBackground`
- `ToolBarButtonChecked`
- `ToolBarOpenHeaderBackground`
- `ToolBarIconVerticalBackground`
- `ToolBarVerticalBackground`
- `ToolBarIconBackground`
- `ToolBarHorizontalBackground`
- `ToolBarDisabledFill`
- `ToolBarDisabledBorder`
- `EnvironmentCommandBar`
- `EnvironmentCommandBarIcon`
- `EnvironmentCommandBarMenuMouseOverSubmenuGlyph`
- `EnvironmentCommandBarMenuSeparator`
- `EnvironmentCommandBarCheckBox`
- `EnvironmentCommandBarSelectedIcon`
- `EnvironmentCommandBarCheckBoxMouseOver`
- `EnvironmentCommandBarHoverOverSelectedIcon`
- `EnvironmentCommandBarMenuItemMouseOver`
- `CommonControlsButtonIconBackground`
- `CommonControlsButton`
- `CommonControlsButtonBorder`
- `CommonControlsButtonBorderDefault`
- `CommonControlsButtonBorderDisabled`
- `CommonControlsButtonBorderFocused`
- `CommonControlsButtonBorderHover`
- `CommonControlsButtonBorderPressed`
- `CommonControlsButtonDefault`
- `CommonControlsButtonDisabled`
- `CommonControlsButtonFocused`
- `CommonControlsButtonHover`
- `CommonControlsButtonPressed`
- `CommonControlsCheckBoxBackground`
- `CommonControlsCheckBoxBackgroundDisabled`
- `CommonControlsCheckBoxBackgroundFocused`
- `CommonControlsCheckBoxBackgroundHover`
- `CommonControlsCheckBoxBackgroundPressed`
- `CommonControlsCheckBoxBorder`
- `CommonControlsCheckBoxBorderDisabled`
- `CommonControlsCheckBoxBorderFocused`
- `CommonControlsCheckBoxBorderHover`
- `CommonControlsCheckBoxBorderPressed`
- `CommonControlsCheckBoxGlyph`
- `CommonControlsCheckBoxGlyphDisabled`
- `CommonControlsCheckBoxGlyphFocused`
- `CommonControlsCheckBoxGlyphHover`
- `CommonControlsCheckBoxGlyphPressed`
- `CommonControlsCheckBoxText`
- `CommonControlsCheckBoxTextDisabled`
- `CommonControlsCheckBoxTextFocused`
- `CommonControlsCheckBoxTextHover`
- `CommonControlsCheckBoxTextPressed`
- `CommonControlsComboBoxBackground`
- `CommonControlsComboBoxBackgroundDisabled`
- `CommonControlsComboBoxBackgroundFocused`
- `CommonControlsComboBoxBackgroundHover`
- `CommonControlsComboBoxBackgroundPressed`
- `CommonControlsComboBoxBorder`
- `CommonControlsComboBoxBorderDisabled`
- `CommonControlsComboBoxBorderFocused`
- `CommonControlsComboBoxBorderHover`
- `CommonControlsComboBoxBorderPressed`
- `CommonControlsComboBoxGlyph`
- `CommonControlsComboBoxGlyphBackground`
- `CommonControlsComboBoxGlyphBackgroundDisabled`
- `CommonControlsComboBoxGlyphBackgroundFocused`
- `CommonControlsComboBoxGlyphBackgroundHover`
- `CommonControlsComboBoxGlyphBackgroundPressed`
- `CommonControlsComboBoxGlyphDisabled`
- `CommonControlsComboBoxGlyphFocused`
- `CommonControlsComboBoxGlyphHover`
- `CommonControlsComboBoxGlyphPressed`
- `CommonControlsComboBoxListBackground`
- `CommonControlsComboBoxListBorder`
- `CommonControlsComboBoxListItemBackgroundHover`
- `CommonControlsComboBoxListItemBorderHover`
- `CommonControlsComboBoxListItemText`
- `CommonControlsComboBoxListItemTextHover`
- `CommonControlsComboBoxSeparator`
- `CommonControlsComboBoxSeparatorFocused`
- `CommonControlsComboBoxSeparatorHover`
- `CommonControlsComboBoxSeparatorPressed`
- `CommonControlsComboBoxText`
- `CommonControlsComboBoxTextDisabled`
- `CommonControlsComboBoxTextFocused`
- `CommonControlsComboBoxTextHover`
- `CommonControlsComboBoxTextInputSelection`
- `CommonControlsComboBoxTextPressed`
- `CommonControlsRadioButtonBackground`
- `CommonControlsRadioButtonBackgroundDisabled`
- `CommonControlsRadioButtonBackgroundFocused`
- `CommonControlsRadioButtonBackgroundHover`
- `CommonControlsRadioButtonBackgroundPressed`
- `CommonControlsRadioButtonBorder`
- `CommonControlsRadioButtonBorderDisabled`
- `CommonControlsRadioButtonBorderFocused`
- `CommonControlsRadioButtonBorderHover`
- `CommonControlsRadioButtonBorderPressed`
- `CommonControlsRadioButtonGlyph`
- `CommonControlsRadioButtonGlyphDisabled`
- `CommonControlsRadioButtonGlyphFocused`
- `CommonControlsRadioButtonGlyphHover`
- `CommonControlsRadioButtonGlyphPressed`
- `CommonControlsRadioButtonText`
- `CommonControlsRadioButtonTextDisabled`
- `CommonControlsRadioButtonTextFocused`
- `CommonControlsRadioButtonTextHover`
- `CommonControlsRadioButtonTextPressed`
- `CommonControlsTextBox`
- `CommonControlsTextBoxBorder`
- `CommonControlsTextBoxBorderDisabled`
- `CommonControlsTextBoxBorderError`
- `CommonControlsTextBoxBorderFocused`
- `CommonControlsTextBoxDisabled`
- `CommonControlsTextBoxError`
- `CommonControlsTextBoxFocused`
- `CommonControlsTextBoxMouseOverBorder`
- `CommonControlsTextBoxSelection`
- `CommonControlsFocusVisual`
- `TabItemForeground`
- `TabItemStaticBackground`
- `TabItemStaticBorder`
- `TabItemMouseOverBackground`
- `TabItemMouseOverBorder`
- `TabItemSelectedBackground`
- `TabItemSelectedBorder`
- `TabItemDisabledBackground`
- `TabItemDisabledBorder`
- `ListBoxBackground`
- `ListBoxBorder`
- `ListBoxItemMouseOverBackground`
- `ListBoxItemMouseOverBorder`
- `ListBoxItemSelectedInactiveBackground`
- `ListBoxItemSelectedInactiveBorder`
- `ListBoxItemSelectedActiveBackground`
- `ListBoxItemSelectedActiveBorder`
- `ContextMenuBackground`
- `ContextMenuBorderBrush`
- `ContextMenuRectangleFill`
- `ExpanderStaticCircleStroke`
- `ExpanderStaticCircleFill`
- `ExpanderStaticArrowStroke`
- `ExpanderMouseOverCircleStroke`
- `ExpanderMouseOverCircleFill`
- `ExpanderMouseOverArrowStroke`
- `ExpanderPressedCircleStroke`
- `ExpanderPressedCircleFill`
- `ExpanderPressedArrowStroke`
- `ExpanderDisabledCircleStroke`
- `ExpanderDisabledCircleFill`
- `ExpanderDisabledArrowStroke`
- `ProgressBarProgress`
- `ProgressBarBackground`
- `ProgressBarBorder`
- `ResizeGripperForeground`
- `EnvironmentScrollBarArrowBackground`
- `EnvironmentScrollBarArrowDisabledBackground`
- `EnvironmentScrollBarArrowGlyph`
- `EnvironmentScrollBarArrowGlyphDisabled`
- `EnvironmentScrollBarArrowGlyphMouseOver`
- `EnvironmentScrollBarArrowGlyphPressed`
- `EnvironmentScrollBarArrowMouseOverBackground`
- `EnvironmentScrollBarArrowPressedBackground`
- `EnvironmentScrollBarBackground`
- `EnvironmentScrollBarBorder`
- `EnvironmentScrollBarThumbBackground`
- `EnvironmentScrollBarThumbDisabled`
- `EnvironmentScrollBarThumbMouseOverBackground`
- `EnvironmentScrollBarThumbPressedBackground`
- `StatusBarDebugging`
- `ToolTipBackground`
- `ToolTipBorderBrush`
- `ToolTipForeground`
- `ScreenTip`
- `ScreenTipBorder`
- `CompletionToolTip`
- `CompletionToolTipBorder`
- `QuickInfo`
- `QuickInfoBorder`
- `SignatureHelp`
- `SignatureHelpBorder`
- `CilButton`
- `CilButtonBorder`
- `CilButtonBorderFocused`
- `CilButtonBorderHover`
- `CilButtonBorderPressed`
- `CilButtonError`
- `CilButtonErrorBorder`
- `CilButtonFocused`
- `CilButtonHover`
- `CilButtonPressed`
- `CilCheckBoxBackground`
- `CilCheckBoxBackgroundDisabled`
- `CilCheckBoxBackgroundFocused`
- `CilCheckBoxBackgroundHover`
- `CilCheckBoxBackgroundPressed`
- `CilCheckBoxBorder`
- `CilCheckBoxBorderDisabled`
- `CilCheckBoxBorderFocused`
- `CilCheckBoxBorderHover`
- `CilCheckBoxBorderPressed`
- `CilCheckBoxGlyph`
- `CilCheckBoxGlyphDisabled`
- `CilCheckBoxGlyphFocused`
- `CilCheckBoxGlyphHover`
- `CilCheckBoxGlyphPressed`
- `CilCheckBoxText`
- `CilCheckBoxTextDisabled`
- `CilCheckBoxTextFocused`
- `CilCheckBoxTextHover`
- `CilCheckBoxTextPressed`
- `CilComboBoxBorderFocused`
- `CilComboBoxBorderHover`
- `CilComboBoxBorderPressed`
- `CilComboBoxError`
- `CilComboBoxErrorBorder`
- `CilComboBoxListBackground`
- `CilComboBoxListBorder`
- `CilComboBoxListItemBackgroundHover`
- `CilComboBoxListItemBorderHover`
- `CilComboBoxListItemTextHover`
- `CilGridViewBorder`
- `CilGridViewItemContainerMouseOverHoverBorder`
- `CilGridViewItemContainerSelectedBorder`
- `CilGridViewItemContainerSelectedInactiveBorder`
- `CilGridViewItemContainerSelectedMouseOverBorder`
- `CilGridViewListItemHoverFill`
- `CilGridViewListItemSelectedFill`
- `CilGridViewListItemSelectedHoverFill`
- `CilGridViewListItemSelectedInactiveFill`
- `CilGridViewListViewItemFocusVisualStroke`
- `CilListBoxBorder`
- `CilListBoxItemMouseOverBackground`
- `CilListBoxItemMouseOverBorder`
- `CilListBoxItemSelectedActiveBackground`
- `CilListBoxItemSelectedActiveBorder`
- `CilListBoxItemSelectedInactiveBackground`
- `CilListBoxItemSelectedInactiveBorder`
- `CilListViewItem0`
- `CilListViewItem1`
- `CilTextBoxDisabled`
- `CilTextBoxDisabledBorder`
- `CilTextBoxError`
- `CilTextBoxErrorBorder`
- `CilTextBoxFocusedBorder`
- `CilTextBoxMouseOverBorder`
- `CilTextBoxSelection`
- `GridViewBackground`
- `GridViewBorder`
- `HeaderDefault`
- `HeaderGlyph`
- `HeaderMouseDown`
- `HeaderMouseOver`
- `HeaderMouseOverGlyph`
- `HeaderSeparatorLine`
- `GridViewListViewForeground`
- `GridViewItemContainerMouseOverHoverBorder`
- `GridViewItemContainerSelectedBorder`
- `GridViewItemContainerSelectedInactiveBorder`
- `GridViewItemContainerSelectedMouseOverBorder`
- `GridViewListItemHoverFill`
- `GridViewListItemSelectedFill`
- `GridViewListItemSelectedHoverFill`
- `GridViewListItemSelectedInactiveFill`
- `GridViewListViewItemFocusVisualStroke`
- `DecompilerTextViewWaitAdorner`
- `ListArrowBackground`
- `TreeViewItemMouseOver`
- `TreeViewItemSelected`
- `TreeView`
- `TreeViewBorder`
- `TreeViewGlyph`
- `TreeViewGlyphMouseOver`
- `TVItemAlternationBackground`
- `AppSettingsTreeView`
- `AppSettingsTreeViewBorder`
- `EnvironmentFileTabBackground`
- `EnvironmentFileTabBorder`
- `EnvironmentFileTabButtonDownInactiveBorder`
- `EnvironmentFileTabButtonDownInactive`
- `EnvironmentFileTabButtonDownInactiveGlyph`
- `EnvironmentFileTabButtonDownSelectedActiveBorder`
- `EnvironmentFileTabButtonDownSelectedActive`
- `EnvironmentFileTabButtonDownSelectedActiveGlyph`
- `EnvironmentFileTabButtonDownSelectedInactiveBorder`
- `EnvironmentFileTabButtonDownSelectedInactive`
- `EnvironmentFileTabButtonDownSelectedInactiveGlyph`
- `EnvironmentFileTabButtonHoverInactiveBorder`
- `EnvironmentFileTabButtonHoverInactive`
- `EnvironmentFileTabButtonHoverInactiveGlyph`
- `EnvironmentFileTabButtonHoverSelectedActiveBorder`
- `EnvironmentFileTabButtonHoverSelectedActive`
- `EnvironmentFileTabButtonHoverSelectedActiveGlyph`
- `EnvironmentFileTabButtonHoverSelectedInactiveBorder`
- `EnvironmentFileTabButtonHoverSelectedInactive`
- `EnvironmentFileTabButtonHoverSelectedInactiveGlyph`
- `EnvironmentFileTabButtonSelectedActiveGlyph`
- `EnvironmentFileTabButtonSelectedInactiveGlyph`
- `EnvironmentFileTabInactiveBorder`
- `EnvironmentFileTabInactiveGradient`
- `EnvironmentFileTabInactiveText`
- `EnvironmentFileTabSelectedBorder`
- `EnvironmentFileTabSelectedGradient`
- `EnvironmentFileTabSelectedText`
- `EnvironmentFileTabText`
- `EnvironmentFileTabHotGradient`
- `EnvironmentFileTabHotBorder`
- `EnvironmentFileTabHotText`
- `EnvironmentFileTabHotGlyph`
- `EnvironmentTitleBarActive`
- `EnvironmentTitleBarActiveBorder`
- `EnvironmentTitleBarActiveGradient`
- `EnvironmentTitleBarDragHandle`
- `EnvironmentTitleBarDragHandleActive`
- `EnvironmentTitleBarInactive`
- `EnvironmentTitleBarInactiveBorder`
- `EnvironmentTitleBarInactiveGradient`
- `EnvironmentToolWindow`
- `EnvironmentToolWindowBorder`
- `EnvironmentToolWindowButtonActiveGlyph`
- `EnvironmentToolWindowButtonDown`
- `EnvironmentToolWindowButtonDownActiveGlyph`
- `EnvironmentToolWindowButtonDownBorder`
- `EnvironmentToolWindowButtonHoverActive`
- `EnvironmentToolWindowButtonHoverActiveBorder`
- `EnvironmentToolWindowButtonHoverActiveGlyph`
- `EnvironmentToolWindowButtonHoverInactive`
- `EnvironmentToolWindowButtonHoverInactiveBorder`
- `EnvironmentToolWindowButtonHoverInactiveGlyph`
- `EnvironmentToolWindowButtonInactiveGlyph`
- `EnvironmentToolWindowTabBorder`
- `EnvironmentToolWindowTabGradient`
- `EnvironmentToolWindowTabMouseOverBackgroundGradient`
- `EnvironmentToolWindowTabMouseOverBorder`
- `EnvironmentToolWindowTabMouseOverText`
- `EnvironmentToolWindowTabSelectedActiveText`
- `EnvironmentToolWindowTabSelectedBorder`
- `EnvironmentToolWindowTabSelectedTab`
- `EnvironmentToolWindowTabSelectedText`
- `EnvironmentToolWindowTabText`
- `SearchBoxWatermark`
- `MemoryWindowDisabled`
- `TreeViewNode`
- `EnvironmentDropDownGlyph`
- `EnvironmentDropDownMouseOverGlyph`
- `EnvironmentDropDownMouseDownGlyph`
- `EnvironmentCommandBarMouseOverBackground`
- `EnvironmentCommandBarMouseDownBackground`
- `EnvironmentComboBoxDisabledBackground`
- `EnvironmentIconGeneralStroke`
- `EnvironmentIconGeneralFill`
- `EnvironmentIconActionFill`
- `SearchControlMouseOverDropDownButtonGlyph`
- `HexSearchControlMouseOverDropDownButtonGlyph`
- `HexSearchingTextBox`
- `HexSearchingTextBoxBorder`
- `EnvironmentCommandBarToolBarSeparator`
- `EnvironmentCommandBarToolBarSeparatorHighlight`
- `DebuggerBreakpointGlyphMarginControlBorder`
- `DebuggerBreakpointGlyphMarginControlBackground`
- `DebuggerBreakpointGlyphMarginControlHoverBackground`
- `HyperlinkNormal`
- `HyperlinkMouseOver`
- `HyperlinkDisabled`
- `LastUI`

## Class `ExtensionMethods`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Themes.ExtensionMethods members directly without instantiation.
dnSpy.Contracts.Themes.ExtensionMethods./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Themes/ExtensionMethods.cs` (line 26)

### Methods

- `public static ColorType ToColorType(this TextColor self)`
  - Summary: Converts the color to a
  - Parameters:
    - `this TextColor self`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ExtensionMethods.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Themes.ExtensionMethods.ToColorType(self: /* TextColor */);
    ```

## Interface `ITheme`

A theme

**Example**

```csharp
// Instantiate dnSpy.Contracts.Themes.ITheme and call its members.
var instance = new dnSpy.Contracts.Themes.ITheme(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 26)

### Methods

- `IThemeColor GetColor(ColorType colorType)`
  - Summary: Gets the inherited color
  - Parameters:
    - `ColorType colorType`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColor(colorType: /* ColorType */);
    ```
- `IThemeColor GetExplicitColor(ColorType colorType)`
  - Summary: Gets the color that was defined in the theme file. Inherited colors aren't included.
  - Parameters:
    - `ColorType colorType`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.GetExplicitColor(colorType: /* ColorType */);
    ```
- `IThemeColor GetTextColor(ColorType colorType)`
  - Summary: Gets the inherited color that can be used by a text editor (default colors are null)
  - Parameters:
    - `ColorType colorType`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTextColor(colorType: /* ColorType */);
    ```

### Properties

- `Guid Guid { get; }`
  - Summary: Guid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `bool IsDark { get; }`
  - Summary: true if it's a dark colored theme
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDark;
    ```
- `bool IsHighContrast { get; }`
  - Summary: true if this is a high-contrast theme
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsHighContrast;
    ```
- `bool IsLight { get; }`
  - Summary: true if it's a light colored theme
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsLight;
    ```
- `double Order { get; }`
  - Summary: Theme order. Can be used by a UI class to sort the themes before showing them to the user
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string MenuName { get; }`
  - Summary: Name of theme that can be used in a MenuItem
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MenuName;
    ```
- `string Name { get; }`
  - Summary: Name or an empty string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ITheme.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `IThemeColor`

Theme color

**Example**

```csharp
// Instantiate dnSpy.Contracts.Themes.IThemeColor and call its members.
var instance = new dnSpy.Contracts.Themes.IThemeColor(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeColor.cs` (line 27)

### Properties

- `Brush Background { get; }`
  - Summary: Background (second) color null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeColor.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Background;
    ```
- `Brush Color3 { get; }`
  - Summary: Third color or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeColor.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Color3;
    ```
- `Brush Color4 { get; }`
  - Summary: Fourth color or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeColor.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Color4;
    ```
- `Brush Foreground { get; }`
  - Summary: Foreground (first) color or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeColor.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Foreground;
    ```
- `FontStyle? FontStyle { get; }`
  - Summary: Font style or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeColor.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontStyle;
    ```
- `FontWeight? FontWeight { get; }`
  - Summary: Font weight or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeColor.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FontWeight;
    ```
- `string Name { get; }`
  - Summary: Name of color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeColor.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `IThemeService`

Manages all s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Themes.IThemeService and call its members.
var instance = new dnSpy.Contracts.Themes.IThemeService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeService.cs` (line 26)

### Properties

- `ITheme Theme { get; }`
  - Summary: Gets the current theme
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeService.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Theme;
    ```

### Events

- `event EventHandler<ThemeChangedEventArgs> ThemeChanged`
  - Summary: Raised when gets changed and is notified after and before
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeService.cs` (line 42)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ThemeChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<ThemeChangedEventArgs> ThemeChangedHighPriority`
  - Summary: Raised when gets changed, and is raised before and
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeService.cs` (line 36)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ThemeChangedHighPriority += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<ThemeChangedEventArgs> ThemeChangedLowPriority`
  - Summary: Raised when gets changed and is notified after and
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/IThemeService.cs` (line 48)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ThemeChangedLowPriority += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `ThemeChangedEventArgs`

Theme changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Themes.ThemeChangedEventArgs and call its members.
var instance = new dnSpy.Contracts.Themes.ThemeChangedEventArgs(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Themes/ThemeChangedEventArgs.cs` (line 26)

## Class `ThemeConstants`

Constants

**Example**

```csharp
// Access dnSpy.Contracts.Themes.ThemeConstants members directly without instantiation.
dnSpy.Contracts.Themes.ThemeConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Themes/ThemeConstants.cs` (line 26)

### Fields

- `public static readonly Guid THEME_BLUE_GUID = new Guid("61AA341E-281D-4154-985F-C81E9269034B")`
  - Summary: Blue theme guid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ThemeConstants.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Themes.ThemeConstants.THEME_BLUE_GUID;
    ```
- `public static readonly Guid THEME_DARK_GUID = new Guid("64EFBB2C-0ACA-467C-8389-9FA350376F3F")`
  - Summary: Dark theme guid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ThemeConstants.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Themes.ThemeConstants.THEME_DARK_GUID;
    ```
- `public static readonly Guid THEME_HIGHCONTRAST_GUID = new Guid("D0EA082A-BF0D-439F-B396-547C29D97E37")`
  - Summary: High contrast theme guid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ThemeConstants.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Themes.ThemeConstants.THEME_HIGHCONTRAST_GUID;
    ```
- `public static readonly Guid THEME_LIGHT_GUID = new Guid("B3D71E74-C353-4206-9AD1-05847BE95CBE")`
  - Summary: Light theme guid
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Themes/ThemeConstants.cs` (line 45)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Themes.ThemeConstants.THEME_LIGHT_GUID;
    ```

