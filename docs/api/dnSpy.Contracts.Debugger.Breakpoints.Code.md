# Namespace `dnSpy.Contracts.Debugger.Breakpoints.Code`

## Struct `DbgBoundBreakpointsMessageChangedEventArgs`

changed event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBoundBreakpointsMessageChangedEventArgs(breakpoints: /* ReadOnlyCollection<DbgCodeBreakpoint> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 112)

### Constructors

- `public DbgBoundBreakpointsMessageChangedEventArgs(ReadOnlyCollection<DbgCodeBreakpoint> breakpoints)`
  - Summary: Constructor
  - Parameters:
    - `ReadOnlyCollection<DbgCodeBreakpoint> breakpoints`: Breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 122)

### Properties

- `public ReadOnlyCollection<DbgCodeBreakpoint> Breakpoints { get; }`
  - Summary: Gets all breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoints;
    ```

## Class `DbgBoundCodeBreakpoint`

A bound breakpoint. These only exist while debugging a program. A bound breakpoint is only created if the breakpoint is enabled.

**Inherits/Implements:** `DbgObject`, `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBoundCodeBreakpoint and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBoundCodeBreakpoint(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 29)

### Properties

- `public DbgProcess Process => Runtime.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DbgBoundCodeBreakpointMessage Message { get; }`
  - Summary: Gets the warning/error message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```
- `public abstract DbgCodeBreakpoint Breakpoint { get; }`
  - Summary: Gets the breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoint;
    ```
- `public abstract DbgModule Module { get; }`
  - Summary: Gets the module or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract ulong Address { get; }`
  - Summary: Gets the address of the breakpoint. This property is valid if is true
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```
- `public bool HasAddress => Address != DbgObjectFactory.BoundBreakpointNoAddress`
  - Summary: true if is a valid address
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasAddress;
    ```

### Events

- `public abstract event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 33)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `DbgBoundCodeBreakpointMessage`

Bound breakpoint message

**Inherits/Implements:** `IEquatable<DbgBoundCodeBreakpointMessage>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBoundCodeBreakpointMessage(severity: /* DbgBoundCodeBreakpointSeverity */, message: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 94)

### Constructors

- `public DbgBoundCodeBreakpointMessage(DbgBoundCodeBreakpointSeverity severity, string message)`
  - Summary: Constructor
  - Parameters:
    - `DbgBoundCodeBreakpointSeverity severity`: Severity
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 115)

### Methods

- `public bool Equals(DbgBoundCodeBreakpointMessage other)`
  - Summary: Compares this instance to
  - Parameters:
    - `DbgBoundCodeBreakpointMessage other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgBoundCodeBreakpointMessage */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 137)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 149)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DbgBoundCodeBreakpointSeverity Severity { get; }`
  - Summary: Gets the severity
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 103)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Severity;
    ```
- `public string Message { get; }`
  - Summary: Gets the message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 108)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```

### Fields

- `public static readonly DbgBoundCodeBreakpointMessage None = new DbgBoundCodeBreakpointMessage(DbgBoundCodeBreakpointSeverity.None, string.Empty)`
  - Summary: No error/warning message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 98)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBoundCodeBreakpointMessage.None;
    ```

### Operators

- `public static bool operator !=(DbgBoundCodeBreakpointMessage left, DbgBoundCodeBreakpointMessage right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 122)
- `public static bool operator ==(DbgBoundCodeBreakpointMessage left, DbgBoundCodeBreakpointMessage right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 121)

## Enum `DbgBoundCodeBreakpointSeverity`

Bound breakpoint message severity

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBoundCodeBreakpointSeverity and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBoundCodeBreakpointSeverity(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBoundCodeBreakpoint.cs` (line 74)

### Members

- `None`: No error/warning message
- `Warning`: Warning
- `Error`: Error

## Class `DbgBreakpointHitCheckEventArgs`

Breakpoint hit check event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBreakpointHitCheckEventArgs(boundBreakpoint: /* DbgBoundCodeBreakpoint */, thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 133)

