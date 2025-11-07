# Namespace `dnSpy.Debugger.DotNet.Interpreter`

## Enum `AddOpCodeKind`

Add opcode kind

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.AddOpCodeKind and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.AddOpCodeKind(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 279)

### Members

- `Add`: Normal addition
- `Add_Ovf`: Signed addition with an overflow check
- `Add_Ovf_Un`: Unsigned addition with an overflow check

## Class `ByRefILValue`

Managed pointer

**Inherits/Implements:** `ILValue`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.ByRefILValue and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.ByRefILValue(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 1042)

### Properties

- `public sealed override ILValueKind Kind => ILValueKind.ByRef`
  - Summary: Always returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 1046)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `ConstantFloatILValue`

64-bit floating point value (32-bit floating point numbers are extended to 64 bits)

**Inherits/Implements:** `ILValue`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.ConstantFloatILValue(appDomain: /* DmdAppDomain */, value: /* double */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 463)

### Constructors

- `public ConstantFloatILValue(DmdAppDomain appDomain, double value)`
  - Summary: Constructor
  - Parameters:
    - `DmdAppDomain appDomain`: AppDomain
    - `double value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 479)
- `public ConstantFloatILValue(DmdType type, double value)`
  - Summary: Constructor
  - Parameters:
    - `DmdType type`: Type, eg.
    - `double value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 491)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 505)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public double Value { get; }`
  - Summary: Gets the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 472)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public override DmdType Type { get; }`
  - Summary: Gets the type of the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 499)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public sealed override ILValueKind Kind => ILValueKind.Float`
  - Summary: Always returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 467)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `ConstantInt32ILValue`

32-bit integer. 1-byte, 2-byte and 4-byte integer values, booleans, and chars use this class. Smaller values are sign or zero extended.

**Inherits/Implements:** `ILValue`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.ConstantInt32ILValue(appDomain: /* DmdAppDomain */, value: /* int */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 355)

### Constructors

- `public ConstantInt32ILValue(DmdAppDomain appDomain, int value)`
  - Summary: Constructor
  - Parameters:
    - `DmdAppDomain appDomain`: AppDomain
    - `int value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 378)
- `public ConstantInt32ILValue(DmdType type, int value)`
  - Summary: Constructor
  - Parameters:
    - `DmdType type`: Type, eg.
    - `int value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 390)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 404)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public int Value { get; }`
  - Summary: Gets the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 364)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public override DmdType Type { get; }`
  - Summary: Gets the type of the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 398)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public sealed override ILValueKind Kind => ILValueKind.Int32`
  - Summary: Always returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 359)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public uint UnsignedValue => (uint)Value`
  - Summary: Gets the value as a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 369)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UnsignedValue;
    ```

## Class `ConstantInt64ILValue`

64-bit integer

**Inherits/Implements:** `ILValue`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.ConstantInt64ILValue(appDomain: /* DmdAppDomain */, value: /* long */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 410)

### Constructors

- `public ConstantInt64ILValue(DmdAppDomain appDomain, long value)`
  - Summary: Constructor
  - Parameters:
    - `DmdAppDomain appDomain`: AppDomain
    - `long value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 431)
- `public ConstantInt64ILValue(DmdType type, long value)`
  - Summary: Constructor
  - Parameters:
    - `DmdType type`: Type, eg.
    - `long value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 443)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 457)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public long Value { get; }`
  - Summary: Gets the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 419)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public override DmdType Type { get; }`
  - Summary: Gets the type of the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 451)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public sealed override ILValueKind Kind => ILValueKind.Int64`
  - Summary: Always returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 414)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public ulong UnsignedValue => (ulong)Value`
  - Summary: Gets the value as a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 424)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UnsignedValue;
    ```

## Class `ConstantNativeIntILValue`

native integer or unmanaged pointer

**Inherits/Implements:** `NativeIntILValue`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.ConstantNativeIntILValue(appDomain: /* DmdAppDomain */, value: /* int */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 521)

### Constructors

- `protected ConstantNativeIntILValue(DmdAppDomain appDomain, int value)`
  - Summary: Constructor
  - Parameters:
    - `DmdAppDomain appDomain`: AppDomain
    - `int value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 581)
- `protected ConstantNativeIntILValue(DmdAppDomain appDomain, long value)`
  - Summary: Constructor
  - Parameters:
    - `DmdAppDomain appDomain`: AppDomain
    - `long value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 593)
- `protected ConstantNativeIntILValue(DmdType type, int value)`
  - Summary: Constructor
  - Parameters:
    - `DmdType type`: Type, eg.
    - `int value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 605)
