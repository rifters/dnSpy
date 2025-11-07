# Namespace `dnSpy.Contracts.Debugger.Breakpoints.Modules`

## Struct `DbgBreakpointsModifiedEventArgs`

Breakpoints modified event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Modules.DbgBreakpointsModifiedEventArgs(breakpoints: /* ReadOnlyCollection<DbgModuleBreakpointAndOldSettings> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 131)

### Constructors

- `public DbgBreakpointsModifiedEventArgs(ReadOnlyCollection<DbgModuleBreakpointAndOldSettings> breakpoints)`
  - Summary: Constructor
  - Parameters:
    - `ReadOnlyCollection<DbgModuleBreakpointAndOldSettings> breakpoints`: Breakpoints and old settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 141)

### Properties

- `public ReadOnlyCollection<DbgModuleBreakpointAndOldSettings> Breakpoints { get; }`
  - Summary: Gets the breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 135)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoints;
    ```

## Class `DbgModuleBreakpoint`

Module breakpoint

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Modules.DbgModuleBreakpoint and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Modules.DbgModuleBreakpoint(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 24)

### Methods

- `public abstract void Remove()`
  - Summary: Removes this breakpoint from the module breakpoints list
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove();
    ```

### Properties

- `public abstract DbgModuleBreakpointSettings Settings { get; set; }`
  - Summary: Gets/sets the current settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```
- `public abstract bool IsEnabled { get; set; }`
  - Summary: true if the breakpoint is enabled
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnabled;
    ```
- `public abstract bool? IsDynamic { get; set; }`
  - Summary: true if dynamic, false if not dynamic, and null if any value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDynamic;
    ```
- `public abstract bool? IsInMemory { get; set; }`
  - Summary: true if in-memory, false if not in-memory, and null if any value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInMemory;
    ```
- `public abstract int Id { get; }`
  - Summary: Gets the unique module breakpoint id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public abstract int? Order { get; set; }`
  - Summary: Order or null if any value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public abstract string AppDomainName { get; set; }`
  - Summary: App domain name (case insensitive) or null/empty string if any name. Wildcards can be used
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomainName;
    ```
- `public abstract string ModuleName { get; set; }`
  - Summary: Name of module (case insensitive) or null/empty string if any name. Wildcards can be used
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleName;
    ```
- `public abstract string ProcessName { get; set; }`
  - Summary: Process name (case insensitive) or null/empty string if any name. Wildcards can be used
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpoint.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessName;
    ```

## Struct `DbgModuleBreakpointAndOldSettings`

Breakpoint and old settings

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Modules.DbgModuleBreakpointAndOldSettings(breakpoint: /* DbgModuleBreakpoint */, oldSettings: /* DbgModuleBreakpointSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 106)

### Constructors

- `public DbgModuleBreakpointAndOldSettings(DbgModuleBreakpoint breakpoint, DbgModuleBreakpointSettings oldSettings)`
  - Summary: Constructor
  - Parameters:
    - `DbgModuleBreakpoint breakpoint`: Breakpoint
    - `DbgModuleBreakpointSettings oldSettings`: Old settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 122)

### Properties

- `public DbgModuleBreakpoint Breakpoint { get; }`
  - Summary: Gets the breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 110)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoint;
    ```
- `public DbgModuleBreakpointSettings OldSettings { get; }`
  - Summary: Gets the old settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 115)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldSettings;
    ```

## Struct `DbgModuleBreakpointAndSettings`

Breakpoint and settings

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Modules.DbgModuleBreakpointAndSettings(breakpoint: /* DbgModuleBreakpoint */, settings: /* DbgModuleBreakpointSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 148)

### Constructors

- `public DbgModuleBreakpointAndSettings(DbgModuleBreakpoint breakpoint, DbgModuleBreakpointSettings settings)`
  - Summary: Constructor
  - Parameters:
    - `DbgModuleBreakpoint breakpoint`: Breakpoint
    - `DbgModuleBreakpointSettings settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 164)

### Properties

- `public DbgModuleBreakpoint Breakpoint { get; }`
  - Summary: Gets the breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 152)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoint;
    ```
- `public DbgModuleBreakpointSettings Settings { get; }`
  - Summary: Gets the new settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 157)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```

## Struct `DbgModuleBreakpointInfo`

Module info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Modules.DbgModuleBreakpointInfo(module: /* DbgModule */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointInfo.cs` (line 26)

### Constructors

- `public DbgModuleBreakpointInfo(DbgModule module)`
  - Summary: Constructor
  - Parameters:
    - `DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointInfo.cs` (line 61)

### Properties

- `public bool IsDynamic { get; }`
  - Summary: true if dynamic
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDynamic;
    ```
- `public bool IsInMemory { get; }`
  - Summary: true if in-memory
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointInfo.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInMemory;
    ```
- `public int Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointInfo.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string AppDomainName { get; }`
  - Summary: App domain name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointInfo.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomainName;
    ```
- `public string ModuleName { get; }`
  - Summary: Name of module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleName;
    ```
- `public string ProcessName { get; }`
  - Summary: Process name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointInfo.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessName;
    ```

## Struct `DbgModuleBreakpointSettings`

Module breakpoint settings

**Inherits/Implements:** `IEquatable<DbgModuleBreakpointSettings>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Modules.DbgModuleBreakpointSettings and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Modules.DbgModuleBreakpointSettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 26)

### Methods

- `public bool Equals(DbgModuleBreakpointSettings other)`
  - Summary: Compares this instance to
  - Parameters:
    - `DbgModuleBreakpointSettings other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgModuleBreakpointSettings */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 92)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public bool IsEnabled { get; set; }`
  - Summary: true if the breakpoint is enabled
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnabled;
    ```
