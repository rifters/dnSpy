# Namespace `dnSpy.Contracts.Hex.Operations`

## Enum `HexCopySpecialKind`

Passed to

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Operations.HexCopySpecialKind and call its members.
var instance = new dnSpy.Contracts.Hex.Operations.HexCopySpecialKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 395)

### Members

- `Utf8String`: UTF-8 string
- `UnicodeString`: Unicode string
- `CSharpArray`: C# array
- `VisualBasicArray`: Visual Basic array
- `Offset`: Offset
- `Value`: Value at caret
- `UInt16`: (little endian) at caret
- `UInt16BigEndian`: (big endian) at caret
- `UInt32`: (little endian) at caret
- `UInt32BigEndian`: (big endian) at caret
- `UInt64`: (little endian) at caret
- `UInt64BigEndian`: (big endian) at caret
- `FileOffset`: File offset. If it's a PE file, the position is converted to a position within the PE file on disk. If it's not a PE file, it's the offset relative to the start of the file.
- `AbsoluteFileOffset`: Current position
- `RVA`: RVA

## Class `HexEditorOperations`

Hex editor operations

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Operations.HexEditorOperations();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 28)

### Constructors

- `protected HexEditorOperations()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 32)

### Methods

- `public abstract bool ClearData()`
  - Summary: Clears data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 332)
  - Example:
    ```csharp
    // Example invocation
    instance.ClearData();
    ```
- `public abstract bool CopySelectionBytes()`
  - Summary: Copy selection, bytes (as text)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 235)
  - Example:
    ```csharp
    // Example invocation
    instance.CopySelectionBytes();
    ```
- `public abstract bool CopySelectionText()`
  - Summary: Copy selection, UI text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 241)
  - Example:
    ```csharp
    // Example invocation
    instance.CopySelectionText();
    ```
- `public abstract bool CopySpecial(HexCopySpecialKind copyKind)`
  - Summary: Copies text to the clipboard
  - Parameters:
    - `HexCopySpecialKind copyKind`: What kind of data to copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 248)
  - Example:
    ```csharp
    // Example invocation
    instance.CopySpecial(copyKind: /* HexCopySpecialKind */);
    ```
- `public abstract bool InsertText(string text)`
  - Summary: Inserts text
  - Parameters:
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 183)
  - Example:
    ```csharp
    // Example invocation
    instance.InsertText(text: /* string */);
    ```
- `public abstract bool Paste()`
  - Summary: Paste
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 254)
  - Example:
    ```csharp
    // Example invocation
    instance.Paste();
    ```
- `public abstract bool PasteSpecial(HexPasteSpecialKind pasteKind)`
  - Summary: Pastes data from the clipboard
  - Parameters:
    - `HexPasteSpecialKind pasteKind`: What kind of data to paste
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 261)
  - Example:
    ```csharp
    // Example invocation
    instance.PasteSpecial(pasteKind: /* HexPasteSpecialKind */);
    ```
- `public abstract void ExtendSelection(HexBufferPoint newEnd)`
  - Summary: Extend selection
  - Parameters:
    - `HexBufferPoint newEnd`: New end position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 206)
  - Example:
    ```csharp
    // Example invocation
    instance.ExtendSelection(newEnd: /* HexBufferPoint */);
    ```
- `public abstract void FollowFieldValueReference()`
  - Summary: Follows the field reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 374)
  - Example:
    ```csharp
    // Example invocation
    instance.FollowFieldValueReference();
    ```
- `public abstract void GoToCodeOrStructure()`
  - Summary: Go to high-level code (eg. decompiled code) or other high level structure
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 369)
  - Example:
    ```csharp
    // Example invocation
    instance.GoToCodeOrStructure();
    ```
- `public abstract void MoveCaret(HexViewLine hexLine, double horizontalOffset, bool extendSelection, HexMoveToFlags flags)`
  - Summary: Move caret to a line
  - Parameters:
    - `HexViewLine hexLine`: Line
    - `double horizontalOffset`: Horizontal offset
    - `bool extendSelection`: true to extend the selection
    - `HexMoveToFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 224)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveCaret(hexLine: /* HexViewLine */, horizontalOffset: /* double */, extendSelection: /* bool */, flags: /* HexMoveToFlags */);
    ```
- `public abstract void MoveCurrentLineToBottom()`
  - Summary: Move current line to bottom of the view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 159)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveCurrentLineToBottom();
    ```
