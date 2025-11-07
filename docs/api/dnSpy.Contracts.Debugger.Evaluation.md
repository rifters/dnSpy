# Namespace `dnSpy.Contracts.Debugger.Evaluation`

## Enum `CreateObjectIdOptions`

Object ID options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.CreateObjectIdOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.CreateObjectIdOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 112)

### Members

- `None`: No bit is set
- `Hidden` = `x00000001`: Hidden object Id. It's not shown in any of the variables windows.

## Struct `DbgCreateValueNodeResult`

Contains the created or an error message

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgCreateValueNodeResult(node: /* DbgValueNode */, causesSideEffects: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeFactory.cs` (line 65)

### Constructors

- `public DbgCreateValueNodeResult(DbgValueNode node, bool causesSideEffects)`
  - Summary: Constructor
  - Parameters:
    - `DbgValueNode node`: New value node
    - `bool causesSideEffects`: true if the expression wasn't evaluated because it causes side effects ( was used)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeFactory.cs` (line 81)

### Properties

- `public DbgValueNode ValueNode { get; }`
  - Summary: Gets the created node or null if there was an error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeFactory.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueNode;
    ```
- `public bool CausesSideEffects { get; }`
  - Summary: true if the expression wasn't evaluated because it causes side effects ( was used)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeFactory.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CausesSideEffects;
    ```

## Struct `DbgEEAssignmentResult`

Expression evaluator assignment result

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgEEAssignmentResult(flags: /* DbgEEAssignmentResultFlags */, error: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 209)

### Constructors

- `public DbgEEAssignmentResult(DbgEEAssignmentResultFlags flags, string error)`
  - Summary: Constructor
  - Parameters:
    - `DbgEEAssignmentResultFlags flags`: Result flags
    - `string error`: Error message or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 230)

### Properties

- `public DbgEEAssignmentResultFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 218)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public bool IsCompilerError => (Flags & DbgEEAssignmentResultFlags.CompilerError) != 0`
  - Summary: true if the error is from the compiler and no debuggee code was executed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 223)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsCompilerError;
    ```
- `public string Error { get; }`
  - Summary: Error message or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 213)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Enum `DbgEEAssignmentResultFlags`

Assignment result flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgEEAssignmentResultFlags and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgEEAssignmentResultFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 188)

### Members

- `None`: No bit is set
- `CompilerError` = `x00000001`: The error is from the compiler and no debuggee code was executed
- `ExecutedCode` = `x00000002`: Code in the debuggee was executed

## Class `DbgEvaluationContext`

Evaluation context

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgEvaluationContext and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgEvaluationContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationContext.cs` (line 26)

### Methods

- `public void Close()`
  - Summary: Closes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationContext.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```

### Properties

- `public DbgProcess Process => Runtime.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationContext.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DbgEvaluationContextOptions Options { get; }`
  - Summary: Context options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationContext.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```
- `public abstract DbgLanguage Language { get; }`
  - Summary: Gets the language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationContext.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Language;
    ```
- `public abstract DbgObject ContinueContext { get; }`
  - Summary: This object gets closed (and recreated) when the process continues
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationContext.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContinueContext;
    ```
- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationContext.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract TimeSpan FuncEvalTimeout { get; }`
  - Summary: Func-eval timeout (func-eval = calling functions in debugged process)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationContext.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FuncEvalTimeout;
    ```

## Enum `DbgEvaluationContextOptions`

Evaluation context options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgEvaluationContextOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgEvaluationContextOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 119)

### Members

- `None`: No bit is set
- `RunAllThreads` = `x00000001`: Set if all threads should run when func-evaluating (calling code in the debugged process), or cleared if only one thread should run. Usually only one thread is run, but that can lead to a deadlock if the thread calls a suspended thread or if it tries to acquire a lock owned by a suspended thread.
- `NoMethodBody` = `x00000002`: If method body info isn't needed, this option should be used. It prevents decompiling the method to get sequence points and other debug info. Can be used when formatting stack frames.

## Class `DbgEvaluationInfo`

Contains the classes needed to func-eval

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgEvaluationInfo(context: /* DbgEvaluationContext */, frame: /* DbgStackFrame */, cancellationToken: /* CancellationToken */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationInfo.cs` (line 28)

### Constructors

- `public DbgEvaluationInfo(DbgEvaluationContext context, DbgStackFrame frame, CancellationToken cancellationToken = default)`
  - Summary: Constructor
  - Parameters:
    - `DbgEvaluationContext context`: Evaluation context
    - `DbgStackFrame frame`: Stack frame
    - `CancellationToken cancellationToken` (default: `default`): Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationInfo.cs` (line 55)

### Methods

- `public void Close()`
  - Summary: Closes and
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationInfo.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```

### Properties

- `public CancellationToken CancellationToken { get; }`
  - Summary: Gets the cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationInfo.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CancellationToken;
    ```
- `public DbgEvaluationContext Context { get; }`
  - Summary: Gets the evaluation context
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationInfo.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Context;
    ```
- `public DbgRuntime Runtime => Context.Runtime`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationInfo.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public DbgStackFrame Frame { get; }`
  - Summary: Gets the stack frame
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgEvaluationInfo.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Frame;
    ```

## Enum `DbgEvaluationOptions`

Evaluation options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgEvaluationOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgEvaluationOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 63)

### Members

- `None`: No bit is set
- `Expression` = `x00000001`: Set if it's an expression, false if it's a statement
- `NoSideEffects` = `x00000002`: Fail if the expression causes side effects, eg. method calls
- `NoFuncEval` = `x00000004`: Don't allow function evaluations (calling code in debugged process)
- `NoName` = `x00000008`: Don't create a name/expression (only used by value nodes)
- `RawLocals` = `x00000010`: Use only the locals that exist in the metadata. Don't show captured variables, show their display class variables instead

## Struct `DbgEvaluationResult`

Evaluation result

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgEvaluationResult(value: /* DbgValue */, formatSpecifiers: /* ReadOnlyCollection<string> */, flags: /* DbgEvaluationResultFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 130)

### Constructors

- `public DbgEvaluationResult(DbgValue value, ReadOnlyCollection<string> formatSpecifiers, DbgEvaluationResultFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `DbgValue value`: Value
    - `ReadOnlyCollection<string> formatSpecifiers`: Format specifiers or null
    - `DbgEvaluationResultFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 164)
- `public DbgEvaluationResult(string error, ReadOnlyCollection<string> formatSpecifiers = null, DbgEvaluationResultFlags flags = 0)`
  - Summary: Constructor
  - Parameters:
    - `string error`: Error message
    - `ReadOnlyCollection<string> formatSpecifiers` (default: `null`): Format specifiers or null
    - `DbgEvaluationResultFlags flags` (default: `0`): Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 177)

### Properties

- `public DbgEvaluationResultFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 144)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public DbgValue Value { get; }`
  - Summary: Gets the value or null if there was an error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public ReadOnlyCollection<string> FormatSpecifiers { get; }`
  - Summary: Gets the format specifiers
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 139)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FormatSpecifiers;
    ```
- `public bool IsThrownException => (Flags & DbgEvaluationResultFlags.ThrownException) != 0`
  - Summary: true if is a thrown exception
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 149)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsThrownException;
    ```
- `public string Error { get; }`
  - Summary: Gets the error or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 154)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Enum `DbgEvaluationResultFlags`

Evaluation result flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgEvaluationResultFlags and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgEvaluationResultFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 99)

