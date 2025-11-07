# Namespace `dnSpy.Decompiler.CSharp`

## Struct `CSharpFormatter`

**Example**

```csharp
var instance = new dnSpy.Decompiler.CSharp.CSharpFormatter(output: /* ITextColorWriter */, options: /* FormatterOptions */, cultureInfo: /* CultureInfo */);
```

*Defined in* `dnSpy/dnSpy.Decompiler/CSharp/CSharpFormatter.cs` (line 32)

### Constructors

- `public CSharpFormatter(ITextColorWriter output, FormatterOptions options, CultureInfo cultureInfo)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `FormatterOptions options`: Description not provided.
    - `CultureInfo cultureInfo`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/CSharp/CSharpFormatter.cs` (line 132)

### Methods

- `public void Write(IMemberRef member)`
  - Parameters:
    - `IMemberRef member`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/CSharp/CSharpFormatter.cs` (line 250)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(member: /* IMemberRef */);
    ```
- `public void WriteNamespaceToolTip(string @namespace)`
  - Parameters:
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/CSharp/CSharpFormatter.cs` (line 1084)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteNamespaceToolTip(@namespace: /* string */);
    ```
- `public void WriteToolTip(IMemberRef member)`
  - Parameters:
    - `IMemberRef member`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/CSharp/CSharpFormatter.cs` (line 211)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteToolTip(member: /* IMemberRef */);
    ```
- `public void WriteToolTip(ISourceVariable variable)`
  - Parameters:
    - `ISourceVariable variable`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/CSharp/CSharpFormatter.cs` (line 1065)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteToolTip(variable: /* ISourceVariable */);
    ```

