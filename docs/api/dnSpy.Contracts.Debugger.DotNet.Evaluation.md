# Namespace `dnSpy.Contracts.Debugger.DotNet.Evaluation`

## Struct `DbgDotNetAliasInfo`

Alias

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetAliasInfo(kind: /* DbgDotNetAliasInfoKind */, type: /* DmdType */, id: /* uint */, customTypeInfoId: /* Guid */, customTypeInfo: /* ReadOnlyCollection<byte> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetAliasInfo.cs` (line 28)

### Constructors

- `public DbgDotNetAliasInfo(DbgDotNetAliasInfoKind kind, DmdType type, uint id, Guid customTypeInfoId, ReadOnlyCollection<byte> customTypeInfo)`
  - Summary: Constructor
  - Parameters:
    - `DbgDotNetAliasInfoKind kind`: Alias kind
    - `DmdType type`: Alias type
    - `uint id`: Alias id
    - `Guid customTypeInfoId`: Custom type info ID
    - `ReadOnlyCollection<byte> customTypeInfo`: Custom type info understood by the EE or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetAliasInfo.cs` (line 62)

### Properties

- `public DbgDotNetAliasInfoKind Kind { get; }`
  - Summary: Alias kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetAliasInfo.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public DmdType Type { get; }`
  - Summary: Alias type
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetAliasInfo.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public uint Id { get; }`
  - Summary: Alias id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetAliasInfo.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

### Fields

- `public readonly Guid CustomTypeInfoId`
  - Summary: Custom type info ID
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetAliasInfo.cs` (line 52)
  - Example:
    ```csharp
    var value = instance.CustomTypeInfoId;
    ```
- `public readonly ReadOnlyCollection<byte> CustomTypeInfo`
  - Summary: Custom type info understood by the EE or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetAliasInfo.cs` (line 47)
  - Example:
    ```csharp
    var value = instance.CustomTypeInfo;
    ```

## Enum `DbgDotNetAliasInfoKind`

Alias kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetAliasInfoKind and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetAliasInfoKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetAliasInfo.cs` (line 74)

### Members

- `Exception`: An exception, eg. "$exception"
- `StowedException`: A stowed exception, eg. "$stowedexception"
- `ReturnValue`: A return value, eg. "$ReturnValue1"

## Struct `DbgDotNetArrayDimensionInfo`

Contains base index and length of an array dimension

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetArrayDimensionInfo(baseIndex: /* int */, length: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 148)

### Constructors

- `public DbgDotNetArrayDimensionInfo(int baseIndex, uint length)`
  - Summary: Constructor
  - Parameters:
    - `int baseIndex`: Base index
    - `uint length`: Number of elements in this dimension
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 164)

### Properties

- `public int BaseIndex { get; }`
  - Summary: Base index
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 152)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BaseIndex;
    ```
- `public uint Length { get; }`
  - Summary: Number of elements in this dimension
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 157)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```

## Class `DbgDotNetCustomTypeInfo`

Extra custom type info provided by the expression compiler and used by language formatters

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetCustomTypeInfo(customTypeInfoId: /* Guid */, customTypeInfo: /* ReadOnlyCollection<byte> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetCustomTypeInfo.cs` (line 27)

### Constructors

- `public DbgDotNetCustomTypeInfo(Guid customTypeInfoId, ReadOnlyCollection<byte> customTypeInfo)`
  - Summary: Constructor
  - Parameters:
    - `Guid customTypeInfoId`: Custom type info ID
    - `ReadOnlyCollection<byte> customTypeInfo`: Custom type info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetCustomTypeInfo.cs` (line 43)

### Properties

- `public Guid CustomTypeInfoId { get; }`
  - Summary: Gets the custom type info ID
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetCustomTypeInfo.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CustomTypeInfoId;
    ```
- `public ReadOnlyCollection<byte> CustomTypeInfo { get; }`
  - Summary: Gets the custom type info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetCustomTypeInfo.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CustomTypeInfo;
    ```

## Class `DbgDotNetDispatcher`

Invokes code on another thread.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetDispatcher and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetDispatcher(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetDispatcher.cs` (line 27)

### Methods

- `public abstract T Invoke<T>(Func<T> callback)`
  - Summary: Executes code on the dispatcher thread
  - Parameters:
    - `Func<T> callback`: Code to execute
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetDispatcher.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.Invoke(callback: /* Func<T> */);
    ```
- `public abstract bool CheckAccess()`
  - Summary: Checks whether the current thread is the dispatcher thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetDispatcher.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.CheckAccess();
    ```