- `protected ConstantNativeIntILValue(DmdType type, long value)`
  - Summary: Constructor
  - Parameters:
    - `DmdType type`: Type, eg.
    - `long value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 615)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 629)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static ConstantNativeIntILValue Create32(DmdAppDomain appDomain, int value)`
  - Summary: Creates a 32-bit native int
  - Parameters:
    - `DmdAppDomain appDomain`: AppDomain
    - `int value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 550)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Interpreter.ConstantNativeIntILValue.Create32(appDomain: /* DmdAppDomain */, value: /* int */);
    ```
- `public static ConstantNativeIntILValue Create32(DmdType type, int value)`
  - Summary: Creates a 32-bit native int
  - Parameters:
    - `DmdType type`: Type, eg.
    - `int value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 566)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Interpreter.ConstantNativeIntILValue.Create32(type: /* DmdType */, value: /* int */);
    ```
- `public static ConstantNativeIntILValue Create64(DmdAppDomain appDomain, long value)`
  - Summary: Creates a 64-bit native int
  - Parameters:
    - `DmdAppDomain appDomain`: AppDomain
    - `long value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 558)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Interpreter.ConstantNativeIntILValue.Create64(appDomain: /* DmdAppDomain */, value: /* long */);
    ```
- `public static ConstantNativeIntILValue Create64(DmdType type, long value)`
  - Summary: Creates a 64-bit native int
  - Parameters:
    - `DmdType type`: Type, eg.
    - `long value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 574)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Interpreter.ConstantNativeIntILValue.Create64(type: /* DmdType */, value: /* long */);
    ```

### Properties

- `public int Value32 => (int)value`
  - Summary: Gets the value as a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 527)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value32;
    ```
- `public long Value64 => value`
  - Summary: Gets the value as a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 532)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value64;
    ```
- `public override DmdType Type { get; }`
  - Summary: Gets the type of the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 623)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public uint UnsignedValue32 => (uint)value`
  - Summary: Gets the value as a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 537)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UnsignedValue32;
    ```
- `public ulong UnsignedValue64 => (ulong)value`
  - Summary: Gets the value as a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 542)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UnsignedValue64;
    ```

## Enum `ConvOpCodeKind`

Convert opcode kind

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.ConvOpCodeKind and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.ConvOpCodeKind(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 319)

### Members

- `Conv_I`: Convert to a
- `Conv_Ovf_I`: Convert to a , signed, overflow check
- `Conv_Ovf_I_Un`: Convert to a , unsigned, overflow check
- `Conv_U`: Convert to a
- `Conv_Ovf_U`: Convert to a , signed, overflow check
- `Conv_Ovf_U_Un`: Convert to a , unsigned, overflow check

## Class `DebuggerRuntime`

Class implemented by the debugger. It provides access to the debugged process' locals, arguments, allows calling methods etc.

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.DebuggerRuntime and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.DebuggerRuntime(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 28)

### Methods

- `public abstract ILValue Box(ILValue value, DmdType type)`
  - Summary: Boxes a value or returns null on failure
  - Parameters:
    - `ILValue value`: Value to box
    - `DmdType type`: Target type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 129)
  - Example:
    ```csharp
    // Example invocation
    instance.Box(value: /* ILValue */, type: /* DmdType */);
    ```
- `public abstract ILValue CreateInstance(DmdConstructorInfo ctor, ILValue[] arguments)`
  - Summary: Creates a new instance and calls its constructor or returns null on failure. The constructor could be a CLR-generated array constructor
  - Parameters:
    - `DmdConstructorInfo ctor`: Constructor
    - `ILValue[] arguments`: Constructor arguments
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInstance(ctor: /* DmdConstructorInfo */, arguments: /* ILValue[] */);
    ```
- `public abstract ILValue CreateRuntimeFieldHandle(DmdFieldInfo field)`
  - Summary: Creates a value or returns null on failure
  - Parameters:
    - `DmdFieldInfo field`: Field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 107)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateRuntimeFieldHandle(field: /* DmdFieldInfo */);
    ```
- `public abstract ILValue CreateRuntimeMethodHandle(DmdMethodBase method)`
  - Summary: Creates a value or returns null on failure
  - Parameters:
    - `DmdMethodBase method`: Method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateRuntimeMethodHandle(method: /* DmdMethodBase */);
    ```
