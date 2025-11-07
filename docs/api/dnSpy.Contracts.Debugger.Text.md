# Namespace `dnSpy.Contracts.Debugger.Text`

## Class `DbgStringBuilderTextWriter`

An using a . It ignores all colors passed to it.

**Inherits/Implements:** `IDbgTextWriter`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Text.DbgStringBuilderTextWriter();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Text/DbgStringBuilderTextWriter.cs` (line 28)

### Constructors

- `public DbgStringBuilderTextWriter()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DbgStringBuilderTextWriter.cs` (line 44)
- `public DbgStringBuilderTextWriter(StringBuilder stringBuilder)`
  - Summary: Constructor
  - Parameters:
    - `StringBuilder stringBuilder`: String builder
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DbgStringBuilderTextWriter.cs` (line 50)

### Methods

- `public override string ToString()`
  - Summary: Gets all the text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DbgStringBuilderTextWriter.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public void Reset()`
  - Summary: Resets this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DbgStringBuilderTextWriter.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.Reset();
    ```
- `public void Write(DbgTextColor color, string text)`
  - Summary: Writes text
  - Parameters:
    - `DbgTextColor color`: Color
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DbgStringBuilderTextWriter.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(color: /* DbgTextColor */, text: /* string */);
    ```
- `public void WriteLine()`
  - Summary: Writes a new line
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DbgStringBuilderTextWriter.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLine();
    ```

### Properties

- `public bool IsEmpty => sb.Length == 0`
  - Summary: true if nothing has been written
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DbgStringBuilderTextWriter.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public string Text => sb.ToString()`
  - Summary: Gets all the text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DbgStringBuilderTextWriter.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Enum `DbgTextColor`

Text colors used by formatters

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Text.DbgTextColor and call its members.
var instance = new dnSpy.Contracts.Debugger.Text.DbgTextColor(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Text/DbgTextColor.cs` (line 24)

### Members

- `Text`
- `Operator`
- `Punctuation`
- `Number`
- `Comment`
- `Keyword`
- `String`
- `VerbatimString`
- `Char`
- `Namespace`
- `Type`
- `SealedType`
- `StaticType`
- `Delegate`
- `Enum`
- `Interface`
- `ValueType`
- `Module`
- `TypeGenericParameter`
- `MethodGenericParameter`
- `InstanceMethod`
- `StaticMethod`
- `ExtensionMethod`
- `InstanceField`
- `EnumField`
- `LiteralField`
- `StaticField`
- `InstanceEvent`
- `StaticEvent`
- `InstanceProperty`
- `StaticProperty`
- `Local`
- `Parameter`
- `ModuleName`
- `Error`
- `ToStringEval`
- `ExceptionName`
- `StowedExceptionName`
- `ReturnValueName`
- `VariableName`
- `ObjectIdName`
- `DebuggerDisplayAttributeEval`
- `DebuggerNoStringQuotesEval`
- `DebugViewPropertyName`

## Interface `IDbgTextWriter`

Writes text

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Text.IDbgTextWriter and call its members.
var instance = new dnSpy.Contracts.Debugger.Text.IDbgTextWriter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Text/IDbgTextWriter.cs` (line 24)

### Methods

- `void Write(DbgTextColor color, string text)`
  - Summary: Writes text
  - Parameters:
    - `DbgTextColor color`: Color
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/IDbgTextWriter.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(color: /* DbgTextColor */, text: /* string */);
    ```

