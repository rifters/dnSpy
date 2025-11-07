# Namespace `dnSpy.Contracts.Debugger.Engine.Evaluation`

## Struct `DbgEngineEEAssignmentResult`

Expression evaluator assignment result

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineEEAssignmentResult(flags: /* DbgEEAssignmentResultFlags */, error: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 111)

### Constructors

- `public DbgEngineEEAssignmentResult(DbgEEAssignmentResultFlags flags, string error)`
  - Summary: Constructor
  - Parameters:
    - `DbgEEAssignmentResultFlags flags`: Result flags
    - `string error`: Error message or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 132)

### Properties

- `public DbgEEAssignmentResultFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 120)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public bool IsCompilerError => (Flags & DbgEEAssignmentResultFlags.CompilerError) != 0`
  - Summary: true if the error is from the compiler and no debuggee code was executed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 125)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsCompilerError;
    ```
- `public string Error { get; }`
  - Summary: Error message or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 115)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Struct `DbgEngineEvaluationResult`

Evaluation result

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineEvaluationResult(value: /* DbgEngineValue */, formatSpecifiers: /* ReadOnlyCollection<string> */, flags: /* DbgEvaluationResultFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 59)

### Constructors

- `public DbgEngineEvaluationResult(DbgEngineValue value, ReadOnlyCollection<string> formatSpecifiers, DbgEvaluationResultFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `DbgEngineValue value`: Value
    - `ReadOnlyCollection<string> formatSpecifiers`: Format specifiers or null
    - `DbgEvaluationResultFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 88)
- `public DbgEngineEvaluationResult(string error, DbgEvaluationResultFlags flags = 0)`
  - Summary: Constructor
  - Parameters:
    - `string error`: Error message
    - `DbgEvaluationResultFlags flags` (default: `0`): Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 100)

### Properties

- `public DbgEngineValue Value { get; }`
  - Summary: Gets the value or null if there was an error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public DbgEvaluationResultFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public ReadOnlyCollection<string> FormatSpecifiers { get; }`
  - Summary: Gets the format specifiers, if any
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FormatSpecifiers;
    ```
- `public string Error { get; }`
  - Summary: Gets the error or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Class `DbgEngineExpressionEvaluator`

Expression evaluator

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineExpressionEvaluator and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineExpressionEvaluator(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 28)

### Methods

- `public abstract DbgEngineEEAssignmentResult Assign(DbgEvaluationInfo evalInfo, string expression, string valueExpression, DbgEvaluationOptions options)`
  - Summary: Assigns the value of an expression to another expression
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `string expression`: Target expression (lhs)
    - `string valueExpression`: Source expression (rhs)
    - `DbgEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.Assign(evalInfo: /* DbgEvaluationInfo */, expression: /* string */, valueExpression: /* string */, options: /* DbgEvaluationOptions */);
    ```
- `public abstract DbgEngineEvaluationResult Evaluate(DbgEvaluationInfo evalInfo, string expression, DbgEvaluationOptions options, object state)`
  - Summary: Evaluates an expression
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `string expression`: Expression to evaluate
    - `DbgEvaluationOptions options`: Options
    - `object state`: State created by or null to store the state in 's context
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.Evaluate(evalInfo: /* DbgEvaluationInfo */, expression: /* string */, options: /* DbgEvaluationOptions */, state: /* object */);
    ```
- `public abstract object CreateExpressionEvaluatorState()`
  - Summary: Creates evaluator state used to cache data that is needed to evaluate an expression
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineExpressionEvaluator.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateExpressionEvaluatorState();
    ```

## Class `DbgEngineFormatter`

Formats names, types, values, stack frames

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineFormatter and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineFormatter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineFormatter.cs` (line 28)

### Methods

- `public abstract void FormatExceptionName(DbgEvaluationContext context, IDbgTextWriter output, uint id)`
  - Summary: Formats an exception name
  - Parameters:
    - `DbgEvaluationContext context`: Evaluation context
    - `IDbgTextWriter output`: Output
    - `uint id`: Exception id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineFormatter.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatExceptionName(context: /* DbgEvaluationContext */, output: /* IDbgTextWriter */, id: /* uint */);
    ```
- `public abstract void FormatFrame(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgStackFrameFormatterOptions options, DbgValueFormatterOptions valueOptions, CultureInfo cultureInfo)`
  - Summary: Formats a stack frame
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgStackFrameFormatterOptions options`: Stack frame options
    - `DbgValueFormatterOptions valueOptions`: Value option
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineFormatter.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatFrame(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, options: /* DbgStackFrameFormatterOptions */, valueOptions: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```
- `public abstract void FormatObjectIdName(DbgEvaluationContext context, IDbgTextWriter output, uint id)`
  - Summary: Formats an object ID name
  - Parameters:
    - `DbgEvaluationContext context`: Evaluation context
    - `IDbgTextWriter output`: Output
    - `uint id`: Object id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineFormatter.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatObjectIdName(context: /* DbgEvaluationContext */, output: /* IDbgTextWriter */, id: /* uint */);
    ```
- `public abstract void FormatReturnValueName(DbgEvaluationContext context, IDbgTextWriter output, uint id)`
  - Summary: Formats a return value name
  - Parameters:
    - `DbgEvaluationContext context`: Evaluation context
    - `IDbgTextWriter output`: Output
    - `uint id`: Return value id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineFormatter.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatReturnValueName(context: /* DbgEvaluationContext */, output: /* IDbgTextWriter */, id: /* uint */);
    ```
- `public abstract void FormatStowedExceptionName(DbgEvaluationContext context, IDbgTextWriter output, uint id)`
  - Summary: Formats a stowed exception name
  - Parameters:
    - `DbgEvaluationContext context`: Evaluation context
    - `IDbgTextWriter output`: Output
    - `uint id`: Stowed exception id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineFormatter.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatStowedExceptionName(context: /* DbgEvaluationContext */, output: /* IDbgTextWriter */, id: /* uint */);
    ```
- `public abstract void FormatType(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgEngineValue value, DbgValueFormatterTypeOptions options, CultureInfo cultureInfo)`
  - Summary: Formats a value's type
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgEngineValue value`: Value to format
    - `DbgValueFormatterTypeOptions options`: Options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineFormatter.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatType(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, value: /* DbgEngineValue */, options: /* DbgValueFormatterTypeOptions */, cultureInfo: /* CultureInfo */);
    ```
- `public abstract void FormatValue(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgEngineValue value, DbgValueFormatterOptions options, CultureInfo cultureInfo)`
  - Summary: Formats a value
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgEngineValue value`: Value to format
    - `DbgValueFormatterOptions options`: Options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineFormatter.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatValue(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, value: /* DbgEngineValue */, options: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```

## Class `DbgEngineLanguage`

Debugger language that evaluates expressions and formats values

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineLanguage and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineLanguage(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 28)

### Methods

- `public abstract void InitializeContext(DbgEvaluationContext context, DbgCodeLocation location, CancellationToken cancellationToken)`
  - Summary: Initializes an evaluation context
  - Parameters:
    - `DbgEvaluationContext context`: Context
    - `DbgCodeLocation location`: Location or null
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializeContext(context: /* DbgEvaluationContext */, location: /* DbgCodeLocation */, cancellationToken: /* CancellationToken */);
    ```

### Properties

- `public abstract DbgEngineExpressionEvaluator ExpressionEvaluator { get; }`
  - Summary: Gets the expression evaluator
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExpressionEvaluator;
    ```
- `public abstract DbgEngineFormatter Formatter { get; }`
  - Summary: Gets the formatter
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Formatter;
    ```
- `public abstract DbgEngineLocalsValueNodeProvider LocalsProvider { get; }`
  - Summary: Gets the locals and parameters provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LocalsProvider;
    ```
- `public abstract DbgEngineValueNodeFactory ValueNodeFactory { get; }`
  - Summary: Gets the factory
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueNodeFactory;
    ```
- `public abstract DbgEngineValueNodeProvider AutosProvider { get; }`
  - Summary: Gets the autos provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AutosProvider;
    ```
- `public abstract DbgEngineValueNodeProvider ExceptionsProvider { get; }`
  - Summary: Gets the exceptions provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExceptionsProvider;
    ```
- `public abstract DbgEngineValueNodeProvider ReturnValuesProvider { get; }`
  - Summary: Gets the return values provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReturnValuesProvider;
    ```
- `public abstract DbgEngineValueNodeProvider TypeVariablesProvider { get; }`
  - Summary: Gets the type variables provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeVariablesProvider;
    ```
- `public abstract string DisplayName { get; }`
  - Summary: Gets the language's display name (shown in the UI)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DisplayName;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the language name, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguage.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `DbgEngineLanguageProvider`

Creates s. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineLanguageProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineLanguageProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguageProvider.cs` (line 29)

### Methods

- `public abstract IEnumerable<DbgEngineLanguage> Create()`
  - Summary: Creates all languages
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguageProvider.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

### Properties

- `public abstract string RuntimeDisplayName { get; }`
  - Summary: Gets the runtime display name, eg. ".NET"
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguageProvider.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeDisplayName;
    ```

## Struct `DbgEngineLocalsValueNodeInfo`

Contains a value node and its kind

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineLocalsValueNodeInfo(kind: /* DbgLocalsValueNodeKind */, valueNode: /* DbgEngineValueNode */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeProvider.cs` (line 54)

### Constructors

- `public DbgEngineLocalsValueNodeInfo(DbgLocalsValueNodeKind kind, DbgEngineValueNode valueNode)`
  - Summary: Constructor
  - Parameters:
    - `DbgLocalsValueNodeKind kind`: What kind of value this is (local or parameter)
    - `DbgEngineValueNode valueNode`: Value node
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeProvider.cs` (line 70)

### Properties

- `public DbgEngineValueNode ValueNode { get; }`
  - Summary: Gets the node
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeProvider.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueNode;
    ```
- `public DbgLocalsValueNodeKind Kind { get; }`
  - Summary: What kind of value this is (local or parameter)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeProvider.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Class `DbgEngineLocalsValueNodeProvider`

Provides s for the locals windows

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineLocalsValueNodeProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineLocalsValueNodeProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeProvider.cs` (line 40)

### Methods

- `public abstract DbgEngineLocalsValueNodeInfo[] GetNodes(DbgEvaluationInfo evalInfo, DbgValueNodeEvaluationOptions options, DbgLocalsValueNodeEvaluationOptions localsOptions)`
  - Summary: Gets all values
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgValueNodeEvaluationOptions options`: Options
    - `DbgLocalsValueNodeEvaluationOptions localsOptions`: Locals value node provider options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeProvider.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNodes(evalInfo: /* DbgEvaluationInfo */, options: /* DbgValueNodeEvaluationOptions */, localsOptions: /* DbgLocalsValueNodeEvaluationOptions */);
    ```

## Class `DbgEngineObjectId`

References a value in the debugged process

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineObjectId and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineObjectId(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectId.cs` (line 26)

### Methods

- `public abstract DbgEngineValue GetValue(DbgEvaluationInfo evalInfo)`
  - Summary: Creates a new value
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectId.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValue(evalInfo: /* DbgEvaluationInfo */);
    ```

### Properties

- `public abstract uint Id { get; }`
  - Summary: Gets the unique id in the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectId.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Class `DbgEngineObjectIdFactory`

Creates s. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineObjectIdFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineObjectIdFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 28)

### Methods

- `public abstract DbgEngineObjectId CreateObjectId(DbgEngineValue value, uint id)`
  - Summary: Creates an object id or returns null
  - Parameters:
    - `DbgEngineValue value`: Value created by this runtime
    - `uint id`: Unique id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateObjectId(value: /* DbgEngineValue */, id: /* uint */);
    ```
- `public abstract bool CanCreateObjectId(DbgEngineValue value)`
  - Summary: Returns true if it's possible to create an object id
  - Parameters:
    - `DbgEngineValue value`: Value created by this runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.CanCreateObjectId(value: /* DbgEngineValue */);
    ```
- `public abstract bool Equals(DbgEngineObjectId objectId, DbgEngineValue value)`
  - Summary: Checks if an object id and a value refer to the same data
  - Parameters:
    - `DbgEngineObjectId objectId`: Object id created by this class
    - `DbgEngineValue value`: Value created by this runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(objectId: /* DbgEngineObjectId */, value: /* DbgEngineValue */);
    ```
- `public abstract int GetHashCode(DbgEngineObjectId objectId)`
  - Summary: Gets the hash code of an object id
  - Parameters:
    - `DbgEngineObjectId objectId`: Object id created by this class
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(objectId: /* DbgEngineObjectId */);
    ```
- `public abstract int GetHashCode(DbgEngineValue value)`
  - Summary: Gets the hash code of a value created by this runtime
  - Parameters:
    - `DbgEngineValue value`: Value created by this runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(value: /* DbgEngineValue */);
    ```

## Class `DbgEngineValue`

Result of evaluating an expression

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineValue and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineValue(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValue.cs` (line 26)

### Methods

- `public abstract DbgRawAddressValue? GetRawAddressValue(bool onlyDataAddress)`
  - Summary: Gets the address of the value or null if there's no address available. The returned address gets invalid when the runtime continues.
  - Parameters:
    - `bool onlyDataAddress`: If true and if it's a supported type (eg. a simple type such as integers, floating point values, strings or byte arrays) the returned object contains the address of the actual value, else the returned address and length covers the whole object including vtable, method table or other special data.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValue.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRawAddressValue(onlyDataAddress: /* bool */);
    ```

### Properties

- `public abstract DbgSimpleValueType ValueType { get; }`
  - Summary: Type of the value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValue.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueType;
    ```
- `public abstract bool HasRawValue { get; }`
  - Summary: true if is valid
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValue.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasRawValue;
    ```
- `public abstract object InternalValue { get; }`
  - Summary: Gets the value object created by the debug engine
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValue.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InternalValue;
    ```
- `public abstract object RawValue { get; }`
  - Summary: The value. It's only valid if is true. A null value is a valid value. If it's an enum value, it's stored as the enum's underlying type (eg. )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValue.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RawValue;
    ```

## Class `DbgEngineValueNode`

A value shown in a treeview (eg. in locals window)

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineValueNode and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineValueNode(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 27)

### Methods

- `public abstract DbgEngineValueNodeAssignmentResult Assign(DbgEvaluationInfo evalInfo, string expression, DbgEvaluationOptions options)`
  - Summary: Writes a new value
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `string expression`: Source expression (rhs)
    - `DbgEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    instance.Assign(evalInfo: /* DbgEvaluationInfo */, expression: /* string */, options: /* DbgEvaluationOptions */);
    ```
- `public abstract DbgEngineValueNode[] GetChildren(DbgEvaluationInfo evalInfo, ulong index, int count, DbgValueNodeEvaluationOptions options)`
  - Summary: Creates new children
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `ulong index`: Index of first child
    - `int count`: Max number of children to return
    - `DbgValueNodeEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.GetChildren(evalInfo: /* DbgEvaluationInfo */, index: /* ulong */, count: /* int */, options: /* DbgValueNodeEvaluationOptions */);
    ```
- `public abstract ulong GetChildCount(DbgEvaluationInfo evalInfo)`
  - Summary: Number of children. This property is called as late as possible and can be lazily initialized. It's assumed to be 0 if is false.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.GetChildCount(evalInfo: /* DbgEvaluationInfo */);
    ```
- `public abstract void Format(DbgEvaluationInfo evalInfo, IDbgValueNodeFormatParameters options, CultureInfo cultureInfo)`
  - Summary: Formats the name, value, and type
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgValueNodeFormatParameters options`: Options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.Format(evalInfo: /* DbgEvaluationInfo */, options: /* IDbgValueNodeFormatParameters */, cultureInfo: /* CultureInfo */);
    ```

### Properties

- `public abstract DbgEngineValue Value { get; }`
  - Summary: Gets the value or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public abstract bool CausesSideEffects { get; }`
  - Summary: true if the expression causes side effects
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CausesSideEffects;
    ```
- `public abstract bool IsReadOnly { get; }`
  - Summary: true if this is a read-only value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsReadOnly;
    ```
- `public abstract bool? HasChildren { get; }`
  - Summary: Returns true if it has children, false if it has no children and null if it's unknown (eg. it's too expensive to calculate it now). UI code can use this property to decide if it shows the treeview node expander ("|>").
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasChildren;
    ```
- `public abstract string ErrorMessage { get; }`
  - Summary: Gets the error message or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ErrorMessage;
    ```
- `public abstract string Expression { get; }`
  - Summary: Gets the expression that is used when adding an expression to the watch window or when assigning a new value to the source.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Expression;
    ```
- `public abstract string ImageName { get; }`
  - Summary: Image name, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageName;
    ```

## Struct `DbgEngineValueNodeAssignmentResult`

Assignment result

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineValueNodeAssignmentResult(flags: /* DbgEEAssignmentResultFlags */, error: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 104)

### Constructors

- `public DbgEngineValueNodeAssignmentResult(DbgEEAssignmentResultFlags flags, string error)`
  - Summary: Constructor
  - Parameters:
    - `DbgEEAssignmentResultFlags flags`: Result flags
    - `string error`: Error message or one of the errors in
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 120)

### Properties

- `public DbgEEAssignmentResultFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 113)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public string Error { get; }`
  - Summary: Gets the error message (also see ) or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNode.cs` (line 108)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Class `DbgEngineValueNodeFactory`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineValueNodeFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineValueNodeFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeFactory.cs` (line 26)

### Methods

- `public abstract DbgEngineValueNode[] Create(DbgEvaluationInfo evalInfo, DbgEngineObjectId[] objectIds, DbgValueNodeEvaluationOptions options)`
  - Summary: Creates s
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgEngineObjectId[] objectIds`: Object ids
    - `DbgValueNodeEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeFactory.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(evalInfo: /* DbgEvaluationInfo */, objectIds: /* DbgEngineObjectId[] */, options: /* DbgValueNodeEvaluationOptions */);
    ```
- `public abstract DbgEngineValueNode[] Create(DbgEvaluationInfo evalInfo, DbgExpressionEvaluationInfo[] expressions)`
  - Summary: Creates s
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgExpressionEvaluationInfo[] expressions`: Expressions to evaluate
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeFactory.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(evalInfo: /* DbgEvaluationInfo */, expressions: /* DbgExpressionEvaluationInfo[] */);
    ```

## Class `DbgEngineValueNodeProvider`

Provides s for the variables windows

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineValueNodeProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.DbgEngineValueNodeProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeProvider.cs` (line 27)

### Methods

- `public abstract DbgEngineValueNode[] GetNodes(DbgEvaluationInfo evalInfo, DbgValueNodeEvaluationOptions options)`
  - Summary: Gets all values
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgValueNodeEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineValueNodeProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNodes(evalInfo: /* DbgEvaluationInfo */, options: /* DbgValueNodeEvaluationOptions */);
    ```

## Class `ExportDbgEngineLanguageProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgEngineLanguageProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.ExportDbgEngineLanguageProviderAttribute(runtimeKindGuid: /* string */, order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguageProvider.cs` (line 53)

### Constructors

- `public ExportDbgEngineLanguageProviderAttribute(string runtimeKindGuid, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string runtimeKindGuid`: Runtime kind GUID, see
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguageProvider.cs` (line 60)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguageProvider.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string RuntimeKindGuid { get; }`
  - Summary: Runtime kind GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguageProvider.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeKindGuid;
    ```

## Class `ExportDbgEngineObjectIdFactoryAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgEngineObjectIdFactoryMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.ExportDbgEngineObjectIdFactoryAttribute(runtimeGuid: /* string */, order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 78)

### Constructors

- `public ExportDbgEngineObjectIdFactoryAttribute(string runtimeGuid, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string runtimeGuid`: Runtime GUID, see
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 85)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 99)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string RuntimeGuid { get; }`
  - Summary: Runtime GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeGuid;
    ```

## Interface `IDbgEngineLanguageProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.IDbgEngineLanguageProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.IDbgEngineLanguageProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguageProvider.cs` (line 43)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguageProvider.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string RuntimeKindGuid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineLanguageProvider.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeKindGuid;
    ```

## Interface `IDbgEngineObjectIdFactoryMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Engine.Evaluation.IDbgEngineObjectIdFactoryMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Engine.Evaluation.IDbgEngineObjectIdFactoryMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 68)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string RuntimeGuid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/DbgEngineObjectIdFactory.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeGuid;
    ```

## Class `PredefinedEvaluationErrorMessages`

Common error messages

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages members directly without instantiation.
dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 26)

### Fields

- `public const string CanFuncEvalOnlyWhenPaused = nameof(CanFuncEvalOnlyWhenPaused) + SUFFIX`
  - Summary: The debugged program isn't paused so it's not possible to func-eval
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.CanFuncEvalOnlyWhenPaused;
    ```