- `public bool? IsDynamic { get; set; }`
  - Summary: true if dynamic, false if not dynamic, and null if any value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDynamic;
    ```
- `public bool? IsInMemory { get; set; }`
  - Summary: true if in-memory, false if not in-memory, and null if any value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInMemory;
    ```
- `public int? Order { get; set; }`
  - Summary: Module load order or null if any value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string AppDomainName { get; set; }`
  - Summary: App domain name (case insensitive) or null/empty string if any name. Wildcards can be used
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomainName;
    ```
- `public string ModuleName { get; set; }`
  - Summary: Name of module (case insensitive) or null/empty string if any name. Wildcards can be used
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleName;
    ```
- `public string ProcessName { get; set; }`
  - Summary: Process name (case insensitive) or null/empty string if any name. Wildcards can be used
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessName;
    ```

### Operators

- `public static bool operator !=(DbgModuleBreakpointSettings left, DbgModuleBreakpointSettings right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 64)
- `public static bool operator ==(DbgModuleBreakpointSettings left, DbgModuleBreakpointSettings right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointSettings.cs` (line 63)

## Class `DbgModuleBreakpointsService`

Module breakpoints service

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Modules.DbgModuleBreakpointsService and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Modules.DbgModuleBreakpointsService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 27)

### Methods

- `public DbgModuleBreakpoint Add(DbgModuleBreakpointSettings settings)`
  - Summary: Adds a breakpoint
  - Parameters:
    - `DbgModuleBreakpointSettings settings`: Breakpoint settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(settings: /* DbgModuleBreakpointSettings */);
    ```
- `public abstract DbgModuleBreakpoint[] Add(DbgModuleBreakpointSettings[] settings)`
  - Summary: Adds breakpoints
  - Parameters:
    - `DbgModuleBreakpointSettings[] settings`: Breakpoint settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(settings: /* DbgModuleBreakpointSettings[] */);
    ```
- `public abstract DbgModuleBreakpoint[] Find(in DbgModuleBreakpointInfo module)`
  - Summary: Finds breakpoints
  - Parameters:
    - `in DbgModuleBreakpointInfo module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.Find(module: /* DbgModuleBreakpointInfo */);
    ```
- `public abstract bool IsMatch(in DbgModuleBreakpointInfo module)`
  - Summary: Checks if matches at least one breakpoint
  - Parameters:
    - `in DbgModuleBreakpointInfo module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.IsMatch(module: /* DbgModuleBreakpointInfo */);
    ```
- `public abstract void Clear()`
  - Summary: Removes all module breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```
- `public abstract void Modify(DbgModuleBreakpointAndSettings[] settings)`
  - Summary: Modifies breakpoints
  - Parameters:
    - `DbgModuleBreakpointAndSettings[] settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Modify(settings: /* DbgModuleBreakpointAndSettings[] */);
    ```
- `public abstract void Remove(DbgModuleBreakpoint[] breakpoints)`
  - Summary: Removes breakpoints
  - Parameters:
    - `DbgModuleBreakpoint[] breakpoints`: Breakpoints to remove
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(breakpoints: /* DbgModuleBreakpoint[] */);
    ```
- `public void Modify(DbgModuleBreakpoint breakpoint, DbgModuleBreakpointSettings settings)`
  - Summary: Modifies a breakpoint
  - Parameters:
    - `DbgModuleBreakpoint breakpoint`: Breakpoint
    - `DbgModuleBreakpointSettings settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Modify(breakpoint: /* DbgModuleBreakpoint */, settings: /* DbgModuleBreakpointSettings */);
    ```
- `public void Remove(DbgModuleBreakpoint breakpoint)`
  - Summary: Removes a breakpoint
  - Parameters:
    - `DbgModuleBreakpoint breakpoint`: Breakpoint to remove
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(breakpoint: /* DbgModuleBreakpoint */);
    ```

### Properties

- `public abstract DbgModuleBreakpoint[] Breakpoints { get; }`
  - Summary: Gets all breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoints;
    ```

### Events

- `public abstract event EventHandler<DbgBreakpointsModifiedEventArgs> BreakpointsModified`
  - Summary: Raised when breakpoints are modified
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 45)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BreakpointsModified += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgModuleBreakpoint>> BreakpointsChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Modules/DbgModuleBreakpointsService.cs` (line 55)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BreakpointsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

