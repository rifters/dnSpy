# dnSpy Debugger API Reference

## Table of Contents

1. [Overview](#overview)
2. [DbgManager](#dbgmanager)
3. [Processes and Threads](#processes-and-threads)
4. [Breakpoints](#breakpoints)
5. [Call Stack](#call-stack)
6. [Expression Evaluation](#expression-evaluation)
7. [Step Debugging](#step-debugging)
8. [Exceptions](#exceptions)
9. [Advanced Debugging](#advanced-debugging)
10. [Complete Examples](#complete-examples)

---

## Overview

The dnSpy debugger API provides comprehensive access to debugging functionality for .NET applications. The API is built around the `DbgManager` class and follows a dispatcher-based threading model where all debugger events are raised on a specific thread.

### Key Concepts

- **DbgManager**: Central manager for all debugging operations
- **DbgDispatcher**: Thread dispatcher for debugger operations
- **DbgProcess**: Represents a debugged process
- **DbgRuntime**: Represents a runtime within a process (.NET Framework, .NET Core, etc.)
- **DbgThread**: Represents a thread in a debugged process
- **DbgModule**: Represents a loaded module (assembly)
- **DbgAppDomain**: Represents an application domain

### Threading Model

All debugger events are raised on the debugger dispatcher thread. Access `DbgManager.Dispatcher` to get the dispatcher and ensure thread-safe operations:

```csharp
dbgManager.Dispatcher.BeginInvoke(() => {
    // Debugger operation on correct thread
});
```

---

## DbgManager

The `DbgManager` abstract class is the entry point for all debugging operations.

### Properties

#### State Properties

```csharp
// Check if currently debugging
public abstract bool IsDebugging { get; }

// Check running state: true = all running, false = all paused, null = mixed
public abstract bool? IsRunning { get; }

// Check if restart is available
public abstract bool CanRestart { get; }

// Check if can detach without terminating
public abstract bool CanDetachWithoutTerminating { get; }
```

#### Current Objects

```csharp
// Current process (user selected or break context)
public abstract DbgCurrentObject<DbgProcess> CurrentProcess { get; }

// Current runtime
public abstract DbgCurrentObject<DbgRuntime> CurrentRuntime { get; }

// Current thread
public abstract DbgCurrentObject<DbgThread> CurrentThread { get; }
```

The `DbgCurrentObject<T>` class provides:
- `T Current` - Currently selected object
- `T Break` - Object that caused the break

#### Collections

```csharp
// All debugged processes
public abstract DbgProcess[] Processes { get; }

// Active debug tags
public abstract string[] DebugTags { get; }

// Debugger dispatcher thread
public abstract DbgDispatcher Dispatcher { get; }
```

### Methods

#### Starting and Stopping

```csharp
// Start debugging
// Returns error message on failure, null on success
public abstract string Start(DebugProgramOptions options);

// Example usage
var options = new DebugProgramOptions(
    filename: @"C:\path\to\program.exe",
    commandLine: "arg1 arg2",
    currentDirectory: @"C:\path\to",
    pauseOnException: false);
    
string error = dbgManager.Start(options);
if (error != null) {
    Console.WriteLine($"Failed to start: {error}");
}

// Restart current debug session
public abstract void Restart();

// Stop all debugging
public abstract void StopDebuggingAll();

// Terminate all processes
public abstract void TerminateAll();

// Detach from all processes
public abstract void DetachAll();
```

#### Execution Control

```csharp
// Break all processes
public abstract void BreakAll();

// Resume all processes
public abstract void RunAll();

// Resume specific process
public abstract void Run(DbgProcess process);
```

#### Utilities

```csharp
// Write message to output window
public abstract void WriteMessage(string message);

// Show error to user
public void ShowError(string errorMessage);

// Write message with specific kind
public abstract void WriteMessage(string messageKind, string message);

// Close a debugger object
public abstract void Close(DbgObject obj);
public abstract void Close(IEnumerable<DbgObject> objs);

// Check if runtime can be debugged
public abstract bool CanDebugRuntime(int pid, RuntimeId rid);
```

### Events

```csharp
// Raised when IsDebugging changes
public abstract event EventHandler IsDebuggingChanged;

// Raised when IsRunning changes
public abstract event EventHandler IsRunningChanged;

// Raised when processes have been running for a while
public abstract event EventHandler DelayedIsRunningChanged;

// Raised when a process pauses
public abstract event EventHandler<ProcessPausedEventArgs> ProcessPaused;

// Raised when processes collection changes
public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgProcess>> 
    ProcessesChanged;

// Raised when current process changes
public abstract event EventHandler<DbgCurrentObjectChangedEventArgs<DbgProcess>> 
    CurrentProcessChanged;

// Raised when current thread changes
public abstract event EventHandler<DbgCurrentObjectChangedEventArgs<DbgThread>> 
    CurrentThreadChanged;

// Raised for debug messages
public abstract event EventHandler<DbgMessageEventArgs> Message;

// Raised when modules are refreshed (e.g., decrypted)
public abstract event EventHandler<ModulesRefreshedEventArgs> ModulesRefreshed;

// Raised for manager messages
public abstract event EventHandler<DbgManagerMessageEventArgs> DbgManagerMessage;

// Raised when debug tags change
public abstract event EventHandler<DbgCollectionChangedEventArgs<string>> 
    DebugTagsChanged;
```

### Example: Complete Debugger Monitor

```csharp
using System;
using System.ComponentModel.Composition;
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Extension;

[ExportAutoLoaded]
public sealed class DebuggerMonitor : IAutoLoaded {
    readonly DbgManager dbgManager;
    
    [ImportingConstructor]
    public DebuggerMonitor(DbgManager dbgManager) {
        this.dbgManager = dbgManager;
        
        // Subscribe to all important events
        dbgManager.IsDebuggingChanged += OnIsDebuggingChanged;
        dbgManager.IsRunningChanged += OnIsRunningChanged;
        dbgManager.ProcessesChanged += OnProcessesChanged;
        dbgManager.CurrentThreadChanged += OnCurrentThreadChanged;
        dbgManager.Message += OnMessage;
        dbgManager.ProcessPaused += OnProcessPaused;
    }
    
    void OnIsDebuggingChanged(object sender, EventArgs e) {
        Console.WriteLine($"IsDebugging: {dbgManager.IsDebugging}");
        
        if (dbgManager.IsDebugging) {
            // Debugging started
            Console.WriteLine($"Process count: {dbgManager.Processes.Length}");
        } else {
            // Debugging stopped
            Console.WriteLine("All processes terminated");
        }
    }
    
    void OnIsRunningChanged(object sender, EventArgs e) {
        string state = dbgManager.IsRunning switch {
            true => "All Running",
            false => "All Paused",
            null => "Mixed State"
        };
        Console.WriteLine($"Running State: {state}");
    }
    
    void OnProcessesChanged(object sender, 
        DbgCollectionChangedEventArgs<DbgProcess> e) {
        
        if (e.Added) {
            foreach (var process in e.Objects) {
                Console.WriteLine($"Process Added: {process.Name} " +
                    $"(PID: {process.Id})");
            }
        } else {
            foreach (var process in e.Objects) {
                Console.WriteLine($"Process Removed: {process.Name}");
            }
        }
    }
    
    void OnCurrentThreadChanged(object sender, 
        DbgCurrentObjectChangedEventArgs<DbgThread> e) {
        
        if (e.CurrentChanged) {
            var thread = dbgManager.CurrentThread.Current;
            if (thread != null) {
                Console.WriteLine($"Current Thread: {thread.UIName} " +
                    $"(TID: {thread.Id})");
            }
        }
    }
    
    void OnMessage(object sender, DbgMessageEventArgs e) {
        Console.WriteLine($"Debug Message: {e.Message.Kind}");
    }
    
    void OnProcessPaused(object sender, ProcessPausedEventArgs e) {
        Console.WriteLine($"Process Paused: {e.Process.Name}");
        if (e.Thread != null) {
            Console.WriteLine($"  Thread: {e.Thread.UIName}");
        }
    }
}
```

---

## Processes and Threads

### DbgProcess

Represents a debugged process.

```csharp
public abstract class DbgProcess : DbgObject {
    // Process ID
    public abstract int Id { get; }
    
    // Process name
    public abstract string Name { get; }
    
    // Process filename
    public abstract string Filename { get; }
    
    // Working directory
    public abstract string WorkingDirectory { get; }
    
    // Command line
    public abstract string CommandLine { get; }
    
    // Machine architecture
    public abstract DbgArchitecture Architecture { get; }
    
    // Operating system (Windows, Linux, macOS)
    public abstract string OperatingSystem { get; }
    
    // All runtimes in this process
    public abstract DbgRuntime[] Runtimes { get; }
    
    // true if process has exited
    public abstract bool HasExited { get; }
    
    // Exit code (valid only if HasExited is true)
    public abstract int? ExitCode { get; }
    
    // Current state
    public abstract DbgProcessState State { get; }
    
    // Events
    public abstract event EventHandler HasExitedChanged;
    public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgRuntime>> 
        RuntimesChanged;
    public abstract event EventHandler DbgStateChanged;
}
```

### DbgThread

Represents a thread in a debugged process.

```csharp
public abstract class DbgThread : DbgObject {
    // Runtime this thread belongs to
    public abstract DbgRuntime Runtime { get; }
    
    // Thread ID
    public abstract ulong Id { get; }
    
    // Managed thread ID (for .NET threads)
    public abstract ulong? ManagedId { get; }
    
    // Thread name
    public abstract string Name { get; }
    
    // UI-friendly name
    public abstract string UIName { get; }
    
    // Thread kind (see PredefinedThreadKinds)
    public abstract string Kind { get; }
    
    // AppDomain (if applicable)
    public abstract DbgAppDomain AppDomain { get; }
    
    // Current state
    public abstract DbgThreadState State { get; }
    
    // Suspend count
    public abstract int SuspendedCount { get; }
    
    // Events
    public abstract event EventHandler NameChanged;
    public abstract event EventHandler AppDomainChanged;
    public abstract event EventHandler DbgStateChanged;
}
```

### DbgRuntime

Represents a runtime (CLR) within a process.

```csharp
public abstract class DbgRuntime : DbgObject {
    // Process this runtime belongs to
    public abstract DbgProcess Process { get; }
    
    // Runtime ID
    public abstract RuntimeId Id { get; }
    
    // Runtime GUID (e.g., PredefinedDbgRuntimeGuids.DotNetFramework)
    public abstract Guid Guid { get; }
    
    // Runtime kind GUID
    public abstract Guid RuntimeKindGuid { get; }
    
    // Runtime name
    public abstract string Name { get; }
    
    // All modules loaded in this runtime
    public abstract DbgModule[] Modules { get; }
    
    // All threads in this runtime
    public abstract DbgThread[] Threads { get; }
    
    // All app domains in this runtime
    public abstract DbgAppDomain[] AppDomains { get; }
    
    // true if runtime has exited
    public abstract bool HasExited { get; }
    
    // Runtime tags (see PredefinedDbgRuntimeTags)
    public abstract string[] Tags { get; }
    
    // Events
    public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgModule>> 
        ModulesChanged;
    public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgThread>> 
        ThreadsChanged;
    public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgAppDomain>> 
        AppDomainsChanged;
    public abstract event EventHandler HasExitedChanged;
}
```

### Example: Process and Thread Enumeration

```csharp
using dnSpy.Contracts.Debugger;

public void EnumerateProcessesAndThreads(DbgManager dbgManager) {
    foreach (var process in dbgManager.Processes) {
        Console.WriteLine($"Process: {process.Name} (PID: {process.Id})");
        Console.WriteLine($"  Filename: {process.Filename}");
        Console.WriteLine($"  Architecture: {process.Architecture}");
        Console.WriteLine($"  State: {process.State}");
        
        foreach (var runtime in process.Runtimes) {
            Console.WriteLine($"  Runtime: {runtime.Name}");
            Console.WriteLine($"    Modules: {runtime.Modules.Length}");
            
            foreach (var thread in runtime.Threads) {
                Console.WriteLine($"    Thread: {thread.UIName} " +
                    $"(TID: {thread.Id}, ManagedID: {thread.ManagedId})");
                Console.WriteLine($"      Kind: {thread.Kind}");
                Console.WriteLine($"      State: {thread.State}");
            }
        }
    }
}
```

---

## Breakpoints

### DbgCodeBreakpointsService

Manages code breakpoints.

```csharp
[Export]
public sealed class BreakpointManager {
    readonly DbgCodeBreakpointsService breakpointsService;
    
    [ImportingConstructor]
    public BreakpointManager(DbgCodeBreakpointsService breakpointsService) {
        this.breakpointsService = breakpointsService;
        
        // Subscribe to events
        breakpointsService.BreakpointsChanged += OnBreakpointsChanged;
        breakpointsService.BreakpointsModified += OnBreakpointsModified;
        breakpointsService.BoundBreakpointsMessageChanged += OnBoundMessageChanged;
    }
    
    void OnBreakpointsChanged(object sender, 
        DbgCollectionChangedEventArgs<DbgCodeBreakpoint> e) {
        if (e.Added) {
            Console.WriteLine($"Breakpoint added: {e.Objects[0]}");
        } else {
            Console.WriteLine($"Breakpoint removed: {e.Objects[0]}");
        }
    }
    
    void OnBreakpointsModified(object sender, 
        DbgBreakpointsModifiedEventArgs e) {
        Console.WriteLine($"Breakpoint modified");
    }
    
    void OnBoundMessageChanged(object sender, 
        BoundBreakpointsMessageChangedEventArgs e) {
        // Breakpoint bound/unbound message changed
    }
}
```

### Creating Breakpoints

```csharp
using dnSpy.Contracts.Debugger.Breakpoints.Code;
using dnSpy.Contracts.Debugger.Code;

public void AddBreakpoint(DbgCodeBreakpointsService service, 
    DbgCodeLocation location) {
    
    var settings = new DbgCodeBreakpointSettings {
        IsEnabled = true,
        HitCount = null, // No hit count filter
        Condition = null, // No condition
        Labels = Array.Empty<string>()
    };
    
    var info = new DbgCodeBreakpointInfo(location, settings);
    var breakpoint = service.Add(info);
}

public void AddConditionalBreakpoint(DbgCodeBreakpointsService service,
    DbgCodeLocation location, string condition) {
    
    var settings = new DbgCodeBreakpointSettings {
        IsEnabled = true,
        Condition = new DbgCodeBreakpointCondition {
            Condition = condition,
            Kind = DbgCodeBreakpointConditionKind.WhenTrue
        }
    };
    
    var info = new DbgCodeBreakpointInfo(location, settings);
    service.Add(info);
}

public void AddHitCountBreakpoint(DbgCodeBreakpointsService service,
    DbgCodeLocation location, int hitCount) {
    
    var settings = new DbgCodeBreakpointSettings {
        IsEnabled = true,
        HitCount = new DbgCodeBreakpointHitCount {
            Count = hitCount,
            Kind = DbgCodeBreakpointHitCountKind.Equals
        }
    };
    
    var info = new DbgCodeBreakpointInfo(location, settings);
    service.Add(info);
}
```

### Managing Breakpoints

```csharp
public class BreakpointOperations {
    readonly DbgCodeBreakpointsService service;
    
    public BreakpointOperations(DbgCodeBreakpointsService service) {
        this.service = service;
    }
    
    // Get all breakpoints
    public DbgCodeBreakpoint[] GetAllBreakpoints() {
        return service.Breakpoints;
    }
    
    // Enable/disable breakpoint
    public void SetEnabled(DbgCodeBreakpoint breakpoint, bool enabled) {
        var settings = breakpoint.Settings;
        settings.IsEnabled = enabled;
        service.Modify(breakpoint, settings);
    }
    
    // Remove breakpoint
    public void Remove(DbgCodeBreakpoint breakpoint) {
        service.Remove(breakpoint);
    }
    
    // Remove all breakpoints
    public void ClearAll() {
        service.Clear();
    }
    
    // Get breakpoints at location
    public DbgCodeBreakpoint[] GetBreakpointsAt(DbgCodeLocation location) {
        return service.Breakpoints
            .Where(bp => bp.Location.Equals(location))
            .ToArray();
    }
}
```

### Breakpoint Events

```csharp
// When breakpoint is hit
dbgManager.Message += (sender, e) => {
    if (e.Message.Kind == DbgMessageKind.Breakpoint) {
        var bp = e.Message.GetBreakpoint();
        if (bp != null) {
            Console.WriteLine($"Breakpoint hit: {bp.Location}");
        }
    }
};
```

---

## Call Stack

### DbgCallStackService

Provides access to call stacks.

```csharp
using dnSpy.Contracts.Debugger.CallStack;

[Export]
public sealed class CallStackViewer {
    readonly DbgCallStackService callStackService;
    
    [ImportingConstructor]
    public CallStackViewer(DbgCallStackService callStackService) {
        this.callStackService = callStackService;
    }
    
    public void ShowCallStack(DbgThread thread) {
        var frames = callStackService.GetFrames(thread);
        
        Console.WriteLine($"Call Stack for Thread {thread.UIName}:");
        for (int i = 0; i < frames.Frames.Length; i++) {
            var frame = frames.Frames[i];
            Console.WriteLine($"  #{i}: {FormatFrame(frame)}");
        }
    }
    
    string FormatFrame(DbgStackFrame frame) {
        var location = frame.Location;
        if (location != null) {
            return $"{location} at {frame.Module?.ModuleName ?? "???"}";
        }
        return $"<Unknown> at {frame.Module?.ModuleName ?? "???"}";
    }
}
```

### DbgStackFrame

Represents a stack frame.

```csharp
public abstract class DbgStackFrame : DbgObject {
    // Runtime this frame belongs to
    public abstract DbgRuntime Runtime { get; }
    
    // Thread
    public abstract DbgThread Thread { get; }
    
    // Module containing the code
    public abstract DbgModule Module { get; }
    
    // Code location
    public abstract DbgCodeLocation Location { get; }
    
    // Function offset
    public abstract uint FunctionOffset { get; }
    
    // Function token (metadata token)
    public abstract uint FunctionToken { get; }
    
    // Frame index (0 = top frame)
    public abstract uint Index { get; }
    
    // true if this is a special frame (e.g., runtime transition)
    public abstract bool IsSpecialFrame { get; }
}
```

### Advanced Call Stack Operations

```csharp
public class AdvancedCallStackOperations {
    readonly DbgCallStackService service;
    readonly DbgManager dbgManager;
    
    public AdvancedCallStackOperations(
        DbgCallStackService service,
        DbgManager dbgManager) {
        
        this.service = service;
        this.dbgManager = dbgManager;
    }
    
    // Get current call stack
    public DbgStackFrame[] GetCurrentCallStack() {
        var thread = dbgManager.CurrentThread.Current;
        if (thread == null)
            return Array.Empty<DbgStackFrame>();
        
        var frames = service.GetFrames(thread);
        return frames.Frames;
    }
    
    // Find frames by module
    public DbgStackFrame[] FindFramesByModule(DbgThread thread, string moduleName) {
        var frames = service.GetFrames(thread);
        return frames.Frames
            .Where(f => f.Module?.ModuleName.Equals(moduleName, 
                StringComparison.OrdinalIgnoreCase) == true)
            .ToArray();
    }
    
    // Get frame at specific index
    public DbgStackFrame GetFrame(DbgThread thread, int index) {
        var frames = service.GetFrames(thread);
        if (index >= 0 && index < frames.Frames.Length)
            return frames.Frames[index];
        return null;
    }
}
```

---

## Expression Evaluation

### DbgLanguageService and Evaluation

```csharp
using dnSpy.Contracts.Debugger.Evaluation;

[Export]
public sealed class ExpressionEvaluator {
    readonly DbgLanguageService languageService;
    
    [ImportingConstructor]
    public ExpressionEvaluator(DbgLanguageService languageService) {
        this.languageService = languageService;
    }
    
    public DbgValue EvaluateExpression(
        DbgEvaluationContext context,
        string expression) {
        
        var language = context.Language;
        var evaluator = language.ExpressionEvaluator;
        
        var evalInfo = new DbgExpressionEvaluationInfo(
            context,
            expression,
            DbgEvaluationOptions.None,
            timeout: TimeSpan.FromSeconds(5));
        
        var result = evaluator.Evaluate(evalInfo);
        
        if (result.Error != null) {
            Console.WriteLine($"Error: {result.Error}");
            return null;
        }
        
        return result.Value;
    }
    
    public string FormatValue(DbgValue value, DbgEvaluationContext context) {
        var formatter = context.Language.Formatter;
        var output = new StringBuilderTextColorOutput();
        
        formatter.FormatValue(
            new DbgEvaluationInfo(context, CancellationToken.None),
            output,
            value,
            new DbgValueFormatterOptions(),
            CancellationToken.None);
        
        return output.ToString();
    }
}
```

### Creating Evaluation Context

```csharp
public DbgEvaluationContext CreateEvaluationContext(
    DbgStackFrame frame,
    DbgLanguageService languageService) {
    
    // Get the language for the frame
    var language = languageService.GetLanguage(frame.Runtime);
    
    // Create evaluation context
    var context = language.CreateContext(
        frame,
        new DbgLanguageDebugInfo(),
        DbgEvaluationContextOptions.None);
    
    return context;
}
```

### Value Nodes

```csharp
using dnSpy.Contracts.Debugger.Evaluation;

public void DisplayLocals(DbgEvaluationContext context) {
    var valueNodeProvider = context.Language.ValueNodeProvider;
    
    // Get local variables
    var options = DbgValueNodeEvaluationOptions.None;
    var nodes = valueNodeProvider.GetLocals(
        new DbgEvaluationInfo(context, CancellationToken.None),
        options,
        CancellationToken.None);
    
    foreach (var node in nodes) {
        Console.WriteLine($"{node.Name} = {node.ValueText}");
        
        // Get children if it's an object
        if (node.ChildCount > 0) {
            var children = node.GetChildren(
                new DbgEvaluationInfo(context, CancellationToken.None),
                0,
                int.MaxValue,
                options,
                CancellationToken.None);
            
            foreach (var child in children) {
                Console.WriteLine($"  {child.Name} = {child.ValueText}");
            }
        }
        
        node.Dispose();
    }
}
```

---

## Step Debugging

### DbgCodeStepperService

```csharp
using dnSpy.Contracts.Debugger.Steppers;

[Export]
public sealed class SteppingController {
    readonly DbgManager dbgManager;
    
    [ImportingConstructor]
    public SteppingController(DbgManager dbgManager) {
        this.dbgManager = dbgManager;
    }
    
    // Step into
    public void StepInto() {
        var thread = dbgManager.CurrentThread.Current;
        if (thread == null)
            return;
        
        thread.CreateStepper().StepInto();
    }
    
    // Step over
    public void StepOver() {
        var thread = dbgManager.CurrentThread.Current;
        if (thread == null)
            return;
        
        thread.CreateStepper().StepOver();
    }
    
    // Step out
    public void StepOut() {
        var thread = dbgManager.CurrentThread.Current;
        if (thread == null)
            return;
        
        thread.CreateStepper().StepOut();
    }
    
    // Run to cursor
    public void RunToCursor(DbgCodeLocation location) {
        var thread = dbgManager.CurrentThread.Current;
        if (thread == null)
            return;
        
        var stepper = thread.CreateStepper();
        stepper.Step(new DbgCodeStepperStepInfo {
            Kind = DbgCodeStepKind.StepUntil,
            Location = location
        });
    }
}
```

---

## Exceptions

### Exception Handling Configuration

```csharp
using dnSpy.Contracts.Debugger.Exceptions;

[Export]
public sealed class ExceptionManager {
    readonly DbgExceptionSettingsService exceptionSettings;
    
    [ImportingConstructor]
    public ExceptionManager(DbgExceptionSettingsService exceptionSettings) {
        this.exceptionSettings = exceptionSettings;
        exceptionSettings.SettingsChanged += OnSettingsChanged;
    }
    
    // Break on all exceptions
    public void BreakOnAllExceptions() {
        var settings = exceptionSettings.Settings;
        
        foreach (var category in settings.ExceptionCategories) {
            var modified = category with {
                BreakOnFirstChance = true
            };
            exceptionSettings.Modify(category, modified);
        }
    }
    
    // Break on specific exception
    public void BreakOnException(string exceptionName) {
        var settings = exceptionSettings.Settings;
        
        // Find or create exception definition
        var exDef = settings.ExceptionDefinitions
            .FirstOrDefault(ex => ex.Name == exceptionName);
        
        if (exDef != null) {
            var modified = exDef with {
                BreakOnFirstChance = true
            };
            exceptionSettings.Modify(exDef, modified);
        }
    }
    
    void OnSettingsChanged(object sender, EventArgs e) {
        // Exception settings changed
    }
}
```

---

## Advanced Debugging

### Module Events

```csharp
public void MonitorModules(DbgRuntime runtime) {
    runtime.ModulesChanged += (sender, e) => {
        if (e.Added) {
            foreach (var module in e.Objects) {
                Console.WriteLine($"Module Loaded: {module.ModuleName}");
                Console.WriteLine($"  Address: 0x{module.Address:X}");
                Console.WriteLine($"  Size: {module.Size} bytes");
                Console.WriteLine($"  IsDynamic: {module.IsDynamic}");
                Console.WriteLine($"  IsInMemory: {module.IsInMemory}");
            }
        } else {
            foreach (var module in e.Objects) {
                Console.WriteLine($"Module Unloaded: {module.ModuleName}");
            }
        }
    };
}
```

### Memory Access

```csharp
using dnSpy.Contracts.Debugger;

public byte[] ReadProcessMemory(
    DbgProcess process,
    ulong address,
    int size) {
    
    var buffer = new byte[size];
    int bytesRead = process.ReadMemory(address, buffer, 0, size);
    
    if (bytesRead != size) {
        Console.WriteLine($"Warning: Only read {bytesRead} of {size} bytes");
    }
    
    return buffer;
}

public void WriteProcessMemory(
    DbgProcess process,
    ulong address,
    byte[] data) {
    
    int bytesWritten = process.WriteMemory(address, data, 0, data.Length);
    
    if (bytesWritten != data.Length) {
        Console.WriteLine($"Warning: Only wrote {bytesWritten} of {data.Length} bytes");
    }
}
```

---

## Complete Examples

### Example 1: Auto-Break on Main

```csharp
using System;
using System.ComponentModel.Composition;
using System.Linq;
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Debugger.Breakpoints.Code;
using dnSpy.Contracts.Debugger.DotNet.Code;
using dnSpy.Contracts.Extension;

[ExportAutoLoaded]
public sealed class AutoBreakOnMain : IAutoLoaded {
    readonly DbgManager dbgManager;
    readonly DbgCodeBreakpointsService breakpointsService;
    
    [ImportingConstructor]
    public AutoBreakOnMain(
        DbgManager dbgManager,
        DbgCodeBreakpointsService breakpointsService) {
        
        this.dbgManager = dbgManager;
        this.breakpointsService = breakpointsService;
        
        dbgManager.ProcessesChanged += OnProcessesChanged;
    }
    
    void OnProcessesChanged(object sender, 
        DbgCollectionChangedEventArgs<DbgProcess> e) {
        
        if (!e.Added)
            return;
        
        foreach (var process in e.Objects) {
            foreach (var runtime in process.Runtimes) {
                runtime.ModulesChanged += (s, me) => {
                    if (me.Added)
                        TryBreakOnMain(me.Objects);
                };
            }
        }
    }
    
    void TryBreakOnMain(DbgModule[] modules) {
        foreach (var module in modules) {
            // Look for Main method
            var mainLocation = FindMainMethod(module);
            if (mainLocation != null) {
                var settings = new DbgCodeBreakpointSettings {
                    IsEnabled = true
                };
                
                var info = new DbgCodeBreakpointInfo(mainLocation, settings);
                breakpointsService.Add(info);
                
                Console.WriteLine($"Added breakpoint at Main in {module.ModuleName}");
            }
        }
    }
    
    DbgCodeLocation FindMainMethod(DbgModule module) {
        // Implementation depends on your needs
        // Would use DbgDotNetCodeLocation to create location
        return null;
    }
}
```

### Example 2: Variable Logger

```csharp
using System;
using System.ComponentModel.Composition;
using System.Threading;
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Debugger.CallStack;
using dnSpy.Contracts.Debugger.Evaluation;
using dnSpy.Contracts.Extension;

[ExportAutoLoaded]
public sealed class VariableLogger : IAutoLoaded {
    readonly DbgManager dbgManager;
    readonly DbgCallStackService callStackService;
    readonly DbgLanguageService languageService;
    
    [ImportingConstructor]
    public VariableLogger(
        DbgManager dbgManager,
        DbgCallStackService callStackService,
        DbgLanguageService languageService) {
        
        this.dbgManager = dbgManager;
        this.callStackService = callStackService;
        this.languageService = languageService;
        
        dbgManager.ProcessPaused += OnProcessPaused;
    }
    
    void OnProcessPaused(object sender, ProcessPausedEventArgs e) {
        if (e.Thread == null)
            return;
        
        LogVariables(e.Thread);
    }
    
    void LogVariables(DbgThread thread) {
        var frames = callStackService.GetFrames(thread);
        if (frames.Frames.Length == 0)
            return;
        
        var topFrame = frames.Frames[0];
        var language = languageService.GetLanguage(thread.Runtime);
        
        var context = language.CreateContext(
            topFrame,
            new DbgLanguageDebugInfo(),
            DbgEvaluationContextOptions.None);
        
        try {
            var valueNodeProvider = language.ValueNodeProvider;
            var evalInfo = new DbgEvaluationInfo(context, CancellationToken.None);
            
            var locals = valueNodeProvider.GetLocals(
                evalInfo,
                DbgValueNodeEvaluationOptions.None,
                CancellationToken.None);
            
            Console.WriteLine($"\n=== Variables at {topFrame.Location} ===");
            
            foreach (var local in locals) {
                Console.WriteLine($"{local.Name} = {local.ValueText}");
                local.Dispose();
            }
        }
        finally {
            context?.Close(dbgManager.Dispatcher);
        }
    }
}
```

### Example 3: Performance Profiler

```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel.Composition;
using System.Diagnostics;
using System.Linq;
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Extension;

[ExportAutoLoaded]
public sealed class PerformanceProfiler : IAutoLoaded {
    readonly DbgManager dbgManager;
    readonly Dictionary<string, MethodProfile> methodProfiles = 
        new Dictionary<string, MethodProfile>();
    
    [ImportingConstructor]
    public PerformanceProfiler(DbgManager dbgManager) {
        this.dbgManager = dbgManager;
        
        dbgManager.IsRunningChanged += OnIsRunningChanged;
        dbgManager.DelayedIsRunningChanged += OnDelayedIsRunningChanged;
    }
    
    void OnIsRunningChanged(object sender, EventArgs e) {
        if (dbgManager.IsRunning == false) {
            // Paused - record timestamp
            RecordPauseEvent();
        } else if (dbgManager.IsRunning == true) {
            // Running - calculate time
            CalculateRunTime();
        }
    }
    
    void OnDelayedIsRunningChanged(object sender, EventArgs e) {
        // Process has been running for a while
        if (dbgManager.IsRunning == true) {
            // Good time to show periodic stats
            ShowStats();
        }
    }
    
    void RecordPauseEvent() {
        // Record pause event with current location
    }
    
    void CalculateRunTime() {
        // Calculate how long process ran
    }
    
    void ShowStats() {
        Console.WriteLine("\n=== Performance Stats ===");
        var sorted = methodProfiles
            .OrderByDescending(kvp => kvp.Value.TotalTime)
            .Take(10);
        
        foreach (var kvp in sorted) {
            Console.WriteLine($"{kvp.Key}: {kvp.Value.TotalTime.TotalMilliseconds:F2}ms " +
                $"({kvp.Value.CallCount} calls)");
        }
    }
    
    class MethodProfile {
        public TimeSpan TotalTime { get; set; }
        public int CallCount { get; set; }
    }
}
```

---

## Best Practices

### Threading

- Always use `dbgManager.Dispatcher` for debugger operations
- Subscribe and unsubscribe from events properly
- Use `Dispatcher.BeginInvoke()` when calling from other threads

### Resource Management

- Always dispose `DbgEvaluationContext` when done
- Call `Close()` on `DbgObject` instances when no longer needed
- Unsubscribe from events to prevent memory leaks

### Error Handling

```csharp
try {
    var result = evaluator.Evaluate(evalInfo);
    if (result.Error != null) {
        Console.WriteLine($"Evaluation error: {result.Error}");
        return;
    }
    // Use result.Value
}
catch (Exception ex) {
    Console.WriteLine($"Exception: {ex.Message}");
}
```

### Performance

- Cache expensive lookups
- Use events instead of polling
- Limit evaluation timeouts to reasonable values
- Batch operations when possible

---

*For more information, see the main [API Documentation](API_DOCUMENTATION.md) and example extensions.*
