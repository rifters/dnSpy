# Namespace `dnSpy.Contracts.Language.Intellisense`

## Class `CompletionConstants`

Completion constants

**Example**

```csharp
// Access dnSpy.Contracts.Language.Intellisense.CompletionConstants members directly without instantiation.
dnSpy.Contracts.Language.Intellisense.CompletionConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/CompletionConstants.cs` (line 24)

### Fields

- `public static readonly int MimimumSearchLengthForFilter = 2`
  - Summary: Minimum length of search string before the collection gets filtered
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/CompletionConstants.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.CompletionConstants.MimimumSearchLengthForFilter;
    ```

## Class `DsCompletion`

A completion item

**Inherits/Implements:** `Completion2`

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.DsCompletion();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletion.cs` (line 30)

### Constructors

- `public DsCompletion()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletion.cs` (line 50)
- `public DsCompletion(string displayText, string filterText = null, string insertionText = null, string description = null, ImageReference imageReference = default, string iconAutomationText = null, IEnumerable<DsCompletionIcon> attributeIcons = null, string suffix = null)`
  - Summary: Constructor
  - Parameters:
    - `string displayText`: Text shown in the UI
    - `string filterText` (default: `null`): Text used to filter out items or null to use
    - `string insertionText` (default: `null`): Text that gets inserted in the text buffer or null to use
    - `string description` (default: `null`): Description or null
    - `ImageReference imageReference` (default: `default`): Icon moniker or null
    - `string iconAutomationText` (default: `null`): Icon automation text or null
    - `IEnumerable<DsCompletionIcon> attributeIcons` (default: `null`): Attribute icons shown on the right side
    - `string suffix` (default: `null`): Text shown after the normal completion text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletion.cs` (line 64)

### Methods

- `protected virtual ImageReference GetImageReference()`
  - Summary: Gets the image reference. Only called if hasn't been initialized.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletion.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.GetImageReference();
    ```
- `public virtual void Commit(ITrackingSpan replaceSpan)`
  - Summary: Adds the new text to the text buffer
  - Parameters:
    - `ITrackingSpan replaceSpan`: Span to replace with new content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletion.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.Commit(replaceSpan: /* ITrackingSpan */);
    ```

### Properties

- `public string FilterText { get; protected set; }`
  - Summary: Gets the text that is used to filter this item
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletion.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FilterText;
    ```
- `public string Suffix { get; }`
  - Summary: Gets the suffix or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletion.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Suffix;
    ```
- `public virtual ImageReference ImageReference => imageReference ?? (imageReference = GetImageReference()).Value`
  - Summary: Gets the icon
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletion.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageReference;
    ```

## Class `DsCompletionIcon`

Completion icon

**Inherits/Implements:** `CompletionIcon`

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.DsCompletionIcon(imageReference: /* ImageReference */, themeImage: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionIcon.cs` (line 27)

### Constructors

- `public DsCompletionIcon(ImageReference imageReference, bool themeImage = false)`
  - Summary: Constructor
  - Parameters:
    - `ImageReference imageReference`: Image
    - `bool themeImage` (default: `false`): true to theme the image by changing it so it matches the background color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionIcon.cs` (line 43)

### Properties

- `public virtual ImageReference ImageReference { get; }`
  - Summary: Gets the image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionIcon.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageReference;
    ```
- `public virtual bool ThemeImage { get; }`
  - Summary: true to theme the image by changing it so it matches the background color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionIcon.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ThemeImage;
    ```

## Class `DsCompletionSet`

collection

**Inherits/Implements:** `CompletionSet`

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.DsCompletionSet();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 31)

### Constructors

- `protected DsCompletionSet()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 66)
- `public DsCompletionSet(string moniker, string displayName, ITrackingSpan applicableTo, IEnumerable<Completion> completions, IEnumerable<Completion> completionBuilders, IReadOnlyList<DsIntellisenseFilter> filters)`
  - Summary: Constructor
  - Parameters:
    - `string moniker`: Unique non-localized identifier
    - `string displayName`: Name shown in the UI if there are multiple s
    - `ITrackingSpan applicableTo`: Span that will be modified when a gets committed
    - `IEnumerable<Completion> completions`: Completion items
    - `IEnumerable<Completion> completionBuilders`: Completion builders
    - `IReadOnlyList<DsIntellisenseFilter> filters`: Filters or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 77)

### Methods

- `protected virtual CompletionSelectionStatus GetBestMatch()`
  - Summary: Gets the best match in
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 166)
  - Example:
    ```csharp
    // Example invocation
    instance.GetBestMatch();
    ```
- `protected virtual int GetMruIndex(Completion completion)`
  - Summary: Gets the MRU index of
  - Parameters:
    - `Completion completion`: Completion item
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 211)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMruIndex(completion: /* Completion */);
    ```