- `public abstract void BeginInvoke(Action callback)`
  - Summary: Executes code asynchronously on the dispatcher thread. This method returns immediately even if it happens to be called on the dispatcher thread.
  - Parameters:
    - `Action callback`: Code to execute
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetDispatcher.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.BeginInvoke(callback: /* Action */);
    ```
- `public bool TryBeginInvoke(Action callback)`
  - Summary: Executes code asynchronously on the dispatcher thread. This method returns immediately even if it happens to be called on the dispatcher thread.
  - Parameters:
    - `Action callback`: Code to execute
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetDispatcher.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.TryBeginInvoke(callback: /* Action */);
    ```
- `public bool TryInvoke(Action callback)`
  - Summary: Executes code on the dispatcher thread
  - Parameters:
    - `Action callback`: Code to execute
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetDispatcher.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.TryInvoke(callback: /* Action */);
    ```
- `public bool TryInvoke<T>(Func<T> callback, out T result)`
  - Summary: Executes code on the dispatcher thread
  - Parameters:
    - `Func<T> callback`: Code to execute
    - `out T result`: Result if successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetDispatcher.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.TryInvoke(callback: /* Func<T> */, result: /* T */);
    ```
- `public void Invoke(Action callback)`
  - Summary: Executes code on the dispatcher thread
  - Parameters:
    - `Action callback`: Code to execute
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetDispatcher.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.Invoke(callback: /* Action */);
    ```
- `public void VerifyAccess()`
  - Summary: Throws if the current thread isn't the dispatcher thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetDispatcher.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.VerifyAccess();
    ```

## Struct `DbgDotNetExceptionInfo`

Exception info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetExceptionInfo(value: /* DbgDotNetValue */, id: /* uint */, flags: /* DbgDotNetExceptionInfoFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetExceptionInfo.cs` (line 26)

### Constructors

- `public DbgDotNetExceptionInfo(DbgDotNetValue value, uint id, DbgDotNetExceptionInfoFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `DbgDotNetValue value`: Exception value
    - `uint id`: Exception id
    - `DbgDotNetExceptionInfoFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetExceptionInfo.cs` (line 53)

### Properties

- `public DbgDotNetExceptionInfoFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetExceptionInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public DbgDotNetValue Value { get; }`
  - Summary: Gets the exception instance. There's no guarantee that it derives from .
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetExceptionInfo.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public bool IsStowedException => (Flags & DbgDotNetExceptionInfoFlags.StowedException) != 0`
  - Summary: true if it's a stowed exception
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetExceptionInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsStowedException;
    ```
- `public uint Id { get; }`
  - Summary: Gets the exception id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetExceptionInfo.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Enum `DbgDotNetExceptionInfoFlags`

Exception info flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetExceptionInfoFlags and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetExceptionInfoFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetExceptionInfo.cs` (line 63)

### Members

- `None`: No bit is set
- `StowedException` = `x00000001`: If set, it's a stowed exception, else it's an exception

## Enum `DbgDotNetInvokeOptions`

Invoke options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetInvokeOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetInvokeOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 345)

### Members

- `None`: No bit is set
- `NonVirtual` = `x00000001`: Non-virtual call

## Class `DbgDotNetLanguageGuids`

.NET language guids

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetLanguageGuids members directly without instantiation.
dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetLanguageGuids./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetLanguageGuids.cs` (line 24)

### Fields

- `public const string CSharp = "7860A5A1-BF16-484D-B292-FADE130CEFAE"`
  - Summary: C# language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetLanguageGuids.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetLanguageGuids.CSharp;
    ```
- `public const string VisualBasic = "7B3A65F9-5444-4389-B1BE-4C150AFC3246"`
  - Summary: Visual Basic language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetLanguageGuids.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetLanguageGuids.VisualBasic;
    ```

## Class `DbgDotNetObjectId`

References a value in the debugged process

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetObjectId and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetObjectId(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetObjectId.cs` (line 27)

### Methods

- `public abstract void Dispose()`
  - Summary: Called when its owner () gets closed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetObjectId.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Properties

- `public abstract uint Id { get; }`
  - Summary: Gets the unique id in the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetObjectId.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Struct `DbgDotNetRawModuleBytes`

Contains .NET module data information

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetRawModuleBytes(rawBytes: /* byte[] */, isFileLayout: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 418)

### Constructors

- `public DbgDotNetRawModuleBytes(byte[] rawBytes, bool isFileLayout)`
  - Summary: Constructor
  - Parameters:
    - `byte[] rawBytes`: Raw bytes of the .NET module
    - `bool isFileLayout`: true if it's file layout, false if it's memory layout
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 439)

