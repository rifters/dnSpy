# Namespace `dnSpy.Contracts.Debugger`

## Enum `AsyncProgramMessageSource`

Message source kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.AsyncProgramMessageSource and call its members.
var instance = new dnSpy.Contracts.Debugger.AsyncProgramMessageSource(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 742)

### Members

- `Other`: Some other source
- `StandardOutput`: Standard output text
- `StandardError`: Standard error text

## Class `AttachToProgramOptions`

Attach to program base class. Created eg. by

**Inherits/Implements:** `DebugProgramOptions`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.AttachToProgramOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.AttachToProgramOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/AttachToProgramOptions.cs` (line 27)

### Methods

- `protected AttachToProgramOptions CopyTo(AttachToProgramOptions other)`
  - Summary: Copies this instance to and returns it
  - Parameters:
    - `AttachToProgramOptions other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/AttachToProgramOptions.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* AttachToProgramOptions */);
    ```

## Class `DbgAppDomain`

An application domain

**Inherits/Implements:** `DbgObject`, `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgAppDomain and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgAppDomain(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgAppDomain.cs` (line 27)

### Properties

- `public DbgModule[] Modules => Runtime.Modules.Where(a => a.AppDomain == this).ToArray()`
  - Summary: Gets all modules
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgAppDomain.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Modules;
    ```
- `public DbgProcess Process => Runtime.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgAppDomain.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DbgInternalAppDomain InternalAppDomain { get; }`
  - Summary: Gets the app domain object created by the debug engine
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgAppDomain.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InternalAppDomain;
    ```
- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgAppDomain.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract int Id { get; }`
  - Summary: Gets the app domain id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgAppDomain.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the name of the app domain
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgAppDomain.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

### Events

- `public abstract event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgAppDomain.cs` (line 31)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DbgAppDomainExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DbgAppDomainExtensions members directly without instantiation.
dnSpy.Contracts.Debugger.DbgAppDomainExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgAppDomainExtensions.cs` (line 27)

### Methods

- `public static DbgDotNetInternalAppDomain GetDotNetInternalAppDomain(this DbgAppDomain appDomain)`
  - Summary: Gets the internal .NET app domain or null if it's not a managed app domain
  - Parameters:
    - `this DbgAppDomain appDomain`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgAppDomainExtensions.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DbgAppDomainExtensions.GetDotNetInternalAppDomain(appDomain: /* DbgAppDomain */);
    ```
- `public static DmdAppDomain GetReflectionAppDomain(this DbgAppDomain appDomain)`
  - Summary: Gets the reflection app domain or null if this isn't a managed app domain
  - Parameters:
    - `this DbgAppDomain appDomain`: Debugger app domain
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgAppDomainExtensions.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DbgAppDomainExtensions.GetReflectionAppDomain(appDomain: /* DbgAppDomain */);
    ```

## Enum `DbgArchitecture`

Architecture

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgArchitecture and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgArchitecture(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 231)

### Members

- `X86`: x86, 32-bit
- `X64`: x64, 64-bit
- `Arm`: 32-bit ARM
- `Arm64`: 64-bit ARM

## Struct `DbgBreakInfo`

Break info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgBreakInfo(kind: /* DbgBreakInfoKind */, data: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 159)

### Constructors

- `public DbgBreakInfo(DbgBreakInfoKind kind, object data)`
  - Summary: Constructor
  - Parameters:
    - `DbgBreakInfoKind kind`: Kind
    - `object data`: Data
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 175)
- `public DbgBreakInfo(DbgMessageEventArgs message)`
  - Summary: Constructor
  - Parameters:
    - `DbgMessageEventArgs message`: Debug message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 184)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DbgBreakInfoKind Kind { get; }`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 163)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public object Data { get; }`
  - Summary: Gets the data, see for more info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 168)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```

## Enum `DbgBreakInfoKind`

Break info kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgBreakInfoKind and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgBreakInfoKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 139)

### Members

- `Unknown`: Unknown break reason
- `Connected`: We've connected to the debugged process
- `Message`: It's paused due to some debug message. is a

## Struct `DbgCollectionChangedEventArgs<T>`

Contains added or removed objects

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgCollectionChangedEventArgs<T>(objects: /* ReadOnlyCollection<T> */, added: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgCollectionChangedEventArgs.cs` (line 28)

### Constructors

- `public DbgCollectionChangedEventArgs(IList<T> objects, bool added)`
  - Summary: Constructor
  - Parameters:
    - `IList<T> objects`: The objects that got added or removed (see )
    - `bool added`: true if were added, false if they were removed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgCollectionChangedEventArgs.cs` (line 54)
- `public DbgCollectionChangedEventArgs(ReadOnlyCollection<T> objects, bool added)`
  - Summary: Constructor
  - Parameters:
    - `ReadOnlyCollection<T> objects`: The objects that got added or removed (see )
    - `bool added`: true if were added, false if they were removed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgCollectionChangedEventArgs.cs` (line 44)
- `public DbgCollectionChangedEventArgs(T obj, bool added)`
  - Summary: Constructor
  - Parameters:
    - `T obj`: The object that got added or removed (see )
    - `bool added`: true if was added, false if it was removed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgCollectionChangedEventArgs.cs` (line 64)

### Properties

- `public ReadOnlyCollection<T> Objects { get; }`
  - Summary: The objects that got added or removed (see )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgCollectionChangedEventArgs.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Objects;
    ```
- `public bool Added { get; }`
  - Summary: true if were added, false if they were removed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgCollectionChangedEventArgs.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Added;
    ```

## Class `DbgCurrentObject<T>`

Contains the current object and the object that caused the debugger to enter break mode

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgCurrentObject<T> and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgCurrentObject<T>(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 281)

### Properties

- `public abstract T Break { get; }`
  - Summary: Gets the object that caused the debugger to enter break mode
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 290)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Break;
    ```
- `public abstract T Current { get; set; }`
  - Summary: Gets the current object or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 285)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Current;
    ```

## Struct `DbgCurrentObjectChangedEventArgs<T>`

changed event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgCurrentObjectChangedEventArgs<T>(currentChanged: /* bool */, breakChanged: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 297)

### Constructors

- `public DbgCurrentObjectChangedEventArgs(bool currentChanged, bool breakChanged)`
  - Summary: Constructor
  - Parameters:
    - `bool currentChanged`: true if changed
    - `bool breakChanged`: true if changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 313)

### Properties

- `public bool BreakChanged { get; }`
  - Summary: true if changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 306)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BreakChanged;
    ```
- `public bool CurrentChanged { get; }`
  - Summary: true if changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 301)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CurrentChanged;
    ```

## Class `DbgDispatcher`