- `public abstract ILValue CreateRuntimeTypeHandle(DmdType type)`
  - Summary: Creates a value or returns null on failure
  - Parameters:
    - `DmdType type`: Type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateRuntimeTypeHandle(type: /* DmdType */);
    ```
- `public abstract ILValue CreateSZArray(DmdType elementType, long length)`
  - Summary: Creates an SZ array or returns null on failure
  - Parameters:
    - `DmdType elementType`: Element type
    - `long length`: Number of elements
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateSZArray(elementType: /* DmdType */, length: /* long */);
    ```
- `public abstract ILValue CreateTypeNoConstructor(DmdType type)`
  - Summary: Creates a type without calling its constructor or returns null on failure. All fields are initialized to 0 or null depending on field type
  - Parameters:
    - `DmdType type`: Type to create
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTypeNoConstructor(type: /* DmdType */);
    ```
- `public abstract ILValue LoadArgument(int index)`
  - Summary: Gets an argument value or returns null on failure
  - Parameters:
    - `int index`: Argument index
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadArgument(index: /* int */);
    ```
- `public abstract ILValue LoadArgumentAddress(int index, DmdType type)`
  - Summary: Gets the address of an argument or returns null on failure
  - Parameters:
    - `int index`: Argument index
    - `DmdType type`: Type of the argument
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadArgumentAddress(index: /* int */, type: /* DmdType */);
    ```
- `public abstract ILValue LoadLocal(int index)`
  - Summary: Gets a local value or returns null on failure
  - Parameters:
    - `int index`: Local index
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadLocal(index: /* int */);
    ```
- `public abstract ILValue LoadLocalAddress(int index, DmdType type)`
  - Summary: Gets the address of a local or returns null on failure
  - Parameters:
    - `int index`: Local index
    - `DmdType type`: Type of the local
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadLocalAddress(index: /* int */, type: /* DmdType */);
    ```
- `public abstract ILValue LoadStaticField(DmdFieldInfo field)`
  - Summary: Returns the value of a static field or returns null on failure
  - Parameters:
    - `DmdFieldInfo field`: Field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 163)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadStaticField(field: /* DmdFieldInfo */);
    ```
- `public abstract ILValue LoadStaticFieldAddress(DmdFieldInfo field)`
  - Summary: Returns the address of a static field or returns null on failure
  - Parameters:
    - `DmdFieldInfo field`: Field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 170)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadStaticFieldAddress(field: /* DmdFieldInfo */);
    ```
- `public abstract ILValue LoadString(DmdType type, string value)`
  - Summary: Returns a new string value
  - Parameters:
    - `DmdType type`: String type
    - `string value`: String value. This is never null.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 185)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadString(type: /* DmdType */, value: /* string */);
    ```
- `public abstract bool CallStatic(DmdMethodBase method, ILValue[] arguments, out ILValue returnValue)`
  - Summary: Calls a static method or returns false on failure
  - Parameters:
    - `DmdMethodBase method`: Method to call
    - `ILValue[] arguments`: Method arguments
    - `out ILValue returnValue`: Return value. It's ignored if the method returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 138)
  - Example:
    ```csharp
    // Example invocation
    instance.CallStatic(method: /* DmdMethodBase */, arguments: /* ILValue[] */, returnValue: /* ILValue */);
    ```
- `public abstract bool CallStaticIndirect(DmdMethodSignature methodSig, ILValue methodAddress, ILValue[] arguments, out ILValue returnValue)`
  - Summary: Calls a static method or returns false on failure
  - Parameters:
    - `DmdMethodSignature methodSig`: Method signature
    - `ILValue methodAddress`: Method address
    - `ILValue[] arguments`: Method arguments
    - `out ILValue returnValue`: Return value. It's ignored if the method returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 156)
  - Example:
    ```csharp
    // Example invocation
    instance.CallStaticIndirect(methodSig: /* DmdMethodSignature */, methodAddress: /* ILValue */, arguments: /* ILValue[] */, returnValue: /* ILValue */);
    ```
- `public abstract bool StoreArgument(int index, DmdType type, ILValue value)`
  - Summary: Writes to an argument or returns false on failure
  - Parameters:
    - `int index`: Argument index
    - `DmdType type`: Type of the argument
    - `ILValue value`: New value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreArgument(index: /* int */, type: /* DmdType */, value: /* ILValue */);
    ```
- `public abstract bool StoreLocal(int index, DmdType type, ILValue value)`
  - Summary: Writes to a local or returns false on failure
  - Parameters:
    - `int index`: Local index
    - `DmdType type`: Type of the local
    - `ILValue value`: New value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreLocal(index: /* int */, type: /* DmdType */, value: /* ILValue */);
    ```
