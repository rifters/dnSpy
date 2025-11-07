# Namespace `dnSpy.Contracts.Metadata`

## Class `ExportModuleIdFactoryProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IModuleIdFactoryProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Metadata.ExportModuleIdFactoryProviderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdFactoryProvider.cs` (line 45)

### Constructors

- `public ExportModuleIdFactoryProviderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdFactoryProvider.cs` (line 48)
- `public ExportModuleIdFactoryProviderAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order of this instance, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdFactoryProvider.cs` (line 54)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdFactoryProvider.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IModuleIdFactory`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Metadata.IModuleIdFactory and call its members.
var instance = new dnSpy.Contracts.Metadata.IModuleIdFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdFactory.cs` (line 26)

### Methods

- `ModuleId? Create(ModuleDef module)`
  - Summary: Creates a or returns null. The returned value can be cached so it must always produce the same value for the same input module.
  - Parameters:
    - `ModuleDef module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdFactory.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleDef */);
    ```

## Interface `IModuleIdFactoryProvider`

Creates a . Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Metadata.IModuleIdFactoryProvider and call its members.
var instance = new dnSpy.Contracts.Metadata.IModuleIdFactoryProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdFactoryProvider.cs` (line 28)

### Methods

- `IModuleIdFactory Create()`
  - Summary: Creates a or returns null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdFactoryProvider.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

## Interface `IModuleIdFactoryProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Metadata.IModuleIdFactoryProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Metadata.IModuleIdFactoryProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdFactoryProvider.cs` (line 37)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdFactoryProvider.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IModuleIdProvider`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Metadata.IModuleIdProvider and call its members.
var instance = new dnSpy.Contracts.Metadata.IModuleIdProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdProvider.cs` (line 26)

### Methods

- `ModuleId Create(ModuleDef module)`
  - Summary: Creates a
  - Parameters:
    - `ModuleDef module`: Module or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Metadata/IModuleIdProvider.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleDef */);
    ```

## Struct `ModuleId`

Module ID

**Inherits/Implements:** `IEquatable<ModuleId>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Metadata.ModuleId(asmFullName: /* string */, moduleName: /* string */, isDynamic: /* bool */, isInMemory: /* bool */, nameOnly: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 31)

### Constructors

- `public ModuleId(string asmFullName, string moduleName, bool isDynamic, bool isInMemory, bool nameOnly)`
  - Summary: Constructor
  - Parameters:
    - `string asmFullName`: Assembly full name
    - `string moduleName`: Module name
    - `bool isDynamic`: true if it's a dynamic module
    - `bool isInMemory`: true if it's an in-memory module
    - `bool nameOnly`: true if is ignored
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 86)

### Methods

- `public bool Equals(ModuleId other)`
  - Summary: Equals()
  - Parameters:
    - `ModuleId other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 177)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* ModuleId */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 201)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static ModuleId Create(ModuleDef module, bool isDynamic, bool isInMemory)`
  - Summary: Creates a
  - Parameters:
    - `ModuleDef module`: Module
    - `bool isDynamic`: true if it's a dynamic module
    - `bool isInMemory`: true if it's an in-memory module
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Metadata.ModuleId.Create(module: /* ModuleDef */, isDynamic: /* bool */, isInMemory: /* bool */);
    ```
- `public static ModuleId Create(string asmFullName, string moduleName, bool isDynamic, bool isInMemory, bool moduleNameOnly)`
  - Summary: Creates a
  - Parameters:
    - `string asmFullName`: Full name of assembly. Must be identical to
    - `string moduleName`: Name of module. This is the filename if is false, else it must be identical to
    - `bool isDynamic`: true if it's a dynamic module
    - `bool isInMemory`: true if it's an in-memory module
    - `bool moduleNameOnly`: true if is ignored
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Metadata.ModuleId.Create(asmFullName: /* string */, moduleName: /* string */, isDynamic: /* bool */, isInMemory: /* bool */, moduleNameOnly: /* bool */);
    ```
- `public static ModuleId Create(string moduleFilename)`
  - Summary: Creates a that was loaded from a file
  - Parameters:
    - `string moduleFilename`: Module filename
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Metadata.ModuleId.Create(moduleFilename: /* string */);
    ```