### Constructors

- `public DbgBreakpointHitCheckEventArgs(DbgBoundCodeBreakpoint boundBreakpoint, DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `DbgBoundCodeBreakpoint boundBreakpoint`: Bound breakpoint
    - `DbgThread thread`: Thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 160)

### Properties

- `public DbgBoundCodeBreakpoint BoundBreakpoint { get; }`
  - Summary: Gets the bound breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 148)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BoundBreakpoint;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 153)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public bool Pause {
			get => pause;
			set => pause = value;
		}`
  - Summary: If false, it doesn't count as a hit and the process is not paused. If true, the normal BP settings decide if the process gets paused. The default value is true.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 139)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Pause;
    ```

## Class `DbgBreakpointHitEventArgs`

Breakpoint hit event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBreakpointHitEventArgs(boundBreakpoint: /* DbgBoundCodeBreakpoint */, thread: /* DbgThread */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 170)

### Constructors

- `public DbgBreakpointHitEventArgs(DbgBoundCodeBreakpoint boundBreakpoint, DbgThread thread)`
  - Summary: Constructor
  - Parameters:
    - `DbgBoundCodeBreakpoint boundBreakpoint`: Bound breakpoint
    - `DbgThread thread`: Thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 186)

### Properties

- `public DbgBoundCodeBreakpoint BoundBreakpoint { get; }`
  - Summary: Gets the bound breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 174)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BoundBreakpoint;
    ```
- `public DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 179)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```

## Class `DbgBreakpointLocationFormatter`

Formats some columns in the code breakpoints window

**Inherits/Implements:** `INotifyPropertyChanged`, `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBreakpointLocationFormatter and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBreakpointLocationFormatter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatter.cs` (line 28)

### Methods

- `protected void RaiseModuleChanged()`
  - Summary: Called when the module needs to be reformatted
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatter.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.RaiseModuleChanged();
    ```
- `protected void RaiseNameChanged()`
  - Summary: Called when the name needs to be reformatted
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatter.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.RaiseNameChanged();
    ```
- `public abstract void Dispose()`
  - Summary: Called when this instance isn't needed anymore
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatter.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```
- `public abstract void WriteModule(IDbgTextWriter output)`
  - Summary: Writes the module shown in the Module column
  - Parameters:
    - `IDbgTextWriter output`: Output
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatter.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteModule(output: /* IDbgTextWriter */);
    ```
- `public abstract void WriteName(IDbgTextWriter output, DbgBreakpointLocationFormatterOptions options)`
  - Summary: Writes the name shown in the Name column
  - Parameters:
    - `IDbgTextWriter output`: Output
    - `DbgBreakpointLocationFormatterOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatter.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(output: /* IDbgTextWriter */, options: /* DbgBreakpointLocationFormatterOptions */);
    ```

### Fields

- `public const string ModuleProperty = nameof(ModuleProperty)`
  - Summary: Name of the Module property
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatter.cs` (line 37)
  - Example:
    ```csharp
    var value = instance.ModuleProperty;
    ```
- `public const string NameProperty = nameof(NameProperty)`
  - Summary: Name of the Name property
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatter.cs` (line 32)
  - Example:
    ```csharp
    var value = instance.NameProperty;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatter.cs` (line 42)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Enum `DbgBreakpointLocationFormatterOptions`

Formatter options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBreakpointLocationFormatterOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBreakpointLocationFormatterOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatter.cs` (line 78)

### Members

- `None`: No bit is set
- `Tokens` = `x00000001`: Show metadata tokens
- `ModuleNames` = `x00000002`: Show module names
- `ParameterTypes` = `x00000004`: Show parameter types
- `ParameterNames` = `x00000008`: Show parameter names
- `DeclaringTypes` = `x00000010`: Show declaring types
- `ReturnTypes` = `x00000020`: Show return types
- `Namespaces` = `x00000040`: Show namespaces
- `IntrinsicTypeKeywords` = `x00000080`: Show intrinsic type keywords (eg. int instead of Int32)
- `DigitSeparators` = `x00000100`: Use digit separators
- `Decimal` = `x00000200`: Use decimal instead of hexadecimal

## Class `DbgBreakpointLocationFormatterProvider`

Creates formatters. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBreakpointLocationFormatterProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBreakpointLocationFormatterProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatterProvider.cs` (line 29)

