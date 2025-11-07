# Namespace `dnSpy.Contracts.Controls.ToolWindows`

## Class `EditCompletedEventArgs`

event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Controls.ToolWindows.EditCompletedEventArgs(newText: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditValue.cs` (line 60)

### Constructors

- `public EditCompletedEventArgs(string newText)`
  - Summary: Constructor
  - Parameters:
    - `string newText`: New text or null if it was canceled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditValue.cs` (line 70)

### Properties

- `public string NewText { get; }`
  - Summary: Gets the new text or null if it was canceled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditValue.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewText;
    ```

## Class `EditValueControl`

**Inherits/Implements:** `UserControl`

**Example**

```csharp
var instance = new dnSpy.Contracts.Controls.ToolWindows.EditValueControl();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/EditValueControl.xaml.cs` (line 30)

### Constructors

- `public EditValueControl()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/EditValueControl.xaml.cs` (line 67)

### Methods

- `protected override void OnMouseDoubleClick(MouseButtonEventArgs e)`
  - Parameters:
    - `MouseButtonEventArgs e`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/EditValueControl.xaml.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseDoubleClick(e: /* MouseButtonEventArgs */);
    ```
- `protected override void OnMouseLeftButtonUp(MouseButtonEventArgs e)`
  - Parameters:
    - `MouseButtonEventArgs e`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/EditValueControl.xaml.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.OnMouseLeftButtonUp(e: /* MouseButtonEventArgs */);
    ```

### Properties

- `public IEditValueProvider EditValueProvider {
			get => (IEditValueProvider)GetValue(EditValueProviderProperty);
			set => SetValue(EditValueProviderProperty, value);
		}`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/EditValueControl.xaml.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EditValueProvider;
    ```
- `public IEditableValue EditableValue {
			get => (IEditableValue)GetValue(EditableValueProperty);
			set => SetValue(EditableValueProperty, value);
		}`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/EditValueControl.xaml.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EditableValue;
    ```
- `public object ReadOnlyContent {
			get => GetValue(ReadOnlyContentProperty);
			set => SetValue(ReadOnlyContentProperty, value);
		}`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/EditValueControl.xaml.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReadOnlyContent;
    ```

### Fields

- `public static readonly DependencyProperty EditValueProviderProperty = DependencyProperty.Register(nameof(EditValueProvider), typeof(IEditValueProvider), typeof(EditValueControl),
			new FrameworkPropertyMetadata(null, EditValueProviderProperty_PropertyChangedCallback))`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/EditValueControl.xaml.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Controls.ToolWindows.EditValueControl.EditValueProviderProperty;
    ```
- `public static readonly DependencyProperty EditableValueProperty = DependencyProperty.Register(nameof(EditableValue), typeof(IEditableValue), typeof(EditValueControl),
			new FrameworkPropertyMetadata(null, EditableValueProperty_PropertyChangedCallback))`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/EditValueControl.xaml.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Controls.ToolWindows.EditValueControl.EditableValueProperty;
    ```
- `public static readonly DependencyProperty ReadOnlyContentProperty = DependencyProperty.Register(nameof(ReadOnlyContent), typeof(object), typeof(EditValueControl),
			new FrameworkPropertyMetadata(null))`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/EditValueControl.xaml.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Controls.ToolWindows.EditValueControl.ReadOnlyContentProperty;
    ```

## Enum `EditValueFlags`

Edit value flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Controls.ToolWindows.EditValueFlags and call its members.
var instance = new dnSpy.Contracts.Controls.ToolWindows.EditValueFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 78)

### Members

- `None`: No bit is set
- `SelectText` = `x00000001`: Select the text

## Enum `EditableValueOptions`

options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Controls.ToolWindows.EditableValueOptions and call its members.
var instance = new dnSpy.Contracts.Controls.ToolWindows.EditableValueOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 27)

### Members

- `None`: No bit is set
- `SingleClick` = `x00000001`: Single click to edit text

## Struct `EditableValueTextInfo`

Contains the text to edit

**Example**

```csharp
var instance = new dnSpy.Contracts.Controls.ToolWindows.EditableValueTextInfo(text: /* string */, flags: /* EditValueFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 94)

### Constructors

- `public EditableValueTextInfo(string text, EditValueFlags flags = EditValueFlags.SelectText)`
  - Summary: Constructor
  - Parameters:
    - `string text`: Text to edit
    - `EditValueFlags flags` (default: `EditValueFlags.SelectText`): Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 110)

### Properties

- `public EditValueFlags Flags { get; }`
  - Summary: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 103)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public string Text { get; }`
  - Summary: Gets the text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 98)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Text;
    ```

## Interface `IEditValue`

Edits a value

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Controls.ToolWindows.IEditValue and call its members.
var instance = new dnSpy.Contracts.Controls.ToolWindows.IEditValue(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditValue.cs` (line 40)

### Properties

- `bool IsKeyboardFocused { get; }`
  - Summary: true if the control has keyboard focus
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditValue.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsKeyboardFocused;
    ```
- `object UIObject { get; }`
  - Summary: Gets the UI object (text control)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditValue.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIObject;
    ```

### Events

- `event EventHandler<EditCompletedEventArgs> EditCompleted`
  - Summary: Raised when the edit is completed (there's new text or the user canceled the edit operation)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditValue.cs` (line 54)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.EditCompleted += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IEditValueProvider`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Controls.ToolWindows.IEditValueProvider and call its members.
var instance = new dnSpy.Contracts.Controls.ToolWindows.IEditValueProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditValue.cs` (line 26)

### Methods

- `IEditValue Create(string text, EditValueFlags flags)`
  - Summary: Creates a . This is called by the control when the user has started the edit operation.
  - Parameters:
    - `string text`: Text shown in the control
    - `EditValueFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditValue.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(text: /* string */, flags: /* EditValueFlags */);
    ```

## Interface `IEditableValue`

Implemented by data that can be edited

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Controls.ToolWindows.IEditableValue and call its members.
var instance = new dnSpy.Contracts.Controls.ToolWindows.IEditableValue(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 43)

### Methods

- `EditableValueTextInfo GetText()`
  - Summary: Returns the text shown in the control
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.GetText();
    ```
- `void SetText(string text)`
  - Summary: The control calls this method to write the new value
  - Parameters:
    - `string text`: New text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.SetText(text: /* string */);
    ```

### Properties

- `EditableValueOptions Options { get; }`
  - Summary: Gets the options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```
- `bool CanEdit { get; }`
  - Summary: true if the value can be edited, false if it's read-only
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanEdit;
    ```
- `bool IsEditingValue { get; set; }`
  - Summary: When true is written to this property, the edit textbox is made visible and the user can edit the value. The control will write false to it when the edit operation is completed (eg. the user hit enter or escape.) The control also writes true to this property if the user double clicks it.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/IEditableValue.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEditingValue;
    ```

## Class `ListBoxSelectedItemsAP`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Controls.ToolWindows.ListBoxSelectedItemsAP and call its members.
var instance = new dnSpy.Contracts.Controls.ToolWindows.ListBoxSelectedItemsAP(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/ListBoxSelectedItemsAP.cs` (line 29)

### Methods

- `public static IList GetSelectedItemsVM(ListBox listBox)`
  - Parameters:
    - `ListBox listBox`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/ListBoxSelectedItemsAP.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Controls.ToolWindows.ListBoxSelectedItemsAP.GetSelectedItemsVM(listBox: /* ListBox */);
    ```
- `public static void SetSelectedItemsVM(ListBox listBox, IList value)`
  - Parameters:
    - `ListBox listBox`: Description not provided.
    - `IList value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/ListBoxSelectedItemsAP.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Controls.ToolWindows.ListBoxSelectedItemsAP.SetSelectedItemsVM(listBox: /* ListBox */, value: /* IList */);
    ```

### Fields

- `public static readonly DependencyProperty SelectedItemsVMProperty = DependencyProperty.RegisterAttached(
			"SelectedItemsVM", typeof(IList), typeof(ListBoxSelectedItemsAP), new UIPropertyMetadata(null, SelectedItemsVMPropertyChangedCallback))`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Controls/ToolWindows/ListBoxSelectedItemsAP.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Controls.ToolWindows.ListBoxSelectedItemsAP.SelectedItemsVMProperty;
    ```

