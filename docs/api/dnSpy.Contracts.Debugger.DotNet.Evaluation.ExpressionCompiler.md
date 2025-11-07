# Namespace `dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler`

## Struct `DbgDotNetAlias`

An alias (eg. return value, object id, etc)

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetAlias(kind: /* DbgDotNetAliasKind */, type: /* string */, name: /* string */, customTypeInfoId: /* Guid */, customTypeInfo: /* ReadOnlyCollection<byte> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetAlias.cs` (line 57)

### Constructors

- `public DbgDotNetAlias(DbgDotNetAliasKind kind, string type, string name, Guid customTypeInfoId, ReadOnlyCollection<byte> customTypeInfo)`
  - Summary: Constructor
  - Parameters:
    - `DbgDotNetAliasKind kind`: Alias kind
    - `string type`: Serialized type name, see
    - `string name`: Name, eg. "$ReturnValue", "$1"
    - `Guid customTypeInfoId`: Custom type info ID
    - `ReadOnlyCollection<byte> customTypeInfo`: Custom type info understood by the EE or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetAlias.cs` (line 91)

### Fields

- `public DbgDotNetAliasKind Kind`
  - Summary: Alias kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetAlias.cs` (line 61)
  - Example:
    ```csharp
    var value = instance.Kind;
    ```
- `public Guid CustomTypeInfoId`
  - Summary: Custom type info ID
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetAlias.cs` (line 71)
  - Example:
    ```csharp
    var value = instance.CustomTypeInfoId;
    ```
- `public ReadOnlyCollection<byte> CustomTypeInfo`
  - Summary: Custom type info understood by the EE or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetAlias.cs` (line 66)
  - Example:
    ```csharp
    var value = instance.CustomTypeInfo;
    ```
- `public string Name`
  - Summary: Name, eg. "$ReturnValue", "$1"
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetAlias.cs` (line 76)
  - Example:
    ```csharp
    var value = instance.Name;
    ```
- `public string Type`
  - Summary: Serialized type name, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetAlias.cs` (line 81)
  - Example:
    ```csharp
    var value = instance.Type;
    ```

## Enum `DbgDotNetAliasKind`

Alias kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetAliasKind and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetAliasKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetAlias.cs` (line 27)

### Members

- `Exception`: An exception, eg. "$exception"
- `StowedException`: A stowed exception, eg. "$stowedexception"
- `ReturnValue`: A return value, eg. "$ReturnValue", "$ReturnValue1"
- `Variable`: A variable created by the user that doesn't exist in code
- `ObjectId`: An object ID, eg. "$1", "$3"

## Struct `DbgDotNetCompilationResult`

Contains the compiled assembly and info on which method to evaluate to get the result of an expression

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetCompilationResult(errorMessage: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 30)

### Constructors

- `public DbgDotNetCompilationResult(byte[] assembly, DbgDotNetCompiledExpressionResult[] compiledExpressions)`
  - Summary: Constructor
  - Parameters:
    - `byte[] assembly`: .NET assembly bytes
    - `DbgDotNetCompiledExpressionResult[] compiledExpressions`: Compiled expressions info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 67)
- `public DbgDotNetCompilationResult(string errorMessage)`
  - Summary: Constructor
  - Parameters:
    - `string errorMessage`: Error message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 56)

### Properties

- `public DbgDotNetCompiledExpressionResult[] CompiledExpressions { get; }`
  - Summary: Gets the result of all compiled expressions or null if there was an error ()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CompiledExpressions;
    ```
- `public bool IsError => ErrorMessage != null`
  - Summary: true if it has an error message ()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsError;
    ```
- `public byte[] Assembly { get; }`
  - Summary: Gets the .NET assembly bytes or null if there was an error (). It's empty if is empty.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Assembly;
    ```
- `public string ErrorMessage { get; }`
  - Summary: Gets the error message or null if there was no error
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ErrorMessage;
    ```

## Struct `DbgDotNetCompiledExpressionResult`

Compiled expression result

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetCompiledExpressionResult and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetCompiledExpressionResult(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 93)

### Methods

- `public static DbgDotNetCompiledExpressionResult Create(string typeName, string methodName, string expression, DbgDotNetText name, DbgEvaluationResultFlags flags, string imageName, DbgDotNetCustomTypeInfo customTypeInfo = null, ReadOnlyCollection<string> formatSpecifiers = null, DbgDotNetCompiledExpressionResultFlags resultFlags = DbgDotNetCompiledExpressionResultFlags.None, int index = -1)`
  - Summary: Creates a successful compiled expression with no error
  - Parameters:
    - `string typeName`: Name of type that contains the method to evaluate
    - `string methodName`: Name of the method to evaluate
    - `string expression`: Original expression
    - `DbgDotNetText name`: Display name shown in the UI
    - `DbgEvaluationResultFlags flags`: Evaluation result flags
    - `string imageName`: Image, see
    - `DbgDotNetCustomTypeInfo customTypeInfo` (default: `null`): Optional custom type info known by the language expression compiler and the language value formatter
    - `ReadOnlyCollection<string> formatSpecifiers` (default: `null`): Format specifiers
    - `DbgDotNetCompiledExpressionResultFlags resultFlags` (default: `DbgDotNetCompiledExpressionResultFlags.None`): Result flags
    - `int index` (default: `-1`): Parameter/local index or -1 if unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 163)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetCompiledExpressionResult.Create(typeName: /* string */, methodName: /* string */, expression: /* string */, name: /* DbgDotNetText */, flags: /* DbgEvaluationResultFlags */, imageName: /* string */, customTypeInfo: /* DbgDotNetCustomTypeInfo */, formatSpecifiers: /* ReadOnlyCollection<string> */, resultFlags: /* DbgDotNetCompiledExpressionResultFlags */, index: /* int */);
    ```
- `public static DbgDotNetCompiledExpressionResult CreateError(string expression, DbgDotNetText name, string errorMessage)`
  - Summary: Creates an error
  - Parameters:
    - `string expression`: Expression
    - `DbgDotNetText name`: Display name shown in the UI
    - `string errorMessage`: Error message, see also
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetCompiledExpressionResult.CreateError(expression: /* string */, name: /* DbgDotNetText */, errorMessage: /* string */);
    ```