### Properties

- `public bool IsFileLayout { get; }`
  - Summary: true if it's file layout, false if it's memory layout
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 427)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFileLayout;
    ```
- `public byte[] RawBytes { get; }`
  - Summary: Raw bytes of the .NET module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 432)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RawBytes;
    ```

### Fields

- `public static readonly DbgDotNetRawModuleBytes None = default`
  - Summary: No .NET module data is available
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 422)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetRawModuleBytes.None;
    ```

## Struct `DbgDotNetRawValue`

Raw value

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetRawValue(valueType: /* DbgSimpleValueType */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 173)

### Constructors

- `public DbgDotNetRawValue(DbgSimpleValueType valueType)`
  - Summary: Constructor
  - Parameters:
    - `DbgSimpleValueType valueType`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 194)
- `public DbgDotNetRawValue(DbgSimpleValueType valueType, object rawValue)`
  - Summary: Constructor
  - Parameters:
    - `DbgSimpleValueType valueType`: Type
    - `object rawValue`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 206)

### Properties

- `public DbgSimpleValueType ValueType { get; }`
  - Summary: Type of the value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 177)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueType;
    ```
- `public bool HasRawValue { get; }`
  - Summary: true if is valid
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 182)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasRawValue;
    ```
- `public object RawValue { get; }`
  - Summary: The value. It's only valid if is true. A null value is a valid value. If it's an enum value, it's stored as the enum's underlying type (eg. )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 188)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RawValue;
    ```

## Struct `DbgDotNetReturnValueInfo`

Contains a method and its return value

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetReturnValueInfo(id: /* uint */, method: /* DmdMethodBase */, value: /* DbgDotNetValue */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetReturnValueInfo.cs` (line 27)

### Constructors

- `public DbgDotNetReturnValueInfo(uint id, DmdMethodBase method, DbgDotNetValue value)`
  - Summary: Constructor
  - Parameters:
    - `uint id`: Return value id
    - `DmdMethodBase method`: Method
    - `DbgDotNetValue value`: Value returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetReturnValueInfo.cs` (line 49)

### Properties

- `public DbgDotNetValue Value { get; }`
  - Summary: Gets the value returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetReturnValueInfo.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public DmdMethodBase Method { get; }`
  - Summary: Gets the method
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetReturnValueInfo.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Method;
    ```
- `public uint Id { get; }`
  - Summary: Gets the return value id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetReturnValueInfo.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Class `DbgDotNetRuntimeConstants`

Constants

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetRuntimeConstants members directly without instantiation.
dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetRuntimeConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 398)

### Fields

- `public const uint ExceptionId = 1`
  - Summary: Exception ID
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 402)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetRuntimeConstants.ExceptionId;
    ```
- `public const uint LastReturnValueId = 0`
  - Summary: ID of last return value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 412)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetRuntimeConstants.LastReturnValueId;
    ```
- `public const uint StowedExceptionId = 1`
  - Summary: Stowed exception ID
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 407)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetRuntimeConstants.StowedExceptionId;
    ```

## Enum `DbgDotNetRuntimeFeatures`

.NET runtime features

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetRuntimeFeatures and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetRuntimeFeatures(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 361)

### Members

- `None`: No bit is set
- `ObjectIds` = `x00000001`: Object IDs are supported
- `NoGenericMethods` = `x00000002`: Calling generic methods isn't supported
- `NoDereferencePointers` = `x00000004`: and isn't supported for pointers.
- `NoAsyncStepObjectId` = `x00000008`: Async step with object ids isn't supported
- `NativeMethodBodies` = `x00000010`: It's possible to get the native code of jitted managed methods

## Class `DbgDotNetValue`

Result of evaluating an expression. All values are automatically closed when the runtime continues but they implement and should be disposed of earlier if possible.

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetValue and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetValue(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 31)

### Methods

- `public virtual DbgDotNetRawValue GetRawValue()`
  - Summary: Gets the raw value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 131)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRawValue();
    ```
- `public virtual DbgDotNetValueResult GetArrayElementAt(uint index)`
  - Summary: Gets the element at in the array. This method can be called even if it's a multi-dimensional array.
  - Parameters:
    - `uint index`: Zero-based index of the element
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.GetArrayElementAt(index: /* uint */);
    ```
- `public virtual DbgDotNetValueResult LoadIndirect()`
  - Summary: Gets the referenced value if it's a by-ref or a pointer
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadIndirect();
    ```
