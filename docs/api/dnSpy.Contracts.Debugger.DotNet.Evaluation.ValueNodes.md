# Namespace `dnSpy.Contracts.Debugger.DotNet.Evaluation.ValueNodes`

## Struct `DbgDotNetTypeVariableInfo`

Contains the generic parameter and type

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ValueNodes.DbgDotNetTypeVariableInfo(genericParameterType: /* DmdType */, genericArgumentType: /* DmdType */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 141)

### Constructors

- `public DbgDotNetTypeVariableInfo(DmdType genericParameterType, DmdType genericArgumentType)`
  - Summary: Constructor
  - Parameters:
    - `DmdType genericParameterType`: Generic parameter type
    - `DmdType genericArgumentType`: Generic argument type
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 157)

### Properties

- `public DmdType GenericArgumentType { get; }`
  - Summary: Gets the generic argument type
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 150)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericArgumentType;
    ```
- `public DmdType GenericParameterType { get; }`
  - Summary: Gets the generic parameter type
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 145)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericParameterType;
    ```

## Class `DbgDotNetValueNode`

A .NET value node

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.ValueNodes.DbgDotNetValueNode and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ValueNodes.DbgDotNetValueNode(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 32)

### Methods

- `public abstract DbgDotNetValueNode[] GetChildren(DbgEvaluationInfo evalInfo, ulong index, int count, DbgValueNodeEvaluationOptions options)`
  - Summary: Creates new children
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `ulong index`: Index of first child
    - `int count`: Max number of children to return
    - `DbgValueNodeEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.GetChildren(evalInfo: /* DbgEvaluationInfo */, index: /* ulong */, count: /* int */, options: /* DbgValueNodeEvaluationOptions */);
    ```