### Fields

- `public DbgDotNetCompiledExpressionResultFlags ResultFlags`
  - Summary: Gets the compiled expression flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 147)
  - Example:
    ```csharp
    var value = instance.ResultFlags;
    ```
- `public DbgDotNetCustomTypeInfo CustomTypeInfo`
  - Summary: Gets extra custom type info or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 132)
  - Example:
    ```csharp
    var value = instance.CustomTypeInfo;
    ```
- `public DbgDotNetText Name`
  - Summary: Display name shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 117)
  - Example:
    ```csharp
    var value = instance.Name;
    ```
- `public DbgEvaluationResultFlags Flags`
  - Summary: Gets the evaluation result flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 122)
  - Example:
    ```csharp
    var value = instance.Flags;
    ```
- `public ReadOnlyCollection<string> FormatSpecifiers`
  - Summary: Gets the format specifiers or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 137)
  - Example:
    ```csharp
    var value = instance.FormatSpecifiers;
    ```
- `public int Index`
  - Summary: Parameter/local index or -1 if unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 142)
  - Example:
    ```csharp
    var value = instance.Index;
    ```
- `public string ErrorMessage`
  - Summary: Error message or null if no error. See also
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 97)
  - Example:
    ```csharp
    var value = instance.ErrorMessage;
    ```
- `public string Expression`
  - Summary: Gets the expression that was compiled. This is eg. a C# or Visual Basic expression.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 112)
  - Example:
    ```csharp
    var value = instance.Expression;
    ```
- `public string ImageName`
  - Summary: Gets the image, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 127)
  - Example:
    ```csharp
    var value = instance.ImageName;
    ```
- `public string MethodName`
  - Summary: Name of the method that should be evaluated. The declaring type is
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 107)
  - Example:
    ```csharp
    var value = instance.MethodName;
    ```
- `public string TypeName`
  - Summary: Name of the type that contains the method () that should be evaluated
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 102)
  - Example:
    ```csharp
    var value = instance.TypeName;
    ```

## Enum `DbgDotNetCompiledExpressionResultFlags`