- `public virtual DbgDotNetValueResult? Box(DbgEvaluationInfo evalInfo)`
  - Summary: Boxes the value type, returns null on failure
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.Box(evalInfo: /* DbgEvaluationInfo */);
    ```
- `public virtual DbgDotNetValueResult? GetArrayElementAddressAt(uint index)`
  - Summary: Gets the address of the element at in the array or null if it's not supported. This method can be called even if it's a multi-dimensional array.
  - Parameters:
    - `uint index`: Zero-based index of the element
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.GetArrayElementAddressAt(index: /* uint */);
    ```
- `public virtual DbgRawAddressValue? GetRawAddressValue(bool onlyDataAddress)`
  - Summary: Gets the address of the value or null if there's no address available. The returned address gets invalid when the runtime continues.
  - Parameters:
    - `bool onlyDataAddress`: If true and if it's a supported type (eg. a simple type such as integers, floating point values, strings or byte arrays) the returned object contains the address of the actual value, else the returned address and length covers the whole object including vtable, method table or other special data.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRawAddressValue(onlyDataAddress: /* bool */);
    ```
- `public virtual IDbgDotNetRuntime TryGetDotNetRuntime()`
  - Summary: Returns the instance or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 137)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetDotNetRuntime();
    ```
- `public virtual bool GetArrayCount(out uint elementCount)`
  - Summary: Gets the number of elements of the array
  - Parameters:
    - `out uint elementCount`: Total number of elements in the array
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.GetArrayCount(elementCount: /* uint */);
    ```
- `public virtual bool GetArrayInfo(out uint elementCount, out DbgDotNetArrayDimensionInfo[] dimensionInfos)`
  - Summary: Gets array information if it's an array or returns false
  - Parameters:
    - `out uint elementCount`: Total number of elements in the array
    - `out DbgDotNetArrayDimensionInfo[] dimensionInfos`: Dimension base indexes and lengths
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.GetArrayInfo(elementCount: /* uint */, dimensionInfos: /* DbgDotNetArrayDimensionInfo[] */);
    ```
- `public virtual string SetArrayElementAt(DbgEvaluationInfo evalInfo, uint index, object value)`
  - Summary: Stores a value at in the array. This method can be called even if it's a multi-dimensional array. The return value is null or an error message.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint index`: Zero-based index of the element
    - `object value`: Value to store: A or a primitive number or a string or arrays of primitive numbers / strings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.SetArrayElementAt(evalInfo: /* DbgEvaluationInfo */, index: /* uint */, value: /* object */);
    ```
- `public virtual string StoreIndirect(DbgEvaluationInfo evalInfo, object value)`
  - Summary: Writes to the referenced value (by-ref or pointer). The return value is null or an error message.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `object value`: Value to store: A or a primitive number or a string or arrays of primitive numbers / strings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreIndirect(evalInfo: /* DbgEvaluationInfo */, value: /* object */);
    ```
- `public virtual void Dispose()`
  - Summary: Called when its owner () gets closed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 142)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Properties

- `public abstract DmdType Type { get; }`
  - Summary: Gets the type of the value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public virtual bool IsNull => false`
  - Summary: true if this is a null value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValue.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNull;
    ```

## Struct `DbgDotNetValueResult`

Return value of methods creating s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetValueResult and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetValueResult(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValueResult.cs` (line 26)

### Methods

- `public static DbgDotNetValueResult Create(DbgDotNetValue value)`
  - Summary: Creates a normal result
  - Parameters:
    - `DbgDotNetValue value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValueResult.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetValueResult.Create(value: /* DbgDotNetValue */);
    ```
- `public static DbgDotNetValueResult CreateError(string errorMessage)`
  - Summary: Creates an error result
  - Parameters:
    - `string errorMessage`: Error message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValueResult.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetValueResult.CreateError(errorMessage: /* string */);
    ```
- `public static DbgDotNetValueResult CreateException(DbgDotNetValue value)`
  - Summary: Creates an exception result
  - Parameters:
    - `DbgDotNetValue value`: Exception value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValueResult.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgDotNetValueResult.CreateException(value: /* DbgDotNetValue */);
    ```

### Properties

- `public DbgDotNetValue Value { get; }`
  - Summary: Gets the value or null if there was an error (). If is true, this is the thrown exception value.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValueResult.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public bool HasError => ErrorMessage != null`
  - Summary: true if there was an error, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValueResult.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasError;
    ```
- `public bool IsNormalResult => !HasError && !ValueIsException`
  - Summary: true if there's no error and no exception was thrown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValueResult.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNormalResult;
    ```
- `public bool ValueIsException { get; }`
  - Summary: true if contains the thrown exception instead of the expected return value / field value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValueResult.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueIsException;
    ```
- `public string ErrorMessage { get; }`
  - Summary: Gets the error message or null if there was no error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgDotNetValueResult.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ErrorMessage;
    ```

## Class `DbgLanguageDebugInfo`

Method debug info used by a .NET debugger language. An instance of this class is attached to a , see and

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgLanguageDebugInfo(methodDebugInfo: /* DbgMethodDebugInfo */, methodToken: /* int */, localVarSigTok: /* int */, methodVersion: /* int */, ilOffset: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 30)

### Constructors

- `public DbgLanguageDebugInfo(DbgMethodDebugInfo methodDebugInfo, int methodToken, int localVarSigTok, int methodVersion, uint ilOffset)`
  - Summary: Constructor
  - Parameters:
    - `DbgMethodDebugInfo methodDebugInfo`: Method debug info
    - `int methodToken`: Method token
    - `int localVarSigTok`: Method local variables signature token
    - `int methodVersion`: Method version number, a 1-based number
    - `uint ilOffset`: IL offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 64)