- `public abstract ulong GetChildCount(DbgEvaluationInfo evalInfo)`
  - Summary: Number of children. This property is called as late as possible and can be lazily initialized. It's assumed to be 0 if is false.
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.GetChildCount(evalInfo: /* DbgEvaluationInfo */);
    ```
- `public virtual bool FormatActualType(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgDotNetFormatter formatter, DbgValueFormatterTypeOptions options, DbgValueFormatterOptions valueOptions, CultureInfo cultureInfo)`
  - Summary: Formats the actual type. Returns false if nothing was written to
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgDotNetFormatter formatter`: Formatter
    - `DbgValueFormatterTypeOptions options`: Options
    - `DbgValueFormatterOptions valueOptions`: Value options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 151)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatActualType(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, formatter: /* DbgDotNetFormatter */, options: /* DbgValueFormatterTypeOptions */, valueOptions: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```
- `public virtual bool FormatExpectedType(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgDotNetFormatter formatter, DbgValueFormatterTypeOptions options, DbgValueFormatterOptions valueOptions, CultureInfo cultureInfo)`
  - Summary: Formats the expected type. Returns false if nothing was written to
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgDotNetFormatter formatter`: Formatter
    - `DbgValueFormatterTypeOptions options`: Options
    - `DbgValueFormatterOptions valueOptions`: Value options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatExpectedType(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, formatter: /* DbgDotNetFormatter */, options: /* DbgValueFormatterTypeOptions */, valueOptions: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```
- `public virtual bool FormatName(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgDotNetFormatter formatter, DbgValueFormatterOptions options, CultureInfo cultureInfo)`
  - Summary: Formats the name. Returns false if nothing was written to
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgDotNetFormatter formatter`: Formatter
    - `DbgValueFormatterOptions options`: Options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 116)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatName(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, formatter: /* DbgDotNetFormatter */, options: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```
- `public virtual bool FormatValue(DbgEvaluationInfo evalInfo, IDbgTextWriter output, DbgDotNetFormatter formatter, DbgValueFormatterOptions options, CultureInfo cultureInfo)`
  - Summary: Formats the value column. Returns false if nothing was written to
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `IDbgTextWriter output`: Output
    - `DbgDotNetFormatter formatter`: Formatter
    - `DbgValueFormatterOptions options`: Options
    - `CultureInfo cultureInfo`: Culture or null to use invariant culture
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 127)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatValue(evalInfo: /* DbgEvaluationInfo */, output: /* IDbgTextWriter */, formatter: /* DbgDotNetFormatter */, options: /* DbgValueFormatterOptions */, cultureInfo: /* CultureInfo */);
    ```

### Properties

- `public abstract DbgDotNetText Name { get; }`
  - Summary: Gets the name
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public abstract DbgDotNetValue Value { get; }`
  - Summary: Gets the value or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public abstract DmdType ActualType { get; }`
  - Summary: Gets the actual type or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActualType;
    ```
- `public abstract DmdType ExpectedType { get; }`
  - Summary: Gets the expected type or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExpectedType;
    ```
- `public abstract ReadOnlyCollection<string> FormatSpecifiers { get; }`
  - Summary: Gets the format specifiers or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FormatSpecifiers;
    ```
- `public abstract bool CausesSideEffects { get; }`
  - Summary: true if the expression causes side effects
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CausesSideEffects;
    ```
- `public abstract bool IsReadOnly { get; }`
  - Summary: true if this is a read-only value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsReadOnly;
    ```
- `public abstract bool? HasChildren { get; }`
  - Summary: Returns true if it has children, false if it has no children and null if it's unknown (eg. it's too expensive to calculate it now). UI code can use this property to decide if it shows the treeview node expander ("|>").
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasChildren;
    ```
- `public abstract string ErrorMessage { get; }`
  - Summary: Gets the error message or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ErrorMessage;
    ```
- `public abstract string Expression { get; }`
  - Summary: Gets the expression
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Expression;
    ```
- `public abstract string ImageName { get; }`
  - Summary: Image name, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNode.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageName;
    ```

## Class `DbgDotNetValueNodeFactory`

Creates value nodes. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.ValueNodes.DbgDotNetValueNodeFactory and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ValueNodes.DbgDotNetValueNodeFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 32)

### Methods

- `public abstract DbgDotNetValueNode Create(DbgEvaluationInfo evalInfo, DbgDotNetText name, DbgDotNetValue value, ReadOnlyCollection<string> formatSpecifiers, DbgValueNodeEvaluationOptions options, string expression, string imageName, bool isReadOnly, bool causesSideEffects, DmdType expectedType)`
  - Summary: Creates a value node
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgDotNetText name`: Name
    - `DbgDotNetValue value`: Value
    - `ReadOnlyCollection<string> formatSpecifiers`: Format specifiers or null
    - `DbgValueNodeEvaluationOptions options`: Options
    - `string expression`: Expression
    - `string imageName`: Image name, see
    - `bool isReadOnly`: true if it's a read-only value
    - `bool causesSideEffects`: true if the expression causes side effects
    - `DmdType expectedType`: Expected type
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(evalInfo: /* DbgEvaluationInfo */, name: /* DbgDotNetText */, value: /* DbgDotNetValue */, formatSpecifiers: /* ReadOnlyCollection<string> */, options: /* DbgValueNodeEvaluationOptions */, expression: /* string */, imageName: /* string */, isReadOnly: /* bool */, causesSideEffects: /* bool */, expectedType: /* DmdType */);
    ```
- `public abstract DbgDotNetValueNode CreateError(DbgEvaluationInfo evalInfo, DbgDotNetText name, string errorMessage, string expression, bool causesSideEffects)`
  - Summary: Creates an error value node
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgDotNetText name`: Name
    - `string errorMessage`: Error message
    - `string expression`: Expression
    - `bool causesSideEffects`: true if the expression causes side effects
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 92)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateError(evalInfo: /* DbgEvaluationInfo */, name: /* DbgDotNetText */, errorMessage: /* string */, expression: /* string */, causesSideEffects: /* bool */);
    ```
- `public abstract DbgDotNetValueNode CreateException(DbgEvaluationInfo evalInfo, uint id, DbgDotNetValue value, ReadOnlyCollection<string> formatSpecifiers, DbgValueNodeEvaluationOptions options)`
  - Summary: Creates an exception value node
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint id`: Exception id
    - `DbgDotNetValue value`: Value
    - `ReadOnlyCollection<string> formatSpecifiers`: Format specifiers or null
    - `DbgValueNodeEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateException(evalInfo: /* DbgEvaluationInfo */, id: /* uint */, value: /* DbgDotNetValue */, formatSpecifiers: /* ReadOnlyCollection<string> */, options: /* DbgValueNodeEvaluationOptions */);
    ```
- `public abstract DbgDotNetValueNode CreateReturnValue(DbgEvaluationInfo evalInfo, uint id, DbgDotNetValue value, ReadOnlyCollection<string> formatSpecifiers, DbgValueNodeEvaluationOptions options, DmdMethodBase method)`
  - Summary: Creates a return value node
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint id`: Return value id
    - `DbgDotNetValue value`: Value
    - `ReadOnlyCollection<string> formatSpecifiers`: Format specifiers or null
    - `DbgValueNodeEvaluationOptions options`: Options
    - `DmdMethodBase method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateReturnValue(evalInfo: /* DbgEvaluationInfo */, id: /* uint */, value: /* DbgDotNetValue */, formatSpecifiers: /* ReadOnlyCollection<string> */, options: /* DbgValueNodeEvaluationOptions */, method: /* DmdMethodBase */);
    ```
- `public abstract DbgDotNetValueNode CreateStowedException(DbgEvaluationInfo evalInfo, uint id, DbgDotNetValue value, ReadOnlyCollection<string> formatSpecifiers, DbgValueNodeEvaluationOptions options)`
  - Summary: Creates an exception value node
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `uint id`: Stowed exception id
    - `DbgDotNetValue value`: Value
    - `ReadOnlyCollection<string> formatSpecifiers`: Format specifiers or null
    - `DbgValueNodeEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateStowedException(evalInfo: /* DbgEvaluationInfo */, id: /* uint */, value: /* DbgDotNetValue */, formatSpecifiers: /* ReadOnlyCollection<string> */, options: /* DbgValueNodeEvaluationOptions */);
    ```
- `public abstract DbgDotNetValueNode CreateTypeVariables(DbgEvaluationInfo evalInfo, DbgDotNetTypeVariableInfo[] typeVariableInfos)`
  - Summary: Creates type variables value node
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgDotNetTypeVariableInfo[] typeVariableInfos`: Type variables
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTypeVariables(evalInfo: /* DbgEvaluationInfo */, typeVariableInfos: /* DbgDotNetTypeVariableInfo[] */);
    ```

## Class `ExportDbgDotNetValueNodeFactoryAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgDotNetValueNodeFactoryMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ValueNodes.ExportDbgDotNetValueNodeFactoryAttribute(languageGuid: /* string */, order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 114)

### Constructors

- `public ExportDbgDotNetValueNodeFactoryAttribute(string languageGuid, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string languageGuid`: Language GUID, see
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 121)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 135)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string LanguageGuid { get; }`
  - Summary: Language GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 130)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LanguageGuid;
    ```

## Interface `IDbgDotNetValueNodeFactoryMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.ValueNodes.IDbgDotNetValueNodeFactoryMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ValueNodes.IDbgDotNetValueNodeFactoryMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 104)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 108)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string LanguageGuid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ValueNodes/DbgDotNetValueNodeFactory.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LanguageGuid;
    ```

