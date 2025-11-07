# Namespace `dnSpy.Contracts.Text.Editor.Operations`

## Interface `ITextViewUndoManager`

Text view undo manager

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.Operations.ITextViewUndoManager and call its members.
var instance = new dnSpy.Contracts.Text.Editor.Operations.ITextViewUndoManager(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/Operations/ITextViewUndoManager.cs` (line 26)

### Methods

- `void ClearUndoHistory()`
  - Summary: Clears the undo/redo history. also gets updated with a new instance.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/Operations/ITextViewUndoManager.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.ClearUndoHistory();
    ```

### Properties

- `IDsWpfTextView TextView { get; }`
  - Summary: Gets the text view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/Operations/ITextViewUndoManager.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextView;
    ```
- `ITextUndoHistory TextViewUndoHistory { get; }`
  - Summary: Gets the undo history
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/Operations/ITextViewUndoManager.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewUndoHistory;
    ```

## Interface `ITextViewUndoManagerProvider`

Enables undo/redo in text views

**Example**

```csharp
// Instantiate dnSpy.Contracts.Text.Editor.Operations.ITextViewUndoManagerProvider and call its members.
var instance = new dnSpy.Contracts.Text.Editor.Operations.ITextViewUndoManagerProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/Operations/ITextViewUndoManagerProvider.cs` (line 24)

### Methods

- `ITextViewUndoManager GetTextViewUndoManager(IDsWpfTextView textView)`
  - Summary: Creates or returns a cached instance
  - Parameters:
    - `IDsWpfTextView textView`: Text view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/Operations/ITextViewUndoManagerProvider.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTextViewUndoManager(textView: /* IDsWpfTextView */);
    ```
- `bool TryGetTextViewUndoManager(IDsWpfTextView textView, out ITextViewUndoManager manager)`
  - Summary: Tries to return an existing instance
  - Parameters:
    - `IDsWpfTextView textView`: Text view
    - `out ITextViewUndoManager manager`: Updated with the existing instance or null if none exists
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/Operations/ITextViewUndoManagerProvider.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetTextViewUndoManager(textView: /* IDsWpfTextView */, manager: /* ITextViewUndoManager */);
    ```
- `void RemoveTextViewUndoManager(IDsWpfTextView textView)`
  - Summary: Removes the cached instance, if any.
  - Parameters:
    - `IDsWpfTextView textView`: Text view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Text/Editor/Operations/ITextViewUndoManagerProvider.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveTextViewUndoManager(textView: /* IDsWpfTextView */);
    ```