### Properties

- `public DbgMethodDebugInfo MethodDebugInfo { get; }`
  - Summary: Gets the method debug info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MethodDebugInfo;
    ```
- `public int LocalVarSigTok { get; }`
  - Summary: Gets the method local variables signature token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LocalVarSigTok;
    ```
- `public int MethodToken { get; }`
  - Summary: Gets the method token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MethodToken;
    ```
- `public int MethodVersion { get; }`
  - Summary: Gets the method version number, a 1-based number
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MethodVersion;
    ```
- `public uint ILOffset { get; }`
  - Summary: Gets the IL offset
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ILOffset;
    ```

## Class `DbgLanguageDebugInfoExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgLanguageDebugInfoExtensions members directly without instantiation.
dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgLanguageDebugInfoExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 78)

### Methods

- `public static DbgLanguageDebugInfo GetLanguageDebugInfo(this DbgEvaluationContext context)`
  - Summary: Gets the debug info and throws if there is none
  - Parameters:
    - `this DbgEvaluationContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgLanguageDebugInfoExtensions.GetLanguageDebugInfo(context: /* DbgEvaluationContext */);
    ```
- `public static DbgLanguageDebugInfo TryGetLanguageDebugInfo(this DbgEvaluationContext context)`
  - Summary: Gets the debug info or null if there's none
  - Parameters:
    - `this DbgEvaluationContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgLanguageDebugInfoExtensions.TryGetLanguageDebugInfo(context: /* DbgEvaluationContext */);
    ```
- `public static void SetLanguageDebugInfo(DbgEvaluationContext context, DbgLanguageDebugInfo debugInfo)`
  - Summary: Attaches to
  - Parameters:
    - `DbgEvaluationContext context`: Context
    - `DbgLanguageDebugInfo debugInfo`: Debug info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/DbgLanguageDebugInfo.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Evaluation.DbgLanguageDebugInfoExtensions.SetLanguageDebugInfo(context: /* DbgEvaluationContext */, debugInfo: /* DbgLanguageDebugInfo */);
    ```

## Interface `IDbgDotNetRuntime`

Implemented by a .NET engine, see

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.IDbgDotNetRuntime and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.IDbgDotNetRuntime(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 32)

### Methods

- `DbgDotNetAliasInfo[] GetAliases(DbgEvaluationInfo evalInfo)`
  - Summary: Gets aliases
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 154)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAliases(evalInfo: /* DbgEvaluationInfo */);
    ```
- `DbgDotNetExceptionInfo[] GetExceptions(DbgEvaluationInfo evalInfo)`
  - Summary: Gets all exceptions
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 161)
  - Example:
    ```csharp
    // Example invocation
    instance.GetExceptions(evalInfo: /* DbgEvaluationInfo */);
    ```