### Methods

- `public abstract DbgBreakpointLocationFormatter Create(DbgCodeLocation location)`
  - Summary: Returns a formatter or null
  - Parameters:
    - `DbgCodeLocation location`: Breakpoint location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatterProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(location: /* DbgCodeLocation */);
    ```

## Struct `DbgBreakpointsModifiedEventArgs`

Breakpoints modified event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgBreakpointsModifiedEventArgs(breakpoints: /* ReadOnlyCollection<DbgCodeBreakpointAndOldSettings> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 154)

### Constructors

- `public DbgBreakpointsModifiedEventArgs(ReadOnlyCollection<DbgCodeBreakpointAndOldSettings> breakpoints)`
  - Summary: Constructor
  - Parameters:
    - `ReadOnlyCollection<DbgCodeBreakpointAndOldSettings> breakpoints`: Breakpoints and old settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 164)

### Properties

- `public ReadOnlyCollection<DbgCodeBreakpointAndOldSettings> Breakpoints { get; }`
  - Summary: Gets the breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 158)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoints;
    ```

## Class `DbgCodeBreakpoint`

Code breakpoint

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpoint and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpoint(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 28)

### Methods

- `public abstract void Remove()`
  - Summary: Removes the breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 127)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove();
    ```

### Properties

- `public abstract DbgBoundCodeBreakpointMessage BoundBreakpointsMessage { get; }`
  - Summary: Gets the bound breakpoints warning/error message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 117)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BoundBreakpointsMessage;
    ```
- `public abstract DbgBoundCodeBreakpoint[] BoundBreakpoints { get; }`
  - Summary: Gets all bound breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BoundBreakpoints;
    ```
- `public abstract DbgCodeBreakpointCondition? Condition { get; set; }`
  - Summary: Condition
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Condition;
    ```
- `public abstract DbgCodeBreakpointFilter? Filter { get; set; }`
  - Summary: Filter
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filter;
    ```
- `public abstract DbgCodeBreakpointHitCount? HitCount { get; set; }`
  - Summary: Hit count
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HitCount;
    ```
- `public abstract DbgCodeBreakpointOptions Options { get; }`
  - Summary: Gets the breakpoint options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```
- `public abstract DbgCodeBreakpointSettings Settings { get; set; }`
  - Summary: Gets/sets the current settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```
- `public abstract DbgCodeBreakpointTrace? Trace { get; set; }`
  - Summary: Trace message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Trace;
    ```
- `public abstract DbgCodeLocation Location { get; }`
  - Summary: Gets the breakpoint location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Location;
    ```
- `public abstract ReadOnlyCollection<string> Labels { get; set; }`
  - Summary: Labels
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Labels;
    ```
- `public abstract bool IsEnabled { get; set; }`
  - Summary: true if the breakpoint is enabled
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnabled;
    ```
- `public abstract int Id { get; }`
  - Summary: Gets the unique code breakpoint id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public bool IsHidden => (Options & DbgCodeBreakpointOptions.Hidden) != 0`
  - Summary: true if it's a hidden breakpoint. It's not shown in the UI (eg. breakpoints window, call stack window, glyph margin, text view)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsHidden;
    ```
- `public bool IsOneShot => (Options & DbgCodeBreakpointOptions.OneShot) != 0`
  - Summary: true if it's a one-shot breakpoint. When the breakpoint is hit, the process is paused and the breakpoint is removed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOneShot;
    ```
- `public bool IsTemporary => (Options & DbgCodeBreakpointOptions.Temporary) != 0`
  - Summary: true if it's a temporary breakpoint that gets removed when all debugged processes have exited
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsTemporary;
    ```

