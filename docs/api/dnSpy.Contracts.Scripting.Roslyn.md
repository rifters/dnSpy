# Namespace `dnSpy.Contracts.Scripting.Roslyn`

## Interface `ICachedWriter`

Writes text to a buffer and flushes it when (or ) is called.

**Inherits/Implements:** `ITextPrinter`, `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Scripting.Roslyn.ICachedWriter and call its members.
var instance = new dnSpy.Contracts.Scripting.Roslyn.ICachedWriter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ICachedWriter.cs` (line 27)

### Methods

- `void Flush()`
  - Summary: Flushes current output. This method gets called automatically by
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ICachedWriter.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.Flush();
    ```

## Interface `IPrintOptions`

Print options ()

**Example**

```csharp
// Instantiate dnSpy.Contracts.Scripting.Roslyn.IPrintOptions and call its members.
var instance = new dnSpy.Contracts.Scripting.Roslyn.IPrintOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IPrintOptions.cs` (line 26)

### Properties

- `MemberDisplayFormat MemberDisplayFormat { get; set; }`
  - Summary: Member display format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IPrintOptions.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberDisplayFormat;
    ```
- `bool AutoColorizeObjects { get; set; }`
  - Summary: If true, all calls to will call if the object implements that interface.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IPrintOptions.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AutoColorizeObjects;
    ```
- `bool EscapeNonPrintableCharacters { get; set; }`
  - Summary: Escape non-printable characters
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IPrintOptions.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EscapeNonPrintableCharacters;
    ```
- `int MaximumOutputLength { get; set; }`
  - Summary: Maximum output length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IPrintOptions.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MaximumOutputLength;
    ```
- `int NumberRadix { get; set; }`
  - Summary: Number radix
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IPrintOptions.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NumberRadix;
    ```
- `string Ellipsis { get; set; }`
  - Summary: Ellipsis string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IPrintOptions.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Ellipsis;
    ```

## Interface `IScriptGlobals`

The script's global class

**Inherits/Implements:** `ITextPrinter`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Scripting.Roslyn.IScriptGlobals and call its members.
var instance = new dnSpy.Contracts.Scripting.Roslyn.IScriptGlobals(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 31)

### Methods

- `ICachedWriter CreateWriter()`
  - Summary: Creates a new instance. Useful if your script runs in the background and prints text.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 235)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateWriter();
    ```
- `MsgBoxButton Show(string message, MsgBoxButton buttons = MsgBoxButton.OK, Window ownerWindow = null)`
  - Summary: Shows a message box
  - Parameters:
    - `string message`: Message to show
    - `MsgBoxButton buttons` (default: `MsgBoxButton.OK`): Buttons that should be present
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 278)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(message: /* string */, buttons: /* MsgBoxButton */, ownerWindow: /* Window */);
    ```
- `MsgBoxButton ShowOC(string message, Window ownerWindow = null)`
  - Summary: Shows a message box with buttons OK and Cancel
  - Parameters:
    - `string message`: Message to show
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 294)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowOC(message: /* string */, ownerWindow: /* Window */);
    ```
- `MsgBoxButton ShowOKCancel(string message, Window ownerWindow = null)`
  - Summary: Shows a message box with buttons OK and Cancel
  - Parameters:
    - `string message`: Message to show
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 286)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowOKCancel(message: /* string */, ownerWindow: /* Window */);
    ```
- `MsgBoxButton ShowYN(string message, Window ownerWindow = null)`
  - Summary: Shows a message box with buttons Yes and No
  - Parameters:
    - `string message`: Message to show
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 310)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowYN(message: /* string */, ownerWindow: /* Window */);
    ```
- `MsgBoxButton ShowYNC(string message, Window ownerWindow = null)`
  - Summary: Shows a message box with buttons Yes, No and Cancel
  - Parameters:
    - `string message`: Message to show
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 326)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowYNC(message: /* string */, ownerWindow: /* Window */);
    ```
- `MsgBoxButton ShowYesNo(string message, Window ownerWindow = null)`
  - Summary: Shows a message box with buttons Yes and No
  - Parameters:
    - `string message`: Message to show
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 302)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowYesNo(message: /* string */, ownerWindow: /* Window */);
    ```