- `public static ModuleId CreateFromFile(ModuleDef module)`
  - Summary: Creates a that was loaded from a file
  - Parameters:
    - `ModuleDef module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 122)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Metadata.ModuleId.CreateFromFile(module: /* ModuleDef */);
    ```
- `public static ModuleId CreateInMemory(ModuleDef module)`
  - Summary: Creates an in-memory
  - Parameters:
    - `ModuleDef module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Metadata.ModuleId.CreateInMemory(module: /* ModuleDef */);
    ```

### Properties

- `public bool IsDynamic => (flags & Flags.IsDynamic) != 0`
  - Summary: true if it's a dynamic module
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDynamic;
    ```
- `public bool IsInMemory => (flags & Flags.IsInMemory) != 0`
  - Summary: true if it's an in-memory module and the file doesn't exist on disk
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInMemory;
    ```
- `public bool ModuleNameOnly => (flags & Flags.NameOnly) != 0`
  - Summary: true if isn't used when comparing this instance against other instances.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleNameOnly;
    ```
- `public string AssemblyFullName => asmFullName ?? string.Empty`
  - Summary: Gets the full name, identical to the dnlib assembly full name
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyFullName;
    ```
- `public string ModuleName => moduleName ?? string.Empty`
  - Summary: Name of module. This is the filename if is false, else it's
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleName;
    ```

### Operators

- `public static bool operator !=(ModuleId a, ModuleId b) => !a.Equals(b);`
  - Summary: operator!=()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 170)
- `public static bool operator ==(ModuleId a, ModuleId b) => a.Equals(b);`
  - Summary: operator==()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 162)
- `public static implicit operator ModuleId(string moduleFilename) => Create(moduleFilename);`
  - Summary: implicit operator
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleId.cs` (line 43)

## Class `ModuleIdFactoryProviderConstants`

constants

**Example**

```csharp
// Access dnSpy.Contracts.Metadata.ModuleIdFactoryProviderConstants members directly without instantiation.
dnSpy.Contracts.Metadata.ModuleIdFactoryProviderConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Metadata/ModuleIdFactoryProviderConstants.cs` (line 24)

### Fields

- `public const double OrderDebugger = 10000`
  - Summary: Order of debugger extension's
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Metadata/ModuleIdFactoryProviderConstants.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Metadata.ModuleIdFactoryProviderConstants.OrderDebugger;
    ```
- `public const double OrderDefault = double.MaxValue`
  - Summary: Default order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Metadata/ModuleIdFactoryProviderConstants.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Metadata.ModuleIdFactoryProviderConstants.OrderDefault;
    ```

## Struct `ModuleTokenId`

and token

**Inherits/Implements:** `IEquatable<ModuleTokenId>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Metadata.ModuleTokenId(module: /* ModuleId */, mdToken: /* MDToken */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleTokenId.cs` (line 27)

### Constructors

- `public ModuleTokenId(ModuleId module, MDToken mdToken)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module id
    - `MDToken mdToken`: Token
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleTokenId.cs` (line 45)
- `public ModuleTokenId(ModuleId module, int token)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module id
    - `int token`: Token
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleTokenId.cs` (line 64)
- `public ModuleTokenId(ModuleId module, uint token)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module id
    - `uint token`: Token
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleTokenId.cs` (line 54)

### Methods

- `public bool Equals(ModuleTokenId other)`
  - Summary: Equals()
  - Parameters:
    - `ModuleTokenId other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleTokenId.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* ModuleTokenId */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleTokenId.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleTokenId.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleTokenId.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public ModuleId Module => module`
  - Summary: Gets the module id
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleTokenId.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public uint Token => token`
  - Summary: Gets the token in the module
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Metadata/ModuleTokenId.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