- `public const string CannotReadLocalOrArgumentMaybeOptimizedAway = nameof(CannotReadLocalOrArgumentMaybeOptimizedAway) + SUFFIX`
  - Summary: Can't read local or argument because it's not available at the current IP or it's been optimized away
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 83)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.CannotReadLocalOrArgumentMaybeOptimizedAway;
    ```
- `public const string CantFuncEval = nameof(CantFuncEval) + SUFFIX`
  - Summary: It's not possible to func-eval, eg. because we're already func-eval'ing
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.CantFuncEval;
    ```
- `public const string CantFuncEvalWhenUnhandledExceptionHasOccurred = nameof(CantFuncEvalWhenUnhandledExceptionHasOccurred) + SUFFIX`
  - Summary: It's not possible to func-eval when an unhandled exception has occurred
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.CantFuncEvalWhenUnhandledExceptionHasOccurred;
    ```
- `public const string CantFuncEvaluateWhenThreadIsAtUnsafePoint = nameof(CantFuncEvaluateWhenThreadIsAtUnsafePoint) + SUFFIX`
  - Summary: It's not possible to func-eval because the thread isn't at a safe point where a GC can occur
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.CantFuncEvaluateWhenThreadIsAtUnsafePoint;
    ```
- `public const string ExpressionCausesSideEffects = nameof(ExpressionCausesSideEffects) + SUFFIX`
  - Summary: is set but expression causes side effects
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.ExpressionCausesSideEffects;
    ```
- `public const string FuncEvalDisabled = nameof(FuncEvalDisabled) + SUFFIX`
  - Summary: or is set but code must call a method
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.FuncEvalDisabled;
    ```