- `public abstract bool StoreStaticField(DmdFieldInfo field, ILValue value)`
  - Summary: Stores a value in a static field or returns false on failure
  - Parameters:
    - `DmdFieldInfo field`: Field
    - `ILValue value`: Value to store in the field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 177)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreStaticField(field: /* DmdFieldInfo */, value: /* ILValue */);
    ```
- `public abstract bool? Equals(ILValue left, ILValue right)`
  - Summary: Checks if equals or returns null on failure
  - Parameters:
    - `ILValue left`: Left operand
    - `ILValue right`: Right operand
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 211)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(left: /* ILValue */, right: /* ILValue */);
    ```
- `public abstract int GetSizeOfValueType(DmdType type)`
  - Summary: Gets the size of a value type
  - Parameters:
    - `DmdType type`: Value type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 218)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSizeOfValueType(type: /* DmdType */);
    ```
- `public abstract int? CompareSigned(ILValue left, ILValue right)`
  - Summary: Compares and , returning less than 0, 0 or greater than 0. This method is called if one of the inputs is a non-constant native int or by-ref.
  - Parameters:
    - `ILValue left`: Left operand
    - `ILValue right`: Right operand
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 194)
  - Example:
    ```csharp
    // Example invocation
    instance.CompareSigned(left: /* ILValue */, right: /* ILValue */);
    ```
- `public abstract int? CompareUnsigned(ILValue left, ILValue right)`
  - Summary: Compares and , returning less than 0, 0 or greater than 0. This method is called if one of the inputs is a non-constant native int or by-ref.
  - Parameters:
    - `ILValue left`: Left operand
    - `ILValue right`: Right operand
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 203)
  - Example:
    ```csharp
    // Example invocation
    instance.CompareUnsigned(left: /* ILValue */, right: /* ILValue */);
    ```
- `public abstract void Initialize(DmdMethodBase method, DmdMethodBody body)`
  - Summary: Called before executing the method
  - Parameters:
    - `DmdMethodBase method`: Method
    - `DmdMethodBody body`: Method body
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Initialize(method: /* DmdMethodBase */, body: /* DmdMethodBody */);
    ```

### Properties

- `public abstract int PointerSize { get; }`
  - Summary: Gets the size of a pointer in bytes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PointerSize;
    ```

## Class `FunctionPointerILValue`

Function pointer, created by the ldftn/ldvirtftn instructions

**Inherits/Implements:** `NativeIntILValue`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.FunctionPointerILValue(method: /* DmdMethodBase */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 635)

### Constructors

- `public FunctionPointerILValue(DmdMethodBase method)`
  - Summary: Constructor (used by ldftn instruction)
  - Parameters:
    - `DmdMethodBase method`: Method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 655)
- `public FunctionPointerILValue(DmdMethodBase method, ILValue thisValue)`
  - Summary: Constructor (used by ldvirtftn instruction)
  - Parameters:
    - `DmdMethodBase method`: Method
    - `ILValue thisValue`: This object
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 665)

### Properties

- `public DmdMethodBase Method { get; }`
  - Summary: Gets the method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 649)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Method;
    ```
- `public ILValue VirtualThisObject { get; }`
  - Summary: Gets the this value if and only if this was created by a ldvirtftn instruction, otherwise it's null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 644)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VirtualThisObject;
    ```
- `public bool IsVirtual => VirtualThisObject != null`
  - Summary: true if it was created by a ldvirtftn instruction, false it was created by a ldftn instruction
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 639)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsVirtual;
    ```
- `public override DmdType Type { get; }`
  - Summary: Gets the type of the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 674)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```

## Class `ILVM`

Interprets IL code and returns the result

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.ILVM and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.ILVM(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILVM.cs` (line 26)

### Methods

- `public abstract ILVMExecuteState CreateExecuteState(DmdMethodBase method)`
  - Summary: Creates state that can be passed in to
  - Parameters:
    - `DmdMethodBase method`: Method to execute
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILVM.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateExecuteState(method: /* DmdMethodBase */);
    ```
- `public abstract ILValue Execute(DebuggerRuntime debuggerRuntime, ILVMExecuteState state)`
  - Summary: Interprets the IL instructions in the method body. All calls are handled by
  - Parameters:
    - `DebuggerRuntime debuggerRuntime`: Debugger class that can call methods in the debugged process
    - `ILVMExecuteState state`: State created by
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILVM.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(debuggerRuntime: /* DebuggerRuntime */, state: /* ILVMExecuteState */);
    ```

## Class `ILVMExecuteState`

