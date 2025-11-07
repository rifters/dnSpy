# Namespace `dnSpy.Contracts.Text.Classification`

## Class `EditorFormatMapConstants`

constants

**Example**

```csharp
// Access dnSpy.Contracts.Text.Classification.EditorFormatMapConstants members directly without instantiation.
dnSpy.Contracts.Text.Classification.EditorFormatMapConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/EditorFormatMapConstants.cs` (line 27)

### Fields

- `public const string PlainText = "Plain Text"`
  - Summary: Plain text font and color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/EditorFormatMapConstants.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.EditorFormatMapConstants.PlainText;
    ```
- `public const string TextViewBackgroundId = "TextView Background"`
  - Summary: background
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/EditorFormatMapConstants.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.EditorFormatMapConstants.TextViewBackgroundId;
    ```

## Interface `ITextClassifier`

Classifies text

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Classification.ITextClassifier and call its members.
var instance = new dnSpy.Contracts.Text.Classification.ITextClassifier(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ITextClassifier.cs` (line 26)

### Methods

- `IEnumerable<TextClassificationTag> GetTags(TextClassifierContext context)`
  - Summary: Classifies text
  - Parameters:
    - `TextClassifierContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ITextClassifier.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTags(context: /* TextClassifierContext */);
    ```

## Interface `ITextClassifierAggregator`

Text classifier aggregator, see

**Inherits/Implements:** `ITextClassifier`, `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Classification.ITextClassifierAggregator and call its members.
var instance = new dnSpy.Contracts.Text.Classification.ITextClassifierAggregator(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ITextClassifierAggregator.cs` (line 26)

## Interface `ITextClassifierAggregatorService`

Creates a that aggregates and normalizes all contributions.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Classification.ITextClassifierAggregatorService and call its members.
var instance = new dnSpy.Contracts.Text.Classification.ITextClassifierAggregatorService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ITextClassifierAggregatorService.cs` (line 27)

### Methods

- `ITextClassifierAggregator Create(IContentType contentType)`
  - Summary: Creates a
  - Parameters:
    - `IContentType contentType`: Content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ITextClassifierAggregatorService.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(contentType: /* IContentType */);
    ```

## Interface `ITextClassifierProvider`

Creates s. Export the instance with at least one .

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Classification.ITextClassifierProvider and call its members.
var instance = new dnSpy.Contracts.Text.Classification.ITextClassifierProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ITextClassifierProvider.cs` (line 27)

### Methods

- `ITextClassifier Create(IContentType contentType)`
  - Summary: Creates a or returns null
  - Parameters:
    - `IContentType contentType`: Content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ITextClassifierProvider.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(contentType: /* IContentType */);
    ```

## Interface `ITextElementProvider`

Creates WPF text elements

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Classification.ITextElementProvider and call its members.
var instance = new dnSpy.Contracts.Text.Classification.ITextElementProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ITextElementProvider.cs` (line 27)

### Methods

- `FrameworkElement CreateTextElement(IClassificationFormatMap classificationFormatMap, TextClassifierContext context, string contentType, TextElementFlags flags)`
  - Summary: Creates a WPF text element
  - Parameters:
    - `IClassificationFormatMap classificationFormatMap`: Classification format map
    - `TextClassifierContext context`: Text classifier context
    - `string contentType`: Content type
    - `TextElementFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ITextElementProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextElement(classificationFormatMap: /* IClassificationFormatMap */, context: /* TextClassifierContext */, contentType: /* string */, flags: /* TextElementFlags */);
    ```

## Interface `IThemeClassificationTypeService`

Returns theme s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Classification.IThemeClassificationTypeService and call its members.
var instance = new dnSpy.Contracts.Text.Classification.IThemeClassificationTypeService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/IThemeClassificationTypeService.cs` (line 26)

### Methods

- `IClassificationType GetClassificationType(TextColor color)`
  - Summary: Gets a classification type or a default classification type if is invalid
  - Parameters:
    - `TextColor color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/IThemeClassificationTypeService.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.GetClassificationType(color: /* TextColor */);
    ```

## Class `LanguagePriority`

Language priority

**Example**

```csharp
// Access dnSpy.Contracts.Text.Classification.LanguagePriority members directly without instantiation.
dnSpy.Contracts.Text.Classification.LanguagePriority./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/LanguagePriority.cs` (line 24)

### Fields

- `public const string FormalLanguage = "Formal Language Priority"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/LanguagePriority.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.LanguagePriority.FormalLanguage;
    ```
- `public const string NaturalLanguage = "Natural Language Priority"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/LanguagePriority.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.LanguagePriority.NaturalLanguage;
    ```

## Class `PredefinedClassificationTypeNames`

Predefined classification type names

**Example**

```csharp
// Access dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames members directly without instantiation.
dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 24)

### Fields

- `public const string Character = "character"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.Character;
    ```
- `public const string Comment = "comment"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.Comment;
    ```
- `public const string ExcludedCode = "excluded code"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.ExcludedCode;
    ```
- `public const string FormalLanguage = "formal language"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.FormalLanguage;
    ```
- `public const string Identifier = "identifier"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.Identifier;
    ```
- `public const string Keyword = "keyword"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.Keyword;
    ```
- `public const string Literal = "literal"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.Literal;
    ```
- `public const string NaturalLanguage = "natural language"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.NaturalLanguage;
    ```
- `public const string Number = "number"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.Number;
    ```
- `public const string Operator = "operator"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.Operator;
    ```
- `public const string Other = "other"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.Other;
    ```
- `public const string PreprocessorKeyword = "preprocessor keyword"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.PreprocessorKeyword;
    ```
- `public const string String = "string"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.String;
    ```
- `public const string WhiteSpace = "whitespace"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedClassificationTypeNames.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedClassificationTypeNames.WhiteSpace;
    ```

## Class `PredefinedTextClassifierTags`

Text classifier tags

**Example**

```csharp
// Access dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags members directly without instantiation.
dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 24)

### Fields

- `public static readonly string AttachToProcessWindowCommandLine = "CommandLine"`
  - Summary: Attach to Process window column: Command Line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 178)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.AttachToProcessWindowCommandLine;
    ```
- `public static readonly string AttachToProcessWindowFullPath = "Path"`
  - Summary: Attach to Process window column: Path
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 173)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.AttachToProcessWindowFullPath;
    ```
- `public static readonly string AttachToProcessWindowMachine = "Machine"`
  - Summary: Attach to Process window column: Machine
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 168)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.AttachToProcessWindowMachine;
    ```
- `public static readonly string AttachToProcessWindowPid = "PID"`
  - Summary: Attach to Process window column: PID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 153)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.AttachToProcessWindowPid;
    ```
- `public static readonly string AttachToProcessWindowProcess = "Process"`
  - Summary: Attach to Process window column: Process
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 148)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.AttachToProcessWindowProcess;
    ```
- `public static readonly string AttachToProcessWindowTitle = "Title"`
  - Summary: Attach to Process window column: Title
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 158)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.AttachToProcessWindowTitle;
    ```
- `public static readonly string AttachToProcessWindowType = "Type"`
  - Summary: Attach to Process window column: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 163)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.AttachToProcessWindowType;
    ```
- `public static readonly string AutosWindowName = "Name"`
  - Summary: Autos window column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 213)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.AutosWindowName;
    ```
- `public static readonly string AutosWindowType = "Type"`
  - Summary: Autos window column: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 223)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.AutosWindowType;
    ```
- `public static readonly string AutosWindowValue = "Value"`
  - Summary: Autos window column: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 218)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.AutosWindowValue;
    ```
- `public static readonly string BookmarksWindowLabels = "Labels"`
  - Summary: Bookmarks window column: Labels
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.BookmarksWindowLabels;
    ```
- `public static readonly string BookmarksWindowLocation = "Location"`
  - Summary: Bookmarks window column: Location
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 78)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.BookmarksWindowLocation;
    ```
- `public static readonly string BookmarksWindowModule = "Module"`
  - Summary: Bookmarks window column: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 83)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.BookmarksWindowModule;
    ```
- `public static readonly string BookmarksWindowName = "Name"`
  - Summary: Bookmarks window column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.BookmarksWindowName;
    ```
- `public static readonly string CallStackWindowName = "Name"`
  - Summary: Call Stack window column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 143)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.CallStackWindowName;
    ```
- `public static readonly string CodeBreakpointsWindowCondition = "Condition"`
  - Summary: Code breakpoints window column: Condition
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 98)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.CodeBreakpointsWindowCondition;
    ```
- `public static readonly string CodeBreakpointsWindowFilter = "Filter"`
  - Summary: Code breakpoints window column: Filter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 108)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.CodeBreakpointsWindowFilter;
    ```
- `public static readonly string CodeBreakpointsWindowHitCount = "HitCount"`
  - Summary: Code breakpoints window column: Hit Count
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 103)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.CodeBreakpointsWindowHitCount;
    ```
- `public static readonly string CodeBreakpointsWindowLabels = "Labels"`
  - Summary: Code breakpoints window column: Labels
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 93)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.CodeBreakpointsWindowLabels;
    ```
- `public static readonly string CodeBreakpointsWindowModule = "Module"`
  - Summary: Code breakpoints window column: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 118)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.CodeBreakpointsWindowModule;
    ```
- `public static readonly string CodeBreakpointsWindowName = "Name"`
  - Summary: Code breakpoints window column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.CodeBreakpointsWindowName;
    ```
- `public static readonly string CodeBreakpointsWindowWhenHit = "WhenHit"`
  - Summary: Code breakpoints window column: When Hit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 113)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.CodeBreakpointsWindowWhenHit;
    ```
- `public static readonly string DocListDialogCount = "DocumentCount"`
  - Summary: List dialog column: Count
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.DocListDialogCount;
    ```
- `public static readonly string DocListDialogName = "Name"`
  - Summary: List dialog column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.DocListDialogName;
    ```
- `public static readonly string ExceptionSettingsWindowCategory = "Category"`
  - Summary: Exception Settings window column: Category
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 188)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ExceptionSettingsWindowCategory;
    ```
- `public static readonly string ExceptionSettingsWindowConditions = "Conditions"`
  - Summary: Exception Settings window column: Conditions
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 193)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ExceptionSettingsWindowConditions;
    ```
- `public static readonly string ExceptionSettingsWindowName = "Name"`
  - Summary: Exception Settings window column: Break When Thrown
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 183)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ExceptionSettingsWindowName;
    ```
- `public static readonly string GacDialogName = "Name"`
  - Summary: GAC dialog column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.GacDialogName;
    ```
- `public static readonly string GacDialogVersion = "Version"`
  - Summary: GAC dialog column: Version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.GacDialogVersion;
    ```
- `public static readonly string LocalsWindowName = "Name"`
  - Summary: Locals window column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 198)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.LocalsWindowName;
    ```
- `public static readonly string LocalsWindowType = "Type"`
  - Summary: Locals window column: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 208)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.LocalsWindowType;
    ```
- `public static readonly string LocalsWindowValue = "Value"`
  - Summary: Locals window column: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 203)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.LocalsWindowValue;
    ```
- `public static readonly string MethodBodyEditor = nameof(MethodBodyEditor)`
  - Summary: Method body editor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.MethodBodyEditor;
    ```
- `public static readonly string ModuleBreakpointsWindowModuleAppDomainName = "AppDomainName"`
  - Summary: Module Breakpoints window column: AppDomain Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 133)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModuleBreakpointsWindowModuleAppDomainName;
    ```
- `public static readonly string ModuleBreakpointsWindowModuleName = "ModuleName"`
  - Summary: Module Breakpoints window column: Module Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 123)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModuleBreakpointsWindowModuleName;
    ```
- `public static readonly string ModuleBreakpointsWindowOrder = "Order"`
  - Summary: Module Breakpoints window column: Order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 128)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModuleBreakpointsWindowOrder;
    ```
- `public static readonly string ModuleBreakpointsWindowProcessName = "ProcessName"`
  - Summary: Module Breakpoints window column: Process Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 138)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModuleBreakpointsWindowProcessName;
    ```
- `public static readonly string ModulesWindowAddress = "Address"`
  - Summary: Modules window column: Address
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 283)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowAddress;
    ```
- `public static readonly string ModulesWindowAppDomain = "AppDomain"`
  - Summary: Modules window column: AppDomain
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 293)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowAppDomain;
    ```
- `public static readonly string ModulesWindowDynamic = "Dynamic"`
  - Summary: Modules window column: Dynamic
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 258)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowDynamic;
    ```
- `public static readonly string ModulesWindowInMemory = "InMemory"`
  - Summary: Modules window column: InMemory
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 263)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowInMemory;
    ```
- `public static readonly string ModulesWindowName = "Name"`
  - Summary: Modules window column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 243)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowName;
    ```
- `public static readonly string ModulesWindowOptimized = "Optimized"`
  - Summary: Modules window column: Optimized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 253)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowOptimized;
    ```
- `public static readonly string ModulesWindowOrder = "Order"`
  - Summary: Modules window column: Order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 268)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowOrder;
    ```
- `public static readonly string ModulesWindowPath = "Path"`
  - Summary: Modules window column: Path
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 248)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowPath;
    ```