Invokes code on another thread.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgDispatcher and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgDispatcher(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgDispatcher.cs` (line 26)

### Methods

- `public abstract bool CheckAccess()`
  - Summary: Checks whether the current thread is the dispatcher thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgDispatcher.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.CheckAccess();
    ```
- `public abstract void BeginInvoke(Action callback)`
  - Summary: Executes code asynchronously on the dispatcher thread. This method returns immediately even if it happens to be called on the dispatcher thread.
  - Parameters:
    - `Action callback`: Code to execute
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgDispatcher.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.BeginInvoke(callback: /* Action */);
    ```
- `public void VerifyAccess()`
  - Summary: Throws if the current thread isn't the dispatcher thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgDispatcher.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.VerifyAccess();
    ```

## Class `DbgDotNetRuntimeExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DbgDotNetRuntimeExtensions members directly without instantiation.
dnSpy.Contracts.Debugger.DbgDotNetRuntimeExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetRuntimeExtensions.cs` (line 28)

### Methods

- `public static IDbgDotNetRuntime GetDotNetRuntime(this DbgRuntime runtime)`
  - Summary: Gets the instance or throws if it's not a .NET runtime
  - Parameters:
    - `this DbgRuntime runtime`: Runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetRuntimeExtensions.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DbgDotNetRuntimeExtensions.GetDotNetRuntime(runtime: /* DbgRuntime */);
    ```

## Class `DbgEnvironment`

Target environment

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgEnvironment();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgEnvironment.cs` (line 27)

### Constructors

- `public DbgEnvironment()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgEnvironment.cs` (line 38)
- `public DbgEnvironment(DbgEnvironment other)`
  - Summary: Copy constructor
  - Parameters:
    - `DbgEnvironment other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgEnvironment.cs` (line 51)

### Methods

- `public void Add(string key, string value)`
  - Summary: Adds a key and value to the environment
  - Parameters:
    - `string key`: Key
    - `string value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgEnvironment.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(key: /* string */, value: /* string */);
    ```
- `public void AddRange(IEnumerable<KeyValuePair<string, string>> environment)`
  - Summary: Adds values to the environment
  - Parameters:
    - `IEnumerable<KeyValuePair<string, string>> environment`: Environment
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgEnvironment.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.AddRange(environment: /* IEnumerable<KeyValuePair<string, string>> */);
    ```
- `public void Clear()`
  - Summary: Clears the environment
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgEnvironment.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```
- `public void Remove(string key)`
  - Summary: Removes a key from the environment
  - Parameters:
    - `string key`: Key
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgEnvironment.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(key: /* string */);
    ```

### Properties

- `public KeyValuePair<string, string>[] Environment => environment.ToArray()`
  - Summary: Gets the environment keys and values
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgEnvironment.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Environment;
    ```

## Enum `DbgImageLayout`

Image layout

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgImageLayout and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgImageLayout(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgImageLayout.cs` (line 24)

### Members

- `Unknown`: Unknown layout
- `File`: File layout
- `Memory`: Memory layout

## Class `DbgInternalAppDomain`

Base class of a app domain object implemented by the debug engine

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgInternalAppDomain and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgInternalAppDomain(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgInternalAppDomain.cs` (line 24)

### Properties

- `public abstract DbgAppDomain AppDomain { get; }`
  - Summary: Gets the app domain
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgInternalAppDomain.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```

## Class `DbgInternalModule`

Base class of a module object implemented by the debug engine

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgInternalModule and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgInternalModule(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgInternalModule.cs` (line 24)

### Properties

- `public abstract DbgModule Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgInternalModule.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```

## Class `DbgInternalRuntime`

Base class of a runtime object implemented by the debug engine

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgInternalRuntime and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgInternalRuntime(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgInternalRuntime.cs` (line 24)

### Properties

- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgInternalRuntime.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```

## Class `DbgManager`

Manages all debug engines. All events are raised on the dispatcher thread. If you need to hook events before debugging starts, you should export an . It gets called when gets called for the first time.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgManager and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgManager(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 29)

### Methods

- `public abstract bool CanDebugRuntime(int pid, RuntimeId rid)`
  - Summary: Returns true if the runtime can be debugged
  - Parameters:
    - `int pid`: Process id
    - `RuntimeId rid`: Runtime id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.CanDebugRuntime(pid: /* int */, rid: /* RuntimeId */);
    ```
- `public abstract string Start(DebugProgramOptions options)`
  - Summary: Starts debugging. Returns an error string if it failed to create a debug engine, or null on success. See on how to get called the first time this method gets called.
  - Parameters:
    - `DebugProgramOptions options`: Options needed to start the program or attach to it
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Start(options: /* DebugProgramOptions */);
    ```
- `public abstract void BreakAll()`
  - Summary: Pauses all debugged processes
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 116)
  - Example:
    ```csharp
    // Example invocation
    instance.BreakAll();
    ```
- `public abstract void Close(DbgObject obj)`
  - Summary: Closes
  - Parameters:
    - `DbgObject obj`: Object to close
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(obj: /* DbgObject */);
    ```
- `public abstract void Close(IEnumerable<DbgObject> objs)`
  - Summary: Closes
  - Parameters:
    - `IEnumerable<DbgObject> objs`: Objects to close
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 205)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(objs: /* IEnumerable<DbgObject> */);
    ```
- `public abstract void DetachAll()`
  - Summary: Detaches all debugged programs, if possible. If it's not possible to detach a program, it will be terminated.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 145)
  - Example:
    ```csharp
    // Example invocation
    instance.DetachAll();
    ```
- `public abstract void Restart()`
  - Summary: Restarts the debugged program(s)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.Restart();
    ```
- `public abstract void Run(DbgProcess process)`
  - Summary: Lets run again. If is true, all other processes will also run.
  - Parameters:
    - `DbgProcess process`: Process to run
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 128)
  - Example:
    ```csharp
    // Example invocation
    instance.Run(process: /* DbgProcess */);
    ```
- `public abstract void RunAll()`
  - Summary: Lets all programs run again. This is the inverse of
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.RunAll();
    ```
- `public abstract void StopDebuggingAll()`
  - Summary: Stops debugging. All programs started by the debugger will be terminated. All other programs will be detached, if possible, else terminated.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 134)
  - Example:
    ```csharp
    // Example invocation
    instance.StopDebuggingAll();
    ```
- `public abstract void TerminateAll()`
  - Summary: Terminates all debugged programs
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.TerminateAll();
    ```
- `public abstract void WriteMessage(string messageKind, string message)`
  - Summary: Writes a message
  - Parameters:
    - `string messageKind`: Message kind, see
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 224)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteMessage(messageKind: /* string */, message: /* string */);
    ```
- `public void ShowError(string errorMessage)`
  - Summary: Shows an error message and returns immediately
  - Parameters:
    - `string errorMessage`: Error message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 217)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowError(errorMessage: /* string */);
    ```
- `public void WriteMessage(string message)`
  - Summary: Writes a message that will be shown in the output window
  - Parameters:
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 211)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteMessage(message: /* string */);
    ```

### Properties

- `public abstract DbgCurrentObject<DbgProcess> CurrentProcess { get; }`
  - Summary: Gets the current process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 155)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CurrentProcess;
    ```
- `public abstract DbgCurrentObject<DbgRuntime> CurrentRuntime { get; }`
  - Summary: Gets the current runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 165)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CurrentRuntime;
    ```
- `public abstract DbgCurrentObject<DbgThread> CurrentThread { get; }`
  - Summary: Gets the current thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 175)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CurrentThread;
    ```
- `public abstract DbgDispatcher Dispatcher { get; }`
  - Summary: Gets the dispatcher. All debugger events are raised on this thread. is also called on this thread including disposing of data added by eg. .
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Dispatcher;
    ```
- `public abstract DbgProcess[] Processes { get; }`
  - Summary: Gets all debugged processes. Can be empty even if is true if the process hasn't been created yet.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Processes;
    ```
- `public abstract bool CanDetachWithoutTerminating { get; }`
  - Summary: true if can be called without terminating any programs
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 150)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanDetachWithoutTerminating;
    ```
- `public abstract bool CanRestart { get; }`
  - Summary: true if can be called
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanRestart;
    ```
- `public abstract bool IsDebugging { get; }`
  - Summary: true if a program is being debugged
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDebugging;
    ```
- `public abstract bool? IsRunning { get; }`
  - Summary: true if all processes are running, false if they're all paused, and null if some are running and some are paused. This property is valid only if is true.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRunning;
    ```
- `public abstract string[] DebugTags { get; }`
  - Summary: Gets all debug tags, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 89)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DebugTags;
    ```

### Events

- `public abstract event EventHandler DelayedIsRunningChanged`
  - Summary: Raised when all processes have been running for a little while, eg. 1 second.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 84)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.DelayedIsRunningChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler IsDebuggingChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 67)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.IsDebuggingChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler IsRunningChanged`
  - Summary: Raised when is changed, see also
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 79)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.IsRunningChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgProcess>> ProcessesChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 111)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ProcessesChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCollectionChangedEventArgs<string>> DebugTagsChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 94)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.DebugTagsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCurrentObjectChangedEventArgs<DbgProcess>> CurrentProcessChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 160)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.CurrentProcessChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCurrentObjectChangedEventArgs<DbgRuntime>> CurrentRuntimeChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 170)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.CurrentRuntimeChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCurrentObjectChangedEventArgs<DbgThread>> CurrentThreadChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 180)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.CurrentThreadChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgManagerMessageEventArgs> DbgManagerMessage`
  - Summary: Raised when gets called. This event is raised on a random thread.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 229)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.DbgManagerMessage += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgMessageEventArgs> Message`
  - Summary: Raised on the debugger thread when there's a new message, eg. a process was created, a thread has exited, etc. The listeners can pause the debugged program by setting to true.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 40)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Message += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<ModulesRefreshedEventArgs> ModulesRefreshed`
  - Summary: Raised when the module's memory has been updated (eg. decrypted)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 185)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ModulesRefreshed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<ProcessPausedEventArgs> ProcessPaused`
  - Summary: Raised when a process gets paused due to some event in the process. If more than one process is being debugged, this is normally only raised once, for the first process.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 100)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ProcessPaused += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `DbgManagerMessageEventArgs`

Message event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgManagerMessageEventArgs(messageKind: /* string */, message: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 255)

### Constructors

- `public DbgManagerMessageEventArgs(string messageKind, string message)`
  - Summary: Constructor
  - Parameters:
    - `string messageKind`: Message kind, see
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 271)

### Properties

- `public string Message { get; }`
  - Summary: Gets the message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 264)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```
- `public string MessageKind { get; }`
  - Summary: Gets the message kind, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 259)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```

## Class `DbgMessageAppDomainEventArgs`

App domain message base class

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageAppDomainEventArgs(appDomain: /* DbgAppDomain */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 265)

### Constructors

- `protected DbgMessageAppDomainEventArgs(DbgAppDomain appDomain)`
  - Summary: Constructor
  - Parameters:
    - `DbgAppDomain appDomain`: App domain
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 275)

