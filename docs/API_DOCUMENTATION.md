# dnSpy API Documentation

## Overview

dnSpy is an extensible debugger and .NET assembly editor with a rich public API. This documentation covers the main extension points and APIs available for building custom functionality.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Extension Development](#extension-development)
3. [Core APIs](#core-apis)
4. [Debugger APIs](#debugger-apis)
5. [Document and Assembly APIs](#document-and-assembly-apis)
6. [UI Components](#ui-components)
7. [Examples](#examples)

---

## Getting Started

### Prerequisites

- .NET Framework 4.6.1 or later
- Visual Studio 2017 or later (for extension development)
- Understanding of C# and .NET

### Creating Your First Extension

1. Create a new .NET Framework class library project
2. Target .NET Framework 4.6.1 or later
3. Reference the appropriate dnSpy.Contracts.* assemblies
4. Implement `IExtension` and export it with `[ExportExtension]`

**Minimal Extension Example:**

```csharp
using System.Collections.Generic;
using dnSpy.Contracts.Extension;

namespace MyExtension {
    [ExportExtension]
    public sealed class MyExtension : IExtension {
        public ExtensionInfo ExtensionInfo => new ExtensionInfo {
            ShortDescription = "My Custom Extension"
        };

        public IEnumerable<string> MergedResourceDictionaries {
            get { yield break; }
        }

        public void OnEvent(ExtensionEvent @event, object obj) {
            // Handle extension lifecycle events
        }
    }
}
```

---

## Extension Development

### Extension Lifecycle

Extensions must implement `IExtension` and are loaded when dnSpy starts. The `OnEvent` method is called during various lifecycle events:

- `ExtensionEvent.Loaded` - After all extensions have been loaded
- `ExtensionEvent.Unloaded` - Before the extension is unloaded

### MEF (Managed Extensibility Framework)

dnSpy uses MEF for dependency injection. Use standard MEF attributes:

- `[Export]` - Export a type
- `[Import]` / `[ImportingConstructor]` - Import dependencies
- Custom export attributes like `[ExportMenuItem]`, `[ExportToolBarButton]`, etc.

### Extension Metadata

```csharp
public interface IExtension {
    ExtensionInfo ExtensionInfo { get; }
    IEnumerable<string> MergedResourceDictionaries { get; }
    void OnEvent(ExtensionEvent @event, object obj);
}
```

---

## Core APIs

### Menu System

Add custom menu items to the main menu or context menus.

#### Creating a Main Menu Item

```csharp
using dnSpy.Contracts.App;
using dnSpy.Contracts.Menus;

[ExportMenuItem(
    OwnerGuid = MenuConstants.APP_MENU_VIEW_GUID, 
    Header = "My Command", 
    Group = MenuConstants.GROUP_APP_MENU_VIEW_WINDOWS, 
    Order = 1000)]
public sealed class MyMenuCommand : MenuItemBase {
    public override void Execute(IMenuItemContext context) {
        MsgBox.Instance.Show("Hello from my command!");
    }
    
    public override bool IsEnabled(IMenuItemContext context) => true;
    public override bool IsVisible(IMenuItemContext context) => true;
}
```

#### Creating a Context Menu Item

```csharp
[ExportMenuItem(
    OwnerGuid = MenuConstants.CTX_MENU_GUID,
    Header = "My Context Command",
    Group = "MyGroup",
    Order = 0)]
public sealed class MyContextCommand : MenuItemBase {
    public override void Execute(IMenuItemContext context) {
        // Access context information
        var obj = context.Find<MyObject>();
        if (obj != null) {
            // Perform action on obj
        }
    }
}
```

#### Menu Item API Reference

**IMenuItemContext Members:**
- `Guid MenuGuid` - Top-level menu GUID
- `bool OpenedFromKeyboard` - True if opened via keyboard
- `GuidObject CreatorObject` - Object that created the menu
- `IEnumerable<GuidObject> GuidObjects` - All available objects
- `T Find<T>()` - Find first object of type T
- `T GetOrCreateState<T>(object key, Func<T> createState)` - Cache state across menu calls

**MenuItemBase Virtual Methods:**
- `void Execute(IMenuItemContext context)` - Execute the command (required)
- `bool IsEnabled(IMenuItemContext context)` - Return true if enabled
- `bool IsVisible(IMenuItemContext context)` - Return true if visible
- `string GetHeader(IMenuItemContext context)` - Custom header text
- `ImageReference? GetIcon(IMenuItemContext context)` - Custom icon
- `string GetInputGestureText(IMenuItemContext context)` - Custom shortcut text
- `bool IsChecked(IMenuItemContext context)` - Return true if checked

### ToolBar System

Add buttons, comboboxes, and custom UI elements to toolbars.

#### Adding a ToolBar Button

```csharp
using dnSpy.Contracts.Images;
using dnSpy.Contracts.ToolBars;

[ExportToolBarButton(
    Icon = DsImagesAttribute.Assembly,
    ToolTip = "My Button",
    Group = ToolBarConstants.GROUP_APP_TB_MAIN_NAVIGATION,
    Order = 0)]
public sealed class MyToolBarButton : ToolBarButtonBase {
    public override void Execute(IToolBarItemContext context) {
        // Button clicked
    }
}
```

#### Adding a Custom ToolBar Object

```csharp
using System.Windows.Controls;
using dnSpy.Contracts.ToolBars;

[ExportToolBarObject(
    Group = ToolBarConstants.GROUP_APP_TB_MAIN_NAVIGATION,
    Order = 10)]
public sealed class MyToolBarComboBox : ToolBarObjectBase {
    readonly ComboBox comboBox;
    
    public MyToolBarComboBox() {
        comboBox = new ComboBox { Width = 150 };
        comboBox.Items.Add("Option 1");
        comboBox.Items.Add("Option 2");
        comboBox.SelectionChanged += ComboBox_SelectionChanged;
    }
    
    public override object GetUIObject(IToolBarItemContext context, IInputElement commandTarget) {
        return comboBox;
    }
    
    void ComboBox_SelectionChanged(object sender, SelectionChangedEventArgs e) {
        // Handle selection
    }
}
```

### Settings System

Persist extension settings using the `ISettingsService`.

#### Reading and Writing Settings

```csharp
using System;
using System.ComponentModel.Composition;
using dnSpy.Contracts.Settings;

[Export]
public sealed class MySettings {
    readonly ISettingsService settingsService;
    
    // Use a unique GUID for your settings section
    static readonly Guid SETTINGS_GUID = new Guid("12345678-1234-1234-1234-123456789ABC");
    
    [ImportingConstructor]
    public MySettings(ISettingsService settingsService) {
        this.settingsService = settingsService;
        Load();
    }
    
    public string MyStringSetting { get; set; } = "default";
    public int MyIntSetting { get; set; } = 42;
    
    void Load() {
        var section = settingsService.GetOrCreateSection(SETTINGS_GUID);
        MyStringSetting = section.Attribute<string>(nameof(MyStringSetting)) ?? MyStringSetting;
        MyIntSetting = section.Attribute<int?>(nameof(MyIntSetting)) ?? MyIntSetting;
    }
    
    public void Save() {
        var section = settingsService.RecreateSection(SETTINGS_GUID);
        section.Attribute(nameof(MyStringSetting), MyStringSetting);
        section.Attribute(nameof(MyIntSetting), MyIntSetting);
    }
}
```

#### Adding a Settings Page to Options Dialog

```csharp
using System;
using System.ComponentModel.Composition;
using dnSpy.Contracts.Settings.Dialog;

[Export(typeof(IAppSettingsPage))]
public sealed class MySettingsPage : IAppSettingsPage {
    readonly MySettings settings;
    
    public Guid Guid => new Guid("87654321-4321-4321-4321-CBA987654321");
    public double Order => AppSettingsConstants.ORDER_SETTINGS_TAB_MISC + 1;
    public string Title => "My Extension";
    public object UIObject => new MySettingsControl { DataContext = this };
    
    [ImportingConstructor]
    public MySettingsPage(MySettings settings) {
        this.settings = settings;
    }
    
    public void OnClosed() {
        // Called when dialog closes
    }
    
    public void OnApply() {
        settings.Save();
    }
}
```

### Command System

Handle keyboard shortcuts and commands.

#### Registering Keyboard Shortcuts

```csharp
using System.ComponentModel.Composition;
using System.Windows.Input;
using dnSpy.Contracts.Controls;
using dnSpy.Contracts.Extension;
using dnSpy.Contracts.MVVM;

[ExportAutoLoaded]
public sealed class MyCommandLoader : IAutoLoaded {
    public static readonly RoutedCommand MyCommand = new RoutedCommand(
        "MyCommand", 
        typeof(MyCommandLoader));
    
    [ImportingConstructor]
    public MyCommandLoader(IWpfCommandService wpfCommandService) {
        var cmds = wpfCommandService.GetCommands(ControlConstants.GUID_MAINWINDOW);
        
        // Register command handler
        cmds.Add(MyCommand, new RelayCommand(Execute));
        
        // Register keyboard shortcut (Ctrl+Shift+M)
        cmds.Add(MyCommand, ModifierKeys.Control | ModifierKeys.Shift, Key.M);
    }
    
    void Execute(object parameter) {
        // Command executed
    }
}
```

### Tool Windows

Create custom dockable tool windows.

#### Complete Tool Window Example

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel.Composition;
using System.Windows;
using System.Windows.Input;
using dnSpy.Contracts.Controls;
using dnSpy.Contracts.Extension;
using dnSpy.Contracts.Menus;
using dnSpy.Contracts.MVVM;
using dnSpy.Contracts.ToolWindows;
using dnSpy.Contracts.ToolWindows.App;

// Tool window content provider
[Export(typeof(IToolWindowContentProvider))]
public sealed class MyToolWindowProvider : IToolWindowContentProvider {
    readonly Lazy<MyToolWindow> toolWindow;
    
    [ImportingConstructor]
    public MyToolWindowProvider() {
        toolWindow = new Lazy<MyToolWindow>(() => new MyToolWindow());
    }
    
    public IEnumerable<ToolWindowContentInfo> ContentInfos {
        get {
            yield return new ToolWindowContentInfo(
                MyToolWindow.GUID,
                AppToolWindowLocation.DefaultHorizontal,
                order: 0,
                isDefault: false);
        }
    }
    
    public ToolWindowContent GetOrCreate(Guid guid) {
        if (guid == MyToolWindow.GUID)
            return toolWindow.Value;
        return null;
    }
}

// Tool window content
public sealed class MyToolWindow : ToolWindowContent {
    public static readonly Guid GUID = new Guid("AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE");
    
    public override Guid Guid => GUID;
    public override string Title => "My Tool Window";
    public override object UIObject => control;
    public override IInputElement FocusedElement => control.textBox;
    public override FrameworkElement ZoomElement => control;
    
    readonly MyToolWindowControl control;
    
    public MyToolWindow() {
        control = new MyToolWindowControl();
    }
    
    public override void OnVisibilityChanged(ToolWindowContentVisibilityEvent visEvent) {
        // Handle visibility changes
        switch (visEvent) {
            case ToolWindowContentVisibilityEvent.Added:
                // Window added to UI
                break;
            case ToolWindowContentVisibilityEvent.Removed:
                // Window removed from UI
                break;
            case ToolWindowContentVisibilityEvent.Visible:
                // Window became visible
                break;
            case ToolWindowContentVisibilityEvent.Hidden:
                // Window became hidden
                break;
        }
    }
}

// Show tool window command
[ExportAutoLoaded]
public sealed class ShowMyToolWindowCommand : IAutoLoaded {
    public static readonly RoutedCommand ShowCommand = 
        new RoutedCommand("ShowMyToolWindow", typeof(ShowMyToolWindowCommand));
    
    [ImportingConstructor]
    public ShowMyToolWindowCommand(
        IWpfCommandService wpfCommandService,
        IDsToolWindowService toolWindowService) {
        
        var cmds = wpfCommandService.GetCommands(ControlConstants.GUID_MAINWINDOW);
        cmds.Add(ShowCommand, new RelayCommand(a => 
            toolWindowService.Show(MyToolWindow.GUID)));
        cmds.Add(ShowCommand, ModifierKeys.Control | ModifierKeys.Alt, Key.M);
    }
}

// Menu command to show tool window
[ExportMenuItem(
    OwnerGuid = MenuConstants.APP_MENU_VIEW_GUID,
    Header = "My Tool Window",
    InputGestureText = "Ctrl+Alt+M",
    Group = MenuConstants.GROUP_APP_MENU_VIEW_WINDOWS,
    Order = 2000)]
public sealed class ShowMyToolWindowMenuItem : MenuItemCommand {
    public ShowMyToolWindowMenuItem() 
        : base(ShowMyToolWindowCommand.ShowCommand) {
    }
}
```

---

## Debugger APIs

### DbgManager - Core Debugging Interface

The `DbgManager` class is the central interface for all debugging operations.

#### Starting a Debug Session

```csharp
using System.ComponentModel.Composition;
using dnSpy.Contracts.Debugger;

[Export]
public sealed class MyDebugger {
    readonly DbgManager dbgManager;
    
    [ImportingConstructor]
    public MyDebugger(DbgManager dbgManager) {
        this.dbgManager = dbgManager;
        
        // Subscribe to debugging events
        dbgManager.IsDebuggingChanged += DbgManager_IsDebuggingChanged;
        dbgManager.IsRunningChanged += DbgManager_IsRunningChanged;
        dbgManager.ProcessesChanged += DbgManager_ProcessesChanged;
    }
    
    void DbgManager_IsDebuggingChanged(object sender, EventArgs e) {
        if (dbgManager.IsDebugging) {
            // Debugging started
        } else {
            // Debugging stopped
        }
    }
    
    void DbgManager_IsRunningChanged(object sender, EventArgs e) {
        if (dbgManager.IsRunning == true) {
            // All processes are running
        } else if (dbgManager.IsRunning == false) {
            // All processes are paused
        } else {
            // Mixed state: some running, some paused
        }
    }
    
    void DbgManager_ProcessesChanged(object sender, 
        DbgCollectionChangedEventArgs<DbgProcess> e) {
        // Processes added or removed
    }
}
```

#### DbgManager Key Members

**Properties:**
- `DbgDispatcher Dispatcher` - Thread for all debugger operations
- `bool IsDebugging` - True if currently debugging
- `bool? IsRunning` - True/false/null for all running/paused/mixed
- `bool CanRestart` - True if restart is available
- `bool CanDetachWithoutTerminating` - True if can detach cleanly
- `DbgProcess[] Processes` - All debugged processes
- `string[] DebugTags` - Active debug tags
- `DbgCurrentObject<DbgProcess> CurrentProcess` - Current process
- `DbgCurrentObject<DbgRuntime> CurrentRuntime` - Current runtime
- `DbgCurrentObject<DbgThread> CurrentThread` - Current thread

**Methods:**
- `string Start(DebugProgramOptions options)` - Start debugging
- `void Restart()` - Restart debugging
- `void BreakAll()` - Break all processes
- `void RunAll()` - Resume all processes
- `void Run(DbgProcess process)` - Resume specific process
- `void StopDebuggingAll()` - Stop debugging all processes
- `void TerminateAll()` - Terminate all processes
- `void DetachAll()` - Detach from all processes
- `void Close(DbgObject obj)` - Close a debugger object
- `void WriteMessage(string message)` - Write to output window
- `void ShowError(string errorMessage)` - Show error message

**Events:**
- `event EventHandler<DbgMessageEventArgs> Message` - Debug messages
- `event EventHandler IsDebuggingChanged` - Debugging state changed
- `event EventHandler IsRunningChanged` - Running state changed
- `event EventHandler DelayedIsRunningChanged` - Running for a while
- `event EventHandler<ProcessPausedEventArgs> ProcessPaused` - Process paused
- `event EventHandler<DbgCollectionChangedEventArgs<DbgProcess>> ProcessesChanged`
- `event EventHandler<DbgCollectionChangedEventArgs<string>> DebugTagsChanged`
- `event EventHandler<DbgCurrentObjectChangedEventArgs<T>> CurrentProcessChanged`
- `event EventHandler<DbgCurrentObjectChangedEventArgs<T>> CurrentThreadChanged`

### Breakpoints

#### Managing Code Breakpoints

```csharp
using dnSpy.Contracts.Debugger.Breakpoints.Code;
using dnSpy.Contracts.Debugger.Code;

[Export]
public sealed class MyBreakpointManager {
    readonly DbgCodeBreakpointsService breakpointsService;
    
    [ImportingConstructor]
    public MyBreakpointManager(DbgCodeBreakpointsService breakpointsService) {
        this.breakpointsService = breakpointsService;
        breakpointsService.BreakpointsChanged += OnBreakpointsChanged;
        breakpointsService.BreakpointsModified += OnBreakpointsModified;
    }
    
    public void AddBreakpoint(DbgCodeLocation location) {
        var settings = new DbgCodeBreakpointSettings {
            IsEnabled = true,
            Condition = null // Or add condition string
        };
        
        breakpointsService.Add(new DbgCodeBreakpointInfo(location, settings));
    }
    
    public void RemoveAllBreakpoints() {
        breakpointsService.Clear();
    }
    
    void OnBreakpointsChanged(object sender, 
        DbgCollectionChangedEventArgs<DbgCodeBreakpoint> e) {
        // Breakpoints added or removed
    }
    
    void OnBreakpointsModified(object sender, 
        DbgBreakpointsModifiedEventArgs e) {
        // Breakpoint settings modified
    }
}
```

### Call Stack

```csharp
using dnSpy.Contracts.Debugger.CallStack;

[Export]
public sealed class MyCallStackViewer {
    readonly DbgCallStackService callStackService;
    
    [ImportingConstructor]
    public MyCallStackViewer(DbgCallStackService callStackService) {
        this.callStackService = callStackService;
    }
    
    public void ShowCallStack(DbgThread thread) {
        var frames = callStackService.GetFrames(thread);
        foreach (var frame in frames.Frames) {
            // frame.Location - Where in code
            // frame.Module - Module containing code
            // frame.FunctionOffset - Offset in function
        }
    }
}
```

### Expression Evaluation

```csharp
using dnSpy.Contracts.Debugger.Evaluation;

public void EvaluateExpression(DbgEvaluationContext context, string expression) {
    var language = context.Language;
    var evaluator = language.ExpressionEvaluator;
    
    var options = DbgEvaluationOptions.None;
    var evalInfo = new DbgExpressionEvaluationInfo(
        context,
        expression,
        options,
        timeout: TimeSpan.FromSeconds(5));
    
    var result = evaluator.Evaluate(evalInfo);
    if (result.Error != null) {
        // Handle error
    } else {
        var value = result.Value;
        // Use value
    }
}
```

---

## Document and Assembly APIs

### IDsDocument - Document Interface

Documents represent loaded assemblies, PE files, or other files in dnSpy.

#### Working with Documents

```csharp
using dnSpy.Contracts.Documents;

[Export]
public sealed class MyDocumentManager {
    readonly IDsDocumentService documentService;
    
    [ImportingConstructor]
    public MyDocumentManager(IDsDocumentService documentService) {
        this.documentService = documentService;
        documentService.CollectionChanged += OnDocumentsChanged;
    }
    
    void OnDocumentsChanged(object sender, 
        NotifyDocumentCollectionChangedEventArgs e) {
        // Documents added or removed
    }
    
    public void LoadAssembly(string filename) {
        var document = documentService.TryGetOrCreate(
            DsDocumentInfo.CreateDocument(filename));
        if (document != null) {
            // Document loaded successfully
            var moduleDef = document.ModuleDef;
            var assemblyDef = document.AssemblyDef;
        }
    }
    
    public void EnumerateAllTypes() {
        foreach (var document in documentService.GetDocuments()) {
            foreach (var module in document.GetModules<ModuleDef>()) {
                foreach (var type in module.GetTypes()) {
                    // Process type
                }
            }
        }
    }
}
```

#### IDsDocument Members

**Properties:**
- `DsDocumentInfo? SerializedDocument` - Serialization info
- `IDsDocumentNameKey Key` - Unique key for document
- `AssemblyDef AssemblyDef` - Assembly (if .NET assembly)
- `ModuleDef ModuleDef` - Module (if .NET file)
- `IPEImage PEImage` - PE image (if PE file)
- `string Filename` - File path
- `bool IsAutoLoaded` - True if auto-loaded by dnSpy
- `TList<IDsDocument> Children` - Child documents
- `bool ChildrenLoaded` - True if children initialized

### Document Tree View

Interact with the Assembly Explorer tree view.

```csharp
using dnSpy.Contracts.Documents.TreeView;

[Export]
public sealed class MyTreeViewManager {
    readonly IDocumentTreeView documentTreeView;
    
    [ImportingConstructor]
    public MyTreeViewManager(IDocumentTreeView documentTreeView) {
        this.documentTreeView = documentTreeView;
        documentTreeView.SelectionChanged += OnSelectionChanged;
    }
    
    void OnSelectionChanged(object sender, 
        TreeViewSelectionChangedEventArgs e) {
        var nodes = documentTreeView.TreeView.SelectedItems;
        foreach (DocumentTreeNodeData node in nodes) {
            // Process selected node
        }
    }
    
    public void FindAndSelectType(string fullName) {
        var node = documentTreeView.FindNode(fullName);
        if (node != null) {
            documentTreeView.TreeView.SelectItems(new[] { node });
        }
    }
}
```

### Assembly Editing

```csharp
using dnlib.DotNet;
using dnSpy.Contracts.Documents;

public void ModifyAssembly(IDsDocument document) {
    var module = document.ModuleDef;
    if (module == null)
        return;
    
    // Add a new type
    var newType = new TypeDefUser("MyNamespace", "MyClass");
    newType.Attributes = TypeAttributes.Public | TypeAttributes.Class;
    module.Types.Add(newType);
    
    // Add a method
    var method = new MethodDefUser(
        "MyMethod",
        MethodSig.CreateStatic(module.CorLibTypes.Void),
        MethodAttributes.Public | MethodAttributes.Static);
    newType.Methods.Add(method);
    
    // Save the modified assembly
    var writer = new ModuleWriterOptions(module);
    module.Write(document.Filename + ".modified.dll", writer);
}
```

---

## UI Components

### Text Editor Integration

#### Adding Custom References

```csharp
using dnSpy.Contracts.Text;
using dnSpy.Contracts.Text.Editor;

public void AddCustomReferences(ITextView textView) {
    var refs = new List<object>();
    
    // Add custom references that will be shown in the text
    refs.Add(new MyCustomReference {
        Span = new Span(10, 20),
        Data = "Custom data"
    });
    
    textView.Properties[typeof(MyCustomReference)] = refs;
}
```

#### Text Colorization

```csharp
using dnSpy.Contracts.Text.Classification;

[Export(typeof(ITextClassifierProvider))]
[ContentType(ContentTypes.CSharp)]
public sealed class MyTextClassifierProvider : ITextClassifierProvider {
    public ITextClassifier Create(IContentType contentType) {
        return new MyTextClassifier();
    }
}

class MyTextClassifier : ITextClassifier {
    public IEnumerable<TextClassificationTag> GetTags(
        TextClassifierContext context) {
        
        // Return classification tags for colorization
        yield return new TextClassificationTag(
            new Span(0, 10),
            PredefinedTextClassificationTags.Keyword);
    }
}
```

### Output Window

```csharp
using dnSpy.Contracts.Output;

[Export]
public sealed class MyOutputWriter {
    readonly IOutputService outputService;
    IOutputTextPane myPane;
    
    [ImportingConstructor]
    public MyOutputWriter(IOutputService outputService) {
        this.outputService = outputService;
    }
    
    void EnsurePane() {
        if (myPane == null) {
            myPane = outputService.Create(
                new Guid("12345678-1234-1234-1234-123456789012"),
                "My Extension Output");
        }
    }
    
    public void WriteLine(string text) {
        EnsurePane();
        myPane.WriteLine(text);
    }
    
    public void WriteError(string text) {
        EnsurePane();
        myPane.Write(text, OutputColor.Error);
    }
}
```

### Themes and Images

```csharp
using dnSpy.Contracts.Images;

// Using built-in images
public ImageReference GetIcon() {
    return new ImageReference(
        GetType().Assembly,
        "MyExtension.Resources.MyIcon.png");
}

// Or use dnSpy built-in images
public ImageReference GetBuiltInIcon() {
    return DsImages.Assembly;
    // DsImages.Class, DsImages.Method, DsImages.Property, etc.
}
```

---

## Examples

### Example 1: Simple Command Extension

Creates a menu command that shows a message box.

```csharp
using System.Collections.Generic;
using dnSpy.Contracts.App;
using dnSpy.Contracts.Extension;
using dnSpy.Contracts.Menus;

namespace SimpleExtension {
    [ExportExtension]
    public sealed class SimpleExtension : IExtension {
        public ExtensionInfo ExtensionInfo => new ExtensionInfo {
            ShortDescription = "Simple Extension Example"
        };
        
        public IEnumerable<string> MergedResourceDictionaries {
            get { yield break; }
        }
        
        public void OnEvent(ExtensionEvent @event, object obj) { }
    }
    
    [ExportMenuItem(
        OwnerGuid = MenuConstants.APP_MENU_VIEW_GUID,
        Header = "Show Message",
        Group = MenuConstants.GROUP_APP_MENU_VIEW_WINDOWS,
        Order = 9999)]
    public sealed class ShowMessageCommand : MenuItemBase {
        public override void Execute(IMenuItemContext context) {
            MsgBox.Instance.Show("Hello from Simple Extension!");
        }
    }
}
```

### Example 2: Document Analyzer

Analyzes loaded assemblies and displays statistics.

```csharp
using System.ComponentModel.Composition;
using System.Linq;
using dnlib.DotNet;
using dnSpy.Contracts.App;
using dnSpy.Contracts.Documents;
using dnSpy.Contracts.Menus;

[ExportMenuItem(
    OwnerGuid = MenuConstants.APP_MENU_VIEW_GUID,
    Header = "Analyze Assemblies",
    Group = MenuConstants.GROUP_APP_MENU_VIEW_WINDOWS,
    Order = 9998)]
public sealed class AnalyzeAssembliesCommand : MenuItemBase {
    readonly IDsDocumentService documentService;
    
    [ImportingConstructor]
    public AnalyzeAssembliesCommand(IDsDocumentService documentService) {
        this.documentService = documentService;
    }
    
    public override void Execute(IMenuItemContext context) {
        int totalTypes = 0;
        int totalMethods = 0;
        int totalFields = 0;
        
        foreach (var doc in documentService.GetDocuments()) {
            foreach (var module in doc.GetModules<ModuleDef>()) {
                foreach (var type in module.GetTypes()) {
                    totalTypes++;
                    totalMethods += type.Methods.Count;
                    totalFields += type.Fields.Count;
                }
            }
        }
        
        var message = $"Assembly Statistics:\n" +
                     $"Types: {totalTypes}\n" +
                     $"Methods: {totalMethods}\n" +
                     $"Fields: {totalFields}";
        
        MsgBox.Instance.Show(message);
    }
    
    public override bool IsEnabled(IMenuItemContext context) {
        return documentService.GetDocuments().Any();
    }
}
```

### Example 3: Debugger Event Monitor

Monitors debugging events and logs them.

```csharp
using System;
using System.ComponentModel.Composition;
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Extension;
using dnSpy.Contracts.Output;

[ExportAutoLoaded]
public sealed class DebuggerMonitor : IAutoLoaded {
    readonly DbgManager dbgManager;
    readonly IOutputService outputService;
    IOutputTextPane outputPane;
    
    [ImportingConstructor]
    public DebuggerMonitor(DbgManager dbgManager, IOutputService outputService) {
        this.dbgManager = dbgManager;
        this.outputService = outputService;
        
        // Create output pane
        outputPane = outputService.Create(
            new Guid("ABCD1234-5678-90AB-CDEF-1234567890AB"),
            "Debugger Monitor");
        
        // Subscribe to events
        dbgManager.IsDebuggingChanged += OnIsDebuggingChanged;
        dbgManager.IsRunningChanged += OnIsRunningChanged;
        dbgManager.ProcessesChanged += OnProcessesChanged;
        dbgManager.CurrentThreadChanged += OnCurrentThreadChanged;
    }
    
    void OnIsDebuggingChanged(object sender, EventArgs e) {
        outputPane.WriteLine($"[{DateTime.Now:HH:mm:ss}] " +
            $"IsDebugging: {dbgManager.IsDebugging}");
    }
    
    void OnIsRunningChanged(object sender, EventArgs e) {
        outputPane.WriteLine($"[{DateTime.Now:HH:mm:ss}] " +
            $"IsRunning: {dbgManager.IsRunning}");
    }
    
    void OnProcessesChanged(object sender, 
        DbgCollectionChangedEventArgs<DbgProcess> e) {
        if (e.Added) {
            outputPane.WriteLine($"[{DateTime.Now:HH:mm:ss}] " +
                $"Process added: {e.Objects[0].Name} (PID: {e.Objects[0].Id})");
        } else {
            outputPane.WriteLine($"[{DateTime.Now:HH:mm:ss}] " +
                $"Process removed: {e.Objects[0].Name}");
        }
    }
    
    void OnCurrentThreadChanged(object sender, 
        DbgCurrentObjectChangedEventArgs<DbgThread> e) {
        if (e.CurrentChanged && dbgManager.CurrentThread.Current != null) {
            var thread = dbgManager.CurrentThread.Current;
            outputPane.WriteLine($"[{DateTime.Now:HH:mm:ss}] " +
                $"Current thread: {thread.Name} (TID: {thread.Id})");
        }
    }
}
```

### Example 4: Custom Tree Node

Adds custom nodes to the Assembly Explorer.

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel.Composition;
using dnSpy.Contracts.Documents.TreeView;
using dnSpy.Contracts.Images;
using dnSpy.Contracts.TreeView;

[Export(typeof(IDocumentTreeNodeDataProvider))]
public sealed class CustomNodeProvider : IDocumentTreeNodeDataProvider {
    public IEnumerable<DocumentTreeNodeData> Create(
        DocumentTreeNodeDataCreatorContext context) {
        
        // Add custom nodes to assembly nodes
        if (context.OwnerNode is AssemblyDocumentNode asmNode) {
            yield return new CustomNode(asmNode);
        }
    }
}

public sealed class CustomNode : DocumentTreeNodeData {
    readonly AssemblyDocumentNode owner;
    
    public CustomNode(AssemblyDocumentNode owner) {
        this.owner = owner;
    }
    
    public override Guid Guid => new Guid("11111111-2222-3333-4444-555555555555");
    
    public override NodePathName NodePathName => 
        new NodePathName(Guid, "CustomNode");
    
    public override object Text => "Custom Information";
    
    public override ImageReference Icon => DsImages.Reference;
    
    public override IEnumerable<TreeNodeData> CreateChildren() {
        // Add child nodes if needed
        yield break;
    }
    
    protected override void WriteCore(ITextColorWriter output, 
        DocumentNodeWriteOptions options) {
        output.Write("Custom Information Node");
    }
}
```

---

## Additional Resources

### Important Constants

**MenuConstants:**
- `APP_MENU_GUID` - Main application menu
- `CTX_MENU_GUID` - Context menu
- `APP_MENU_FILE_GUID` - File menu
- `APP_MENU_EDIT_GUID` - Edit menu
- `APP_MENU_VIEW_GUID` - View menu
- `APP_MENU_DEBUG_GUID` - Debug menu

**ToolBarConstants:**
- `GROUP_APP_TB_MAIN_NAVIGATION` - Navigation group
- `GROUP_APP_TB_MAIN_OPEN` - Open group
- `GROUP_APP_TB_MAIN_ASMED` - Assembly editor group
- `GROUP_APP_TB_MAIN_DEBUG` - Debug group

**ControlConstants:**
- `GUID_MAINWINDOW` - Main window GUID

### Best Practices

1. **Use MEF for Dependency Injection**: Import services through constructor parameters
2. **Handle Disposal**: Dispose of resources and unsubscribe from events
3. **Thread Safety**: Most debugger operations must be on the debugger dispatcher thread
4. **Use Unique GUIDs**: Generate new GUIDs for all your extension components
5. **Cache Expensive Operations**: Use `IMenuItemContext.GetOrCreateState<T>` for caching
6. **Test with Multiple Scenarios**: Test with different runtimes (.NET Framework, .NET Core, Unity)
7. **Document Your Extension**: Provide clear documentation for users

### Common Pitfalls

1. **Forgetting to Export Types**: Ensure all public types have appropriate `[Export]` attributes
2. **Wrong Thread Context**: Debugger operations must be on dispatcher thread
3. **Not Checking for Null**: Always check if documents, threads, etc. exist
4. **Memory Leaks**: Unsubscribe from events when disposing
5. **Blocking UI**: Long operations should run asynchronously

---

## API Reference Summary

### Core Namespaces

- `dnSpy.Contracts.Extension` - Extension infrastructure
- `dnSpy.Contracts.Menus` - Menu system
- `dnSpy.Contracts.ToolBars` - Toolbar system
- `dnSpy.Contracts.Settings` - Settings persistence
- `dnSpy.Contracts.ToolWindows` - Tool window system
- `dnSpy.Contracts.Command` - Command infrastructure
- `dnSpy.Contracts.Controls` - UI controls
- `dnSpy.Contracts.Documents` - Document/Assembly management
- `dnSpy.Contracts.Documents.TreeView` - Assembly Explorer
- `dnSpy.Contracts.Text` - Text editor integration
- `dnSpy.Contracts.Output` - Output window
- `dnSpy.Contracts.Images` - Image and icon resources

### Debugger Namespaces

- `dnSpy.Contracts.Debugger` - Core debugger infrastructure
- `dnSpy.Contracts.Debugger.Breakpoints` - Breakpoint management
- `dnSpy.Contracts.Debugger.CallStack` - Call stack navigation
- `dnSpy.Contracts.Debugger.Evaluation` - Expression evaluation
- `dnSpy.Contracts.Debugger.Code` - Code location and debugging info
- `dnSpy.Contracts.Debugger.DotNet` - .NET-specific debugging
- `dnSpy.Contracts.Debugger.DotNet.Evaluation` - .NET expression evaluation
- `dnSpy.Contracts.Debugger.DotNet.Code` - .NET code information

### External Dependencies

- **dnlib** - .NET metadata reader/writer (for assembly manipulation)
- **VS MEF** - Managed Extensibility Framework
- **ICSharpCode.Decompiler** - ILSpy decompiler engine
- **Microsoft.CodeAnalysis** - Roslyn compiler services

---

## Support and Contributing

For more information, examples, and support:

- **GitHub**: https://github.com/0xd4d/dnSpy
- **Wiki**: https://github.com/0xd4d/dnSpy/wiki
- **Examples**: See `/Extensions/Examples/` directory in source code
- **License**: GPLv3

---

*This documentation covers dnSpy's public API as of the current version. APIs may change in future releases.*
