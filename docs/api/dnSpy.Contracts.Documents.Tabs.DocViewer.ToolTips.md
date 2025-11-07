# Namespace `dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips`

## Class `ExportDocumentViewerToolTipProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IDocumentViewerToolTipProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.ExportDocumentViewerToolTipProviderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProvider.cs` (line 47)

### Constructors

- `public ExportDocumentViewerToolTipProviderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProvider.cs` (line 50)
- `public ExportDocumentViewerToolTipProviderAttribute(double order)`
  - Summary: Constructor
  - Parameters:
    - `double order`: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProvider.cs` (line 56)

### Properties

- `public double Order { get; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProvider.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `ICodeToolTipProvider`

Creates code tooltips

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.ICodeToolTipProvider and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.ICodeToolTipProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipProvider.cs` (line 26)

### Methods

- `ICodeToolTipWriter CreateNewOutput()`
  - Summary: Creates a new output that is shown on a new line
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipProvider.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateNewOutput();
    ```
- `object Create()`
  - Summary: Creates the tooltip
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipProvider.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```
- `void SetImage(object @ref)`
  - Summary: Initializes with an image
  - Parameters:
    - `object @ref`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.SetImage(@ref: /* object */);
    ```

### Properties

- `ICodeToolTipWriter Output { get; }`
  - Summary: Gets the current output
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Output;
    ```
- `ImageReference? Image { get; set; }`
  - Summary: Sets the image that should be shown in the tooltip or null if none should be shown
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipProvider.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Image;
    ```

## Interface `ICodeToolTipWriter`

Writes tooltips

**Inherits/Implements:** `ITextColorWriter`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.ICodeToolTipWriter and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.ICodeToolTipWriter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipWriter.cs` (line 27)

### Methods

- `bool WriteXmlDoc(string xmlDoc)`
  - Summary: Writes an XML doc comment. Returns true if it was written, false otherwise
  - Parameters:
    - `string xmlDoc`: XML doc
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipWriter.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteXmlDoc(xmlDoc: /* string */);
    ```
- `bool WriteXmlDocGeneric(string xmlDoc, string gpName)`
  - Summary: Writes an XML doc generic. Returns true if it was written, false otherwise
  - Parameters:
    - `string xmlDoc`: XML doc
    - `string gpName`: Name of generic parameter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipWriter.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteXmlDocGeneric(xmlDoc: /* string */, gpName: /* string */);
    ```
- `bool WriteXmlDocParameter(string xmlDoc, string paramName)`
  - Summary: Writes an XML doc parameter. Returns true if it was written, false otherwise
  - Parameters:
    - `string xmlDoc`: XML doc
    - `string paramName`: Name of parameter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipWriter.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteXmlDocParameter(xmlDoc: /* string */, paramName: /* string */);
    ```
- `void Write(IClassificationType classificationType, string text)`
  - Summary: Writes text
  - Parameters:
    - `IClassificationType classificationType`: Classification type
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/ICodeToolTipWriter.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(classificationType: /* IClassificationType */, text: /* string */);
    ```

## Interface `IDocumentViewerToolTipProvider`

Creates tooltips. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.IDocumentViewerToolTipProvider and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.IDocumentViewerToolTipProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProvider.cs` (line 28)

### Methods

- `object Create(IDocumentViewerToolTipProviderContext context, object @ref)`
  - Summary: Creates a tooltip or returns null
  - Parameters:
    - `IDocumentViewerToolTipProviderContext context`: Context
    - `object @ref`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(context: /* IDocumentViewerToolTipProviderContext */, @ref: /* object */);
    ```

## Interface `IDocumentViewerToolTipProviderContext`

context

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.IDocumentViewerToolTipProviderContext and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.IDocumentViewerToolTipProviderContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProviderContext.cs` (line 26)

### Methods

- `ICodeToolTipProvider Create()`
  - Summary: Creates a instance that can be used to create the code tooltip
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProviderContext.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

### Properties

- `IDecompiler Decompiler { get; }`
  - Summary: Language to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProviderContext.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Decompiler;
    ```
- `IDocumentViewer DocumentViewer { get; }`
  - Summary: Document viewer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProviderContext.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DocumentViewer;
    ```

## Interface `IDocumentViewerToolTipProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.IDocumentViewerToolTipProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.Tabs.DocViewer.ToolTips.IDocumentViewerToolTipProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProvider.cs` (line 39)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/Tabs/DocViewer/ToolTips/IDocumentViewerToolTipProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

