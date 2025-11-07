# .NET-Specific Debugger API Reference

## Overview

The `dnSpy.Contracts.Debugger.DotNet` namespace provides .NET-specific debugging functionality built on top of the core debugger API. This includes specialized evaluation, code location, and metadata access for .NET applications.

## Table of Contents

1. [.NET Runtimes](#net-runtimes)
2. [.NET Code Locations](#net-code-locations)
3. [.NET Expression Evaluation](#net-expression-evaluation)
4. [.NET Values](#net-values)
5. [Metadata Access](#metadata-access)
6. [Decompiler Integration](#decompiler-integration)
7. [Examples](#examples)

---

## .NET Runtimes

### IDbgDotNetRuntime

Extension interface for .NET-specific runtime operations.

```csharp
using dnSpy.Contracts.Debugger.DotNet.Evaluation;

public interface IDbgDotNetRuntime {
    // Get reflection objects for .NET types
    DmdAppDomain GetReflectionAppDomain();
    
    // Create .NET values
    DbgDotNetValueResult CreateValue(object value);
    
    // Load assemblies
    DmdAssembly LoadAssembly(string assemblyName);
}
```

### Accessing .NET Runtime

```csharp
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Debugger.DotNet;

public IDbgDotNetRuntime GetDotNetRuntime(DbgRuntime runtime) {
    return runtime.GetDotNetRuntime();
}

// Example usage
var dotNetRuntime = runtime.GetDotNetRuntime();
if (dotNetRuntime != null) {
    var appDomain = dotNetRuntime.GetReflectionAppDomain();
    // Work with reflection metadata
}
```

---

## .NET Code Locations

### DbgDotNetCodeLocation

Represents a location in .NET code.

```csharp
using dnSpy.Contracts.Debugger.DotNet.Code;

public sealed class DbgDotNetCodeLocation : DbgCodeLocation {
    // Module containing the code
    public DbgModule Module { get; }
    
    // Method token
    public uint Token { get; }
    
    // IL offset within the method
    public uint Offset { get; }
    
    // Native code location (if available)
    public DbgNativeCodeLocation NativeLocation { get; }
}
```

### Creating Code Locations

```csharp
using dnSpy.Contracts.Debugger.Code;
using dnSpy.Contracts.Debugger.DotNet.Code;

[Export]
public sealed class CodeLocationFactory {
    readonly DbgDotNetCodeLocationFactory factory;
    
    [ImportingConstructor]
    public CodeLocationFactory(DbgDotNetCodeLocationFactory factory) {
        this.factory = factory;
    }
    
    // Create location by method token and IL offset
    public DbgCodeLocation CreateLocation(
        DbgModule module,
        uint token,
        uint ilOffset) {
        
        return factory.Create(module, token, ilOffset);
    }
    
    // Create location from method and offset
    public DbgCodeLocation CreateLocation(
        DbgModule module,
        DmdMethodBase method,
        uint ilOffset) {
        
        return factory.Create(module, method.MetadataToken, ilOffset);
    }
}
```

### IL Offset Constants

```csharp
public static class DbgDotNetInstructionOffsetConstants {
    // Prolog of method
    public const uint PROLOG = 0xFFFFFFFE;
    
    // Epilog of method
    public const uint EPILOG = 0xFFFFFFFF;
    
    // Unmapped location
    public const uint UNMAPPED = 0xFFFFFFFD;
}
```

### Method Debug Info

```csharp
using dnSpy.Contracts.Debugger.DotNet.Code;

public sealed class DbgMethodDebugInfo {
    // Method this info is for
    public DmdMethodBase Method { get; }
    
    // Compiler that generated the code
    public DbgCompilerKind CompilerKind { get; }
    
    // IL-to-source code mappings
    public DbgILOffsetMapping[] ILOffsetMapping { get; }
    
    // Local variables
    public DbgLocal[] Locals { get; }
    
    // Parameters
    public DbgParameter[] Parameters { get; }
    
    // Scopes
    public DbgMethodDebugScope[] Scopes { get; }
    
    // Async method info (if async)
    public DbgAsyncMethodDebugInfo AsyncInfo { get; }
}
```

---

## .NET Expression Evaluation

### DbgDotNetValue

Base class for .NET values in the debugger.

```csharp
public abstract class DbgDotNetValue {
    // Runtime this value belongs to
    public abstract DbgRuntime Runtime { get; }
    
    // .NET type of the value
    public abstract DmdType Type { get; }
    
    // true if this is a null reference
    public abstract bool IsNull { get; }
    
    // Raw value (for primitives)
    public abstract object RawValue { get; }
}
```

### Evaluating .NET Expressions

```csharp
using dnSpy.Contracts.Debugger.DotNet.Evaluation;
using dnSpy.Contracts.Debugger.Evaluation;

public class DotNetExpressionEvaluator {
    public DbgDotNetValueResult EvaluateDotNetExpression(
        DbgEvaluationContext context,
        DbgStackFrame frame,
        string expression) {
        
        var dotNetContext = context as DbgDotNetEvaluationContext;
        if (dotNetContext == null)
            return null;
        
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
        
        // Get .NET-specific value
        var dotNetValue = result.Value?.GetDotNetValue();
        return new DbgDotNetValueResult {
            Value = dotNetValue,
            Error = result.Error
        };
    }
}
```

### Type System (DmdType)

The debugger uses a reflection-like type system for .NET types.

```csharp
// DmdType represents a .NET type in the debugger
public abstract class DmdType {
    // Type name
    public abstract string Name { get; }
    
    // Full name including namespace
    public abstract string FullName { get; }
    
    // Assembly this type is defined in
    public abstract DmdAssembly Assembly { get; }
    
    // Base type
    public abstract DmdType BaseType { get; }
    
    // Implemented interfaces
    public abstract ReadOnlyCollection<DmdType> GetInterfaces();
    
    // Get methods
    public abstract ReadOnlyCollection<DmdMethodInfo> GetMethods(
        DmdBindingFlags bindingFlags);
    
    // Get fields
    public abstract ReadOnlyCollection<DmdFieldInfo> GetFields(
        DmdBindingFlags bindingFlags);
    
    // Get properties
    public abstract ReadOnlyCollection<DmdPropertyInfo> GetProperties(
        DmdBindingFlags bindingFlags);
}
```

### Working with .NET Types

```csharp
using dnSpy.Contracts.Debugger.DotNet.Evaluation;

public void AnalyzeType(DmdType type) {
    Console.WriteLine($"Type: {type.FullName}");
    Console.WriteLine($"Assembly: {type.Assembly.GetName().Name}");
    Console.WriteLine($"IsClass: {type.IsClass}");
    Console.WriteLine($"IsValueType: {type.IsValueType}");
    Console.WriteLine($"IsInterface: {type.IsInterface}");
    
    if (type.BaseType != null) {
        Console.WriteLine($"Base Type: {type.BaseType.FullName}");
    }
    
    // List methods
    Console.WriteLine("\nMethods:");
    var methods = type.GetMethods(
        DmdBindingFlags.Public | 
        DmdBindingFlags.Instance | 
        DmdBindingFlags.Static);
    
    foreach (var method in methods) {
        Console.WriteLine($"  {method.Name}");
    }
    
    // List fields
    Console.WriteLine("\nFields:");
    var fields = type.GetFields(
        DmdBindingFlags.Public | 
        DmdBindingFlags.Instance | 
        DmdBindingFlags.Static);
    
    foreach (var field in fields) {
        Console.WriteLine($"  {field.Name}: {field.FieldType.Name}");
    }
}
```

---

## .NET Values

### Creating and Manipulating Values

```csharp
using dnSpy.Contracts.Debugger.DotNet.Evaluation;

public class DotNetValueOperations {
    readonly IDbgDotNetRuntime dotNetRuntime;
    
    public DotNetValueOperations(IDbgDotNetRuntime dotNetRuntime) {
        this.dotNetRuntime = dotNetRuntime;
    }
    
    // Create a primitive value
    public DbgDotNetValue CreateInt32(int value) {
        var result = dotNetRuntime.CreateValue(value);
        return result.Value;
    }
    
    // Create a string value
    public DbgDotNetValue CreateString(string value) {
        var result = dotNetRuntime.CreateValue(value);
        return result.Value;
    }
    
    // Get field value
    public DbgDotNetValue GetFieldValue(
        DbgDotNetValue obj,
        string fieldName) {
        
        var type = obj.Type;
        var field = type.GetFields(DmdBindingFlags.Instance | DmdBindingFlags.Public)
            .FirstOrDefault(f => f.Name == fieldName);
        
        if (field == null)
            return null;
        
        var runtime = obj.Runtime.GetDotNetRuntime();
        // Implementation would use reflection to get field value
        return null;
    }
}
```

### Array Values

```csharp
public void WorkWithArray(DbgDotNetValue arrayValue) {
    if (!arrayValue.Type.IsArray)
        return;
    
    // Get array length
    var lengthProperty = arrayValue.Type.GetProperty("Length");
    // Get elements
    // Implementation would iterate array elements
}
```

### Object IDs

```csharp
using dnSpy.Contracts.Debugger.DotNet.Evaluation;

public class ObjectIdManager {
    readonly DbgObjectIdService objectIdService;
    
    [ImportingConstructor]
    public ObjectIdManager(DbgObjectIdService objectIdService) {
        this.objectIdService = objectIdService;
    }
    
    // Create an object ID for tracking an object across evaluations
    public DbgObjectId CreateObjectId(DbgValue value) {
        return objectIdService.CreateObjectId(value, 0);
    }
    
    // Get value from object ID
    public DbgValue GetValue(DbgObjectId objectId, DbgEvaluationContext context) {
        // Implementation would retrieve value
        return null;
    }
    
    // Remove object ID
    public void RemoveObjectId(DbgObjectId objectId) {
        objectIdService.Remove(new[] { objectId });
    }
}
```

---

## Metadata Access

### DbgMetadataService

Access module metadata without loading assemblies.

```csharp
using dnSpy.Contracts.Debugger.DotNet.Metadata;

[Export]
public sealed class MetadataExplorer {
    readonly DbgMetadataService metadataService;
    
    [ImportingConstructor]
    public MetadataExplorer(DbgMetadataService metadataService) {
        this.metadataService = metadataService;
    }
    
    public void ExploreModule(DbgModule module) {
        // Get module metadata
        var moduleId = module.GetModuleId();
        if (moduleId == null)
            return;
        
        Console.WriteLine($"Module: {module.ModuleName}");
        Console.WriteLine($"  Module Version ID: {moduleId.Value.Mvid}");
        Console.WriteLine($"  Assembly: {moduleId.Value.AssemblyName}");
        Console.WriteLine($"  Version: {moduleId.Value.Version}");
    }
}
```

### Dynamic Module Provider

Handle dynamically generated modules.

```csharp
using dnSpy.Contracts.Debugger.DotNet.Metadata;

[Export(typeof(DbgDynamicModuleProvider))]
public sealed class CustomDynamicModuleProvider : DbgDynamicModuleProvider {
    public override DbgDynamicModuleInfo[] GetDynamicModules(
        DbgRuntime runtime) {
        
        // Return information about dynamic modules
        var modules = new List<DbgDynamicModuleInfo>();
        
        // Populate with dynamic module information
        
        return modules.ToArray();
    }
}
```

---

## Decompiler Integration

### DbgDotNetDecompilerService

Integrate with the decompiler to get source code from IL.

```csharp
using dnSpy.Contracts.Debugger.DotNet.Code;

[Export]
public sealed class SourceCodeProvider {
    readonly DbgDotNetDecompilerService decompilerService;
    
    [ImportingConstructor]
    public SourceCodeProvider(DbgDotNetDecompilerService decompilerService) {
        this.decompilerService = decompilerService;
    }
    
    public DbgMethodDebugInfo GetMethodDebugInfo(
        DbgModule module,
        uint token) {
        
        // Get debug info including IL mappings
        var debugInfo = decompilerService.GetMethodDebugInfo(
            module.Runtime,
            module,
            token);
        
        return debugInfo;
    }
    
    public string GetDecompiledMethod(
        DbgModule module,
        uint token) {
        
        var debugInfo = GetMethodDebugInfo(module, token);
        if (debugInfo == null)
            return null;
        
        // Use debug info to show source code
        return FormatMethodSource(debugInfo);
    }
    
    string FormatMethodSource(DbgMethodDebugInfo debugInfo) {
        var sb = new StringBuilder();
        
        // Format method signature
        sb.AppendLine(debugInfo.Method.ToString());
        
        // Show IL mappings
        foreach (var mapping in debugInfo.ILOffsetMapping) {
            sb.AppendLine($"IL_{mapping.ILOffset:X4}: " +
                $"Line {mapping.StartLine}-{mapping.EndLine}");
        }
        
        return sb.ToString();
    }
}
```

### Compiler Detection

```csharp
using dnSpy.Contracts.Debugger.DotNet.Code;

public void DetectCompiler(DbgMethodDebugInfo debugInfo) {
    switch (debugInfo.CompilerKind) {
        case DbgCompilerKind.CSharp:
            Console.WriteLine("Compiled with C# compiler");
            break;
        
        case DbgCompilerKind.VisualBasic:
            Console.WriteLine("Compiled with Visual Basic compiler");
            break;
        
        case DbgCompilerKind.FSharp:
            Console.WriteLine("Compiled with F# compiler");
            break;
        
        default:
            Console.WriteLine("Unknown compiler");
            break;
    }
}
```

---

## Examples

### Example 1: Inspect All Loaded Types

```csharp
using System;
using System.ComponentModel.Composition;
using System.Linq;
using dnSpy.Contracts.App;
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Debugger.DotNet;
using dnSpy.Contracts.Menus;

[ExportMenuItem(
    OwnerGuid = MenuConstants.APP_MENU_DEBUG_GUID,
    Header = "List All Types",
    Group = "9999",
    Order = 9999)]
public sealed class ListAllTypesCommand : MenuItemBase {
    readonly DbgManager dbgManager;
    
    [ImportingConstructor]
    public ListAllTypesCommand(DbgManager dbgManager) {
        this.dbgManager = dbgManager;
    }
    
    public override void Execute(IMenuItemContext context) {
        var process = dbgManager.CurrentProcess.Current;
        if (process == null) {
            MsgBox.Instance.Show("No process is being debugged");
            return;
        }
        
        var types = new List<string>();
        
        foreach (var runtime in process.Runtimes) {
            var dotNetRuntime = runtime.GetDotNetRuntime();
            if (dotNetRuntime == null)
                continue;
            
            var appDomain = dotNetRuntime.GetReflectionAppDomain();
            var assemblies = appDomain.GetAssemblies();
            
            foreach (var assembly in assemblies) {
                var asmTypes = assembly.GetTypes();
                foreach (var type in asmTypes) {
                    types.Add($"{assembly.GetName().Name}::{type.FullName}");
                }
            }
        }
        
        var message = $"Found {types.Count} types:\n\n" +
            string.Join("\n", types.Take(50));
        
        if (types.Count > 50) {
            message += $"\n\n... and {types.Count - 50} more";
        }
        
        MsgBox.Instance.Show(message);
    }
    
    public override bool IsEnabled(IMenuItemContext context) {
        return dbgManager.IsDebugging;
    }
}
```

### Example 2: Find Instances of Type

```csharp
using System;
using System.ComponentModel.Composition;
using System.Linq;
using System.Threading;
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Debugger.CallStack;
using dnSpy.Contracts.Debugger.DotNet.Evaluation;
using dnSpy.Contracts.Debugger.Evaluation;
using dnSpy.Contracts.Extension;

[ExportAutoLoaded]
public sealed class TypeInstanceFinder : IAutoLoaded {
    readonly DbgManager dbgManager;
    readonly DbgCallStackService callStackService;
    readonly DbgLanguageService languageService;
    
    [ImportingConstructor]
    public TypeInstanceFinder(
        DbgManager dbgManager,
        DbgCallStackService callStackService,
        DbgLanguageService languageService) {
        
        this.dbgManager = dbgManager;
        this.callStackService = callStackService;
        this.languageService = languageService;
    }
    
    public DbgDotNetValue[] FindInstancesOfType(string typeName) {
        var thread = dbgManager.CurrentThread.Current;
        if (thread == null)
            return Array.Empty<DbgDotNetValue>();
        
        var frames = callStackService.GetFrames(thread);
        if (frames.Frames.Length == 0)
            return Array.Empty<DbgDotNetValue>();
        
        var topFrame = frames.Frames[0];
        var language = languageService.GetLanguage(thread.Runtime);
        
        var context = language.CreateContext(
            topFrame,
            new DbgLanguageDebugInfo(),
            DbgEvaluationContextOptions.None);
        
        try {
            var instances = new List<DbgDotNetValue>();
            var valueNodeProvider = language.ValueNodeProvider;
            var evalInfo = new DbgEvaluationInfo(context, CancellationToken.None);
            
            // Get all locals
            var locals = valueNodeProvider.GetLocals(
                evalInfo,
                DbgValueNodeEvaluationOptions.None,
                CancellationToken.None);
            
            foreach (var local in locals) {
                var value = local.Value?.GetDotNetValue();
                if (value != null && value.Type.FullName == typeName) {
                    instances.Add(value);
                }
                
                local.Dispose();
            }
            
            return instances.ToArray();
        }
        finally {
            context?.Close(dbgManager.Dispatcher);
        }
    }
}
```

### Example 3: Custom Expression Evaluator Helper

```csharp
using System;
using System.ComponentModel.Composition;
using System.Threading;
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Debugger.CallStack;
using dnSpy.Contracts.Debugger.DotNet.Evaluation;
using dnSpy.Contracts.Debugger.Evaluation;

[Export]
public sealed class ExpressionHelper {
    readonly DbgManager dbgManager;
    readonly DbgCallStackService callStackService;
    readonly DbgLanguageService languageService;
    
    [ImportingConstructor]
    public ExpressionHelper(
        DbgManager dbgManager,
        DbgCallStackService callStackService,
        DbgLanguageService languageService) {
        
        this.dbgManager = dbgManager;
        this.callStackService = callStackService;
        this.languageService = languageService;
    }
    
    public T EvaluateExpression<T>(string expression) {
        var thread = dbgManager.CurrentThread.Current;
        if (thread == null)
            return default(T);
        
        var frames = callStackService.GetFrames(thread);
        if (frames.Frames.Length == 0)
            return default(T);
        
        var topFrame = frames.Frames[0];
        var language = languageService.GetLanguage(thread.Runtime);
        
        var context = language.CreateContext(
            topFrame,
            new DbgLanguageDebugInfo(),
            DbgEvaluationContextOptions.None);
        
        try {
            var evaluator = language.ExpressionEvaluator;
            var evalInfo = new DbgExpressionEvaluationInfo(
                context,
                expression,
                DbgEvaluationOptions.None,
                timeout: TimeSpan.FromSeconds(5));
            
            var result = evaluator.Evaluate(evalInfo);
            
            if (result.Error != null) {
                Console.WriteLine($"Error: {result.Error}");
                return default(T);
            }
            
            var dotNetValue = result.Value?.GetDotNetValue();
            if (dotNetValue == null)
                return default(T);
            
            // Convert to requested type
            if (typeof(T) == typeof(string)) {
                var formatter = language.Formatter;
                var output = new StringBuilderTextColorOutput();
                
                formatter.FormatValue(
                    new DbgEvaluationInfo(context, CancellationToken.None),
                    output,
                    result.Value,
                    new DbgValueFormatterOptions(),
                    CancellationToken.None);
                
                return (T)(object)output.ToString();
            }
            
            // For primitives, use raw value
            if (dotNetValue.RawValue is T rawValue) {
                return rawValue;
            }
            
            return default(T);
        }
        finally {
            context?.Close(dbgManager.Dispatcher);
        }
    }
    
    public void SetVariable(string variableName, object value) {
        // Implementation would set a variable's value
        var expression = $"{variableName} = {value}";
        EvaluateExpression<object>(expression);
    }
}
```

### Example 4: Async Method State Inspector

```csharp
using System;
using System.ComponentModel.Composition;
using dnSpy.Contracts.Debugger;
using dnSpy.Contracts.Debugger.CallStack;
using dnSpy.Contracts.Debugger.DotNet.Code;
using dnSpy.Contracts.Extension;

[ExportAutoLoaded]
public sealed class AsyncMethodInspector : IAutoLoaded {
    readonly DbgManager dbgManager;
    readonly DbgCallStackService callStackService;
    readonly DbgDotNetDecompilerService decompilerService;
    
    [ImportingConstructor]
    public AsyncMethodInspector(
        DbgManager dbgManager,
        DbgCallStackService callStackService,
        DbgDotNetDecompilerService decompilerService) {
        
        this.dbgManager = dbgManager;
        this.callStackService = callStackService;
        this.decompilerService = decompilerService;
        
        dbgManager.ProcessPaused += OnProcessPaused;
    }
    
    void OnProcessPaused(object sender, ProcessPausedEventArgs e) {
        if (e.Thread == null)
            return;
        
        var frames = callStackService.GetFrames(e.Thread);
        foreach (var frame in frames.Frames) {
            InspectFrame(frame);
        }
    }
    
    void InspectFrame(DbgStackFrame frame) {
        if (frame.Module == null)
            return;
        
        var debugInfo = decompilerService.GetMethodDebugInfo(
            frame.Runtime,
            frame.Module,
            frame.FunctionToken);
        
        if (debugInfo?.AsyncInfo != null) {
            Console.WriteLine($"Async Method: {debugInfo.Method.Name}");
            Console.WriteLine($"  State Machine Type: " +
                $"{debugInfo.AsyncInfo.StateMachineType?.FullName}");
            Console.WriteLine($"  Kickoff Method: " +
                $"{debugInfo.AsyncInfo.KickoffMethod?.Name}");
            
            if (debugInfo.AsyncInfo.AsyncStepInfos != null) {
                Console.WriteLine($"  Await Points: " +
                    $"{debugInfo.AsyncInfo.AsyncStepInfos.Length}");
                
                foreach (var stepInfo in debugInfo.AsyncInfo.AsyncStepInfos) {
                    Console.WriteLine($"    Yield Offset: IL_{stepInfo.YieldOffset:X4}");
                    Console.WriteLine($"    Resume Offset: IL_{stepInfo.ResumeOffset:X4}");
                }
            }
        }
    }
}
```

---

## Best Practices

### Memory Management

```csharp
// Always dispose contexts
DbgEvaluationContext context = null;
try {
    context = CreateContext();
    // Use context
}
finally {
    context?.Close(dbgManager.Dispatcher);
}
```

### Type Checking

```csharp
// Check types before operations
if (value.Type.IsClass || value.Type.IsInterface) {
    // Can be null
    if (value.IsNull) {
        Console.WriteLine("Value is null");
        return;
    }
}

// Check for specific types
if (value.Type.FullName == "System.String") {
    // It's a string
}
```

### Performance

- Cache `DmdType` and `DmdMethodInfo` objects when possible
- Use `DbgEvaluationOptions` to control evaluation behavior
- Set reasonable timeouts for expression evaluation
- Dispose of value nodes when done with them

### Error Handling

```csharp
var result = dotNetRuntime.CreateValue(myObject);
if (result.Error != null) {
    Console.WriteLine($"Error creating value: {result.Error}");
    return;
}

var value = result.Value;
// Use value safely
```

---

## Language-Specific Features

### C# Language Support

```csharp
using dnSpy.Contracts.Debugger.DotNet.Evaluation;

// C# language GUID
var csharpGuid = DbgDotNetLanguageGuids.CSharp;

// Check if language is C#
if (context.Language.LanguageGuid == csharpGuid) {
    // C#-specific operations
}
```

### Visual Basic Support

```csharp
// VB language GUID
var vbGuid = DbgDotNetLanguageGuids.VisualBasic;

if (context.Language.LanguageGuid == vbGuid) {
    // VB-specific operations
}
```

---

## Advanced Topics

### Custom Type Formatters

Implement custom formatting for specific types during debugging.

```csharp
using dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters;

[Export(typeof(DbgDotNetFormatter))]
public sealed class MyCustomFormatter : DbgDotNetFormatter {
    public override bool Format(
        DbgEvaluationInfo evalInfo,
        ITextColorWriter output,
        DbgDotNetValue value,
        DbgDotNetFormatterOptions options) {
        
        // Check if we can format this type
        if (value.Type.FullName != "MyNamespace.MyType")
            return false;
        
        // Custom formatting
        output.Write("CustomFormat: ");
        output.Write(value.ToString());
        
        return true;
    }
}
```

### Exception Information

```csharp
using dnSpy.Contracts.Debugger.DotNet.Evaluation;

public void InspectException(DbgDotNetValue exceptionValue) {
    if (!exceptionValue.Type.IsSubclassOf("System.Exception"))
        return;
    
    Console.WriteLine($"Exception Type: {exceptionValue.Type.FullName}");
    
    // Get Message property
    var messageProperty = exceptionValue.Type.GetProperty("Message");
    // Get StackTrace property
    var stackTraceProperty = exceptionValue.Type.GetProperty("StackTrace");
    
    // Read property values using reflection
}
```

---

*For more information, see [Debugger API](DEBUGGER_API.md) and [Main API Documentation](API_DOCUMENTATION.md).*