State created by to speed up executing a method

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.ILVMExecuteState and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.ILVMExecuteState(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILVM.cs` (line 46)

## Class `ILVMFactory`

Creates instances

**Example**

```csharp
// Access dnSpy.Debugger.DotNet.Interpreter.ILVMFactory members directly without instantiation.
dnSpy.Debugger.DotNet.Interpreter.ILVMFactory./* member */
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILVMFactory.cs` (line 26)

### Methods

- `public static ILVM Create()`
  - Summary: Creates a new instance
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILVMFactory.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Interpreter.ILVMFactory.Create();
    ```

## Class `ILValue`

A value that can be stored on the IL stack

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.ILValue and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.ILValue(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 63)

### Methods

- `public virtual ILValue Add(AddOpCodeKind kind, long value, int pointerSize)`
  - Summary: Adds a constant to a copy of this value and returns the result. Returns null if it's not supported.
  - Parameters:
    - `AddOpCodeKind kind`: Opcode kind
    - `long value`: Value to add
    - `int pointerSize`: Size of a pointer in bytes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 248)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(kind: /* AddOpCodeKind */, value: /* long */, pointerSize: /* int */);
    ```
- `public virtual ILValue Box(DmdType type)`
  - Summary: Boxes this instance. Returns null if it's not supported.
  - Parameters:
    - `DmdType type`: Target type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    instance.Box(type: /* DmdType */);
    ```
- `public virtual ILValue Clone()`
  - Summary: Makes a copy of this instance so the new instance can be pushed onto the stack. The default implementation returns itself. Only mutable value types need to override this method.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```
- `public virtual ILValue Conv(ConvOpCodeKind kind)`
  - Summary: Converts this value to a new value. Returns null if it's not supported.
  - Parameters:
    - `ConvOpCodeKind kind`: Opcode kind
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 273)
  - Example:
    ```csharp
    // Example invocation
    instance.Conv(kind: /* ConvOpCodeKind */);
    ```
- `public virtual ILValue LoadField(DmdFieldInfo field)`
  - Summary: Loads an instance field. Returns null if it's not supported.
  - Parameters:
    - `DmdFieldInfo field`: Field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadField(field: /* DmdFieldInfo */);
    ```
- `public virtual ILValue LoadFieldAddress(DmdFieldInfo field)`
  - Summary: Returns the address of an instance field. Returns null if it's not supported.
  - Parameters:
    - `DmdFieldInfo field`: Field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadFieldAddress(field: /* DmdFieldInfo */);
    ```
- `public virtual ILValue LoadIndirect(DmdType type, LoadValueType loadValueType)`
  - Summary: Loads a value. Returns null if it's not supported.
  - Parameters:
    - `DmdType type`: Type
    - `LoadValueType loadValueType`: Type of value to load
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadIndirect(type: /* DmdType */, loadValueType: /* LoadValueType */);
    ```
- `public virtual ILValue LoadSZArrayElement(LoadValueType loadValueType, long index, DmdType elementType)`
  - Summary: Loads an SZ array element. Returns null if it's not supported.
  - Parameters:
    - `LoadValueType loadValueType`: Type of value to load
    - `long index`: Array index
    - `DmdType elementType`: Optional element type (eg. it's the ldelem instruction)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 163)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadSZArrayElement(loadValueType: /* LoadValueType */, index: /* long */, elementType: /* DmdType */);
    ```
- `public virtual ILValue LoadSZArrayElementAddress(long index, DmdType elementType)`
  - Summary: Loads the address of an SZ array element. Returns null if it's not supported.
  - Parameters:
    - `long index`: Index
    - `DmdType elementType`: Element type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadSZArrayElementAddress(index: /* long */, elementType: /* DmdType */);
    ```
- `public virtual ILValue Sub(SubOpCodeKind kind, ILValue value, int pointerSize)`
  - Summary: Subtracts from a copy of this value and returns the result. Returns null if it's not supported.
  - Parameters:
    - `SubOpCodeKind kind`: Opcode kind
    - `ILValue value`: Value to subtract
    - `int pointerSize`: Size of a pointer in bytes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 266)
  - Example:
    ```csharp
    // Example invocation
    instance.Sub(kind: /* SubOpCodeKind */, value: /* ILValue */, pointerSize: /* int */);
    ```
- `public virtual ILValue Sub(SubOpCodeKind kind, long value, int pointerSize)`
  - Summary: Subtracts a constant from a copy of this value and returns the result. Returns null if it's not supported.
  - Parameters:
    - `SubOpCodeKind kind`: Opcode kind
    - `long value`: Value to subtract
    - `int pointerSize`: Size of a pointer in bytes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 257)
  - Example:
    ```csharp
    // Example invocation
    instance.Sub(kind: /* SubOpCodeKind */, value: /* long */, pointerSize: /* int */);
    ```
