# Namespace `dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters`

## Struct `DbgDotNetEvalResult`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.DbgDotNetEvalResult(error: /* string */, formatSpecifiers: /* ReadOnlyCollection<string> */, flags: /* DbgEvaluationResultFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 45)

### Constructors

- `public DbgDotNetEvalResult(DbgDotNetValue value, ReadOnlyCollection<string> formatSpecifiers, DbgEvaluationResultFlags flags)`
  - Parameters:
    - `DbgDotNetValue value`: Description not provided.
    - `ReadOnlyCollection<string> formatSpecifiers`: Description not provided.
    - `DbgEvaluationResultFlags flags`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 58)
- `public DbgDotNetEvalResult(string error, ReadOnlyCollection<string> formatSpecifiers = null, DbgEvaluationResultFlags flags = 0)`
  - Parameters:
    - `string error`: Description not provided.
    - `ReadOnlyCollection<string> formatSpecifiers` (default: `null`): Description not provided.
    - `DbgEvaluationResultFlags flags` (default: `0`): Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 52)

### Properties

- `public DbgDotNetValue Value { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public DbgEvaluationResultFlags Flags { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public ReadOnlyCollection<string> FormatSpecifiers { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FormatSpecifiers;
    ```
- `public bool IsThrownException => (Flags & DbgEvaluationResultFlags.ThrownException) != 0`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsThrownException;
    ```
- `public string Error { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Error;
    ```

## Class `DbgDotNetFormatter`

Formats values, types, names. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.DbgDotNetFormatter and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.DbgDotNetFormatter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 32)

### Methods

- `public abstract void FormatExceptionName(DbgEvaluationContext context, IDbgTextWriter output, uint id)`
  - Summary: Formats an exception name
  - Parameters:
    - `DbgEvaluationContext context`: Evaluation context
    - `IDbgTextWriter output`: Output
    - `uint id`: Exception id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 39)
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
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 94)
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
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 63)
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
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 55)
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
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatStowedExceptionName(context: /* DbgEvaluationContext */, output: /* IDbgTextWriter */, id: /* uint */);
    ```
- `public abstract void FormatType(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DmdType type, DbgDotNetValue value, DbgValueFormatterTypeOptions options, CultureInfo cultureInfo)`
  - Summary: Formats a type
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DmdType type`: Type to format
    - `DbgDotNetValue value`: Value or null
    - `DbgValueFormatterTypeOptions options`: Options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatType(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, type: /* DmdType */, value: /* DbgDotNetValue */, options: /* DbgValueFormatterTypeOptions */, cultureInfo: /* CultureInfo */);
    ```
- `public abstract void FormatValue(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgDotNetValue value, DbgValueFormatterOptions options, CultureInfo cultureInfo)`
  - Summary: Formats a value
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgDotNetValue value`: Value to format
    - `DbgValueFormatterOptions options`: Options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatValue(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, value: /* DbgDotNetValue */, options: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```

## Class `ExportDbgDotNetFormatterAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgDotNetFormatterMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.ExportDbgDotNetFormatterAttribute(languageGuid: /* string */, order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 108)

### Constructors

- `public ExportDbgDotNetFormatterAttribute(string languageGuid, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string languageGuid`: Language GUID, see
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 115)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string LanguageGuid { get; }`
  - Summary: Language GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 124)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LanguageGuid;
    ```

## Interface `IDbgDotNetFormatterMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.IDbgDotNetFormatterMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.IDbgDotNetFormatterMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 98)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string LanguageGuid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/DbgDotNetFormatter.cs` (line 100)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LanguageGuid;
    ```

## Interface `IDebuggerDisplayAttributeEvaluator`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.IDebuggerDisplayAttributeEvaluator and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.IDebuggerDisplayAttributeEvaluator(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 33)

### Methods

- `DbgDotNetEvalResult Evaluate(DbgEvaluationInfo evalInfo, DbgDotNetValue obj, string expression, DbgEvaluationOptions options, object state)`
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Description not provided.
    - `DbgDotNetValue obj`: Description not provided.
    - `string expression`: Description not provided.
    - `DbgEvaluationOptions options`: Description not provided.
    - `object state`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Evaluate(evalInfo: /* DbgEvaluationInfo */, obj: /* DbgDotNetValue */, expression: /* string */, options: /* DbgEvaluationOptions */, state: /* object */);
    ```

## Class `IDebuggerDisplayAttributeEvaluatorUtils`

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.IDebuggerDisplayAttributeEvaluatorUtils members directly without instantiation.
dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.IDebuggerDisplayAttributeEvaluatorUtils./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 37)

### Methods

- `public static IDebuggerDisplayAttributeEvaluator GetDebuggerDisplayAttributeEvaluator(this DbgEvaluationContext context)`
  - Parameters:
    - `this DbgEvaluationContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.IDebuggerDisplayAttributeEvaluatorUtils.GetDebuggerDisplayAttributeEvaluator(context: /* DbgEvaluationContext */);
    ```
- `public static void Initialize(DbgEvaluationContext context, IDebuggerDisplayAttributeEvaluator evaluator)`
  - Parameters:
    - `DbgEvaluationContext context`: Description not provided.
    - `IDebuggerDisplayAttributeEvaluator evaluator`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/Formatters/IDebuggerDisplayAttributeEvaluator.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Evaluation.Formatters.IDebuggerDisplayAttributeEvaluatorUtils.Initialize(context: /* DbgEvaluationContext */, evaluator: /* IDebuggerDisplayAttributeEvaluator */);
    ```

