# Namespace `dnSpy.Contracts.Debugger.Exceptions`

## Class `DbgException`

Thrown exception in the debugged process

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.DbgException and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgException(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 24)

### Properties

- `public DbgProcess Process => Runtime.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DbgExceptionEventFlags Flags { get; }`
  - Summary: Gets the exception event flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public abstract DbgExceptionId Id { get; }`
  - Summary: Gets the exception id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public abstract DbgModule Module { get; }`
  - Summary: Module where exception was thrown or null if it's not known
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract DbgThread Thread { get; }`
  - Summary: Thread where exception was thrown or null if it's not known
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public abstract string Message { get; }`
  - Summary: Exception message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```
- `public bool IsFirstChance => (Flags & DbgExceptionEventFlags.FirstChance) != 0`
  - Summary: true if it's a first chance exception
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFirstChance;
    ```
- `public bool IsSecondChance => (Flags & DbgExceptionEventFlags.SecondChance) != 0`
  - Summary: true if it's a second chance exception
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSecondChance;
    ```
- `public bool IsUnhandled => (Flags & DbgExceptionEventFlags.Unhandled) != 0`
  - Summary: true if it's an unhandled exception. The program will be terminated if it tries to run again.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgException.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsUnhandled;
    ```

## Struct `DbgExceptionCategoryDefinition`