- `protected virtual void Filter(List<Completion> filteredResult, IList<Completion> completions)`
  - Summary: Uses to filter
  - Parameters:
    - `List<Completion> filteredResult`: Result
    - `IList<Completion> completions`: Completion items to filter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.Filter(filteredResult: /* List<Completion> */, completions: /* IList<Completion> */);
    ```
- `public override IReadOnlyList<Span> GetHighlightedSpansInDisplayText(string displayText)`
  - Summary: Gets highlighted text spans or null
  - Parameters:
    - `string displayText`: Text shown in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHighlightedSpansInDisplayText(displayText: /* string */);
    ```
- `public override void Filter()`
  - Summary: Filters the list. should be called after this method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    instance.Filter();
    ```
- `public override void SelectBestMatch()`
  - Summary: Selects the best match and should be called after
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 150)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectBestMatch();
    ```
- `public virtual ICompletionFilter CreateCompletionFilter(string searchText)`
  - Summary: Creates a
  - Parameters:
    - `string searchText`: Search text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateCompletionFilter(searchText: /* string */);
    ```

### Properties

- `public override IList<Completion> CompletionBuilders => filteredCompletionBuilders`
  - Summary: Gets the filtered builders
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CompletionBuilders;
    ```
- `public override IList<Completion> Completions => filteredCompletions`
  - Summary: Gets the filtered s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Completions;
    ```
- `public override ITrackingSpan ApplicableTo {
			get => base.ApplicableTo;
			protected set {
				searchText = null;
				base.ApplicableTo = value;
			}
		}`
  - Summary: Gets or sets the text tracking span to which this completion applies
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ApplicableTo;
    ```
- `public virtual IReadOnlyList<DsIntellisenseFilter> Filters { get; }`
  - Summary: Gets the filters
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsCompletionSet.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filters;
    ```

## Class `DsIntellisenseFilter`

Completion filter

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.DsIntellisenseFilter(imageReference: /* ImageReference */, toolTip: /* string */, accessKey: /* string */, isChecked: /* bool */, isEnabled: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsIntellisenseFilter.cs` (line 26)

### Constructors

- `public DsIntellisenseFilter(ImageReference imageReference, string toolTip, string accessKey, bool isChecked, bool isEnabled)`
  - Summary: Constructor
  - Parameters:
    - `ImageReference imageReference`: Image
    - `string toolTip`: Description not provided.
    - `string accessKey`: Description not provided.
    - `bool isChecked`: Description not provided.
    - `bool isEnabled`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsIntellisenseFilter.cs` (line 35)

### Properties

- `public ImageReference ImageReference { get; }`
  - Summary: Gets the image if any
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsIntellisenseFilter.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageReference;
    ```
- `public bool IsChecked { get; set; }`
  - Summary: true if it's checked
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsIntellisenseFilter.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsChecked;
    ```
- `public bool IsEnabled { get; set; }`
  - Summary: true if it's enabled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsIntellisenseFilter.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnabled;
    ```
- `public string AccessKey { get; }`
  - Summary: Access key or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsIntellisenseFilter.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AccessKey;
    ```
- `public string ToolTip { get; }`
  - Summary: Tooltip or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/DsIntellisenseFilter.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTip;
    ```

## Interface `ICompletionFilter`

Filters s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Language.Intellisense.ICompletionFilter and call its members.
var instance = new dnSpy.Contracts.Language.Intellisense.ICompletionFilter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/ICompletionFilter.cs` (line 27)

### Methods

- `Span[] GetMatchSpans(string completionText)`
  - Summary: Returns spans matching the search text
  - Parameters:
    - `string completionText`: Source text to match, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/ICompletionFilter.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMatchSpans(completionText: /* string */);
    ```