### Members

- `None`: No bit is set
- `SideEffects` = `x00000001`: The expression causes side effects
- `ReadOnly` = `x00000002`: The result is read-only
- `BooleanExpression` = `x00000004`: It's a boolean expression
- `ThrownException` = `x00000008`: The value is a thrown exception

## Struct `DbgExpressionEvaluationInfo`

Contains the expression to evaluate and options

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgExpressionEvaluationInfo(expression: /* string */, nodeOptions: /* DbgValueNodeEvaluationOptions */, options: /* DbgEvaluationOptions */, expressionEvaluatorState: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluationInfo.cs` (line 26)

### Constructors

- `public DbgExpressionEvaluationInfo(string expression, DbgValueNodeEvaluationOptions nodeOptions, DbgEvaluationOptions options, object expressionEvaluatorState)`
  - Summary: Constructor
  - Parameters:
    - `string expression`: Expression to evaluate
    - `DbgValueNodeEvaluationOptions nodeOptions`: Value node options
    - `DbgEvaluationOptions options`: Evaluation options
    - `object expressionEvaluatorState`: Expression evaluator state or null, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluationInfo.cs` (line 54)

### Properties

- `public DbgEvaluationOptions Options { get; }`
  - Summary: Gets the evaluation options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluationInfo.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```
- `public DbgValueNodeEvaluationOptions NodeOptions { get; }`
  - Summary: Gets the value node options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluationInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NodeOptions;
    ```
- `public object ExpressionEvaluatorState { get; }`
  - Summary: Expression evaluator state or null, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluationInfo.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExpressionEvaluatorState;
    ```
- `public string Expression { get; }`
  - Summary: Gets the expression to evaluate
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluationInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Expression;
    ```

## Class `DbgExpressionEvaluator`

Expression evaluator

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgExpressionEvaluator and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgExpressionEvaluator(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 27)

### Methods

- `public abstract DbgEEAssignmentResult Assign(DbgEvaluationInfo evalInfo, string expression, string valueExpression, DbgEvaluationOptions options)`
  - Summary: Assigns the value of an expression to another expression
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `string expression`: Target expression (lhs)
    - `string valueExpression`: Source expression (rhs)
    - `DbgEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.Assign(evalInfo: /* DbgEvaluationInfo */, expression: /* string */, valueExpression: /* string */, options: /* DbgEvaluationOptions */);
    ```
- `public abstract DbgEvaluationResult Evaluate(DbgEvaluationInfo evalInfo, string expression, DbgEvaluationOptions options, object state)`
  - Summary: Evaluates an expression. The returned is automatically closed when its runtime continues.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `string expression`: Expression to evaluate
    - `DbgEvaluationOptions options`: Options
    - `object state`: State created by or null to store the state in 's context
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Evaluate(evalInfo: /* DbgEvaluationInfo */, expression: /* string */, options: /* DbgEvaluationOptions */, state: /* object */);
    ```
- `public abstract object CreateExpressionEvaluatorState()`
  - Summary: Creates evaluator state used to cache data that is needed to evaluate an expression
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateExpressionEvaluatorState();
    ```

### Properties

- `public abstract DbgLanguage Language { get; }`
  - Summary: Gets the language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgExpressionEvaluator.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Language;
    ```

## Class `DbgFormatter`

Formats names, frames, values and types

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgFormatter and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgFormatter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgFormatter.cs` (line 27)

### Methods

- `public abstract void FormatExceptionName(DbgEvaluationContext context, IDbgTextWriter output, uint id)`
  - Summary: Formats an exception name
  - Parameters:
    - `DbgEvaluationContext context`: Evaluation context
    - `IDbgTextWriter output`: Output
    - `uint id`: Exception id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgFormatter.cs` (line 39)
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
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgFormatter.cs` (line 73)
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
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgFormatter.cs` (line 63)
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
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgFormatter.cs` (line 55)
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
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgFormatter.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatStowedExceptionName(context: /* DbgEvaluationContext */, output: /* IDbgTextWriter */, id: /* uint */);
    ```
- `public abstract void FormatType(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgValue value, DbgValueFormatterTypeOptions options, CultureInfo cultureInfo)`
  - Summary: Formats a value's type
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgValue value`: Value to format
    - `DbgValueFormatterTypeOptions options`: Options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgFormatter.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatType(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, value: /* DbgValue */, options: /* DbgValueFormatterTypeOptions */, cultureInfo: /* CultureInfo */);
    ```
- `public abstract void FormatValue(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgValue value, DbgValueFormatterOptions options, CultureInfo cultureInfo)`
  - Summary: Formats a value
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgValue value`: Value to format
    - `DbgValueFormatterOptions options`: Options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgFormatter.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatValue(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, value: /* DbgValue */, options: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```

### Properties

- `public abstract DbgLanguage Language { get; }`
  - Summary: Gets the language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgFormatter.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Language;
    ```

## Class `DbgLanguage`

Debugger language that evaluates expressions and formats values

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgLanguage and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgLanguage(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 29)

### Methods

- `public DbgEvaluationContext CreateContext(DbgStackFrame frame, DbgEvaluationContextOptions options = DbgEvaluationContextOptions.None, TimeSpan funcEvalTimeout = default, CancellationToken cancellationToken = default)`
  - Summary: Creates an evaluation context
  - Parameters:
    - `DbgStackFrame frame`: Stack frame
    - `DbgEvaluationContextOptions options` (default: `DbgEvaluationContextOptions.None`): Options
    - `TimeSpan funcEvalTimeout` (default: `default`): Func-eval timeout (func-eval = calling functions in the debugged process) or default instance to use default timeout value
    - `CancellationToken cancellationToken` (default: `default`): Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateContext(frame: /* DbgStackFrame */, options: /* DbgEvaluationContextOptions */, funcEvalTimeout: /* TimeSpan */, cancellationToken: /* CancellationToken */);
    ```
- `public abstract DbgEvaluationContext CreateContext(DbgRuntime runtime, DbgCodeLocation location, DbgEvaluationContextOptions options = DbgEvaluationContextOptions.None, TimeSpan funcEvalTimeout = default, CancellationToken cancellationToken = default)`
  - Summary: Creates an evaluation context
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `DbgCodeLocation location`: Location or null
    - `DbgEvaluationContextOptions options` (default: `DbgEvaluationContextOptions.None`): Options
    - `TimeSpan funcEvalTimeout` (default: `default`): Func-eval timeout (func-eval = calling functions in the debugged process) or default instance to use default timeout value
    - `CancellationToken cancellationToken` (default: `default`): Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateContext(runtime: /* DbgRuntime */, location: /* DbgCodeLocation */, options: /* DbgEvaluationContextOptions */, funcEvalTimeout: /* TimeSpan */, cancellationToken: /* CancellationToken */);
    ```

### Properties

- `public abstract DbgExpressionEvaluator ExpressionEvaluator { get; }`
  - Summary: Gets the expression evaluator
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExpressionEvaluator;
    ```
- `public abstract DbgFormatter Formatter { get; }`
  - Summary: Gets the formatter
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Formatter;
    ```
- `public abstract DbgLocalsValueNodeProvider LocalsProvider { get; }`
  - Summary: Gets the locals and parameters provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LocalsProvider;
    ```
- `public abstract DbgValueNodeFactory ValueNodeFactory { get; }`
  - Summary: Gets the factory
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueNodeFactory;
    ```
- `public abstract DbgValueNodeProvider AutosProvider { get; }`
  - Summary: Gets the autos provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AutosProvider;
    ```
- `public abstract DbgValueNodeProvider ExceptionsProvider { get; }`
  - Summary: Gets the exceptions provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExceptionsProvider;
    ```
- `public abstract DbgValueNodeProvider ReturnValuesProvider { get; }`
  - Summary: Gets the return values provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReturnValuesProvider;
    ```
- `public abstract DbgValueNodeProvider TypeVariablesProvider { get; }`
  - Summary: Gets the type variables provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeVariablesProvider;
    ```
- `public abstract Guid RuntimeKindGuid { get; }`
  - Summary: Gets the runtime kind GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeKindGuid;
    ```
- `public abstract string DisplayName { get; }`
  - Summary: Gets the language's display name (shown in the UI)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DisplayName;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the language name, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

### Fields

- `public static readonly TimeSpan DefaultFuncEvalTimeout = TimeSpan.FromSeconds(1)`
  - Summary: Default func-eval timeout value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguage.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.DbgLanguage.DefaultFuncEvalTimeout;
    ```

## Struct `DbgLanguageChangedEventArgs`

Language changed event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgLanguageChangedEventArgs(runtimeKindGuid: /* Guid */, language: /* DbgLanguage */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguageService.cs` (line 58)

### Constructors

- `public DbgLanguageChangedEventArgs(Guid runtimeKindGuid, DbgLanguage language)`
  - Summary: Constructor
  - Parameters:
    - `Guid runtimeKindGuid`: Runtime kind GUID, see
    - `DbgLanguage language`: New language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguageService.cs` (line 74)

### Properties

- `public DbgLanguage Language { get; }`
  - Summary: New language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguageService.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Language;
    ```
- `public Guid RuntimeKindGuid { get; }`
  - Summary: Runtime kind GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguageService.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RuntimeKindGuid;
    ```

## Class `DbgLanguageService`

Debugger language service

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgLanguageService and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgLanguageService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguageService.cs` (line 27)

### Methods

- `public abstract DbgLanguage GetCurrentLanguage(Guid runtimeKindGuid)`
  - Summary: Gets the current language the runtime uses
  - Parameters:
    - `Guid runtimeKindGuid`: Runtime kind GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguageService.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCurrentLanguage(runtimeKindGuid: /* Guid */);
    ```
- `public abstract ReadOnlyCollection<DbgLanguage> GetLanguages(Guid runtimeKindGuid)`
  - Summary: Gets all languages
  - Parameters:
    - `Guid runtimeKindGuid`: Runtime kind GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguageService.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLanguages(runtimeKindGuid: /* Guid */);
    ```
- `public abstract void SetCurrentLanguage(Guid runtimeKindGuid, DbgLanguage language)`
  - Summary: Sets the language that should be used by all runtimes with GUID
  - Parameters:
    - `Guid runtimeKindGuid`: Runtime kind GUID, see
    - `DbgLanguage language`: Language to use
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguageService.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.SetCurrentLanguage(runtimeKindGuid: /* Guid */, language: /* DbgLanguage */);
    ```

### Events

- `public abstract event EventHandler<DbgLanguageChangedEventArgs> LanguageChanged`
  - Summary: Raised when a runtime's current language is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgLanguageService.cs` (line 52)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.LanguageChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Enum `DbgLocalsValueNodeEvaluationOptions`

Locals value node provider options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgLocalsValueNodeEvaluationOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgLocalsValueNodeEvaluationOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 44)

### Members

- `None`: No bit is set
- `ShowCompilerGeneratedVariables` = `x00000001`: Show compiler generated variables ()
- `ShowDecompilerGeneratedVariables` = `x00000002`: Show decompiler generated variables ()
- `ShowRawLocals` = `x00000004`: Show raw locals ()

## Struct `DbgLocalsValueNodeInfo`

Contains a value node and its kind

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgLocalsValueNodeInfo(kind: /* DbgLocalsValueNodeKind */, valueNode: /* DbgValueNode */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 114)

### Constructors

- `public DbgLocalsValueNodeInfo(DbgLocalsValueNodeKind kind, DbgValueNode valueNode)`
  - Summary: Constructor
  - Parameters:
    - `DbgLocalsValueNodeKind kind`: What kind of value this is (local or parameter)
    - `DbgValueNode valueNode`: Value node
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 130)

### Properties

- `public DbgLocalsValueNodeKind Kind { get; }`
  - Summary: What kind of value this is (local or parameter)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 118)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public DbgValueNode ValueNode { get; }`
  - Summary: Gets the node
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 123)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueNode;
    ```