### Events

- `public abstract event EventHandler BoundBreakpointsMessageChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 122)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BoundBreakpointsMessageChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgBreakpointHitCheckEventArgs> HitCheck`
  - Summary: Can be used by code to add custom hit test conditions
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 37)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.HitCheck += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgBreakpointHitEventArgs> Hit`
  - Summary: Raised when the breakpoint is hit and the process will be paused
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 42)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Hit += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgBoundCodeBreakpoint>> BoundBreakpointsChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpoint.cs` (line 112)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BoundBreakpointsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `DbgCodeBreakpointAndHitCount`

Breakpoint and hit count

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointAndHitCount(breakpoint: /* DbgCodeBreakpoint */, hitCount: /* int? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 56)

### Constructors

- `public DbgCodeBreakpointAndHitCount(DbgCodeBreakpoint breakpoint, int? hitCount)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeBreakpoint breakpoint`: Breakpoint
    - `int? hitCount`: Current hit count or null if we're not debugging
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 72)

### Properties

- `public DbgCodeBreakpoint Breakpoint { get; }`
  - Summary: Gets the breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoint;
    ```
- `public int? HitCount { get; }`
  - Summary: Gets the current hit count. It's null if we're not debugging
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HitCount;
    ```

## Struct `DbgCodeBreakpointAndOldSettings`

Breakpoint and old settings

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointAndOldSettings(breakpoint: /* DbgCodeBreakpoint */, oldSettings: /* DbgCodeBreakpointSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 129)

### Constructors

- `public DbgCodeBreakpointAndOldSettings(DbgCodeBreakpoint breakpoint, DbgCodeBreakpointSettings oldSettings)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeBreakpoint breakpoint`: Breakpoint
    - `DbgCodeBreakpointSettings oldSettings`: Old settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 145)

### Properties

- `public DbgCodeBreakpoint Breakpoint { get; }`
  - Summary: Gets the breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 133)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoint;
    ```
- `public DbgCodeBreakpointSettings OldSettings { get; }`
  - Summary: Gets the old settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 138)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldSettings;
    ```

## Struct `DbgCodeBreakpointAndSettings`

Breakpoint and settings

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointAndSettings(breakpoint: /* DbgCodeBreakpoint */, settings: /* DbgCodeBreakpointSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 171)

### Constructors

- `public DbgCodeBreakpointAndSettings(DbgCodeBreakpoint breakpoint, DbgCodeBreakpointSettings settings)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeBreakpoint breakpoint`: Breakpoint
    - `DbgCodeBreakpointSettings settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 187)

### Properties

- `public DbgCodeBreakpoint Breakpoint { get; }`
  - Summary: Gets the breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 175)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoint;
    ```
- `public DbgCodeBreakpointSettings Settings { get; }`
  - Summary: Gets the new settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 180)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```

## Struct `DbgCodeBreakpointCondition`

Code breakpoint condition

**Inherits/Implements:** `IEquatable<DbgCodeBreakpointCondition>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointCondition(kind: /* DbgCodeBreakpointConditionKind */, condition: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 138)

### Constructors

- `public DbgCodeBreakpointCondition(DbgCodeBreakpointConditionKind kind, string condition)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeBreakpointConditionKind kind`: Condition kind
    - `string condition`: Condition expression
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 154)

### Methods

- `public bool Equals(DbgCodeBreakpointCondition other)`
  - Summary: Compares this instance to
  - Parameters:
    - `DbgCodeBreakpointCondition other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 169)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgCodeBreakpointCondition */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 176)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DbgCodeBreakpointConditionKind Kind { get; }`
  - Summary: Condition kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 142)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public string Condition { get; }`
  - Summary: Condition expression
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 147)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Condition;
    ```

### Operators

