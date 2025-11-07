# Namespace `dnSpy.Contracts.Debugger.DotNet.Evaluation.Engine`

## Class `DbgDotNetEngineObjectIdFactory`

A .NET . Use to export an instance.

**Inherits/Implements:** `DbgEngineObjectIdFactory`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.Engine.DbgDotNetEngineObjectIdFactory(runtimeGuid: /* Guid */, dbgDotNetLanguageService: /* DbgDotNetLanguageService */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Engine/DbgDotNetEngineObjectIdFactory.cs` (line 28)

### Constructors

- `protected DbgDotNetEngineObjectIdFactory(Guid runtimeGuid, DbgDotNetLanguageService dbgDotNetLanguageService)`
  - Summary: Constructor
  - Parameters:
    - `Guid runtimeGuid`: Runtime guid, see
    - `DbgDotNetLanguageService dbgDotNetLanguageService`: .NET language service instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Engine/DbgDotNetEngineObjectIdFactory.cs` (line 36)

### Methods

- `public sealed override DbgEngineObjectId CreateObjectId(DbgEngineValue value, uint id)`
  - Summary: Creates an object id or returns null
  - Parameters:
    - `DbgEngineValue value`: Value created by this runtime
    - `uint id`: Unique id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Engine/DbgDotNetEngineObjectIdFactory.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateObjectId(value: /* DbgEngineValue */, id: /* uint */);
    ```
- `public sealed override bool CanCreateObjectId(DbgEngineValue value)`
  - Summary: Returns true if it's possible to create an object id
  - Parameters:
    - `DbgEngineValue value`: Value created by this runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Engine/DbgDotNetEngineObjectIdFactory.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.CanCreateObjectId(value: /* DbgEngineValue */);
    ```
- `public sealed override bool Equals(DbgEngineObjectId objectId, DbgEngineValue value)`
  - Summary: Checks if an object id and a value refer to the same data
  - Parameters:
    - `DbgEngineObjectId objectId`: Object id created by this class
    - `DbgEngineValue value`: Value created by this runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Engine/DbgDotNetEngineObjectIdFactory.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(objectId: /* DbgEngineObjectId */, value: /* DbgEngineValue */);
    ```
- `public sealed override int GetHashCode(DbgEngineObjectId objectId)`
  - Summary: Gets the hash code of an object id
  - Parameters:
    - `DbgEngineObjectId objectId`: Object id created by this class
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Engine/DbgDotNetEngineObjectIdFactory.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(objectId: /* DbgEngineObjectId */);
    ```
- `public sealed override int GetHashCode(DbgEngineValue value)`
  - Summary: Gets the hash code of a value created by this runtime
  - Parameters:
    - `DbgEngineValue value`: Value created by this runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Engine/DbgDotNetEngineObjectIdFactory.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(value: /* DbgEngineValue */);
    ```

## Class `DbgDotNetLanguageService`

Used by a to create object id factories

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.Engine.DbgDotNetLanguageService and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.Engine.DbgDotNetLanguageService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Engine/DbgDotNetLanguageService.cs` (line 27)

### Methods

- `public abstract DbgEngineObjectIdFactory GetEngineObjectIdFactory(Guid runtimeGuid)`
  - Summary: Creates a
  - Parameters:
    - `Guid runtimeGuid`: Runtime guid, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Engine/DbgDotNetLanguageService.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEngineObjectIdFactory(runtimeGuid: /* Guid */);
    ```