## Enum `DbgLocalsValueNodeKind`

Value node kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgLocalsValueNodeKind and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgLocalsValueNodeKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 89)

### Members

- `Unknown`: Unknown value
- `Parameter`: Parameter value
- `Local`: Local value
- `Error`: Error value

## Class `DbgLocalsValueNodeProvider`

Provides s for the locals window

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgLocalsValueNodeProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgLocalsValueNodeProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 70)

### Methods

- `public abstract DbgLocalsValueNodeInfo[] GetNodes(DbgEvaluationInfo evalInfo, DbgValueNodeEvaluationOptions options, DbgLocalsValueNodeEvaluationOptions localsOptions)`
  - Summary: Gets all values. The returned s are automatically closed when their runtime continues.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgValueNodeEvaluationOptions options`: Options
    - `DbgLocalsValueNodeEvaluationOptions localsOptions`: Locals value node provider options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNodes(evalInfo: /* DbgEvaluationInfo */, options: /* DbgValueNodeEvaluationOptions */, localsOptions: /* DbgLocalsValueNodeEvaluationOptions */);
    ```

### Properties

- `public abstract DbgLanguage Language { get; }`
  - Summary: Gets the language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Language;
    ```

## Class `DbgObjectId`

References a value in the debugged process

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgObjectId and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgObjectId(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectId.cs` (line 24)

### Methods

- `public abstract DbgValue GetValue(DbgEvaluationInfo evalInfo)`
  - Summary: Creates a new value. The returned is automatically closed when its runtime continues.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectId.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValue(evalInfo: /* DbgEvaluationInfo */);
    ```
- `public abstract void Remove()`
  - Summary: Removes and closes the object id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectId.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove();
    ```

### Properties

- `public DbgProcess Process => Runtime.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectId.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectId.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract uint Id { get; }`
  - Summary: Gets the unique id in the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectId.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Class `DbgObjectIdService`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgObjectIdService and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgObjectIdService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 27)

### Methods