- `public static readonly string ModulesWindowProcess = "Process"`
  - Summary: Modules window column: Process
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 288)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowProcess;
    ```
- `public static readonly string ModulesWindowTimestamp = "Timestamp"`
  - Summary: Modules window column: Timestamp
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 278)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowTimestamp;
    ```
- `public static readonly string ModulesWindowVersion = "Version"`
  - Summary: Modules window column: Version
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 273)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ModulesWindowVersion;
    ```
- `public static readonly string OptionsDialogText = "Text"`
  - Summary: Options dialog text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 388)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.OptionsDialogText;
    ```
- `public static readonly string ProcessesWindowArchitecture = "Architecture"`
  - Summary: Processes window column: Architecture
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 378)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ProcessesWindowArchitecture;
    ```
- `public static readonly string ProcessesWindowDebugging = "Debugging"`
  - Summary: Processes window column: Debugging
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 373)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ProcessesWindowDebugging;
    ```
- `public static readonly string ProcessesWindowId = "ID"`
  - Summary: Processes window column: ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 358)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ProcessesWindowId;
    ```
- `public static readonly string ProcessesWindowName = "Name"`
  - Summary: Processes window column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 353)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ProcessesWindowName;
    ```
- `public static readonly string ProcessesWindowPath = "Path"`
  - Summary: Processes window column: Path
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 383)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ProcessesWindowPath;
    ```
- `public static readonly string ProcessesWindowState = "State"`
  - Summary: Processes window column: State
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 368)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ProcessesWindowState;
    ```
- `public static readonly string ProcessesWindowTitle = "Title"`
  - Summary: Processes window column: Title
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 363)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ProcessesWindowTitle;
    ```
- `public static readonly string TabsDialogModule = "Module"`
  - Summary: Windows dialog column: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.TabsDialogModule;
    ```
- `public static readonly string TabsDialogName = "Name"`
  - Summary: Windows dialog column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.TabsDialogName;
    ```
- `public static readonly string TabsDialogPath = "Path"`
  - Summary: Windows dialog column: Path
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.TabsDialogPath;
    ```
- `public static readonly string ThreadsWindowAffinityMask = "AffinityMask"`
  - Summary: Threads window column: AffinityMask
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 328)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowAffinityMask;
    ```
- `public static readonly string ThreadsWindowAppDomain = "AppDomain"`
  - Summary: Threads window column: AppDomain
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 343)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowAppDomain;
    ```
- `public static readonly string ThreadsWindowCategoryText = "CategoryText"`
  - Summary: Threads window column: CategoryText
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 308)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowCategoryText;
    ```
- `public static readonly string ThreadsWindowId = "ID"`
  - Summary: Threads window column: Id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 298)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowId;
    ```
- `public static readonly string ThreadsWindowLocation = "Location"`
  - Summary: Threads window column: Location
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 318)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowLocation;
    ```
- `public static readonly string ThreadsWindowManagedId = "ManagedId"`
  - Summary: Threads window column: ManagedId
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 303)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowManagedId;
    ```
- `public static readonly string ThreadsWindowName = "Name"`
  - Summary: Threads window column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 313)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowName;
    ```
- `public static readonly string ThreadsWindowPriority = "Priority"`
  - Summary: Threads window column: Priority
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 323)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowPriority;
    ```
- `public static readonly string ThreadsWindowProcess = "ProcessName"`
  - Summary: Threads window column: Process Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 338)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowProcess;
    ```
- `public static readonly string ThreadsWindowSuspended = "SuspendedCount"`
  - Summary: Threads window column: Suspended Count
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 333)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowSuspended;
    ```
- `public static readonly string ThreadsWindowUserState = "State"`
  - Summary: Threads window column: State
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 348)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.ThreadsWindowUserState;
    ```
- `public static readonly string WatchWindowName = "Name"`
  - Summary: Watch window column: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 228)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.WatchWindowName;
    ```
- `public static readonly string WatchWindowType = "Type"`
  - Summary: Watch window column: Type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 238)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.WatchWindowType;
    ```
- `public static readonly string WatchWindowValue = "Value"`
  - Summary: Watch window column: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/PredefinedTextClassifierTags.cs` (line 233)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.PredefinedTextClassifierTags.WatchWindowValue;
    ```

## Class `RoslynClassificationTypeNames`

Roslyn classification type names

**Example**

```csharp
// Access dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames members directly without instantiation.
dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 24)

### Fields

- `public const string ClassName = "class name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.ClassName;
    ```
- `public const string DelegateName = "delegate name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 27)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.DelegateName;
    ```
- `public const string EnumName = "enum name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.EnumName;
    ```
- `public const string InterfaceName = "interface name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.InterfaceName;
    ```
- `public const string ModuleName = "module name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.ModuleName;
    ```
- `public const string NumericLiteral = PredefinedClassificationTypeNames.Number`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.NumericLiteral;
    ```
- `public const string PreprocessorText = "preprocessor text"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.PreprocessorText;
    ```
- `public const string Punctuation = "punctuation"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.Punctuation;
    ```
- `public const string StringLiteral = PredefinedClassificationTypeNames.String`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.StringLiteral;
    ```
- `public const string StructName = "struct name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.StructName;
    ```
- `public const string Text = "text"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.Text;
    ```
- `public const string TypeParameterName = "type parameter name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.TypeParameterName;
    ```
- `public const string VerbatimStringLiteral = "string - verbatim"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.VerbatimStringLiteral;
    ```
- `public const string XmlDocCommentAttributeName = "xml doc comment - attribute name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 39)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlDocCommentAttributeName;
    ```
- `public const string XmlDocCommentAttributeQuotes = "xml doc comment - attribute quotes"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlDocCommentAttributeQuotes;
    ```
- `public const string XmlDocCommentAttributeValue = "xml doc comment - attribute value"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlDocCommentAttributeValue;
    ```
- `public const string XmlDocCommentCDataSection = "xml doc comment - cdata section"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlDocCommentCDataSection;
    ```
- `public const string XmlDocCommentComment = "xml doc comment - comment"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlDocCommentComment;
    ```
- `public const string XmlDocCommentDelimiter = "xml doc comment - delimiter"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlDocCommentDelimiter;
    ```
- `public const string XmlDocCommentEntityReference = "xml doc comment - entity reference"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 45)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlDocCommentEntityReference;
    ```
- `public const string XmlDocCommentName = "xml doc comment - name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlDocCommentName;
    ```
- `public const string XmlDocCommentProcessingInstruction = "xml doc comment - processing instruction"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlDocCommentProcessingInstruction;
    ```
- `public const string XmlDocCommentText = "xml doc comment - text"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlDocCommentText;
    ```
- `public const string XmlLiteralAttributeName = "xml literal - attribute name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralAttributeName;
    ```
- `public const string XmlLiteralAttributeQuotes = "xml literal - attribute quotes"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralAttributeQuotes;
    ```
- `public const string XmlLiteralAttributeValue = "xml literal - attribute value"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 51)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralAttributeValue;
    ```
- `public const string XmlLiteralCDataSection = "xml literal - cdata section"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralCDataSection;
    ```
- `public const string XmlLiteralComment = "xml literal - comment"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralComment;
    ```
- `public const string XmlLiteralDelimiter = "xml literal - delimiter"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 54)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralDelimiter;
    ```
- `public const string XmlLiteralEmbeddedExpression = "xml literal - embedded expression"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralEmbeddedExpression;
    ```
- `public const string XmlLiteralEntityReference = "xml literal - entity reference"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralEntityReference;
    ```
- `public const string XmlLiteralName = "xml literal - name"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 57)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralName;
    ```
- `public const string XmlLiteralProcessingInstruction = "xml literal - processing instruction"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralProcessingInstruction;
    ```
- `public const string XmlLiteralText = "xml literal - text"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/RoslynClassificationTypeNames.cs` (line 59)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.RoslynClassificationTypeNames.XmlLiteralText;
    ```

## Class `TextClassificationTag`

Text classification tag

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Classification.TextClassificationTag(span: /* Span */, classificationType: /* IClassificationType */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassificationTag.cs` (line 28)

### Constructors

- `public TextClassificationTag(Span span, IClassificationType classificationType)`
  - Summary: Constructor
  - Parameters:
    - `Span span`: Span
    - `IClassificationType classificationType`: Classification type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassificationTag.cs` (line 44)

### Properties

- `public IClassificationType ClassificationType { get; }`
  - Summary: Gets the classification type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassificationTag.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ClassificationType;
    ```
- `public Span Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassificationTag.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Class `TextClassifierContext`

context

**Inherits/Implements:** `IPropertyOwner`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Classification.TextClassifierContext(text: /* string */, tag: /* string */, colorize: /* bool */, colors: /* IReadOnlyCollection<SpanData<object>> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierContext.cs` (line 29)

### Constructors

- `public TextClassifierContext(string text, string tag, bool colorize, IReadOnlyCollection<SpanData<object>> colors = null)`
  - Summary: Constructor
  - Parameters:
    - `string text`: Text to classify
    - `string tag`: Tag (), can be null
    - `bool colorize`: true if it should be colorized. Only special classifiers can ignore this, eg. highlighters
    - `IReadOnlyCollection<SpanData<object>> colors` (default: `null`): Default colors or null (see )
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierContext.cs` (line 69)

### Properties

- `public IReadOnlyCollection<SpanData<object>> Colors { get; }`
  - Summary: Default colors, can be empty and there could be non-classified parts
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierContext.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Colors;
    ```
- `public PropertyCollection Properties {
			get {
				if (properties == null)
					Interlocked.CompareExchange(ref properties, new PropertyCollection(), null);
				return properties;
			}
		}`
  - Summary: Gets the properties
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierContext.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Properties;
    ```
- `public bool Colorize { get; }`
  - Summary: true if it should be colorized. Only special classifiers can ignore this, eg. highlighters
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierContext.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Colorize;
    ```
- `public string Tag { get; }`
  - Summary: Tag, see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierContext.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```
- `public string Text { get; }`
  - Summary: Gets the text to classify
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierContext.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Class `TextClassifierTextColorWriter`

Implements and stores all colors and text. The result can be passed to

**Inherits/Implements:** `ITextColorWriter`

**Example**

```csharp
var instance = new dnSpy.Contracts.Text.Classification.TextClassifierTextColorWriter();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierTextColorWriter.cs` (line 29)

### Constructors

- `public TextClassifierTextColorWriter()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierTextColorWriter.cs` (line 51)

### Methods

- `public void Clear()`
  - Summary: Clears the text and colors so the instance can be reused
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierTextColorWriter.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```
- `public void Write(TextColor color, string text)`
  - Parameters:
    - `TextColor color`: Description not provided.
    - `string text`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierTextColorWriter.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(color: /* TextColor */, text: /* string */);
    ```
- `public void Write(object color, string text)`
  - Parameters:
    - `object color`: Description not provided.
    - `string text`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierTextColorWriter.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(color: /* object */, text: /* string */);
    ```

### Properties

- `public List<SpanData<object>> Colors => colors`
  - Summary: Gets the colors
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierTextColorWriter.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Colors;
    ```
- `public int Length => sb.Length`
  - Summary: Gets the text length
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierTextColorWriter.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public string Text => sb.ToString()`
  - Summary: Gets the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextClassifierTextColorWriter.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Enum `TextElementFlags`

Text element flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Classification.TextElementFlags and call its members.
var instance = new dnSpy.Contracts.Text.Classification.TextElementFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/TextElementFlags.cs` (line 27)

### Members

- `None`: No bit is set
- `FilterOutNewLines` = `x00000001`: Filter out newlines from the string by replacing them with spaces
- `NewFormatter` = `x00000002`: Use the new text formatter, it's faster but doesn't support word wrap or all unicode characters
- `WrapMask` = `x0000000C`: Mask to get word wrap enum
- `NoWrap` = `x00000000`
- `WrapWithOverflow` = `x00000004`
- `Wrap` = `x00000008`
- `TrimmingMask` = `x00000030`: Mask to get text trimming enum
- `NoTrimming` = `x00000000`
- `CharacterEllipsis` = `x00000010`
- `WordEllipsis` = `x00000020`

## Class `ThemeClassificationTypeNameKeys`

Classification type keys

**Example**

```csharp
// Access dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys members directly without instantiation.
dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 24)

### Fields

- `public const string ActiveBookmarkName = nameof(ActiveBookmarkName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1478)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ActiveBookmarkName;
    ```
- `public const string ActiveStatementMarker = nameof(ActiveStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 803)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ActiveStatementMarker;
    ```
- `public const string AdvancedBreakpointErrorStatement = nameof(AdvancedBreakpointErrorStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1338)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedBreakpointErrorStatement;
    ```
- `public const string AdvancedBreakpointErrorStatementMarker = nameof(AdvancedBreakpointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1343)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedBreakpointErrorStatementMarker;
    ```
- `public const string AdvancedBreakpointStatement = nameof(AdvancedBreakpointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1263)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedBreakpointStatement;
    ```
- `public const string AdvancedBreakpointStatementMarker = nameof(AdvancedBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1268)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedBreakpointStatementMarker;
    ```
