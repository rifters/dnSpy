# dnSpy API Quick Reference

A concise reference for common dnSpy extension development tasks.

## Table of Contents

- [Extension Setup](#extension-setup)
- [Menus](#menus)
- [ToolBars](#toolbars)
- [Commands](#commands)
- [Tool Windows](#tool-windows)
- [Settings](#settings)
- [Debugger](#debugger)
- [Documents](#documents)
- [Common Imports](#common-imports)

---

## Extension Setup

### Minimal Extension

```csharp
using dnSpy.Contracts.Extension;

[ExportExtension]
public sealed class MyExtension : IExtension {
    public ExtensionInfo ExtensionInfo => new ExtensionInfo {
        ShortDescription = "My Extension"
    };
    
    public IEnumerable<string> MergedResourceDictionaries {
        get { yield break; }
    }
    
    public void OnEvent(ExtensionEvent @event, object obj) { }
}
```

### Auto-Loaded Component

```csharp
using dnSpy.Contracts.Extension;

[ExportAutoLoaded]
public sealed class MyComponent : IAutoLoaded {
    [ImportingConstructor]
    public MyComponent(/* dependencies */) {
        // Initialize
    }
}
```

---

## Menus

### Main Menu Item

```csharp
[ExportMenuItem(
    OwnerGuid = MenuConstants.APP_MENU_VIEW_GUID,
    Header = "My Command",
    Group = MenuConstants.GROUP_APP_MENU_VIEW_WINDOWS,
    Order = 1000)]
public sealed class MyCommand : MenuItemBase {
    public override void Execute(IMenuItemContext context) {
        // Execute command
    }
}
```

### Context Menu Item

```csharp
[ExportMenuItem(
    OwnerGuid = MenuConstants.CTX_MENU_GUID,
    Header = "My Context Command",
    Group = "MyGroup",
    Order = 0)]
public sealed class MyContextCommand : MenuItemBase {
    public override void Execute(IMenuItemContext context) {
        var obj = context.Find<MyType>();
        // Handle context
    }
}
```

### Menu with Keyboard Shortcut

```csharp
[ExportMenuItem(
    OwnerGuid = MenuConstants.APP_MENU_VIEW_GUID,
    Header = "My Command",
    InputGestureText = "Ctrl+Alt+M",
    Group = MenuConstants.GROUP_APP_MENU_VIEW_WINDOWS)]
public sealed class MyCommand : MenuItemCommand {
    public MyCommand() : base(MyCommands.ShowCommand) { }
}

[ExportAutoLoaded]
public sealed class MyCommands : IAutoLoaded {
    public static readonly RoutedCommand ShowCommand = 
        new RoutedCommand("Show", typeof(MyCommands));
    
    [ImportingConstructor]
    public MyCommands(IWpfCommandService wpfCommandService) {
        var cmds = wpfCommandService.GetCommands(ControlConstants.GUID_MAINWINDOW);
        cmds.Add(ShowCommand, new RelayCommand(Execute));
        cmds.Add(ShowCommand, ModifierKeys.Control | ModifierKeys.Alt, Key.M);
    }
    
    void Execute(object parameter) { }
}
```

---

## ToolBars

### ToolBar Button

```csharp
[ExportToolBarButton(
    Icon = DsImagesAttribute.Assembly,
    ToolTip = "My Button",
    Group = ToolBarConstants.GROUP_APP_TB_MAIN_NAVIGATION,
    Order = 0)]
public sealed class MyButton : ToolBarButtonBase {
    public override void Execute(IToolBarItemContext context) {
        // Button clicked
    }
}
```

### ToolBar ComboBox

```csharp
[ExportToolBarObject(
    Group = ToolBarConstants.GROUP_APP_TB_MAIN_NAVIGATION,
    Order = 10)]
public sealed class MyComboBox : ToolBarObjectBase {
    readonly ComboBox comboBox;
    
    public MyComboBox() {
        comboBox = new ComboBox { Width = 150 };
        comboBox.Items.Add("Item 1");
        comboBox.SelectionChanged += OnSelectionChanged;
    }
    
    public override object GetUIObject(IToolBarItemContext context, 
        IInputElement commandTarget) => comboBox;
    
    void OnSelectionChanged(object sender, SelectionChangedEventArgs e) { }
}
```

---

## Commands

### Register Command with Keyboard Shortcut

```csharp
[ExportAutoLoaded]
public sealed class MyCommandLoader : IAutoLoaded {
    public static readonly RoutedCommand MyCommand = 
        new RoutedCommand("MyCommand", typeof(MyCommandLoader));
    
    [ImportingConstructor]
    public MyCommandLoader(IWpfCommandService wpfCommandService) {
        var cmds = wpfCommandService.GetCommands(ControlConstants.GUID_MAINWINDOW);
        cmds.Add(MyCommand, new RelayCommand(Execute));
        cmds.Add(MyCommand, ModifierKeys.Control, Key.Q);
    }
    
    void Execute(object parameter) { }
}
```

---

## Tool Windows

### Complete Tool Window

```csharp
// Provider
[Export(typeof(IToolWindowContentProvider))]
public sealed class MyToolWindowProvider : IToolWindowContentProvider {
    public IEnumerable<ToolWindowContentInfo> ContentInfos {
        get {
            yield return new ToolWindowContentInfo(
                MyToolWindow.GUID,
                AppToolWindowLocation.DefaultHorizontal,
                0, false);
        }
    }
    
    public ToolWindowContent GetOrCreate(Guid guid) {
        if (guid == MyToolWindow.GUID)
            return new MyToolWindow();
        return null;
    }
}

// Content
public sealed class MyToolWindow : ToolWindowContent {
    public static readonly Guid GUID = new Guid("{GUID-HERE}");
    
    public override Guid Guid => GUID;
    public override string Title => "My Tool Window";
    public override object UIObject => control;
    
    readonly UserControl control;
    
    public MyToolWindow() {
        control = new UserControl();
    }
}

// Show Command
[ExportMenuItem(
    OwnerGuid = MenuConstants.APP_MENU_VIEW_GUID,
    Header = "My Tool Window",
    Group = MenuConstants.GROUP_APP_MENU_VIEW_WINDOWS)]
public sealed class ShowMyToolWindow : MenuItemBase {
    readonly IDsToolWindowService toolWindowService;
    
    [ImportingConstructor]
    public ShowMyToolWindow(IDsToolWindowService toolWindowService) {
        this.toolWindowService = toolWindowService;
    }
    
    public override void Execute(IMenuItemContext context) {
        toolWindowService.Show(MyToolWindow.GUID);
    }
}
```

---

## Settings

### Save and Load Settings

```csharp
[Export]
public sealed class MySettings {
    readonly ISettingsService settingsService;
    static readonly Guid SETTINGS_GUID = new Guid("{GUID-HERE}");
    
    public string StringSetting { get; set; } = "default";
    public int IntSetting { get; set; } = 42;
    
    [ImportingConstructor]
    public MySettings(ISettingsService settingsService) {
        this.settingsService = settingsService;
        Load();
    }
    
    void Load() {
        var section = settingsService.GetOrCreateSection(SETTINGS_GUID);
        StringSetting = section.Attribute<string>(nameof(StringSetting)) ?? StringSetting;
        IntSetting = section.Attribute<int?>(nameof(IntSetting)) ?? IntSetting;
    }
    
    public void Save() {
        var section = settingsService.RecreateSection(SETTINGS_GUID);
        section.Attribute(nameof(StringSetting), StringSetting);
        section.Attribute(nameof(IntSetting), IntSetting);
    }
}
```

### Settings Page

```csharp
[Export(typeof(IAppSettingsPage))]
public sealed class MySettingsPage : IAppSettingsPage {
    public Guid Guid => new Guid("{GUID-HERE}");
    public double Order => AppSettingsConstants.ORDER_SETTINGS_TAB_MISC + 1;
    public string Title => "My Extension";
    public object UIObject => new MySettingsControl();
    
    public void OnClosed() { }
    public void OnApply() {
        // Save settings
    }
}
```

---

## Debugger

### Start Debugging

```csharp
[ImportingConstructor]
public MyClass(DbgManager dbgManager) {
    var options = new DebugProgramOptions(
        filename: @"C:\path\to\program.exe",
        commandLine: "arg1 arg2",
        currentDirectory: @"C:\path\to");
    
    string error = dbgManager.Start(options);
    if (error != null) {
        MsgBox.Instance.Show($"Failed: {error}");
    }
}
```

### Monitor Debugging Events

```csharp
[ExportAutoLoaded]
public sealed class DebugMonitor : IAutoLoaded {
    [ImportingConstructor]
    public DebugMonitor(DbgManager dbgManager) {
        dbgManager.IsDebuggingChanged += (s, e) => {
            if (dbgManager.IsDebugging) {
                Console.WriteLine("Debugging started");
            }
        };
        
        dbgManager.ProcessPaused += (s, e) => {
            Console.WriteLine($"Process paused: {e.Process.Name}");
        };
    }
}
```

### Add Breakpoint

```csharp
public void AddBreakpoint(
    DbgCodeBreakpointsService service,
    DbgCodeLocation location) {
    
    var settings = new DbgCodeBreakpointSettings {
        IsEnabled = true
    };
    
    var info = new DbgCodeBreakpointInfo(location, settings);
    service.Add(info);
}
```

### Evaluate Expression

```csharp
public void EvaluateExpression(
    DbgEvaluationContext context,
    string expression) {
    
    var evaluator = context.Language.ExpressionEvaluator;
    
    var evalInfo = new DbgExpressionEvaluationInfo(
        context, expression,
        DbgEvaluationOptions.None,
        TimeSpan.FromSeconds(5));
    
    var result = evaluator.Evaluate(evalInfo);
    
    if (result.Error != null) {
        Console.WriteLine($"Error: {result.Error}");
    } else {
        Console.WriteLine($"Result: {result.Value}");
    }
}
```

### Get Call Stack

```csharp
public void ShowCallStack(
    DbgCallStackService callStackService,
    DbgThread thread) {
    
    var frames = callStackService.GetFrames(thread);
    
    for (int i = 0; i < frames.Frames.Length; i++) {
        var frame = frames.Frames[i];
        Console.WriteLine($"#{i}: {frame.Location}");
    }
}
```

---

## Documents

### Load Assembly

```csharp
[ImportingConstructor]
public MyClass(IDsDocumentService documentService) {
    var doc = documentService.TryGetOrCreate(
        DsDocumentInfo.CreateDocument(@"C:\path\to\assembly.dll"));
    
    if (doc != null) {
        var module = doc.ModuleDef;
        var assembly = doc.AssemblyDef;
    }
}
```

### Enumerate Types

```csharp
public void EnumerateTypes(IDsDocumentService documentService) {
    foreach (var doc in documentService.GetDocuments()) {
        foreach (var module in doc.GetModules<ModuleDef>()) {
            foreach (var type in module.GetTypes()) {
                Console.WriteLine(type.FullName);
            }
        }
    }
}
```

### Modify Assembly

```csharp
public void ModifyAssembly(IDsDocument document) {
    var module = document.ModuleDef;
    
    // Add new type
    var newType = new TypeDefUser("MyNamespace", "MyClass");
    newType.Attributes = TypeAttributes.Public | TypeAttributes.Class;
    module.Types.Add(newType);
    
    // Add method
    var method = new MethodDefUser("MyMethod",
        MethodSig.CreateStatic(module.CorLibTypes.Void),
        MethodAttributes.Public | MethodAttributes.Static);
    newType.Methods.Add(method);
}
```

### Monitor Document Changes

```csharp
[ExportAutoLoaded]
public sealed class DocumentMonitor : IAutoLoaded {
    [ImportingConstructor]
    public DocumentMonitor(IDsDocumentService documentService) {
        documentService.CollectionChanged += (s, e) => {
            if (e.Added) {
                Console.WriteLine($"Document added: {e.Documents[0].Filename}");
            }
        };
    }
}
```

---

## Common Imports

### Essential Services

```csharp
using System.ComponentModel.Composition;

[Export]
public sealed class MyService {
    readonly DbgManager dbgManager;
    readonly IDsDocumentService documentService;
    readonly ISettingsService settingsService;
    readonly IOutputService outputService;
    readonly IDsToolWindowService toolWindowService;
    
    [ImportingConstructor]
    public MyService(
        DbgManager dbgManager,
        IDsDocumentService documentService,
        ISettingsService settingsService,
        IOutputService outputService,
        IDsToolWindowService toolWindowService) {
        
        this.dbgManager = dbgManager;
        this.documentService = documentService;
        this.settingsService = settingsService;
        this.outputService = outputService;
        this.toolWindowService = toolWindowService;
    }
}
```

### Common Namespaces

```csharp
// Extension
using dnSpy.Contracts.Extension;

// Menus
using dnSpy.Contracts.Menus;

// ToolBars
using dnSpy.Contracts.ToolBars;

// Commands
using dnSpy.Contracts.Command;
using dnSpy.Contracts.Controls;
using dnSpy.Contracts.MVVM;

// Documents
using dnSpy.Contracts.Documents;
using dnSpy.Contracts.Documents.TreeView;

// Debugger
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Debugger.Breakpoints.Code;
using dnSpy.Contracts.Debugger.CallStack;
using dnSpy.Contracts.Debugger.Evaluation;
using dnSpy.Contracts.Debugger.DotNet;
using dnSpy.Contracts.Debugger.DotNet.Evaluation;

// Settings
using dnSpy.Contracts.Settings;
using dnSpy.Contracts.Settings.Dialog;

// Output
using dnSpy.Contracts.Output;

// Tool Windows
using dnSpy.Contracts.ToolWindows;
using dnSpy.Contracts.ToolWindows.App;

// Images
using dnSpy.Contracts.Images;

// Text Editor
using dnSpy.Contracts.Text;
using dnSpy.Contracts.Text.Editor;

// Themes
using dnSpy.Contracts.Themes;

// MEF
using System.ComponentModel.Composition;

// dnlib
using dnlib.DotNet;
using dnlib.PE;
```

---

## Constants

### Menu GUIDs

```csharp
MenuConstants.APP_MENU_GUID              // Main application menu
MenuConstants.CTX_MENU_GUID              // Context menu
MenuConstants.APP_MENU_FILE_GUID         // File menu
MenuConstants.APP_MENU_EDIT_GUID         // Edit menu
MenuConstants.APP_MENU_VIEW_GUID         // View menu
MenuConstants.APP_MENU_DEBUG_GUID        // Debug menu
MenuConstants.APP_MENU_WINDOW_GUID       // Window menu

// Groups
MenuConstants.GROUP_APP_MENU_VIEW_WINDOWS
MenuConstants.GROUP_APP_MENU_DEBUG_START
```

### ToolBar Groups

```csharp
ToolBarConstants.GROUP_APP_TB_MAIN_NAVIGATION
ToolBarConstants.GROUP_APP_TB_MAIN_OPEN
ToolBarConstants.GROUP_APP_TB_MAIN_ASMED
ToolBarConstants.GROUP_APP_TB_MAIN_DEBUG
```

### Control GUIDs

```csharp
ControlConstants.GUID_MAINWINDOW         // Main window
ControlConstants.GUID_DOCUMENTVIEWER     // Document viewer
```

### Built-in Images

```csharp
DsImages.Assembly
DsImages.Class
DsImages.Method
DsImages.Property
DsImages.Field
DsImages.Event
DsImages.Namespace
DsImages.Module
DsImages.Reference
```

---

## Output Window

### Create Output Pane

```csharp
[Export]
public sealed class MyOutput {
    readonly IOutputService outputService;
    IOutputTextPane pane;
    
    [ImportingConstructor]
    public MyOutput(IOutputService outputService) {
        this.outputService = outputService;
    }
    
    void EnsurePane() {
        if (pane == null) {
            pane = outputService.Create(
                new Guid("{GUID-HERE}"),
                "My Extension");
        }
    }
    
    public void WriteLine(string text) {
        EnsurePane();
        pane.WriteLine(text);
    }
    
    public void WriteError(string text) {
        EnsurePane();
        pane.Write(text, OutputColor.Error);
    }
}
```

---

## Message Boxes

```csharp
using dnSpy.Contracts.App;

// Simple message
MsgBox.Instance.Show("Message");

// With title
MsgBox.Instance.Show("Message", "Title");

// Question
var result = MsgBox.Instance.Show("Question?", MsgBoxButton.YesNo);
if (result == MsgBoxButton.Yes) {
    // Yes clicked
}
```

---

## Best Practices

1. **Always use unique GUIDs** - Generate new GUIDs for your components
2. **Import dependencies via constructor** - Use `[ImportingConstructor]`
3. **Unsubscribe from events** - Prevent memory leaks
4. **Use dispatcher for debugger operations** - `dbgManager.Dispatcher`
5. **Dispose resources** - Call `Dispose()` or `Close()` when done
6. **Check for null** - Always validate objects before use
7. **Handle errors gracefully** - Use try-catch and check return values

---

## Debugging Tips

```csharp
// Check if debugging
if (!dbgManager.IsDebugging) {
    MsgBox.Instance.Show("Not debugging");
    return;
}

// Get current thread safely
var thread = dbgManager.CurrentThread.Current;
if (thread == null) {
    MsgBox.Instance.Show("No current thread");
    return;
}

// Always use dispatcher
dbgManager.Dispatcher.BeginInvoke(() => {
    // Debugger operation
});

// Dispose contexts
DbgEvaluationContext context = null;
try {
    context = CreateContext();
    // Use context
}
finally {
    context?.Close(dbgManager.Dispatcher);
}
```

---

For detailed information, see:
- [API Documentation](API_DOCUMENTATION.md)
- [Debugger API](DEBUGGER_API.md)
- [.NET Debugger API](DOTNET_DEBUGGER_API.md)
