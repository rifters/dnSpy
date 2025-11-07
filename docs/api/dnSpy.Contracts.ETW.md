# Namespace `dnSpy.Contracts.ETW`

## Class `DnSpyEventSource`

**Inherits/Implements:** `EventSource`

**Example**

```csharp
// Instantiate dnSpy.Contracts.ETW.DnSpyEventSource and call its members.
var instance = new dnSpy.Contracts.ETW.DnSpyEventSource(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 24)

### Methods

- `public void CompileStart()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.CompileStart();
    ```
- `public void CompileStop()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.CompileStop();
    ```
- `public void EditCodePatchModuleStart(string Filename)`
  - Parameters:
    - `string Filename`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.EditCodePatchModuleStart(Filename: /* string */);
    ```
- `public void EditCodePatchModuleStop(string Filename)`
  - Parameters:
    - `string Filename`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.EditCodePatchModuleStop(Filename: /* string */);
    ```
- `public void ExportToProjectStart()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.ExportToProjectStart();
    ```
- `public void ExportToProjectStop()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.ExportToProjectStop();
    ```
- `public void OpenFromGACStart()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.OpenFromGACStart();
    ```
- `public void OpenFromGACStop()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.OpenFromGACStop();
    ```
- `public void SaveDocumentsStart()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.SaveDocumentsStart();
    ```
- `public void SaveDocumentsStop()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.SaveDocumentsStop();
    ```
- `public void ShowDocumentTabContentStart()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowDocumentTabContentStart();
    ```
- `public void ShowDocumentTabContentStop()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowDocumentTabContentStop();
    ```
- `public void StartupStart()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 29)
  - Example:
    ```csharp
    // Example invocation
    instance.StartupStart();
    ```
- `public void StartupStop()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.StartupStop();
    ```

### Fields

- `public static readonly DnSpyEventSource Log = new DnSpyEventSource()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ETW/DnSpyEventSource.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ETW.DnSpyEventSource.Log;
    ```