### Properties

- `public DbgAppDomain AppDomain { get; }`
  - Summary: Gets the app domain
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 269)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```

## Class `DbgMessageAppDomainLoadedEventArgs`

App domain loaded message ()

**Inherits/Implements:** `DbgMessageAppDomainEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageAppDomainLoadedEventArgs(appDomain: /* DbgAppDomain */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 282)

### Constructors

- `public DbgMessageAppDomainLoadedEventArgs(DbgAppDomain appDomain)`
  - Summary: Constructor
  - Parameters:
    - `DbgAppDomain appDomain`: App domain
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 292)

### Properties

- `public override DbgMessageKind Kind => DbgMessageKind.AppDomainLoaded`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 286)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageAppDomainUnloadedEventArgs`

App domain unloaded message ()

**Inherits/Implements:** `DbgMessageAppDomainEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageAppDomainUnloadedEventArgs(appDomain: /* DbgAppDomain */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 300)

### Constructors

- `public DbgMessageAppDomainUnloadedEventArgs(DbgAppDomain appDomain)`
  - Summary: Constructor
  - Parameters:
    - `DbgAppDomain appDomain`: App domain
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 310)

### Properties

- `public override DbgMessageKind Kind => DbgMessageKind.AppDomainUnloaded`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 304)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageAsyncProgramMessageEventArgs`

Message from the debugged program ()

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageAsyncProgramMessageEventArgs(source: /* AsyncProgramMessageSource */, message: /* string */, runtime: /* DbgRuntime */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 762)

### Constructors

- `public DbgMessageAsyncProgramMessageEventArgs(AsyncProgramMessageSource source, string message, DbgRuntime runtime)`
  - Summary: Constructor
  - Parameters:
    - `AsyncProgramMessageSource source`: Source
    - `string message`: Message
    - `DbgRuntime runtime`: Runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 789)

### Properties

- `public AsyncProgramMessageSource Source { get; }`
  - Summary: Gets the message source kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 771)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Source;
    ```
- `public DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 781)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.AsyncProgramMessage`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 766)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public string Message { get; }`
  - Summary: Gets the text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 776)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```

## Class `DbgMessageBoundBreakpointEventArgs`

A bound breakpoint was hit ()

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageBoundBreakpointEventArgs(boundBreakpoint: /* DbgBoundCodeBreakpoint */, thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 520)

### Constructors

- `public DbgMessageBoundBreakpointEventArgs(DbgBoundCodeBreakpoint boundBreakpoint, DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `DbgBoundCodeBreakpoint boundBreakpoint`: Bound breakpoint
    - `DbgThread thread`: Thread or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 541)

### Properties

- `public DbgBoundCodeBreakpoint BoundBreakpoint { get; }`
  - Summary: Gets the bound breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 529)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BoundBreakpoint;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 534)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.BoundBreakpoint`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 524)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageBreakEventArgs`

The program was paused by the user, or because some other program was paused for some other reason ()

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageBreakEventArgs(runtime: /* DbgRuntime */, thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 712)

### Constructors

- `public DbgMessageBreakEventArgs(DbgRuntime runtime, DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `DbgThread thread`: Thread or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 733)

### Properties

- `public DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 721)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 726)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.Break`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 716)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageEntryPointBreakEventArgs`

The entry point has been reached (). This message is only sent if the user chose to break at the entry point.

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageEntryPointBreakEventArgs(runtime: /* DbgRuntime */, thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 453)

### Constructors

- `public DbgMessageEntryPointBreakEventArgs(DbgRuntime runtime, DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `DbgThread thread`: Thread or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 474)

### Properties

- `public DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 462)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 467)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.EntryPointBreak`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 457)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageEventArgs`

Base class of all debugger messages

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgMessageEventArgs and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgMessageEventArgs(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 134)

### Properties

- `public abstract DbgMessageKind Kind { get; }`
  - Summary: Gets the message kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 138)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public bool Pause {
			get => pause;
			set => pause |= value;
		}`
  - Summary: true if the program should be paused. It's only possible to write true to this property.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 143)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Pause;
    ```

## Class `DbgMessageExceptionThrownEventArgs`

Exception thrown message ()

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageExceptionThrownEventArgs(exception: /* DbgException */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 430)

### Constructors

- `public DbgMessageExceptionThrownEventArgs(DbgException exception)`
  - Summary: Constructor
  - Parameters:
    - `DbgException exception`: Exception
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 445)

### Properties

- `public DbgException Exception { get; }`
  - Summary: Gets the exception
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 439)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Exception;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.ExceptionThrown`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 434)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Enum `DbgMessageKind`

Debugger message kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgMessageKind and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgMessageKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 28)

### Members

- `ProcessCreated`: A process was created ()
- `ProcessExited`: A process has exited ()
- `RuntimeCreated`: A runtime was created ()
- `RuntimeExited`: A runtime has exited ()
- `AppDomainLoaded`: An app domain was loaded ()
- `AppDomainUnloaded`: An app domain was unloaded (). This message isn't sent if the program has exited.
- `ModuleLoaded`: A module was loaded ()
- `ModuleUnloaded`: A module was unloaded (). This message isn't sent if the program has exited or if its app domain has unloaded.
- `ThreadCreated`: A thread was created ()
- `ThreadExited`: A thread has exited (). This message isn't sent if the program has exited.
- `ExceptionThrown`: An exception was thrown ()
- `EntryPointBreak`: The entry point has been reached (). This message is only sent if the user chose to break at the entry point.
- `ProgramMessage`: Message from the debugged program ()
- `BoundBreakpoint`: A bound breakpoint was hit ()
- `ProgramBreak`: The program paused itself by executing a break instruction or method ()
- `StepComplete`: Step into/over/out is complete ()
- `SetIPComplete`: SetIP() is complete ()
- `UserMessage`: Some message that should be shown to the user, eg. we failed to connect to the debugged process ()
- `Break`: The program was paused by the user, or because some other program was paused for some other reason ()
- `AsyncProgramMessage`: Message from the debugged program ()

## Class `DbgMessageModuleEventArgs`

Module message base class

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageModuleEventArgs(module: /* DbgModule */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 318)

### Constructors

- `protected DbgMessageModuleEventArgs(DbgModule module)`
  - Summary: Constructor
  - Parameters:
    - `DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 328)

### Properties

- `public DbgModule Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 322)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```

## Class `DbgMessageModuleLoadedEventArgs`

Module loaded message ()

**Inherits/Implements:** `DbgMessageModuleEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageModuleLoadedEventArgs(module: /* DbgModule */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 335)

### Constructors

- `public DbgMessageModuleLoadedEventArgs(DbgModule module)`
  - Summary: Constructor
  - Parameters:
    - `DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 345)

### Properties

- `public override DbgMessageKind Kind => DbgMessageKind.ModuleLoaded`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 339)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageModuleUnloadedEventArgs`

Module unloaded message ()

**Inherits/Implements:** `DbgMessageModuleEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageModuleUnloadedEventArgs(module: /* DbgModule */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 353)

### Constructors

- `public DbgMessageModuleUnloadedEventArgs(DbgModule module)`
  - Summary: Constructor
  - Parameters:
    - `DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 363)

### Properties

- `public override DbgMessageKind Kind => DbgMessageKind.ModuleUnloaded`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 357)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageProcessCreatedEventArgs`

Process created message ()

**Inherits/Implements:** `DbgMessageProcessEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageProcessCreatedEventArgs(process: /* DbgProcess */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 170)

### Constructors

- `public DbgMessageProcessCreatedEventArgs(DbgProcess process)`
  - Summary: Constructor
  - Parameters:
    - `DbgProcess process`: Process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 180)

### Properties

- `public override DbgMessageKind Kind => DbgMessageKind.ProcessCreated`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 174)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageProcessEventArgs`

Process message base class

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageProcessEventArgs(process: /* DbgProcess */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 153)

### Constructors

- `protected DbgMessageProcessEventArgs(DbgProcess process)`
  - Summary: Constructor
  - Parameters:
    - `DbgProcess process`: Process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 163)

### Properties

- `public DbgProcess Process { get; }`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 157)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```

## Class `DbgMessageProcessExitedEventArgs`

Process exited message ()

**Inherits/Implements:** `DbgMessageProcessEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageProcessExitedEventArgs(process: /* DbgProcess */, exitCode: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 188)

### Constructors

- `public DbgMessageProcessExitedEventArgs(DbgProcess process, int exitCode)`
  - Summary: Constructor
  - Parameters:
    - `DbgProcess process`: Process
    - `int exitCode`: Process exit code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 204)

### Properties

- `public int ExitCode { get; }`
  - Summary: Gets the exit code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 197)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExitCode;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.ProcessExited`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 192)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageProgramBreakEventArgs`

The program paused itself by executing a break instruction or method ()

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageProgramBreakEventArgs(runtime: /* DbgRuntime */, thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 550)

### Constructors

- `public DbgMessageProgramBreakEventArgs(DbgRuntime runtime, DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `DbgThread thread`: Thread or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 571)