- `MsgBoxButton ShowYesNoCancel(string message, Window ownerWindow = null)`
  - Summary: Shows a message box with buttons Yes, No and Cancel
  - Parameters:
    - `string message`: Message to show
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 318)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowYesNoCancel(message: /* string */, ownerWindow: /* Window */);
    ```
- `T Ask<T>(string labelMessage, string defaultText = null, string title = null, Func<string, T> converter = null, Func<string, string> verifier = null, Window ownerWindow = null)`
  - Summary: Asks the user for a value and returns it or the default value (eg. null or 0) if the user canceled the dialog box.
  - Parameters:
    - `string labelMessage`: Label
    - `string defaultText` (default: `null`): Default text to write to the textbox or null
    - `string title` (default: `null`): Title or null
    - `Func<string, T> converter` (default: `null`): Converts a string to the type, or null to use the default converter.
    - `Func<string, string> verifier` (default: `null`): Verifies the typed message. Returns null or an empty string if it's a valid value, else an error message to show to the user.
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 342)
  - Example:
    ```csharp
    // Example invocation
    instance.Ask(labelMessage: /* string */, defaultText: /* string */, title: /* string */, converter: /* Func<string, T> */, verifier: /* Func<string, string> */, ownerWindow: /* Window */);
    ```
- `T Resolve<T>()`
  - Summary: Resolves a service, and throws if it wasn't found
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 262)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve();
    ```
- `T TryResolve<T>()`
  - Summary: Resolves a service or returns null if not found
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 269)
  - Example:
    ```csharp
    // Example invocation
    instance.TryResolve();
    ```
- `T UI<T>(Func<T> func)`
  - Summary: Executes in the UI thread
  - Parameters:
    - `Func<T> func`: Code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 249)
  - Example:
    ```csharp
    // Example invocation
    instance.UI(func: /* Func<T> */);
    ```
- `void Break()`
  - Summary: Calls . Use dnSpy to debug itself (dnSpy --multiple) and then call this method from your script in the debugged dnSpy process.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 255)
  - Example:
    ```csharp
    // Example invocation
    instance.Break();
    ```
- `void Show(Exception exception, string msg = null, Window ownerWindow = null)`
  - Summary: Shows an exception message
  - Parameters:
    - `Exception exception`: Exception
    - `string msg` (default: `null`): Message to show or null
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 350)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(exception: /* Exception */, msg: /* string */, ownerWindow: /* Window */);
    ```
- `void UI(Action action)`
  - Summary: Executes in the UI thread
  - Parameters:
    - `Action action`: Code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 241)
  - Example:
    ```csharp
    // Example invocation
    instance.UI(action: /* Action */);
    ```

### Properties

- `CancellationToken Token { get; }`
  - Summary: Cancellation token that gets signalled when the script gets reset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```
- `Dispatcher UIDispatcher { get; }`
  - Summary: UI thread dispatcher
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 228)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIDispatcher;
    ```
- `IScriptGlobals Instance { get; }`
  - Summary: Returns itself so it can be passed into classes that can't access the globals
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Instance;
    ```

### Events

- `event EventHandler ScriptResetting`
  - Summary: Raised before the script gets reset. Can be used to unregister from events to prevent memory leaks. Raised on the UI thread.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/IScriptGlobals.cs` (line 41)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ScriptResetting += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `ITextPrinter`

Prints text

**Inherits/Implements:** `IOutputWriter`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Scripting.Roslyn.ITextPrinter and call its members.
var instance = new dnSpy.Contracts.Scripting.Roslyn.ITextPrinter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 27)

### Methods

- `void Print(Exception ex, TextColor color = TextColor.Error)`
  - Summary: Formats and prints an exception to the screen
  - Parameters:
    - `Exception ex`: Exception
    - `TextColor color` (default: `TextColor.Error`): Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 185)
  - Example:
    ```csharp
    // Example invocation
    instance.Print(ex: /* Exception */, color: /* TextColor */);
    ```
- `void Print(Exception ex, object color)`
  - Summary: Formats and prints an exception to the screen
  - Parameters:
    - `Exception ex`: Exception
    - `object color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 178)
  - Example:
    ```csharp
    // Example invocation
    instance.Print(ex: /* Exception */, color: /* object */);
    ```
- `void Print(TextColor color, string fmt, params object[] args)`
  - Summary: Prints text to the screen
  - Parameters:
    - `TextColor color`: Color
    - `string fmt`: Format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.Print(color: /* TextColor */, fmt: /* string */);
    ```
- `void Print(TextColor color, string text)`
  - Summary: Prints text to the screen
  - Parameters:
    - `TextColor color`: Color
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.Print(color: /* TextColor */, text: /* string */);
    ```
- `void Print(object color, string fmt, params object[] args)`
  - Summary: Prints text to the screen
  - Parameters:
    - `object color`: Color
    - `string fmt`: Format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.Print(color: /* object */, fmt: /* string */);
    ```
- `void Print(object color, string text)`
  - Summary: Prints text to the screen
  - Parameters:
    - `object color`: Color
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.Print(color: /* object */, text: /* string */);
    ```
