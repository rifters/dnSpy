# Namespace `dnSpy.Contracts.Debugger.Attach`

## Class `AttachProgramOptions`

Options shown in the 'attach to process' dialog box and created by

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Attach.AttachProgramOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Attach.AttachProgramOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 26)

### Methods

- `public abstract AttachToProgramOptions GetOptions()`
  - Summary: Gets all options required to attach to the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptions();
    ```

### Properties

- `public abstract Guid RuntimeGuid { get; }`
  - Summary: Gets the runtime GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeGuid;
    ```
- `public abstract Guid RuntimeKindGuid { get; }`
  - Summary: Gets the runtime kind GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeKindGuid;
    ```
- `public abstract RuntimeId RuntimeId { get; }`
  - Summary: Runtime id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeId;
    ```
- `public abstract int ProcessId { get; }`
  - Summary: Process id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessId;
    ```
- `public abstract string RuntimeName { get; }`
  - Summary: Runtime name, eg. "CLR v4.0.30319"
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeName;
    ```
- `public virtual DbgArchitecture? Architecture => null`
  - Summary: Processor architecture or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Architecture;
    ```
- `public virtual DbgOperatingSystem? OperatingSystem => null`
  - Summary: Operating system or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OperatingSystem;
    ```
- `public virtual string CommandLine => null`
  - Summary: Command line or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CommandLine;
    ```
- `public virtual string Filename => null`
  - Summary: Full filename or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public virtual string Name => null`
  - Summary: Short process name (filename) or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public virtual string Title => null`
  - Summary: Process title or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptions.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Title;
    ```

## Class `AttachProgramOptionsProvider`

Creates

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Attach.AttachProgramOptionsProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Attach.AttachProgramOptionsProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProvider.cs` (line 29)

### Methods

- `public abstract IEnumerable<AttachProgramOptions> Create(AttachProgramOptionsProviderContext context)`
  - Summary: Creates new instances. This method is called on a background thread.
  - Parameters:
    - `AttachProgramOptionsProviderContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(context: /* AttachProgramOptionsProviderContext */);
    ```

## Class `AttachProgramOptionsProviderContext`

Context passed to

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Attach.AttachProgramOptionsProviderContext(cancellationToken: /* CancellationToken */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProvider.cs` (line 41)

### Constructors

- `public AttachProgramOptionsProviderContext(CancellationToken cancellationToken)`
  - Summary: Constructor
  - Parameters:
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProvider.cs` (line 61)
- `public AttachProgramOptionsProviderContext(int[] processIds, Func<Process, bool> isValidProcess, CancellationToken cancellationToken)`
  - Summary: Constructor
  - Parameters:
    - `int[] processIds`: All valid process ids or null/empty if any process id is valid
    - `Func<Process, bool> isValidProcess`: Checks if it's a valid process. May be null.
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProvider.cs` (line 69)

### Properties

- `public CancellationToken CancellationToken { get; }`
  - Summary: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProvider.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CancellationToken;
    ```
- `public Func<Process, bool> IsValidProcess { get; }`
  - Summary: Checks if it's a valid process. May be null.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProvider.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsValidProcess;
    ```
- `public int[] ProcessIds { get; }`
  - Summary: All valid process ids or empty if any process id is valid
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProvider.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessIds;
    ```

## Class `AttachProgramOptionsProviderFactory`

Creates instances. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Attach.AttachProgramOptionsProviderFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.Attach.AttachProgramOptionsProviderFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProviderFactory.cs` (line 28)

### Methods

- `public abstract AttachProgramOptionsProvider Create(bool allFactories)`
  - Summary: Creates a new or returns null
  - Parameters:
    - `bool allFactories`: true if all factories are called, false if only some of them get called
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProviderFactory.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(allFactories: /* bool */);
    ```

## Class `AttachableProcess`

A process that can be attached to

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Attach.AttachableProcess and call its members.
var instance = new dnSpy.Contracts.Debugger.Attach.AttachableProcess(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 26)

### Methods

- `public abstract AttachToProgramOptions GetOptions()`
  - Summary: Gets all options required to attach to the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptions();
    ```
- `public abstract void Attach()`
  - Summary: Attaches to the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.Attach();
    ```

### Properties

- `public abstract DbgArchitecture Architecture { get; }`
  - Summary: Processor architecture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Architecture;
    ```
- `public abstract DbgOperatingSystem OperatingSystem { get; }`
  - Summary: Operating system
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OperatingSystem;
    ```
- `public abstract Guid RuntimeGuid { get; }`
  - Summary: Gets the runtime GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeGuid;
    ```
- `public abstract Guid RuntimeKindGuid { get; }`
  - Summary: Gets the runtime kind GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeKindGuid;
    ```
- `public abstract RuntimeId RuntimeId { get; }`
  - Summary: Runtime id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeId;
    ```
