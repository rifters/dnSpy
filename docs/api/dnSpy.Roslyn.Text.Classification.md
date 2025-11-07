# Namespace `dnSpy.Roslyn.Text.Classification`

## Struct `ClassifierResult`

Classifier result

**Example**

```csharp
var instance = new dnSpy.Roslyn.Text.Classification.ClassifierResult(span: /* Span */, color: /* object */);
```

*Defined in* `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassifier.cs` (line 33)

### Constructors

- `public ClassifierResult(Span span, object color)`
  - Summary: Constructor
  - Parameters:
    - `Span span`: Span
    - `object color`: Color
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassifier.cs` (line 49)

### Fields

- `public readonly Span Span`
  - Summary: Span
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassifier.cs` (line 37)
  - Example:
    ```csharp
    var value = instance.Span;
    ```
- `public readonly object Color`
  - Summary: Color
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassifier.cs` (line 42)
  - Example:
    ```csharp
    var value = instance.Color;
    ```

## Class `RoslynClassificationTypes`

Classification types used by

**Example**

```csharp
// Instantiate dnSpy.Roslyn.Text.Classification.RoslynClassificationTypes and call its members.
var instance = new dnSpy.Roslyn.Text.Classification.RoslynClassificationTypes(/* arguments */);
```

*Defined in* `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 29)

### Methods

- `public static RoslynClassificationTypes GetClassificationTypeInstance(IThemeClassificationTypeService themeClassificationTypeService)`
  - Summary: Gets the cached instance that contains values
  - Parameters:
    - `IThemeClassificationTypeService themeClassificationTypeService`: Description not provided.
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 159)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Roslyn.Text.Classification.RoslynClassificationTypes.GetClassificationTypeInstance(themeClassificationTypeService: /* IThemeClassificationTypeService */);
    ```

### Fields

- `public readonly object Comment`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 31)
  - Example:
    ```csharp
    var value = instance.Comment;
    ```
- `public readonly object Delegate`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 32)
  - Example:
    ```csharp
    var value = instance.Delegate;
    ```
- `public readonly object Enum`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 33)
  - Example:
    ```csharp
    var value = instance.Enum;
    ```
- `public readonly object EnumField`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 34)
  - Example:
    ```csharp
    var value = instance.EnumField;
    ```
- `public readonly object ExcludedCode`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 35)
  - Example:
    ```csharp
    var value = instance.ExcludedCode;
    ```
- `public readonly object ExtensionMethod`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 36)
  - Example:
    ```csharp
    var value = instance.ExtensionMethod;
    ```
- `public readonly object InstanceEvent`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 37)
  - Example:
    ```csharp
    var value = instance.InstanceEvent;
    ```
- `public readonly object InstanceField`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 38)
  - Example:
    ```csharp
    var value = instance.InstanceField;
    ```
- `public readonly object InstanceMethod`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 39)
  - Example:
    ```csharp
    var value = instance.InstanceMethod;
    ```
- `public readonly object InstanceProperty`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 40)
  - Example:
    ```csharp
    var value = instance.InstanceProperty;
    ```
- `public readonly object Interface`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 41)
  - Example:
    ```csharp
    var value = instance.Interface;
    ```
- `public readonly object Keyword`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 42)
  - Example:
    ```csharp
    var value = instance.Keyword;
    ```
- `public readonly object Label`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 43)
  - Example:
    ```csharp
    var value = instance.Label;
    ```
- `public readonly object LiteralField`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 44)
  - Example:
    ```csharp
    var value = instance.LiteralField;
    ```
- `public readonly object Local`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 45)
  - Example:
    ```csharp
    var value = instance.Local;
    ```
- `public readonly object MethodGenericParameter`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 46)
  - Example:
    ```csharp
    var value = instance.MethodGenericParameter;
    ```
- `public readonly object Module`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 47)
  - Example:
    ```csharp
    var value = instance.Module;
    ```
- `public readonly object Namespace`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 48)
  - Example:
    ```csharp
    var value = instance.Namespace;
    ```
- `public readonly object Number`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 49)
  - Example:
    ```csharp
    var value = instance.Number;
    ```
- `public readonly object Operator`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 50)
  - Example:
    ```csharp
    var value = instance.Operator;
    ```
- `public readonly object Parameter`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 51)
  - Example:
    ```csharp
    var value = instance.Parameter;
    ```
- `public readonly object PreprocessorKeyword`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 52)
  - Example:
    ```csharp
    var value = instance.PreprocessorKeyword;
    ```
- `public readonly object PreprocessorText`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 53)
  - Example:
    ```csharp
    var value = instance.PreprocessorText;
    ```
- `public readonly object Punctuation`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 54)
  - Example:
    ```csharp
    var value = instance.Punctuation;
    ```
- `public readonly object SealedType`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 55)
  - Example:
    ```csharp
    var value = instance.SealedType;
    ```
- `public readonly object StaticEvent`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 56)
  - Example:
    ```csharp
    var value = instance.StaticEvent;
    ```
- `public readonly object StaticField`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 57)
  - Example:
    ```csharp
    var value = instance.StaticField;
    ```
- `public readonly object StaticMethod`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 58)
  - Example:
    ```csharp
    var value = instance.StaticMethod;
    ```
- `public readonly object StaticProperty`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 59)
  - Example:
    ```csharp
    var value = instance.StaticProperty;
    ```
- `public readonly object StaticType`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 60)
  - Example:
    ```csharp
    var value = instance.StaticType;
    ```
- `public readonly object String`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 61)
  - Example:
    ```csharp
    var value = instance.String;
    ```
- `public readonly object Text`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 62)
  - Example:
    ```csharp
    var value = instance.Text;
    ```
- `public readonly object Type`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 63)
  - Example:
    ```csharp
    var value = instance.Type;
    ```
- `public readonly object TypeGenericParameter`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 64)
  - Example:
    ```csharp
    var value = instance.TypeGenericParameter;
    ```
- `public readonly object ValueType`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 65)
  - Example:
    ```csharp
    var value = instance.ValueType;
    ```
- `public readonly object VerbatimString`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 66)
  - Example:
    ```csharp
    var value = instance.VerbatimString;
    ```
- `public readonly object XmlDocCommentAttributeName`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 67)
  - Example:
    ```csharp
    var value = instance.XmlDocCommentAttributeName;
    ```
- `public readonly object XmlDocCommentAttributeQuotes`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 68)
  - Example:
    ```csharp
    var value = instance.XmlDocCommentAttributeQuotes;
    ```
- `public readonly object XmlDocCommentAttributeValue`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 69)
  - Example:
    ```csharp
    var value = instance.XmlDocCommentAttributeValue;
    ```
- `public readonly object XmlDocCommentCDataSection`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 70)
  - Example:
    ```csharp
    var value = instance.XmlDocCommentCDataSection;
    ```
- `public readonly object XmlDocCommentComment`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 71)
  - Example:
    ```csharp
    var value = instance.XmlDocCommentComment;
    ```
- `public readonly object XmlDocCommentDelimiter`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 72)
  - Example:
    ```csharp
    var value = instance.XmlDocCommentDelimiter;
    ```
- `public readonly object XmlDocCommentEntityReference`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 73)
  - Example:
    ```csharp
    var value = instance.XmlDocCommentEntityReference;
    ```
- `public readonly object XmlDocCommentName`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 74)
  - Example:
    ```csharp
    var value = instance.XmlDocCommentName;
    ```
- `public readonly object XmlDocCommentProcessingInstruction`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 75)
  - Example:
    ```csharp
    var value = instance.XmlDocCommentProcessingInstruction;
    ```
- `public readonly object XmlDocCommentText`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 76)
  - Example:
    ```csharp
    var value = instance.XmlDocCommentText;
    ```
- `public readonly object XmlLiteralAttributeName`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 77)
  - Example:
    ```csharp
    var value = instance.XmlLiteralAttributeName;
    ```
- `public readonly object XmlLiteralAttributeQuotes`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 78)
  - Example:
    ```csharp
    var value = instance.XmlLiteralAttributeQuotes;
    ```
- `public readonly object XmlLiteralAttributeValue`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 79)
  - Example:
    ```csharp
    var value = instance.XmlLiteralAttributeValue;
    ```
- `public readonly object XmlLiteralCDataSection`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 80)
  - Example:
    ```csharp
    var value = instance.XmlLiteralCDataSection;
    ```
- `public readonly object XmlLiteralComment`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 81)
  - Example:
    ```csharp
    var value = instance.XmlLiteralComment;
    ```
- `public readonly object XmlLiteralDelimiter`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 82)
  - Example:
    ```csharp
    var value = instance.XmlLiteralDelimiter;
    ```
- `public readonly object XmlLiteralEmbeddedExpression`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 83)
  - Example:
    ```csharp
    var value = instance.XmlLiteralEmbeddedExpression;
    ```
- `public readonly object XmlLiteralEntityReference`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 84)
  - Example:
    ```csharp
    var value = instance.XmlLiteralEntityReference;
    ```
- `public readonly object XmlLiteralName`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 85)
  - Example:
    ```csharp
    var value = instance.XmlLiteralName;
    ```
- `public readonly object XmlLiteralProcessingInstruction`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 86)
  - Example:
    ```csharp
    var value = instance.XmlLiteralProcessingInstruction;
    ```
- `public readonly object XmlLiteralText`
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 87)
  - Example:
    ```csharp
    var value = instance.XmlLiteralText;
    ```
- `public static readonly RoslynClassificationTypes Default = new RoslynClassificationTypes()`
  - Summary: Gets the default instance
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassificationTypes.cs` (line 93)
  - Example:
    ```csharp
    var value = dnSpy.Roslyn.Text.Classification.RoslynClassificationTypes.Default;
    ```

