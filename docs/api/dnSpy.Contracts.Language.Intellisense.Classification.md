# Namespace `dnSpy.Contracts.Language.Intellisense.Classification`

## Class `CompletionClassifierContext`

Completion classifier context

**Inherits/Implements:** `TextClassifierContext`

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.Classification.CompletionClassifierContext(completionSet: /* CompletionSet */, completion: /* Completion */, text: /* string */, colorize: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionClassifierContext.cs` (line 28)

### Constructors

- `protected CompletionClassifierContext(CompletionSet completionSet, Completion completion, string text, bool colorize)`
  - Summary: Constructor
  - Parameters:
    - `CompletionSet completionSet`: Completion set
    - `Completion completion`: Completion to classify
    - `string text`: Text to classify
    - `bool colorize`: true if it should be colorized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionClassifierContext.cs` (line 51)

### Properties

- `public Completion Completion { get; }`
  - Summary: Gets the completion to classify
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionClassifierContext.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Completion;
    ```
- `public CompletionSet CompletionSet { get; }`
  - Summary: Gets the collection
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionClassifierContext.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CompletionSet;
    ```
- `public abstract CompletionClassifierKind Kind { get; }`
  - Summary: Context kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionClassifierContext.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

## Enum `CompletionClassifierKind`

Completion classifier kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Language.Intellisense.Classification.CompletionClassifierKind and call its members.
var instance = new dnSpy.Contracts.Language.Intellisense.Classification.CompletionClassifierKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionClassifierKind.cs` (line 26)

### Members

- `DisplayText`: Classify , the context is a
- `Suffix`: Classify , the context is a

## Class `CompletionDisplayTextClassifierContext`

Context needed to classify

**Inherits/Implements:** `CompletionClassifierContext`

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.Classification.CompletionDisplayTextClassifierContext(completionSet: /* CompletionSet */, completion: /* Completion */, displayText: /* string */, inputText: /* string */, colorize: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionDisplayTextClassifierContext.cs` (line 27)

### Constructors

- `public CompletionDisplayTextClassifierContext(CompletionSet completionSet, Completion completion, string displayText, string inputText, bool colorize)`
  - Summary: Constructor
  - Parameters:
    - `CompletionSet completionSet`: Completion set
    - `Completion completion`: Completion to classify
    - `string displayText`: Text to classify
    - `string inputText`: Current user input text
    - `bool colorize`: true if it should be colorized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionDisplayTextClassifierContext.cs` (line 46)

### Properties

- `public override CompletionClassifierKind Kind => CompletionClassifierKind.DisplayText`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionDisplayTextClassifierContext.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public string InputText { get; }`
  - Summary: Gets the current user input text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionDisplayTextClassifierContext.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InputText;
    ```

## Class `CompletionSuffixClassifierContext`

Context needed to classify

**Inherits/Implements:** `CompletionClassifierContext`

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.Classification.CompletionSuffixClassifierContext(completionSet: /* CompletionSet */, completion: /* Completion */, suffix: /* string */, colorize: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionSuffixClassifierContext.cs` (line 26)

### Constructors

- `public CompletionSuffixClassifierContext(CompletionSet completionSet, Completion completion, string suffix, bool colorize)`
  - Summary: Constructor
  - Parameters:
    - `CompletionSet completionSet`: Completion set
    - `Completion completion`: Completion to classify
    - `string suffix`: Text to classify
    - `bool colorize`: true if it should be colorized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionSuffixClassifierContext.cs` (line 39)

### Properties

- `public override CompletionClassifierKind Kind => CompletionClassifierKind.Suffix`
  - Summary: Returns
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/Classification/CompletionSuffixClassifierContext.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```