- `public const string AdvancedBreakpointWarningStatement = nameof(AdvancedBreakpointWarningStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1323)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedBreakpointWarningStatement;
    ```
- `public const string AdvancedBreakpointWarningStatementMarker = nameof(AdvancedBreakpointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1328)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedBreakpointWarningStatementMarker;
    ```
- `public const string AdvancedTracepointErrorStatement = nameof(AdvancedTracepointErrorStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1458)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedTracepointErrorStatement;
    ```
- `public const string AdvancedTracepointErrorStatementMarker = nameof(AdvancedTracepointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1463)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedTracepointErrorStatementMarker;
    ```
- `public const string AdvancedTracepointStatement = nameof(AdvancedTracepointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1383)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedTracepointStatement;
    ```
- `public const string AdvancedTracepointStatementMarker = nameof(AdvancedTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1388)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedTracepointStatementMarker;
    ```
- `public const string AdvancedTracepointWarningStatement = nameof(AdvancedTracepointWarningStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1443)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedTracepointWarningStatement;
    ```
- `public const string AdvancedTracepointWarningStatementMarker = nameof(AdvancedTracepointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1448)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AdvancedTracepointWarningStatementMarker;
    ```
- `public const string AppSettingsTextMatchHighlight = nameof(AppSettingsTextMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1168)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AppSettingsTextMatchHighlight;
    ```
- `public const string AppSettingsTreeViewNodeMatchHighlight = nameof(AppSettingsTreeViewNodeMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1163)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AppSettingsTreeViewNodeMatchHighlight;
    ```
- `public const string AsmAddress = nameof(AsmAddress)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1613)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmAddress;
    ```
- `public const string AsmComment = nameof(AsmComment)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1538)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmComment;
    ```
- `public const string AsmData = nameof(AsmData)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1608)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmData;
    ```
- `public const string AsmDirective = nameof(AsmDirective)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1543)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmDirective;
    ```
- `public const string AsmFunction = nameof(AsmFunction)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1603)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmFunction;
    ```
- `public const string AsmFunctionAddress = nameof(AsmFunctionAddress)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1593)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmFunctionAddress;
    ```
- `public const string AsmHexBytes = nameof(AsmHexBytes)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1618)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmHexBytes;
    ```
- `public const string AsmKeyword = nameof(AsmKeyword)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1558)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmKeyword;
    ```
- `public const string AsmLabel = nameof(AsmLabel)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1598)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmLabel;
    ```
- `public const string AsmLabelAddress = nameof(AsmLabelAddress)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1588)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmLabelAddress;
    ```
- `public const string AsmMnemonic = nameof(AsmMnemonic)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1553)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmMnemonic;
    ```
- `public const string AsmNumber = nameof(AsmNumber)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1573)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmNumber;
    ```
- `public const string AsmOperator = nameof(AsmOperator)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1563)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmOperator;
    ```
- `public const string AsmPrefix = nameof(AsmPrefix)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1548)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmPrefix;
    ```
- `public const string AsmPunctuation = nameof(AsmPunctuation)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1568)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmPunctuation;
    ```
- `public const string AsmRegister = nameof(AsmRegister)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1578)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmRegister;
    ```
- `public const string AsmSelectorValue = nameof(AsmSelectorValue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1583)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AsmSelectorValue;
    ```
- `public const string Assembly = nameof(Assembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 463)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Assembly;
    ```
- `public const string AssemblyExe = nameof(AssemblyExe)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 468)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AssemblyExe;
    ```
- `public const string AssemblyModule = nameof(AssemblyModule)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 473)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.AssemblyModule;
    ```
- `public const string Black = nameof(Black)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 523)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Black;
    ```
- `public const string BlockStructureAccessor = nameof(BlockStructureAccessor)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 933)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureAccessor;
    ```
- `public const string BlockStructureAnonymousMethod = nameof(BlockStructureAnonymousMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 938)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureAnonymousMethod;
    ```
- `public const string BlockStructureCase = nameof(BlockStructureCase)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1023)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureCase;
    ```
- `public const string BlockStructureCatch = nameof(BlockStructureCatch)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 983)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureCatch;
    ```
- `public const string BlockStructureConditional = nameof(BlockStructureConditional)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 958)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureConditional;
    ```
- `public const string BlockStructureConstructor = nameof(BlockStructureConstructor)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 943)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureConstructor;
    ```
- `public const string BlockStructureDestructor = nameof(BlockStructureDestructor)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 948)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureDestructor;
    ```
- `public const string BlockStructureEvent = nameof(BlockStructureEvent)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 973)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureEvent;
    ```
- `public const string BlockStructureFault = nameof(BlockStructureFault)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 998)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureFault;
    ```
- `public const string BlockStructureFilter = nameof(BlockStructureFilter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 988)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureFilter;
    ```
- `public const string BlockStructureFinally = nameof(BlockStructureFinally)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 993)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureFinally;
    ```
- `public const string BlockStructureFixed = nameof(BlockStructureFixed)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1013)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureFixed;
    ```
- `public const string BlockStructureInterface = nameof(BlockStructureInterface)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 923)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureInterface;
    ```
- `public const string BlockStructureLocalFunction = nameof(BlockStructureLocalFunction)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1028)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureLocalFunction;
    ```
- `public const string BlockStructureLock = nameof(BlockStructureLock)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1003)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureLock;
    ```
- `public const string BlockStructureLoop = nameof(BlockStructureLoop)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 963)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureLoop;
    ```
- `public const string BlockStructureMethod = nameof(BlockStructureMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 928)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureMethod;
    ```
- `public const string BlockStructureModule = nameof(BlockStructureModule)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 913)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureModule;
    ```
- `public const string BlockStructureNamespace = nameof(BlockStructureNamespace)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 903)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureNamespace;
    ```
- `public const string BlockStructureOperator = nameof(BlockStructureOperator)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 953)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureOperator;
    ```
- `public const string BlockStructureOther = nameof(BlockStructureOther)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1033)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureOther;
    ```
- `public const string BlockStructureProperty = nameof(BlockStructureProperty)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 968)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureProperty;
    ```
- `public const string BlockStructureSwitch = nameof(BlockStructureSwitch)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1018)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureSwitch;
    ```
- `public const string BlockStructureTry = nameof(BlockStructureTry)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 978)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureTry;
    ```
- `public const string BlockStructureType = nameof(BlockStructureType)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 908)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureType;
    ```
- `public const string BlockStructureUsing = nameof(BlockStructureUsing)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1008)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureUsing;
    ```
- `public const string BlockStructureValueType = nameof(BlockStructureValueType)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 918)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureValueType;
    ```
- `public const string BlockStructureXaml = nameof(BlockStructureXaml)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1043)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureXaml;
    ```
- `public const string BlockStructureXml = nameof(BlockStructureXml)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1038)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BlockStructureXml;
    ```
- `public const string Blue = nameof(Blue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 528)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Blue;
    ```
- `public const string BookmarkName = nameof(BookmarkName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1473)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BookmarkName;
    ```
- `public const string BraceMatching = "brace matching"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 888)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BraceMatching;
    ```
- `public const string BreakpointErrorStatement = nameof(BreakpointErrorStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1308)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BreakpointErrorStatement;
    ```
- `public const string BreakpointErrorStatementMarker = nameof(BreakpointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1313)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BreakpointErrorStatementMarker;
    ```
- `public const string BreakpointStatement = nameof(BreakpointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 808)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BreakpointStatement;
    ```
- `public const string BreakpointStatementMarker = nameof(BreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 813)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BreakpointStatementMarker;
    ```
- `public const string BreakpointWarningStatement = nameof(BreakpointWarningStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1293)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BreakpointWarningStatement;
    ```
- `public const string BreakpointWarningStatementMarker = nameof(BreakpointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1298)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.BreakpointWarningStatementMarker;
    ```
- `public const string CallReturn = nameof(CallReturn)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 793)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.CallReturn;
    ```
- `public const string CallReturnMarker = nameof(CallReturnMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 798)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.CallReturnMarker;
    ```