- `public abstract void MoveCurrentLineToTop()`
  - Summary: Move current line to top of the view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 154)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveCurrentLineToTop();
    ```
- `public abstract void MoveLineDown(bool extendSelection)`
  - Summary: Move down a line
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveLineDown(extendSelection: /* bool */);
    ```
- `public abstract void MoveLineUp(bool extendSelection)`
  - Summary: Move up a line
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 107)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveLineUp(extendSelection: /* bool */);
    ```
- `public abstract void MoveToBottomOfView(bool extendSelection)`
  - Summary: Move the caret to the bottom of the view
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 171)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToBottomOfView(extendSelection: /* bool */);
    ```
- `public abstract void MoveToEndOfDocument(bool extendSelection)`
  - Summary: Move to end of document
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 149)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToEndOfDocument(extendSelection: /* bool */);
    ```
- `public abstract void MoveToEndOfLine(bool extendSelection)`
  - Summary: Move to the end of the line
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 131)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToEndOfLine(extendSelection: /* bool */);
    ```
- `public abstract void MoveToNextCharacter(bool extendSelection)`
  - Summary: Moves the caret to the next character
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToNextCharacter(extendSelection: /* bool */);
    ```
- `public abstract void MoveToNextValidStartEnd(bool extendSelection)`
  - Summary: Move to the next closest start/end position of a block of memory
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 358)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToNextValidStartEnd(extendSelection: /* bool */);
    ```
- `public abstract void MoveToNextWord(bool extendSelection)`
  - Summary: Moves the caret to the next word (cell)
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToNextWord(extendSelection: /* bool */);
    ```
- `public abstract void MoveToPreviousCharacter(bool extendSelection)`
  - Summary: Moves the caret to the previous character
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToPreviousCharacter(extendSelection: /* bool */);
    ```
- `public abstract void MoveToPreviousValidStartEnd(bool extendSelection)`
  - Summary: Move to the previous closest start/end position of a block of memory
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 364)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToPreviousValidStartEnd(extendSelection: /* bool */);
    ```
- `public abstract void MoveToPreviousWord(bool extendSelection)`
  - Summary: Moves the caret to the previous word (cell)
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToPreviousWord(extendSelection: /* bool */);
    ```
- `public abstract void MoveToStartOfDocument(bool extendSelection)`
  - Summary: Move to start of document
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToStartOfDocument(extendSelection: /* bool */);
    ```
- `public abstract void MoveToStartOfLine(bool extendSelection)`
  - Summary: Move to the start of the line
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 137)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToStartOfLine(extendSelection: /* bool */);
    ```
- `public abstract void MoveToTopOfView(bool extendSelection)`
  - Summary: Move the caret to the top of the view
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 165)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToTopOfView(extendSelection: /* bool */);
    ```
- `public abstract void PageDown(bool extendSelection)`
  - Summary: Page down
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.PageDown(extendSelection: /* bool */);
    ```
- `public abstract void PageUp(bool extendSelection)`
  - Summary: Page up
  - Parameters:
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 119)
  - Example:
    ```csharp
    // Example invocation
    instance.PageUp(extendSelection: /* bool */);
    ```
- `public abstract void Refresh()`
  - Summary: Refreshes the screen and clears any read caches
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 347)
  - Example:
    ```csharp
    // Example invocation
    instance.Refresh();
    ```
- `public abstract void ResetSelection()`
  - Summary: Reset selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 229)
  - Example:
    ```csharp
    // Example invocation
    instance.ResetSelection();
    ```