- `DbgDotNetObjectId CreateObjectId(DbgDotNetValue value, uint id)`
  - Summary: Creates an object id or returns null
  - Parameters:
    - `DbgDotNetValue value`: Value created by this runtime
    - `uint id`: Unique id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 277)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateObjectId(value: /* DbgDotNetValue */, id: /* uint */);
    ```
- `DbgDotNetRawModuleBytes GetRawModuleBytes(DbgModule module)`
  - Summary: Gets the module data or
  - Parameters:
    - `DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRawModuleBytes(module: /* DbgModule */);
    ```
- `DbgDotNetReturnValueInfo[] GetReturnValues(DbgEvaluationInfo evalInfo)`
  - Summary: Gets all return values
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 168)
  - Example:
    ```csharp
    // Example invocation
    instance.GetReturnValues(evalInfo: /* DbgEvaluationInfo */);
    ```
- `DbgDotNetValue GetException(DbgEvaluationInfo evalInfo, uint id)`
  - Summary: Gets an exception or null
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint id`: Exception id, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 176)
  - Example:
    ```csharp
    // Example invocation
    instance.GetException(evalInfo: /* DbgEvaluationInfo */, id: /* uint */);
    ```
- `DbgDotNetValue GetLocalValueAddress(DbgEvaluationInfo evalInfo, uint index, DmdType targetType)`
  - Summary: Gets the address of a local value or null if it's not supported
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint index`: Metadata index of local
    - `DmdType targetType`: Type of the local
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 237)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLocalValueAddress(evalInfo: /* DbgEvaluationInfo */, index: /* uint */, targetType: /* DmdType */);
    ```
- `DbgDotNetValue GetParameterValueAddress(DbgEvaluationInfo evalInfo, uint index, DmdType targetType)`
  - Summary: Gets the address of a parameter value or null if it's not supported
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint index`: Metadata index of local
    - `DmdType targetType`: Type of the parameter
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 246)
  - Example:
    ```csharp
    // Example invocation
    instance.GetParameterValueAddress(evalInfo: /* DbgEvaluationInfo */, index: /* uint */, targetType: /* DmdType */);
    ```
- `DbgDotNetValue GetReturnValue(DbgEvaluationInfo evalInfo, uint id)`
  - Summary: Gets a return value or null
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint id`: Return value id, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 192)
  - Example:
    ```csharp
    // Example invocation
    instance.GetReturnValue(evalInfo: /* DbgEvaluationInfo */, id: /* uint */);
    ```
- `DbgDotNetValue GetStowedException(DbgEvaluationInfo evalInfo, uint id)`
  - Summary: Gets a stowed exception or null
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint id`: Stowed exception id, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 184)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStowedException(evalInfo: /* DbgEvaluationInfo */, id: /* uint */);
    ```
- `DbgDotNetValue GetValue(DbgEvaluationInfo evalInfo, DbgDotNetObjectId objectId)`
  - Summary: Gets an object ID's value or null if there was an error
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgDotNetObjectId objectId`: Object id created by this class
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 307)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValue(evalInfo: /* DbgEvaluationInfo */, objectId: /* DbgDotNetObjectId */);
    ```
- `DbgDotNetValue LoadFieldAddress(DbgEvaluationInfo evalInfo, DbgDotNetValue obj, DmdFieldInfo field)`
  - Summary: Loads the address of an instance or a static field or returns null if it's not supported
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgDotNetValue obj`: Instance object or null if it's a static field
    - `DmdFieldInfo field`: Field
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadFieldAddress(evalInfo: /* DbgEvaluationInfo */, obj: /* DbgDotNetValue */, field: /* DmdFieldInfo */);
    ```
- `DbgDotNetValueResult Box(DbgEvaluationInfo evalInfo, object value)`
  - Summary: Boxes the value type
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `object value`: Value to box
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 262)
  - Example:
    ```csharp
    // Example invocation
    instance.Box(evalInfo: /* DbgEvaluationInfo */, value: /* object */);
    ```
- `DbgDotNetValueResult Call(DbgEvaluationInfo evalInfo, DbgDotNetValue obj, DmdMethodBase method, object[] arguments, DbgDotNetInvokeOptions invokeOptions)`
  - Summary: Calls an instance or a static method
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgDotNetValue obj`: Instance object or null if it's a static method
    - `DmdMethodBase method`: Method
    - `object[] arguments`: Arguments: A or a primitive number or a string or arrays of primitive numbers / strings
    - `DbgDotNetInvokeOptions invokeOptions`: Invoke options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.Call(evalInfo: /* DbgEvaluationInfo */, obj: /* DbgDotNetValue */, method: /* DmdMethodBase */, arguments: /* object[] */, invokeOptions: /* DbgDotNetInvokeOptions */);
    ```
- `DbgDotNetValueResult CreateArray(DbgEvaluationInfo evalInfo, DmdType elementType, DbgDotNetArrayDimensionInfo[] dimensionInfos)`
  - Summary: Creates a multi-dimensional array
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DmdType elementType`: Element type
    - `DbgDotNetArrayDimensionInfo[] dimensionInfos`: Dimension infos
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 147)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateArray(evalInfo: /* DbgEvaluationInfo */, elementType: /* DmdType */, dimensionInfos: /* DbgDotNetArrayDimensionInfo[] */);
    ```