- `public const string Char = PredefinedClassificationTypeNames.Character`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 78)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Char;
    ```
- `public const string Comment = nameof(Comment)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Comment;
    ```
- `public const string CompletionMatchHighlight = nameof(CompletionMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1048)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.CompletionMatchHighlight;
    ```
- `public const string CompletionSuffix = nameof(CompletionSuffix)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1053)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.CompletionSuffix;
    ```
- `public const string CurrentLine = nameof(CurrentLine)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 828)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.CurrentLine;
    ```
- `public const string CurrentLineNoFocus = nameof(CurrentLineNoFocus)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 833)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.CurrentLineNoFocus;
    ```
- `public const string CurrentStatement = nameof(CurrentStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 783)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.CurrentStatement;
    ```
- `public const string CurrentStatementMarker = nameof(CurrentStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 788)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.CurrentStatementMarker;
    ```
- `public const string Cyan = nameof(Cyan)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 533)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Cyan;
    ```
- `public const string DarkBlue = nameof(DarkBlue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 538)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DarkBlue;
    ```
- `public const string DarkCyan = nameof(DarkCyan)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 543)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DarkCyan;
    ```
- `public const string DarkGray = nameof(DarkGray)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 548)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DarkGray;
    ```
- `public const string DarkGreen = nameof(DarkGreen)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 553)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DarkGreen;
    ```
- `public const string DarkMagenta = nameof(DarkMagenta)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 558)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DarkMagenta;
    ```
- `public const string DarkRed = nameof(DarkRed)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 563)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DarkRed;
    ```
- `public const string DarkYellow = nameof(DarkYellow)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 568)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DarkYellow;
    ```
- `public const string DebugExceptionName = nameof(DebugExceptionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1498)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugExceptionName;
    ```
- `public const string DebugLogExceptionHandled = nameof(DebugLogExceptionHandled)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 683)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogExceptionHandled;
    ```
- `public const string DebugLogExceptionUnhandled = nameof(DebugLogExceptionUnhandled)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 688)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogExceptionUnhandled;
    ```
- `public const string DebugLogExitProcess = nameof(DebugLogExitProcess)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 708)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogExitProcess;
    ```
- `public const string DebugLogExitThread = nameof(DebugLogExitThread)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 713)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogExitThread;
    ```
- `public const string DebugLogExtensionMessage = nameof(DebugLogExtensionMessage)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1488)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogExtensionMessage;
    ```
- `public const string DebugLogLoadModule = nameof(DebugLogLoadModule)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 698)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogLoadModule;
    ```
- `public const string DebugLogMDA = nameof(DebugLogMDA)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 723)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogMDA;
    ```
- `public const string DebugLogProgramOutput = nameof(DebugLogProgramOutput)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 718)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogProgramOutput;
    ```
- `public const string DebugLogStepFiltering = nameof(DebugLogStepFiltering)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 693)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogStepFiltering;
    ```
- `public const string DebugLogTimestamp = nameof(DebugLogTimestamp)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 728)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogTimestamp;
    ```
- `public const string DebugLogTrace = nameof(DebugLogTrace)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1483)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogTrace;
    ```
- `public const string DebugLogUnloadModule = nameof(DebugLogUnloadModule)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 703)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugLogUnloadModule;
    ```
- `public const string DebugObjectIdName = nameof(DebugObjectIdName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1518)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugObjectIdName;
    ```
- `public const string DebugReturnValueName = nameof(DebugReturnValueName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1508)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugReturnValueName;
    ```
- `public const string DebugStowedExceptionName = nameof(DebugStowedExceptionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1503)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugStowedExceptionName;
    ```
- `public const string DebugVariableName = nameof(DebugVariableName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1513)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugVariableName;
    ```
- `public const string DebugViewPropertyName = nameof(DebugViewPropertyName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1533)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebugViewPropertyName;
    ```
- `public const string DebuggerDisplayAttributeEval = nameof(DebuggerDisplayAttributeEval)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1523)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebuggerDisplayAttributeEval;
    ```
- `public const string DebuggerNoStringQuotesEval = nameof(DebuggerNoStringQuotesEval)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1528)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebuggerNoStringQuotesEval;
    ```
- `public const string DebuggerValueChangedHighlight = nameof(DebuggerValueChangedHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1493)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DebuggerValueChangedHighlight;
    ```
- `public const string Delegate = RoslynClassificationTypeNames.DelegateName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 103)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Delegate;
    ```
- `public const string DirectoryPart = nameof(DirectoryPart)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 478)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DirectoryPart;
    ```
- `public const string DisabledAdvancedBreakpointStatement = nameof(DisabledAdvancedBreakpointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1278)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DisabledAdvancedBreakpointStatement;
    ```
- `public const string DisabledAdvancedBreakpointStatementMarker = nameof(DisabledAdvancedBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1283)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DisabledAdvancedBreakpointStatementMarker;
    ```
- `public const string DisabledAdvancedTracepointStatement = nameof(DisabledAdvancedTracepointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1398)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DisabledAdvancedTracepointStatement;
    ```
- `public const string DisabledAdvancedTracepointStatementMarker = nameof(DisabledAdvancedTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1403)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DisabledAdvancedTracepointStatementMarker;
    ```
- `public const string DisabledBreakpointStatementMarker = nameof(DisabledBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 823)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DisabledBreakpointStatementMarker;
    ```
- `public const string DisabledTracepointStatement = nameof(DisabledTracepointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1368)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DisabledTracepointStatement;
    ```
- `public const string DisabledTracepointStatementMarker = nameof(DisabledTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1373)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DisabledTracepointStatementMarker;
    ```
- `public const string DocumentListMatchHighlight = nameof(DocumentListMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1153)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.DocumentListMatchHighlight;
    ```
- `public const string Enum = RoslynClassificationTypeNames.EnumName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 108)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Enum;
    ```
- `public const string EnumField = nameof(EnumField)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 158)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.EnumField;
    ```
- `public const string Error = nameof(Error)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 493)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Error;
    ```
- `public const string ExcludedCode = "Excluded Code"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 233)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ExcludedCode;
    ```
- `public const string ExtensionMethod = nameof(ExtensionMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 148)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ExtensionMethod;
    ```
- `public const string FileExtension = nameof(FileExtension)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 488)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.FileExtension;
    ```
- `public const string FileNameNoExtension = nameof(FileNameNoExtension)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 483)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.FileNameNoExtension;
    ```
- `public const string FindMatchHighlightMarker = nameof(FindMatchHighlightMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 898)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.FindMatchHighlightMarker;
    ```
- `public const string GacMatchHighlight = nameof(GacMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1158)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.GacMatchHighlight;
    ```
- `public const string GlyphMargin = "Indicator Margin"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 883)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.GlyphMargin;
    ```
- `public const string Gray = nameof(Gray)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 573)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Gray;
    ```
- `public const string Green = nameof(Green)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 578)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Green;
    ```
- `public const string HexAscii = nameof(HexAscii)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 863)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexAscii;
    ```
- `public const string HexByte0 = nameof(HexByte0)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 848)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexByte0;
    ```
- `public const string HexByte1 = nameof(HexByte1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 853)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexByte1;
    ```
- `public const string HexByteError = nameof(HexByteError)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 858)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexByteError;
    ```
- `public const string HexCaret = nameof(HexCaret)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 868)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexCaret;
    ```
- `public const string HexColumnLine0 = nameof(HexColumnLine0)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1188)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexColumnLine0;
    ```
- `public const string HexColumnLine1 = nameof(HexColumnLine1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1193)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexColumnLine1;
    ```
- `public const string HexColumnLineGroup0 = nameof(HexColumnLineGroup0)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1198)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexColumnLineGroup0;
    ```
- `public const string HexColumnLineGroup1 = nameof(HexColumnLineGroup1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1203)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexColumnLineGroup1;
    ```
- `public const string HexCor20Header = nameof(HexCor20Header)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1113)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexCor20Header;
    ```
- `public const string HexCurrentAsciiCell = nameof(HexCurrentAsciiCell)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1228)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexCurrentAsciiCell;
    ```
- `public const string HexCurrentLine = nameof(HexCurrentLine)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1173)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexCurrentLine;
    ```
- `public const string HexCurrentLineNoFocus = nameof(HexCurrentLineNoFocus)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1178)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexCurrentLineNoFocus;
    ```
- `public const string HexCurrentValueCell = nameof(HexCurrentValueCell)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1223)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexCurrentValueCell;
    ```
- `public const string HexFindMatchHighlightMarker = nameof(HexFindMatchHighlightMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1238)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexFindMatchHighlightMarker;
    ```
- `public const string HexGlyphMargin = nameof(HexGlyphMargin)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1218)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexGlyphMargin;
    ```
- `public const string HexHighlightedAsciiColumn = nameof(HexHighlightedAsciiColumn)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1213)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexHighlightedAsciiColumn;
    ```
- `public const string HexHighlightedValuesColumn = nameof(HexHighlightedValuesColumn)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1208)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexHighlightedValuesColumn;
    ```
- `public const string HexInactiveCaret = nameof(HexInactiveCaret)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 873)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexInactiveCaret;
    ```
- `public const string HexInactiveSelectedText = nameof(HexInactiveSelectedText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1183)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexInactiveSelectedText;
    ```
- `public const string HexOffset = nameof(HexOffset)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 843)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexOffset;
    ```
- `public const string HexPeDosHeader = nameof(HexPeDosHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1083)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexPeDosHeader;
    ```
- `public const string HexPeFileHeader = nameof(HexPeFileHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1088)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexPeFileHeader;
    ```
- `public const string HexPeOptionalHeader32 = nameof(HexPeOptionalHeader32)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1093)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexPeOptionalHeader32;
    ```
- `public const string HexPeOptionalHeader64 = nameof(HexPeOptionalHeader64)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1098)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexPeOptionalHeader64;
    ```
- `public const string HexPeSection = nameof(HexPeSection)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1103)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexPeSection;
    ```
- `public const string HexPeSectionName = nameof(HexPeSectionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1108)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexPeSectionName;
    ```
- `public const string HexSelection = nameof(HexSelection)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 878)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexSelection;
    ```
- `public const string HexStorageHeader = nameof(HexStorageHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1123)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexStorageHeader;
    ```
- `public const string HexStorageSignature = nameof(HexStorageSignature)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1118)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexStorageSignature;
    ```
- `public const string HexStorageStream = nameof(HexStorageStream)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1128)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexStorageStream;
    ```
- `public const string HexStorageStreamName = nameof(HexStorageStreamName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1133)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexStorageStreamName;
    ```
- `public const string HexStorageStreamNameInvalid = nameof(HexStorageStreamNameInvalid)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1138)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexStorageStreamNameInvalid;
    ```
- `public const string HexTableName = nameof(HexTableName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1148)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexTableName;
    ```
- `public const string HexTablesStream = nameof(HexTablesStream)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1143)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexTablesStream;
    ```
- `public const string HexText = nameof(HexText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 838)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexText;
    ```
- `public const string HexToolTipServiceCurrentField = nameof(HexToolTipServiceCurrentField)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1253)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexToolTipServiceCurrentField;
    ```
- `public const string HexToolTipServiceField0 = nameof(HexToolTipServiceField0)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1243)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexToolTipServiceField0;
    ```
- `public const string HexToolTipServiceField1 = nameof(HexToolTipServiceField1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1248)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HexToolTipServiceField1;
    ```
- `public const string HighlightedDefinition = "MarkerFormatDefinition/HighlightedDefinition"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 778)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HighlightedDefinition;
    ```
- `public const string HighlightedReference = "MarkerFormatDefinition/HighlightedReference"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 768)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HighlightedReference;
    ```
- `public const string HighlightedWrittenReference = "MarkerFormatDefinition/HighlightedWrittenReference"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 773)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.HighlightedWrittenReference;
    ```
- `public const string ILDirective = nameof(ILDirective)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 223)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ILDirective;
    ```
- `public const string ILModule = nameof(ILModule)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 228)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ILModule;
    ```
- `public const string Identifier = nameof(Identifier)`
  - Summary: Identifier
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Identifier;
    ```
- `public const string InactiveSelectedText = "Inactive Selected Text"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 763)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InactiveSelectedText;
    ```
- `public const string InstanceEvent = nameof(InstanceEvent)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 173)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InstanceEvent;
    ```
- `public const string InstanceField = nameof(InstanceField)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 153)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InstanceField;
    ```
- `public const string InstanceMethod = nameof(InstanceMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 138)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InstanceMethod;
    ```
- `public const string InstanceProperty = nameof(InstanceProperty)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 183)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InstanceProperty;
    ```
- `public const string Interface = RoslynClassificationTypeNames.InterfaceName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 113)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Interface;
    ```
- `public const string InvBlack = nameof(InvBlack)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 603)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvBlack;
    ```
- `public const string InvBlue = nameof(InvBlue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 608)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvBlue;
    ```
- `public const string InvCyan = nameof(InvCyan)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 613)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvCyan;
    ```
- `public const string InvDarkBlue = nameof(InvDarkBlue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 618)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvDarkBlue;
    ```
- `public const string InvDarkCyan = nameof(InvDarkCyan)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 623)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvDarkCyan;
    ```
- `public const string InvDarkGray = nameof(InvDarkGray)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 628)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvDarkGray;
    ```
- `public const string InvDarkGreen = nameof(InvDarkGreen)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 633)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvDarkGreen;
    ```
- `public const string InvDarkMagenta = nameof(InvDarkMagenta)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 638)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvDarkMagenta;
    ```
- `public const string InvDarkRed = nameof(InvDarkRed)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 643)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvDarkRed;
    ```
- `public const string InvDarkYellow = nameof(InvDarkYellow)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 648)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvDarkYellow;
    ```
- `public const string InvGray = nameof(InvGray)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 653)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvGray;
    ```
- `public const string InvGreen = nameof(InvGreen)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 658)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvGreen;
    ```
- `public const string InvMagenta = nameof(InvMagenta)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 663)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvMagenta;
    ```
- `public const string InvRed = nameof(InvRed)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 668)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvRed;
    ```
- `public const string InvWhite = nameof(InvWhite)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 673)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvWhite;
    ```
- `public const string InvYellow = nameof(InvYellow)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 678)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.InvYellow;
    ```
- `public const string Keyword = nameof(Keyword)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Keyword;
    ```
- `public const string Label = nameof(Label)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 213)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Label;
    ```
- `public const string LineNumber = "Line Number"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 733)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.LineNumber;
    ```
- `public const string LineSeparator = nameof(LineSeparator)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 893)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.LineSeparator;
    ```
- `public const string ListFindMatchHighlight = nameof(ListFindMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1258)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ListFindMatchHighlight;
    ```
- `public const string Literal = nameof(Literal)`
  - Summary: Literal
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Literal;
    ```
- `public const string LiteralField = nameof(LiteralField)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 163)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.LiteralField;
    ```
- `public const string Local = nameof(Local)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 193)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Local;
    ```
- `public const string Magenta = nameof(Magenta)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 583)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Magenta;
    ```
- `public const string MethodGenericParameter = nameof(MethodGenericParameter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 133)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.MethodGenericParameter;
    ```
- `public const string Module = RoslynClassificationTypeNames.ModuleName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 123)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Module;
    ```
- `public const string Namespace = nameof(Namespace)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 83)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Namespace;
    ```
- `public const string Number = nameof(Number)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Number;
    ```
- `public const string OpCode = nameof(OpCode)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 218)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.OpCode;
    ```
- `public const string Operator = nameof(Operator)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Operator;
    ```
- `public const string OutputWindowText = nameof(OutputWindowText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1233)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.OutputWindowText;
    ```
- `public const string Parameter = nameof(Parameter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 198)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Parameter;
    ```
- `public const string PreprocessorKeyword = "Preprocessor Keyword"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 203)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.PreprocessorKeyword;
    ```
- `public const string PreprocessorText = RoslynClassificationTypeNames.PreprocessorText`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 208)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.PreprocessorText;
    ```
