# Namespace `dnSpy.Contracts.Debugger.DotNet.Text`

## Struct `DbgDotNetText`

Contains text and color

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Text.DbgDotNetText(text: /* DbgDotNetTextPart */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 28)

### Constructors

- `public DbgDotNetText(DbgDotNetTextPart text)`
  - Summary: Constructor
  - Parameters:
    - `DbgDotNetTextPart text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 43)
- `public DbgDotNetText(DbgDotNetTextPart[] parts)`
  - Summary: Constructor
  - Parameters:
    - `DbgDotNetTextPart[] parts`: Color and text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 49)

### Methods

- `public override string ToString()`
  - Summary: Gets all text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public void WriteTo(IDbgTextWriter output)`
  - Summary: Writes all text and colors to
  - Parameters:
    - `IDbgTextWriter output`: Output
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteTo(output: /* IDbgTextWriter */);
    ```

### Properties

- `public DbgDotNetTextPart[] Parts { get; }`
  - Summary: Gets all colors and text parts
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Parts;
    ```

### Fields

- `public static readonly DbgDotNetText Empty = new DbgDotNetText(Array.Empty<DbgDotNetTextPart>())`
  - Summary: Gets the empty instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.DotNet.Text.DbgDotNetText.Empty;
    ```

## Class `DbgDotNetTextOutput`

Creates

**Inherits/Implements:** `IDbgTextWriter`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Text.DbgDotNetTextOutput();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetTextOutput.cs` (line 27)

### Constructors

- `public DbgDotNetTextOutput()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetTextOutput.cs` (line 33)

### Methods

- `public DbgDotNetText Create()`
  - Summary: Creates a
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetTextOutput.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```
- `public DbgDotNetText CreateAndReset()`
  - Summary: Creates a and clears this instance so it can be reused
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetTextOutput.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAndReset();
    ```
- `public void Clear()`
  - Summary: Clears this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetTextOutput.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```
- `public void Write(DbgTextColor color, string text)`
  - Summary: Writes text
  - Parameters:
    - `DbgTextColor color`: Color
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetTextOutput.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(color: /* DbgTextColor */, text: /* string */);
    ```

## Struct `DbgDotNetTextPart`

Color and text

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.DotNet.Text.DbgDotNetTextPart(color: /* DbgTextColor */, text: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 77)

### Constructors

- `public DbgDotNetTextPart(DbgTextColor color, string text)`
  - Summary: Constructor
  - Parameters:
    - `DbgTextColor color`: Color
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 93)

### Properties

- `public DbgTextColor Color { get; }`
  - Summary: Gets the color
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Color;
    ```
- `public string Text { get; }`
  - Summary: Gets the text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Text/DbgDotNetText.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

