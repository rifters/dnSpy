# Namespace `dnSpy.Contracts.Debugger.Text.DnSpy`

## Class `ColorConverter`

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.Text.DnSpy.ColorConverter members directly without instantiation.
dnSpy.Contracts.Debugger.Text.DnSpy.ColorConverter./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/ColorConverter.cs` (line 27)

### Methods

- `public static DbgTextColor ToDebuggerColor(object color)`
  - Parameters:
    - `object color`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/ColorConverter.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Text.DnSpy.ColorConverter.ToDebuggerColor(color: /* object */);
    ```
- `public static object ToDnSpyColor(DbgTextColor color)`
  - Parameters:
    - `DbgTextColor color`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/ColorConverter.cs` (line 110)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Debugger.Text.DnSpy.ColorConverter.ToDnSpyColor(color: /* DbgTextColor */);
    ```

## Class `DbgTextClassifierTextColorWriter`

Implements and stores all colors and text. The result can be passed to

**Inherits/Implements:** `IDbgTextWriter`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Text.DnSpy.DbgTextClassifierTextColorWriter();
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextClassifierTextColorWriter.cs` (line 31)

### Constructors

- `public DbgTextClassifierTextColorWriter()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextClassifierTextColorWriter.cs` (line 53)

### Methods

- `public void Clear()`
  - Summary: Clears the text and colors so the instance can be reused
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextClassifierTextColorWriter.cs` (line 71)
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
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextClassifierTextColorWriter.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(color: /* DbgTextColor */, text: /* string */);
    ```

### Properties

- `public List<SpanData<object>> Colors => colors`
  - Summary: Gets the colors
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextClassifierTextColorWriter.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Colors;
    ```
- `public int Length => sb.Length`
  - Summary: Gets the text length
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextClassifierTextColorWriter.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public string Text => sb.ToString()`
  - Summary: Gets the text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextClassifierTextColorWriter.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Class `DbgTextColorWriter`

Implements and writes to a

**Inherits/Implements:** `ITextColorWriter`

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.Text.DnSpy.DbgTextColorWriter(writer: /* IDbgTextWriter */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextColorWriter.cs` (line 27)

### Constructors

- `public DbgTextColorWriter(IDbgTextWriter writer)`
  - Summary: Constructor
  - Parameters:
    - `IDbgTextWriter writer`: Debug text writer
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextColorWriter.cs` (line 34)

### Methods

- `public void Write(TextColor color, string text)`
  - Summary: Writes text
  - Parameters:
    - `TextColor color`: Color
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextColorWriter.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(color: /* TextColor */, text: /* string */);
    ```
- `public void Write(object color, string text)`
  - Summary: Writes text
  - Parameters:
    - `object color`: Color
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Text/DnSpy/DbgTextColorWriter.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(color: /* object */, text: /* string */);
    ```

