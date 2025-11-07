# Namespace `dnSpy.Contracts.Disassembly.Viewer`

## Struct `DisassemblyContent`

Disassembled content shown in the disassembly viewer

**Example**

```csharp
var instance = new dnSpy.Contracts.Disassembly.Viewer.DisassemblyContent(kind: /* DisassemblyContentKind */, text: /* DisassemblyText[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContent.cs` (line 26)

### Constructors

- `public DisassemblyContent(DisassemblyContentKind kind, DisassemblyText[] text)`
  - Summary: Constructor
  - Parameters:
    - `DisassemblyContentKind kind`: Content kind
    - `DisassemblyText[] text`: Disassembly
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContent.cs` (line 42)

### Properties

- `public DisassemblyContentKind Kind { get; }`
  - Summary: Gets the content kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContent.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public DisassemblyText[] Text { get; }`
  - Summary: Gets the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContent.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Enum `DisassemblyContentFormatterOptions`

Disassembly options

**Inherits/Implements:** `uint`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.Viewer.DisassemblyContentFormatterOptions and call its members.
var instance = new dnSpy.Contracts.Disassembly.Viewer.DisassemblyContentFormatterOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentFormatterOptions.cs` (line 26)

### Members

- `None`: No option is enabled
- `EmptyLineBetweenBasicBlocks` = `x00000001`: Add an empty line between basic blocks (overrides global options)
- `NoEmptyLineBetweenBasicBlocks` = `x00000002`: Don't add an empty line between basic blocks (overrides global options)
- `InstructionAddresses` = `x00000004`: Show instruction addresses (overrides global options)
- `NoInstructionAddresses` = `x00000008`: Don't show instruction addresses (overrides global options)
- `InstructionBytes` = `x00000010`: Show instruction bytes (overrides global options)
- `NoInstructionBytes` = `x00000020`: Don't show instruction bytes (overrides global options)
- `AddLabels` = `x00000040`: Add labels to the disassembled code (overrides global options)
- `NoAddLabels` = `x00000080`: Don't add labels to the disassembled code (overrides global options)

## Enum `DisassemblyContentKind`

Content kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.Viewer.DisassemblyContentKind and call its members.
var instance = new dnSpy.Contracts.Disassembly.Viewer.DisassemblyContentKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContent.cs` (line 51)

### Members

- `Unknown`: Some other unknown kind
- `Masm`: x86 masm syntax
- `Nasm`: x86 nasm syntax
- `ATT`: x86 AT&T syntax

## Class `DisassemblyContentProvider`

Creates the text shown in the disassembly window and notifies listeners when the text is changed. Created by

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.Viewer.DisassemblyContentProvider and call its members.
var instance = new dnSpy.Contracts.Disassembly.Viewer.DisassemblyContentProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentProvider.cs` (line 27)

### Methods

- `public abstract DisassemblyContent GetContent()`
  - Summary: Gets the content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetContent();
    ```
- `public abstract DisassemblyContentProvider Clone()`
  - Summary: Clones this instance so it can be shown in a new tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentProvider.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```
- `public abstract void Dispose()`
  - Summary: Called when it's no longer used by a view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentProvider.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Events

- `public abstract event EventHandler OnContentChanged`
  - Summary: Raised when the content is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentProvider.cs` (line 31)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.OnContentChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DisassemblyContentProviderFactory`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.Viewer.DisassemblyContentProviderFactory and call its members.
var instance = new dnSpy.Contracts.Disassembly.Viewer.DisassemblyContentProviderFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentProviderFactory.cs` (line 24)

### Methods

- `public abstract DisassemblyContentProvider Create(NativeCode code, DisassemblyContentFormatterOptions formatterOptions, ISymbolResolver symbolResolver, string header)`
  - Summary: Creates a that can be passed to
  - Parameters:
    - `NativeCode code`: Native code
    - `DisassemblyContentFormatterOptions formatterOptions`: Options
    - `ISymbolResolver symbolResolver`: Symbol resolver or null
    - `string header`: Header comment added at the top of the document or null. This can contain multiple lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentProviderFactory.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(code: /* NativeCode */, formatterOptions: /* DisassemblyContentFormatterOptions */, symbolResolver: /* ISymbolResolver */, header: /* string */);
    ```

## Class `DisassemblyContentSettings`

Disassembly content settings

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.Viewer.DisassemblyContentSettings and call its members.
var instance = new dnSpy.Contracts.Disassembly.Viewer.DisassemblyContentSettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 26)

### Methods

- `protected void OnPropertyChanged(string propName)`
  - Summary: Raises
  - Parameters:
    - `string propName`: Name of property that changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propName: /* string */);
    ```

### Properties

