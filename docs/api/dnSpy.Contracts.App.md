# Namespace `dnSpy.Contracts.App`

## Class `AppDirectories`

Application directories

**Example**

```csharp
// Access dnSpy.Contracts.App.AppDirectories members directly without instantiation.
dnSpy.Contracts.App.AppDirectories./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/AppDirectories.cs` (line 29)

### Methods

- `public static IEnumerable<string> GetDirectories(string subDir)`
  - Summary: Returns directories relative to and in that order. If they're identical, only one path is returned.
  - Parameters:
    - `string subDir`: Sub directory
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/AppDirectories.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.App.AppDirectories.GetDirectories(subDir: /* string */);
    ```

### Properties

- `public static string BinDirectory { get; }`
  - Summary: Base directory of dnSpy binaries
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/AppDirectories.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.App.AppDirectories.BinDirectory;
    ```
- `public static string DataDirectory { get; }`
  - Summary: Base directory of data directory. Usually %APPDATA%\dnSpy but could be identical to .
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/AppDirectories.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.App.AppDirectories.DataDirectory;
    ```
- `public static string SettingsFilename => settingsFilename`
  - Summary: dnSpy settings filename
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/AppDirectories.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.App.AppDirectories.SettingsFilename;
    ```

## Class `ExportDsLoaderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDsLoaderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.App.ExportDsLoaderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/IDsLoader.cs` (line 62)

### Constructors

- `public ExportDsLoaderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IDsLoader.cs` (line 65)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IDsLoader.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IAppCommandLineArgs`

Application command line arguments

**Example**

```csharp
// Instantiate dnSpy.Contracts.App.IAppCommandLineArgs and call its members.
var instance = new dnSpy.Contracts.App.IAppCommandLineArgs(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 29)

### Methods

- `IEnumerable<Tuple<string, string>> GetArguments()`
  - Summary: Gets all user arguments and values
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 112)
  - Example:
    ```csharp
    // Example invocation
    instance.GetArguments();
    ```
- `bool HasArgument(string argName)`
  - Summary: Returns true if the argument is present
  - Parameters:
    - `string argName`: Argument name, eg. --my-arg
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.HasArgument(argName: /* string */);
    ```
- `string GetArgumentValue(string argName)`
  - Summary: Gets the argument value or null if the argument isn't present
  - Parameters:
    - `string argName`: Argument name, eg. --my-arg
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.GetArgumentValue(argName: /* string */);
    ```

### Properties

- `IEnumerable<string> Filenames { get; }`
  - Summary: Filenames to load
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filenames;
    ```
- `bool Activate { get; }`
  - Summary: true to activate the window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Activate;
    ```
- `bool LoadFiles { get; }`
  - Summary: true to load all saved files at startup
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LoadFiles;
    ```
- `bool NewTab { get; }`
  - Summary: Show the file in a new tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewTab;
    ```
- `bool ShowStartupTime { get; }`
  - Summary: Show start up time
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowStartupTime;
    ```
- `bool SingleInstance { get; }`
  - Summary: true if single-instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SingleInstance;
    ```
- `bool? FullScreen { get; }`
  - Summary: Full screen
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FullScreen;
    ```
- `int DebugAttachPid { get; }`
  - Summary: Attach to this process, unless it's 0
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DebugAttachPid;
    ```
- `string Culture { get; }`
  - Summary: Culture
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Culture;
    ```
- `string DebugAttachProcess { get; }`
  - Summary: Attach to this process name, unless it's empty. Can contain wildcards.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DebugAttachProcess;
    ```
- `string HideToolWindow { get; }`
  - Summary: Tool windows to hide
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HideToolWindow;
    ```
- `string Language { get; }`
  - Summary: Language, either human readable or a language guid ( or )
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Language;
    ```
- `string SearchFor { get; }`
  - Summary: Search type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SearchFor;
    ```
- `string SearchIn { get; }`
  - Summary: Search location
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SearchIn;
    ```
- `string SearchText { get; }`
  - Summary: Search string or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SearchText;
    ```
- `string SelectMember { get; }`
  - Summary: Member to select, either an MD token or an XML doc name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectMember;
    ```
- `string SettingsFilename { get; }`
  - Summary: Settings filename
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SettingsFilename;
    ```
- `string ShowToolWindow { get; }`
  - Summary: Tool windows to show
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowToolWindow;
    ```
- `string Theme { get; }`
  - Summary: Theme name ( or )
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Theme;
    ```
- `uint DebugEvent { get; }`
  - Summary: Event handle duplicated into the postmortem debugger process
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DebugEvent;
    ```