- `public const string Punctuation = RoslynClassificationTypeNames.Punctuation`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Punctuation;
    ```
- `public const string Red = nameof(Red)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 588)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Red;
    ```
- `public const string ReplLineNumberInput1 = nameof(ReplLineNumberInput1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 738)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ReplLineNumberInput1;
    ```
- `public const string ReplLineNumberInput2 = nameof(ReplLineNumberInput2)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 743)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ReplLineNumberInput2;
    ```
- `public const string ReplLineNumberOutput = nameof(ReplLineNumberOutput)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 748)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ReplLineNumberOutput;
    ```
- `public const string ReplOutputText = nameof(ReplOutputText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 513)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ReplOutputText;
    ```
- `public const string ReplPrompt1 = nameof(ReplPrompt1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 503)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ReplPrompt1;
    ```
- `public const string ReplPrompt2 = nameof(ReplPrompt2)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 508)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ReplPrompt2;
    ```
- `public const string ReplScriptOutputText = nameof(ReplScriptOutputText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 518)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ReplScriptOutputText;
    ```
- `public const string SealedType = nameof(SealedType)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 93)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SealedType;
    ```
- `public const string SelectedAdvancedBreakpointErrorStatementMarker = nameof(SelectedAdvancedBreakpointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1348)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedAdvancedBreakpointErrorStatementMarker;
    ```
- `public const string SelectedAdvancedBreakpointStatementMarker = nameof(SelectedAdvancedBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1273)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedAdvancedBreakpointStatementMarker;
    ```
- `public const string SelectedAdvancedBreakpointWarningStatementMarker = nameof(SelectedAdvancedBreakpointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1333)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedAdvancedBreakpointWarningStatementMarker;
    ```
- `public const string SelectedAdvancedTracepointErrorStatementMarker = nameof(SelectedAdvancedTracepointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1468)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedAdvancedTracepointErrorStatementMarker;
    ```
- `public const string SelectedAdvancedTracepointStatementMarker = nameof(SelectedAdvancedTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1393)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedAdvancedTracepointStatementMarker;
    ```
- `public const string SelectedAdvancedTracepointWarningStatementMarker = nameof(SelectedAdvancedTracepointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1453)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedAdvancedTracepointWarningStatementMarker;
    ```
- `public const string SelectedBreakpointErrorStatementMarker = nameof(SelectedBreakpointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1318)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedBreakpointErrorStatementMarker;
    ```
- `public const string SelectedBreakpointStatementMarker = nameof(SelectedBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 818)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedBreakpointStatementMarker;
    ```
- `public const string SelectedBreakpointWarningStatementMarker = nameof(SelectedBreakpointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1303)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedBreakpointWarningStatementMarker;
    ```
- `public const string SelectedDisabledAdvancedBreakpointStatementMarker = nameof(SelectedDisabledAdvancedBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1288)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedDisabledAdvancedBreakpointStatementMarker;
    ```
- `public const string SelectedDisabledAdvancedTracepointStatementMarker = nameof(SelectedDisabledAdvancedTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1408)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedDisabledAdvancedTracepointStatementMarker;
    ```
- `public const string SelectedDisabledTracepointStatementMarker = nameof(SelectedDisabledTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1378)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedDisabledTracepointStatementMarker;
    ```
- `public const string SelectedText = "Selected Text"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 758)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedText;
    ```
- `public const string SelectedTracepointErrorStatementMarker = nameof(SelectedTracepointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1438)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedTracepointErrorStatementMarker;
    ```
- `public const string SelectedTracepointStatementMarker = nameof(SelectedTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1363)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedTracepointStatementMarker;
    ```
- `public const string SelectedTracepointWarningStatementMarker = nameof(SelectedTracepointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1423)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SelectedTracepointWarningStatementMarker;
    ```
- `public const string SignatureHelpCurrentParameter = "CurrentParameterFormat"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1063)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SignatureHelpCurrentParameter;
    ```
- `public const string SignatureHelpDocumentation = "SigHelpDocumentationFormat"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1058)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SignatureHelpDocumentation;
    ```
- `public const string SignatureHelpParameter = nameof(SignatureHelpParameter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1068)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SignatureHelpParameter;
    ```
- `public const string SignatureHelpParameterDocumentation = nameof(SignatureHelpParameterDocumentation)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1073)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.SignatureHelpParameterDocumentation;
    ```
- `public const string StaticEvent = nameof(StaticEvent)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 178)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.StaticEvent;
    ```
- `public const string StaticField = nameof(StaticField)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 168)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.StaticField;
    ```
- `public const string StaticMethod = nameof(StaticMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 143)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.StaticMethod;
    ```
- `public const string StaticProperty = nameof(StaticProperty)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 188)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.StaticProperty;
    ```
- `public const string StaticType = nameof(StaticType)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 98)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.StaticType;
    ```
- `public const string String = nameof(String)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.String;
    ```
- `public const string Text = RoslynClassificationTypeNames.Text`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Text;
    ```
- `public const string ToStringEval = nameof(ToStringEval)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 498)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ToStringEval;
    ```
- `public const string TracepointErrorStatement = nameof(TracepointErrorStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1428)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.TracepointErrorStatement;
    ```
- `public const string TracepointErrorStatementMarker = nameof(TracepointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1433)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.TracepointErrorStatementMarker;
    ```
- `public const string TracepointStatement = nameof(TracepointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1353)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.TracepointStatement;
    ```
- `public const string TracepointStatementMarker = nameof(TracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1358)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.TracepointStatementMarker;
    ```
- `public const string TracepointWarningStatement = nameof(TracepointWarningStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1413)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.TracepointWarningStatement;
    ```
- `public const string TracepointWarningStatementMarker = nameof(TracepointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1418)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.TracepointWarningStatementMarker;
    ```
- `public const string Type = RoslynClassificationTypeNames.ClassName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Type;
    ```
- `public const string TypeGenericParameter = RoslynClassificationTypeNames.TypeParameterName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 128)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.TypeGenericParameter;
    ```
- `public const string Url = "urlformat"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 1078)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Url;
    ```
- `public const string ValueType = RoslynClassificationTypeNames.StructName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 118)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.ValueType;
    ```
- `public const string VerbatimString = RoslynClassificationTypeNames.VerbatimStringLiteral`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.VerbatimString;
    ```
- `public const string VisibleWhitespace = nameof(VisibleWhitespace)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 753)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.VisibleWhitespace;
    ```
- `public const string White = nameof(White)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 593)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.White;
    ```
- `public const string XamlAttribute = nameof(XamlAttribute)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 393)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlAttribute;
    ```
- `public const string XamlAttributeQuotes = nameof(XamlAttributeQuotes)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 398)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlAttributeQuotes;
    ```
- `public const string XamlAttributeValue = nameof(XamlAttributeValue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 403)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlAttributeValue;
    ```
- `public const string XamlCDataSection = nameof(XamlCDataSection)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 408)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlCDataSection;
    ```
- `public const string XamlComment = nameof(XamlComment)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 413)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlComment;
    ```
- `public const string XamlDelimiter = nameof(XamlDelimiter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 418)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlDelimiter;
    ```
- `public const string XamlKeyword = nameof(XamlKeyword)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 423)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlKeyword;
    ```
- `public const string XamlMarkupExtensionClass = nameof(XamlMarkupExtensionClass)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 428)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlMarkupExtensionClass;
    ```
- `public const string XamlMarkupExtensionParameterName = nameof(XamlMarkupExtensionParameterName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 433)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlMarkupExtensionParameterName;
    ```
- `public const string XamlMarkupExtensionParameterValue = nameof(XamlMarkupExtensionParameterValue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 438)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlMarkupExtensionParameterValue;
    ```
- `public const string XamlName = nameof(XamlName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 443)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlName;
    ```
- `public const string XamlProcessingInstruction = nameof(XamlProcessingInstruction)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 448)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlProcessingInstruction;
    ```
- `public const string XamlText = nameof(XamlText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 453)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XamlText;
    ```
- `public const string XmlAttribute = nameof(XmlAttribute)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 343)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlAttribute;
    ```
- `public const string XmlAttributeQuotes = nameof(XmlAttributeQuotes)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 348)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlAttributeQuotes;
    ```
- `public const string XmlAttributeValue = nameof(XmlAttributeValue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 353)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlAttributeValue;
    ```
- `public const string XmlCDataSection = nameof(XmlCDataSection)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 358)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlCDataSection;
    ```
- `public const string XmlComment = nameof(XmlComment)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 363)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlComment;
    ```
- `public const string XmlDelimiter = nameof(XmlDelimiter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 368)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDelimiter;
    ```
- `public const string XmlDocCommentAttributeName = RoslynClassificationTypeNames.XmlDocCommentAttributeName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 238)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocCommentAttributeName;
    ```
- `public const string XmlDocCommentAttributeQuotes = RoslynClassificationTypeNames.XmlDocCommentAttributeQuotes`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 243)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocCommentAttributeQuotes;
    ```
- `public const string XmlDocCommentAttributeValue = RoslynClassificationTypeNames.XmlDocCommentAttributeValue`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 248)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocCommentAttributeValue;
    ```
- `public const string XmlDocCommentCDataSection = RoslynClassificationTypeNames.XmlDocCommentCDataSection`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 253)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocCommentCDataSection;
    ```
- `public const string XmlDocCommentComment = RoslynClassificationTypeNames.XmlDocCommentComment`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 258)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocCommentComment;
    ```
- `public const string XmlDocCommentDelimiter = RoslynClassificationTypeNames.XmlDocCommentDelimiter`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 263)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocCommentDelimiter;
    ```
- `public const string XmlDocCommentEntityReference = RoslynClassificationTypeNames.XmlDocCommentEntityReference`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 268)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocCommentEntityReference;
    ```
- `public const string XmlDocCommentName = RoslynClassificationTypeNames.XmlDocCommentName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 273)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocCommentName;
    ```
- `public const string XmlDocCommentProcessingInstruction = RoslynClassificationTypeNames.XmlDocCommentProcessingInstruction`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 278)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocCommentProcessingInstruction;
    ```
- `public const string XmlDocCommentText = RoslynClassificationTypeNames.XmlDocCommentText`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 283)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocCommentText;
    ```
- `public const string XmlDocToolTipHeader = nameof(XmlDocToolTipHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 458)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlDocToolTipHeader;
    ```
- `public const string XmlKeyword = nameof(XmlKeyword)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 373)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlKeyword;
    ```
- `public const string XmlLiteralAttributeName = RoslynClassificationTypeNames.XmlLiteralAttributeName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 288)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralAttributeName;
    ```
- `public const string XmlLiteralAttributeQuotes = RoslynClassificationTypeNames.XmlLiteralAttributeQuotes`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 293)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralAttributeQuotes;
    ```
- `public const string XmlLiteralAttributeValue = RoslynClassificationTypeNames.XmlLiteralAttributeValue`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 298)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralAttributeValue;
    ```
- `public const string XmlLiteralCDataSection = RoslynClassificationTypeNames.XmlLiteralCDataSection`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 303)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralCDataSection;
    ```
- `public const string XmlLiteralComment = RoslynClassificationTypeNames.XmlLiteralComment`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 308)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralComment;
    ```
- `public const string XmlLiteralDelimiter = RoslynClassificationTypeNames.XmlLiteralDelimiter`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 313)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralDelimiter;
    ```
- `public const string XmlLiteralEmbeddedExpression = RoslynClassificationTypeNames.XmlLiteralEmbeddedExpression`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 318)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralEmbeddedExpression;
    ```
- `public const string XmlLiteralEntityReference = RoslynClassificationTypeNames.XmlLiteralEntityReference`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 323)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralEntityReference;
    ```
- `public const string XmlLiteralName = RoslynClassificationTypeNames.XmlLiteralName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 328)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralName;
    ```
- `public const string XmlLiteralProcessingInstruction = RoslynClassificationTypeNames.XmlLiteralProcessingInstruction`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 333)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralProcessingInstruction;
    ```
- `public const string XmlLiteralText = RoslynClassificationTypeNames.XmlLiteralText`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 338)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlLiteralText;
    ```
- `public const string XmlName = nameof(XmlName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 378)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlName;
    ```
- `public const string XmlProcessingInstruction = nameof(XmlProcessingInstruction)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 383)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlProcessingInstruction;
    ```
- `public const string XmlText = nameof(XmlText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 388)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.XmlText;
    ```
- `public const string Yellow = nameof(Yellow)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNameKeys.cs` (line 598)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNameKeys.Yellow;
    ```

## Class `ThemeClassificationTypeNames`

Classification type names

**Example**

```csharp
// Access dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames members directly without instantiation.
dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 24)

### Fields

- `public const string ActiveBookmarkName = "Theme-" + nameof(ActiveBookmarkName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1478)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ActiveBookmarkName;
    ```
- `public const string ActiveStatementMarker = "Theme-" + nameof(ActiveStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 803)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ActiveStatementMarker;
    ```
- `public const string AdvancedBreakpointErrorStatement = "Theme-" + nameof(AdvancedBreakpointErrorStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1338)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedBreakpointErrorStatement;
    ```
- `public const string AdvancedBreakpointErrorStatementMarker = "Theme-" + nameof(AdvancedBreakpointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1343)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedBreakpointErrorStatementMarker;
    ```
- `public const string AdvancedBreakpointStatement = "Theme-" + nameof(AdvancedBreakpointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1263)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedBreakpointStatement;
    ```
- `public const string AdvancedBreakpointStatementMarker = "Theme-" + nameof(AdvancedBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1268)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedBreakpointStatementMarker;
    ```
- `public const string AdvancedBreakpointWarningStatement = "Theme-" + nameof(AdvancedBreakpointWarningStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1323)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedBreakpointWarningStatement;
    ```
- `public const string AdvancedBreakpointWarningStatementMarker = "Theme-" + nameof(AdvancedBreakpointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1328)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedBreakpointWarningStatementMarker;
    ```
- `public const string AdvancedTracepointErrorStatement = "Theme-" + nameof(AdvancedTracepointErrorStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1458)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedTracepointErrorStatement;
    ```
- `public const string AdvancedTracepointErrorStatementMarker = "Theme-" + nameof(AdvancedTracepointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1463)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedTracepointErrorStatementMarker;
    ```
- `public const string AdvancedTracepointStatement = "Theme-" + nameof(AdvancedTracepointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1383)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedTracepointStatement;
    ```
- `public const string AdvancedTracepointStatementMarker = "Theme-" + nameof(AdvancedTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1388)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedTracepointStatementMarker;
    ```
- `public const string AdvancedTracepointWarningStatement = "Theme-" + nameof(AdvancedTracepointWarningStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1443)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedTracepointWarningStatement;
    ```
- `public const string AdvancedTracepointWarningStatementMarker = "Theme-" + nameof(AdvancedTracepointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1448)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AdvancedTracepointWarningStatementMarker;
    ```
- `public const string AppSettingsTextMatchHighlight = "Theme-" + nameof(AppSettingsTextMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1168)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AppSettingsTextMatchHighlight;
    ```
- `public const string AppSettingsTreeViewNodeMatchHighlight = "Theme-" + nameof(AppSettingsTreeViewNodeMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1163)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AppSettingsTreeViewNodeMatchHighlight;
    ```
- `public const string AsmAddress = "Theme-" + nameof(AsmAddress)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1613)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmAddress;
    ```
- `public const string AsmComment = "Theme-" + nameof(AsmComment)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1538)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmComment;
    ```