- `public abstract X86Disassembler X86Disassembler { get; set; }`
  - Summary: x86 disassembler
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.X86Disassembler;
    ```
- `public abstract bool AddLabels { get; set; }`
  - Summary: Add labels to the disassembled code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AddLabels;
    ```
- `public abstract bool EmptyLineBetweenBasicBlocks { get; set; }`
  - Summary: Add an empty line between basic blocks
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EmptyLineBetweenBasicBlocks;
    ```
- `public abstract bool ShowCode { get; set; }`
  - Summary: Show source code or decompiled code, if available
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowCode;
    ```
- `public abstract bool ShowILCode { get; set; }`
  - Summary: Show IL code, if available
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowILCode;
    ```
- `public abstract bool ShowInstructionAddress { get; set; }`
  - Summary: Show instruction address
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowInstructionAddress;
    ```
- `public abstract bool ShowInstructionBytes { get; set; }`
  - Summary: Show instruction bytes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowInstructionBytes;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 30)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Enum `DisassemblyReferenceFlags`

reference flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.Viewer.DisassemblyReferenceFlags and call its members.
var instance = new dnSpy.Contracts.Disassembly.Viewer.DisassemblyReferenceFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyText.cs` (line 65)

### Members

- `None`: No bit is set
- `Definition` = `x00000001`: It's a definition if set, else it's a reference to the definition
- `Local` = `x00000002`: It's a local definition or reference, eg. a label

## Struct `DisassemblyText`

Text and color

**Example**

```csharp
var instance = new dnSpy.Contracts.Disassembly.Viewer.DisassemblyText(color: /* object */, text: /* string */, reference: /* object */, referenceFlags: /* DisassemblyReferenceFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyText.cs` (line 26)

### Constructors

- `public DisassemblyText(object color, string text, object reference, DisassemblyReferenceFlags referenceFlags)`
  - Summary: Constructor
  - Parameters:
    - `object color`: Color
    - `string text`: Text
    - `object reference`: Reference or null
    - `DisassemblyReferenceFlags referenceFlags`: Reference flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyText.cs` (line 54)

### Properties

- `public DisassemblyReferenceFlags ReferenceFlags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyText.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReferenceFlags;
    ```
- `public object Color { get; }`
  - Summary: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyText.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Color;
    ```
- `public object Reference { get; }`
  - Summary: Gets the reference or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyText.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reference;
    ```
- `public string Text { get; }`
  - Summary: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyText.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Class `DisassemblyViewerService`

Shows disassembled code in a disassembly viewer

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.Viewer.DisassemblyViewerService and call its members.
var instance = new dnSpy.Contracts.Disassembly.Viewer.DisassemblyViewerService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyViewerService.cs` (line 24)

### Methods

- `public abstract void Show(DisassemblyContentProvider contentProvider, bool newTab, string title = null)`
  - Summary: Shows the disassembly in a viewer
  - Parameters:
    - `DisassemblyContentProvider contentProvider`: Content provider
    - `bool newTab`: true to always create a new tab, false to re-use an existing disassembly viewer
    - `string title` (default: `null`): Tab title or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyViewerService.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(contentProvider: /* DisassemblyContentProvider */, newTab: /* bool */, title: /* string */);
    ```
- `public void Show(DisassemblyContentProvider contentProvider, string title = null)`
  - Summary: Shows the disassembly in a viewer
  - Parameters:
    - `DisassemblyContentProvider contentProvider`: Content provider
    - `string title` (default: `null`): Tab title or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyViewerService.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(contentProvider: /* DisassemblyContentProvider */, title: /* string */);
    ```

### Properties

- `public abstract DisassemblyViewerServiceSettings Settings { get; }`
  - Summary: Gets the settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyViewerService.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```

## Class `DisassemblyViewerServiceSettings`

settings

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.Viewer.DisassemblyViewerServiceSettings and call its members.
var instance = new dnSpy.Contracts.Disassembly.Viewer.DisassemblyViewerServiceSettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyViewerServiceSettings.cs` (line 26)

### Methods

- `protected void OnPropertyChanged(string propName)`
  - Summary: Raises
  - Parameters:
    - `string propName`: Name of property that changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyViewerServiceSettings.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propName: /* string */);
    ```

### Properties

- `public abstract bool OpenNewTab { get; set; }`
  - Summary: Open a new tab instead of reusing the current tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyViewerServiceSettings.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OpenNewTab;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyViewerServiceSettings.cs` (line 30)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Enum `X86Disassembler`

x86 disassembler

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.Viewer.X86Disassembler and call its members.
var instance = new dnSpy.Contracts.Disassembly.Viewer.X86Disassembler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/Viewer/DisassemblyContentSettings.cs` (line 77)

### Members

- `Masm`: masm disassembler
- `Nasm`: nasm disassembler
- `Gas`: GNU assembler (AT&T) disassembler

