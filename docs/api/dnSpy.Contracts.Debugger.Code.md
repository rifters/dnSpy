# Namespace `dnSpy.Contracts.Debugger.Code`

## Class `DbgCodeLocation`

Code location. There must be one owner per instance. If you must create a breakpoint using the same location, call and use the new instance as the breakpoint location.

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Code.DbgCodeLocation and call its members.
var instance = new dnSpy.Contracts.Debugger.Code.DbgCodeLocation(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocation.cs` (line 25)

### Methods

- `public abstract DbgCodeLocation Clone()`
  - Summary: Clones this instance. The returned instance can be used to create a breakpoint. Use to close it.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocation.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```
- `public abstract override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocation.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public abstract override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocation.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public abstract void Close()`
  - Summary: Closes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocation.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```

### Properties

- `public abstract string Type { get; }`
  - Summary: Unique type, see . There should be a 1-1 correspondence between this string and the derived type.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocation.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```

## Class `DbgCodeLocationSerializer`

serializer. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Code.DbgCodeLocationSerializer and call its members.
var instance = new dnSpy.Contracts.Debugger.Code.DbgCodeLocationSerializer(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocationSerializer.cs` (line 29)

### Methods

- `public abstract DbgCodeLocation Deserialize(ISettingsSection section)`
  - Summary: Deserializes a breakpoint location or returns null if it failed
  - Parameters:
    - `ISettingsSection section`: Serialized section
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocationSerializer.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Deserialize(section: /* ISettingsSection */);
    ```
- `public abstract void Serialize(ISettingsSection section, DbgCodeLocation location)`
  - Summary: Serializes
  - Parameters:
    - `ISettingsSection section`: Destination section
    - `DbgCodeLocation location`: Breakpoint location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocationSerializer.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Serialize(section: /* ISettingsSection */, location: /* DbgCodeLocation */);
    ```

## Class `ExportDbgCodeLocationSerializerAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgCodeLocationSerializerMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Code.ExportDbgCodeLocationSerializerAttribute(type: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocationSerializer.cs` (line 54)

### Constructors

- `public ExportDbgCodeLocationSerializerAttribute(string type)`
  - Summary: Constructor
  - Parameters:
    - `string type`: Type (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocationSerializer.cs` (line 60)
- `public ExportDbgCodeLocationSerializerAttribute(string[] types)`
  - Summary: Constructor
  - Parameters:
    - `string[] types`: Types (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocationSerializer.cs` (line 67)

### Properties

- `public string[] Types { get; }`
  - Summary: Types (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocationSerializer.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Types;
    ```

## Interface `IDbgCodeLocationSerializerMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Code.IDbgCodeLocationSerializerMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Code.IDbgCodeLocationSerializerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocationSerializer.cs` (line 46)

### Properties

- `string[] Types { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/DbgCodeLocationSerializer.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Types;
    ```

## Class `PredefinedDbgCodeLocationTypes`

Predefined types

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.Code.PredefinedDbgCodeLocationTypes members directly without instantiation.
dnSpy.Contracts.Debugger.Code.PredefinedDbgCodeLocationTypes./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Code/PredefinedDbgCodeLocationTypes.cs` (line 24)

### Fields

- `public const string DotNet = nameof(DotNet)`
  - Summary: .NET code location with a module, token, and IL offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/PredefinedDbgCodeLocationTypes.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Code.PredefinedDbgCodeLocationTypes.DotNet;
    ```
- `public const string DotNetCorDebugNative = nameof(DotNetCorDebugNative)`
  - Summary: .NET (CorDebug): native breakpoint location
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Code/PredefinedDbgCodeLocationTypes.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Code.PredefinedDbgCodeLocationTypes.DotNetCorDebugNative;
    ```

