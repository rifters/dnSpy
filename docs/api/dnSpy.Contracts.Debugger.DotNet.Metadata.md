# Namespace `dnSpy.Contracts.Debugger.DotNet.Metadata`

## Struct `ClassLoadedEventArgs`

Class loaded event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Metadata.ClassLoadedEventArgs(module: /* DbgModule */, loadedClassToken: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 74)

### Constructors

- `public ClassLoadedEventArgs(DbgModule module, uint loadedClassToken)`
  - Summary: Constructor
  - Parameters:
    - `DbgModule module`: Module
    - `uint loadedClassToken`: Token of loaded class
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 90)

### Properties

- `public DbgModule Module { get; }`
  - Summary: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public uint LoadedClassToken { get; }`
  - Summary: Token of loaded class
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LoadedClassToken;
    ```

## Class `DbgAssemblyInfoProvider`

Assembly info provider

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Metadata.DbgAssemblyInfoProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Metadata.DbgAssemblyInfoProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgAssemblyInfoProvider.cs` (line 26)

### Methods

- `public DbgModule GetManifestModule(DbgModule module)`
  - Summary: Returns the manifest module (first module) or null if it's not part of an assembly
  - Parameters:
    - `DbgModule module`: A module in some assembly
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgAssemblyInfoProvider.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.GetManifestModule(module: /* DbgModule */);
    ```
- `public abstract DbgModule[] GetAssemblyModules(DbgModule module)`
  - Summary: Gets all modules in an assembly or an empty array if it's not part of an assembly. The manifest module is always the first module.
  - Parameters:
    - `DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgAssemblyInfoProvider.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAssemblyModules(module: /* DbgModule */);
    ```

## Class `DbgAssemblyInfoProviderFactory`

Creates instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Metadata.DbgAssemblyInfoProviderFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Metadata.DbgAssemblyInfoProviderFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgAssemblyInfoProviderFactory.cs` (line 24)

### Methods

- `public abstract DbgAssemblyInfoProvider Create(DbgRuntime runtime)`
  - Summary: Creates a or returns null
  - Parameters:
    - `DbgRuntime runtime`: Runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgAssemblyInfoProviderFactory.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(runtime: /* DbgRuntime */);
    ```

## Class `DbgDynamicModuleProvider`

Loads and creates dynamic modules (they can get extra classses and members at runtime)

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Metadata.DbgDynamicModuleProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Metadata.DbgDynamicModuleProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 29)

### Methods

- `public abstract IEnumerable<uint> GetModifiedTypes(DbgModule module)`
  - Summary: Gets all modified types. This method is called on the engine thread (see )
  - Parameters:
    - `DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetModifiedTypes(module: /* DbgModule */);
    ```
- `public abstract ModuleDef GetDynamicMetadata(DbgModule module, out ModuleId moduleId)`
  - Summary: Gets the dynamic module's metadata or null if none is available
  - Parameters:
    - `DbgModule module`: Module
    - `out ModuleId moduleId`: Module id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDynamicMetadata(module: /* DbgModule */, moduleId: /* ModuleId */);
    ```
- `public abstract void BeginInvoke(Action action)`
  - Summary: Executes asynchronously on the thread required to load dynamic modules.
  - Parameters:
    - `Action action`: Code to execute
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.BeginInvoke(action: /* Action */);
    ```
- `public abstract void InitializeNonLoadedClasses(DbgModule module, uint[] nonLoadedTokens)`
  - Summary: Initializes new classes that haven't gotten a load-class event yet. This method is called on the engine thread (see )
  - Parameters:
    - `DbgModule module`: Module
    - `uint[] nonLoadedTokens`: Sorted tokens of classes that haven't been loaded but are still present in the metadata
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializeNonLoadedClasses(module: /* DbgModule */, nonLoadedTokens: /* uint[] */);
    ```
- `public abstract void LoadEverything(DbgModule[] modules, bool started)`
  - Summary: Called on the engine thread just before and just after all types and members are force loaded
  - Parameters:
    - `DbgModule[] modules`: Modules that will be loaded
    - `bool started`: true if we're about to load all modules, false if we're done
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadEverything(modules: /* DbgModule[] */, started: /* bool */);
    ```

### Events

- `public abstract event EventHandler<ClassLoadedEventArgs> ClassLoaded`
  - Summary: Raised when a new class has been loaded in a dynamic assembly
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProvider.cs` (line 33)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ClassLoaded += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DbgDynamicModuleProviderFactory`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Metadata.DbgDynamicModuleProviderFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Metadata.DbgDynamicModuleProviderFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProviderFactory.cs` (line 24)

### Methods

- `public abstract DbgDynamicModuleProvider Create(DbgRuntime runtime)`
  - Summary: Creates a or returns null
  - Parameters:
    - `DbgRuntime runtime`: Runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgDynamicModuleProviderFactory.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(runtime: /* DbgRuntime */);
    ```

## Enum `DbgLoadModuleOptions`

Options used when loading modules

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Metadata.DbgLoadModuleOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Metadata.DbgLoadModuleOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgMetadataService.cs` (line 49)

### Members

- `None`: No bit is set
- `AutoLoaded` = `x00000001`: The module load was caused by a non-user action
- `ForceMemory` = `x00000002`: Always load the module from the process' address space instead of from the module's file on disk

## Class `DbgMetadataService`

Provides .NET metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Metadata.DbgMetadataService and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Metadata.DbgMetadataService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgMetadataService.cs` (line 28)

### Methods

- `public abstract ModuleDef TryGetMetadata(DbgModule module, DbgLoadModuleOptions options = DbgLoadModuleOptions.None)`
  - Summary: Returns a or null if none could be loaded
  - Parameters:
    - `DbgModule module`: Module
    - `DbgLoadModuleOptions options` (default: `DbgLoadModuleOptions.None`): Load options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgMetadataService.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetMetadata(module: /* DbgModule */, options: /* DbgLoadModuleOptions */);
    ```
- `public abstract ModuleDef TryGetMetadata(ModuleId moduleId, DbgLoadModuleOptions options = DbgLoadModuleOptions.None)`
  - Summary: Returns a or null if none could be loaded
  - Parameters:
    - `ModuleId moduleId`: Module id
    - `DbgLoadModuleOptions options` (default: `DbgLoadModuleOptions.None`): Load options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgMetadataService.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetMetadata(moduleId: /* ModuleId */, options: /* DbgLoadModuleOptions */);
    ```

## Class `DbgModuleIdProvider`

Provides s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Metadata.DbgModuleIdProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Metadata.DbgModuleIdProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgModuleIdProvider.cs` (line 26)

### Methods

- `public abstract ModuleId? GetModuleId(DbgModule module)`
  - Summary: Gets the or null
  - Parameters:
    - `DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Metadata/DbgModuleIdProvider.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.GetModuleId(module: /* DbgModule */);
    ```