- `bool IsMatch(Completion completion)`
  - Summary: Returns true if the search text matches this
  - Parameters:
    - `Completion completion`: Completion
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/ICompletionFilter.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.IsMatch(completion: /* Completion */);
    ```

## Interface `ICompletionSetContentTypeProvider`

Can be implemented by a to return a content type that should be used when classifying completion items

**Example**

```csharp
// Instantiate dnSpy.Contracts.Language.Intellisense.ICompletionSetContentTypeProvider and call its members.
var instance = new dnSpy.Contracts.Language.Intellisense.ICompletionSetContentTypeProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/ICompletionSetContentTypeProvider.cs` (line 29)

### Methods

- `IContentType GetContentType(IContentTypeRegistryService contentTypeRegistryService, CompletionClassifierKind kind)`
  - Summary: Returns the content type or null
  - Parameters:
    - `IContentTypeRegistryService contentTypeRegistryService`: Content type registry service
    - `CompletionClassifierKind kind`: Kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/ICompletionSetContentTypeProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetContentType(contentTypeRegistryService: /* IContentTypeRegistryService */, kind: /* CompletionClassifierKind */);
    ```

## Class `ParameterDocumentationSignatureHelpClassifierContext`

Parameter documentation signature help classifier context

**Inherits/Implements:** `SignatureHelpClassifierContext`

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.ParameterDocumentationSignatureHelpClassifierContext(session: /* ISignatureHelpSession */, parameter: /* IParameter */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 101)

### Constructors

- `public ParameterDocumentationSignatureHelpClassifierContext(ISignatureHelpSession session, IParameter parameter)`
  - Summary: Constructor
  - Parameters:
    - `ISignatureHelpSession session`: Signature help session
    - `IParameter parameter`: Parameter to classify
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 112)

### Properties

- `public IParameter Parameter { get; }`
  - Summary: Gets the parameter to classify
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 105)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Parameter;
    ```

## Class `ParameterNameSignatureHelpClassifierContext`

Parameter name signature help classifier context

**Inherits/Implements:** `SignatureHelpClassifierContext`

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.ParameterNameSignatureHelpClassifierContext(session: /* ISignatureHelpSession */, parameter: /* IParameter */, nameOffset: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 72)

### Constructors

- `public ParameterNameSignatureHelpClassifierContext(ISignatureHelpSession session, IParameter parameter, int nameOffset)`
  - Summary: Constructor
  - Parameters:
    - `ISignatureHelpSession session`: Signature help session
    - `IParameter parameter`: Parameter to classify
    - `int nameOffset`: Offset of in the text buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 89)

### Properties

- `public IParameter Parameter { get; }`
  - Summary: Gets the parameter to classify
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Parameter;
    ```
- `public int NameOffset { get; }`
  - Summary: Gets the offset of in the text buffer.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NameOffset;
    ```

## Class `PredefinedDsCompletionSourceProviders`

Predefined s

**Example**

```csharp
// Access dnSpy.Contracts.Language.Intellisense.PredefinedDsCompletionSourceProviders members directly without instantiation.
dnSpy.Contracts.Language.Intellisense.PredefinedDsCompletionSourceProviders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedDsCompletionSourceProviders.cs` (line 26)

### Fields

- `public const string Roslyn = "dnSpy-" + nameof(Roslyn)`
  - Summary: Roslyn languages (C# or Visual Basic)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedDsCompletionSourceProviders.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.PredefinedDsCompletionSourceProviders.Roslyn;
    ```

## Class `PredefinedDsQuickInfoSourceProviders`

Predefined names

**Example**

```csharp
// Access dnSpy.Contracts.Language.Intellisense.PredefinedDsQuickInfoSourceProviders members directly without instantiation.
dnSpy.Contracts.Language.Intellisense.PredefinedDsQuickInfoSourceProviders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedDsQuickInfoSourceProviders.cs` (line 27)

### Fields

- `public const string DocumentViewer = "dnSpy-" + nameof(DocumentViewer)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedDsQuickInfoSourceProviders.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.PredefinedDsQuickInfoSourceProviders.DocumentViewer;
    ```