- `DbgDotNetValueResult CreateInstance(DbgEvaluationInfo evalInfo, DmdConstructorInfo ctor, object[] arguments, DbgDotNetInvokeOptions invokeOptions)`
  - Summary: Creates a new instance of a type by calling its constructor
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DmdConstructorInfo ctor`: Constructor
    - `object[] arguments`: Arguments: A or a primitive number or a string or arrays of primitive numbers / strings
    - `DbgDotNetInvokeOptions invokeOptions`: Invoke options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInstance(evalInfo: /* DbgEvaluationInfo */, ctor: /* DmdConstructorInfo */, arguments: /* object[] */, invokeOptions: /* DbgDotNetInvokeOptions */);
    ```
- `DbgDotNetValueResult CreateInstanceNoConstructor(DbgEvaluationInfo evalInfo, DmdType type)`
  - Summary: Creates a new instance of a type. All fields are initialized to 0 or null. The constructor isn't called.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DmdType type`: Type to create
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 129)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInstanceNoConstructor(evalInfo: /* DbgEvaluationInfo */, type: /* DmdType */);
    ```
- `DbgDotNetValueResult CreateSZArray(DbgEvaluationInfo evalInfo, DmdType elementType, int length)`
  - Summary: Creates an SZ array
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DmdType elementType`: Element type
    - `int length`: Length of the array
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 138)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateSZArray(evalInfo: /* DbgEvaluationInfo */, elementType: /* DmdType */, length: /* int */);
    ```
- `DbgDotNetValueResult CreateValue(DbgEvaluationInfo evalInfo, object value)`
  - Summary: Creates a simple value (a primitive number or a string, or arrays of those types)
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `object value`: A or a primitive number or a string or arrays of primitive numbers / strings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 254)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateValue(evalInfo: /* DbgEvaluationInfo */, value: /* object */);
    ```
- `DbgDotNetValueResult GetLocalValue(DbgEvaluationInfo evalInfo, uint index)`
  - Summary: Gets a local value
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint index`: Metadata index of local
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 200)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLocalValue(evalInfo: /* DbgEvaluationInfo */, index: /* uint */);
    ```
- `DbgDotNetValueResult GetParameterValue(DbgEvaluationInfo evalInfo, uint index)`
  - Summary: Gets a parameter value
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint index`: Metadata index of parameter
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 208)
  - Example:
    ```csharp
    // Example invocation
    instance.GetParameterValue(evalInfo: /* DbgEvaluationInfo */, index: /* uint */);
    ```
- `DbgDotNetValueResult LoadField(DbgEvaluationInfo evalInfo, DbgDotNetValue obj, DmdFieldInfo field)`
  - Summary: Loads an instance or a static field
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgDotNetValue obj`: Instance object or null if it's a static field
    - `DmdFieldInfo field`: Field
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadField(evalInfo: /* DbgEvaluationInfo */, obj: /* DbgDotNetValue */, field: /* DmdFieldInfo */);
    ```
- `DmdMethodBase GetFrameMethod(DbgEvaluationInfo evalInfo)`
  - Summary: Gets the current method or null if it's not a normal IL frame
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFrameMethod(evalInfo: /* DbgEvaluationInfo */);
    ```
- `ModuleId GetModuleId(DbgModule module)`
  - Summary: Gets the module id
  - Parameters:
    - `DbgModule module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetModuleId(module: /* DbgModule */);
    ```
- `bool CanCreateObjectId(DbgDotNetValue value)`
  - Summary: Returns true if it's possible to create an object id
  - Parameters:
    - `DbgDotNetValue value`: Value created by this runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 269)
  - Example:
    ```csharp
    // Example invocation
    instance.CanCreateObjectId(value: /* DbgDotNetValue */);
    ```
- `bool Equals(DbgDotNetObjectId objectId, DbgDotNetValue value)`
  - Summary: Checks if an object id and a value refer to the same data
  - Parameters:
    - `DbgDotNetObjectId objectId`: Object id created by this class
    - `DbgDotNetValue value`: Value created by this runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 285)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(objectId: /* DbgDotNetObjectId */, value: /* DbgDotNetValue */);
    ```
- `bool TryGetMethodToken(DbgModule module, int methodToken, out int metadataMethodToken, out int metadataLocalVarSigTok)`
  - Summary: Translates a method token from the original dynamic module's metadata to the saved module metadata used by the expression compiler
  - Parameters:
    - `DbgModule module`: Module
    - `int methodToken`: Method token
    - `out int metadataMethodToken`: New method token
    - `out int metadataLocalVarSigTok`: New method body local variables signature token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetMethodToken(module: /* DbgModule */, methodToken: /* int */, metadataMethodToken: /* int */, metadataLocalVarSigTok: /* int */);
    ```