- `public const string AsmData = "Theme-" + nameof(AsmData)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1608)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmData;
    ```
- `public const string AsmDirective = "Theme-" + nameof(AsmDirective)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1543)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmDirective;
    ```
- `public const string AsmFunction = "Theme-" + nameof(AsmFunction)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1603)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmFunction;
    ```
- `public const string AsmFunctionAddress = "Theme-" + nameof(AsmFunctionAddress)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1593)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmFunctionAddress;
    ```
- `public const string AsmHexBytes = "Theme-" + nameof(AsmHexBytes)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1618)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmHexBytes;
    ```
- `public const string AsmKeyword = "Theme-" + nameof(AsmKeyword)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1558)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmKeyword;
    ```
- `public const string AsmLabel = "Theme-" + nameof(AsmLabel)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1598)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmLabel;
    ```
- `public const string AsmLabelAddress = "Theme-" + nameof(AsmLabelAddress)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1588)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmLabelAddress;
    ```
- `public const string AsmMnemonic = "Theme-" + nameof(AsmMnemonic)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1553)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmMnemonic;
    ```
- `public const string AsmNumber = "Theme-" + nameof(AsmNumber)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1573)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmNumber;
    ```
- `public const string AsmOperator = "Theme-" + nameof(AsmOperator)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1563)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmOperator;
    ```
- `public const string AsmPrefix = "Theme-" + nameof(AsmPrefix)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1548)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmPrefix;
    ```
- `public const string AsmPunctuation = "Theme-" + nameof(AsmPunctuation)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1568)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmPunctuation;
    ```
- `public const string AsmRegister = "Theme-" + nameof(AsmRegister)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1578)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmRegister;
    ```
- `public const string AsmSelectorValue = "Theme-" + nameof(AsmSelectorValue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1583)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AsmSelectorValue;
    ```
- `public const string Assembly = "Theme-" + nameof(Assembly)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 463)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Assembly;
    ```
- `public const string AssemblyExe = "Theme-" + nameof(AssemblyExe)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 468)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AssemblyExe;
    ```
- `public const string AssemblyModule = "Theme-" + nameof(AssemblyModule)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 473)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.AssemblyModule;
    ```
- `public const string Black = "Theme-" + nameof(Black)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 523)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Black;
    ```
- `public const string BlockStructureAccessor = "Theme-" + nameof(BlockStructureAccessor)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 933)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureAccessor;
    ```
- `public const string BlockStructureAnonymousMethod = "Theme-" + nameof(BlockStructureAnonymousMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 938)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureAnonymousMethod;
    ```
- `public const string BlockStructureCase = "Theme-" + nameof(BlockStructureCase)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1023)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureCase;
    ```
- `public const string BlockStructureCatch = "Theme-" + nameof(BlockStructureCatch)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 983)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureCatch;
    ```
- `public const string BlockStructureConditional = "Theme-" + nameof(BlockStructureConditional)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 958)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureConditional;
    ```
- `public const string BlockStructureConstructor = "Theme-" + nameof(BlockStructureConstructor)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 943)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureConstructor;
    ```
- `public const string BlockStructureDestructor = "Theme-" + nameof(BlockStructureDestructor)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 948)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureDestructor;
    ```
- `public const string BlockStructureEvent = "Theme-" + nameof(BlockStructureEvent)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 973)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureEvent;
    ```
- `public const string BlockStructureFault = "Theme-" + nameof(BlockStructureFault)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 998)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureFault;
    ```
- `public const string BlockStructureFilter = "Theme-" + nameof(BlockStructureFilter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 988)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureFilter;
    ```
- `public const string BlockStructureFinally = "Theme-" + nameof(BlockStructureFinally)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 993)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureFinally;
    ```
- `public const string BlockStructureFixed = "Theme-" + nameof(BlockStructureFixed)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1013)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureFixed;
    ```
- `public const string BlockStructureInterface = "Theme-" + nameof(BlockStructureInterface)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 923)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureInterface;
    ```
- `public const string BlockStructureLocalFunction = "Theme-" + nameof(BlockStructureLocalFunction)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1028)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureLocalFunction;
    ```
- `public const string BlockStructureLock = "Theme-" + nameof(BlockStructureLock)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1003)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureLock;
    ```
- `public const string BlockStructureLoop = "Theme-" + nameof(BlockStructureLoop)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 963)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureLoop;
    ```
- `public const string BlockStructureMethod = "Theme-" + nameof(BlockStructureMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 928)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureMethod;
    ```
- `public const string BlockStructureModule = "Theme-" + nameof(BlockStructureModule)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 913)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureModule;
    ```
- `public const string BlockStructureNamespace = "Theme-" + nameof(BlockStructureNamespace)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 903)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureNamespace;
    ```
- `public const string BlockStructureOperator = "Theme-" + nameof(BlockStructureOperator)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 953)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureOperator;
    ```
- `public const string BlockStructureOther = "Theme-" + nameof(BlockStructureOther)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1033)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureOther;
    ```
- `public const string BlockStructureProperty = "Theme-" + nameof(BlockStructureProperty)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 968)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureProperty;
    ```
- `public const string BlockStructureSwitch = "Theme-" + nameof(BlockStructureSwitch)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1018)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureSwitch;
    ```
- `public const string BlockStructureTry = "Theme-" + nameof(BlockStructureTry)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 978)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureTry;
    ```
- `public const string BlockStructureType = "Theme-" + nameof(BlockStructureType)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 908)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureType;
    ```
- `public const string BlockStructureUsing = "Theme-" + nameof(BlockStructureUsing)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1008)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureUsing;
    ```
- `public const string BlockStructureValueType = "Theme-" + nameof(BlockStructureValueType)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 918)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureValueType;
    ```
- `public const string BlockStructureXaml = "Theme-" + nameof(BlockStructureXaml)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1043)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureXaml;
    ```
- `public const string BlockStructureXml = "Theme-" + nameof(BlockStructureXml)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1038)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BlockStructureXml;
    ```
- `public const string Blue = "Theme-" + nameof(Blue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 528)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Blue;
    ```
- `public const string BookmarkName = "Theme-" + nameof(BookmarkName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1473)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BookmarkName;
    ```
- `public const string BraceMatching = "brace matching"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 888)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BraceMatching;
    ```
- `public const string BreakpointErrorStatement = "Theme-" + nameof(BreakpointErrorStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1308)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BreakpointErrorStatement;
    ```
- `public const string BreakpointErrorStatementMarker = "Theme-" + nameof(BreakpointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1313)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BreakpointErrorStatementMarker;
    ```
- `public const string BreakpointStatement = "Theme-" + nameof(BreakpointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 808)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BreakpointStatement;
    ```
- `public const string BreakpointStatementMarker = "Theme-" + nameof(BreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 813)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BreakpointStatementMarker;
    ```
- `public const string BreakpointWarningStatement = "Theme-" + nameof(BreakpointWarningStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1293)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BreakpointWarningStatement;
    ```
- `public const string BreakpointWarningStatementMarker = "Theme-" + nameof(BreakpointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1298)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.BreakpointWarningStatementMarker;
    ```
- `public const string CallReturn = "Theme-" + nameof(CallReturn)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 793)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.CallReturn;
    ```
- `public const string CallReturnMarker = "Theme-" + nameof(CallReturnMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 798)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.CallReturnMarker;
    ```
- `public const string Char = PredefinedClassificationTypeNames.Character`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 78)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Char;
    ```
- `public const string Comment = PredefinedClassificationTypeNames.Comment`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Comment;
    ```
- `public const string CompletionMatchHighlight = "Theme-" + nameof(CompletionMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1048)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.CompletionMatchHighlight;
    ```
- `public const string CompletionSuffix = "Theme-" + nameof(CompletionSuffix)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1053)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.CompletionSuffix;
    ```
- `public const string CurrentLine = "Theme-" + nameof(CurrentLine)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 828)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.CurrentLine;
    ```
- `public const string CurrentLineNoFocus = "Theme-" + nameof(CurrentLineNoFocus)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 833)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.CurrentLineNoFocus;
    ```
- `public const string CurrentStatement = "Theme-" + nameof(CurrentStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 783)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.CurrentStatement;
    ```
- `public const string CurrentStatementMarker = "Theme-" + nameof(CurrentStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 788)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.CurrentStatementMarker;
    ```
- `public const string Cyan = "Theme-" + nameof(Cyan)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 533)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Cyan;
    ```
- `public const string DarkBlue = "Theme-" + nameof(DarkBlue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 538)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DarkBlue;
    ```
- `public const string DarkCyan = "Theme-" + nameof(DarkCyan)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 543)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DarkCyan;
    ```
- `public const string DarkGray = "Theme-" + nameof(DarkGray)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 548)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DarkGray;
    ```
- `public const string DarkGreen = "Theme-" + nameof(DarkGreen)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 553)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DarkGreen;
    ```
- `public const string DarkMagenta = "Theme-" + nameof(DarkMagenta)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 558)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DarkMagenta;
    ```
- `public const string DarkRed = "Theme-" + nameof(DarkRed)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 563)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DarkRed;
    ```
- `public const string DarkYellow = "Theme-" + nameof(DarkYellow)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 568)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DarkYellow;
    ```
- `public const string DebugExceptionName = "Theme-" + nameof(DebugExceptionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1498)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugExceptionName;
    ```
- `public const string DebugLogExceptionHandled = "Theme-" + nameof(DebugLogExceptionHandled)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 683)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogExceptionHandled;
    ```
- `public const string DebugLogExceptionUnhandled = "Theme-" + nameof(DebugLogExceptionUnhandled)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 688)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogExceptionUnhandled;
    ```
- `public const string DebugLogExitProcess = "Theme-" + nameof(DebugLogExitProcess)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 708)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogExitProcess;
    ```
- `public const string DebugLogExitThread = "Theme-" + nameof(DebugLogExitThread)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 713)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogExitThread;
    ```
- `public const string DebugLogExtensionMessage = "Theme-" + nameof(DebugLogExtensionMessage)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1488)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogExtensionMessage;
    ```
- `public const string DebugLogLoadModule = "Theme-" + nameof(DebugLogLoadModule)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 698)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogLoadModule;
    ```
- `public const string DebugLogMDA = "Theme-" + nameof(DebugLogMDA)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 723)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogMDA;
    ```
- `public const string DebugLogProgramOutput = "Theme-" + nameof(DebugLogProgramOutput)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 718)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogProgramOutput;
    ```
- `public const string DebugLogStepFiltering = "Theme-" + nameof(DebugLogStepFiltering)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 693)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogStepFiltering;
    ```
- `public const string DebugLogTimestamp = "Theme-" + nameof(DebugLogTimestamp)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 728)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogTimestamp;
    ```
- `public const string DebugLogTrace = "Theme-" + nameof(DebugLogTrace)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1483)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogTrace;
    ```
- `public const string DebugLogUnloadModule = "Theme-" + nameof(DebugLogUnloadModule)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 703)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugLogUnloadModule;
    ```
- `public const string DebugObjectIdName = "Theme-" + nameof(DebugObjectIdName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1518)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugObjectIdName;
    ```
- `public const string DebugReturnValueName = "Theme-" + nameof(DebugReturnValueName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1508)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugReturnValueName;
    ```
- `public const string DebugStowedExceptionName = "Theme-" + nameof(DebugStowedExceptionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1503)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugStowedExceptionName;
    ```
- `public const string DebugVariableName = "Theme-" + nameof(DebugVariableName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1513)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugVariableName;
    ```
- `public const string DebugViewPropertyName = "Theme-" + nameof(DebugViewPropertyName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1533)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebugViewPropertyName;
    ```
- `public const string DebuggerDisplayAttributeEval = "Theme-" + nameof(DebuggerDisplayAttributeEval)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1523)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebuggerDisplayAttributeEval;
    ```
- `public const string DebuggerNoStringQuotesEval = "Theme-" + nameof(DebuggerNoStringQuotesEval)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1528)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebuggerNoStringQuotesEval;
    ```
- `public const string DebuggerValueChangedHighlight = "Theme-" + nameof(DebuggerValueChangedHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1493)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DebuggerValueChangedHighlight;
    ```
- `public const string Delegate = RoslynClassificationTypeNames.DelegateName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 103)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Delegate;
    ```
- `public const string DirectoryPart = "Theme-" + nameof(DirectoryPart)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 478)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DirectoryPart;
    ```
- `public const string DisabledAdvancedBreakpointStatement = "Theme-" + nameof(DisabledAdvancedBreakpointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1278)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DisabledAdvancedBreakpointStatement;
    ```
- `public const string DisabledAdvancedBreakpointStatementMarker = "Theme-" + nameof(DisabledAdvancedBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1283)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DisabledAdvancedBreakpointStatementMarker;
    ```
- `public const string DisabledAdvancedTracepointStatement = "Theme-" + nameof(DisabledAdvancedTracepointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1398)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DisabledAdvancedTracepointStatement;
    ```
- `public const string DisabledAdvancedTracepointStatementMarker = "Theme-" + nameof(DisabledAdvancedTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1403)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DisabledAdvancedTracepointStatementMarker;
    ```
