# Namespace `dnSpy.Contracts.Text.Editor.OptionsExtensionMethods`

## Class `DefaultDsOptionsExtensions`

extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsOptionsExtensions members directly without instantiation.
dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsOptionsExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsOptionsExtensions.cs` (line 27)

### Methods

- `public static IndentStyle GetIndentStyle(this IEditorOptions options)`
  - Summary: Gets the indent style option
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsOptionsExtensions.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsOptionsExtensions.GetIndentStyle(options: /* IEditorOptions */);
    ```

## Class `DefaultDsTextViewOptionsExtensions`

extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions members directly without instantiation.
dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 27)

### Methods

- `public static BlockStructureLineKind GetBlockStructureLineKind(this IEditorOptions options)`
  - Summary: Gets the value
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.GetBlockStructureLineKind(options: /* IEditorOptions */);
    ```
- `public static bool IsAllowBoxSelectionEnabled(this IEditorOptions options)`
  - Summary: Returns true if box selection is enabled
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsAllowBoxSelectionEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsBraceMatchingEnabled(this IEditorOptions options)`
  - Summary: Returns true if braces should be highlighted
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsBraceMatchingEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsCanChangeOverwriteModeEnabled(this IEditorOptions options)`
  - Summary: Returns true if the user can change overwrite mode
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsCanChangeOverwriteModeEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsCanChangeUseVisibleWhitespaceEnabled(this IEditorOptions options)`
  - Summary: Returns true if the user can enable or disable use-visible-whitespace option
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsCanChangeUseVisibleWhitespaceEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsCanChangeWordWrapStyleEnabled(this IEditorOptions options)`
  - Summary: Returns true if the user can change word wrap style
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsCanChangeWordWrapStyleEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsColorizationEnabled(this IEditorOptions options)`
  - Summary: Returns true if text should be colorized
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsColorizationEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsCompressEmptyOrWhitespaceLinesEnabled(this IEditorOptions options)`
  - Summary: Returns true if empty or whitespace-only lines should be compressed
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 154)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsCompressEmptyOrWhitespaceLinesEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsCompressNonLetterLinesEnabled(this IEditorOptions options)`
  - Summary: Returns true if non-empty lines that don't contain letters or digits should be compressed
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 165)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsCompressNonLetterLinesEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsHighlightRelatedKeywordsEnabled(this IEditorOptions options)`
  - Summary: Returns true if related keywords should be highlighted
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsHighlightRelatedKeywordsEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsLineSeparatorEnabled(this IEditorOptions options)`
  - Summary: Returns true if line separators should be shown
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsLineSeparatorEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsReferenceHighlightingEnabled(this IEditorOptions options)`
  - Summary: Returns true if references should be highlighted
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 110)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsReferenceHighlightingEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsRefreshScreenOnChangeEnabled(this IEditorOptions options)`
  - Summary: Returns true if refresh-screen-on-change is enabled
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsRefreshScreenOnChangeEnabled(options: /* IEditorOptions */);
    ```
- `public static bool IsRemoveExtraTextLineVerticalPixelsEnabled(this IEditorOptions options)`
  - Summary: Returns true if extra vertical pixels should be removed from text lines
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 176)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.IsRemoveExtraTextLineVerticalPixelsEnabled(options: /* IEditorOptions */);
    ```
- `public static int GetRefreshScreenOnChangeWaitMilliSeconds(this IEditorOptions options)`
  - Summary: Returns the number of milliseconds to wait before refreshing the screen after the document gets changed
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsTextViewOptionsExtensions.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsTextViewOptionsExtensions.GetRefreshScreenOnChangeWaitMilliSeconds(options: /* IEditorOptions */);
    ```

## Class `DefaultDsWpfViewOptionsExtensions`

extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsWpfViewOptionsExtensions members directly without instantiation.
dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsWpfViewOptionsExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsWpfViewOptionsExtensions.cs` (line 27)

### Methods

- `public static bool IsForceClearTypeIfNeededEnabled(this IEditorOptions options)`
  - Summary: Returns true if clear type should be forced is enabled
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultDsWpfViewOptionsExtensions.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultDsWpfViewOptionsExtensions.IsForceClearTypeIfNeededEnabled(options: /* IEditorOptions */);
    ```

## Class `DefaultReplEditorOptionsExtensions`

extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultReplEditorOptionsExtensions members directly without instantiation.
dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultReplEditorOptionsExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultReplEditorOptionsExtensions.cs` (line 27)

### Methods

- `public static bool IsReplRefreshScreenOnChangeEnabled(this IEditorOptions options)`
  - Summary: Returns true if refresh-screen-on-change is enabled
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultReplEditorOptionsExtensions.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultReplEditorOptionsExtensions.IsReplRefreshScreenOnChangeEnabled(options: /* IEditorOptions */);
    ```
- `public static int GetReplRefreshScreenOnChangeWaitMilliSeconds(this IEditorOptions options)`
  - Summary: Returns the number of milliseconds to wait before refreshing the screen after the document gets changed
  - Parameters:
    - `this IEditorOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/OptionsExtensionMethods/DefaultReplEditorOptionsExtensions.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Text.Editor.OptionsExtensionMethods.DefaultReplEditorOptionsExtensions.GetReplRefreshScreenOnChangeWaitMilliSeconds(options: /* IEditorOptions */);
    ```