- `public virtual ILValue Unbox(DmdType type)`
  - Summary: Unboxes this instance. Returns null if it's not supported.
  - Parameters:
    - `DmdType type`: Target type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 154)
  - Example:
    ```csharp
    // Example invocation
    instance.Unbox(type: /* DmdType */);
    ```
- `public virtual ILValue UnboxAny(DmdType type)`
  - Summary: Unboxes this instance. Returns null if it's not supported.
  - Parameters:
    - `DmdType type`: Target type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 147)
  - Example:
    ```csharp
    // Example invocation
    instance.UnboxAny(type: /* DmdType */);
    ```
- `public virtual bool Call(bool isCallvirt, DmdMethodBase method, ILValue[] arguments, out ILValue returnValue)`
  - Summary: Calls an instance method. The method could be a CLR-generated method, eg. an array Address() method, see . Returns false if it's not supported.
  - Parameters:
    - `bool isCallvirt`: true if this is a virtual call, false if it's a non-virtual call
    - `DmdMethodBase method`: Method
    - `ILValue[] arguments`: Arguments. The hidden 'this' value isn't included, it's this instance.
    - `out ILValue returnValue`: Updated with the return value. Can be null if the return type is
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.Call(isCallvirt: /* bool */, method: /* DmdMethodBase */, arguments: /* ILValue[] */, returnValue: /* ILValue */);
    ```
- `public virtual bool CallIndirect(DmdMethodSignature methodSig, ILValue methodAddress, ILValue[] arguments, out ILValue returnValue)`
  - Summary: Calls an instance method or returns false on failure
  - Parameters:
    - `DmdMethodSignature methodSig`: Method signature
    - `ILValue methodAddress`: Method address
    - `ILValue[] arguments`: Method arguments
    - `out ILValue returnValue`: Return value. It's ignored if the method returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    instance.CallIndirect(methodSig: /* DmdMethodSignature */, methodAddress: /* ILValue */, arguments: /* ILValue[] */, returnValue: /* ILValue */);
    ```
- `public virtual bool CopyMemory(ILValue source, long size)`
  - Summary: Copies memory to this value. Returns false if it's not supported.
  - Parameters:
    - `ILValue source`: Source value
    - `long size`: Size in bytes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 239)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyMemory(source: /* ILValue */, size: /* long */);
    ```
- `public virtual bool CopyObject(DmdType type, ILValue source)`
  - Summary: Copies to this value. Returns false if it's not supported.
  - Parameters:
    - `DmdType type`: Type
    - `ILValue source`: Source value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 223)
  - Example:
    ```csharp
    // Example invocation
    instance.CopyObject(type: /* DmdType */, source: /* ILValue */);
    ```
- `public virtual bool GetSZArrayLength(out long length)`
  - Summary: Gets the length of an SZ array. Returns false if it's not supported.
  - Parameters:
    - `out long length`: Updated with the length of the array
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSZArrayLength(length: /* long */);
    ```
- `public virtual bool InitializeMemory(byte value, long size)`
  - Summary: Initializes memory. Returns false if it's not supported.
  - Parameters:
    - `byte value`: Value to write
    - `long size`: Size of data
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 231)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializeMemory(value: /* byte */, size: /* long */);
    ```
- `public virtual bool InitializeObject(DmdType type)`
  - Summary: Clears the memory. Returns false if it's not supported.
  - Parameters:
    - `DmdType type`: Type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 215)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializeObject(type: /* DmdType */);
    ```
- `public virtual bool StoreField(DmdFieldInfo field, ILValue value)`
  - Summary: Stores a value in an instance field. Returns false if it's not supported.
  - Parameters:
    - `DmdFieldInfo field`: Field
    - `ILValue value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreField(field: /* DmdFieldInfo */, value: /* ILValue */);
    ```
- `public virtual bool StoreIndirect(DmdType type, LoadValueType loadValueType, ILValue value)`
  - Summary: Stores a value. Returns false if it's not supported.
  - Parameters:
    - `DmdType type`: Type
    - `LoadValueType loadValueType`: Type of value to store
    - `ILValue value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 208)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreIndirect(type: /* DmdType */, loadValueType: /* LoadValueType */, value: /* ILValue */);
    ```