- `bool TryGetNativeCode(DbgStackFrame frame, out DbgDotNetNativeCode nativeCode)`
  - Summary: Tries to get the native code
  - Parameters:
    - `DbgStackFrame frame`: Frame
    - `out DbgDotNetNativeCode nativeCode`: Updated with the native code if successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 323)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetNativeCode(frame: /* DbgStackFrame */, nativeCode: /* DbgDotNetNativeCode */);
    ```
- `bool TryGetNativeCode(DmdMethodBase method, out DbgDotNetNativeCode nativeCode)`
  - Summary: Tries to get the native code
  - Parameters:
    - `DmdMethodBase method`: Method
    - `out DbgDotNetNativeCode nativeCode`: Updated with the native code if successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 331)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetNativeCode(method: /* DmdMethodBase */, nativeCode: /* DbgDotNetNativeCode */);
    ```
- `bool TryGetSymbol(ulong address, out SymbolResolverResult result)`
  - Summary: Tries to get a symbol
  - Parameters:
    - `ulong address`: Address
    - `out SymbolResolverResult result`: Updated with the symbol if successful
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 339)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetSymbol(address: /* ulong */, result: /* SymbolResolverResult */);
    ```
- `bool? Equals(DbgDotNetValue a, DbgDotNetValue b)`
  - Summary: Checks if two values are equal. Returns null if it's unknown.
  - Parameters:
    - `DbgDotNetValue a`: Value #1
    - `DbgDotNetValue b`: Value #2
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 315)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* DbgDotNetValue */, b: /* DbgDotNetValue */);
    ```
- `int GetHashCode(DbgDotNetObjectId objectId)`
  - Summary: Gets the hash code of an object id
  - Parameters:
    - `DbgDotNetObjectId objectId`: Object id created by this class
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 292)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(objectId: /* DbgDotNetObjectId */);
    ```
- `int GetHashCode(DbgDotNetValue value)`
  - Summary: Gets the hash code of a value created by this runtime
  - Parameters:
    - `DbgDotNetValue value`: Value created by this runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 299)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(value: /* DbgDotNetValue */);
    ```
- `string SetLocalValue(DbgEvaluationInfo evalInfo, uint index, DmdType targetType, object value)`
  - Summary: Writes a new local value. Returns an error message or null.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint index`: Metadata index of parameter
    - `DmdType targetType`: Type of the local
    - `object value`: New value: A or a primitive number or a string or arrays of primitive numbers / strings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 218)
  - Example:
    ```csharp
    // Example invocation
    instance.SetLocalValue(evalInfo: /* DbgEvaluationInfo */, index: /* uint */, targetType: /* DmdType */, value: /* object */);
    ```
- `string SetParameterValue(DbgEvaluationInfo evalInfo, uint index, DmdType targetType, object value)`
  - Summary: Writes a new parameter value. Returns an error message or null.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint index`: Metadata index of parameter
    - `DmdType targetType`: Type of the parameter
    - `object value`: New value: A or a primitive number or a string or arrays of primitive numbers / strings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 228)
  - Example:
    ```csharp
    // Example invocation
    instance.SetParameterValue(evalInfo: /* DbgEvaluationInfo */, index: /* uint */, targetType: /* DmdType */, value: /* object */);
    ```
- `string StoreField(DbgEvaluationInfo evalInfo, DbgDotNetValue obj, DmdFieldInfo field, object value)`
  - Summary: Stores a value in a field. Returns null or an error message
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgDotNetValue obj`: Instance object or null if it's a static field
    - `DmdFieldInfo field`: Field
    - `object value`: Value to store: A or a primitive number or a string or arrays of primitive numbers / strings
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreField(evalInfo: /* DbgEvaluationInfo */, obj: /* DbgDotNetValue */, field: /* DmdFieldInfo */, value: /* object */);
    ```

### Properties

- `DbgDotNetDispatcher Dispatcher { get; }`
  - Summary: Gets the dispatcher
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Dispatcher;
    ```
- `DbgDotNetRuntimeFeatures Features { get; }`
  - Summary: Gets the feature flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/IDbgDotNetRuntime.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Features;
    ```

