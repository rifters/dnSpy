# Namespace `dnSpy.Decompiler.VisualBasic`

## Struct `VisualBasicFormatter`

**Example**

```csharp
var instance = new dnSpy.Decompiler.VisualBasic.VisualBasicFormatter(output: /* ITextColorWriter */, options: /* FormatterOptions */, cultureInfo: /* CultureInfo */);
```

*Defined in* `dnSpy/dnSpy.Decompiler/VisualBasic/VisualBasicFormatter.cs` (line 32)

### Constructors

- `public VisualBasicFormatter(ITextColorWriter output, FormatterOptions options, CultureInfo cultureInfo)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `FormatterOptions options`: Description not provided.
    - `CultureInfo cultureInfo`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/VisualBasic/VisualBasicFormatter.cs` (line 137)

### Methods

- `public void Write(IMemberRef member)`
  - Parameters:
    - `IMemberRef member`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/VisualBasic/VisualBasicFormatter.cs` (line 266)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(member: /* IMemberRef */);
    ```
- `public void WriteNamespaceToolTip(string @namespace)`
  - Parameters:
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/VisualBasic/VisualBasicFormatter.cs` (line 1092)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteNamespaceToolTip(@namespace: /* string */);
    ```
- `public void WriteToolTip(IMemberRef member)`
  - Parameters:
    - `IMemberRef member`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/VisualBasic/VisualBasicFormatter.cs` (line 227)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteToolTip(member: /* IMemberRef */);
    ```
- `public void WriteToolTip(ISourceVariable variable)`
  - Parameters:
    - `ISourceVariable variable`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/VisualBasic/VisualBasicFormatter.cs` (line 1065)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteToolTip(variable: /* ISourceVariable */);
    ```

