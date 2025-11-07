# Namespace `dnSpy.Contracts.Debugger.StartDebugging`

## Class `DbgProcessStarter`

Starts a process without debugging

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.StartDebugging.DbgProcessStarter and call its members.
var instance = new dnSpy.Contracts.Debugger.StartDebugging.DbgProcessStarter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 28)

### Methods

- `public abstract bool IsSupported(string filename)`
  - Summary: Checks if this instance supports starting the executable
  - Parameters:
    - `string filename`: Filename
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.IsSupported(filename: /* string */);
    ```
- `public abstract bool TryStart(string filename, out string error)`
  - Summary: Starts the executable. Returns false and an error message if it failed or throws an exception
  - Parameters:
    - `string filename`: Filename
    - `out string error`: Updated with an error message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.TryStart(filename: /* string */, error: /* string */);
    ```

## Class `ExportDbgProcessStarterAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgProcessStarterMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.StartDebugging.ExportDbgProcessStarterAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 54)

### Constructors

- `public ExportDbgProcessStarterAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 60)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportGenericDebugEngineGuidProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IGenericDebugEngineGuidProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.StartDebugging.ExportGenericDebugEngineGuidProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/GenericDebugEngineGuidProvider.cs` (line 46)

### Constructors

- `public ExportGenericDebugEngineGuidProviderAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/GenericDebugEngineGuidProvider.cs` (line 52)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/GenericDebugEngineGuidProvider.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `GenericDebugEngineGuidProvider`

Detects the debug engine that should be shown by default when showing the options. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.StartDebugging.GenericDebugEngineGuidProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.StartDebugging.GenericDebugEngineGuidProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/GenericDebugEngineGuidProvider.cs` (line 28)

### Methods

- `public abstract Guid? GetEngineGuid(string filename)`
  - Summary: Gets the guid of an engine (see )
  - Parameters:
    - `string filename`: Filename
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/GenericDebugEngineGuidProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEngineGuid(filename: /* string */);
    ```

## Interface `IDbgProcessStarterMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.StartDebugging.IDbgProcessStarterMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.StartDebugging.IDbgProcessStarterMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 46)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IGenericDebugEngineGuidProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.StartDebugging.IGenericDebugEngineGuidProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.StartDebugging.IGenericDebugEngineGuidProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/GenericDebugEngineGuidProvider.cs` (line 38)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/GenericDebugEngineGuidProvider.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `PredefinedDbgProcessStarterOrders`

Predefined order constants

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.StartDebugging.PredefinedDbgProcessStarterOrders members directly without instantiation.
dnSpy.Contracts.Debugger.StartDebugging.PredefinedDbgProcessStarterOrders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 72)

### Fields

- `public const double DefaultExe = double.MaxValue`
  - Summary: Default process starter that calls
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 81)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.PredefinedDbgProcessStarterOrders.DefaultExe;
    ```
- `public const double DotNetCore = 1000000`
  - Summary: .NET Core
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/DbgProcessStarter.cs` (line 76)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.PredefinedDbgProcessStarterOrders.DotNetCore;
    ```

## Class `PredefinedGenericDebugEngineGuidProviderOrders`

Predefined order constants

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.StartDebugging.PredefinedGenericDebugEngineGuidProviderOrders members directly without instantiation.
dnSpy.Contracts.Debugger.StartDebugging.PredefinedGenericDebugEngineGuidProviderOrders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/GenericDebugEngineGuidProvider.cs` (line 64)

### Fields

- `public const double DotNet = 1000000`
  - Summary: .NET Framework / .NET Core
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/GenericDebugEngineGuidProvider.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.PredefinedGenericDebugEngineGuidProviderOrders.DotNet;
    ```
- `public const double DotNetUnity = DotNet + 1`
  - Summary: Unity
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/GenericDebugEngineGuidProvider.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.PredefinedGenericDebugEngineGuidProviderOrders.DotNetUnity;
    ```

## Class `PredefinedGenericDebugEngineGuids`

Predefined generic debug engine guids

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.StartDebugging.PredefinedGenericDebugEngineGuids members directly without instantiation.
dnSpy.Contracts.Debugger.StartDebugging.PredefinedGenericDebugEngineGuids./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/PredefinedGenericDebugEngineGuids.cs` (line 26)

### Fields

- `public static readonly Guid DotNetCore = new Guid("7D294510-4730-433B-85C1-61EC0B4F6C3C")`
  - Summary: .NET Core
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/PredefinedGenericDebugEngineGuids.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.PredefinedGenericDebugEngineGuids.DotNetCore;
    ```
- `public static readonly Guid DotNetFramework = new Guid("0F99555D-5523-4AAE-BD4C-0451B9D50126")`
  - Summary: .NET Framework or compatible framework (eg. Mono)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/PredefinedGenericDebugEngineGuids.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.PredefinedGenericDebugEngineGuids.DotNetFramework;
    ```
- `public static readonly Guid DotNetUnity = new Guid("7FE300C8-C855-46F0-A3F4-2A18B4283C70")`
  - Summary: Unity
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/PredefinedGenericDebugEngineGuids.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.PredefinedGenericDebugEngineGuids.DotNetUnity;
    ```