Compiled expression result flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetCompiledExpressionResultFlags and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetCompiledExpressionResultFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetCompilationResult.cs` (line 77)

### Members

- `None`: No bit is set
- `CompilerGenerated` = `x00000001`: Compiler generated variable

## Class `DbgDotNetExpressionCompiler`

A .NET expression compiler. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetExpressionCompiler and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetExpressionCompiler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 32)

### Methods

- `public abstract DbgDotNetCompilationResult CompileAssignment(DbgEvaluationInfo evalInfo, DbgModuleReference[] references, DbgDotNetAlias[] aliases, string target, string expression, DbgEvaluationOptions options)`
  - Summary: Compiles an assignment
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgModuleReference[] references`: .NET module references
    - `DbgDotNetAlias[] aliases`: Aliases
    - `string target`: Target expression (lhs)
    - `string expression`: Expression (rhs)
    - `DbgEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.CompileAssignment(evalInfo: /* DbgEvaluationInfo */, references: /* DbgModuleReference[] */, aliases: /* DbgDotNetAlias[] */, target: /* string */, expression: /* string */, options: /* DbgEvaluationOptions */);
    ```
- `public abstract DbgDotNetCompilationResult CompileExpression(DbgEvaluationInfo evalInfo, DbgModuleReference[] references, DbgDotNetAlias[] aliases, string expression, DbgEvaluationOptions options)`
  - Summary: Compiles an expression
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgModuleReference[] references`: .NET module references
    - `DbgDotNetAlias[] aliases`: Aliases
    - `string expression`: Expression
    - `DbgEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.CompileExpression(evalInfo: /* DbgEvaluationInfo */, references: /* DbgModuleReference[] */, aliases: /* DbgDotNetAlias[] */, expression: /* string */, options: /* DbgEvaluationOptions */);
    ```
- `public abstract DbgDotNetCompilationResult CompileGetLocals(DbgEvaluationInfo evalInfo, DbgModuleReference[] references, DbgEvaluationOptions options)`
  - Summary: Creates an assembly that is used to get all the locals
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DbgModuleReference[] references`: .NET module references
    - `DbgEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.CompileGetLocals(evalInfo: /* DbgEvaluationInfo */, references: /* DbgModuleReference[] */, options: /* DbgEvaluationOptions */);
    ```
- `public abstract DbgDotNetCompilationResult CompileTypeExpression(DbgEvaluationInfo evalInfo, DmdType type, DbgModuleReference[] references, DbgDotNetAlias[] aliases, string expression, DbgEvaluationOptions options)`
  - Summary: Compiles a type expression (compiles expressions)
  - Parameters:
    - `DbgEvaluationInfo evalInfo`: Evaluation info
    - `DmdType type`: Type
    - `DbgModuleReference[] references`: .NET module references
    - `DbgDotNetAlias[] aliases`: Aliases
    - `string expression`: Expression
    - `DbgEvaluationOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.CompileTypeExpression(evalInfo: /* DbgEvaluationInfo */, type: /* DmdType */, references: /* DbgModuleReference[] */, aliases: /* DbgDotNetAlias[] */, expression: /* string */, options: /* DbgEvaluationOptions */);
    ```
- `public abstract bool TryGetAliasInfo(string aliasName, out DbgDotNetParsedAlias aliasInfo)`
  - Summary: Gets alias info
  - Parameters:
    - `string aliasName`: Alias name
    - `out DbgDotNetParsedAlias aliasInfo`: Updated with alias info
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetAliasInfo(aliasName: /* string */, aliasInfo: /* DbgDotNetParsedAlias */);
    ```

## Struct `DbgDotNetParsedAlias`

Alias info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgDotNetParsedAlias(kind: /* DbgDotNetAliasKind */, id: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 166)

### Constructors

- `public DbgDotNetParsedAlias(DbgDotNetAliasKind kind, uint id)`
  - Summary: Constructor
  - Parameters:
    - `DbgDotNetAliasKind kind`: Alias kind
    - `uint id`: Id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 182)

### Fields

- `public DbgDotNetAliasKind Kind`
  - Summary: Alias kind
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 170)
  - Example:
    ```csharp
    var value = instance.Kind;
    ```
- `public uint Id`
  - Summary: Id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 175)
  - Example:
    ```csharp
    var value = instance.Id;
    ```

## Class `DbgModuleReference`

A reference to module metadata used by .NET expression compilers

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgModuleReference and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.DbgModuleReference(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgModuleReference.cs` (line 26)

