# Namespace `dnSpy.Contracts.Command`

## Enum `BookmarkIds`

Bookmark IDs

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.BookmarkIds and call its members.
var instance = new dnSpy.Contracts.Command.BookmarkIds(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/BookmarkIds.cs` (line 24)

### Members

- `ShowBookmarkWindow`: Shows bookmarks window
- `ClearAllBookmarksInDocument`: Removes all bookmarks in the document
- `ClearBookmarks`: Removes all bookmarks
- `EnableAllBookmarks`: Enables or disables all bookmarks
- `EnableBookmark`: Enables or disables a bookmark
- `ToggleBookmark`: Toggles (adds or removes) a bookmark
- `NextBookmark`: Goes to the next bookmark
- `PreviousBookmark`: Goes to the previous bookmark
- `NextBookmarkInDocument`: Goes to the next bookmark in the document
- `PreviousBookmarkInDocument`: Goes to the previous bookmark in the document
- `NextBookmarkWithSameLabel`: Goes to the next bookmark with the same label
- `PreviousBookmarkWithSameLabel`: Goes to the previous bookmark with the same label

## Class `CommandConstants`

Command constants

**Example**

```csharp
// Access dnSpy.Contracts.Command.CommandConstants members directly without instantiation.
dnSpy.Contracts.Command.CommandConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandConstants.cs` (line 26)

### Fields

- `public static readonly Guid BookmarkGroup = new Guid("BF33ED4E-B503-4D95-995D-F5C5A4541923")`
  - Summary: Bookmark command IDs ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandConstants.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandConstants.BookmarkGroup;
    ```
- `public static readonly Guid HexEditorGroup = new Guid("3C6A823B-CF80-4D19-914E-498F773DEC7E")`
  - Summary: Hex editor command IDs ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandConstants.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandConstants.HexEditorGroup;
    ```
- `public static readonly Guid OutputTextPaneGroup = new Guid("091D1F2F-175A-4BD9-A0F3-C5F052D22D75")`
  - Summary: Output logger text pane command IDs ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandConstants.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandConstants.OutputTextPaneGroup;
    ```
- `public static readonly Guid ReplGroup = new Guid("8DBB0C94-6B10-4AC3-A715-CC4D478F7B67")`
  - Summary: REPL command IDs ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandConstants.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandConstants.ReplGroup;
    ```
- `public static readonly Guid StandardGroup = new Guid("14608CB3-3965-49B2-A8A9-46CDBB4E2E30")`
  - Summary: Standard command IDs ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandConstants.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandConstants.StandardGroup;
    ```
- `public static readonly Guid TextEditorGroup = new Guid("2313BC9A-8895-4390-87BF-FA563F35B33B")`
  - Summary: Text editor command IDs ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandConstants.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandConstants.TextEditorGroup;
    ```
- `public static readonly Guid TextReferenceGroup = new Guid("8D5BC6C7-C013-4401-9ADC-62B411573F3C")`
  - Summary: Text reference command IDs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandConstants.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandConstants.TextReferenceGroup;
    ```

## Struct `CommandInfo`

Command data

**Example**

```csharp
var instance = new dnSpy.Contracts.Command.CommandInfo(group: /* Guid */, id: /* int */, arguments: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfo.cs` (line 26)

### Constructors

- `public CommandInfo(Guid group, int id, object arguments = null)`
  - Summary: Constructor
  - Parameters:
    - `Guid group`: Command group, eg.
    - `int id`: Command id
    - `object arguments` (default: `null`): Command arguments or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfo.cs` (line 48)

### Properties

- `public Guid Group { get; }`
  - Summary: Gets the group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Group;
    ```
- `public int ID { get; }`
  - Summary: Gets the command id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ID;
    ```
- `public object Arguments { get; }`
  - Summary: Gets the arguments or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfo.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Arguments;
    ```

## Class `CommandInfoProviderOrder`

order constants

**Example**

```csharp
// Access dnSpy.Contracts.Command.CommandInfoProviderOrder members directly without instantiation.
dnSpy.Contracts.Command.CommandInfoProviderOrder./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfoProviderOrder.cs` (line 24)

### Fields

- `public const double Bookmarks = TextEditor - 4000`
  - Summary: Document viewer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfoProviderOrder.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandInfoProviderOrder.Bookmarks;
    ```
- `public const double Default = 100000`
  - Summary: Default
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfoProviderOrder.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandInfoProviderOrder.Default;
    ```
- `public const double DocumentViewer = TextEditor - 3000`
  - Summary: Document viewer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfoProviderOrder.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandInfoProviderOrder.DocumentViewer;
    ```
- `public const double EditCode = TextEditor - 3000`
  - Summary: Edit Code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfoProviderOrder.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandInfoProviderOrder.EditCode;
    ```
- `public const double HexEditor = TextEditor`
  - Summary: Hex editor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfoProviderOrder.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandInfoProviderOrder.HexEditor;
    ```
- `public const double OutputTextPane = TextEditor - 3000`
  - Summary: Output logger text pane
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfoProviderOrder.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandInfoProviderOrder.OutputTextPane;
    ```
- `public const double REPL = TextEditor - 3000`
  - Summary: REPL editor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfoProviderOrder.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandInfoProviderOrder.REPL;
    ```
- `public const double TextEditor = 50000`
  - Summary: Text editor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfoProviderOrder.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandInfoProviderOrder.TextEditor;
    ```
- `public const double TextReferences = TextEditor - 2000`
  - Summary: Text references
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandInfoProviderOrder.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandInfoProviderOrder.TextReferences;
    ```

## Struct `CommandShortcut`

Keyboard shortcut and command

**Example**

```csharp
var instance = new dnSpy.Contracts.Command.CommandShortcut(shortcut: /* KeyShortcut */, cmd: /* CommandInfo */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 26)

### Constructors

- `public CommandShortcut(KeyShortcut shortcut, CommandInfo cmd)`
  - Parameters:
    - `KeyShortcut shortcut`: Description not provided.
    - `CommandInfo cmd`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 41)

### Methods