- `public DbgObjectId CreateObjectId(DbgValue value, CreateObjectIdOptions options = CreateObjectIdOptions.None)`
  - Summary: Creates an object id or returns null
  - Parameters:
    - `DbgValue value`: Value
    - `CreateObjectIdOptions options` (default: `CreateObjectIdOptions.None`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateObjectId(value: /* DbgValue */, options: /* CreateObjectIdOptions */);
    ```
- `public abstract DbgObjectId GetObjectId(DbgRuntime runtime, uint id)`
  - Summary: Returns a non-hidden object id or null if there's none
  - Parameters:
    - `DbgRuntime runtime`: Runtime
    - `uint id`: Object id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.GetObjectId(runtime: /* DbgRuntime */, id: /* uint */);
    ```
- `public abstract DbgObjectId GetObjectId(DbgValue value)`
  - Summary: Returns an non-hidden object id or null if there's none that references
  - Parameters:
    - `DbgValue value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.GetObjectId(value: /* DbgValue */);
    ```
- `public abstract DbgObjectId[] CreateObjectIds(DbgValue[] values, CreateObjectIdOptions options = CreateObjectIdOptions.None)`
  - Summary: Creates object ids. The returned array will contain null elements if it wasn't possible to create object ids
  - Parameters:
    - `DbgValue[] values`: Values
    - `CreateObjectIdOptions options` (default: `CreateObjectIdOptions.None`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateObjectIds(values: /* DbgValue[] */, options: /* CreateObjectIdOptions */);
    ```
- `public abstract DbgObjectId[] GetObjectIds(DbgRuntime runtime)`
  - Summary: Gets all non-hidden object ids
  - Parameters:
    - `DbgRuntime runtime`: Runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.GetObjectIds(runtime: /* DbgRuntime */);
    ```
- `public abstract bool CanCreateObjectId(DbgValue value, CreateObjectIdOptions options = CreateObjectIdOptions.None)`
  - Summary: Returns true if it's possible to create an object id
  - Parameters:
    - `DbgValue value`: Value
    - `CreateObjectIdOptions options` (default: `CreateObjectIdOptions.None`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.CanCreateObjectId(value: /* DbgValue */, options: /* CreateObjectIdOptions */);
    ```
- `public abstract bool Equals(DbgObjectId objectId, DbgValue value)`
  - Summary: Checks if an object id and a value refer to the same data
  - Parameters:
    - `DbgObjectId objectId`: Object id
    - `DbgValue value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(objectId: /* DbgObjectId */, value: /* DbgValue */);
    ```
- `public abstract int GetHashCode(DbgObjectId objectId)`
  - Summary: Gets the hash code of an object id
  - Parameters:
    - `DbgObjectId objectId`: Object id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(objectId: /* DbgObjectId */);
    ```
- `public abstract void Remove(IEnumerable<DbgObjectId> objectIds)`
  - Summary: Removes and closes object ids
  - Parameters:
    - `IEnumerable<DbgObjectId> objectIds`: Object ids to remove and close
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(objectIds: /* IEnumerable<DbgObjectId> */);
    ```
- `public void Remove(DbgObjectId objectId)`
  - Summary: Removes and closes an object id
  - Parameters:
    - `DbgObjectId objectId`: Object id to remove and close
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(objectId: /* DbgObjectId */);
    ```

### Events

- `public abstract event EventHandler ObjectIdsChanged`
  - Summary: Raised when one or more non-hidden s are created or removed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgObjectIdService.cs` (line 31)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ObjectIdsChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `DbgRawAddressValue`

Contains the address and length of a value

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgRawAddressValue(address: /* ulong */, length: /* ulong */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 181)

### Constructors

- `public DbgRawAddressValue(ulong address, ulong length)`
  - Summary: Constructor
  - Parameters:
    - `ulong address`: Address
    - `ulong length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 197)

### Properties

- `public ulong Address { get; }`
  - Summary: Gets the address
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 185)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```
- `public ulong Length { get; }`
  - Summary: Gets the length
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 190)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```

## Enum `DbgSimpleValueType`

Type of value

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgSimpleValueType and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgSimpleValueType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 76)

### Members

- `Other`: Some other type
- `Void`: There's no value
- `Boolean`: Boolean, is a boxed
- `Char1`: 1-byte char, is a boxed
- `CharUtf16`: Char, is a boxed
- `Int8`: 8-bit signed int, is a boxed
- `Int16`: 16-bit signed int, is a boxed
- `Int32`: 32-bit signed int, is a boxed
- `Int64`: 64-bit signed int, is a boxed
- `UInt8`: 8-bit unsigned int, is a boxed
- `UInt16`: 16-bit unsigned int, is a boxed
- `UInt32`: 32-bit unsigned int, is a boxed
- `UInt64`: 64-bit unsigned int, is a boxed
- `Float32`: 32-bit floating point number, is a boxed
- `Float64`: 64-bit floating point number, is a boxed
- `Decimal`: Decimal, is a boxed
- `Ptr32`: 32-bit pointer, is a boxed
- `Ptr64`: 64-bit pointer, is a boxed
- `StringUtf16`: UTF-16 string, is a or null
- `DateTime`: A , is a boxed

## Enum `DbgStackFrameFormatterOptions`

Stack frame formatter options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgStackFrameFormatterOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgStackFrameFormatterOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgStackFrameFormatterOptions.cs` (line 26)

### Members

- `None`: No bit is set
- `ModuleNames` = `x00000001`: Show module name, eg. module.dll!func
- `ParameterTypes` = `x00000002`: Show parameter types
- `ParameterNames` = `x00000004`: Show parameter names
- `ParameterValues` = `x00000008`: Show parameter values
- `DeclaringTypes` = `x00000010`: Show declaring type
- `ReturnTypes` = `x00000020`: Show return type
- `Namespaces` = `x00000040`: Show namespace
- `IntrinsicTypeKeywords` = `x00000080`: Show intrinsic type keywords (eg. int instead of Int32)
- `Decimal` = `x00000100`: Set if integers are shown in decimal, clear if integers are shown in hexadecimal
- `Tokens` = `x00000200`: Show tokens
- `IP` = `x00000400`: Show instruction pointer
- `DigitSeparators` = `x00000800`: Use digit separators

## Class `DbgValue`

Result of evaluating an expression

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgValue and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgValue(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 24)

### Methods

- `public abstract DbgRawAddressValue? GetRawAddressValue(bool onlyDataAddress)`
  - Summary: Gets the address of the value or null if there's no address available. The returned address gets invalid when the runtime continues.
  - Parameters:
    - `bool onlyDataAddress`: If true and if it's a supported type (eg. a simple type such as integers, floating point values, strings or byte arrays) the returned object contains the address of the actual value, else the returned address and length covers the whole object including vtable, method table or other special data.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRawAddressValue(onlyDataAddress: /* bool */);
    ```
- `public abstract void Close()`
  - Summary: Closes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```

### Properties

- `public DbgProcess Process => Runtime.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract DbgSimpleValueType ValueType { get; }`
  - Summary: Type of the value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueType;
    ```
- `public abstract bool HasRawValue { get; }`
  - Summary: true if is valid
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasRawValue;
    ```
- `public abstract object InternalValue { get; }`
  - Summary: Gets the value object created by the debug engine
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InternalValue;
    ```
- `public abstract object RawValue { get; }`
  - Summary: The value. It's only valid if is true. A null value is a valid value. If it's an enum value, it's stored as the enum's underlying type (eg. )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValue.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RawValue;
    ```

## Class `DbgValueExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.Evaluation.DbgValueExtensions members directly without instantiation.
dnSpy.Contracts.Debugger.Evaluation.DbgValueExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgValueExtensions.cs` (line 26)

### Methods

- `public static DbgDotNetValue GetDotNetValue(this DbgValue value)`
  - Summary: Gets the .NET engine value
  - Parameters:
    - `this DbgValue value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DbgValueExtensions.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Evaluation.DbgValueExtensions.GetDotNetValue(value: /* DbgValue */);
    ```

## Enum `DbgValueFormatterOptions`

Value formatter options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgValueFormatterOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgValueFormatterOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueFormatterOptions.cs` (line 26)

### Members

