# Namespace `dnSpy.Contracts.Output`

## Class `ExportOutputServiceListenerAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IOutputServiceListenerMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Output.ExportOutputServiceListenerAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputServiceListener.cs` (line 52)

### Constructors

- `public ExportOutputServiceListenerAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputServiceListener.cs` (line 55)
- `public ExportOutputServiceListenerAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputServiceListener.cs` (line 61)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputServiceListener.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `ICachedWriter`

Writes text to a buffer and flushes it when (or ) is called.

**Inherits/Implements:** `IOutputWriter`, `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Output.ICachedWriter and call its members.
var instance = new dnSpy.Contracts.Output.ICachedWriter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Output/ICachedWriter.cs` (line 27)

### Methods

- `void Flush()`
  - Summary: Flushes current output. This method gets called automatically by
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/ICachedWriter.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.Flush();
    ```

## Interface `IOutputService`

Output manager. Export an to get notified whenever the output window is first shown.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Output.IOutputService and call its members.
var instance = new dnSpy.Contracts.Output.IOutputService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputService.cs` (line 28)

### Methods

- `IOutputTextPane Create(Guid guid, string name, IContentType contentType = null)`
  - Summary: Creates a . Returns an existing one if it's already been created.
  - Parameters:
    - `Guid guid`: Guid of text pane
    - `string name`: Name shown in the UI
    - `IContentType contentType` (default: `null`): Content type or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputService.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(guid: /* Guid */, name: /* string */, contentType: /* IContentType */);
    ```
- `IOutputTextPane Create(Guid guid, string name, string contentType)`
  - Summary: Creates a . Returns an existing one if it's already been created.
  - Parameters:
    - `Guid guid`: Guid of text pane
    - `string name`: Name shown in the UI
    - `string contentType`: Content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputService.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(guid: /* Guid */, name: /* string */, contentType: /* string */);
    ```
- `IOutputTextPane GetTextPane(Guid guid)`
  - Summary: Returns a
  - Parameters:
    - `Guid guid`: Guid of text pane
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputService.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTextPane(guid: /* Guid */);
    ```
- `void Select(Guid guid)`
  - Summary: Selects a
  - Parameters:
    - `Guid guid`: Guid of text pane
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputService.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.Select(guid: /* Guid */);
    ```

## Interface `IOutputServiceListener`

Gets created when gets created. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Output.IOutputServiceListener and call its members.
var instance = new dnSpy.Contracts.Output.IOutputServiceListener(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputServiceListener.cs` (line 28)

## Interface `IOutputServiceListener2`

Gets created when gets created. Use to export an instance.

**Inherits/Implements:** `IOutputServiceListener`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Output.IOutputServiceListener2 and call its members.
var instance = new dnSpy.Contracts.Output.IOutputServiceListener2(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputServiceListener.cs` (line 35)

### Methods

- `void Initialize(IOutputService outputService)`
  - Summary: Called to initialize the instance
  - Parameters:
    - `IOutputService outputService`: Output service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputServiceListener.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Initialize(outputService: /* IOutputService */);
    ```

## Interface `IOutputServiceListenerMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Output.IOutputServiceListenerMetadata and call its members.
var instance = new dnSpy.Contracts.Output.IOutputServiceListenerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputServiceListener.cs` (line 44)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputServiceListener.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IOutputTextPane`

Writes to one of the output buffers

**Inherits/Implements:** `IOutputWriter`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Output.IOutputTextPane and call its members.
var instance = new dnSpy.Contracts.Output.IOutputTextPane(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputTextPane.cs` (line 26)

### Methods

- `ICachedWriter CreateWriter()`
  - Summary: Creates a new instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputTextPane.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateWriter();
    ```
- `string GetText()`
  - Summary: Gets all text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputTextPane.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.GetText();
    ```
- `void Clear()`
  - Summary: Clears all text in the buffer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputTextPane.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```

### Properties

- `Guid Guid { get; }`
  - Summary: Guid of writer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputTextPane.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```

## Interface `IOutputWriter`

Writes text to a

**Inherits/Implements:** `ITextColorWriter`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Output.IOutputWriter and call its members.
var instance = new dnSpy.Contracts.Output.IOutputWriter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputWriter.cs` (line 27)

### Methods

- `void Write(IEnumerable<ColorAndText> text)`
  - Summary: Writes text
  - Parameters:
    - `IEnumerable<ColorAndText> text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputWriter.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* IEnumerable<ColorAndText> */);
    ```
- `void WriteLine(TextColor color, string text)`
  - Summary: Writes text
  - Parameters:
    - `TextColor color`: Color
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputWriter.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLine(color: /* TextColor */, text: /* string */);
    ```
- `void WriteLine(object color, string text)`
  - Summary: Writes text
  - Parameters:
    - `object color`: Color
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Output/IOutputWriter.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLine(color: /* object */, text: /* string */);
    ```

