# Namespace `dnSpy.Contracts.Debugger.DotNet.CorDebug`

## Enum `CorDebugRuntimeKind`

kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.CorDebug.CorDebugRuntimeKind and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.CorDebug.CorDebugRuntimeKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeKind.cs` (line 24)

### Members

- `DotNetFramework`: .NET Framework
- `DotNetCore`: .NET Core

## Struct `CorDebugRuntimeVersion`

Runtime version

**Inherits/Implements:** `IEquatable<CorDebugRuntimeVersion>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.CorDebug.CorDebugRuntimeVersion(kind: /* CorDebugRuntimeKind */, version: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeVersion.cs` (line 26)

### Constructors

- `public CorDebugRuntimeVersion(CorDebugRuntimeKind kind, string version)`
  - Summary: Constructor
  - Parameters:
    - `CorDebugRuntimeKind kind`: Kind
    - `string version`: Version string
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeVersion.cs` (line 43)

### Methods

- `public bool Equals(CorDebugRuntimeVersion other)`
  - Parameters:
    - `CorDebugRuntimeVersion other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeVersion.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* CorDebugRuntimeVersion */);
    ```
- `public override bool Equals(object obj)`
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeVersion.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeVersion.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeVersion.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public CorDebugRuntimeKind Kind { get; }`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeVersion.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public string Version { get; }`
  - Summary: Gets the version string, eg. "v2.0.50727" or "v4.0.30319" if it's .NET Framework. If it's .NET Core, this is currently an empty string.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeVersion.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Version;
    ```

### Operators

- `public static bool operator !=(CorDebugRuntimeVersion left, CorDebugRuntimeVersion right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeVersion.cs` (line 50)
- `public static bool operator ==(CorDebugRuntimeVersion left, CorDebugRuntimeVersion right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugRuntimeVersion.cs` (line 49)

## Class `CorDebugStartDebuggingOptions`

Debugging options base class shared by .NET Framework code and .NET Core code

**Inherits/Implements:** `StartDebuggingOptions`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.CorDebug.CorDebugStartDebuggingOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugStartDebuggingOptions.cs` (line 26)

### Constructors

- `protected CorDebugStartDebuggingOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugStartDebuggingOptions.cs` (line 50)

### Methods

- `protected void CopyTo(CorDebugStartDebuggingOptions other)`
  - Summary: Copies this instance to
  - Parameters:
    - `CorDebugStartDebuggingOptions other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugStartDebuggingOptions.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* CorDebugStartDebuggingOptions */);
    ```

### Properties

- `public DbgEnvironment Environment { get; }`
  - Summary: Environment variables
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugStartDebuggingOptions.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Environment;
    ```
- `public string CommandLine { get; set; }`
  - Summary: Command line
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugStartDebuggingOptions.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CommandLine;
    ```
- `public string Filename { get; set; }`
  - Summary: Path to application to debug
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugStartDebuggingOptions.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public string WorkingDirectory { get; set; }`
  - Summary: Working directory
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorDebugStartDebuggingOptions.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.WorkingDirectory;
    ```

## Class `CorThreadUserStates`

values

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates members directly without instantiation.
dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorThreadUserStates.cs` (line 24)

### Fields

- `public static readonly string Background = nameof(Background)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorThreadUserStates.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates.Background;
    ```
- `public static readonly string StopRequested = nameof(StopRequested)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorThreadUserStates.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates.StopRequested;
    ```
- `public static readonly string Stopped = nameof(Stopped)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorThreadUserStates.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates.Stopped;
    ```
- `public static readonly string SuspendRequested = nameof(SuspendRequested)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorThreadUserStates.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates.SuspendRequested;
    ```
- `public static readonly string Suspended = nameof(Suspended)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorThreadUserStates.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates.Suspended;
    ```
- `public static readonly string ThreadPool = nameof(ThreadPool)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorThreadUserStates.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates.ThreadPool;
    ```
- `public static readonly string UnsafePoint = nameof(UnsafePoint)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorThreadUserStates.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates.UnsafePoint;
    ```
- `public static readonly string Unstarted = nameof(Unstarted)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorThreadUserStates.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates.Unstarted;
    ```
- `public static readonly string WaitSleepJoin = nameof(WaitSleepJoin)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/CorThreadUserStates.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.CorDebug.CorThreadUserStates.WaitSleepJoin;
    ```

## Class `DbgCorDebugInternalRuntime`

.NET Framework / .NET Core runtime. It must implement

**Inherits/Implements:** `DbgDotNetInternalRuntime`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.CorDebug.DbgCorDebugInternalRuntime and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.CorDebug.DbgCorDebugInternalRuntime(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DbgCorDebugInternalRuntime.cs` (line 26)

### Properties

- `public CorDebugRuntimeKind Kind => Version.Kind`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DbgCorDebugInternalRuntime.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public abstract CorDebugRuntimeVersion Version { get; }`
  - Summary: Gets the runtime version
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DbgCorDebugInternalRuntime.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Version;
    ```
- `public abstract string ClrFilename { get; }`
  - Summary: Path to the CLR dll (clr.dll, mscorwks.dll, mscorsvr.dll, coreclr.dll)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DbgCorDebugInternalRuntime.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ClrFilename;
    ```
- `public abstract string RuntimeDirectory { get; }`
  - Summary: Path to the runtime directory
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DbgCorDebugInternalRuntime.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeDirectory;
    ```

## Class `DotNetCoreStartDebuggingOptions`

Debugging options that will start and debug an application when passed to . This is used to debug .NET Core assemblies.

**Inherits/Implements:** `CorDebugStartDebuggingOptions`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.CorDebug.DotNetCoreStartDebuggingOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.CorDebug.DotNetCoreStartDebuggingOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DotNetCoreStartDebuggingOptions.cs` (line 27)

### Methods

- `public DotNetCoreStartDebuggingOptions CopyTo(DotNetCoreStartDebuggingOptions other)`
  - Summary: Copies this instance to and returns it
  - Parameters:
    - `DotNetCoreStartDebuggingOptions other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DotNetCoreStartDebuggingOptions.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* DotNetCoreStartDebuggingOptions */);
    ```
- `public override DebugProgramOptions Clone()`
  - Summary: Clones this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DotNetCoreStartDebuggingOptions.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

### Properties

- `public string Host { get; set; }`
  - Summary: Path to host (eg. dotnet.exe) or null if dnSpy should try to find dotnet.exe
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DotNetCoreStartDebuggingOptions.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Host;
    ```
- `public string HostArguments { get; set; }`
  - Summary: Host arguments (eg. "exec" if .NET Core's dotnet.exe is used)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DotNetCoreStartDebuggingOptions.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HostArguments;
    ```

## Class `DotNetFrameworkStartDebuggingOptions`

Debugging options that will start and debug an application when passed to . This is used to debug .NET Framework assemblies.

**Inherits/Implements:** `CorDebugStartDebuggingOptions`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.CorDebug.DotNetFrameworkStartDebuggingOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.CorDebug.DotNetFrameworkStartDebuggingOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DotNetFrameworkStartDebuggingOptions.cs` (line 27)

### Methods

- `public DotNetFrameworkStartDebuggingOptions CopyTo(DotNetFrameworkStartDebuggingOptions other)`
  - Summary: Copies this instance to and returns it
  - Parameters:
    - `DotNetFrameworkStartDebuggingOptions other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DotNetFrameworkStartDebuggingOptions.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* DotNetFrameworkStartDebuggingOptions */);
    ```
- `public override DebugProgramOptions Clone()`
  - Summary: Clones this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.CorDebug/DotNetFrameworkStartDebuggingOptions.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