- `public static bool operator !=(DbgCodeBreakpointCondition left, DbgCodeBreakpointCondition right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 161)
- `public static bool operator ==(DbgCodeBreakpointCondition left, DbgCodeBreakpointCondition right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 160)

## Enum `DbgCodeBreakpointConditionKind`

Code breakpoint condition kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointConditionKind and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointConditionKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 123)

### Members

- `IsTrue`: Condition is true
- `WhenChanged`: Condition is changed

## Class `DbgCodeBreakpointDisplaySettings`

Code breakpoint display settings

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointDisplaySettings and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointDisplaySettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 26)

### Methods

- `protected void OnPropertyChanged(string propName)`
  - Summary: Raises
  - Parameters:
    - `string propName`: Name of property that got changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propName: /* string */);
    ```

### Properties

- `public abstract bool ShowDeclaringTypes { get; set; }`
  - Summary: Show declaring types
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowDeclaringTypes;
    ```
- `public abstract bool ShowIntrinsicTypeKeywords { get; set; }`
  - Summary: Show intrinsic type keywords (eg. int instead of Int32)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowIntrinsicTypeKeywords;
    ```
- `public abstract bool ShowModuleNames { get; set; }`
  - Summary: Show module names
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowModuleNames;
    ```
- `public abstract bool ShowNamespaces { get; set; }`
  - Summary: Show namespaces
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowNamespaces;
    ```
- `public abstract bool ShowParameterNames { get; set; }`
  - Summary: Show parameter names
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowParameterNames;
    ```
- `public abstract bool ShowParameterTypes { get; set; }`
  - Summary: Show parameter types
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowParameterTypes;
    ```
- `public abstract bool ShowReturnTypes { get; set; }`
  - Summary: Show return types
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowReturnTypes;
    ```
- `public abstract bool ShowTokens { get; set; }`
  - Summary: Show metadata tokens
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowTokens;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointDisplaySettings.cs` (line 30)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `DbgCodeBreakpointFilter`

Code breakpoint filter

**Inherits/Implements:** `IEquatable<DbgCodeBreakpointFilter>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointFilter(filter: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 270)

### Constructors

- `public DbgCodeBreakpointFilter(string filter)`
  - Summary: Constructor
  - Parameters:
    - `string filter`: Filter
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 280)

### Methods

- `public bool Equals(DbgCodeBreakpointFilter other)`
  - Summary: Compares this instance to
  - Parameters:
    - `DbgCodeBreakpointFilter other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 292)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgCodeBreakpointFilter */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 299)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 305)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 311)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public string Filter { get; }`
  - Summary: Filter
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 274)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filter;
    ```

### Operators

- `public static bool operator !=(DbgCodeBreakpointFilter left, DbgCodeBreakpointFilter right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 284)
- `public static bool operator ==(DbgCodeBreakpointFilter left, DbgCodeBreakpointFilter right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 283)

## Struct `DbgCodeBreakpointHitCount`

Hit count

**Inherits/Implements:** `IEquatable<DbgCodeBreakpointHitCount>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointHitCount(kind: /* DbgCodeBreakpointHitCountKind */, count: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 214)

### Constructors

- `public DbgCodeBreakpointHitCount(DbgCodeBreakpointHitCountKind kind, int count)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeBreakpointHitCountKind kind`: Hit count kind
    - `int count`: Hit count
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 230)

### Methods

- `public bool Equals(DbgCodeBreakpointHitCount other)`
  - Summary: Compares this instance to
  - Parameters:
    - `DbgCodeBreakpointHitCount other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 245)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgCodeBreakpointHitCount */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 252)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 258)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 264)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DbgCodeBreakpointHitCountKind Kind { get; }`
  - Summary: Hit count kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 218)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public int Count { get; }`
  - Summary: Hit count
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 223)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Count;
    ```

### Operators

- `public static bool operator !=(DbgCodeBreakpointHitCount left, DbgCodeBreakpointHitCount right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 237)
- `public static bool operator ==(DbgCodeBreakpointHitCount left, DbgCodeBreakpointHitCount right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 236)