- `public static CommandShortcut Alt(Key key, CommandInfo cmd)`
  - Parameters:
    - `Key key`: Description not provided.
    - `CommandInfo cmd`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.CommandShortcut.Alt(key: /* Key */, cmd: /* CommandInfo */);
    ```
- `public static CommandShortcut Control(Key key, CommandInfo cmd)`
  - Parameters:
    - `Key key`: Description not provided.
    - `CommandInfo cmd`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.CommandShortcut.Control(key: /* Key */, cmd: /* CommandInfo */);
    ```
- `public static CommandShortcut Create(Key key, CommandInfo cmd)`
  - Parameters:
    - `Key key`: Description not provided.
    - `CommandInfo cmd`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.CommandShortcut.Create(key: /* Key */, cmd: /* CommandInfo */);
    ```
- `public static CommandShortcut Create(KeyInput key1, KeyInput key2, CommandInfo cmd)`
  - Parameters:
    - `KeyInput key1`: Description not provided.
    - `KeyInput key2`: Description not provided.
    - `CommandInfo cmd`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.CommandShortcut.Create(key1: /* KeyInput */, key2: /* KeyInput */, cmd: /* CommandInfo */);
    ```
- `public static CommandShortcut CtrlAlt(Key key, CommandInfo cmd)`
  - Parameters:
    - `Key key`: Description not provided.
    - `CommandInfo cmd`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.CommandShortcut.CtrlAlt(key: /* Key */, cmd: /* CommandInfo */);
    ```
- `public static CommandShortcut CtrlShift(Key key, CommandInfo cmd)`
  - Parameters:
    - `Key key`: Description not provided.
    - `CommandInfo cmd`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.CommandShortcut.CtrlShift(key: /* Key */, cmd: /* CommandInfo */);
    ```
- `public static CommandShortcut CtrlShiftAlt(Key key, CommandInfo cmd)`
  - Parameters:
    - `Key key`: Description not provided.
    - `CommandInfo cmd`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.CommandShortcut.CtrlShiftAlt(key: /* Key */, cmd: /* CommandInfo */);
    ```
- `public static CommandShortcut Shift(Key key, CommandInfo cmd)`
  - Parameters:
    - `Key key`: Description not provided.
    - `CommandInfo cmd`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.CommandShortcut.Shift(key: /* Key */, cmd: /* CommandInfo */);
    ```
- `public static CommandShortcut ShiftAlt(Key key, CommandInfo cmd)`
  - Parameters:
    - `Key key`: Description not provided.
    - `CommandInfo cmd`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.CommandShortcut.ShiftAlt(key: /* Key */, cmd: /* CommandInfo */);
    ```

### Properties

- `public CommandInfo CommandInfo { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 29)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CommandInfo;
    ```
- `public KeyShortcut KeyShortcut { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandShortcut.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.KeyShortcut;
    ```

## Class `CommandTargetCommand`

Implements by using a instance

**Inherits/Implements:** `ICommand`

**Example**

```csharp
var instance = new dnSpy.Contracts.Command.CommandTargetCommand(commandTarget: /* ICommandTarget */, cmdId: /* StandardIds */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetCommand.cs` (line 27)

### Constructors

- `public CommandTargetCommand(ICommandTarget commandTarget, Guid group, int cmdId)`
  - Summary: Constructor
  - Parameters:
    - `ICommandTarget commandTarget`: Command target
    - `Guid group`: Command group, eg.
    - `int cmdId`: Command ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetCommand.cs` (line 56)
- `public CommandTargetCommand(ICommandTarget commandTarget, StandardIds cmdId)`
  - Summary: Constructor
  - Parameters:
    - `ICommandTarget commandTarget`: Command target
    - `StandardIds cmdId`: Command ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetCommand.cs` (line 37)
- `public CommandTargetCommand(ICommandTarget commandTarget, TextEditorIds cmdId)`
  - Summary: Constructor
  - Parameters:
    - `ICommandTarget commandTarget`: Command target
    - `TextEditorIds cmdId`: Command ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetCommand.cs` (line 46)

## Class `CommandTargetFilterOrder`

order constants

**Example**

```csharp
// Access dnSpy.Contracts.Command.CommandTargetFilterOrder members directly without instantiation.
dnSpy.Contracts.Command.CommandTargetFilterOrder./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 24)

### Fields

- `public const double Bookmarks = TextEditor - 4000`
  - Summary: Document viewer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.Bookmarks;
    ```
- `public const double DocumentViewer = TextEditor - 3000`
  - Summary: Document viewer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.DocumentViewer;
    ```
- `public const double EditCode = TextEditor - 3000`
  - Summary: Edit Code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.EditCode;
    ```
- `public const double HexDefaultIntellisenseQuickInfo = HexIntellisenseSessionStack - 1000`
  - Summary: Default quick info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 74)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.HexDefaultIntellisenseQuickInfo;
    ```
- `public const double HexEditor = TextEditor`
  - Summary: Hex editor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.HexEditor;
    ```
- `public const double HexIntellisenseSessionStack = HexEditor - 4000`
  - Summary: Intellisense session stack
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 71)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.HexIntellisenseSessionStack;
    ```
- `public const double HexViewSearchService = HexEditor - 1000`
  - Summary: Search service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 80)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.HexViewSearchService;
    ```
- `public const double HexViewSearchServiceFocused = HexEditor - 1000000`
  - Summary: Search service when UI is visible
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 77)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.HexViewSearchServiceFocused;
    ```
- `public const double IntellisenseDefaultStatmentCompletion = IntellisenseSessionStack - 1000`
  - Summary: Default statement completion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.IntellisenseDefaultStatmentCompletion;
    ```
- `public const double IntellisenseRoslynQuickInfo = IntellisenseRoslynSignatureHelp - 1000`
  - Summary: Roslyn quick info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 65)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.IntellisenseRoslynQuickInfo;
    ```
- `public const double IntellisenseRoslynSignatureHelp = IntellisenseRoslynStatmentCompletion - 1000`
  - Summary: Roslyn signature help
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 62)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.IntellisenseRoslynSignatureHelp;
    ```