- `public const string Roslyn = "dnSpy-" + nameof(Roslyn)`
  - Summary: Roslyn languages (C# or Visual Basic)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedDsQuickInfoSourceProviders.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.PredefinedDsQuickInfoSourceProviders.Roslyn;
    ```
- `public const string Uri = "dnSpy-" + nameof(Uri)`
  - Summary: URI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedDsQuickInfoSourceProviders.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.PredefinedDsQuickInfoSourceProviders.Uri;
    ```

## Class `PredefinedDsSignatureHelpSourceProviders`

Predefined names

**Example**

```csharp
// Access dnSpy.Contracts.Language.Intellisense.PredefinedDsSignatureHelpSourceProviders members directly without instantiation.
dnSpy.Contracts.Language.Intellisense.PredefinedDsSignatureHelpSourceProviders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedDsSignatureHelpSourceProviders.cs` (line 26)

### Fields

- `public const string Roslyn = "dnSpy-" + nameof(Roslyn)`
  - Summary: Roslyn languages (C# or Visual Basic)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedDsSignatureHelpSourceProviders.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.PredefinedDsSignatureHelpSourceProviders.Roslyn;
    ```

## Class `PredefinedIntellisensePresenterProviders`

Names of s

**Example**

```csharp
// Access dnSpy.Contracts.Language.Intellisense.PredefinedIntellisensePresenterProviders members directly without instantiation.
dnSpy.Contracts.Language.Intellisense.PredefinedIntellisensePresenterProviders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedIntellisensePresenterProviders.cs` (line 26)

### Fields

- `public const string DefaultCompletionPresenter = "Default Completion Presenter"`
  - Summary: Name of default completion presenter provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedIntellisensePresenterProviders.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.PredefinedIntellisensePresenterProviders.DefaultCompletionPresenter;
    ```
- `public const string DefaultQuickInfoPresenter = "Default Quick Info Presenter"`
  - Summary: Name of default quick info presenter provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedIntellisensePresenterProviders.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.PredefinedIntellisensePresenterProviders.DefaultQuickInfoPresenter;
    ```
- `public const string DefaultSignatureHelpPresenter = "Default Signature Help Presenter"`
  - Summary: Name of default signature help presenter provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedIntellisensePresenterProviders.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.PredefinedIntellisensePresenterProviders.DefaultSignatureHelpPresenter;
    ```

## Class `PredefinedUIElementProviderNames`

Names of exports

**Example**

```csharp
// Access dnSpy.Contracts.Language.Intellisense.PredefinedUIElementProviderNames members directly without instantiation.
dnSpy.Contracts.Language.Intellisense.PredefinedUIElementProviderNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedUIElementProviderNames.cs` (line 26)

### Fields

- `public const string RoslynCompletionToolTipProvider = nameof(RoslynCompletionToolTipProvider)`
  - Summary: Roslyn tooltip provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/PredefinedUIElementProviderNames.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.PredefinedUIElementProviderNames.RoslynCompletionToolTipProvider;
    ```

## Class `SignatureDocumentationSignatureHelpClassifierContext`

Signature documentation signature help classifier context

**Inherits/Implements:** `SignatureHelpClassifierContext`

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.SignatureDocumentationSignatureHelpClassifierContext(session: /* ISignatureHelpSession */, signature: /* ISignature */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 54)

### Constructors

- `public SignatureDocumentationSignatureHelpClassifierContext(ISignatureHelpSession session, ISignature signature)`
  - Summary: Constructor
  - Parameters:
    - `ISignatureHelpSession session`: Signature help session
    - `ISignature signature`: Signature to classify
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 65)

### Properties

- `public ISignature Signature { get; }`
  - Summary: Gets the signature to classify
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Signature;
    ```

## Class `SignatureHelpClassifierContext`

Signature help classifier context. Use to get the instance.

**Example**

```csharp
var instance = new dnSpy.Contracts.Language.Intellisense.SignatureHelpClassifierContext(type: /* string */, session: /* ISignatureHelpSession */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 29)

### Constructors

- `protected internal SignatureHelpClassifierContext(string type, ISignatureHelpSession session)`
  - Summary: Constructor
  - Parameters:
    - `string type`: Context type, eg.
    - `ISignatureHelpSession session`: Signature help session
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 45)

### Properties

- `public ISignatureHelpSession Session { get; }`
  - Summary: Gets the signature help session
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Session;
    ```
- `public string Type { get; }`
  - Summary: Gets the type, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```

## Class `SignatureHelpClassifierContextTypes`

Signature help context types (see )

**Example**

```csharp
// Access dnSpy.Contracts.Language.Intellisense.SignatureHelpClassifierContextTypes members directly without instantiation.
dnSpy.Contracts.Language.Intellisense.SignatureHelpClassifierContextTypes./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 119)

### Fields

- `public static readonly string ParameterDocumentation = nameof(ParameterDocumentation)`
  - Summary: Parameter documentation
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 133)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.SignatureHelpClassifierContextTypes.ParameterDocumentation;
    ```
- `public static readonly string ParameterName = nameof(ParameterName)`
  - Summary: Parameter name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 128)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.SignatureHelpClassifierContextTypes.ParameterName;
    ```