- `None`: No bit is set
- `Edit` = `x00000001`: Set if it should be formatted so it can be edited
- `Decimal` = `x00000002`: Set if integers are shown in decimal, clear if integers are shown in hexadecimal
- `FuncEval` = `x00000004`: Set to allow function evaluations (calling methods in the debugged process)
- `ToString` = `x00000008`: Set to allow calling methods to get a string representation of the value. must also be set. If it's a simple type (eg. an integer), it's formatted without calling any methods in the debugged process and this flag is ignored.
- `DigitSeparators` = `x00000010`: Use digit separators. This flag is ignored if is set and the language doesn't support digit separators
- `NoStringQuotes` = `x00000020`: Don't show string quotes, just the raw string value
- `NoDebuggerDisplay` = `x00000040`: Don't use debugger display attributes
- `Namespaces` = `x20000000`: Show namespaces. Only used if is clear
- `IntrinsicTypeKeywords` = `x40000000`: Show intrinsic type keywords (eg. int instead of Int32)
- `Tokens` = `nt.MinValue`: Show tokens. Only used if is clear

## Enum `DbgValueFormatterTypeOptions`

Type formatter options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgValueFormatterTypeOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgValueFormatterTypeOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueFormatterTypeOptions.cs` (line 26)

### Members

- `None`: No bit is set
- `Decimal` = `x00000001`: Set if integers are shown in decimal, clear if integers are shown in hexadecimal
- `DigitSeparators` = `x00000002`: Use digit separators
- `Namespaces` = `x20000000`: Show namespaces
- `IntrinsicTypeKeywords` = `x40000000`: Show intrinsic type keywords (eg. int instead of Int32)
- `Tokens` = `nt.MinValue`: Show tokens

## Class `DbgValueNode`

A value shown in a treeview (eg. in locals window)

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgValueNode and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgValueNode(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 28)

### Methods

- `public abstract DbgValueNodeAssignmentResult Assign(DbgEvaluationInfo evalInfo, string expression, DbgEvaluationOptions options)`
  - Summary: Writes a new value
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `string expression`: Source expression (rhs)
    - `DbgEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 185)
  - Example:
    ```csharp
    // Example invocation
    instance.Assign(evalInfo: /* DbgEvaluationInfo */, expression: /* string */, options: /* DbgEvaluationOptions */);
    ```
- `public abstract DbgValueNode[] GetChildren(DbgEvaluationInfo evalInfo, ulong index, int count, DbgValueNodeEvaluationOptions options)`
  - Summary: Creates new children. The returned s are automatically closed when their runtime continues
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `ulong index`: Index of first child
    - `int count`: Max number of children to return
    - `DbgValueNodeEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 112)
  - Example:
    ```csharp
    // Example invocation
    instance.GetChildren(evalInfo: /* DbgEvaluationInfo */, index: /* ulong */, count: /* int */, options: /* DbgValueNodeEvaluationOptions */);
    ```
- `public abstract ulong GetChildCount(DbgEvaluationInfo evalInfo)`
  - Summary: Number of children. This property is called as late as possible and can be lazily initialized. It's assumed to be 0 if is false.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 102)
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
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 176)
  - Example:
    ```csharp
    // Example invocation
    instance.Format(evalInfo: /* DbgEvaluationInfo */, options: /* IDbgValueNodeFormatParameters */, cultureInfo: /* CultureInfo */);
    ```
- `public void FormatActualType(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgValueFormatterTypeOptions options, DbgValueFormatterOptions valueOptions, CultureInfo cultureInfo)`
  - Summary: Formats the actual type (value type)
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgValueFormatterTypeOptions options`: Formatter options
    - `DbgValueFormatterOptions valueOptions`: Value options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 163)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatActualType(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, options: /* DbgValueFormatterTypeOptions */, valueOptions: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```
- `public void FormatExpectedType(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgValueFormatterTypeOptions options, DbgValueFormatterOptions valueOptions, CultureInfo cultureInfo)`
  - Summary: Formats the expected type ("field" type)
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgValueFormatterTypeOptions options`: Formatter options
    - `DbgValueFormatterOptions valueOptions`: Value options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 148)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatExpectedType(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, options: /* DbgValueFormatterTypeOptions */, valueOptions: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```
- `public void FormatName(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgValueFormatterOptions options, CultureInfo cultureInfo = null)`
  - Summary: Formats the name
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgValueFormatterOptions options`: Formatter options
    - `CultureInfo cultureInfo` (default: `null`): Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatName(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, options: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```
- `public void FormatValue(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgValueFormatterOptions options, CultureInfo cultureInfo)`
  - Summary: Formats the value
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgValueFormatterOptions options`: Formatter options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 134)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatValue(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, options: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```

### Properties

- `public DbgProcess Process => Runtime.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public abstract DbgLanguage Language { get; }`
  - Summary: Gets the language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Language;
    ```
- `public abstract DbgRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract DbgValue Value { get; }`
  - Summary: Gets the value or null if there's none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public abstract bool CanEvaluateExpression { get; }`
  - Summary: true if it's a node that has an can be evaluated, false if it's a non-value node, eg. 'Type variables', 'Raw View', etc.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanEvaluateExpression;
    ```
- `public abstract bool CausesSideEffects { get; }`
  - Summary: true if the expression causes side effects
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CausesSideEffects;
    ```
- `public abstract bool IsReadOnly { get; }`
  - Summary: true if this is a read-only value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsReadOnly;
    ```
- `public abstract bool? HasChildren { get; }`
  - Summary: Returns true if it has children, false if it has no children and null if it's unknown (eg. it's too expensive to calculate it now). UI code can use this property to decide if it shows the treeview node expander ("|>").
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasChildren;
    ```
- `public abstract string ErrorMessage { get; }`
  - Summary: Gets the error message or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ErrorMessage;
    ```
- `public abstract string Expression { get; }`
  - Summary: Gets the expression that is used when adding an expression to the watch window or when assigning a new value to the source. See also .
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Expression;
    ```
- `public abstract string ImageName { get; }`
  - Summary: Image name, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageName;
    ```
- `public bool HasError => ErrorMessage != null`
  - Summary: true if this is an error value node
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasError;
    ```
- `public bool HasValue => Value != null`
  - Summary: true if is not null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasValue;
    ```

## Struct `DbgValueNodeAssignmentResult`

Assignment result

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgValueNodeAssignmentResult(flags: /* DbgEEAssignmentResultFlags */, error: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 191)

### Constructors

- `public DbgValueNodeAssignmentResult(DbgEEAssignmentResultFlags flags, string error)`
  - Summary: Constructor
  - Parameters:
    - `DbgEEAssignmentResultFlags flags`: Result flags
    - `string error`: Error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 207)

### Properties

- `public DbgEEAssignmentResultFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 200)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public string Error { get; }`
  - Summary: Gets the error message or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 195)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Enum `DbgValueNodeEvaluationOptions`

evaluation options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgValueNodeEvaluationOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgValueNodeEvaluationOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeEvaluationOptions.cs` (line 28)

### Members

- `None`: No bit is set
- `NoFuncEval` = `x00000001`: Don't allow function evaluations (calling code in debugged process)
- `ResultsView` = `x00000002`: Show the Results View only
- `DynamicView` = `x00000004`: Show the Dynamic View only
- `RawView` = `x00000008`: Show the raw view (don't use debugger type proxies)
- `HideCompilerGeneratedMembers` = `x00000010`: Hide compiler generated members in variables windows (respect debugger attributes, eg. )
- `RespectHideMemberAttributes` = `x00000020`: Respect attributes that can hide a member, eg. and
- `PublicMembers` = `x00000040`: Only show public members
- `NoHideRoots` = `x00000080`: Roots can't be hidden
- `HideDeprecatedError` = `x00000100`: Hide deprecated members

## Class `DbgValueNodeFactory`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgValueNodeFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgValueNodeFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeFactory.cs` (line 26)

### Methods

- `public DbgCreateValueNodeResult Create(DbgEvaluationInfo evalInfo, string expression, DbgValueNodeEvaluationOptions nodeOptions, DbgEvaluationOptions options, object expressionEvaluatorState)`
  - Summary: Creates s
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `string expression`: Expression
    - `DbgValueNodeEvaluationOptions nodeOptions`: Value node options
    - `DbgEvaluationOptions options`: Eval options
    - `object expressionEvaluatorState`: State created by or null to store the state in 's context
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeFactory.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(evalInfo: /* DbgEvaluationInfo */, expression: /* string */, nodeOptions: /* DbgValueNodeEvaluationOptions */, options: /* DbgEvaluationOptions */, expressionEvaluatorState: /* object */);
    ```
- `public abstract DbgCreateValueNodeResult[] Create(DbgEvaluationInfo evalInfo, DbgExpressionEvaluationInfo[] expressions)`
  - Summary: Creates a . The returned s are automatically closed when their runtime continues.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgExpressionEvaluationInfo[] expressions`: Expressions to evaluate
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeFactory.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(evalInfo: /* DbgEvaluationInfo */, expressions: /* DbgExpressionEvaluationInfo[] */);
    ```
- `public abstract DbgValueNode[] Create(DbgEvaluationInfo evalInfo, DbgObjectId[] objectIds, DbgValueNodeEvaluationOptions options)`
  - Summary: Creates s. The returned s are automatically closed when their runtime continues.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgObjectId[] objectIds`: Object ids
    - `DbgValueNodeEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeFactory.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(evalInfo: /* DbgEvaluationInfo */, objectIds: /* DbgObjectId[] */, options: /* DbgValueNodeEvaluationOptions */);
    ```

### Properties

- `public abstract DbgLanguage Language { get; }`
  - Summary: Gets the language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeFactory.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Language;
    ```

## Class `DbgValueNodeProvider`

Provides s for the variables windows

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.DbgValueNodeProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.DbgValueNodeProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 26)

### Methods

- `public abstract DbgValueNode[] GetNodes(DbgEvaluationInfo evalInfo, DbgValueNodeEvaluationOptions options)`
  - Summary: Gets all values. The returned s are automatically closed when their runtime continues.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgValueNodeEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNodes(evalInfo: /* DbgEvaluationInfo */, options: /* DbgValueNodeEvaluationOptions */);
    ```

### Properties

- `public abstract DbgLanguage Language { get; }`
  - Summary: Gets the language
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNodeProvider.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Language;
    ```

## Interface `IDbgValueNodeFormatParameters`

Parameters when formatting a

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Evaluation.IDbgValueNodeFormatParameters and call its members.
var instance = new dnSpy.Contracts.Debugger.Evaluation.IDbgValueNodeFormatParameters(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 216)

### Properties

- `DbgValueFormatterOptions NameFormatterOptions { get; }`
  - Summary: Name formatter options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 240)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NameFormatterOptions;
    ```
- `DbgValueFormatterOptions TypeFormatterOptions { get; }`
  - Summary: Type formatter options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 250)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeFormatterOptions;
    ```
- `DbgValueFormatterOptions ValueFormatterOptions { get; }`
  - Summary: Value formatter options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 245)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueFormatterOptions;
    ```
- `DbgValueFormatterTypeOptions ActualTypeFormatterOptions { get; }`
  - Summary: Actual type formatter options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 260)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActualTypeFormatterOptions;
    ```
- `DbgValueFormatterTypeOptions ExpectedTypeFormatterOptions { get; }`
  - Summary: Expected type formatter options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 255)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExpectedTypeFormatterOptions;
    ```