### Properties

- `public DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 559)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 564)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.ProgramBreak`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 554)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageProgramMessageEventArgs`

Message from the debugged program ()

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageProgramMessageEventArgs(message: /* string */, runtime: /* DbgRuntime */, thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 483)

### Constructors

- `public DbgMessageProgramMessageEventArgs(string message, DbgRuntime runtime, DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
    - `DbgRuntime runtime`: Runtime
    - `DbgThread thread`: Thread or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 510)

### Properties

- `public DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 497)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 502)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.ProgramMessage`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 487)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public string Message { get; }`
  - Summary: Gets the text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 492)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```

## Class `DbgMessageRuntimeCreatedEventArgs`

Runtime created message ()

**Inherits/Implements:** `DbgMessageRuntimeEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageRuntimeCreatedEventArgs(runtime: /* DbgRuntime */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 229)

### Constructors

- `public DbgMessageRuntimeCreatedEventArgs(DbgRuntime runtime)`
  - Summary: Constructor
  - Parameters:
    - `DbgRuntime runtime`: Runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 239)

### Properties

- `public override DbgMessageKind Kind => DbgMessageKind.RuntimeCreated`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 233)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageRuntimeEventArgs`

Runtime message base class

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageRuntimeEventArgs(runtime: /* DbgRuntime */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 212)

### Constructors

- `protected DbgMessageRuntimeEventArgs(DbgRuntime runtime)`
  - Summary: Constructor
  - Parameters:
    - `DbgRuntime runtime`: Runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 222)

### Properties

- `public DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 216)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```

## Class `DbgMessageRuntimeExitedEventArgs`

Runtime exited message ()

**Inherits/Implements:** `DbgMessageRuntimeEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageRuntimeExitedEventArgs(runtime: /* DbgRuntime */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 247)

### Constructors

- `public DbgMessageRuntimeExitedEventArgs(DbgRuntime runtime)`
  - Summary: Constructor
  - Parameters:
    - `DbgRuntime runtime`: Runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 257)

### Properties

- `public override DbgMessageKind Kind => DbgMessageKind.RuntimeExited`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 251)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageSetIPCompleteEventArgs`

SetIP() is complete ()

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageSetIPCompleteEventArgs(thread: /* DbgThread */, framesInvalidated: /* bool */, error: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 620)

### Constructors

- `public DbgMessageSetIPCompleteEventArgs(DbgThread thread, bool framesInvalidated, string error)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread
    - `bool framesInvalidated`: true if all frames in the thread have been invalidated
    - `string error`: Error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 657)

### Properties

- `public DbgRuntime Runtime => Thread.Runtime`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 629)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 634)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public bool FramesInvalidated { get; }`
  - Summary: true if all frames in the thread have been invalidated
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 639)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FramesInvalidated;
    ```
- `public bool HasError => Error != null`
  - Summary: true if there was an error. Error message is in
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 649)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasError;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.SetIPComplete`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 624)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public string Error { get; }`
  - Summary: Gets the error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 644)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Class `DbgMessageStepCompleteEventArgs`

Step into/over/out is complete ()

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageStepCompleteEventArgs(thread: /* DbgThread */, error: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 580)

### Constructors

- `public DbgMessageStepCompleteEventArgs(DbgThread thread, string error)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread
    - `string error`: Error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 611)

### Properties

- `public DbgRuntime Runtime => Thread.Runtime`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 589)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 594)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public bool HasError => Error != null`
  - Summary: true if there was an error. Error message is in
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 604)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasError;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.StepComplete`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 584)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public string Error { get; }`
  - Summary: Gets the error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 599)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Class `DbgMessageThreadCreatedEventArgs`

Thread created message ()

**Inherits/Implements:** `DbgMessageThreadEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageThreadCreatedEventArgs(thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 388)

### Constructors

- `public DbgMessageThreadCreatedEventArgs(DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 398)

### Properties

- `public override DbgMessageKind Kind => DbgMessageKind.ThreadCreated`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 392)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageThreadEventArgs`

Thread message base class

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageThreadEventArgs(thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 371)

### Constructors

- `protected DbgMessageThreadEventArgs(DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 381)

### Properties

- `public DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 375)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```

## Class `DbgMessageThreadExitedEventArgs`

Thread exited message ()

**Inherits/Implements:** `DbgMessageThreadEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageThreadExitedEventArgs(thread: /* DbgThread */, exitCode: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 406)

### Constructors

- `public DbgMessageThreadExitedEventArgs(DbgThread thread, int exitCode)`
  - Summary: Constructor
  - Parameters:
    - `DbgThread thread`: Thread
    - `int exitCode`: Thread exit code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 422)

### Properties

- `public int ExitCode { get; }`
  - Summary: Gets the exit code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 415)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExitCode;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.ThreadExited`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 410)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgMessageUserMessageEventArgs`

A message that should be shown to the user

**Inherits/Implements:** `DbgMessageEventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgMessageUserMessageEventArgs(messageKind: /* UserMessageKind */, message: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 667)

### Constructors

- `public DbgMessageUserMessageEventArgs(UserMessageKind messageKind, string message)`
  - Summary: Constructor
  - Parameters:
    - `UserMessageKind messageKind`: Message kind
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 688)

### Properties

- `public UserMessageKind MessageKind { get; }`
  - Summary: Gets the message kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 676)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MessageKind;
    ```
- `public override DbgMessageKind Kind => DbgMessageKind.UserMessage`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 671)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public string Message { get; }`
  - Summary: Gets the message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 681)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```

## Class `DbgModule`

A module in a process

**Inherits/Implements:** `DbgObject`, `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgModule and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgModule(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 28)

### Properties

- `public DbgProcess Process => Runtime.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DateTime? Timestamp { get; }`
  - Summary: Timestamp (UTC) of module (eg. as found in the PE header) or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 112)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Timestamp;
    ```
- `public abstract DbgAppDomain AppDomain { get; }`
  - Summary: Gets the app domain or null if it's a process module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public abstract DbgImageLayout ImageLayout { get; }`
  - Summary: Image layout
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageLayout;
    ```
- `public abstract DbgInternalModule InternalModule { get; }`
  - Summary: Gets the module object created by the debug engine
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InternalModule;
    ```
- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract bool IsDynamic { get; }`
  - Summary: true if it's a dynamic module (the application can add more types and members to the module at runtime)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDynamic;
    ```
- `public abstract bool IsExe { get; }`
  - Summary: true if it's an EXE file, false if it's a DLL file
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsExe;
    ```
- `public abstract bool IsInMemory { get; }`
  - Summary: true if it's an in-memory module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInMemory;
    ```
- `public abstract bool? IsOptimized { get; }`
  - Summary: true if it's an optimized module, false if it's an unoptimized module, and null if it's a native module.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOptimized;
    ```
- `public abstract int Order { get; }`
  - Summary: Load order of this module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public abstract int RefreshedVersion { get; }`
  - Summary: Gets incremented when the module gets refreshed ()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 127)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RefreshedVersion;
    ```
- `public abstract string Filename { get; }`
  - Summary: Filename if it exists on disk, else it could be any longer name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public abstract string Name { get; }`
  - Summary: Name of module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public abstract string Version { get; }`
  - Summary: Gets the version, eg. the file version, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 117)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Version;
    ```
- `public abstract uint Size { get; }`
  - Summary: Size of module. Only valid if is true
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Size;
    ```
- `public abstract ulong Address { get; }`
  - Summary: Address of module. Only valid if is true
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```
- `public bool HasAddress => Address != 0 && Size != 0`
  - Summary: true if and are valid
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasAddress;
    ```

### Events

- `public abstract event EventHandler Refreshed`
  - Summary: Raised when the module's memory has been updated (eg. decrypted)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 122)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Refreshed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModule.cs` (line 32)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DbgModuleDotNetExtensions`

extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DbgModuleDotNetExtensions members directly without instantiation.
dnSpy.Contracts.Debugger.DbgModuleDotNetExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Modules/DbgModuleDotNetExtensions.cs` (line 24)

### Methods

- `public static bool IsDotNetModule(this DbgModule module)`
  - Summary: Returns true if is a .NET module
  - Parameters:
    - `this DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Modules/DbgModuleDotNetExtensions.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DbgModuleDotNetExtensions.IsDotNetModule(module: /* DbgModule */);
    ```

