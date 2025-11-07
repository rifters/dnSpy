# Namespace `dnSpy.Contracts.Hex.Text`

## Struct `HexClassifiedText`

Classified text

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Text.HexClassifiedText(text: /* string */, tag: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexClassifiedText.cs` (line 26)

### Constructors

- `public HexClassifiedText(string text, string tag)`
  - Summary: Constructor
  - Parameters:
    - `string text`: Text
    - `string tag`: Tag, see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexClassifiedText.cs` (line 42)

### Properties

- `public string Tag { get; }`
  - Summary: Tag, see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexClassifiedText.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```
- `public string Text { get; }`
  - Summary: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexClassifiedText.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Class `HexClassifiedTextCollection`

collection

**Inherits/Implements:** `IEnumerable<HexClassifiedText>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Text.HexClassifiedTextCollection(text: /* IEnumerable<HexClassifiedText> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexClassifiedTextCollection.cs` (line 29)

### Constructors

- `public HexClassifiedTextCollection(HexClassifiedText[] text)`
  - Summary: Constructor
  - Parameters:
    - `HexClassifiedText[] text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexClassifiedTextCollection.cs` (line 58)
- `public HexClassifiedTextCollection(IEnumerable<HexClassifiedText> text)`
  - Summary: Constructor
  - Parameters:
    - `IEnumerable<HexClassifiedText> text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexClassifiedTextCollection.cs` (line 48)

### Methods

- `public IEnumerator<HexClassifiedText> GetEnumerator()`
  - Summary: Gets the enumerator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexClassifiedTextCollection.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEnumerator();
    ```

### Properties

- `public int Count => text.Length`
  - Summary: Gets the number of elements in the collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexClassifiedTextCollection.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Count;
    ```

### Indexers

- `public ref readonly HexClassifiedText this[int index]`
  - Summary: Gets a
  - Parameters:
    - `int index`: Index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexClassifiedTextCollection.cs` (line 42)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

## Class `HexTextWriter`

Writes text

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Text.HexTextWriter();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexTextWriter.cs` (line 26)

### Constructors

- `protected HexTextWriter()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexTextWriter.cs` (line 30)

### Methods

- `public abstract void Write(string text, string tag)`
  - Summary: Writes text
  - Parameters:
    - `string text`: Text
    - `string tag`: Tag, see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexTextWriter.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, tag: /* string */);
    ```
- `public void WriteLine()`
  - Summary: Writes a new line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexTextWriter.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLine();
    ```
- `public void WriteSpace()`
  - Summary: Writes a space
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/HexTextWriter.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteSpace();
    ```

## Class `PredefinedClassifiedTextTags`

tags

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags members directly without instantiation.
dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 24)

### Fields

- `public const string ArrayName = nameof(ArrayName)`
  - Summary: Array name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.ArrayName;
    ```
- `public const string Char = nameof(Char)`
  - Summary: Char
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.Char;
    ```
- `public const string DotNetHeapName = nameof(DotNetHeapName)`
  - Summary: .NET heap name, eg. #GUID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 64)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.DotNetHeapName;
    ```
- `public const string Enum = nameof(Enum)`
  - Summary: Enum type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.Enum;
    ```
- `public const string EnumField = nameof(EnumField)`
  - Summary: Enum field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.EnumField;
    ```
- `public const string Error = nameof(Error)`
  - Summary: Error
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.Error;
    ```
- `public const string Field = nameof(Field)`
  - Summary: Field
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.Field;
    ```
- `public const string FileDot = nameof(FileDot)`
  - Summary: Dot between filename and extension
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 60)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.FileDot;
    ```
- `public const string FileExtension = nameof(FileExtension)`
  - Summary: File extension
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 62)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.FileExtension;
    ```
- `public const string Filename = nameof(Filename)`
  - Summary: Filename without extension
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.Filename;
    ```
- `public const string Keyword = nameof(Keyword)`
  - Summary: Keyword
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.Keyword;
    ```
- `public const string Number = nameof(Number)`
  - Summary: Number
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.Number;
    ```
- `public const string Operator = nameof(Operator)`
  - Summary: Operator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.Operator;
    ```
- `public const string PathName = nameof(PathName)`
  - Summary: Path name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 54)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.PathName;
    ```
- `public const string PathSeparator = nameof(PathSeparator)`
  - Summary: Path separator
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.PathSeparator;
    ```
- `public const string Punctuation = nameof(Punctuation)`
  - Summary: Punctuation
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.Punctuation;
    ```
- `public const string String = nameof(String)`
  - Summary: String
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.String;
    ```
- `public const string StructureName = nameof(StructureName)`
  - Summary: Structure name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.StructureName;
    ```
- `public const string Text = nameof(Text)`
  - Summary: Normal text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.Text;
    ```
- `public const string ValueType = nameof(ValueType)`
  - Summary: Value type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Text/PredefinedClassifiedTextTags.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Text.PredefinedClassifiedTextTags.ValueType;
    ```