## Enum `DbgCodeBreakpointHitCountKind`

Hit count kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointHitCountKind and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointHitCountKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 194)

### Members

- `Equals`: Hit count == value
- `MultipleOf`: (Hit count % value) == 0
- `GreaterThanOrEquals`: Hit count >= value

## Class `DbgCodeBreakpointHitCountService`

Breakpoint hit count service

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointHitCountService and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointHitCountService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 27)

### Methods

- `public abstract int? GetHitCount(DbgCodeBreakpoint breakpoint)`
  - Summary: Gets the hit count or null if we're not debugging
  - Parameters:
    - `DbgCodeBreakpoint breakpoint`: Breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHitCount(breakpoint: /* DbgCodeBreakpoint */);
    ```
- `public abstract void Reset(DbgCodeBreakpoint[] breakpoints)`
  - Summary: Resets the hit count
  - Parameters:
    - `DbgCodeBreakpoint[] breakpoints`: Breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Reset(breakpoints: /* DbgCodeBreakpoint[] */);
    ```
- `public void Reset(DbgCodeBreakpoint breakpoint)`
  - Summary: Resets the hit count
  - Parameters:
    - `DbgCodeBreakpoint breakpoint`: Breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.Reset(breakpoint: /* DbgCodeBreakpoint */);
    ```

### Events

- `public abstract event EventHandler<DbgHitCountChangedEventArgs> HitCountChanged`
  - Summary: Raised when the hit count is updated
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 31)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.HitCountChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `DbgCodeBreakpointInfo`

Info needed to add a breakpoint

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointInfo(location: /* DbgCodeLocation */, settings: /* DbgCodeBreakpointSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 196)

### Constructors

- `public DbgCodeBreakpointInfo(DbgCodeLocation location, DbgCodeBreakpointSettings settings)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeLocation location`: Breakpoint location. If you don't own this location instance, you must call
    - `DbgCodeBreakpointSettings settings`: Breakpoint settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 217)
- `public DbgCodeBreakpointInfo(DbgCodeLocation location, DbgCodeBreakpointSettings settings, DbgCodeBreakpointOptions options)`
  - Summary: Constructor
  - Parameters:
    - `DbgCodeLocation location`: Breakpoint location. If you don't own this location instance, you must call
    - `DbgCodeBreakpointSettings settings`: Breakpoint settings
    - `DbgCodeBreakpointOptions options`: Breakpoint options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 229)

### Properties

- `public DbgCodeBreakpointOptions Options { get; }`
  - Summary: Breakpoint options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 210)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```
- `public DbgCodeBreakpointSettings Settings { get; }`
  - Summary: Breakpoint settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 205)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```
- `public DbgCodeLocation Location { get; }`
  - Summary: Breakpoint location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 200)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Location;
    ```

## Enum `DbgCodeBreakpointOptions`

options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointOptions.cs` (line 26)

### Members

- `None`: No bit is set
- `Temporary` = `x00000001`: It's a temporary breakpoint that gets removed when all debugged processes have exited
- `Hidden` = `x00000002`: It's a hidden breakpoint. It's not shown in the UI (eg. breakpoints window, call stack window, glyph margin, text view)
- `OneShot` = `x00000004`: It's a one-shot breakpoint. When the breakpoint is hit, the process is paused and the breakpoint is removed

## Struct `DbgCodeBreakpointSettings`

Code breakpoint settings

**Inherits/Implements:** `IEquatable<DbgCodeBreakpointSettings>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointSettings and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointSettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 27)

### Methods

- `public bool Equals(DbgCodeBreakpointSettings other)`
  - Summary: Compares this instance to
  - Parameters:
    - `DbgCodeBreakpointSettings other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgCodeBreakpointSettings */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public DbgCodeBreakpointCondition? Condition { get; set; }`
  - Summary: Condition
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Condition;
    ```
- `public DbgCodeBreakpointFilter? Filter { get; set; }`
  - Summary: Filter
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filter;
    ```