- `IDbgTextWriter ActualTypeOutput { get; }`
  - Summary: Used when writing the actual type (value type) or null if it's not written
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 235)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActualTypeOutput;
    ```
- `IDbgTextWriter ExpectedTypeOutput { get; }`
  - Summary: Used when writing the expected type ("field" type) or null if it's not written
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 230)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExpectedTypeOutput;
    ```
- `IDbgTextWriter NameOutput { get; }`
  - Summary: Used when writing the name or null if it's not written
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 220)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NameOutput;
    ```
- `IDbgTextWriter ValueOutput { get; }`
  - Summary: Used when writing the value or null if it's not written
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/DbgValueNode.cs` (line 225)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueOutput;
    ```

## Class `PredefinedDbgLanguageNames`

Predefined language names. These aren't language display names, they're just unique language names.

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgLanguageNames members directly without instantiation.
dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgLanguageNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgLanguageNames.cs` (line 24)

### Fields

- `public const string CSharp = "c-#-"`
  - Summary: C#
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgLanguageNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgLanguageNames.CSharp;
    ```
- `public const string None = "<no language>"`
  - Summary: No language is available
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgLanguageNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgLanguageNames.None;
    ```
- `public const string VisualBasic = "v-b-"`
  - Summary: Visual Basic
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgLanguageNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgLanguageNames.VisualBasic;
    ```

## Class `PredefinedDbgValueNodeImageNames`

Image names returned by

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames members directly without instantiation.
dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 24)

### Fields

- `public const string Array = nameof(Array)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Array;
    ```
- `public const string ArrayElement = nameof(ArrayElement)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ArrayElement;
    ```
- `public const string Class = nameof(Class)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 57)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Class;
    ```
- `public const string ClassInternal = nameof(ClassInternal)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ClassInternal;
    ```
- `public const string ClassPrivate = nameof(ClassPrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 59)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ClassPrivate;
    ```
- `public const string ClassProtected = nameof(ClassProtected)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 60)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ClassProtected;
    ```
- `public const string ClassPublic = nameof(ClassPublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 61)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ClassPublic;
    ```
- `public const string Constant = nameof(Constant)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 95)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Constant;
    ```
- `public const string ConstantAssembly = nameof(ConstantAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 99)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ConstantAssembly;
    ```
- `public const string ConstantCompilerControlled = nameof(ConstantCompilerControlled)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 102)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ConstantCompilerControlled;
    ```
- `public const string ConstantFamily = nameof(ConstantFamily)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 98)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ConstantFamily;
    ```
- `public const string ConstantFamilyAndAssembly = nameof(ConstantFamilyAndAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 100)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ConstantFamilyAndAssembly;
    ```
- `public const string ConstantFamilyOrAssembly = nameof(ConstantFamilyOrAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 101)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ConstantFamilyOrAssembly;
    ```
- `public const string ConstantPrivate = nameof(ConstantPrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 96)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ConstantPrivate;
    ```
- `public const string ConstantPublic = nameof(ConstantPublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 97)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ConstantPublic;
    ```
- `public const string Data = nameof(Data)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Data;
    ```
- `public const string Delegate = nameof(Delegate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 90)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Delegate;
    ```
- `public const string DelegateInternal = nameof(DelegateInternal)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 91)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.DelegateInternal;
    ```
- `public const string DelegatePrivate = nameof(DelegatePrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 92)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.DelegatePrivate;
    ```
- `public const string DelegateProtected = nameof(DelegateProtected)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 93)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.DelegateProtected;
    ```
- `public const string DelegatePublic = nameof(DelegatePublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 94)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.DelegatePublic;
    ```
- `public const string DereferencedPointer = nameof(DereferencedPointer)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.DereferencedPointer;
    ```
- `public const string DynamicView = nameof(DynamicView)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 51)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.DynamicView;
    ```
- `public const string DynamicViewElement = nameof(DynamicViewElement)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.DynamicViewElement;
    ```
- `public const string EEVariable = nameof(EEVariable)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EEVariable;
    ```
- `public const string Edit = nameof(Edit)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Edit;
    ```
- `public const string Enumeration = nameof(Enumeration)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 72)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Enumeration;
    ```
- `public const string EnumerationInternal = nameof(EnumerationInternal)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationInternal;
    ```
- `public const string EnumerationItem = nameof(EnumerationItem)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 77)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationItem;
    ```
- `public const string EnumerationItemAssembly = nameof(EnumerationItemAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 81)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationItemAssembly;
    ```
- `public const string EnumerationItemCompilerControlled = nameof(EnumerationItemCompilerControlled)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 84)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationItemCompilerControlled;
    ```
- `public const string EnumerationItemFamily = nameof(EnumerationItemFamily)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 80)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationItemFamily;
    ```
- `public const string EnumerationItemFamilyAndAssembly = nameof(EnumerationItemFamilyAndAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 82)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationItemFamilyAndAssembly;
    ```
- `public const string EnumerationItemFamilyOrAssembly = nameof(EnumerationItemFamilyOrAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 83)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationItemFamilyOrAssembly;
    ```
- `public const string EnumerationItemPrivate = nameof(EnumerationItemPrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 78)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationItemPrivate;
    ```
- `public const string EnumerationItemPublic = nameof(EnumerationItemPublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 79)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationItemPublic;
    ```
- `public const string EnumerationPrivate = nameof(EnumerationPrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 74)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationPrivate;
    ```
- `public const string EnumerationProtected = nameof(EnumerationProtected)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 75)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationProtected;
    ```
- `public const string EnumerationPublic = nameof(EnumerationPublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 76)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EnumerationPublic;
    ```
- `public const string Error = nameof(Error)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Error;
    ```
- `public const string Event = nameof(Event)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 128)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Event;
    ```
- `public const string EventAssembly = nameof(EventAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 132)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EventAssembly;
    ```
- `public const string EventCompilerControlled = nameof(EventCompilerControlled)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 135)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EventCompilerControlled;
    ```
- `public const string EventFamily = nameof(EventFamily)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 131)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EventFamily;
    ```
- `public const string EventFamilyAndAssembly = nameof(EventFamilyAndAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 133)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EventFamilyAndAssembly;
    ```
- `public const string EventFamilyOrAssembly = nameof(EventFamilyOrAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 134)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EventFamilyOrAssembly;
    ```
- `public const string EventPrivate = nameof(EventPrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 129)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EventPrivate;
    ```
- `public const string EventPublic = nameof(EventPublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 130)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.EventPublic;
    ```
- `public const string Exception = nameof(Exception)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Exception;
    ```
- `public const string ExceptionInternal = nameof(ExceptionInternal)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ExceptionInternal;
    ```
- `public const string ExceptionPrivate = nameof(ExceptionPrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 54)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ExceptionPrivate;
    ```
- `public const string ExceptionProtected = nameof(ExceptionProtected)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ExceptionProtected;
    ```
- `public const string ExceptionPublic = nameof(ExceptionPublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ExceptionPublic;
    ```
- `public const string ExtensionMethod = nameof(ExtensionMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 111)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ExtensionMethod;
    ```
- `public const string Field = nameof(Field)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 103)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Field;
    ```
- `public const string FieldAssembly = nameof(FieldAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 107)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.FieldAssembly;
    ```
- `public const string FieldCompilerControlled = nameof(FieldCompilerControlled)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 110)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.FieldCompilerControlled;
    ```
- `public const string FieldFamily = nameof(FieldFamily)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 106)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.FieldFamily;
    ```
- `public const string FieldFamilyAndAssembly = nameof(FieldFamilyAndAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 108)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.FieldFamilyAndAssembly;
    ```
- `public const string FieldFamilyOrAssembly = nameof(FieldFamilyOrAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 109)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.FieldFamilyOrAssembly;
    ```
- `public const string FieldPrivate = nameof(FieldPrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 104)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.FieldPrivate;
    ```
- `public const string FieldPublic = nameof(FieldPublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 105)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.FieldPublic;
    ```
- `public const string GenericMethodParameter = nameof(GenericMethodParameter)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.GenericMethodParameter;
    ```
- `public const string GenericTypeParameter = nameof(GenericTypeParameter)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.GenericTypeParameter;
    ```
- `public const string Information = nameof(Information)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Information;
    ```
- `public const string InstanceMembers = nameof(InstanceMembers)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.InstanceMembers;
    ```
- `public const string Interface = nameof(Interface)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 67)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Interface;
    ```
- `public const string InterfaceInternal = nameof(InterfaceInternal)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.InterfaceInternal;
    ```
- `public const string InterfacePrivate = nameof(InterfacePrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 69)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.InterfacePrivate;
    ```
- `public const string InterfaceProtected = nameof(InterfaceProtected)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 70)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.InterfaceProtected;
    ```
- `public const string InterfacePublic = nameof(InterfacePublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 71)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.InterfacePublic;
    ```
- `public const string Local = nameof(Local)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Local;
    ```
- `public const string Method = nameof(Method)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 112)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Method;
    ```
- `public const string MethodAssembly = nameof(MethodAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 116)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.MethodAssembly;
    ```
- `public const string MethodCompilerControlled = nameof(MethodCompilerControlled)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 119)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.MethodCompilerControlled;
    ```
- `public const string MethodFamily = nameof(MethodFamily)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 115)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.MethodFamily;
    ```
- `public const string MethodFamilyAndAssembly = nameof(MethodFamilyAndAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 117)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.MethodFamilyAndAssembly;
    ```
- `public const string MethodFamilyOrAssembly = nameof(MethodFamilyOrAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 118)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.MethodFamilyOrAssembly;
    ```
- `public const string MethodPrivate = nameof(MethodPrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 113)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.MethodPrivate;
    ```
- `public const string MethodPublic = nameof(MethodPublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 114)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.MethodPublic;
    ```
- `public const string Module = nameof(Module)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 85)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Module;
    ```
- `public const string ModuleInternal = nameof(ModuleInternal)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 86)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ModuleInternal;
    ```
- `public const string ModulePrivate = nameof(ModulePrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 87)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ModulePrivate;
    ```
- `public const string ModuleProtected = nameof(ModuleProtected)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ModuleProtected;
    ```
- `public const string ModulePublic = nameof(ModulePublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 89)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ModulePublic;
    ```
- `public const string ObjectAddress = nameof(ObjectAddress)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ObjectAddress;
    ```
- `public const string ObjectId = nameof(ObjectId)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ObjectId;
    ```
- `public const string Parameter = nameof(Parameter)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Parameter;
    ```
- `public const string Pointer = nameof(Pointer)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 45)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Pointer;
    ```
- `public const string Property = nameof(Property)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 120)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Property;
    ```
- `public const string PropertyAssembly = nameof(PropertyAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 124)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.PropertyAssembly;
    ```
- `public const string PropertyCompilerControlled = nameof(PropertyCompilerControlled)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 127)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.PropertyCompilerControlled;
    ```
- `public const string PropertyFamily = nameof(PropertyFamily)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 123)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.PropertyFamily;
    ```
- `public const string PropertyFamilyAndAssembly = nameof(PropertyFamilyAndAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 125)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.PropertyFamilyAndAssembly;
    ```
- `public const string PropertyFamilyOrAssembly = nameof(PropertyFamilyOrAssembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 126)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.PropertyFamilyOrAssembly;
    ```
- `public const string PropertyPrivate = nameof(PropertyPrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 121)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.PropertyPrivate;
    ```
- `public const string PropertyPublic = nameof(PropertyPublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 122)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.PropertyPublic;
    ```
- `public const string RawView = nameof(RawView)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.RawView;
    ```
- `public const string ResultsView = nameof(ResultsView)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ResultsView;
    ```
- `public const string ReturnValue = nameof(ReturnValue)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.ReturnValue;
    ```
- `public const string StaticMembers = nameof(StaticMembers)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.StaticMembers;
    ```
- `public const string StowedException = nameof(StowedException)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.StowedException;
    ```
- `public const string Structure = nameof(Structure)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 62)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Structure;
    ```
- `public const string StructureInternal = nameof(StructureInternal)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.StructureInternal;
    ```
- `public const string StructurePrivate = nameof(StructurePrivate)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 64)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.StructurePrivate;
    ```
- `public const string StructureProtected = nameof(StructureProtected)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 65)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.StructureProtected;
    ```
- `public const string StructurePublic = nameof(StructurePublic)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 66)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.StructurePublic;
    ```
- `public const string This = nameof(This)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.This;
    ```
- `public const string TypeVariables = nameof(TypeVariables)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.TypeVariables;
    ```
- `public const string Warning = nameof(Warning)`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedDbgValueNodeImageNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedDbgValueNodeImageNames.Warning;
    ```