- `public abstract int ProcessId { get; }`
  - Summary: Process id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessId;
    ```
- `public abstract string Filename { get; }`
  - Summary: Full filename
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public abstract string Name { get; }`
  - Summary: Short process name (filename)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public abstract string RuntimeName { get; }`
  - Summary: Runtime name, eg. "CLR v4.0.30319"
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeName;
    ```
- `public abstract string Title { get; }`
  - Summary: Process title
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcess.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Title;
    ```

## Class `AttachableProcessesService`

Returns all processes that the debug engines support

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Attach.AttachableProcessesService and call its members.
var instance = new dnSpy.Contracts.Debugger.Attach.AttachableProcessesService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcessesService.cs` (line 27)

### Methods

- `public Task<AttachableProcess[]> GetAttachableProcessesAsync(CancellationToken cancellationToken = default)`
  - Summary: Gets all programs that can be attached to
  - Parameters:
    - `CancellationToken cancellationToken` (default: `default`): Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcessesService.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAttachableProcessesAsync(cancellationToken: /* CancellationToken */);
    ```
- `public Task<AttachableProcess[]> GetAttachableProcessesAsync(string processName, CancellationToken cancellationToken = default)`
  - Summary: Gets all programs that can be attached to
  - Parameters:
    - `string processName`: Process name. If it's empty or null, it matches any string. This can include wildcards (* and ?).
    - `CancellationToken cancellationToken` (default: `default`): Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcessesService.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAttachableProcessesAsync(processName: /* string */, cancellationToken: /* CancellationToken */);
    ```
- `public Task<AttachableProcess[]> GetAttachableProcessesAsync(string[] processNames, string[] providerNames, CancellationToken cancellationToken = default)`
  - Summary: Gets all programs that can be attached to
  - Parameters:
    - `string[] processNames`: Process names or null/empty to match any process name. The process name can include wildcards (* and ?)
    - `string[] providerNames`: names, see
    - `CancellationToken cancellationToken` (default: `default`): Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcessesService.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAttachableProcessesAsync(processNames: /* string[] */, providerNames: /* string[] */, cancellationToken: /* CancellationToken */);
    ```
- `public abstract Task<AttachableProcess[]> GetAttachableProcessesAsync(string[] processNames, int[] processIds, string[] providerNames, CancellationToken cancellationToken = default)`
  - Summary: Gets all programs that can be attached to
  - Parameters:
    - `string[] processNames`: Process names or null/empty to match any process name. The process name can include wildcards (* and ?)
    - `int[] processIds`: Process ids or null/empty to match any process id
    - `string[] providerNames`: names, see
    - `CancellationToken cancellationToken` (default: `default`): Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachableProcessesService.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAttachableProcessesAsync(processNames: /* string[] */, processIds: /* int[] */, providerNames: /* string[] */, cancellationToken: /* CancellationToken */);
    ```

## Class `ExportAttachProgramOptionsProviderFactoryAttribute`

Exports an instance

**Inherits/Implements:** `ExportAttribute`, `IAttachProgramOptionsProviderFactoryMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Attach.ExportAttachProgramOptionsProviderFactoryAttribute(name: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProviderFactory.cs` (line 46)

### Constructors

- `public ExportAttachProgramOptionsProviderFactoryAttribute(string name)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProviderFactory.cs` (line 52)

### Properties

- `public string Name { get; }`
  - Summary: Name, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProviderFactory.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `IAttachProgramOptionsProviderFactoryMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Attach.IAttachProgramOptionsProviderFactoryMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Attach.IAttachProgramOptionsProviderFactoryMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProviderFactory.cs` (line 38)

### Properties

- `string Name { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/AttachProgramOptionsProviderFactory.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `PredefinedAttachProgramOptionsProviderNames`

Predefined names

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.Attach.PredefinedAttachProgramOptionsProviderNames members directly without instantiation.
dnSpy.Contracts.Debugger.Attach.PredefinedAttachProgramOptionsProviderNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/PredefinedAttachProgramOptionsProviderNames.cs` (line 24)

### Fields

- `public const string DotNetCore = nameof(DotNetCore)`
  - Summary: .NET Core
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/PredefinedAttachProgramOptionsProviderNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Attach.PredefinedAttachProgramOptionsProviderNames.DotNetCore;
    ```
- `public const string DotNetFramework = nameof(DotNetFramework)`
  - Summary: .NET Framework
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/PredefinedAttachProgramOptionsProviderNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Attach.PredefinedAttachProgramOptionsProviderNames.DotNetFramework;
    ```
- `public const string UnityEditor = nameof(UnityEditor)`
  - Summary: Unity Editor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/PredefinedAttachProgramOptionsProviderNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Attach.PredefinedAttachProgramOptionsProviderNames.UnityEditor;
    ```
- `public const string UnityPlayer = nameof(UnityPlayer)`
  - Summary: Unity Player
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/PredefinedAttachProgramOptionsProviderNames.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Attach.PredefinedAttachProgramOptionsProviderNames.UnityPlayer;
    ```

