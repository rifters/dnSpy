# Namespace `dnSpy.Text.MEF`

## Interface `IAdornmentLayersMetadata`

**Inherits/Implements:** `IOrderable`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IAdornmentLayersMetadata and call its members.
var instance = new dnSpy.Text.MEF.IAdornmentLayersMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 52)

### Properties

- `LayerKind LayerKind { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LayerKind;
    ```
- `bool IsOverlayLayer { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOverlayLayer;
    ```

## Interface `IClassificationFormatMetadata`

**Inherits/Implements:** `IEditorFormatMetadata`, `IOrderable`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IClassificationFormatMetadata and call its members.
var instance = new dnSpy.Text.MEF.IClassificationFormatMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 48)

### Properties

- `IEnumerable<string> ClassificationTypeNames { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ClassificationTypeNames;
    ```

## Interface `IClassificationTypeDefinitionMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IClassificationTypeDefinitionMetadata and call its members.
var instance = new dnSpy.Text.MEF.IClassificationTypeDefinitionMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 75)

### Properties

- `IEnumerable<string> BaseDefinition { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BaseDefinition;
    ```
- `string Name { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 79)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `IContentTypeAndTextViewRoleMetadata`

**Inherits/Implements:** `IContentTypeMetadata`, `ITextViewRoleMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IContentTypeAndTextViewRoleMetadata and call its members.
var instance = new dnSpy.Text.MEF.IContentTypeAndTextViewRoleMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 35)

## Interface `IContentTypeDefinitionMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IContentTypeDefinitionMetadata and call its members.
var instance = new dnSpy.Text.MEF.IContentTypeDefinitionMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 82)

### Properties

- `IEnumerable<string> BaseDefinition { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BaseDefinition;
    ```
- `string MimeType { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MimeType;
    ```
- `string Name { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `IDeferrableContentTypeAndTextViewRoleMetadata`

**Inherits/Implements:** `IContentTypeAndTextViewRoleMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IDeferrableContentTypeAndTextViewRoleMetadata and call its members.
var instance = new dnSpy.Text.MEF.IDeferrableContentTypeAndTextViewRoleMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 108)

### Properties

- `string OptionName { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 109)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OptionName;
    ```

## Interface `IEditorFormatMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IEditorFormatMetadata and call its members.
var instance = new dnSpy.Text.MEF.IEditorFormatMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 38)

### Properties

- `bool UserVisible { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UserVisible;
    ```
- `int Priority { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Priority;
    ```
- `string Name { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `IGlyphMarginMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IGlyphMarginMetadata and call its members.
var instance = new dnSpy.Text.MEF.IGlyphMarginMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 116)

### Properties

- `IEnumerable<string> GlyphMargins { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 117)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GlyphMargins;
    ```

## Interface `IGlyphMetadata`

**Inherits/Implements:** `ITaggerMetadata`, `IOrderable`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IGlyphMetadata and call its members.
var instance = new dnSpy.Text.MEF.IGlyphMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 124)

## Interface `IGlyphMouseProcessorProviderMetadata`

**Inherits/Implements:** `IGlyphMarginMetadata`, `IOrderableContentTypeMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IGlyphMouseProcessorProviderMetadata and call its members.
var instance = new dnSpy.Text.MEF.IGlyphMouseProcessorProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 121)

## Interface `IGlyphTextMarkerMouseProcessorProviderMetadata`

**Inherits/Implements:** `IOrderable`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IGlyphTextMarkerMouseProcessorProviderMetadata and call its members.
var instance = new dnSpy.Text.MEF.IGlyphTextMarkerMouseProcessorProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 127)

### Properties

- `IEnumerable<string> TextViewRoles { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 128)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewRoles;
    ```

## Interface `IMarginContextMenuHandlerProviderMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IMarginContextMenuHandlerProviderMetadata and call its members.
var instance = new dnSpy.Text.MEF.IMarginContextMenuHandlerProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 132)

### Properties

- `IEnumerable<string> TextViewRoles { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 133)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewRoles;
    ```
- `string MarginName { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 136)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MarginName;
    ```

## Interface `INamedTaggerMetadata`

**Inherits/Implements:** `ITaggerMetadata`, `INamedContentTypeMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.INamedTaggerMetadata and call its members.
var instance = new dnSpy.Text.MEF.INamedTaggerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 67)

## Interface `IOrderableContentTypeAndTextViewRoleMetadata`

**Inherits/Implements:** `IContentTypeAndTextViewRoleMetadata`, `IOrderable`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IOrderableContentTypeAndTextViewRoleMetadata and call its members.
var instance = new dnSpy.Text.MEF.IOrderableContentTypeAndTextViewRoleMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 60)

## Interface `IOrderableContentTypeMetadata`

**Inherits/Implements:** `IContentTypeMetadata`, `IOrderable`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IOrderableContentTypeMetadata and call its members.
var instance = new dnSpy.Text.MEF.IOrderableContentTypeMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 113)

## Interface `ITaggerMetadata`

**Inherits/Implements:** `IContentTypeMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.ITaggerMetadata and call its members.
var instance = new dnSpy.Text.MEF.ITaggerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 63)

### Properties

- `IEnumerable<Type> TagTypes { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TagTypes;
    ```

## Interface `ITextViewRoleMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.ITextViewRoleMetadata and call its members.
var instance = new dnSpy.Text.MEF.ITextViewRoleMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 31)

### Properties

- `IEnumerable<string> TextViewRoles { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewRoles;
    ```

## Interface `IViewTaggerMetadata`

**Inherits/Implements:** `INamedTaggerMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IViewTaggerMetadata and call its members.
var instance = new dnSpy.Text.MEF.IViewTaggerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 70)

### Properties

- `IEnumerable<string> TextViewRoles { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewRoles;
    ```

## Interface `IWpfTextViewMarginMetadata`

**Inherits/Implements:** `IOrderableContentTypeAndTextViewRoleMetadata`

**Example**

```csharp
// Instantiate dnSpy.Text.MEF.IWpfTextViewMarginMetadata and call its members.
var instance = new dnSpy.Text.MEF.IWpfTextViewMarginMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 92)

### Properties

- `GridUnitType GridUnitType { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 98)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GridUnitType;
    ```
- `IEnumerable<string> Replaces { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 104)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Replaces;
    ```
- `double GridCellLength { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 95)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GridCellLength;
    ```
- `string MarginContainer { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MarginContainer;
    ```
- `string OptionName { get; }`
  - Defined in: `dnSpy/dnSpy/Text/MEF/Metadata.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OptionName;
    ```