- `public abstract void ScrollColumnLeft()`
  - Summary: Scoll one column left
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 286)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollColumnLeft();
    ```
- `public abstract void ScrollColumnRight()`
  - Summary: Scoll one column right
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 291)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollColumnRight();
    ```
- `public abstract void ScrollDownAndMoveCaretIfNecessary()`
  - Summary: Scroll down and move caret so it's within the viewport
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 271)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollDownAndMoveCaretIfNecessary();
    ```
- `public abstract void ScrollLineBottom()`
  - Summary: Move current line to the bottom of the view, don't move the caret
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 296)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollLineBottom();
    ```
- `public abstract void ScrollLineCenter()`
  - Summary: Move current line to the center of the view, don't move the caret
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 306)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollLineCenter();
    ```
- `public abstract void ScrollLineTop()`
  - Summary: Move current line to the top of the view, don't move the caret
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 301)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollLineTop();
    ```
- `public abstract void ScrollPageDown()`
  - Summary: Page down, but don't move caret
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 281)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollPageDown();
    ```
- `public abstract void ScrollPageUp()`
  - Summary: Page up, but don't move caret
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 276)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollPageUp();
    ```
- `public abstract void ScrollUpAndMoveCaretIfNecessary()`
  - Summary: Scroll up and move caret so it's within the viewport
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 266)
  - Example:
    ```csharp
    // Example invocation
    instance.ScrollUpAndMoveCaretIfNecessary();
    ```
- `public abstract void SelectAll()`
  - Summary: Select all
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 200)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectAll();
    ```
- `public abstract void SelectAllBytesBlock()`
  - Summary: Selects all bytes in the current block, unless the caret is in a memory hole
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 352)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectAllBytesBlock();
    ```
- `public abstract void SelectAndMoveCaret(HexColumnType column, HexBufferPoint anchorPoint, HexBufferPoint activePoint, bool alignPoints, VSTE.EnsureSpanVisibleOptions? scrollOptions)`
  - Summary: Selects data and moves the caret
  - Parameters:
    - `HexColumnType column`: Column
    - `HexBufferPoint anchorPoint`: Anchor position
    - `HexBufferPoint activePoint`: Active position
    - `bool alignPoints`: true to align the span to include all bytes of the cells
    - `VSTE.EnsureSpanVisibleOptions? scrollOptions`: Scroll options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectAndMoveCaret(column: /* HexColumnType */, anchorPoint: /* HexBufferPoint */, activePoint: /* HexBufferPoint */, alignPoints: /* bool */, scrollOptions: /* VSTE.EnsureSpanVisibleOptions? */);
    ```
- `public abstract void SelectCurrentWord()`
  - Summary: Selects the current word (cell)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 195)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectCurrentWord();
    ```
- `public abstract void SelectFile()`
  - Summary: Select the non-nested file at current position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 384)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectFile();
    ```
- `public abstract void SelectLine(HexViewLine viewLine, bool extendSelection)`
  - Summary: Selects the line
  - Parameters:
    - `HexViewLine viewLine`: Line
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 190)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectLine(viewLine: /* HexViewLine */, extendSelection: /* bool */);
    ```
- `public abstract void SelectNestedFile()`
  - Summary: Select the most nested file at current position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 379)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectNestedFile();
    ```
- `public abstract void SelectStructure()`
  - Summary: Selects the current structure
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 389)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectStructure();
    ```
- `public abstract void ShowAllBytes()`
  - Summary: Shows all bytes ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 337)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowAllBytes();
    ```
- `public abstract void ShowOnlySelectedBytes()`
  - Summary: Shows only the selected bytes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 342)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowOnlySelectedBytes();
    ```
- `public abstract void SwapCaretAndAnchor()`
  - Summary: Swap selection caret and anchor positions
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 176)
  - Example:
    ```csharp
    // Example invocation
    instance.SwapCaretAndAnchor();
    ```
- `public abstract void ToggleColumn()`
  - Summary: Toggles active column
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 327)
  - Example:
    ```csharp
    // Example invocation
    instance.ToggleColumn();
    ```