- `public const string FuncEvalRequiresAllThreadsToRun = nameof(FuncEvalRequiresAllThreadsToRun) + SUFFIX`
  - Summary: Can't func eval since all threads must execute (the code called )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 78)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.FuncEvalRequiresAllThreadsToRun;
    ```
- `public const string FuncEvalTimedOut = nameof(FuncEvalTimedOut) + SUFFIX`
  - Summary: Function evaluation timed out
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.FuncEvalTimedOut;
    ```
- `public const string FuncEvalTimedOutNowDisabled = nameof(FuncEvalTimedOutNowDisabled) + SUFFIX`
  - Summary: Function evaluation timed out previously and is disabled until the user continues the debugged program
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.FuncEvalTimedOutNowDisabled;
    ```
- `public const string InternalDebuggerError = nameof(InternalDebuggerError) + SUFFIX`
  - Summary: Some error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.InternalDebuggerError;
    ```
- `public const string RuntimeIsUnableToEvaluateExpression = nameof(RuntimeIsUnableToEvaluateExpression) + SUFFIX`
  - Summary: Runtime can't read a field, local
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Engine/Evaluation/PredefinedEvaluationErrorMessages.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Engine.Evaluation.PredefinedEvaluationErrorMessages.RuntimeIsUnableToEvaluateExpression;
    ```

