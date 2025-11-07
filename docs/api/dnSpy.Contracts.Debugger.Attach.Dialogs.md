# Namespace `dnSpy.Contracts.Debugger.Attach.Dialogs`

## Struct `AttachToProcessLinkInfo`

Link info

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Attach.Dialogs.AttachToProcessLinkInfo and call its members.
var instance = new dnSpy.Contracts.Debugger.Attach.Dialogs.AttachToProcessLinkInfo(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialogOptions.cs` (line 55)

### Properties

- `public string ToolTipMessage { get; set; }`
  - Summary: Tooltip message
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialogOptions.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTipMessage;
    ```
- `public string Url { get; set; }`
  - Summary: URL to go to when button is clicked
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialogOptions.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Url;
    ```

## Class `ShowAttachToProcessDialog`

Shows the Attach to Process dialog box

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Attach.Dialogs.ShowAttachToProcessDialog and call its members.
var instance = new dnSpy.Contracts.Debugger.Attach.Dialogs.ShowAttachToProcessDialog(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialog.cs` (line 24)

### Methods

- `public abstract AttachToProgramOptions[] Show(ShowAttachToProcessDialogOptions options = null)`
  - Summary: Shows the dialog box and returns the selected processes or an empty list
  - Parameters:
    - `ShowAttachToProcessDialogOptions options` (default: `null`): Options or null to use the default options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialog.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(options: /* ShowAttachToProcessDialogOptions */);
    ```
- `public abstract void Attach(ShowAttachToProcessDialogOptions options = null)`
  - Summary: Shows the dialog box and attaches to the selected processes
  - Parameters:
    - `ShowAttachToProcessDialogOptions options` (default: `null`): Options or null to use the default options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialog.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Attach(options: /* ShowAttachToProcessDialogOptions */);
    ```

## Class `ShowAttachToProcessDialogOptions`

Attach to Process dialog options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Attach.Dialogs.ShowAttachToProcessDialogOptions and call its members.
var instance = new dnSpy.Contracts.Debugger.Attach.Dialogs.ShowAttachToProcessDialogOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialogOptions.cs` (line 24)

### Properties

- `public AttachToProcessLinkInfo? InfoLink { get; set; }`
  - Summary: Link button info shown next to the OK button
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialogOptions.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InfoLink;
    ```
- `public string Message { get; set; }`
  - Summary: Text shown at the bottom of the dialog box between the buttons or null to use the default value
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialogOptions.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Message;
    ```
- `public string ProcessType { get; set; }`
  - Summary: Type of processes that can be attached to. Shown in the title bar, eg. "Unity" or null to not show anything
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialogOptions.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessType;
    ```
- `public string Title { get; set; }`
  - Summary: Gets the title or null to use the default title
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialogOptions.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Title;
    ```
- `public string[] ProviderNames { get; set; }`
  - Summary: names, see or null to check every provider
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Attach/Dialogs/ShowAttachToProcessDialogOptions.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProviderNames;
    ```