- `public const double IntellisenseRoslynStatmentCompletion = IntellisenseDefaultStatmentCompletion - 1000`
  - Summary: Roslyn statement completion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 59)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.IntellisenseRoslynStatmentCompletion;
    ```
- `public const double IntellisenseSessionStack = TextEditor - 4000`
  - Summary: Intellisense session stack
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.IntellisenseSessionStack;
    ```
- `public const double OutputTextPane = TextEditor - 3000`
  - Summary: Output logger text pane
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.OutputTextPane;
    ```
- `public const double REPL = TextEditor - 3000`
  - Summary: REPL editor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.REPL;
    ```
- `public const double SearchService = TextEditor - 1000`
  - Summary: Search service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.SearchService;
    ```
- `public const double SearchServiceFocused = TextEditor - 1000000`
  - Summary: Search service when UI is visible
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.SearchServiceFocused;
    ```
- `public const double TextEditor = 50000`
  - Summary: Text editor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.TextEditor;
    ```
- `public const double UndoRedo = TextEditor - 1`
  - Summary: Undo/redo
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetFilterOrder.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.CommandTargetFilterOrder.UndoRedo;
    ```

## Enum `CommandTargetStatus`

result

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.CommandTargetStatus and call its members.
var instance = new dnSpy.Contracts.Command.CommandTargetStatus(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/CommandTargetStatus.cs` (line 24)

### Members

- `Handled`: Command was handled, don't call the next in the chain
- `NotHandled`: Command was not handled, call the next in the chain
- `LetWpfHandleCommand`: Let WPF handle the command, don't pass it to the next handler

## Class `ExportCommandInfoProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `ICommandInfoProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Command.ExportCommandInfoProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandInfoProvider.cs` (line 60)

### Constructors

- `public ExportCommandInfoProviderAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order of this instance, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandInfoProvider.cs` (line 64)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandInfoProvider.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportCommandTargetFilterProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `ICommandTargetFilterProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Command.ExportCommandTargetFilterProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetFilterProvider.cs` (line 46)

### Constructors

- `public ExportCommandTargetFilterProviderAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order of this instance, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetFilterProvider.cs` (line 50)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetFilterProvider.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Enum `HexEditorIds`

Text editor command IDs (group = )

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.HexEditorIds and call its members.
var instance = new dnSpy.Contracts.Command.HexEditorIds(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/HexEditorIds.cs` (line 26)

### Members

- `TYPECHAR`: Type character. The argument is the string to add.
- `BACKSPACE`: Backspace
- `RETURN`: ENTER
- `TAB`: Tab
- `BACKTAB`: Tab Left
- `DELETE`: Delete
- `LEFT`: Char Left; Move the caret left one character.
- `LEFT_EXT`: Char Left Extend; Move the caret left one character, extending the selection.
- `RIGHT`: Char Right; Move the caret right one character.
- `RIGHT_EXT`: Char Right Extend; Move the caret right one character, extending the selection.
- `UP`: Line Up.
- `UP_EXT`: Line Up Extend; Move the caret up one line, extending the selection.
- `DOWN`: Line Down; Move the caret down one line.
- `DOWN_EXT`: Line Down Extend; Move the caret down one line, extending the selection.
- `HOME`: Document Start; Move the caret to the start of the document.
- `HOME_EXT`: Document Start Extend; Move the caret to the start of the document, extending the selection.
- `END`: Document End; Move the caret to the end of the document.
- `END_EXT`: Document End Extend; Move the caret to the end of the document, extending the selection.
- `BOL`: Line Start; Move the caret to the start of the line.
- `BOL_EXT`: Line Start Extend; Move the caret to the start of the line, extending the selection.
- `EOL`: Line End; Move the caret to the end of the line..
- `EOL_EXT`: Line End Extend; Move the caret to the end of the line, extending the selection.
- `PAGEUP`: Page Up; Move the caret up one page.
- `PAGEUP_EXT`: Page Up Extend; Move the caret up one page, extending the selection.
- `PAGEDN`: Page Down; Move the caret down one page.
- `PAGEDN_EXT`: Page Down Extend; Move the caret down one page, extending the selection.
- `TOPLINE`: View Top; Move the caret to the top line in view.
- `TOPLINE_EXT`: View Top Extend; Move the caret to the top line in view, extending the selection.
- `BOTTOMLINE`: View Bottom; Move the caret to the last line in view.
- `BOTTOMLINE_EXT`: View Bottom Extend; Move the caret to the last line in view, extending the selection.
- `SCROLLUP`: Scroll Line Up: Scroll the document up one line.
- `SCROLLDN`: Scroll Line Down; Scroll the document down one line.
- `SCROLLPAGEUP`: Scroll Page Up: Scroll the document up one page..
- `SCROLLPAGEDN`: Scroll Page Down: Scroll the document down one page.
- `SCROLLLEFT`: Scroll Column Left; Scroll the document left one column.
- `SCROLLRIGHT`: Scroll Column Right; Scroll the document right one column.
- `SCROLLBOTTOM`: Scroll Line Bottom; Scroll the current line to the bottom of the view.
- `SCROLLCENTER`: Scroll Line Center; Scroll the current line to the center of the view.
- `SCROLLTOP`: Scroll Line Top: Scroll the current line to the top of the view.
- `SELECTALL`: Select All; Select all of the document.
- `SELSWAPANCHOR`: Swap Anchor; Swap the anchor and end points of the current selection.
- `TOGGLE_OVERTYPE_MODE`: Overtype Mode; Toggle between insert and overtype insertion modes.
- `DELETELINE`: Delete Line; Delete all selected lines, or the current line if no selection.
- `DELETETOEOL`: Delete To EOL; Delete from the caret position to the end of the line.
- `DELETETOBOL`: Delete To BOL; Delete from the caret position to the beginning of the line.
- `SELECTCURRENTWORD`: Select Current Word; Select the word under the caret.
- `WORDPREV`: Word Previous; Move the caret left one word.
- `WORDPREV_EXT`: Word Previous Extend; Move the caret left one word, extending the selection.
- `WORDNEXT`: Word Next; Move the caret right one word.
- `WORDNEXT_EXT`: Word Next Extend; Move the caret right one word, extending the selection.
- `CANCEL`: Selection Cancel; Cancel the current selection moving the caret to the anchor point.
- `ZoomIn`: Zoom in
- `ZoomOut`: Zoom out
- `ZoomReset`: Resets the zoom level to the default zoom level
- `QUICKINFO`: Quick Info; Display Quick Info based on the current language.
- `DECREASEFILTER`: Decrease filter
- `INCREASEFILTER`: Increase filter
- `CopyText`: Copies the text shown in the UI
- `CopyUtf8String`: Copies data (UTF-8)
- `CopyUnicodeString`: Copies data (Unicode)
- `CopyCSharpArray`: Copies data (C# array)
- `CopyVisualBasicArray`: Copies data (Visual Basic array)
- `CopyOffset`: Copies the offset
- `CopyValue`: Copies data (Value)
- `CopyUInt16`: Copies data ()
- `CopyUInt16BigEndian`: Copies data ( Big Endian)
- `CopyUInt32`: Copies data ()
- `CopyUInt32BigEndian`: Copies data ( Big Endian)
- `CopyUInt64`: Copies data ()
- `CopyUInt64BigEndian`: Copies data ( Big Endian)
- `CopyFileOffset`: Copies file offset. If it's a PE file, the position is converted to a position within the PE file on disk. If it's not a PE file, it's the offset relative to the start of the file.
- `CopyAbsoluteFileOffset`: Copies absolute file offset (the position in the buffer)
- `CopyRVA`: Copies RVA
- `PasteUtf8String`: Pastes UTF-8 data
- `PasteUtf8String7BitEncodedLengthPrefix`: Pastes 7-bit encoded length followed by UTF-8 bytes
- `PasteUnicodeString`: Pastes Unicode (UTF-16) data
- `PasteUnicodeString7BitEncodedLengthPrefix`: Pastes 7-bit encoded length followed by Unicode (UTF-16) bytes
- `PasteBlob`: Pastes blob data
- `ShowAllBytes`: Shows all bytes ()
- `ShowOnlySelectedBytes`: Shows only the selected bytes
- `Refresh`: Refreshes the screen and clears any read caches
- `SelectAllBytesBlock`: Selects all bytes in the current block, unless the caret is in a memory hole
- `MoveToNextValidStartEnd`: Move to the next closest start/end position of a block of memory
- `MoveToNextValidStartEndExt`: Move to the next closest start/end position of a block of memory; extend selection
- `MoveToPreviousValidStartEnd`: Move to the previous closest start/end position of a block of memory
- `MoveToPreviousValidStartEndExt`: Move to the previous closest start/end position of a block of memory; extend selection
- `GoToCodeOrStructure`: Go to high-level code (eg. decompiled code) or other high level structure
- `FollowFieldValueReference`: Follows the field reference
- `SelectNestedFile`: Select the most nested file at current position
- `SelectFile`: Select the non-nested file at current position
- `SelectStructure`: Selects the current structure

## Class `HexEditorIdsExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Command.HexEditorIdsExtensions members directly without instantiation.
dnSpy.Contracts.Command.HexEditorIdsExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/HexEditorIdsExtensions.cs` (line 24)

### Methods

- `public static CommandInfo ToCommandInfo(this HexEditorIds id)`
  - Summary: Converts to a
  - Parameters:
    - `this HexEditorIds id`: ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/HexEditorIdsExtensions.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.HexEditorIdsExtensions.ToCommandInfo(id: /* HexEditorIds */);
    ```
- `public static CommandInfo ToCommandInfo(this HexEditorIds id, object arguments)`
  - Summary: Converts to a
  - Parameters:
    - `this HexEditorIds id`: ID
    - `object arguments`: Arguments or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/HexEditorIdsExtensions.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.HexEditorIdsExtensions.ToCommandInfo(id: /* HexEditorIds */, arguments: /* object */);
    ```

## Interface `ICommandHolder`

Implement this interface to return the original instance, eg. a

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandHolder and call its members.
var instance = new dnSpy.Contracts.Command.ICommandHolder(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandHolder.cs` (line 26)

### Properties

- `ICommand Command { get; }`
  - Summary: Returns the original instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandHolder.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Command;
    ```

## Interface `ICommandInfoProvider`

Converts raw input to a . Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandInfoProvider and call its members.
var instance = new dnSpy.Contracts.Command.ICommandInfoProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandInfoProvider.cs` (line 29)

### Methods

- `IEnumerable<CommandShortcut> GetCommandShortcuts(object target)`
  - Summary: Gets all keyboard shortcuts
  - Parameters:
    - `object target`: Target object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandInfoProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCommandShortcuts(target: /* object */);
    ```

## Interface `ICommandInfoProvider2`

Converts user input to a

**Inherits/Implements:** `ICommandInfoProvider`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandInfoProvider2 and call its members.
var instance = new dnSpy.Contracts.Command.ICommandInfoProvider2(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandInfoProvider.cs` (line 41)

### Methods

- `CommandInfo? CreateFromTextInput(object target, string text)`
  - Summary: Returns a created from user text
  - Parameters:
    - `object target`: Target object
    - `string text`: Text typed by the user
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandInfoProvider.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateFromTextInput(target: /* object */, text: /* string */);
    ```

## Interface `ICommandInfoProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandInfoProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Command.ICommandInfoProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandInfoProvider.cs` (line 52)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandInfoProvider.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `ICommandService`

Converts raw input to commands and sends them to s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandService and call its members.
var instance = new dnSpy.Contracts.Command.ICommandService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandService.cs` (line 26)

### Methods

- `IRegisteredCommandElement Register(UIElement sourceElement, object target)`
  - Summary: Registers an element
  - Parameters:
    - `UIElement sourceElement`: Source element that provides the keyboard input
    - `object target`: Target object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandService.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Register(sourceElement: /* UIElement */, target: /* object */);
    ```

## Interface `ICommandTarget`

Handles commands

IOleCommandTarget

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandTarget and call its members.
var instance = new dnSpy.Contracts.Command.ICommandTarget(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTarget.cs` (line 27)

### Methods

- `CommandTargetStatus CanExecute(Guid group, int cmdId)`
  - Summary: Checks whether the command can execute. If it can execute, it must return
  - Parameters:
    - `Guid group`: Command group, eg.
    - `int cmdId`: Command ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTarget.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.CanExecute(group: /* Guid */, cmdId: /* int */);
    ```
- `CommandTargetStatus Execute(Guid group, int cmdId, object args = null)`
  - Summary: Executes the command
  - Parameters:
    - `Guid group`: Command group, eg.
    - `int cmdId`: Command ID
    - `object args` (default: `null`): Arguments or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTarget.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(group: /* Guid */, cmdId: /* int */, args: /* object */);
    ```
- `CommandTargetStatus Execute(Guid group, int cmdId, object args, ref object result)`
  - Summary: Executes the command
  - Parameters:
    - `Guid group`: Command group, eg.
    - `int cmdId`: Command ID
    - `object args`: Arguments or null
    - `ref object result`: Updated with the result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTarget.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(group: /* Guid */, cmdId: /* int */, args: /* object */, result: /* object */);
    ```

## Interface `ICommandTargetCollection`

Allows adding and removing s

**Inherits/Implements:** `ICommandTarget`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandTargetCollection and call its members.
var instance = new dnSpy.Contracts.Command.ICommandTargetCollection(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetCollection.cs` (line 24)

### Methods

- `void AddFilter(ICommandTargetFilter filter, double order)`
  - Summary: Adds a new filter
  - Parameters:
    - `ICommandTargetFilter filter`: Filter to add
    - `double order`: Order, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetCollection.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.AddFilter(filter: /* ICommandTargetFilter */, order: /* double */);
    ```
- `void RemoveFilter(ICommandTargetFilter filter)`
  - Summary: Removes an added filter
  - Parameters:
    - `ICommandTargetFilter filter`: Filter to remove
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetCollection.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveFilter(filter: /* ICommandTargetFilter */);
    ```

## Interface `ICommandTargetCollectionProvider`

provider

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandTargetCollectionProvider and call its members.
var instance = new dnSpy.Contracts.Command.ICommandTargetCollectionProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetCollectionProvider.cs` (line 24)

### Properties

- `ICommandTargetCollection CommandTarget { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetCollectionProvider.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CommandTarget;
    ```

## Interface `ICommandTargetFilter`

Handles commands

**Inherits/Implements:** `ICommandTarget`, `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandTargetFilter and call its members.
var instance = new dnSpy.Contracts.Command.ICommandTargetFilter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetFilter.cs` (line 26)

### Methods

- `void SetNextCommandTarget(ICommandTarget commandTarget)`
  - Summary: Called once to set its next handler
  - Parameters:
    - `ICommandTarget commandTarget`: Next command target
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetFilter.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.SetNextCommandTarget(commandTarget: /* ICommandTarget */);
    ```

## Interface `ICommandTargetFilterProvider`

Creates instances. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandTargetFilterProvider and call its members.
var instance = new dnSpy.Contracts.Command.ICommandTargetFilterProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetFilterProvider.cs` (line 28)

### Methods

- `ICommandTargetFilter Create(object target)`
  - Summary: Creates a new instance or returns null
  - Parameters:
    - `object target`: Target object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetFilterProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(target: /* object */);
    ```

## Interface `ICommandTargetFilterProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ICommandTargetFilterProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Command.ICommandTargetFilterProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetFilterProvider.cs` (line 38)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ICommandTargetFilterProvider.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IRegisteredCommandElement`

Created by

**Inherits/Implements:** `ICommandTargetCollectionProvider`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.IRegisteredCommandElement and call its members.
var instance = new dnSpy.Contracts.Command.IRegisteredCommandElement(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/IRegisteredCommandElement.cs` (line 26)

### Methods

- `void Unregister()`
  - Summary: Unregisters it from
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/IRegisteredCommandElement.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Unregister();
    ```

## Struct `KeyInput`

**Inherits/Implements:** `IEquatable<KeyInput>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Command.KeyInput(key: /* Key */, modifiers: /* ModifierKeys */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 25)

### Constructors

- `public KeyInput(Key key, ModifierKeys modifiers)`
  - Parameters:
    - `Key key`: Description not provided.
    - `ModifierKeys modifiers`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 40)
- `public KeyInput(KeyEventArgs e)`
  - Parameters:
    - `KeyEventArgs e`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 45)

### Methods

- `public bool Equals(KeyInput other)`
  - Parameters:
    - `KeyInput other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* KeyInput */);
    ```
- `public override bool Equals(object obj)`
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static KeyInput Alt(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyInput.Alt(key: /* Key */);
    ```
- `public static KeyInput Control(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyInput.Control(key: /* Key */);
    ```
- `public static KeyInput Create(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyInput.Create(key: /* Key */);
    ```
- `public static KeyInput CtrlAlt(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyInput.CtrlAlt(key: /* Key */);
    ```
- `public static KeyInput CtrlShift(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyInput.CtrlShift(key: /* Key */);
    ```
- `public static KeyInput CtrlShiftAlt(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyInput.CtrlShiftAlt(key: /* Key */);
    ```
- `public static KeyInput Shift(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyInput.Shift(key: /* Key */);
    ```
- `public static KeyInput ShiftAlt(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyInput.ShiftAlt(key: /* Key */);
    ```

### Properties

- `public Key Key { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Key;
    ```
- `public ModifierKeys Modifiers { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 29)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Modifiers;
    ```

### Fields

- `public static readonly KeyInput Default = new KeyInput(Key.None, ModifierKeys.None)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Command.KeyInput.Default;
    ```

### Operators

- `public static bool operator !=(KeyInput a, KeyInput b) => !a.Equals(b);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 51)
- `public static bool operator ==(KeyInput a, KeyInput b) => a.Equals(b);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyInput.cs` (line 50)

## Struct `KeyShortcut`

**Inherits/Implements:** `IEquatable<KeyShortcut>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Command.KeyShortcut(key: /* Key */, modifiers: /* ModifierKeys */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 25)

### Constructors

- `public KeyShortcut(Key key, ModifierKeys modifiers)`
  - Parameters:
    - `Key key`: Description not provided.
    - `ModifierKeys modifiers`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 40)
- `public KeyShortcut(KeyInput keyInput1, KeyInput keyInput2)`
  - Parameters:
    - `KeyInput keyInput1`: Description not provided.
    - `KeyInput keyInput2`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 45)

### Methods

- `public bool Equals(KeyShortcut other)`
  - Parameters:
    - `KeyShortcut other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* KeyShortcut */);
    ```
- `public override bool Equals(object obj)`
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static KeyShortcut Alt(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyShortcut.Alt(key: /* Key */);
    ```
- `public static KeyShortcut Control(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyShortcut.Control(key: /* Key */);
    ```
- `public static KeyShortcut Create(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyShortcut.Create(key: /* Key */);
    ```
- `public static KeyShortcut CtrlAlt(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyShortcut.CtrlAlt(key: /* Key */);
    ```
- `public static KeyShortcut CtrlShift(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyShortcut.CtrlShift(key: /* Key */);
    ```
- `public static KeyShortcut CtrlShiftAlt(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyShortcut.CtrlShiftAlt(key: /* Key */);
    ```
- `public static KeyShortcut Shift(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyShortcut.Shift(key: /* Key */);
    ```
- `public static KeyShortcut ShiftAlt(Key key)`
  - Parameters:
    - `Key key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.KeyShortcut.ShiftAlt(key: /* Key */);
    ```

### Properties

- `public KeyInput KeyInput1 { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 26)
  - Example:
    ```csharp
    // Read the property
    var value = instance.KeyInput1;
    ```
- `public KeyInput KeyInput2 { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 27)
  - Example:
    ```csharp
    // Read the property
    var value = instance.KeyInput2;
    ```
- `public bool HasTwoKeyInputs => KeyInput2 != KeyInput.Default`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 29)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasTwoKeyInputs;
    ```

### Operators

- `public static bool operator !=(KeyShortcut a, KeyShortcut b) => !a.Equals(b);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 51)
- `public static bool operator ==(KeyShortcut a, KeyShortcut b) => a.Equals(b);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/KeyShortcut.cs` (line 50)

## Enum `OutputTextPaneIds`

command IDs

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.OutputTextPaneIds and call its members.
var instance = new dnSpy.Contracts.Command.OutputTextPaneIds(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/OutputTextPaneIds.cs` (line 26)

### Members

- `ClearAll`: Clears all text

## Class `OutputTextPaneIdsExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Command.OutputTextPaneIdsExtensions members directly without instantiation.
dnSpy.Contracts.Command.OutputTextPaneIdsExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/OutputTextPaneIdsExtensions.cs` (line 24)

### Methods

- `public static CommandInfo ToCommandInfo(this OutputTextPaneIds id)`
  - Summary: Converts to a
  - Parameters:
    - `this OutputTextPaneIds id`: ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/OutputTextPaneIdsExtensions.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.OutputTextPaneIdsExtensions.ToCommandInfo(id: /* OutputTextPaneIds */);
    ```
- `public static CommandInfo ToCommandInfo(this OutputTextPaneIds id, object arguments)`
  - Summary: Converts to a
  - Parameters:
    - `this OutputTextPaneIds id`: ID
    - `object arguments`: Arguments or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/OutputTextPaneIdsExtensions.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.OutputTextPaneIdsExtensions.ToCommandInfo(id: /* OutputTextPaneIds */, arguments: /* object */);
    ```

## Enum `ReplIds`

REPL command IDs

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.ReplIds and call its members.
var instance = new dnSpy.Contracts.Command.ReplIds(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ReplIds.cs` (line 24)

### Members

- `CopyCode`: Copies only the code, but not the prompts or script output
- `Submit`: Submits current user input
- `NewLineDontSubmit`: Adds a new line without submitting the current input
- `ClearInput`: Clears the user input
- `ClearScreen`: Clears the screen
- `Reset`: Resets the REPL editor (but not the owner, eg. C# scripting state)
- `SelectPreviousCommand`: Selects the previous command
- `SelectNextCommand`: Selects the next command
- `SelectSameTextPreviousCommand`: Selects the previous command matching the current input text
- `SelectSameTextNextCommand`: Selects the next command matching the current input text

## Class `ReplIdsExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Command.ReplIdsExtensions members directly without instantiation.
dnSpy.Contracts.Command.ReplIdsExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/ReplIdsExtensions.cs` (line 24)

### Methods

- `public static CommandInfo ToCommandInfo(this ReplIds id)`
  - Summary: Converts to a
  - Parameters:
    - `this ReplIds id`: ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ReplIdsExtensions.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.ReplIdsExtensions.ToCommandInfo(id: /* ReplIds */);
    ```
- `public static CommandInfo ToCommandInfo(this ReplIds id, object arguments)`
  - Summary: Converts to a
  - Parameters:
    - `this ReplIds id`: ID
    - `object arguments`: Arguments or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/ReplIdsExtensions.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.ReplIdsExtensions.ToCommandInfo(id: /* ReplIds */, arguments: /* object */);
    ```

## Enum `StandardIds`

Standard command IDs (group = )

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.StandardIds and call its members.
var instance = new dnSpy.Contracts.Command.StandardIds(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/StandardIds.cs` (line 24)

### Members

- `Unknown`: Unknown command, if no other command is found
- `Copy`: Copy
- `Cut`: Cut
- `Paste`: Paste
- `Undo`: Undo
- `Redo`: Redo
- `Find`: Find (eg. Ctrl+F)
- `Replace`: Replace (eg. Ctrl+H)
- `IncrementalSearchForward`: Forward incremental search (eg. Ctrl+I)
- `IncrementalSearchBackward`: Backward incremental search (eg. Ctrl+Shift+I)
- `FindNext`: Find next (eg. F3)
- `FindPrevious`: Find previous (eg. Shift+F3)
- `FindNextSelected`: Find next selected (eg. Ctrl+F3)
- `FindPreviousSelected`: Find previous selected (eg. Ctrl+Shift+F3)

## Class `StandardIdsExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Command.StandardIdsExtensions members directly without instantiation.
dnSpy.Contracts.Command.StandardIdsExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/StandardIdsExtensions.cs` (line 24)

### Methods

- `public static CommandInfo ToCommandInfo(this StandardIds id)`
  - Summary: Converts to a
  - Parameters:
    - `this StandardIds id`: ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/StandardIdsExtensions.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.StandardIdsExtensions.ToCommandInfo(id: /* StandardIds */);
    ```
- `public static CommandInfo ToCommandInfo(this StandardIds id, object arguments)`
  - Summary: Converts to a
  - Parameters:
    - `this StandardIds id`: ID
    - `object arguments`: Arguments or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/StandardIdsExtensions.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.StandardIdsExtensions.ToCommandInfo(id: /* StandardIds */, arguments: /* object */);
    ```

## Enum `TextEditorIds`

Text editor command IDs (group = )

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.TextEditorIds and call its members.
var instance = new dnSpy.Contracts.Command.TextEditorIds(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/TextEditorIds.cs` (line 24)

### Members

- `TYPECHAR`: Type character. The argument is the string to add.
- `BACKSPACE`: Delete Backwards; Delete the current selection, or if no selection, the previous character.
- `RETURN`: Break Line; Insert a line break at the current caret position.
- `TAB`: Insert Tab; Insert a tab character at the current caret position.
- `BACKTAB`: Tab Left; Move the caret back one tab stop.
- `DELETE`: Delete; Delete the current selection.
- `LEFT`: Char Left; Move the caret left one character.
- `LEFT_EXT`: Char Left Extend; Move the caret left one character, extending the selection.
- `RIGHT`: Char Right; Move the caret right one character.
- `RIGHT_EXT`: Char Right Extend; Move the caret right one character, extending the selection.
- `UP`: Line Up.
- `UP_EXT`: Line Up Extend; Move the caret up one line, extending the selection.
- `DOWN`: Line Down; Move the caret down one line.
- `DOWN_EXT`: Line Down Extend; Move the caret down one line, extending the selection.
- `HOME`: Document Start; Move the caret to the start of the document.
- `HOME_EXT`: Document Start Extend; Move the caret to the start of the document, extending the selection.
- `END`: Document End; Move the caret to the end of the document.
- `END_EXT`: Document End Extend; Move the caret to the end of the document, extending the selection.
- `BOL`: Line Start; Move the caret to the start of the line.
- `BOL_EXT`: Line Start Extend; Move the caret to the start of the line, extending the selection.
- `FIRSTCHAR`: Line Start After Indentation; Move the caret to first non-white space character on the line.
- `FIRSTCHAR_EXT`: Line Start After Indentation Extend; Move the caret to first non-white space character on the line, extending the selection.
- `EOL`: Line End; Move the caret to the end of the line..
- `EOL_EXT`: Line End Extend; Move the caret to the end of the line, extending the selection.
- `LASTCHAR`: Line Last Char; Move the caret after the last non-white space character on the line.
- `LASTCHAR_EXT`: Line Last Char Extend; Move the caret after the last non-white space character on the line, extending the selection..
- `PAGEUP`: Page Up; Move the caret up one page.
- `PAGEUP_EXT`: Page Up Extend; Move the caret up one page, extending the selection.
- `PAGEDN`: Page Down; Move the caret down one page.
- `PAGEDN_EXT`: Page Down Extend; Move the caret down one page, extending the selection.
- `TOPLINE`: View Top; Move the caret to the top line in view.
- `TOPLINE_EXT`: View Top Extend; Move the caret to the top line in view, extending the selection.
- `BOTTOMLINE`: View Bottom; Move the caret to the last line in view.
- `BOTTOMLINE_EXT`: View Bottom Extend; Move the caret to the last line in view, extending the selection.
- `SCROLLUP`: Scroll Line Up: Scroll the document up one line.
- `SCROLLDN`: Scroll Line Down; Scroll the document down one line.
- `SCROLLPAGEUP`: Scroll Page Up: Scroll the document up one page..
- `SCROLLPAGEDN`: Scroll Page Down: Scroll the document down one page.
- `SCROLLLEFT`: Scroll Column Left; Scroll the document left one column.
- `SCROLLRIGHT`: Scroll Column Right; Scroll the document right one column.
- `SCROLLBOTTOM`: Scroll Line Bottom; Scroll the current line to the bottom of the view.
- `SCROLLCENTER`: Scroll Line Center; Scroll the current line to the center of the view.
- `SCROLLTOP`: Scroll Line Top: Scroll the current line to the top of the view.
- `SELECTALL`: Select All; Select all of the document.
- `SELTABIFY`: Tabify Selection: Replace spaces in the current selection with tabs.
- `SELUNTABIFY`: Untabify Selection; Replace tabs in the current selection with spaces.
- `SELLOWCASE`: Make Lowercase; Change the text in the current selection to all lower case.
- `SELUPCASE`: Make Uppercase; Change the text in the current selection to all upper case.
- `SELTOGGLECASE`: Toggle Case: Toggle the case of the text in the current selection.
- `SELTITLECASE`: Capitalize; Capitalize the first letter of words in the selection.
- `SELSWAPANCHOR`: Swap Anchor; Swap the anchor and end points of the current selection.
- `GOTOLINE`: Go To Line; Go to the indicated line.
- `GOTOBRACE`: Goto Brace; Move the caret forward to the matching brace.
- `GOTOBRACE_EXT`: Goto Brace Extend; Move the caret forward to the matching brace, extending the selection.
- `TOGGLE_OVERTYPE_MODE`: Overtype Mode; Toggle between insert and overtype insertion modes.
- `CUTLINE`: Line Cut; Cut all selected lines, or the current line if no selection, to the clipboard.
- `DELETELINE`: Delete Line; Delete all selected lines, or the current line if no selection.
- `DELETEBLANKLINES`: Delete Blank Lines; Delete all blank lines in the selection, or the current blank line if no selection.
- `DELETEWHITESPACE`: Delete Horizontal White Space; Collapse white space in the selection, or delete white space adjacent to the caret if no selection.
- `DELETETOEOL`: Delete To EOL; Delete from the caret position to the end of the line.
- `DELETETOBOL`: Delete To BOL; Delete from the caret position to the beginning of the line.
- `OPENLINEABOVE`: Line Open Above; Open a new line above the current line.
- `OPENLINEBELOW`: Line Open Below: Open a new line below the current line.
- `INDENT`: Increase Line Indent; Increase Indent.
- `UNINDENT`: Decrease Line Indent; Line Unindent.
- `TRANSPOSECHAR`: Char Transpose: Transpose the characters on either side of the caret.
- `TRANSPOSEWORD`: Word Transpose; Transpose the words on either side of the caret.
- `TRANSPOSELINE`: Line Transpose; Transpose the current line and the line below.
- `SELECTCURRENTWORD`: Select Current Word; Select the word under the caret.
- `DELETEWORDRIGHT`: Word Delete To End; Delete the word to the right of the caret.
- `DELETEWORDLEFT`: Word Delete To Start; Delete the word to the left of the caret.
- `WORDPREV`: Word Previous; Move the caret left one word.
- `WORDPREV_EXT`: Word Previous Extend; Move the caret left one word, extending the selection.
- `WORDNEXT`: Word Next; Move the caret right one word.
- `WORDNEXT_EXT`: Word Next Extend; Move the caret right one word, extending the selection.
- `CANCEL`: Selection Cancel; Cancel the current selection moving the caret to the anchor point.
- `TOGGLEVISSPACE`: View White Space; Toggle the visibility of white space characters.
- `COMPLETEWORD`: Complete Word; Display Word Completion based on the current language.
- `SHOWMEMBERLIST`: Show Member List; Display an object Member List based on the current language.
- `FIRSTNONWHITEPREV`: Line Start After Indentation Next; Move the caret to the first non-white-space character on the previous line.
- `FIRSTNONWHITENEXT`: Line Start After Indentation Next; Move the caret to the first non-white-space character on the next line.
- `LEFT_EXT_COL`: Char Left Extend Column; Move the caret left one character, extending the column selection.
- `RIGHT_EXT_COL`: Char Right Extend Column; Move the caret right one character, extending the column selection.
- `UP_EXT_COL`: Line Up Extend Column; Move the caret up one line, extending the column selection.
- `DOWN_EXT_COL`: Line Down Extend Column; Move the caret down one line, extending the column selection.
- `TOGGLEWORDWRAP`: Toggle Word Wrap; Toggle Word Wrap mode.
- `BOL_EXT_COL`: Line Start Extend Column; Move the caret to the start of the line, extending the column selection.
- `EOL_EXT_COL`: Line End Extend Column; Move the caret to the end of the line, extending the column selection.
- `WORDPREV_EXT_COL`: Word Previous Extend Column; Move the caret left one word, extending the column selection.
- `WORDNEXT_EXT_COL`: Word Next Extend Column; Move the caret right one word, extending the column selection.
- `ECMD_CONVERTTABSTOSPACES`: Convert tabs to spaces
- `ECMD_CONVERTSPACESTOTABS`: Convert spaces to tabs
- `EditorLineFirstColumn`: Editor line first column
- `EditorLineFirstColumnExtend`: Editor line first column extended
- `ToggleConsumeFirstCompletionMode`: Toggle consume first completion mode
- `ZoomIn`: Zoom in
- `ZoomOut`: Zoom out
- `ZoomReset`: Resets the zoom level to the default zoom level
- `MoveSelLinesUp`: Move selected lines up
- `MoveSelLinesDown`: Move seleted lines down
- `SmartBreakLine`: Smart Break Line
- `DECREASEFILTER`: Decrease filter
- `INCREASEFILTER`: Increase filter
- `QUICKINFO`: Quick Info; Display Quick Info based on the current language.
- `PARAMINFO`: Parameter Info; Display Parameter Info based on the current language.

## Class `TextEditorIdsExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Command.TextEditorIdsExtensions members directly without instantiation.
dnSpy.Contracts.Command.TextEditorIdsExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/TextEditorIdsExtensions.cs` (line 24)

### Methods

- `public static CommandInfo ToCommandInfo(this TextEditorIds id)`
  - Summary: Converts to a
  - Parameters:
    - `this TextEditorIds id`: ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/TextEditorIdsExtensions.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.TextEditorIdsExtensions.ToCommandInfo(id: /* TextEditorIds */);
    ```
- `public static CommandInfo ToCommandInfo(this TextEditorIds id, object arguments)`
  - Summary: Converts to a
  - Parameters:
    - `this TextEditorIds id`: ID
    - `object arguments`: Arguments or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Command/TextEditorIdsExtensions.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Command.TextEditorIdsExtensions.ToCommandInfo(id: /* TextEditorIds */, arguments: /* object */);
    ```

## Enum `TextReferenceIds`

Reference IDs

**Example**

```csharp
// Instantiate dnSpy.Contracts.Command.TextReferenceIds and call its members.
var instance = new dnSpy.Contracts.Command.TextReferenceIds(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Command/TextReferenceIds.cs` (line 24)

### Members

- `MoveToNextReference`: Move the caret to the next reference
- `MoveToPreviousReference`: Move the caret to the previous reference
- `MoveToNextDefinition`: Move the caret to the next definition
- `MoveToPreviousDefinition`: Move the caret to the previous definition
- `FollowReference`: Move the caret to the definition the reference references
- `FollowReferenceNewTab`: Move the caret to the definition the reference references, use a new tab

