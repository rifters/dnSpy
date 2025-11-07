# Namespace `dnSpy.Contracts.Debugger.Breakpoints.Code.Dialogs`

## Class `ShowCodeBreakpointSettingsService`

Shows the breakpoint settings dialog box

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.Breakpoints.Code.Dialogs.ShowCodeBreakpointSettingsService and call its members.
var instance = new dnSpy.Contracts.Debugger.Breakpoints.Code.Dialogs.ShowCodeBreakpointSettingsService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/Dialogs/ShowCodeBreakpointSettingsService.cs` (line 26)

### Methods

- `public abstract DbgCodeBreakpointSettings? Show(DbgCodeBreakpointSettings settings)`
  - Summary: Shows the breakpoint settings dialog box and returns the new settings or null if the user canceled
  - Parameters:
    - `DbgCodeBreakpointSettings settings`: Settings to edit
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/Dialogs/ShowCodeBreakpointSettingsService.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(settings: /* DbgCodeBreakpointSettings */);
    ```
- `public abstract void Edit(DbgCodeBreakpoint[] breakpoints)`
  - Summary: Edits breakpoint settings and writes the new settings to
  - Parameters:
    - `DbgCodeBreakpoint[] breakpoints`: Breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/Dialogs/ShowCodeBreakpointSettingsService.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.Edit(breakpoints: /* DbgCodeBreakpoint[] */);
    ```
- `public void Edit(DbgCodeBreakpoint breakpoint)`
  - Summary: Edits a breakpoint's settings
  - Parameters:
    - `DbgCodeBreakpoint breakpoint`: Breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/Breakpoints/Code/Dialogs/ShowCodeBreakpointSettingsService.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.Edit(breakpoint: /* DbgCodeBreakpoint */);
    ```

