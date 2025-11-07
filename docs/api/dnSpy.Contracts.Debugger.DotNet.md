# Namespace `dnSpy.Contracts.Debugger.DotNet`

## Class `DbgDotNetInternalAppDomain`

Base class of a .NET app domain object implemented by the .NET debug engine

**Inherits/Implements:** `DbgInternalAppDomain`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.DbgDotNetInternalAppDomain and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.DbgDotNetInternalAppDomain(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/DbgDotNetInternalAppDomain.cs` (line 26)

### Properties

- `public abstract DmdAppDomain ReflectionAppDomain { get; }`
  - Summary: Gets the reflection app domain
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/DbgDotNetInternalAppDomain.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReflectionAppDomain;
    ```

## Class `DbgDotNetInternalModule`

Base class of a .NET module object implemented by the .NET debug engine

**Inherits/Implements:** `DbgInternalModule`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.DbgDotNetInternalModule and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.DbgDotNetInternalModule(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/DbgDotNetInternalModule.cs` (line 26)

### Properties

- `public abstract DmdModule ReflectionModule { get; }`
  - Summary: Gets the reflection module or null if this isn't a managed module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/DbgDotNetInternalModule.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReflectionModule;
    ```

## Class `DbgDotNetInternalRuntime`

Base class of a .NET runtime object implemented by the .NET debug engine. It must implement

**Inherits/Implements:** `DbgInternalRuntime`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.DbgDotNetInternalRuntime and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.DbgDotNetInternalRuntime(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/DbgDotNetInternalRuntime.cs` (line 27)

### Properties

- `public abstract DmdRuntime ReflectionRuntime { get; }`
  - Summary: Gets the reflection runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/DbgDotNetInternalRuntime.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReflectionRuntime;
    ```

## Class `PredefinedDotNetDbgRuntimeTags`

Predefined tags ()

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DotNet.PredefinedDotNetDbgRuntimeTags members directly without instantiation.
dnSpy.Contracts.Debugger.DotNet.PredefinedDotNetDbgRuntimeTags./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/PredefinedDotNetDbgRuntimeTags.cs` (line 24)

### Fields

- `public const string DotNet = nameof(DotNet)`
  - Summary: .NET runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/PredefinedDotNetDbgRuntimeTags.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.PredefinedDotNetDbgRuntimeTags.DotNet;
    ```
- `public const string DotNetCore = nameof(DotNetCore)`
  - Summary: .NET Core runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/PredefinedDotNetDbgRuntimeTags.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.PredefinedDotNetDbgRuntimeTags.DotNetCore;
    ```
- `public const string DotNetFramework = nameof(DotNetFramework)`
  - Summary: .NET Framework runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/PredefinedDotNetDbgRuntimeTags.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.PredefinedDotNetDbgRuntimeTags.DotNetFramework;
    ```
- `public const string DotNetMono = nameof(DotNetMono)`
  - Summary: .NET Mono runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/PredefinedDotNetDbgRuntimeTags.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.PredefinedDotNetDbgRuntimeTags.DotNetMono;
    ```
- `public const string DotNetUnity = nameof(DotNetUnity)`
  - Summary: .NET Unity runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/PredefinedDotNetDbgRuntimeTags.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.PredefinedDotNetDbgRuntimeTags.DotNetUnity;
    ```