- `public virtual bool StoreSZArrayElement(LoadValueType loadValueType, long index, ILValue value, DmdType elementType)`
  - Summary: Writes an SZ array element. Returns false if it's not supported.
  - Parameters:
    - `LoadValueType loadValueType`: Type of value to store
    - `long index`: Index
    - `ILValue value`: Value
    - `DmdType elementType`: Optional element type (eg. it's the stelem instruction)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 173)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreSZArrayElement(loadValueType: /* LoadValueType */, index: /* long */, value: /* ILValue */, elementType: /* DmdType */);
    ```

### Properties

- `public abstract DmdType Type { get; }`
  - Summary: Gets the type of the value or null if it's unknown, eg. it's a null reference
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public abstract ILValueKind Kind { get; }`
  - Summary: Gets the stack value kind
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public virtual bool IsNull => false`
  - Summary: true if this is a null value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNull;
    ```

## Enum `ILValueKind`

IL stack value kind

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.ILValueKind and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.ILValueKind(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 28)

### Members

- `Int32`: 32-bit integer. 1-byte and 2-byte integers are sign/zero extended to 32 bits. Booleans and chars are zero extended.
- `Int64`: 64-bit integer
- `Float`: 64-bit float (32-bit floats are extended to 64-bit floats)
- `NativeInt`: Unmanaged pointer or native int
- `ByRef`: Managed pointer
- `Type`: Any other reference type or value type

## Class `InstructionNotSupportedInterpreterException`

Unsupported IL instruction

**Inherits/Implements:** `InterpreterException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.InstructionNotSupportedInterpreterException(message: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 98)

### Constructors

- `public InstructionNotSupportedInterpreterException(string message)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 109)

### Properties

- `public override InterpreterExceptionKind Kind => InterpreterExceptionKind.InstructionNotSupported`
  - Summary: Returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 103)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `InterpreterException`

Interpreter exception

**Inherits/Implements:** `Exception`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.InterpreterException(message: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 34)

### Constructors

- `protected InterpreterException(string message)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 45)
- `protected InterpreterException(string message, Exception innerException)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
    - `Exception innerException`: Inner exception
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 52)

### Properties

- `public abstract InterpreterExceptionKind Kind { get; }`
  - Summary: Gets the exception kind
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Enum `InterpreterExceptionKind`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.InterpreterExceptionKind and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.InterpreterExceptionKind(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 24)

### Members

- `TooManyInstructions`
- `InvalidMethodBody`
- `InstructionNotSupported`

## Class `InterpreterMessageException`

Thrown when IL code is being interpreted and an error is detected.

**Inherits/Implements:** `Exception`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.InterpreterMessageException(message: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterMessageException.cs` (line 27)

### Constructors

- `protected InterpreterMessageException(SerializationInfo info, StreamingContext context)`
  - Summary: Constructor
  - Parameters:
    - `SerializationInfo info`: Description not provided.
    - `StreamingContext context`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterMessageException.cs` (line 47)
- `public InterpreterMessageException(string message)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Error message
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterMessageException.cs` (line 33)
- `public InterpreterMessageException(string message, Exception innerException)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Error message
    - `Exception innerException`: Other exception
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterMessageException.cs` (line 40)

## Class `InterpreterThrownExceptionException`

Contains a thrown exception value

**Inherits/Implements:** `Exception`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.InterpreterThrownExceptionException(thrownValue: /* object */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterThrownExceptionException.cs` (line 26)

### Constructors

- `public InterpreterThrownExceptionException(object thrownValue)`
  - Summary: Constructor
  - Parameters:
    - `object thrownValue`: Thrown value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterThrownExceptionException.cs` (line 36)

### Properties

- `public object ThrownValue { get; }`
  - Summary: Gets the thrown value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterThrownExceptionException.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ThrownValue;
    ```

## Class `InvalidMethodBodyInterpreterException`

Invalid method body, eg. last instruction isn't an unconditional branch instruction (eg. ret/throw)

**Inherits/Implements:** `InterpreterException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.InvalidMethodBodyInterpreterException();
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 74)

### Constructors

- `public InvalidMethodBodyInterpreterException()`
  - Summary: Constructor
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 86)
- `public InvalidMethodBodyInterpreterException(Exception innerException)`
  - Summary: Constructor
  - Parameters:
    - `Exception innerException`: Inner exception
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 92)

### Properties

