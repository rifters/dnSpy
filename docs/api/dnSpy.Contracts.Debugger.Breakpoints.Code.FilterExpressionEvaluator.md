# Namespace `dnSpy.Contracts.Debugger.Breakpoints.Code.FilterExpressionEvaluator`

## Class `DbgFilterEEVariableProvider`

Provides all the values of the variables that can be used by the filter expression

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.FilterExpressionEvaluator.DbgFilterEEVariableProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.FilterExpressionEvaluator.DbgFilterEEVariableProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterEEVariableProvider.cs` (line 24)

### Properties

- `public abstract int ProcessId { get; }`
  - Summary: Process id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterEEVariableProvider.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessId;
    ```
- `public abstract string MachineName { get; }`
  - Summary: Machine name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterEEVariableProvider.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MachineName;
    ```
- `public abstract string ProcessName { get; }`
  - Summary: Process name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterEEVariableProvider.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessName;
    ```
- `public abstract string ThreadName { get; }`
  - Summary: Thread name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterEEVariableProvider.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ThreadName;
    ```
- `public abstract ulong ThreadId { get; }`
  - Summary: Thread id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterEEVariableProvider.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ThreadId;
    ```

## Class `DbgFilterExpressionEvaluator`

Evaluates breakpoint filter expressions. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.FilterExpressionEvaluator.DbgFilterExpressionEvaluator and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.FilterExpressionEvaluator.DbgFilterExpressionEvaluator(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 29)

### Methods

- `public abstract DbgFilterExpressionEvaluatorResult Evaluate(string expr, DbgFilterEEVariableProvider variableProvider)`
  - Summary: Evaluates and returns the result of the expression.
  - Parameters:
    - `string expr`: Filter expression
    - `DbgFilterEEVariableProvider variableProvider`: Provides the values of the variables that can be used by the expression
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.Evaluate(expr: /* string */, variableProvider: /* DbgFilterEEVariableProvider */);
    ```
- `public abstract string IsValidExpression(string expr)`
  - Summary: Checks if is a valid expression. Returns null if it's a valid expression, otherwise an error string is returned.
  - Parameters:
    - `string expr`: Filter expression
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.IsValidExpression(expr: /* string */);
    ```
- `public abstract void Write(IDbgTextWriter output, string expr)`
  - Summary: Parses and writes text and color to
  - Parameters:
    - `IDbgTextWriter output`: Output
    - `string expr`: Expression
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* IDbgTextWriter */, expr: /* string */);
    ```

## Struct `DbgFilterExpressionEvaluatorResult`

Result of evaluating a filter expression

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.FilterExpressionEvaluator.DbgFilterExpressionEvaluatorResult(error: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 57)

### Constructors

- `public DbgFilterExpressionEvaluatorResult(bool result)`
  - Summary: Constructor
  - Parameters:
    - `bool result`: Result of evaluated expression
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 86)
- `public DbgFilterExpressionEvaluatorResult(string error)`
  - Summary: Constructor
  - Parameters:
    - `string error`: Error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 77)

### Properties

- `public bool HasError => Error != null`
  - Summary: true if there was an error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasError;
    ```
- `public bool Result { get; }`
  - Summary: Result if is false
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Result;
    ```
- `public string Error { get; }`
  - Summary: Error message if is true
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Class `ExportDbgFilterExpressionEvaluatorAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgFilterExpressionEvaluatorMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.FilterExpressionEvaluator.ExportDbgFilterExpressionEvaluatorAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 101)

### Constructors

- `public ExportDbgFilterExpressionEvaluatorAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 107)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 113)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDbgFilterExpressionEvaluatorMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.FilterExpressionEvaluator.IDbgFilterExpressionEvaluatorMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.FilterExpressionEvaluator.IDbgFilterExpressionEvaluatorMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 93)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/FilterExpressionEvaluator/DbgFilterExpressionEvaluator.cs` (line 95)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