## Class `PredefinedFormatSpecifiers`

Format specifiers used by variables windows https://docs.microsoft.com/en-us/visualstudio/debugger/format-specifiers-in-csharp

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers members directly without instantiation.
dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 29)

### Methods

- `public static DbgValueFormatterOptions GetValueFormatterOptions(ReadOnlyCollection<string> formatSpecifiers, DbgValueFormatterOptions options)`
  - Summary: Gets value formatter options
  - Parameters:
    - `ReadOnlyCollection<string> formatSpecifiers`: Format specifiers or null
    - `DbgValueFormatterOptions options`: Default options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 174)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.GetValueFormatterOptions(formatSpecifiers: /* ReadOnlyCollection<string> */, options: /* DbgValueFormatterOptions */);
    ```
- `public static DbgValueFormatterTypeOptions GetValueFormatterTypeOptions(ReadOnlyCollection<string> formatSpecifiers, DbgValueFormatterTypeOptions options)`
  - Summary: Gets value formatter type options
  - Parameters:
    - `ReadOnlyCollection<string> formatSpecifiers`: Format specifiers or null
    - `DbgValueFormatterTypeOptions options`: Default options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 238)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.GetValueFormatterTypeOptions(formatSpecifiers: /* ReadOnlyCollection<string> */, options: /* DbgValueFormatterTypeOptions */);
    ```