## Class `DbgModuleExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DbgModuleExtensions members directly without instantiation.
dnSpy.Contracts.Debugger.DbgModuleExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgModuleExtensions.cs` (line 27)

### Methods

- `public static DbgDotNetInternalModule GetDotNetInternalModule(this DbgModule module)`
  - Summary: Gets the internal .NET module or null if it's not a managed module
  - Parameters:
    - `this DbgModule module`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgModuleExtensions.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DbgModuleExtensions.GetDotNetInternalModule(module: /* DbgModule */);
    ```
- `public static DmdModule GetReflectionModule(this DbgModule module)`
  - Summary: Gets the reflection module or null if this isn't a managed module
  - Parameters:
    - `this DbgModule module`: Debugger module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgModuleExtensions.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DbgModuleExtensions.GetReflectionModule(module: /* DbgModule */);
    ```

## Class `DbgModuleMemoryRefreshedNotifier`

Notifies the debugger that the memory of a module has been updated (eg. decrypted)

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgModuleMemoryRefreshedNotifier and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgModuleMemoryRefreshedNotifier(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgModuleMemoryRefreshedNotifier.cs` (line 26)

### Events

- `public abstract event EventHandler<ModulesRefreshedEventArgs> ModulesRefreshed`
  - Summary: Raised when the module's memory has been updated (eg. decrypted). The debugger will try to reset all breakpoints.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModuleMemoryRefreshedNotifier.cs` (line 31)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ModulesRefreshed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DbgObject`

Base class of debugger objects that only exist while debugging

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgObject();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 29)

### Constructors

- `protected DbgObject()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 36)

### Methods

- `protected abstract void CloseCore(DbgDispatcher dispatcher)`
  - Summary: Called by after it has raised and before it disposes of all data. This method is called on the dispatcher thread (see )
  - Parameters:
    - `DbgDispatcher dispatcher`: Dispatcher
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseCore(dispatcher: /* DbgDispatcher */);
    ```
- `public T GetData<T>() where T : class`
  - Summary: Gets existing data or throws if the data doesn't exist
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    instance.GetData();
    ```
- `public T GetOrCreateData<T>() where T : class, new()`
  - Summary: Gets or creates data. If it implements , it will get disposed when this object gets closed.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateData();
    ```
- `public T GetOrCreateData<T>(Func<T> create) where T : class`
  - Summary: Gets or creates data. If it implements , it will get disposed when this object gets closed.
  - Parameters:
    - `Func<T> create`: Creates the data if it doesn't exist
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateData(create: /* Func<T> */);
    ```
- `public bool HasData<T>() where T : class`
  - Summary: Checks if the data exists or is null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.HasData();
    ```
- `public bool TryGetData<T>(out T value) where T : class`
  - Summary: Gets data
  - Parameters:
    - `out T value`: Result
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 119)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetData(value: /* T */);
    ```
- `public void Close(DbgDispatcher dispatcher)`
  - Summary: Closes the instance. This method must only be executed on the dispatcher thread This method must only be called by the owner object.
  - Parameters:
    - `DbgDispatcher dispatcher`: Dispatcher
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(dispatcher: /* DbgDispatcher */);
    ```

### Properties

- `public bool IsClosed => isClosed != 0`
  - Summary: true if the instance has been closed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsClosed;
    ```

### Events

- `public event EventHandler Closed`
  - Summary: Raised when it's closed. Data methods eg. can be called but some other methods could throw or can't be called. After all handlers have been notified, all data get disposed (if they implement ).
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgObject.cs` (line 58)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Closed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Enum `DbgOperatingSystem`

Operating system

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgOperatingSystem and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgOperatingSystem(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 256)

### Members

- `Windows`: Windows OS
- `MacOS`: OSX/MacOS OS
- `Linux`: Linux OS

## Class `DbgProcess`

A debugged process

**Inherits/Implements:** `DbgObject`, `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgProcess and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgProcess(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 28)

### Methods

- `public abstract void Break()`
  - Summary: Pauses the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 220)
  - Example:
    ```csharp
    // Example invocation
    instance.Break();
    ```
- `public abstract void Detach()`
  - Summary: Detaches the process, if possible, else it will be terminated
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 210)
  - Example:
    ```csharp
    // Example invocation
    instance.Detach();
    ```
- `public abstract void ReadMemory(ulong address, byte[] destination, int destinationIndex, int size)`
  - Summary: Reads memory. Unreadable memory is returned as 0s.
  - Parameters:
    - `ulong address`: Address in the debugged process
    - `byte[] destination`: Destination buffer
    - `int destinationIndex`: Destination index
    - `int size`: Number of bytes to read
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 134)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadMemory(address: /* ulong */, destination: /* byte[] */, destinationIndex: /* int */, size: /* int */);
    ```
- `public abstract void Run()`
  - Summary: Lets the process run again
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 225)
  - Example:
    ```csharp
    // Example invocation
    instance.Run();
    ```
- `public abstract void Terminate()`
  - Summary: Terminates the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 215)
  - Example:
    ```csharp
    // Example invocation
    instance.Terminate();
    ```
- `public abstract void WriteMemory(ulong address, byte[] source, int sourceIndex, int size)`
  - Summary: Writes memory.
  - Parameters:
    - `ulong address`: Address in the debugged process
    - `byte[] source`: Source buffer
    - `int sourceIndex`: Source index
    - `int size`: Number of bytes to write
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 178)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteMemory(address: /* ulong */, source: /* byte[] */, sourceIndex: /* int */, size: /* int */);
    ```
- `public byte[] ReadMemory(ulong address, int size)`
  - Summary: Reads memory. Unreadable memory is returned as 0s.
  - Parameters:
    - `ulong address`: Address in the debugged process
    - `int size`: Number of bytes to read
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadMemory(address: /* ulong */, size: /* int */);
    ```
- `public unsafe abstract void ReadMemory(ulong address, void* destination, int size)`
  - Summary: Reads memory. Unreadable memory is returned as 0s.
  - Parameters:
    - `ulong address`: Address in the debugged process
    - `void* destination`: Destination address
    - `int size`: Number of bytes to read
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadMemory(address: /* ulong */, destination: /* void* */, size: /* int */);
    ```
- `public unsafe abstract void WriteMemory(ulong address, void* source, int size)`
  - Summary: Writes memory.
  - Parameters:
    - `ulong address`: Address in the debugged process
    - `void* source`: Source address
    - `int size`: Number of bytes to write
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 169)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteMemory(address: /* ulong */, source: /* void* */, size: /* int */);
    ```
- `public void ReadMemory(ulong address, byte[] destination)`
  - Summary: Reads memory. Unreadable memory is returned as 0s.
  - Parameters:
    - `ulong address`: Address in the debugged process
    - `byte[] destination`: Destination buffer
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 141)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadMemory(address: /* ulong */, destination: /* byte[] */);
    ```
- `public void StopDebugging()`
  - Summary: Stops debugging. This will either detach from the process or terminate it depending on
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 200)
  - Example:
    ```csharp
    // Example invocation
    instance.StopDebugging();
    ```
- `public void WriteMemory(ulong address, byte[] source)`
  - Summary: Writes memory.
  - Parameters:
    - `ulong address`: Address in the debugged process
    - `byte[] source`: Source buffer
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 185)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteMemory(address: /* ulong */, source: /* byte[] */);
    ```

### Properties

- `public abstract DbgArchitecture Architecture { get; }`
  - Summary: Gets the architecture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Architecture;
    ```
- `public abstract DbgManager DbgManager { get; }`
  - Summary: Gets the owner debug manager
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DbgManager;
    ```
- `public abstract DbgOperatingSystem OperatingSystem { get; }`
  - Summary: Gets the operating system
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OperatingSystem;
    ```
- `public abstract DbgProcessState State { get; }`
  - Summary: Gets the process state
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.State;
    ```
- `public abstract DbgRuntime[] Runtimes { get; }`
  - Summary: Gets all runtimes
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtimes;
    ```
- `public abstract DbgThread[] Threads { get; }`
  - Summary: Gets all threads
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Threads;
    ```
- `public abstract ReadOnlyCollection<string> Debugging { get; }`
  - Summary: What is being debugged. This is shown in the UI (eg. Processes window)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Debugging;
    ```
- `public abstract bool IsRunning { get; }`
  - Summary: true if the process is running, false if it's paused or terminated (see )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRunning;
    ```
- `public abstract bool ShouldDetach { get; set; }`
  - Summary: true if the process gets detached when debugging stops (), false if the process gets terminated.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 195)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShouldDetach;
    ```
- `public abstract int Bitness { get; }`
  - Summary: Gets the process bitness (32 or 64)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Bitness;
    ```
- `public abstract int Id { get; }`
  - Summary: Process id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public abstract string Filename { get; }`
  - Summary: Gets the filename or an empty string if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the process name or an empty string if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public int PointerSize => Bitness / 8`
  - Summary: Gets the size of a pointer
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PointerSize;
    ```

### Events

- `public abstract event EventHandler DelayedIsRunningChanged`
  - Summary: Raised when the process has been running for a little while, eg. 1 second.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 117)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.DelayedIsRunningChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler IsRunningChanged`
  - Summary: Raised when is changed, see also
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 112)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.IsRunningChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgRuntime>> RuntimesChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 52)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.RuntimesChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgThread>> ThreadsChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 102)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ThreadsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 32)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Enum `DbgProcessState`