- `public DbgCodeBreakpointHitCount? HitCount { get; set; }`
  - Summary: Hit count
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HitCount;
    ```
- `public DbgCodeBreakpointTrace? Trace { get; set; }`
  - Summary: Trace message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Trace;
    ```
- `public ReadOnlyCollection<string> Labels { get; set; }`
  - Summary: Labels
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Labels;
    ```
- `public bool IsEnabled { get; set; }`
  - Summary: true if the breakpoint is enabled
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnabled;
    ```

### Operators

- `public static bool operator !=(DbgCodeBreakpointSettings left, DbgCodeBreakpointSettings right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 60)
- `public static bool operator ==(DbgCodeBreakpointSettings left, DbgCodeBreakpointSettings right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 59)

## Struct `DbgCodeBreakpointTrace`

Code breakpoint trace message

**Inherits/Implements:** `IEquatable<DbgCodeBreakpointTrace>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointTrace(message: /* string */, @continue: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 317)

### Constructors

- `public DbgCodeBreakpointTrace(string message, bool @continue)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
    - `bool @continue`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 333)

### Methods

- `public bool Equals(DbgCodeBreakpointTrace other)`
  - Summary: Compares this instance to
  - Parameters:
    - `DbgCodeBreakpointTrace other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 348)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgCodeBreakpointTrace */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 355)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 361)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 367)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public bool Continue { get; }`
  - Summary: true to continue execution (trace) or false to break (breakpoint)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 326)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Continue;
    ```
- `public string Message { get; }`
  - Summary: Message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 321)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```

### Operators