- `public abstract void ZoomIn()`
  - Summary: Zoom in
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 311)
  - Example:
    ```csharp
    // Example invocation
    instance.ZoomIn();
    ```
- `public abstract void ZoomOut()`
  - Summary: Zoom out
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 316)
  - Example:
    ```csharp
    // Example invocation
    instance.ZoomOut();
    ```
- `public abstract void ZoomTo(double zoomLevel)`
  - Summary: Zoom to
  - Parameters:
    - `double zoomLevel`: Zoom level, between 20% and 400% (20.0 and 400.0)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 322)
  - Example:
    ```csharp
    // Example invocation
    instance.ZoomTo(zoomLevel: /* double */);
    ```
- `public void MoveCaret(HexViewLine hexLine, double horizontalOffset, bool extendSelection)`
  - Summary: Move caret to a line
  - Parameters:
    - `HexViewLine hexLine`: Line
    - `double horizontalOffset`: Horizontal offset
    - `bool extendSelection`: true to extend the selection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 214)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveCaret(hexLine: /* HexViewLine */, horizontalOffset: /* double */, extendSelection: /* bool */);
    ```
- `public void SelectAndMoveCaret(HexColumnType column, HexBufferPoint anchorPoint, HexBufferPoint activePoint, bool alignPoints)`
  - Summary: Selects data and moves the caret
  - Parameters:
    - `HexColumnType column`: Column
    - `HexBufferPoint anchorPoint`: Anchor position
    - `HexBufferPoint activePoint`: Active position
    - `bool alignPoints`: true to align the span to include all bytes of the cells
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectAndMoveCaret(column: /* HexColumnType */, anchorPoint: /* HexBufferPoint */, activePoint: /* HexBufferPoint */, alignPoints: /* bool */);
    ```

### Properties

- `public VSTE.IEditorOptions Options => HexView.Options`
  - Summary: Gets the editor options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```
- `public abstract HexBufferSpan? ProvisionalCompositionSpan { get; set; }`
  - Summary: Gets/sets the provisional composition span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProvisionalCompositionSpan;
    ```
- `public abstract HexView HexView { get; }`
  - Summary: Gets the hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexView;
    ```
- `public abstract bool CanCopy { get; }`
  - Summary: true if it's possible to copy text to the clipboard
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanCopy;
    ```
- `public abstract bool CanPaste { get; }`
  - Summary: true if it's possible to paste data from the clipboard
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanPaste;
    ```

## Class `HexEditorOperationsFactoryService`

Creates instances

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Operations.HexEditorOperationsFactoryService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperationsFactoryService.cs` (line 26)

### Constructors

- `protected HexEditorOperationsFactoryService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperationsFactoryService.cs` (line 30)

### Methods

- `public abstract HexEditorOperations GetEditorOperations(HexView hexView)`
  - Summary: Gets the hex view's instance
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperationsFactoryService.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEditorOperations(hexView: /* HexView */);
    ```

## Enum `HexFindOptions`

Find options used by

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Operations.HexFindOptions and call its members.
var instance = new dnSpy.Contracts.Hex.Operations.HexFindOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexFindOptions.cs` (line 26)

### Members

- `None`: No options have been set
- `SearchReverse` = `x00000001`: Search in reverse direction
- `Wrap` = `x00000002`: Wrap around
- `NoOverlaps` = `x00000004`: Don't return spans that overlap a previous result. Useful by Replace All code.

## Enum `HexPasteSpecialKind`

Passed to

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Operations.HexPasteSpecialKind and call its members.
var instance = new dnSpy.Contracts.Hex.Operations.HexPasteSpecialKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexEditorOperations.cs` (line 477)

### Members

- `Utf8String`: UTF-8 string
- `Utf8String7BitEncodedLengthPrefix`: 7-bit encoded length followed by UTF-8 bytes
- `UnicodeString`: Unicode (UTF-16) string
- `UnicodeString7BitEncodedLengthPrefix`: 7-bit encoded length followed by Unicode (UTF-16) bytes
- `Blob`: Metadata blob

## Class `HexSearchService`

Search service

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Operations.HexSearchService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchService.cs` (line 28)