Process state

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgProcessState and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgProcessState(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgProcess.cs` (line 276)

### Members

- `Running`: The process is running
- `Paused`: The process is paused
- `Terminated`: The process is terminated

## Class `DbgRuntime`

A runtime in a process

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgRuntime and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgRuntime(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 28)

### Methods

- `public abstract void CloseOnContinue(DbgObject obj)`
  - Summary: Closes just before the runtime continues (or when it gets closed if it never continues)
  - Parameters:
    - `DbgObject obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseOnContinue(obj: /* DbgObject */);
    ```
- `public abstract void CloseOnContinue(IEnumerable<DbgObject> objs)`
  - Summary: Closes just before the runtime continues (or when it gets closed if it never continues)
  - Parameters:
    - `IEnumerable<DbgObject> objs`: Objects
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseOnContinue(objs: /* IEnumerable<DbgObject> */);
    ```
- `public abstract void CloseOnExit(IEnumerable<DbgObject> objs)`
  - Summary: Closes when the runtime closes
  - Parameters:
    - `IEnumerable<DbgObject> objs`: Objects
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseOnExit(objs: /* IEnumerable<DbgObject> */);
    ```
- `public abstract void CloseOnExit(IEnumerable<IDisposable> objs)`
  - Summary: Closes when the runtime closes
  - Parameters:
    - `IEnumerable<IDisposable> objs`: Objects
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseOnExit(objs: /* IEnumerable<IDisposable> */);
    ```
- `public void CloseOnExit(DbgObject obj)`
  - Summary: Closes when the runtime closes
  - Parameters:
    - `DbgObject obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseOnExit(obj: /* DbgObject */);
    ```
- `public void CloseOnExit(IDisposable obj)`
  - Summary: Closes when the runtime closes
  - Parameters:
    - `IDisposable obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 127)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseOnExit(obj: /* IDisposable */);
    ```

### Properties

- `public abstract DbgAppDomain[] AppDomains { get; }`
  - Summary: Gets all app domains
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomains;
    ```
- `public abstract DbgInternalRuntime InternalRuntime { get; }`
  - Summary: Gets the runtime object created by the debug engine
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InternalRuntime;
    ```
- `public abstract DbgModule[] Modules { get; }`
  - Summary: Gets all modules
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Modules;
    ```
- `public abstract DbgProcess Process { get; }`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DbgThread[] Threads { get; }`
  - Summary: Gets all threads
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Threads;
    ```
- `public abstract Guid Guid { get; }`
  - Summary: Gets the runtime GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public abstract Guid RuntimeKindGuid { get; }`
  - Summary: Gets the runtime kind GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeKindGuid;
    ```
- `public abstract ReadOnlyCollection<DbgBreakInfo> BreakInfos { get; }`
  - Summary: Gets the break infos, it gets updated when the runtime breaks and cleared when it continues.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BreakInfos;
    ```
- `public abstract ReadOnlyCollection<string> Tags { get; }`
  - Summary: Gets all runtime tags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tags;
    ```
- `public abstract RuntimeId Id { get; }`
  - Summary: Gets the process unique runtime id. There must be exactly one such id per process.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the runtime name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

### Events

- `public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgAppDomain>> AppDomainsChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 72)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.AppDomainsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgModule>> ModulesChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 82)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ModulesChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgThread>> ThreadsChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgRuntime.cs` (line 92)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ThreadsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DbgRuntimeDotNetExtensions`

extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DbgRuntimeDotNetExtensions members directly without instantiation.
dnSpy.Contracts.Debugger.DbgRuntimeDotNetExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Runtimes/DbgRuntimeDotNetExtensions.cs` (line 28)

### Methods

- `public static bool IsDotNetRuntime(this DbgRuntime runtime)`
  - Summary: Returns true if is a .NET runtime
  - Parameters:
    - `this DbgRuntime runtime`: Runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Runtimes/DbgRuntimeDotNetExtensions.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DbgRuntimeDotNetExtensions.IsDotNetRuntime(runtime: /* DbgRuntime */);
    ```

## Class `DbgRuntimeExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DbgRuntimeExtensions members directly without instantiation.
dnSpy.Contracts.Debugger.DbgRuntimeExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgRuntimeExtensions.cs` (line 27)

### Methods

- `public static DbgDotNetInternalRuntime GetDotNetInternalRuntime(this DbgRuntime runtime)`
  - Summary: Gets the internal .NET runtime or null if it's not a managed runtime
  - Parameters:
    - `this DbgRuntime runtime`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgRuntimeExtensions.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DbgRuntimeExtensions.GetDotNetInternalRuntime(runtime: /* DbgRuntime */);
    ```
- `public static DmdRuntime GetReflectionRuntime(this DbgRuntime runtime)`
  - Summary: Gets the reflection runtime or null if this isn't a managed runtime
  - Parameters:
    - `this DbgRuntime runtime`: Debugger runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgRuntimeExtensions.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DbgRuntimeExtensions.GetReflectionRuntime(runtime: /* DbgRuntime */);
    ```

## Struct `DbgStateInfo`

Contains state and localized state that can be shown in the UI

**Inherits/Implements:** `IEquatable<DbgStateInfo>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DbgStateInfo(state: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 26)

### Constructors

- `public DbgStateInfo(string state)`
  - Summary: Constructor
  - Parameters:
    - `string state`: State
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 41)
- `public DbgStateInfo(string state, string localizedState)`
  - Summary: Constructor
  - Parameters:
    - `string state`: State (non-localized)
    - `string localizedState`: Localized state
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 50)

### Methods

- `public bool Equals(DbgStateInfo other)`
  - Summary: Equals()
  - Parameters:
    - `DbgStateInfo other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgStateInfo */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public string LocalizedState { get; }`
  - Summary: Localized string (shown in the UI)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LocalizedState;
    ```
- `public string State { get; }`
  - Summary: Non-localized string
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.State;
    ```

### Operators

- `public static bool operator !=(DbgStateInfo left, DbgStateInfo right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 57)
- `public static bool operator ==(DbgStateInfo left, DbgStateInfo right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgStateInfo.cs` (line 56)

## Class `DbgThread`

A thread in a debugged process

**Inherits/Implements:** `DbgObject`, `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DbgThread and call its members.
var instance = new dnSpy.Contracts.Debugger.DbgThread(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 32)

### Methods

- `public DbgStackFrame GetTopStackFrame()`
  - Summary: Gets the top stack frame or null if there's none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 120)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTopStackFrame();
    ```
- `public DbgStackFrame[] GetFrames(int count)`
  - Summary: Gets the first frames. The returned frame count can be less than if there's not enough frames available.
  - Parameters:
    - `int count`: Max number of frames to return
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFrames(count: /* int */);
    ```
- `public abstract DbgStackWalker CreateStackWalker()`
  - Summary: Creates a new instance that can be used to get the call stack.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateStackWalker();
    ```
- `public abstract DbgStepper CreateStepper()`
  - Summary: Creates a stepper. The caller must close the returned instance by calling .
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 161)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateStepper();
    ```
- `public abstract bool CanSetIP(DbgCodeLocation location)`
  - Summary: Checks if can be called
  - Parameters:
    - `DbgCodeLocation location`: New location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 174)
  - Example:
    ```csharp
    // Example invocation
    instance.CanSetIP(location: /* DbgCodeLocation */);
    ```
- `public abstract bool HasName()`
  - Summary: Returns true if the thread has a name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    instance.HasName();
    ```
- `public abstract void Freeze()`
  - Summary: Freezes the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.Freeze();
    ```
- `public abstract void SetIP(DbgCodeLocation location)`
  - Summary: Sets a new instruction pointer
  - Parameters:
    - `DbgCodeLocation location`: New location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 167)
  - Example:
    ```csharp
    // Example invocation
    instance.SetIP(location: /* DbgCodeLocation */);
    ```
- `public abstract void Thaw()`
  - Summary: Thaws the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    instance.Thaw();
    ```

### Properties

- `public DbgProcess Process => Runtime.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DbgAppDomain AppDomain { get; }`
  - Summary: Gets the app domain or null if it's a process thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract ReadOnlyCollection<DbgStateInfo> State { get; }`
  - Summary: Thread state
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.State;
    ```
- `public abstract int SuspendedCount { get; }`
  - Summary: Gets the suspended count. It's 0 if the thread isn't suspended, and greater than zero if it's suspended.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SuspendedCount;
    ```
- `public abstract string Kind { get; }`
  - Summary: Gets the thread kind, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the thread name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public abstract string UIName { get; set; }`
  - Summary: Gets the thread name shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIName;
    ```