- `public static bool operator !=(DbgCodeBreakpointTrace left, DbgCodeBreakpointTrace right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 340)
- `public static bool operator ==(DbgCodeBreakpointTrace left, DbgCodeBreakpointTrace right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointSettings.cs` (line 339)

## Class `DbgCodeBreakpointsService`

Code breakpoints service

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointsService and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgCodeBreakpointsService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 30)

### Methods

- `public DbgCodeBreakpoint Add(DbgCodeBreakpointInfo breakpoint)`
  - Summary: Adds a breakpoint. If the breakpoint already exists, null is returned.
  - Parameters:
    - `DbgCodeBreakpointInfo breakpoint`: Breakpoint info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(breakpoint: /* DbgCodeBreakpointInfo */);
    ```
- `public abstract DbgCodeBreakpoint TryGetBreakpoint(DbgCodeLocation location)`
  - Summary: Returns an existing breakpoint at or null if none exists
  - Parameters:
    - `DbgCodeLocation location`: Location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetBreakpoint(location: /* DbgCodeLocation */);
    ```
- `public abstract DbgCodeBreakpoint[] Add(DbgCodeBreakpointInfo[] breakpoints)`
  - Summary: Adds breakpoints. Duplicate breakpoints are ignored.
  - Parameters:
    - `DbgCodeBreakpointInfo[] breakpoints`: Breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(breakpoints: /* DbgCodeBreakpointInfo[] */);
    ```
- `public abstract void Clear()`
  - Summary: Removes all visible breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```
- `public abstract void Modify(DbgCodeBreakpointAndSettings[] settings)`
  - Summary: Modifies breakpoints
  - Parameters:
    - `DbgCodeBreakpointAndSettings[] settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.Modify(settings: /* DbgCodeBreakpointAndSettings[] */);
    ```
- `public abstract void Remove(DbgCodeBreakpoint[] breakpoints)`
  - Summary: Removes breakpoints
  - Parameters:
    - `DbgCodeBreakpoint[] breakpoints`: Breakpoints to remove
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(breakpoints: /* DbgCodeBreakpoint[] */);
    ```
- `public void Modify(DbgCodeBreakpoint breakpoint, DbgCodeBreakpointSettings settings)`
  - Summary: Modifies a breakpoint
  - Parameters:
    - `DbgCodeBreakpoint breakpoint`: Breakpoint
    - `DbgCodeBreakpointSettings settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Modify(breakpoint: /* DbgCodeBreakpoint */, settings: /* DbgCodeBreakpointSettings */);
    ```
- `public void Remove(DbgCodeBreakpoint breakpoint)`
  - Summary: Removes a breakpoint
  - Parameters:
    - `DbgCodeBreakpoint breakpoint`: Breakpoint to remove
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(breakpoint: /* DbgCodeBreakpoint */);
    ```

### Properties

- `public IEnumerable<DbgCodeBreakpoint> VisibleBreakpoints => Breakpoints.Where(a => !a.IsHidden)`
  - Summary: Gets all visible breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VisibleBreakpoints;
    ```
- `public abstract DbgCodeBreakpoint[] Breakpoints { get; }`
  - Summary: Gets all breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoints;
    ```

### Events

- `public abstract event EventHandler<DbgBoundBreakpointsMessageChangedEventArgs> BoundBreakpointsMessageChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 106)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BoundBreakpointsMessageChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgBreakpointsModifiedEventArgs> BreakpointsModified`
  - Summary: Raised when breakpoints are modified
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 48)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BreakpointsModified += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgCodeBreakpoint>> BreakpointsChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 63)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BreakpointsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `DbgHitCountChangedEventArgs`

event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.DbgHitCountChangedEventArgs(breakpoints: /* ReadOnlyCollection<DbgCodeBreakpointAndHitCount> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 81)

### Constructors

- `public DbgHitCountChangedEventArgs(ReadOnlyCollection<DbgCodeBreakpointAndHitCount> breakpoints)`
  - Summary: Constructor
  - Parameters:
    - `ReadOnlyCollection<DbgCodeBreakpointAndHitCount> breakpoints`: Breakpoints and hit counts
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 91)

### Properties

- `public ReadOnlyCollection<DbgCodeBreakpointAndHitCount> Breakpoints { get; }`
  - Summary: Gets breakpoints and hit counts
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointHitCountService.cs` (line 85)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Breakpoints;
    ```

## Class `ExportDbgBreakpointLocationFormatterProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgBreakpointLocationFormatterProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.ExportDbgBreakpointLocationFormatterProviderAttribute(type: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatterProvider.cs` (line 47)

### Constructors

- `public ExportDbgBreakpointLocationFormatterProviderAttribute(string type)`
  - Summary: Constructor
  - Parameters:
    - `string type`: Type (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatterProvider.cs` (line 53)
- `public ExportDbgBreakpointLocationFormatterProviderAttribute(string[] types)`
  - Summary: Constructor
  - Parameters:
    - `string[] types`: Types (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatterProvider.cs` (line 60)

### Properties

- `public string[] Types { get; }`
  - Summary: Types (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatterProvider.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Types;
    ```

## Interface `IDbgBreakpointLocationFormatterProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.IDbgBreakpointLocationFormatterProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.IDbgBreakpointLocationFormatterProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatterProvider.cs` (line 39)

### Properties

- `string[] Types { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgBreakpointLocationFormatterProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Types;
    ```

## Interface `IDbgCodeBreakpointsServiceListener`

Export an instance to get created when gets created

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.IDbgCodeBreakpointsServiceListener and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.IDbgCodeBreakpointsServiceListener(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 239)

### Methods

- `void Initialize(DbgCodeBreakpointsService dbgCodeBreakpointsService)`
  - Summary: Called once by
  - Parameters:
    - `DbgCodeBreakpointsService dbgCodeBreakpointsService`: Breakpoints service
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/DbgCodeBreakpointsService.cs` (line 244)
  - Example:
    ```csharp
    // Example invocation
    instance.Initialize(dbgCodeBreakpointsService: /* DbgCodeBreakpointsService */);
    ```