### Constructors

- `protected HexSearchService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchService.cs` (line 32)

### Methods

- `public HexBufferSpan? Find(HexBufferPoint startingPosition, HexFindOptions options, CancellationToken cancellationToken)`
  - Summary: Finds the pattern
  - Parameters:
    - `HexBufferPoint startingPosition`: Starting position
    - `HexFindOptions options`: Options
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchService.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.Find(startingPosition: /* HexBufferPoint */, options: /* HexFindOptions */, cancellationToken: /* CancellationToken */);
    ```
- `public HexBufferSpan? Find(HexBufferSpan searchRange, HexBufferPoint startingPosition, HexFindOptions options, CancellationToken cancellationToken)`
  - Summary: Finds the pattern
  - Parameters:
    - `HexBufferSpan searchRange`: Search range
    - `HexBufferPoint startingPosition`: Starting position
    - `HexFindOptions options`: Options
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchService.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.Find(searchRange: /* HexBufferSpan */, startingPosition: /* HexBufferPoint */, options: /* HexFindOptions */, cancellationToken: /* CancellationToken */);
    ```
- `public IEnumerable<HexBufferSpan> FindAll(HexBufferSpan searchRange, HexFindOptions options, CancellationToken cancellationToken)`
  - Summary: Finds all matches
  - Parameters:
    - `HexBufferSpan searchRange`: Search range
    - `HexFindOptions options`: Options
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchService.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.FindAll(searchRange: /* HexBufferSpan */, options: /* HexFindOptions */, cancellationToken: /* CancellationToken */);
    ```
- `public abstract IEnumerable<HexBufferSpan> FindAll(HexBufferSpan searchRange, HexBufferPoint startingPosition, HexFindOptions options, CancellationToken cancellationToken)`
  - Summary: Finds all matches
  - Parameters:
    - `HexBufferSpan searchRange`: Search range
    - `HexBufferPoint startingPosition`: Starting position
    - `HexFindOptions options`: Options
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchService.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.FindAll(searchRange: /* HexBufferSpan */, startingPosition: /* HexBufferPoint */, options: /* HexFindOptions */, cancellationToken: /* CancellationToken */);
    ```

### Properties

- `public abstract int ByteCount { get; }`
  - Summary: Gets the size of the data this instance searches for
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchService.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ByteCount;
    ```

## Class `HexSearchServiceProvider`

Creates instances that can search for bytes or strings

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Operations.HexSearchServiceProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 26)

### Constructors

- `protected HexSearchServiceProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 30)

### Methods

- `public HexSearchService CreateByteSearchService(byte value)`
  - Summary: Creates a that can search for values
  - Parameters:
    - `byte value`: Value to search for
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(value: /* byte */);
    ```
- `public HexSearchService CreateByteSearchService(byte[] pattern)`
  - Summary: Creates a that can search for bytes
  - Parameters:
    - `byte[] pattern`: Bytes to search for
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 213)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(pattern: /* byte[] */);
    ```
- `public HexSearchService CreateByteSearchService(double value, bool isBigEndian = false)`
  - Summary: Creates a that can search for values
  - Parameters:
    - `double value`: Value to search for
    - `bool isBigEndian` (default: `false`): true if big-endian, false if little-endian
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(value: /* double */, isBigEndian: /* bool */);
    ```
- `public HexSearchService CreateByteSearchService(float value, bool isBigEndian = false)`
  - Summary: Creates a that can search for values
  - Parameters:
    - `float value`: Value to search for
    - `bool isBigEndian` (default: `false`): true if big-endian, false if little-endian
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(value: /* float */, isBigEndian: /* bool */);
    ```