- `public const string DisabledBreakpointStatementMarker = "Theme-" + nameof(DisabledBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 823)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DisabledBreakpointStatementMarker;
    ```
- `public const string DisabledTracepointStatement = "Theme-" + nameof(DisabledTracepointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1368)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DisabledTracepointStatement;
    ```
- `public const string DisabledTracepointStatementMarker = "Theme-" + nameof(DisabledTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1373)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DisabledTracepointStatementMarker;
    ```
- `public const string DocumentListMatchHighlight = "Theme-" + nameof(DocumentListMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1153)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.DocumentListMatchHighlight;
    ```
- `public const string Enum = RoslynClassificationTypeNames.EnumName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 108)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Enum;
    ```
- `public const string EnumField = "Theme-" + nameof(EnumField)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 158)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.EnumField;
    ```
- `public const string Error = "Theme-" + nameof(Error)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 493)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Error;
    ```
- `public const string ExcludedCode = PredefinedClassificationTypeNames.ExcludedCode`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 233)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ExcludedCode;
    ```
- `public const string ExtensionMethod = "Theme-" + nameof(ExtensionMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 148)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ExtensionMethod;
    ```
- `public const string FileExtension = "Theme-" + nameof(FileExtension)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 488)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.FileExtension;
    ```
- `public const string FileNameNoExtension = "Theme-" + nameof(FileNameNoExtension)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 483)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.FileNameNoExtension;
    ```
- `public const string FindMatchHighlightMarker = "Theme-" + nameof(FindMatchHighlightMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 898)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.FindMatchHighlightMarker;
    ```
- `public const string GacMatchHighlight = "Theme-" + nameof(GacMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1158)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.GacMatchHighlight;
    ```
- `public const string GlyphMargin = "Theme-" + nameof(GlyphMargin)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 883)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.GlyphMargin;
    ```
- `public const string Gray = "Theme-" + nameof(Gray)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 573)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Gray;
    ```
- `public const string Green = "Theme-" + nameof(Green)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 578)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Green;
    ```
- `public const string HexAscii = "Theme-" + nameof(HexAscii)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 863)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexAscii;
    ```
- `public const string HexByte0 = "Theme-" + nameof(HexByte0)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 848)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexByte0;
    ```
- `public const string HexByte1 = "Theme-" + nameof(HexByte1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 853)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexByte1;
    ```
- `public const string HexByteError = "Theme-" + nameof(HexByteError)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 858)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexByteError;
    ```
- `public const string HexCaret = "Theme-" + nameof(HexCaret)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 868)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexCaret;
    ```
- `public const string HexColumnLine0 = "Theme-" + nameof(HexColumnLine0)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1188)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexColumnLine0;
    ```
- `public const string HexColumnLine1 = "Theme-" + nameof(HexColumnLine1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1193)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexColumnLine1;
    ```
- `public const string HexColumnLineGroup0 = "Theme-" + nameof(HexColumnLineGroup0)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1198)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexColumnLineGroup0;
    ```
- `public const string HexColumnLineGroup1 = "Theme-" + nameof(HexColumnLineGroup1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1203)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexColumnLineGroup1;
    ```
- `public const string HexCor20Header = "Theme-" + nameof(HexCor20Header)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1113)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexCor20Header;
    ```
- `public const string HexCurrentAsciiCell = "Theme-" + nameof(HexCurrentAsciiCell)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1228)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexCurrentAsciiCell;
    ```
- `public const string HexCurrentLine = "Theme-" + nameof(HexCurrentLine)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1173)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexCurrentLine;
    ```
- `public const string HexCurrentLineNoFocus = "Theme-" + nameof(HexCurrentLineNoFocus)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1178)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexCurrentLineNoFocus;
    ```
- `public const string HexCurrentValueCell = "Theme-" + nameof(HexCurrentValueCell)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1223)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexCurrentValueCell;
    ```
- `public const string HexFindMatchHighlightMarker = "Theme-" + nameof(HexFindMatchHighlightMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1238)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexFindMatchHighlightMarker;
    ```
- `public const string HexGlyphMargin = "Theme-" + nameof(HexGlyphMargin)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1218)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexGlyphMargin;
    ```
- `public const string HexHighlightedAsciiColumn = "Theme-" + nameof(HexHighlightedAsciiColumn)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1213)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexHighlightedAsciiColumn;
    ```
- `public const string HexHighlightedValuesColumn = "Theme-" + nameof(HexHighlightedValuesColumn)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1208)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexHighlightedValuesColumn;
    ```
- `public const string HexInactiveCaret = "Theme-" + nameof(HexInactiveCaret)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 873)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexInactiveCaret;
    ```
- `public const string HexInactiveSelectedText = "Theme-" + nameof(HexInactiveSelectedText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1183)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexInactiveSelectedText;
    ```
- `public const string HexOffset = "Theme-" + nameof(HexOffset)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 843)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexOffset;
    ```
- `public const string HexPeDosHeader = "Theme-" + nameof(HexPeDosHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1083)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexPeDosHeader;
    ```
- `public const string HexPeFileHeader = "Theme-" + nameof(HexPeFileHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1088)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexPeFileHeader;
    ```
- `public const string HexPeOptionalHeader32 = "Theme-" + nameof(HexPeOptionalHeader32)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1093)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexPeOptionalHeader32;
    ```
- `public const string HexPeOptionalHeader64 = "Theme-" + nameof(HexPeOptionalHeader64)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1098)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexPeOptionalHeader64;
    ```
- `public const string HexPeSection = "Theme-" + nameof(HexPeSection)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1103)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexPeSection;
    ```
- `public const string HexPeSectionName = "Theme-" + nameof(HexPeSectionName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1108)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexPeSectionName;
    ```
- `public const string HexSelection = "Theme-" + nameof(HexSelection)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 878)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexSelection;
    ```
- `public const string HexStorageHeader = "Theme-" + nameof(HexStorageHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1123)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexStorageHeader;
    ```
- `public const string HexStorageSignature = "Theme-" + nameof(HexStorageSignature)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1118)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexStorageSignature;
    ```
- `public const string HexStorageStream = "Theme-" + nameof(HexStorageStream)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1128)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexStorageStream;
    ```
- `public const string HexStorageStreamName = "Theme-" + nameof(HexStorageStreamName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1133)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexStorageStreamName;
    ```
- `public const string HexStorageStreamNameInvalid = "Theme-" + nameof(HexStorageStreamNameInvalid)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1138)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexStorageStreamNameInvalid;
    ```
- `public const string HexTableName = "Theme-" + nameof(HexTableName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1148)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexTableName;
    ```
- `public const string HexTablesStream = "Theme-" + nameof(HexTablesStream)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1143)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexTablesStream;
    ```
- `public const string HexText = "Theme-" + nameof(HexText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 838)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexText;
    ```
- `public const string HexToolTipServiceCurrentField = "Theme-" + nameof(HexToolTipServiceCurrentField)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1253)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexToolTipServiceCurrentField;
    ```
- `public const string HexToolTipServiceField0 = "Theme-" + nameof(HexToolTipServiceField0)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1243)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexToolTipServiceField0;
    ```
- `public const string HexToolTipServiceField1 = "Theme-" + nameof(HexToolTipServiceField1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1248)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HexToolTipServiceField1;
    ```
- `public const string HighlightedDefinition = "Theme-" + nameof(HighlightedDefinition)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 778)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HighlightedDefinition;
    ```
- `public const string HighlightedReference = "Theme-" + nameof(HighlightedReference)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 768)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HighlightedReference;
    ```
- `public const string HighlightedWrittenReference = "Theme-" + nameof(HighlightedWrittenReference)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 773)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.HighlightedWrittenReference;
    ```
- `public const string ILDirective = "Theme-" + nameof(ILDirective)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 223)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ILDirective;
    ```
- `public const string ILModule = "Theme-" + nameof(ILModule)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 228)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ILModule;
    ```
- `public const string Identifier = "identifier"`
  - Summary: Identifier
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Identifier;
    ```
- `public const string InactiveSelectedText = "Theme-" + nameof(InactiveSelectedText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 763)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InactiveSelectedText;
    ```
- `public const string InstanceEvent = "Theme-" + nameof(InstanceEvent)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 173)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InstanceEvent;
    ```
- `public const string InstanceField = "Theme-" + nameof(InstanceField)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 153)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InstanceField;
    ```
- `public const string InstanceMethod = "Theme-" + nameof(InstanceMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 138)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InstanceMethod;
    ```
- `public const string InstanceProperty = "Theme-" + nameof(InstanceProperty)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 183)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InstanceProperty;
    ```
- `public const string Interface = RoslynClassificationTypeNames.InterfaceName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 113)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Interface;
    ```
- `public const string InvBlack = "Theme-" + nameof(InvBlack)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 603)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvBlack;
    ```
- `public const string InvBlue = "Theme-" + nameof(InvBlue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 608)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvBlue;
    ```
- `public const string InvCyan = "Theme-" + nameof(InvCyan)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 613)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvCyan;
    ```
- `public const string InvDarkBlue = "Theme-" + nameof(InvDarkBlue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 618)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvDarkBlue;
    ```
- `public const string InvDarkCyan = "Theme-" + nameof(InvDarkCyan)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 623)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvDarkCyan;
    ```
- `public const string InvDarkGray = "Theme-" + nameof(InvDarkGray)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 628)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvDarkGray;
    ```
- `public const string InvDarkGreen = "Theme-" + nameof(InvDarkGreen)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 633)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvDarkGreen;
    ```
- `public const string InvDarkMagenta = "Theme-" + nameof(InvDarkMagenta)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 638)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvDarkMagenta;
    ```
- `public const string InvDarkRed = "Theme-" + nameof(InvDarkRed)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 643)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvDarkRed;
    ```
- `public const string InvDarkYellow = "Theme-" + nameof(InvDarkYellow)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 648)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvDarkYellow;
    ```
- `public const string InvGray = "Theme-" + nameof(InvGray)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 653)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvGray;
    ```
- `public const string InvGreen = "Theme-" + nameof(InvGreen)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 658)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvGreen;
    ```
- `public const string InvMagenta = "Theme-" + nameof(InvMagenta)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 663)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvMagenta;
    ```
- `public const string InvRed = "Theme-" + nameof(InvRed)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 668)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvRed;
    ```
- `public const string InvWhite = "Theme-" + nameof(InvWhite)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 673)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvWhite;
    ```
- `public const string InvYellow = "Theme-" + nameof(InvYellow)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 678)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.InvYellow;
    ```
- `public const string Keyword = PredefinedClassificationTypeNames.Keyword`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Keyword;
    ```
- `public const string Label = "Theme-" + nameof(Label)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 213)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Label;
    ```
- `public const string LineNumber = "line number"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 733)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.LineNumber;
    ```
- `public const string LineSeparator = "Theme-" + nameof(LineSeparator)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 893)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.LineSeparator;
    ```
- `public const string ListFindMatchHighlight = "Theme-" + nameof(ListFindMatchHighlight)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1258)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ListFindMatchHighlight;
    ```
- `public const string Literal = "literal"`
  - Summary: Literal
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Literal;
    ```
- `public const string LiteralField = "Theme-" + nameof(LiteralField)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 163)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.LiteralField;
    ```
- `public const string Local = "Theme-" + nameof(Local)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 193)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Local;
    ```
- `public const string Magenta = "Theme-" + nameof(Magenta)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 583)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Magenta;
    ```
- `public const string MethodGenericParameter = "Theme-" + nameof(MethodGenericParameter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 133)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.MethodGenericParameter;
    ```
- `public const string Module = RoslynClassificationTypeNames.ModuleName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 123)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Module;
    ```
- `public const string Namespace = "Theme-" + nameof(Namespace)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 83)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Namespace;
    ```
- `public const string Number = PredefinedClassificationTypeNames.Number`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Number;
    ```
- `public const string OpCode = "Theme-" + nameof(OpCode)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 218)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.OpCode;
    ```
- `public const string Operator = PredefinedClassificationTypeNames.Operator`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Operator;
    ```
- `public const string OutputWindowText = "Theme-" + nameof(OutputWindowText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1233)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.OutputWindowText;
    ```
- `public const string Parameter = "Theme-" + nameof(Parameter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 198)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Parameter;
    ```
- `public const string PreprocessorKeyword = PredefinedClassificationTypeNames.PreprocessorKeyword`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 203)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.PreprocessorKeyword;
    ```
- `public const string PreprocessorText = RoslynClassificationTypeNames.PreprocessorText`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 208)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.PreprocessorText;
    ```