Exception category definition

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionCategoryDefinition(flags: /* DbgExceptionCategoryDefinitionFlags */, name: /* string */, displayName: /* string */, shortDisplayName: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionCategoryDefinition.cs` (line 26)

### Constructors

- `public DbgExceptionCategoryDefinition(DbgExceptionCategoryDefinitionFlags flags, string name, string displayName, string shortDisplayName)`
  - Summary: Constructor
  - Parameters:
    - `DbgExceptionCategoryDefinitionFlags flags`: Flags
    - `string name`: Name, see also
    - `string displayName`: Localized name shown in the UI
    - `string shortDisplayName`: Shorter localized name shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionCategoryDefinition.cs` (line 54)

### Methods

- `public override string ToString()`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionCategoryDefinition.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DbgExceptionCategoryDefinitionFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionCategoryDefinition.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public string DisplayName { get; }`
  - Summary: Localized name shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionCategoryDefinition.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DisplayName;
    ```
- `public string Name { get; }`
  - Summary: Name, see also
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionCategoryDefinition.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public string ShortDisplayName { get; }`
  - Summary: Shorter localized name shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionCategoryDefinition.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShortDisplayName;
    ```

## Enum `DbgExceptionCategoryDefinitionFlags`

Exception category flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.DbgExceptionCategoryDefinitionFlags and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionCategoryDefinitionFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionCategoryDefinitionFlags.cs` (line 26)

### Members

- `None`: No bit is set
- `Code` = `x00000001`: Exceptions are integer codes instead of strings
- `DecimalCode` = `x00000002`: Exception code should be displayed in decimal and not in hexadecimal
- `UnsignedCode` = `x00000004`: Exception code is an unsigned integer

## Struct `DbgExceptionConditionSettings`

Exception condition settings

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionConditionSettings(conditionType: /* DbgExceptionConditionType */, condition: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionConditionSettings.cs` (line 26)

### Constructors

- `public DbgExceptionConditionSettings(DbgExceptionConditionType conditionType, string condition)`
  - Summary: Constructor
  - Parameters:
    - `DbgExceptionConditionType conditionType`: Condition type
    - `string condition`: Condition
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionConditionSettings.cs` (line 42)

### Properties

- `public DbgExceptionConditionType ConditionType { get; }`
  - Summary: Exception condition type
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionConditionSettings.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ConditionType;
    ```
- `public string Condition { get; }`
  - Summary: Exception condition
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionConditionSettings.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Condition;
    ```

## Enum `DbgExceptionConditionType`

Exception condition type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.DbgExceptionConditionType and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionConditionType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionConditionSettings.cs` (line 51)

### Members

- `ModuleNameEquals`: Module name equals
- `ModuleNameNotEquals`: Module name does not equal

## Struct `DbgExceptionDefinition`

Exception definition

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionDefinition(id: /* DbgExceptionId */, flags: /* DbgExceptionDefinitionFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinition.cs` (line 26)

### Constructors

- `public DbgExceptionDefinition(DbgExceptionId id, DbgExceptionDefinitionFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `DbgExceptionId id`: Exception id
    - `DbgExceptionDefinitionFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinition.cs` (line 47)
- `public DbgExceptionDefinition(DbgExceptionId id, DbgExceptionDefinitionFlags flags, string description)`
  - Summary: Constructor
  - Parameters:
    - `DbgExceptionId id`: Exception id
    - `DbgExceptionDefinitionFlags flags`: Flags
    - `string description`: Description shown in the UI or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinition.cs` (line 57)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinition.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DbgExceptionDefinitionFlags Flags { get; }`
  - Summary: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinition.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public DbgExceptionId Id { get; }`
  - Summary: Exception ID
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinition.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public string Description { get; }`
  - Summary: Description shown in the UI or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinition.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Description;
    ```

## Enum `DbgExceptionDefinitionFlags`

Exception definition flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.DbgExceptionDefinitionFlags and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionDefinitionFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinitionFlags.cs` (line 26)

### Members

- `None`: No bit is set
- `StopFirstChance` = `x00000001`: Stop at first firing of exception
- `StopSecondChance` = `x00000002`: Stop at second firing of exception

## Class `DbgExceptionDefinitionProvider`

Provides exception category definitions and exception definitions. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.DbgExceptionDefinitionProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionDefinitionProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinitionProvider.cs` (line 29)

### Methods

- `public virtual IEnumerable<DbgExceptionCategoryDefinition> CreateCategories()`
  - Summary: Returns all exception category definitions
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinitionProvider.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateCategories();
    ```
- `public virtual IEnumerable<DbgExceptionDefinition> Create()`
  - Summary: Returns all exception definitions
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinitionProvider.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```
- `public virtual IEnumerable<string> GetExceptionFilenames()`
  - Summary: Gets exception files (*.ex.xml) that define exceptions and exception categories. If a relative filename is returned, it's relative to the assembly of the called type. There's no need to return files already in the debug directory.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinitionProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetExceptionFilenames();
    ```

## Enum `DbgExceptionEventFlags`

Exception event flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.DbgExceptionEventFlags and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionEventFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionEventFlags.cs` (line 26)

### Members

- `None`: No bit is set
- `FirstChance` = `x00000001`: First chance exception
- `SecondChance` = `x00000002`: Second chance exception
- `Unhandled` = `x00000004`: Unhandled exception. The program will be terminated if it tries to run again.

## Class `DbgExceptionFormatter`

Formats exceptions in the Exception Settings window. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.DbgExceptionFormatter and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionFormatter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionFormatter.cs` (line 29)

### Methods

- `public virtual bool WriteName(IDbgTextWriter writer, DbgExceptionDefinition definition)`
  - Summary: Writes the exception name. Returns true if it wrote the name.
  - Parameters:
    - `IDbgTextWriter writer`: Writer
    - `DbgExceptionDefinition definition`: Exception definition
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionFormatter.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(writer: /* IDbgTextWriter */, definition: /* DbgExceptionDefinition */);
    ```

## Struct `DbgExceptionId`

Exception ID

**Inherits/Implements:** `IEquatable<DbgExceptionId>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionId(category: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 26)

### Constructors

- `public DbgExceptionId(string category)`
  - Summary: Constructor for default ids
  - Parameters:
    - `string category`: Exception category, same as
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 76)
- `public DbgExceptionId(string category, int code)`
  - Summary: Constructor
  - Parameters:
    - `string category`: Exception category, same as
    - `int code`: Exception code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 100)
