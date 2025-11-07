# Namespace `dnSpy.Contracts.Debugger.References`

## Class `DbgLoadModuleReference`

If passed to , the module gets loaded and selected in the treeview

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.References.DbgLoadModuleReference(module: /* DbgModule */, useMemory: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReference.cs` (line 28)

### Constructors

- `public DbgLoadModuleReference(DbgModule module, bool useMemory)`
  - Summary: Constructor
  - Parameters:
    - `DbgModule module`: Module
    - `bool useMemory`: true if the module should be read from memory and not from a file on disk
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReference.cs` (line 44)

### Properties

- `public DbgModule Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReference.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public bool UseMemory { get; }`
  - Summary: true if the module should be read from memory and not from a file on disk
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReference.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseMemory;
    ```

## Class `DbgLoadModuleReferenceHandler`

Loads modules (eg. in the Assembly Explorer treeview). Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.References.DbgLoadModuleReferenceHandler and call its members.
var instance = new dnSpy.Contracts.Debugger.References.DbgLoadModuleReferenceHandler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReferenceHandler.cs` (line 30)

### Methods

- `public abstract DbgModule[] Load(DbgModule[] modules, DbgLoadModuleReferenceHandlerOptions options)`
  - Summary: Loads modules in the treeview. Returns an array of modules that got loaded.
  - Parameters:
    - `DbgModule[] modules`: Modules to load. Unsupported modules can be ignored.
    - `DbgLoadModuleReferenceHandlerOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReferenceHandler.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.Load(modules: /* DbgModule[] */, options: /* DbgLoadModuleReferenceHandlerOptions */);
    ```
- `public abstract bool GoTo(DbgLoadModuleReference moduleRef, ReadOnlyCollection<object> options)`
  - Summary: Returns true if it showed the reference, and false if the next handler should get called. This method is called on the UI thread.
  - Parameters:
    - `DbgLoadModuleReference moduleRef`: Module reference
    - `ReadOnlyCollection<object> options`: Options, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReferenceHandler.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GoTo(moduleRef: /* DbgLoadModuleReference */, options: /* ReadOnlyCollection<object> */);
    ```

## Enum `DbgLoadModuleReferenceHandlerOptions`

Load module options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.References.DbgLoadModuleReferenceHandlerOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.References.DbgLoadModuleReferenceHandlerOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReferenceHandler.cs` (line 52)

### Members

- `None`: No bit is set
- `AutoLoaded` = `x00000001`: The module load was caused by a non-user action
- `ForceMemory` = `x00000002`: Always load the module from the process' address space instead of from the module's file on disk

## Class `ExportDbgLoadModuleReferenceHandlerAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgLoadModuleReferenceHandlerMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.References.ExportDbgLoadModuleReferenceHandlerAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReferenceHandler.cs` (line 79)

### Constructors

- `public ExportDbgLoadModuleReferenceHandlerAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReferenceHandler.cs` (line 82)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReferenceHandler.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDbgLoadModuleReferenceHandlerMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.References.IDbgLoadModuleReferenceHandlerMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.References.IDbgLoadModuleReferenceHandlerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReferenceHandler.cs` (line 71)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/References/DbgLoadModuleReferenceHandler.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