## Struct `RoslynClassifier`

Roslyn classifier

**Example**

```csharp
var instance = new dnSpy.Roslyn.Text.Classification.RoslynClassifier(syntaxRoot: /* SyntaxNode */, semanticModel: /* SemanticModel */, workspace: /* Workspace */, roslynClassificationTypes: /* RoslynClassificationTypes */, defaultColor: /* object */, cancellationToken: /* CancellationToken */);
```

*Defined in* `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassifier.cs` (line 58)

### Constructors

- `public RoslynClassifier(SyntaxNode syntaxRoot, SemanticModel semanticModel, Workspace workspace, RoslynClassificationTypes roslynClassificationTypes, object defaultColor, CancellationToken cancellationToken)`
  - Summary: Constructor
  - Parameters:
    - `SyntaxNode syntaxRoot`: Syntax root
    - `SemanticModel semanticModel`: Semantic model
    - `Workspace workspace`: Workspace
    - `RoslynClassificationTypes roslynClassificationTypes`: Colors
    - `object defaultColor`: Default color if a token can't be classified or null to not use anything
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassifier.cs` (line 75)

### Methods

- `public IEnumerable<ClassifierResult> GetColors(TextSpan textSpan)`
  - Summary: Returns all colors
  - Parameters:
    - `TextSpan textSpan`: Span to classify
  - Defined in: `dnSpy/Roslyn/dnSpy.Roslyn/Text/Classification/RoslynClassifier.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColors(textSpan: /* TextSpan */);
    ```