- `public DbgExceptionId(string category, string name)`
  - Summary: Constructor
  - Parameters:
    - `string category`: Exception category, same as
    - `string name`: Name of exception, must not be null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 88)
- `public DbgExceptionId(string category, uint code)`
  - Summary: Constructor
  - Parameters:
    - `string category`: Exception category, same as
    - `uint code`: Exception code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 112)

### Methods

- `public bool Equals(DbgExceptionId other)`
  - Summary: Equals()
  - Parameters:
    - `DbgExceptionId other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgExceptionId */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 147)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hashcode
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 166)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DbgExceptionIdKind Kind => (DbgExceptionIdKind)(flags & Flags.KindMask)`
  - Summary: Gets the id kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public bool HasCode => Kind == DbgExceptionIdKind.Code`
  - Summary: true if the exception has a code, and not a name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasCode;
    ```
- `public bool HasName => Kind == DbgExceptionIdKind.Name`
  - Summary: true if the exception has a name, and not a code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasName;
    ```
- `public bool IsDefaultId => Kind == DbgExceptionIdKind.DefaultId`
  - Summary: true if this is the default exception ID
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefaultId;
    ```
- `public int Code => code`
  - Summary: Exception code. This property is only valid if is true
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Code;
    ```
- `public string Category => category`
  - Summary: Exception category, same as
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Category;
    ```
- `public string Name => name`
  - Summary: Name of exception (case insensitive). This property is only valid if is true
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

### Operators

- `public static bool operator !=(DbgExceptionId left, DbgExceptionId right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 118)
- `public static bool operator ==(DbgExceptionId left, DbgExceptionId right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 117)

## Struct `DbgExceptionIdAndSettings`