- `public HexSearchService CreateByteSearchService(int value, bool isBigEndian = false)`
  - Summary: Creates a that can search for values
  - Parameters:
    - `int value`: Value to search for
    - `bool isBigEndian` (default: `false`): true if big-endian, false if little-endian
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(value: /* int */, isBigEndian: /* bool */);
    ```
- `public HexSearchService CreateByteSearchService(long value, bool isBigEndian = false)`
  - Summary: Creates a that can search for values
  - Parameters:
    - `long value`: Value to search for
    - `bool isBigEndian` (default: `false`): true if big-endian, false if little-endian
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(value: /* long */, isBigEndian: /* bool */);
    ```
- `public HexSearchService CreateByteSearchService(sbyte value)`
  - Summary: Creates a that can search for values
  - Parameters:
    - `sbyte value`: Value to search for
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(value: /* sbyte */);
    ```
- `public HexSearchService CreateByteSearchService(short value, bool isBigEndian = false)`
  - Summary: Creates a that can search for values
  - Parameters:
    - `short value`: Value to search for
    - `bool isBigEndian` (default: `false`): true if big-endian, false if little-endian
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(value: /* short */, isBigEndian: /* bool */);
    ```
- `public HexSearchService CreateByteSearchService(string pattern)`
  - Summary: Creates a that can search for bytes. The wildcard character ? matches any nibble (upper or lower 4 bits) in a byte. Use to validate the input before calling this method.
  - Parameters:
    - `string pattern`: Pattern. Supported characters: whitespace, hex digits and the wildcard character '?'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(pattern: /* string */);
    ```
- `public HexSearchService CreateByteSearchService(uint value, bool isBigEndian = false)`
  - Summary: Creates a that can search for values
  - Parameters:
    - `uint value`: Value to search for
    - `bool isBigEndian` (default: `false`): true if big-endian, false if little-endian
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(value: /* uint */, isBigEndian: /* bool */);
    ```
- `public HexSearchService CreateByteSearchService(ulong value, bool isBigEndian = false)`
  - Summary: Creates a that can search for values
  - Parameters:
    - `ulong value`: Value to search for
    - `bool isBigEndian` (default: `false`): true if big-endian, false if little-endian
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(value: /* ulong */, isBigEndian: /* bool */);
    ```
- `public HexSearchService CreateByteSearchService(ushort value, bool isBigEndian = false)`
  - Summary: Creates a that can search for values
  - Parameters:
    - `ushort value`: Value to search for
    - `bool isBigEndian` (default: `false`): true if big-endian, false if little-endian
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(value: /* ushort */, isBigEndian: /* bool */);
    ```
- `public abstract HexSearchService CreateByteSearchService(byte[] pattern, byte[] mask)`
  - Summary: Creates a that can search for bytes
  - Parameters:
    - `byte[] pattern`: Bytes to search for
    - `byte[] mask`: Mask used when comparing values. This array must have the same length as
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 228)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateByteSearchService(pattern: /* byte[] */, mask: /* byte[] */);
    ```
- `public abstract HexSearchService CreateUtf16StringSearchService(string pattern, bool isCaseSensitive, bool isBigEndian = false)`
  - Summary: Creates a that can search for UTF-16 strings
  - Parameters:
    - `string pattern`: Pattern to search for
    - `bool isCaseSensitive`: true if it's case sensitive, false if it's case insensitive
    - `bool isBigEndian` (default: `false`): true if big-endian, false if little-endian
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 245)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateUtf16StringSearchService(pattern: /* string */, isCaseSensitive: /* bool */, isBigEndian: /* bool */);
    ```
- `public abstract HexSearchService CreateUtf8StringSearchService(string pattern, bool isCaseSensitive)`
  - Summary: Creates a that can search for UTF-8 strings
  - Parameters:
    - `string pattern`: Pattern to search for
    - `bool isCaseSensitive`: true if it's case sensitive, false if it's case insensitive
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 236)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateUtf8StringSearchService(pattern: /* string */, isCaseSensitive: /* bool */);
    ```
- `public bool IsValidByteSearchString(string pattern)`
  - Summary: Checks whether only contains valid characters and at least one valid character
  - Parameters:
    - `string pattern`: Pattern
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Operations/HexSearchServiceProvider.cs` (line 202)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValidByteSearchString(pattern: /* string */);
    ```