- `public abstract ulong Id { get; }`
  - Summary: Gets the id of this thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public abstract ulong? ManagedId { get; }`
  - Summary: Gets the managed id of this thread or null if it's unknown or if it's not a managed thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ManagedId;
    ```
- `public bool IsMain => Kind == PredefinedThreadKinds.Main`
  - Summary: true if this is the main thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMain;
    ```

### Events

- `public abstract event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgThread.cs` (line 36)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DebugProgramOptions`

Debug program base class

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DebugProgramOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.DebugProgramOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DebugProgramOptions.cs` (line 24)

### Methods

- `public abstract DebugProgramOptions Clone()`
  - Summary: Clones this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebugProgramOptions.cs` (line 29)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

## Class `DebuggerSettings`

Global debugger settings. This class is thread safe. Listeners will be notified on a random thread.

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DebuggerSettings and call its members.
var instance = new dnSpy.Contracts.Debugger.DebuggerSettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 29)

### Methods

- `protected void OnPropertyChanged(string propName)`
  - Summary: Raises
  - Parameters:
    - `string propName`: Name of property that got changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propName: /* string */);
    ```

### Properties

- `public abstract bool AntiCheckRemoteDebuggerPresent { get; set; }`
  - Summary: true to patch CheckRemoteDebuggerPresent() so it can't be used to detect native debuggers
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 89)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AntiCheckRemoteDebuggerPresent;
    ```
- `public abstract bool AntiIsDebuggerPresent { get; set; }`
  - Summary: true to patch IsDebuggerPresent() so it can't be used to detect native debuggers
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AntiIsDebuggerPresent;
    ```
- `public abstract bool AsyncDebugging { get; set; }`
  - Summary: Async debugging (step over await statements, step out of async methods)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 198)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsyncDebugging;
    ```
- `public abstract bool AutoOpenLocalsWindow { get; set; }`
  - Summary: true to auto open the locals window when the debugger starts
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AutoOpenLocalsWindow;
    ```
- `public abstract bool BreakAllProcesses { get; set; }`
  - Summary: true to break all processes when one process breaks
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 99)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BreakAllProcesses;
    ```
- `public abstract bool EnableManagedDebuggingAssistants { get; set; }`
  - Summary: true to enable Managed Debugging Assistants (MDA)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 104)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EnableManagedDebuggingAssistants;
    ```
- `public abstract bool FocusActiveProcess { get; set; }`
  - Summary: Give focus to the active process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 173)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FocusActiveProcess;
    ```
- `public abstract bool GroupParametersAndLocalsTogether { get; set; }`
  - Summary: Group parameters and locals together (locals window)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GroupParametersAndLocalsTogether;
    ```
- `public abstract bool HideCompilerGeneratedMembers { get; set; }`
  - Summary: Hide compiler generated members in variables windows (respect debugger attributes, eg. )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 144)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HideCompilerGeneratedMembers;
    ```
- `public abstract bool HideDeprecatedError { get; set; }`
  - Summary: Hide deprecated members
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 154)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HideDeprecatedError;
    ```
- `public abstract bool HighlightChangedVariables { get; set; }`
  - Summary: Highlights the value of a variable that has changed in variables windows
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 109)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HighlightChangedVariables;
    ```
- `public abstract bool IgnoreBreakInstructions { get; set; }`
  - Summary: true to ignore break instructions and method calls
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IgnoreBreakInstructions;
    ```
- `public abstract bool PreventManagedDebuggerDetection { get; set; }`
  - Summary: true to prevent detection of managed debuggers
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 79)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PreventManagedDebuggerDetection;
    ```
- `public abstract bool PropertyEvalAndFunctionCalls { get; set; }`
  - Summary: true if properties and methods can be executed (used by locals / watch windows)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PropertyEvalAndFunctionCalls;
    ```
- `public abstract bool RedirectGuiConsoleOutput { get; set; }`
  - Summary: Redirect GUI applications' console output to the Output window
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 183)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RedirectGuiConsoleOutput;
    ```
- `public abstract bool RespectHideMemberAttributes { get; set; }`
  - Summary: Respect attributes that can hide a member, eg. and
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 149)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RespectHideMemberAttributes;
    ```
- `public abstract bool ShowCompilerGeneratedVariables { get; set; }`
  - Summary: Show compiler generated variables (locals/autos window)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowCompilerGeneratedVariables;
    ```
- `public abstract bool ShowDecompilerGeneratedVariables { get; set; }`
  - Summary: Show decompiler generated variables (locals/autos window)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 139)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowDecompilerGeneratedVariables;
    ```
- `public abstract bool ShowOnlyPublicMembers { get; set; }`
  - Summary: Show only public members in variables windows
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 188)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowOnlyPublicMembers;
    ```
- `public abstract bool ShowRawLocals { get; set; }`
  - Summary: Show all locals. Captured variables aren't shown, their display classes are shown instead.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 193)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowRawLocals;
    ```
- `public abstract bool ShowRawStructureOfObjects { get; set; }`
  - Summary: Shows raw structure of objects in variables windows
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 114)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowRawStructureOfObjects;
    ```
- `public abstract bool ShowReturnValues { get; set; }`
  - Summary: Show return values in Locals window
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 178)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowReturnValues;
    ```
- `public abstract bool SortLocals { get; set; }`
  - Summary: Sort locals (locals window)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 124)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SortLocals;
    ```
- `public abstract bool SortParameters { get; set; }`
  - Summary: Sort parameters (locals window)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 119)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SortParameters;
    ```
- `public abstract bool StepOverPropertiesAndOperators { get; set; }`
  - Summary: Step over properties and operators
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 203)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StepOverPropertiesAndOperators;
    ```
- `public abstract bool SuppressJITOptimization_ProgramModules { get; set; }`
  - Summary: Suppress JIT optimization on module load (program modules). If false, the code will be optimized and much more difficult to debug (it will be like when attaching to a process). All modules in the same folder, or sub folder, as the main executable are considered program modules.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 168)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SuppressJITOptimization_ProgramModules;
    ```
- `public abstract bool SuppressJITOptimization_SystemModules { get; set; }`
  - Summary: Suppress JIT optimization on module load (system modules). If false, the code will be optimized and much more difficult to debug (it will be like when attaching to a process). System modules are all non-program modules (eg. GAC assemblies).
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 161)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SuppressJITOptimization_SystemModules;
    ```
- `public abstract bool SyntaxHighlight { get; set; }`
  - Summary: true to colorize debugger tool windows and other debugger UI objects
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SyntaxHighlight;
    ```
- `public abstract bool UseDigitSeparators { get; set; }`
  - Summary: true to use digit separators
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseDigitSeparators;
    ```
- `public abstract bool UseHexadecimal { get; set; }`
  - Summary: true to use hexadecimal numbers, false to use decimal numbers
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseHexadecimal;
    ```
- `public abstract bool UseMemoryModules { get; set; }`
  - Summary: Use modules loaded from memory instead of files. Useful if a module gets decrypted at runtime.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseMemoryModules;
    ```
- `public abstract bool UseStringConversionFunction { get; set; }`
  - Summary: Use ToString() or similar method to get a string representation of an object (used by locals / watch windows)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseStringConversionFunction;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DebuggerSettings.cs` (line 33)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `ExportThreadCategoryProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IThreadCategoryProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.ExportThreadCategoryProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 46)

### Constructors

- `public ExportThreadCategoryProviderAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 52)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDbgManagerStartListener`