### Properties

- `public abstract Guid GenerationId { get; }`
  - Summary: Gets the module generation id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgModuleReference.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenerationId;
    ```
- `public abstract Guid ModuleVersionId { get; }`
  - Summary: Gets the module version id
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgModuleReference.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleVersionId;
    ```
- `public abstract IntPtr MetadataAddress { get; }`
  - Summary: Gets the address of the .NET metadata (BSJB header)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgModuleReference.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataAddress;
    ```
- `public abstract uint MetadataSize { get; }`
  - Summary: Gets the size of the metadata
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgModuleReference.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataSize;
    ```

## Class `ExportDbgDotNetExpressionCompilerAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDbgDotNetExpressionCompilerMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.ExportDbgDotNetExpressionCompilerAttribute(languageGuid: /* string */, languageName: /* string */, languageDisplayName: /* string */, decompilerGuid: /* string */, order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 103)

### Constructors

- `public ExportDbgDotNetExpressionCompilerAttribute(string languageGuid, string languageName, string languageDisplayName, string decompilerGuid, double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `string languageGuid`: Language GUID, see
    - `string languageName`: Language name, see
    - `string languageDisplayName`: Language's display name (shown in the UI)
    - `string decompilerGuid`: Decompiler GUID, see or one of the decompiler GUIDs ()
    - `double order` (default: `double.MaxValue`): Order, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 113)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 145)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string DecompilerGuid { get; }`
  - Summary: Gets the decompiler GUID, see or one of the decompiler GUIDs ()
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 140)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DecompilerGuid;
    ```
- `public string LanguageDisplayName { get; }`
  - Summary: Gets the language's display name (shown in the UI)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 135)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LanguageDisplayName;
    ```
- `public string LanguageGuid { get; }`
  - Summary: Language GUID, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 125)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LanguageGuid;
    ```
- `public string LanguageName { get; }`
  - Summary: Gets the language name, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 130)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LanguageName;
    ```

## Interface `IDbgDotNetExpressionCompilerMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.IDbgDotNetExpressionCompilerMetadata and call its members.
var instance = new dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.IDbgDotNetExpressionCompilerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 87)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string DecompilerGuid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 95)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DecompilerGuid;
    ```
- `string LanguageDisplayName { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LanguageDisplayName;
    ```
- `string LanguageGuid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 89)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LanguageGuid;
    ```
- `string LanguageName { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LanguageName;
    ```

## Class `PredefinedDbgDotNetExpressionCompilerOrders`

Order of known expression compilers

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.PredefinedDbgDotNetExpressionCompilerOrders members directly without instantiation.
dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.PredefinedDbgDotNetExpressionCompilerOrders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 151)

### Fields

- `public const double CSharp = 1000000`
  - Summary: Order of C# expression compiler
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 155)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.PredefinedDbgDotNetExpressionCompilerOrders.CSharp;
    ```
- `public const double VisualBasic = 2000000`
  - Summary: Order of Visual Basic expression compiler
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/DbgDotNetExpressionCompiler.cs` (line 160)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.PredefinedDbgDotNetExpressionCompilerOrders.VisualBasic;
    ```

## Class `PredefinedDecompilerGuids`

Predefined decompiler guids

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.PredefinedDecompilerGuids members directly without instantiation.
dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.PredefinedDecompilerGuids./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/PredefinedDecompilerGuids.cs` (line 24)

### Fields

- `public const string CSharp = "2B77703E-870A-4A93-B622-C25DA3D44900"`
  - Summary: C# decompiler
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/PredefinedDecompilerGuids.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.PredefinedDecompilerGuids.CSharp;
    ```
- `public const string VisualBasic = "8A47CC93-4CBE-4288-9591-C0EED015B751"`
  - Summary: Visual Basic decompiler
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Evaluation/ExpressionCompiler/PredefinedDecompilerGuids.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Evaluation.ExpressionCompiler.PredefinedDecompilerGuids.VisualBasic;
    ```