- `ulong JitDebugInfo { get; }`
  - Summary: Address of a JIT_DEBUG_INFO structure allocated in the target process' address space (https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/-jdinfo--use-jit-debug-info-)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgs.cs` (line 89)
  - Example:
    ```csharp
    // Read the property
    var value = instance.JitDebugInfo;
    ```

## Interface `IAppCommandLineArgsHandler`

Gets notified when new command line arguments have been passed to dnSpy

**Example**

```csharp
// Instantiate dnSpy.Contracts.App.IAppCommandLineArgsHandler and call its members.
var instance = new dnSpy.Contracts.App.IAppCommandLineArgsHandler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgsHandler.cs` (line 24)

### Methods

- `void OnNewArgs(IAppCommandLineArgs args)`
  - Summary: Called whenever there are new command line arguments
  - Parameters:
    - `IAppCommandLineArgs args`: Command line arguments
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgsHandler.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewArgs(args: /* IAppCommandLineArgs */);
    ```

### Properties

- `double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppCommandLineArgsHandler.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IAppStatusBar`

App status bar

**Example**

```csharp
// Instantiate dnSpy.Contracts.App.IAppStatusBar and call its members.
var instance = new dnSpy.Contracts.App.IAppStatusBar(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/IAppStatusBar.cs` (line 24)

### Methods

- `void Close()`
  - Summary: Closes the status bar
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppStatusBar.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```
- `void Open()`
  - Summary: Opens the status bar
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppStatusBar.cs` (line 28)
  - Example:
    ```csharp
    // Example invocation
    instance.Open();
    ```
- `void Show(string text)`
  - Summary: Shows text in the status bar
  - Parameters:
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppStatusBar.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(text: /* string */);
    ```

## Interface `IAppWindow`

App window

**Example**

```csharp
// Instantiate dnSpy.Contracts.App.IAppWindow and call its members.
var instance = new dnSpy.Contracts.App.IAppWindow(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 30)

### Methods

- `void AddTitleInfo(string info)`
  - Summary: Adds to the window title
  - Parameters:
    - `string info`: Some text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.AddTitleInfo(info: /* string */);
    ```
- `void RefreshToolBar()`
  - Summary: Refreshes the toolbar
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.RefreshToolBar();
    ```
- `void RemoveTitleInfo(string info)`
  - Summary: Removes from the window title
  - Parameters:
    - `string info`: Some text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveTitleInfo(info: /* string */);
    ```

### Properties

- `IAppCommandLineArgs CommandLineArgs { get; }`
  - Summary: Gets the command line args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CommandLineArgs;
    ```
- `IAppStatusBar StatusBar { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StatusBar;
    ```
- `IWpfCommands MainWindowCommands { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MainWindowCommands;
    ```
- `Window MainWindow { get; }`
  - Summary: Gets the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MainWindow;
    ```
- `bool AppLoaded { get; }`
  - Summary: true if the app has been loaded
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppLoaded;
    ```
- `string AssemblyInformationalVersion { get; }`
  - Summary: Gets the version (stored in an attribute)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyInformationalVersion;
    ```

### Events

- `event EventHandler<CancelEventArgs> MainWindowClosing`
  - Summary: Raised when the main window is closing
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 34)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.MainWindowClosing += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<EventArgs> MainWindowClosed`
  - Summary: Raised when the main window has closed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IAppWindow.cs` (line 39)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.MainWindowClosed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IDsLoader`

Called at startup and exit. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.App.IDsLoader and call its members.
var instance = new dnSpy.Contracts.App.IDsLoader(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/IDsLoader.cs` (line 30)

### Methods

- `IEnumerable<object> Load(ISettingsService settingsService, IAppCommandLineArgs args)`
  - Summary: Called when dnSpy has just started. If the method takes too long to execute, give control back to dnSpy by using yield return. Only values in are used by the loader, anything else is ignored.
  - Parameters:
    - `ISettingsService settingsService`: Settings manager
    - `IAppCommandLineArgs args`: Command line arguments
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IDsLoader.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.Load(settingsService: /* ISettingsService */, args: /* IAppCommandLineArgs */);
    ```
- `void OnAppLoaded()`
  - Summary: Called when everything has been loaded
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IDsLoader.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.OnAppLoaded();
    ```
- `void Save(ISettingsService settingsService)`
  - Summary: Called when dnSpy exits
  - Parameters:
    - `ISettingsService settingsService`: Settings manager
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IDsLoader.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Save(settingsService: /* ISettingsService */);
    ```

## Interface `IDsLoaderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.App.IDsLoaderMetadata and call its members.
var instance = new dnSpy.Contracts.App.IDsLoaderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/IDsLoader.cs` (line 54)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IDsLoader.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IMessageBoxService`

Shows message boxes

**Example**

```csharp
// Instantiate dnSpy.Contracts.App.IMessageBoxService and call its members.
var instance = new dnSpy.Contracts.App.IMessageBoxService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/IMessageBoxService.cs` (line 27)

### Methods

- `MsgBoxButton Show(string message, MsgBoxButton buttons = MsgBoxButton.OK, Window ownerWindow = null)`
  - Summary: Shows a message box
  - Parameters:
    - `string message`: Message to show
    - `MsgBoxButton buttons` (default: `MsgBoxButton.OK`): Buttons that should be present
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IMessageBoxService.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(message: /* string */, buttons: /* MsgBoxButton */, ownerWindow: /* Window */);
    ```
- `MsgBoxButton? ShowIgnorableMessage(Guid guid, string message, MsgBoxButton buttons = MsgBoxButton.OK, Window ownerWindow = null)`
  - Summary: Shows a message box unless the user has disabled showing this particular message. null is returned if the message was ignored and no message box was shown. Otherwise, the return value is the same as .
  - Parameters:
    - `Guid guid`: Unique guid for this message
    - `string message`: Message to show
    - `MsgBoxButton buttons` (default: `MsgBoxButton.OK`): Buttons that should be present
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IMessageBoxService.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowIgnorableMessage(guid: /* Guid */, message: /* string */, buttons: /* MsgBoxButton */, ownerWindow: /* Window */);
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
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IMessageBoxService.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.Ask(labelMessage: /* string */, defaultText: /* string */, title: /* string */, converter: /* Func<string, T> */, verifier: /* Func<string, string> */, ownerWindow: /* Window */);
    ```
- `void Show(Exception exception, string msg = null, Window ownerWindow = null)`
  - Summary: Shows an exception message
  - Parameters:
    - `Exception exception`: Exception
    - `string msg` (default: `null`): Message to show or null
    - `Window ownerWindow` (default: `null`): Owner window or null to use the main window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IMessageBoxService.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(exception: /* Exception */, msg: /* string */, ownerWindow: /* Window */);
    ```

## Interface `IOpenFromGAC`

Opens a file from the GAC (Global Assembly Cache)

**Example**

```csharp
// Instantiate dnSpy.Contracts.App.IOpenFromGAC and call its members.
var instance = new dnSpy.Contracts.App.IOpenFromGAC(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/IOpenFromGAC.cs` (line 27)

### Methods

- `ModuleDef[] OpenAssemblies(bool selectAssembly, Window ownerWindow = null)`
  - Summary: Returns an array of selected GAC assemblies
  - Parameters:
    - `bool selectAssembly`: true to select the assembly in Assembly Explorer
    - `Window ownerWindow` (default: `null`): Owner window or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IOpenFromGAC.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.OpenAssemblies(selectAssembly: /* bool */, ownerWindow: /* Window */);
    ```
- `string[] GetPaths(Window ownerWindow = null)`
  - Summary: Returns an array of selected GAC assemblies
  - Parameters:
    - `Window ownerWindow` (default: `null`): Owner window or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/IOpenFromGAC.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPaths(ownerWindow: /* Window */);
    ```

## Class `LoaderConstants`

Constants

**Example**

```csharp
// Access dnSpy.Contracts.App.LoaderConstants members directly without instantiation.
dnSpy.Contracts.App.LoaderConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/LoaderConstants.cs` (line 26)

### Fields

- `public const double ORDER_DOCUMENTTABMANAGER = 1000`
  - Summary: Order of 's instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/LoaderConstants.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.App.LoaderConstants.ORDER_DOCUMENTTABMANAGER;
    ```
- `public static readonly object Delay = new object()`
  - Summary: Delays the loading a short while
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/LoaderConstants.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.App.LoaderConstants.Delay;
    ```

## Class `MsgBox`

Contains an instance

**Example**

```csharp
// Access dnSpy.Contracts.App.MsgBox members directly without instantiation.
dnSpy.Contracts.App.MsgBox./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/MsgBox.cs` (line 26)

### Properties

- `public static IMessageBoxService Instance {
			get => messageBoxService;
			internal set {
				if (messageBoxService != null)
					throw new InvalidOperationException();
				messageBoxService = value ?? throw new ArgumentNullException(nameof(value));
			}
		}`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/App/MsgBox.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.App.MsgBox.Instance;
    ```

## Enum `MsgBoxButton`

Buttons

**Example**

```csharp
// Instantiate dnSpy.Contracts.App.MsgBoxButton and call its members.
var instance = new dnSpy.Contracts.App.MsgBoxButton(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/App/MsgBoxButton.cs` (line 26)

### Members

- `None`: None, eg. the user pressed Alt+F4 to close the message box
- `OK`: OK-button
- `Yes`: Yes-button
- `No`: No-button
- `Cancel`: Cancel-button

