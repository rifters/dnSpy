# Namespace `dnSpy.Contracts.Debugger.DotNet.Mono`

## Class `DbgMonoDebugInternalRuntime`

Mono / Unity runtime. It must implement

**Inherits/Implements:** `DbgDotNetInternalRuntime`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Mono.DbgMonoDebugInternalRuntime and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Mono.DbgMonoDebugInternalRuntime(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/DbgMonoDebugInternalRuntime.cs` (line 26)

### Properties

- `public abstract MonoDebugRuntimeKind Kind { get; }`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/DbgMonoDebugInternalRuntime.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `MonoConnectStartDebuggingOptions`

Debugging options used when connecting to a Mono program

**Inherits/Implements:** `MonoConnectStartDebuggingOptionsBase`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Mono.MonoConnectStartDebuggingOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Mono.MonoConnectStartDebuggingOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoConnectStartDebuggingOptions.cs` (line 26)

### Methods

- `public MonoConnectStartDebuggingOptions CopyTo(MonoConnectStartDebuggingOptions other)`
  - Summary: Copies this instance to and returns it
  - Parameters:
    - `MonoConnectStartDebuggingOptions other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoConnectStartDebuggingOptions.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* MonoConnectStartDebuggingOptions */);
    ```
- `public override DebugProgramOptions Clone()`
  - Summary: Clones this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoConnectStartDebuggingOptions.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

## Class `MonoConnectStartDebuggingOptionsBase`

Debugging options used when connecting to a Mono / Unity program

**Inherits/Implements:** `StartDebuggingOptions`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Mono.MonoConnectStartDebuggingOptionsBase();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoConnectStartDebuggingOptionsBase.cs` (line 26)

### Constructors

- `protected MonoConnectStartDebuggingOptionsBase()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoConnectStartDebuggingOptionsBase.cs` (line 50)

### Methods

- `protected void CopyTo(MonoConnectStartDebuggingOptionsBase other)`
  - Summary: Copies this instance to
  - Parameters:
    - `MonoConnectStartDebuggingOptionsBase other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoConnectStartDebuggingOptionsBase.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* MonoConnectStartDebuggingOptionsBase */);
    ```

### Properties

- `public TimeSpan ConnectionTimeout { get; set; }`
  - Summary: Gets the connection timeout. If it's , the default timeout is used.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoConnectStartDebuggingOptionsBase.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ConnectionTimeout;
    ```
- `public bool ProcessIsSuspended { get; set; }`
  - Summary: true if the process is suspended and waiting for the debugger to connect
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoConnectStartDebuggingOptionsBase.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessIsSuspended;
    ```
- `public string Address { get; set; }`
  - Summary: The IP address mono.exe is listening on or null / empty string to use 127.0.0.1
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoConnectStartDebuggingOptionsBase.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```
- `public ushort Port { get; set; }`
  - Summary: The port mono.exe is listening on
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoConnectStartDebuggingOptionsBase.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Port;
    ```

## Enum `MonoDebugRuntimeKind`

Mono debug runtime kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Mono.MonoDebugRuntimeKind and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Mono.MonoDebugRuntimeKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoDebugRuntimeKind.cs` (line 24)

### Members

- `Mono`: Mono
- `Unity`: Unity

## Enum `MonoExeOptions`

mono.exe options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Mono.MonoExeOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Mono.MonoExeOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptions.cs` (line 71)

### Members

- `None`: No bit is set
- `Debug32` = `x00000001`: 32-bit mono.exe can be used
- `Debug64` = `x00000002`: 64-bit mono.exe can be used
- `Prefer32` = `x000000004`: Prefer 32-bit mono.exe over 64-bit mono.exe
- `Prefer64` = `x00000008`: Prefer 64-bit mono.exe over 32-bit mono.exe

## Class `MonoStartDebuggingOptions`

Debugging options used when starting a Mono program

**Inherits/Implements:** `MonoStartDebuggingOptionsBase`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Mono.MonoStartDebuggingOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptions.cs` (line 26)

### Constructors

- `public MonoStartDebuggingOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptions.cs` (line 40)

### Methods

- `public MonoStartDebuggingOptions CopyTo(MonoStartDebuggingOptions other)`
  - Summary: Copies this instance to and returns it
  - Parameters:
    - `MonoStartDebuggingOptions other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptions.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* MonoStartDebuggingOptions */);
    ```
- `public override DebugProgramOptions Clone()`
  - Summary: Clones this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptions.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

### Properties

- `public MonoExeOptions MonoExeOptions { get; set; }`
  - Summary: mono.exe options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptions.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MonoExeOptions;
    ```
- `public string MonoExePath { get; set; }`
  - Summary: Path to mono.exe or null / empty string if it should be auto detected
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptions.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MonoExePath;
    ```