- `public override InterpreterExceptionKind Kind => InterpreterExceptionKind.InvalidMethodBody`
  - Summary: Returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 79)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Enum `LoadValueType`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.LoadValueType and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.LoadValueType(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/DebuggerRuntime.cs` (line 222)

### Members

- `I`
- `I1`
- `I2`
- `I4`
- `I8`
- `R4`
- `R8`
- `Ref`
- `U1`
- `U2`
- `U4`

## Class `NativeIntILValue`

native integer or unmanaged pointer

**Inherits/Implements:** `ILValue`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.NativeIntILValue and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.NativeIntILValue(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 511)

### Properties

- `public sealed override ILValueKind Kind => ILValueKind.NativeInt`
  - Summary: Always returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 515)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `NativeMemoryILValue`

Pointer to a block of memory. Used by eg. localloc

**Inherits/Implements:** `NativeIntILValue`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.NativeMemoryILValue(appDomain: /* DmdAppDomain */, size: /* int */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 680)

### Constructors

- `public NativeMemoryILValue(DmdAppDomain appDomain, int size)`
  - Summary: Constructor
  - Parameters:
    - `DmdAppDomain appDomain`: AppDomain
    - `int size`: Size of memory
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 694)

### Methods

- `public override ILValue Add(AddOpCodeKind kind, long value, int pointerSize)`
  - Summary: Adds a constant to a copy of this value and returns the result. Returns null if it's not supported.
  - Parameters:
    - `AddOpCodeKind kind`: Opcode kind
    - `long value`: Value to add
    - `int pointerSize`: Size of a pointer in bytes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 713)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(kind: /* AddOpCodeKind */, value: /* long */, pointerSize: /* int */);
    ```
- `public override ILValue LoadIndirect(DmdType type, LoadValueType loadValueType)`
  - Summary: Loads a value. Returns null if it's not supported.
  - Parameters:
    - `DmdType type`: Type
    - `LoadValueType loadValueType`: Type of value to load
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 790)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadIndirect(type: /* DmdType */, loadValueType: /* LoadValueType */);
    ```
- `public override ILValue Sub(SubOpCodeKind kind, long value, int pointerSize)`
  - Summary: Subtracts a constant from a copy of this value and returns the result. Returns null if it's not supported.
  - Parameters:
    - `SubOpCodeKind kind`: Opcode kind
    - `long value`: Value to subtract
    - `int pointerSize`: Size of a pointer in bytes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 752)
  - Example:
    ```csharp
    // Example invocation
    instance.Sub(kind: /* SubOpCodeKind */, value: /* long */, pointerSize: /* int */);
    ```
- `public override bool InitializeMemory(byte value, long size)`
  - Summary: Initializes memory or returns false if it's not supported
  - Parameters:
    - `byte value`: Value to write
    - `long size`: Size of data
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 1022)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializeMemory(value: /* byte */, size: /* long */);
    ```
- `public override bool StoreIndirect(DmdType type, LoadValueType loadValueType, ILValue value)`
  - Summary: Stores a value. Returns false if it's not supported.
  - Parameters:
    - `DmdType type`: Type
    - `LoadValueType loadValueType`: Type of value to store
    - `ILValue value`: Value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 866)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreIndirect(type: /* DmdType */, loadValueType: /* LoadValueType */, value: /* ILValue */);
    ```

### Properties

- `public override DmdType Type { get; }`
  - Summary: Gets the type of the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 1036)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```

## Class `NullObjectRefILValue`

A null reference

**Inherits/Implements:** `TypeILValue`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.NullObjectRefILValue();
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 1062)

### Constructors

- `public NullObjectRefILValue()`
  - Summary: Constructor
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 1071)

### Properties

- `public override DmdType Type => null`
  - Summary: Gets the type of the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 1076)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public sealed override bool IsNull => true`
  - Summary: Returns true since it's a null value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 1066)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNull;
    ```

## Enum `SubOpCodeKind`

Sub opcode kind

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.SubOpCodeKind and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.SubOpCodeKind(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 299)

### Members

- `Sub`: Normal subtraction
- `Sub_Ovf`: Signed subtraction with an overflow check
- `Sub_Ovf_Un`: Unsigned subtraction with an overflow check

## Class `TooManyInstructionsInterpreterException`

Thrown when too many instructions have been interpreted

**Inherits/Implements:** `InterpreterException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Interpreter.TooManyInstructionsInterpreterException();
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 58)

### Constructors

- `public TooManyInstructionsInterpreterException()`
  - Summary: Constructor
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 68)

### Properties

- `public override InterpreterExceptionKind Kind => InterpreterExceptionKind.TooManyInstructions`
  - Summary: Returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/InterpreterException.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `TypeILValue`

A reference type or a value type

**Inherits/Implements:** `ILValue`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Interpreter.TypeILValue and call its members.
var instance = new dnSpy.Debugger.DotNet.Interpreter.TypeILValue(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 1052)

### Properties

- `public sealed override ILValueKind Kind => ILValueKind.Type`
  - Summary: Always returns
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Interpreter/ILValue.cs` (line 1056)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