- `public static DbgValueNodeEvaluationOptions GetValueNodeEvaluationOptions(ReadOnlyCollection<string> formatSpecifiers, DbgValueNodeEvaluationOptions options)`
  - Summary: Gets value node evaluation options
  - Parameters:
    - `ReadOnlyCollection<string> formatSpecifiers`: Format specifiers or null
    - `DbgValueNodeEvaluationOptions options`: Default options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 284)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.GetValueNodeEvaluationOptions(formatSpecifiers: /* ReadOnlyCollection<string> */, options: /* DbgValueNodeEvaluationOptions */);
    ```

### Fields

- `public const string AllowFuncEval = "ac"`
  - Summary: Allow func-eval even if is used and expression causes side effects (ac = always calculate)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 79)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.AllowFuncEval;
    ```
- `public const string DebuggerDisplay = "dda"`
  - Summary: Use if available
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 111)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.DebuggerDisplay;
    ```
- `public const string Decimal = "d"`
  - Summary: Use decimal
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.Decimal;
    ```
- `public const string DigitSeparators = "ds"`
  - Summary: Digit separators
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 86)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.DigitSeparators;
    ```
- `public const string DynamicView = "dynamic"`
  - Summary: Dynamic view only
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.DynamicView;
    ```
- `public const string EditExpression = "edit"`
  - Summary: Use the same expression that's shown in the edit text box
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 96)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.EditExpression;
    ```
- `public const string Emulator = "emulator"`
  - Summary: Emulate the code without real func-eval
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.Emulator;
    ```
- `public const string Hexadecimal = "h"`
  - Summary: Use hexadecimal
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.Hexadecimal;
    ```
- `public const string Intrinsics = "intrinsics"`
  - Summary: Show intrinsic type keywords (eg. int instead of Int32)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 131)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.Intrinsics;
    ```
- `public const string Namespaces = "ns"`
  - Summary: Show namespaces
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 121)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.Namespaces;
    ```
- `public const string NoDebuggerDisplay = "ndda"`
  - Summary: Don't use
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 116)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.NoDebuggerDisplay;
    ```
- `public const string NoDigitSeparators = "nds"`
  - Summary: No digit seaparators
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 91)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.NoDigitSeparators;
    ```
- `public const string NoIntrinsics = "nointrinsics"`
  - Summary: Don't show intrinsic type keywords (eg. int instead of Int32)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 136)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.NoIntrinsics;
    ```
- `public const string NoNamespaces = "nns"`
  - Summary: Don't show namespaces
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 126)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.NoNamespaces;
    ```
- `public const string NoQuotes = "nq"`
  - Summary: No quotes, just show the raw string
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.NoQuotes;
    ```
- `public const string NoRespectHideMemberAttributes = "nhma"`
  - Summary: Don't respect attributes that can hide a member, eg. and
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 166)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.NoRespectHideMemberAttributes;
    ```
- `public const string NoShowCompilerGeneratedMembers = "ncgm"`
  - Summary: Don't show compiler generated members
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 156)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.NoShowCompilerGeneratedMembers;
    ```
- `public const string NoSideEffects = "nse"`
  - Summary: No side effects, it implies
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.NoSideEffects;
    ```
- `public const string NoToString = "nts"`
  - Summary: Don't use ToString() to format the value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 106)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.NoToString;
    ```
- `public const string NoTokens = "notokens"`
  - Summary: Don't show tokens
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 146)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.NoTokens;
    ```
- `public const string RawView = "raw"`
  - Summary: Raw view only
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.RawView;
    ```
- `public const string RespectHideMemberAttributes = "hma"`
  - Summary: Respect attributes that can hide a member, eg. and
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 161)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.RespectHideMemberAttributes;
    ```
- `public const string ResultsView = "results"`
  - Summary: Results view only
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.ResultsView;
    ```
- `public const string ShowAllMembers = "hidden"`
  - Summary: Show all members, even non-public ones
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.ShowAllMembers;
    ```
- `public const string ShowCompilerGeneratedMembers = "cgm"`
  - Summary: Show compiler generated members
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 151)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.ShowCompilerGeneratedMembers;
    ```
- `public const string Tokens = "tokens"`
  - Summary: Show tokens
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 141)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.Tokens;
    ```
- `public new const string ToString = "ts"`
  - Summary: Use ToString() if available to format the value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Evaluation/PredefinedFormatSpecifiers.cs` (line 101)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.Evaluation.PredefinedFormatSpecifiers.ToString;
    ```