- `void Print(object value, TextColor color = TextColor.ReplScriptOutputText)`
  - Summary: Formats and prints a value to the screen
  - Parameters:
    - `object value`: Value, can be null
    - `TextColor color` (default: `TextColor.ReplScriptOutputText`): Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.Print(value: /* object */, color: /* TextColor */);
    ```
- `void Print(object value, object color)`
  - Summary: Formats and prints a value to the screen
  - Parameters:
    - `object value`: Value, can be null
    - `object color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 150)
  - Example:
    ```csharp
    // Example invocation
    instance.Print(value: /* object */, color: /* object */);
    ```
- `void Print(string fmt, params object[] args)`
  - Summary: Prints text to the screen
  - Parameters:
    - `string fmt`: Format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.Print(fmt: /* string */);
    ```
- `void Print(string text)`
  - Summary: Prints text to the screen
  - Parameters:
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Print(text: /* string */);
    ```
- `void PrintError(string fmt, params object[] args)`
  - Summary: Prints text to the screen
  - Parameters:
    - `string fmt`: Format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintError(fmt: /* string */);
    ```
- `void PrintError(string text)`
  - Summary: Prints text to the screen
  - Parameters:
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintError(text: /* string */);
    ```
- `void PrintLine(Exception ex, TextColor color = TextColor.Error)`
  - Summary: Formats and prints an exception followed by a new line to the screen
  - Parameters:
    - `Exception ex`: Exception
    - `TextColor color` (default: `TextColor.Error`): Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLine(ex: /* Exception */, color: /* TextColor */);
    ```
- `void PrintLine(Exception ex, object color)`
  - Summary: Formats and prints an exception followed by a new line to the screen
  - Parameters:
    - `Exception ex`: Exception
    - `object color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 192)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLine(ex: /* Exception */, color: /* object */);
    ```
- `void PrintLine(TextColor color, string fmt, params object[] args)`
  - Summary: Prints text followed by a new line to the screen
  - Parameters:
    - `TextColor color`: Color
    - `string fmt`: Format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 136)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLine(color: /* TextColor */, fmt: /* string */);
    ```
- `void PrintLine(TextColor color, string text)`
  - Summary: Prints text followed by a new line to the screen
  - Parameters:
    - `TextColor color`: Color
    - `string text`: Text or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLine(color: /* TextColor */, text: /* string */);
    ```
- `void PrintLine(object color, string fmt, params object[] args)`
  - Summary: Prints text followed by a new line to the screen
  - Parameters:
    - `object color`: Color
    - `string fmt`: Format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 128)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLine(color: /* object */, fmt: /* string */);
    ```
- `void PrintLine(object color, string text)`
  - Summary: Prints text followed by a new line to the screen
  - Parameters:
    - `object color`: Color
    - `string text`: Text or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 107)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLine(color: /* object */, text: /* string */);
    ```
- `void PrintLine(object value, TextColor color = TextColor.ReplScriptOutputText)`
  - Summary: Formats and prints a value followed by a new line to the screen
  - Parameters:
    - `object value`: Value or null
    - `TextColor color` (default: `TextColor.ReplScriptOutputText`): Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 171)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLine(value: /* object */, color: /* TextColor */);
    ```
- `void PrintLine(object value, object color)`
  - Summary: Formats and prints a value followed by a new line to the screen
  - Parameters:
    - `object value`: Value or null
    - `object color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 164)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLine(value: /* object */, color: /* object */);
    ```
- `void PrintLine(string fmt, params object[] args)`
  - Summary: Prints text followed by a new line to the screen
  - Parameters:
    - `string fmt`: Format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLine(fmt: /* string */);
    ```
- `void PrintLine(string text = null)`
  - Summary: Prints text followed by a new line to the screen
  - Parameters:
    - `string text` (default: `null`): Text or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 120)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLine(text: /* string */);
    ```
- `void PrintLineError(string fmt, params object[] args)`
  - Summary: Prints text followed by a new line to the screen
  - Parameters:
    - `string fmt`: Format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLineError(fmt: /* string */);
    ```
- `void PrintLineError(string text)`
  - Summary: Prints text followed by a new line to the screen
  - Parameters:
    - `string text`: Text or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintLineError(text: /* string */);
    ```

### Properties

- `IPrintOptions PrintOptions { get; }`
  - Summary: Print options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/ITextPrinter.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PrintOptions;
    ```

## Enum `MemberDisplayFormat`

Member display format ()

**Example**

```csharp
// Instantiate dnSpy.Contracts.Scripting.Roslyn.MemberDisplayFormat and call its members.
var instance = new dnSpy.Contracts.Scripting.Roslyn.MemberDisplayFormat(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/Roslyn/MemberDisplayFormat.cs` (line 24)

### Members

- `SingleLine`: Display structure of the object on a single line.
- `SeparateLines`: Displays a simple description of the object followed by list of members. Each member is displayed on a separate line.
- `Hidden`: Display just a simple description of the object, like type name or ToString(). Don't display any members of the object.