Exception id and settings

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionIdAndSettings(id: /* DbgExceptionId */, settings: /* DbgExceptionSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 151)

### Constructors

- `public DbgExceptionIdAndSettings(DbgExceptionId id, DbgExceptionSettings settings)`
  - Summary: Constructor
  - Parameters:
    - `DbgExceptionId id`: Exception id
    - `DbgExceptionSettings settings`: Settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 167)

### Properties

- `public DbgExceptionId Id { get; }`
  - Summary: Gets the exception id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 155)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public DbgExceptionSettings Settings { get; }`
  - Summary: Gets the settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 160)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```

## Enum `DbgExceptionIdKind`

kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.DbgExceptionIdKind and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionIdKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionId.cs` (line 181)

### Members

- `DefaultId`: Default ID
- `Code`: Code
- `Name`: Name

## Struct `DbgExceptionSettings`

Exception settings

**Inherits/Implements:** `IEquatable<DbgExceptionSettings>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionSettings(flags: /* DbgExceptionDefinitionFlags */, conditions: /* ReadOnlyCollection<DbgExceptionConditionSettings> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettings.cs` (line 27)

### Constructors

- `public DbgExceptionSettings(DbgExceptionDefinitionFlags flags, ReadOnlyCollection<DbgExceptionConditionSettings> conditions = null)`
  - Summary: Constructor
  - Parameters:
    - `DbgExceptionDefinitionFlags flags`: Flags
    - `ReadOnlyCollection<DbgExceptionConditionSettings> conditions` (default: `null`): Conditions or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettings.cs` (line 43)

### Methods

- `public bool Equals(DbgExceptionSettings other)`
  - Summary: Equals()
  - Parameters:
    - `DbgExceptionSettings other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettings.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DbgExceptionSettings */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettings.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettings.cs` (line 92)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public DbgExceptionDefinitionFlags Flags { get; }`
  - Summary: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettings.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public ReadOnlyCollection<DbgExceptionConditionSettings> Conditions { get; }`
  - Summary: Conditions
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettings.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Conditions;
    ```

### Operators

- `public static bool operator !=(DbgExceptionSettings left, DbgExceptionSettings right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettings.cs` (line 51)
- `public static bool operator ==(DbgExceptionSettings left, DbgExceptionSettings right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettings.cs` (line 50)

## Struct `DbgExceptionSettingsInfo`

Contains the exception definition and exception settings

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionSettingsInfo(definition: /* DbgExceptionDefinition */, settings: /* DbgExceptionSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 122)

### Constructors

- `public DbgExceptionSettingsInfo(DbgExceptionDefinition definition, DbgExceptionSettings settings)`
  - Summary: Constructor
  - Parameters:
    - `DbgExceptionDefinition definition`: Exception definition
    - `DbgExceptionSettings settings`: Exception settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 138)

### Properties

- `public DbgExceptionDefinition Definition { get; }`
  - Summary: Gets the definition
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 126)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Definition;
    ```
- `public DbgExceptionSettings Settings { get; }`
  - Summary: Gets the settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 131)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```

## Struct `DbgExceptionSettingsModifiedEventArgs`

event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionSettingsModifiedEventArgs(idAndSettings: /* ReadOnlyCollection<DbgExceptionIdAndSettings> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 180)

### Constructors

- `public DbgExceptionSettingsModifiedEventArgs(ReadOnlyCollection<DbgExceptionIdAndSettings> idAndSettings)`
  - Summary: Constructor
  - Parameters:
    - `ReadOnlyCollection<DbgExceptionIdAndSettings> idAndSettings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 190)

### Properties

- `public ReadOnlyCollection<DbgExceptionIdAndSettings> IdAndSettings { get; }`
  - Summary: Gets the ID and new settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 184)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IdAndSettings;
    ```

## Class `DbgExceptionSettingsService`

Exception settings service

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.DbgExceptionSettingsService and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.DbgExceptionSettingsService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 27)

### Methods

- `public abstract DbgExceptionSettings GetSettings(DbgExceptionId id)`
  - Summary: Returns exception settings. If the exception doesn't exist in the collection, the default exception settings is returned
  - Parameters:
    - `DbgExceptionId id`: Id of exception
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSettings(id: /* DbgExceptionId */);
    ```
- `public abstract bool TryGetCategoryDefinition(string category, out DbgExceptionCategoryDefinition definition)`
  - Summary: Gets the category definition if it exists
  - Parameters:
    - `string category`: Category, see
    - `out DbgExceptionCategoryDefinition definition`: Updated with the category definition if the method returns true
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetCategoryDefinition(category: /* string */, definition: /* DbgExceptionCategoryDefinition */);
    ```
- `public abstract bool TryGetDefinition(DbgExceptionId id, out DbgExceptionDefinition definition)`
  - Summary: Returns the exception definition if it exists
  - Parameters:
    - `DbgExceptionId id`: Exception id
    - `out DbgExceptionDefinition definition`: Updated with the exception definition if the method returns true
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetDefinition(id: /* DbgExceptionId */, definition: /* DbgExceptionDefinition */);
    ```
- `public abstract bool TryGetSettings(DbgExceptionId id, out DbgExceptionSettings settings)`
  - Summary: Returns exception settings or false if the exception doesn't exist in the collection
  - Parameters:
    - `DbgExceptionId id`: Id of exception
    - `out DbgExceptionSettings settings`: Updated with the exception settings if the method returns true
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetSettings(id: /* DbgExceptionId */, settings: /* DbgExceptionSettings */);
    ```
- `public abstract void Add(DbgExceptionSettingsInfo[] settings)`
  - Summary: Adds exceptions
  - Parameters:
    - `DbgExceptionSettingsInfo[] settings`: Exception settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(settings: /* DbgExceptionSettingsInfo[] */);
    ```
- `public abstract void Modify(DbgExceptionIdAndSettings[] settings)`
  - Summary: Modifies existing exceptions. It raises if the new settings are not equal to the current settings.
  - Parameters:
    - `DbgExceptionIdAndSettings[] settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Modify(settings: /* DbgExceptionIdAndSettings[] */);
    ```
- `public abstract void Remove(DbgExceptionId[] ids)`
  - Summary: Removes exception settings
  - Parameters:
    - `DbgExceptionId[] ids`: IDs of all exceptions to remove
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(ids: /* DbgExceptionId[] */);
    ```
- `public abstract void Reset()`
  - Summary: Resets all exception settings and removes user-added exceptions
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.Reset();
    ```
- `public void Add(in DbgExceptionSettingsInfo settings)`
  - Summary: Adds an exception
  - Parameters:
    - `in DbgExceptionSettingsInfo settings`: Exception settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(settings: /* DbgExceptionSettingsInfo */);
    ```
- `public void Modify(DbgExceptionId id, DbgExceptionSettings settings)`
  - Summary: Modifies an existing exception. It raises if the new settings are not equal to the current settings.
  - Parameters:
    - `DbgExceptionId id`: Id of existing exception
    - `DbgExceptionSettings settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Modify(id: /* DbgExceptionId */, settings: /* DbgExceptionSettings */);
    ```

### Properties

- `public abstract DbgExceptionSettingsInfo[] Exceptions { get; }`
  - Summary: Gets all exceptions
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Exceptions;
    ```
- `public abstract ReadOnlyCollection<DbgExceptionCategoryDefinition> CategoryDefinitions { get; }`
  - Summary: Gets all category definitions
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CategoryDefinitions;
    ```

### Events

- `public abstract event EventHandler<DbgCollectionChangedEventArgs<DbgExceptionSettingsInfo>> ExceptionsChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 80)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ExceptionsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<DbgExceptionSettingsModifiedEventArgs> ExceptionSettingsModified`
  - Summary: Raised when an exception is modified
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionSettingsService.cs` (line 52)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ExceptionSettingsModified += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `ExportDbgExceptionDefinitionProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgExceptionDefinitionProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Exceptions.ExportDbgExceptionDefinitionProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinitionProvider.cs` (line 66)

### Constructors

- `public ExportDbgExceptionDefinitionProviderAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinitionProvider.cs` (line 72)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinitionProvider.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportDbgExceptionFormatterAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgExceptionFormatterMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Exceptions.ExportDbgExceptionFormatterAttribute(category: /* string */, order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionFormatter.cs` (line 50)

### Constructors

- `public ExportDbgExceptionFormatterAttribute(string category, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string category`: Category, see
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionFormatter.cs` (line 57)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionFormatter.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string Category { get; }`
  - Summary: Category, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionFormatter.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Category;
    ```

## Interface `IDbgExceptionDefinitionProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.IDbgExceptionDefinitionProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.IDbgExceptionDefinitionProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinitionProvider.cs` (line 58)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionDefinitionProvider.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDbgExceptionFormatterMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Exceptions.IDbgExceptionFormatterMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Exceptions.IDbgExceptionFormatterMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionFormatter.cs` (line 40)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionFormatter.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string Category { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/DbgExceptionFormatter.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Category;
    ```

## Class `PredefinedExceptionCategories`

Predefined exception categories

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.Exceptions.PredefinedExceptionCategories members directly without instantiation.
dnSpy.Contracts.Debugger.Exceptions.PredefinedExceptionCategories./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Exceptions/PredefinedExceptionCategories.cs` (line 24)

### Fields

- `public const string DotNet = nameof(DotNet)`
  - Summary: .NET
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/PredefinedExceptionCategories.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Exceptions.PredefinedExceptionCategories.DotNet;
    ```
- `public const string MDA = nameof(MDA)`
  - Summary: MDA (Managed Debugging Assistants)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Exceptions/PredefinedExceptionCategories.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Exceptions.PredefinedExceptionCategories.MDA;
    ```