## Class `MonoStartDebuggingOptionsBase`

Debugging options used when debugging a Mono / Unity program

**Inherits/Implements:** `StartDebuggingOptions`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Mono.MonoStartDebuggingOptionsBase();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptionsBase.cs` (line 26)

### Constructors

- `protected MonoStartDebuggingOptionsBase()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptionsBase.cs` (line 60)

### Methods

- `protected MonoStartDebuggingOptionsBase CopyTo(MonoStartDebuggingOptionsBase other)`
  - Summary: Copies this instance to and returns it
  - Parameters:
    - `MonoStartDebuggingOptionsBase other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptionsBase.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* MonoStartDebuggingOptionsBase */);
    ```

### Properties

- `public DbgEnvironment Environment { get; }`
  - Summary: Environment variables
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptionsBase.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Environment;
    ```
- `public TimeSpan ConnectionTimeout { get; set; }`
  - Summary: Gets the connection timeout. If it's , the default timeout is used.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptionsBase.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ConnectionTimeout;
    ```
- `public string CommandLine { get; set; }`
  - Summary: Command line
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptionsBase.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CommandLine;
    ```
- `public string Filename { get; set; }`
  - Summary: Path to application to debug
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptionsBase.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public string WorkingDirectory { get; set; }`
  - Summary: Working directory
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptionsBase.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.WorkingDirectory;
    ```
- `public ushort ConnectionPort { get; set; }`
  - Summary: Connection port or 0 to use a random port
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/MonoStartDebuggingOptionsBase.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ConnectionPort;
    ```

## Class `ThreadStates`

values

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates members directly without instantiation.
dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/ThreadStates.cs` (line 24)

### Fields

- `public static readonly string AbortRequested = nameof(AbortRequested)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/ThreadStates.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates.AbortRequested;
    ```
- `public static readonly string Aborted = nameof(Aborted)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/ThreadStates.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates.Aborted;
    ```
- `public static readonly string Background = nameof(Background)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/ThreadStates.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates.Background;
    ```
- `public static readonly string StopRequested = nameof(StopRequested)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/ThreadStates.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates.StopRequested;
    ```
- `public static readonly string Stopped = nameof(Stopped)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/ThreadStates.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates.Stopped;
    ```
- `public static readonly string SuspendRequested = nameof(SuspendRequested)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/ThreadStates.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates.SuspendRequested;
    ```
- `public static readonly string Suspended = nameof(Suspended)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/ThreadStates.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates.Suspended;
    ```
- `public static readonly string Unstarted = nameof(Unstarted)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/ThreadStates.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates.Unstarted;
    ```
- `public static readonly string WaitSleepJoin = nameof(WaitSleepJoin)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/ThreadStates.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Mono.ThreadStates.WaitSleepJoin;
    ```

## Class `UnityConnectStartDebuggingOptions`

Debugging options used when connecting to a Unity program

**Inherits/Implements:** `MonoConnectStartDebuggingOptionsBase`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Mono.UnityConnectStartDebuggingOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Mono.UnityConnectStartDebuggingOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/UnityConnectStartDebuggingOptions.cs` (line 26)

### Methods

- `public UnityConnectStartDebuggingOptions CopyTo(UnityConnectStartDebuggingOptions other)`
  - Summary: Copies this instance to and returns it
  - Parameters:
    - `UnityConnectStartDebuggingOptions other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/UnityConnectStartDebuggingOptions.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* UnityConnectStartDebuggingOptions */);
    ```
- `public override DebugProgramOptions Clone()`
  - Summary: Clones this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/UnityConnectStartDebuggingOptions.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

## Class `UnityStartDebuggingOptions`

Debugging options used when starting a Unity game. The game must use a patched mono.dll.

**Inherits/Implements:** `MonoStartDebuggingOptionsBase`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Mono.UnityStartDebuggingOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/UnityStartDebuggingOptions.cs` (line 26)

### Constructors

- `public UnityStartDebuggingOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/UnityStartDebuggingOptions.cs` (line 32)

### Methods

- `public UnityStartDebuggingOptions CopyTo(UnityStartDebuggingOptions other)`
  - Summary: Copies this instance to and returns it
  - Parameters:
    - `UnityStartDebuggingOptions other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/UnityStartDebuggingOptions.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* UnityStartDebuggingOptions */);
    ```
- `public override DebugProgramOptions Clone()`
  - Summary: Clones this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet.Mono/UnityStartDebuggingOptions.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