All exported classes implementing this interface get created the first time gets called.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.IDbgManagerStartListener and call its members.
var instance = new dnSpy.Contracts.Debugger.IDbgManagerStartListener(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/IDbgManagerStartListener.cs` (line 25)

### Methods

- `void OnStart(DbgManager dbgManager)`
  - Summary: Called the first time gets called. The code has a chance to hook events and do other initialization before a program gets debugged.
  - Parameters:
    - `DbgManager dbgManager`: Debug manager instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/IDbgManagerStartListener.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.OnStart(dbgManager: /* DbgManager */);
    ```

## Interface `IThreadCategoryProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.IThreadCategoryProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.IThreadCategoryProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 38)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Struct `ModulesRefreshedEventArgs`

event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.ModulesRefreshedEventArgs(module: /* DbgModule */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgModuleMemoryRefreshedNotifier.cs` (line 37)

### Constructors

- `public ModulesRefreshedEventArgs(DbgModule module)`
  - Summary: Constructor
  - Parameters:
    - `DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModuleMemoryRefreshedNotifier.cs` (line 47)
- `public ModulesRefreshedEventArgs(DbgModule[] modules)`
  - Summary: Constructor
  - Parameters:
    - `DbgModule[] modules`: Modules
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModuleMemoryRefreshedNotifier.cs` (line 53)

### Properties

- `public DbgModule[] Modules { get; }`
  - Summary: Gets the modules
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgModuleMemoryRefreshedNotifier.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Modules;
    ```

## Class `PredefinedBreakKinds`

Predefined break kinds, see

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.PredefinedBreakKinds members directly without instantiation.
dnSpy.Contracts.Debugger.PredefinedBreakKinds./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebuggingOptions.cs` (line 47)

### Fields

- `public const string CreateProcess = nameof(CreateProcess)`
  - Summary: Break as soon as the process has been created
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebuggingOptions.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedBreakKinds.CreateProcess;
    ```
- `public const string DontBreak = nameof(DontBreak)`
  - Summary: Don't break, let the program run
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebuggingOptions.cs` (line 51)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedBreakKinds.DontBreak;
    ```
- `public const string EntryPoint = nameof(EntryPoint)`
  - Summary: Entry point
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebuggingOptions.cs` (line 61)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedBreakKinds.EntryPoint;
    ```

## Class `PredefinedDbgManagerMessageKinds`

Predefined message kinds, see

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.PredefinedDbgManagerMessageKinds members directly without instantiation.
dnSpy.Contracts.Debugger.PredefinedDbgManagerMessageKinds./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 235)

### Fields

- `public const string ErrorUser = nameof(ErrorUser)`
  - Summary: An error message that should be shown to the user
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 244)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgManagerMessageKinds.ErrorUser;
    ```
- `public const string Output = nameof(Output)`
  - Summary: Output window
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 239)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgManagerMessageKinds.Output;
    ```
- `public const string StepFilter = nameof(StepFilter)`
  - Summary: Messages by the stepper
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 249)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgManagerMessageKinds.StepFilter;
    ```

## Class `PredefinedDbgRuntimeGuids`

Predefined GUIDs ()

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.PredefinedDbgRuntimeGuids members directly without instantiation.
dnSpy.Contracts.Debugger.PredefinedDbgRuntimeGuids./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeGuids.cs` (line 26)

### Fields

- `public const string DotNetCore = "E0B4EB52-D1D9-42AB-B130-028CA31CF9F6"`
  - Summary: .NET Core
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeGuids.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgRuntimeGuids.DotNetCore;
    ```
- `public const string DotNetFramework = "CD03ACDD-4F3A-4736-8591-4902B4DCC8C1"`
  - Summary: .NET Framework
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeGuids.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgRuntimeGuids.DotNetFramework;
    ```
- `public const string DotNetMono = "7A99738E-9A75-4268-9B74-BBA174764FC7"`
  - Summary: Mono
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeGuids.cs` (line 60)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgRuntimeGuids.DotNetMono;
    ```
- `public const string DotNetUnity = "CE8A11EE-73EF-4A51-B5D0-BDA2E665A2B4"`
  - Summary: Unity
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeGuids.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgRuntimeGuids.DotNetUnity;
    ```
- `public static readonly Guid DotNetCore_Guid = new Guid(DotNetCore)`
  - Summary: .NET Core
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeGuids.cs` (line 45)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgRuntimeGuids.DotNetCore_Guid;
    ```
- `public static readonly Guid DotNetFramework_Guid = new Guid(DotNetFramework)`
  - Summary: .NET Framework
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeGuids.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgRuntimeGuids.DotNetFramework_Guid;
    ```
- `public static readonly Guid DotNetMono_Guid = new Guid(DotNetMono)`
  - Summary: Mono
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeGuids.cs` (line 65)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgRuntimeGuids.DotNetMono_Guid;
    ```
- `public static readonly Guid DotNetUnity_Guid = new Guid(DotNetUnity)`
  - Summary: Unity
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeGuids.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgRuntimeGuids.DotNetUnity_Guid;
    ```

## Class `PredefinedDbgRuntimeKindGuids`

Predefined runtime kind guids ()

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.PredefinedDbgRuntimeKindGuids members directly without instantiation.
dnSpy.Contracts.Debugger.PredefinedDbgRuntimeKindGuids./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeKindGuids.cs` (line 26)

### Fields

- `public const string DotNet = "03CFDE68-877E-4DD7-9A14-5C100B37A01A"`
  - Summary: .NET
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeKindGuids.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgRuntimeKindGuids.DotNet;
    ```
- `public static readonly Guid DotNet_Guid = new Guid(DotNet)`
  - Summary: .NET
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDbgRuntimeKindGuids.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDbgRuntimeKindGuids.DotNet_Guid;
    ```

## Class `PredefinedDebugTags`

Predefined debug tags

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.PredefinedDebugTags members directly without instantiation.
dnSpy.Contracts.Debugger.PredefinedDebugTags./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/PredefinedDebugTags.cs` (line 24)

### Fields

- `public const string DotNetDebugger = nameof(DotNetDebugger)`
  - Summary: .NET debugger
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedDebugTags.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedDebugTags.DotNetDebugger;
    ```

## Class `PredefinedThreadKinds`

Predefined thread kinds, see also

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.PredefinedThreadKinds members directly without instantiation.
dnSpy.Contracts.Debugger.PredefinedThreadKinds./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/PredefinedThreadKinds.cs` (line 24)

### Fields

- `public const string Finalizer = nameof(Finalizer)`
  - Summary: Finalizer thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedThreadKinds.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedThreadKinds.Finalizer;
    ```
- `public const string GC = nameof(GC)`
  - Summary: Garbage Collector thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedThreadKinds.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedThreadKinds.GC;
    ```
- `public const string Main = nameof(Main)`
  - Summary: Main thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedThreadKinds.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedThreadKinds.Main;
    ```
- `public const string Terminated = nameof(Terminated)`
  - Summary: Terminated thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedThreadKinds.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedThreadKinds.Terminated;
    ```
- `public const string ThreadPool = nameof(ThreadPool)`
  - Summary: Thread pool thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedThreadKinds.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedThreadKinds.ThreadPool;
    ```
- `public const string Unknown = nameof(Unknown)`
  - Summary: Unknown thread kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedThreadKinds.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedThreadKinds.Unknown;
    ```
- `public const string WorkerThread = nameof(WorkerThread)`
  - Summary: Worker thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/PredefinedThreadKinds.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.PredefinedThreadKinds.WorkerThread;
    ```

## Struct `ProcessPausedEventArgs`

Process paused event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.ProcessPausedEventArgs(process: /* DbgProcess */, thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 322)

### Constructors

- `public ProcessPausedEventArgs(DbgProcess process, DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `DbgProcess process`: Process
    - `DbgThread thread`: Thread or null if unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 338)

### Properties

- `public DbgProcess Process { get; }`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 326)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread or null if unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/DbgManager.cs` (line 331)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```

## Class `RuntimeId`

Runtime id; unique per process

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.RuntimeId and call its members.
var instance = new dnSpy.Contracts.Debugger.RuntimeId(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/RuntimeId.cs` (line 24)

### Methods

- `public abstract override bool Equals(object obj)`
  - Summary: Compares this instance to another object
  - Parameters:
    - `object obj`: Other object
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/RuntimeId.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public abstract override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/RuntimeId.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

## Class `StartDebuggingOptions`

Debug a program base class. Created eg. by

**Inherits/Implements:** `DebugProgramOptions`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.StartDebuggingOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.StartDebuggingOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebuggingOptions.cs` (line 27)

### Methods

- `protected void CopyTo(StartDebuggingOptions other)`
  - Summary: Copies this instance to
  - Parameters:
    - `StartDebuggingOptions other`: Destination
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebuggingOptions.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyTo(other: /* StartDebuggingOptions */);
    ```

### Properties

- `public string BreakKind { get; set; }`
  - Summary: Where to break, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebuggingOptions.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BreakKind;
    ```

## Struct `ThreadCategoryInfo`

Thread category info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.ThreadCategoryInfo(image: /* object */, category: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 64)

### Constructors

- `public ThreadCategoryInfo(object image, string category)`
  - Summary: Constructor
  - Parameters:
    - `object image`: Image
    - `string category`: Category
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 80)

### Properties

- `public object Image { get; }`
  - Summary: Image (an ImageReference struct)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Image;
    ```
- `public string Category { get; }`
  - Summary: Category
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Category;
    ```

## Class `ThreadCategoryProvider`

Provides thread categories and images. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.ThreadCategoryProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.ThreadCategoryProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 28)

### Methods

- `public abstract ThreadCategoryInfo? GetCategory(string kind)`
  - Summary: Returns the thread category info or null
  - Parameters:
    - `string kind`: Thread kind, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/ThreadCategoryProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCategory(kind: /* string */);
    ```

## Enum `UserMessageKind`

message kinds

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.UserMessageKind and call its members.
var instance = new dnSpy.Contracts.Debugger.UserMessageKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/DbgMessageEventArgs.cs` (line 697)

### Members

- `CouldNotConnect`: We failed to connect to the debugged process
- `CouldNotBreak`: Could not break the debugged process