- `public const string Punctuation = RoslynClassificationTypeNames.Punctuation`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Punctuation;
    ```
- `public const string Red = "Theme-" + nameof(Red)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 588)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Red;
    ```
- `public const string ReplLineNumberInput1 = "Theme-" + nameof(ReplLineNumberInput1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 738)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ReplLineNumberInput1;
    ```
- `public const string ReplLineNumberInput2 = "Theme-" + nameof(ReplLineNumberInput2)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 743)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ReplLineNumberInput2;
    ```
- `public const string ReplLineNumberOutput = "Theme-" + nameof(ReplLineNumberOutput)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 748)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ReplLineNumberOutput;
    ```
- `public const string ReplOutputText = "Theme-" + nameof(ReplOutputText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 513)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ReplOutputText;
    ```
- `public const string ReplPrompt1 = "Theme-" + nameof(ReplPrompt1)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 503)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ReplPrompt1;
    ```
- `public const string ReplPrompt2 = "Theme-" + nameof(ReplPrompt2)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 508)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ReplPrompt2;
    ```
- `public const string ReplScriptOutputText = "Theme-" + nameof(ReplScriptOutputText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 518)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ReplScriptOutputText;
    ```
- `public const string SealedType = "Theme-" + nameof(SealedType)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 93)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SealedType;
    ```
- `public const string SelectedAdvancedBreakpointErrorStatementMarker = "Theme-" + nameof(SelectedAdvancedBreakpointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1348)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedAdvancedBreakpointErrorStatementMarker;
    ```
- `public const string SelectedAdvancedBreakpointStatementMarker = "Theme-" + nameof(SelectedAdvancedBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1273)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedAdvancedBreakpointStatementMarker;
    ```
- `public const string SelectedAdvancedBreakpointWarningStatementMarker = "Theme-" + nameof(SelectedAdvancedBreakpointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1333)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedAdvancedBreakpointWarningStatementMarker;
    ```
- `public const string SelectedAdvancedTracepointErrorStatementMarker = "Theme-" + nameof(SelectedAdvancedTracepointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1468)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedAdvancedTracepointErrorStatementMarker;
    ```
- `public const string SelectedAdvancedTracepointStatementMarker = "Theme-" + nameof(SelectedAdvancedTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1393)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedAdvancedTracepointStatementMarker;
    ```
- `public const string SelectedAdvancedTracepointWarningStatementMarker = "Theme-" + nameof(SelectedAdvancedTracepointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1453)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedAdvancedTracepointWarningStatementMarker;
    ```
- `public const string SelectedBreakpointErrorStatementMarker = "Theme-" + nameof(SelectedBreakpointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1318)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedBreakpointErrorStatementMarker;
    ```
- `public const string SelectedBreakpointStatementMarker = "Theme-" + nameof(SelectedBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 818)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedBreakpointStatementMarker;
    ```
- `public const string SelectedBreakpointWarningStatementMarker = "Theme-" + nameof(SelectedBreakpointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1303)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedBreakpointWarningStatementMarker;
    ```
- `public const string SelectedDisabledAdvancedBreakpointStatementMarker = "Theme-" + nameof(SelectedDisabledAdvancedBreakpointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1288)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedDisabledAdvancedBreakpointStatementMarker;
    ```
- `public const string SelectedDisabledAdvancedTracepointStatementMarker = "Theme-" + nameof(SelectedDisabledAdvancedTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1408)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedDisabledAdvancedTracepointStatementMarker;
    ```
- `public const string SelectedDisabledTracepointStatementMarker = "Theme-" + nameof(SelectedDisabledTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1378)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedDisabledTracepointStatementMarker;
    ```
- `public const string SelectedText = "Theme-" + nameof(SelectedText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 758)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedText;
    ```
- `public const string SelectedTracepointErrorStatementMarker = "Theme-" + nameof(SelectedTracepointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1438)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedTracepointErrorStatementMarker;
    ```
- `public const string SelectedTracepointStatementMarker = "Theme-" + nameof(SelectedTracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1363)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedTracepointStatementMarker;
    ```
- `public const string SelectedTracepointWarningStatementMarker = "Theme-" + nameof(SelectedTracepointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1423)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SelectedTracepointWarningStatementMarker;
    ```
- `public const string SignatureHelpCurrentParameter = "currentParam"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1063)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SignatureHelpCurrentParameter;
    ```
- `public const string SignatureHelpDocumentation = "sighelp-documentation"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1058)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SignatureHelpDocumentation;
    ```
- `public const string SignatureHelpParameter = "Theme-" + nameof(SignatureHelpParameter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1068)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SignatureHelpParameter;
    ```
- `public const string SignatureHelpParameterDocumentation = "Theme-" + nameof(SignatureHelpParameterDocumentation)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1073)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.SignatureHelpParameterDocumentation;
    ```
- `public const string StaticEvent = "Theme-" + nameof(StaticEvent)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 178)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.StaticEvent;
    ```
- `public const string StaticField = "Theme-" + nameof(StaticField)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 168)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.StaticField;
    ```
- `public const string StaticMethod = "Theme-" + nameof(StaticMethod)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 143)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.StaticMethod;
    ```
- `public const string StaticProperty = "Theme-" + nameof(StaticProperty)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 188)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.StaticProperty;
    ```
- `public const string StaticType = "Theme-" + nameof(StaticType)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 98)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.StaticType;
    ```
- `public const string String = PredefinedClassificationTypeNames.String`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.String;
    ```
- `public const string Text = RoslynClassificationTypeNames.Text`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Text;
    ```
- `public const string ToStringEval = "Theme-" + nameof(ToStringEval)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 498)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ToStringEval;
    ```
- `public const string TracepointErrorStatement = "Theme-" + nameof(TracepointErrorStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1428)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.TracepointErrorStatement;
    ```
- `public const string TracepointErrorStatementMarker = "Theme-" + nameof(TracepointErrorStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1433)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.TracepointErrorStatementMarker;
    ```
- `public const string TracepointStatement = "Theme-" + nameof(TracepointStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1353)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.TracepointStatement;
    ```
- `public const string TracepointStatementMarker = "Theme-" + nameof(TracepointStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1358)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.TracepointStatementMarker;
    ```
- `public const string TracepointWarningStatement = "Theme-" + nameof(TracepointWarningStatement)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1413)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.TracepointWarningStatement;
    ```
- `public const string TracepointWarningStatementMarker = "Theme-" + nameof(TracepointWarningStatementMarker)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1418)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.TracepointWarningStatementMarker;
    ```
- `public const string Type = RoslynClassificationTypeNames.ClassName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Type;
    ```
- `public const string TypeGenericParameter = RoslynClassificationTypeNames.TypeParameterName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 128)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.TypeGenericParameter;
    ```
- `public const string Url = "url"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 1078)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Url;
    ```
- `public const string ValueType = RoslynClassificationTypeNames.StructName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 118)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.ValueType;
    ```
- `public const string VerbatimString = RoslynClassificationTypeNames.VerbatimStringLiteral`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.VerbatimString;
    ```
- `public const string VisibleWhitespace = "Theme-" + nameof(VisibleWhitespace)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 753)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.VisibleWhitespace;
    ```
- `public const string White = "Theme-" + nameof(White)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 593)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.White;
    ```
- `public const string XamlAttribute = "Theme-" + nameof(XamlAttribute)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 393)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlAttribute;
    ```
- `public const string XamlAttributeQuotes = "Theme-" + nameof(XamlAttributeQuotes)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 398)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlAttributeQuotes;
    ```
- `public const string XamlAttributeValue = "Theme-" + nameof(XamlAttributeValue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 403)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlAttributeValue;
    ```
- `public const string XamlCDataSection = "Theme-" + nameof(XamlCDataSection)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 408)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlCDataSection;
    ```
- `public const string XamlComment = "Theme-" + nameof(XamlComment)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 413)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlComment;
    ```
- `public const string XamlDelimiter = "Theme-" + nameof(XamlDelimiter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 418)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlDelimiter;
    ```
- `public const string XamlKeyword = "Theme-" + nameof(XamlKeyword)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 423)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlKeyword;
    ```
- `public const string XamlMarkupExtensionClass = "Theme-" + nameof(XamlMarkupExtensionClass)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 428)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlMarkupExtensionClass;
    ```
- `public const string XamlMarkupExtensionParameterName = "Theme-" + nameof(XamlMarkupExtensionParameterName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 433)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlMarkupExtensionParameterName;
    ```
- `public const string XamlMarkupExtensionParameterValue = "Theme-" + nameof(XamlMarkupExtensionParameterValue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 438)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlMarkupExtensionParameterValue;
    ```
- `public const string XamlName = "Theme-" + nameof(XamlName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 443)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlName;
    ```
- `public const string XamlProcessingInstruction = "Theme-" + nameof(XamlProcessingInstruction)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 448)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlProcessingInstruction;
    ```
- `public const string XamlText = "Theme-" + nameof(XamlText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 453)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XamlText;
    ```
- `public const string XmlAttribute = "Theme-" + nameof(XmlAttribute)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 343)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlAttribute;
    ```
- `public const string XmlAttributeQuotes = "Theme-" + nameof(XmlAttributeQuotes)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 348)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlAttributeQuotes;
    ```
- `public const string XmlAttributeValue = "Theme-" + nameof(XmlAttributeValue)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 353)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlAttributeValue;
    ```
- `public const string XmlCDataSection = "Theme-" + nameof(XmlCDataSection)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 358)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlCDataSection;
    ```
- `public const string XmlComment = "Theme-" + nameof(XmlComment)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 363)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlComment;
    ```
- `public const string XmlDelimiter = "Theme-" + nameof(XmlDelimiter)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 368)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDelimiter;
    ```
- `public const string XmlDocCommentAttributeName = RoslynClassificationTypeNames.XmlDocCommentAttributeName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 238)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocCommentAttributeName;
    ```
- `public const string XmlDocCommentAttributeQuotes = RoslynClassificationTypeNames.XmlDocCommentAttributeQuotes`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 243)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocCommentAttributeQuotes;
    ```
- `public const string XmlDocCommentAttributeValue = RoslynClassificationTypeNames.XmlDocCommentAttributeValue`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 248)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocCommentAttributeValue;
    ```
- `public const string XmlDocCommentCDataSection = RoslynClassificationTypeNames.XmlDocCommentCDataSection`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 253)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocCommentCDataSection;
    ```
- `public const string XmlDocCommentComment = RoslynClassificationTypeNames.XmlDocCommentComment`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 258)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocCommentComment;
    ```
- `public const string XmlDocCommentDelimiter = RoslynClassificationTypeNames.XmlDocCommentDelimiter`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 263)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocCommentDelimiter;
    ```
- `public const string XmlDocCommentEntityReference = RoslynClassificationTypeNames.XmlDocCommentEntityReference`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 268)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocCommentEntityReference;
    ```
- `public const string XmlDocCommentName = RoslynClassificationTypeNames.XmlDocCommentName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 273)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocCommentName;
    ```
- `public const string XmlDocCommentProcessingInstruction = RoslynClassificationTypeNames.XmlDocCommentProcessingInstruction`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 278)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocCommentProcessingInstruction;
    ```
- `public const string XmlDocCommentText = RoslynClassificationTypeNames.XmlDocCommentText`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 283)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocCommentText;
    ```
- `public const string XmlDocToolTipHeader = "Theme-" + nameof(XmlDocToolTipHeader)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 458)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlDocToolTipHeader;
    ```
- `public const string XmlKeyword = "Theme-" + nameof(XmlKeyword)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 373)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlKeyword;
    ```
- `public const string XmlLiteralAttributeName = RoslynClassificationTypeNames.XmlLiteralAttributeName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 288)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralAttributeName;
    ```
- `public const string XmlLiteralAttributeQuotes = RoslynClassificationTypeNames.XmlLiteralAttributeQuotes`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 293)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralAttributeQuotes;
    ```
- `public const string XmlLiteralAttributeValue = RoslynClassificationTypeNames.XmlLiteralAttributeValue`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 298)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralAttributeValue;
    ```
- `public const string XmlLiteralCDataSection = RoslynClassificationTypeNames.XmlLiteralCDataSection`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 303)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralCDataSection;
    ```
- `public const string XmlLiteralComment = RoslynClassificationTypeNames.XmlLiteralComment`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 308)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralComment;
    ```
- `public const string XmlLiteralDelimiter = RoslynClassificationTypeNames.XmlLiteralDelimiter`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 313)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralDelimiter;
    ```
- `public const string XmlLiteralEmbeddedExpression = RoslynClassificationTypeNames.XmlLiteralEmbeddedExpression`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 318)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralEmbeddedExpression;
    ```
- `public const string XmlLiteralEntityReference = RoslynClassificationTypeNames.XmlLiteralEntityReference`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 323)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralEntityReference;
    ```
- `public const string XmlLiteralName = RoslynClassificationTypeNames.XmlLiteralName`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 328)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralName;
    ```
- `public const string XmlLiteralProcessingInstruction = RoslynClassificationTypeNames.XmlLiteralProcessingInstruction`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 333)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralProcessingInstruction;
    ```
- `public const string XmlLiteralText = RoslynClassificationTypeNames.XmlLiteralText`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 338)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlLiteralText;
    ```
- `public const string XmlName = "Theme-" + nameof(XmlName)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 378)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlName;
    ```
- `public const string XmlProcessingInstruction = "Theme-" + nameof(XmlProcessingInstruction)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 383)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlProcessingInstruction;
    ```
- `public const string XmlText = "Theme-" + nameof(XmlText)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 388)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.XmlText;
    ```
- `public const string Yellow = "Theme-" + nameof(Yellow)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Classification/ThemeClassificationTypeNames.cs` (line 598)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Text.Classification.ThemeClassificationTypeNames.Yellow;
    ```