- `public static readonly string SignatureDocumentation = nameof(SignatureDocumentation)`
  - Summary: Signature documentation
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpClassifierContext.cs` (line 123)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.SignatureHelpClassifierContextTypes.SignatureDocumentation;
    ```

## Class `SignatureHelpConstants`

Signature help constants

**Example**

```csharp
// Access dnSpy.Contracts.Language.Intellisense.SignatureHelpConstants members directly without instantiation.
dnSpy.Contracts.Language.Intellisense.SignatureHelpConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpConstants.cs` (line 29)

### Methods

- `public static ISignatureHelpSession TryGetSignatureHelpSession(this ITextBuffer buffer)`
  - Summary: Returns the signature help session or null if is not a signature help buffer
  - Parameters:
    - `this ITextBuffer buffer`: Text buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpConstants.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Language.Intellisense.SignatureHelpConstants.TryGetSignatureHelpSession(buffer: /* ITextBuffer */);
    ```
- `public static SignatureHelpClassifierContext TryGetSignatureHelpClassifierContext(this ITextBuffer buffer)`
  - Summary: Returns the signature help classifier context or null if is not a signature help buffer
  - Parameters:
    - `this ITextBuffer buffer`: Text buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpConstants.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Language.Intellisense.SignatureHelpConstants.TryGetSignatureHelpClassifierContext(buffer: /* ITextBuffer */);
    ```
- `public static bool GetUsePrettyPrintedContent(this ITextBuffer buffer)`
  - Summary: Gets the UsePrettyPrintedContent value
  - Parameters:
    - `this ITextBuffer buffer`: Signature help text buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpConstants.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Language.Intellisense.SignatureHelpConstants.GetUsePrettyPrintedContent(buffer: /* ITextBuffer */);
    ```

### Fields

- `public const string ExtendedSignatureHelpContentTypeSuffix = " Signature Help Ex"`
  - Summary: Suffix added to the current signature's content type name () to get the name of the content type for the signature help documentation and parameter text and documentation. This feature is only enabled if this content type has been defined, it's not created by the signature help code. The classifier should use to get the information it needs.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpConstants.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.SignatureHelpConstants.ExtendedSignatureHelpContentTypeSuffix;
    ```
- `public const string SignatureHelpContentTypeSuffix = " Signature Help"`
  - Summary: Suffix added to the current signature's content type name () to get the name of the content type for the signature help text. This content type is created if it doesn't exist.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpConstants.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.SignatureHelpConstants.SignatureHelpContentTypeSuffix;
    ```
- `public const string UsePrettyPrintedContentBufferKey = "UsePrettyPrintedContent"`
  - Summary: property key of a that indicates whether the pretty printed content should be used ( vs and vs )
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpConstants.cs` (line 57)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.SignatureHelpConstants.UsePrettyPrintedContentBufferKey;
    ```
- `public static readonly object SessionBufferKey = typeof(ISignatureHelpSession)`
  - Summary: property key to get the instance. It's used by the signature help classifiers to get the session to classify.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpConstants.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.SignatureHelpConstants.SessionBufferKey;
    ```
- `public static readonly object SignatureHelpClassifierContextBufferKey = typeof(SignatureHelpClassifierContext)`
  - Summary: property key to get the instance.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Language/Intellisense/SignatureHelpConstants.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Language.Intellisense.SignatureHelpConstants.SignatureHelpClassifierContextBufferKey;
    ```

