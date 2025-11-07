# Namespace `dnSpy.Hex.MEF`

## Interface `IAdornmentLayersMetadata`

**Inherits/Implements:** `VSUTIL.IOrderable`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.IAdornmentLayersMetadata and call its members.
var instance = new dnSpy.Hex.MEF.IAdornmentLayersMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 43)

### Properties

- `HexLayerKind LayerKind { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LayerKind;
    ```
- `bool IsOverlayLayer { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOverlayLayer;
    ```

## Interface `IDeferrableTextViewRoleMetadata`

**Inherits/Implements:** `ITextViewRoleMetadata`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.IDeferrableTextViewRoleMetadata and call its members.
var instance = new dnSpy.Hex.MEF.IDeferrableTextViewRoleMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 82)

### Properties

- `string OptionName { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OptionName;
    ```

## Interface `IGlyphMarginMetadata`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.IGlyphMarginMetadata and call its members.
var instance = new dnSpy.Hex.MEF.IGlyphMarginMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 87)

### Properties

- `IEnumerable<string> GlyphMargins { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GlyphMargins;
    ```

## Interface `IGlyphMetadata`

**Inherits/Implements:** `ITaggerMetadata`, `VSUTIL.IOrderable`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.IGlyphMetadata and call its members.
var instance = new dnSpy.Hex.MEF.IGlyphMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 95)

## Interface `IGlyphMouseProcessorProviderMetadata`

**Inherits/Implements:** `IGlyphMarginMetadata`, `VSUTIL.IOrderable`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.IGlyphMouseProcessorProviderMetadata and call its members.
var instance = new dnSpy.Hex.MEF.IGlyphMouseProcessorProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 92)

## Interface `IMarginContextMenuHandlerProviderMetadata`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.IMarginContextMenuHandlerProviderMetadata and call its members.
var instance = new dnSpy.Hex.MEF.IMarginContextMenuHandlerProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 98)

### Properties

- `IEnumerable<string> TextViewRoles { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 99)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewRoles;
    ```
- `string MarginName { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MarginName;
    ```

## Interface `INameAndReplacesMetadata`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.INameAndReplacesMetadata and call its members.
var instance = new dnSpy.Hex.MEF.INameAndReplacesMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 35)

### Properties

- `IEnumerable<string> Replaces { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Replaces;
    ```
- `string Name { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `INamedTaggerMetadata`

**Inherits/Implements:** `ITaggerMetadata`, `INameAndReplacesMetadata`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.INamedTaggerMetadata and call its members.
var instance = new dnSpy.Hex.MEF.INamedTaggerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 58)

## Interface `IOrderableTextViewRoleMetadata`

**Inherits/Implements:** `ITextViewRoleMetadata`, `VSUTIL.IOrderable`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.IOrderableTextViewRoleMetadata and call its members.
var instance = new dnSpy.Hex.MEF.IOrderableTextViewRoleMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 51)

## Interface `ITaggerMetadata`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.ITaggerMetadata and call its members.
var instance = new dnSpy.Hex.MEF.ITaggerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 54)

### Properties

- `IEnumerable<Type> TagTypes { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TagTypes;
    ```

## Interface `ITextViewRoleMetadata`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.ITextViewRoleMetadata and call its members.
var instance = new dnSpy.Hex.MEF.ITextViewRoleMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 31)

### Properties

- `IEnumerable<string> TextViewRoles { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewRoles;
    ```

## Interface `IViewTaggerMetadata`

**Inherits/Implements:** `INamedTaggerMetadata`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.IViewTaggerMetadata and call its members.
var instance = new dnSpy.Hex.MEF.IViewTaggerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 61)

### Properties

- `IEnumerable<string> TextViewRoles { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewRoles;
    ```

## Interface `IWpfHexViewMarginMetadata`

**Inherits/Implements:** `IOrderableTextViewRoleMetadata`

**Example**

```csharp
// Instantiate dnSpy.Hex.MEF.IWpfHexViewMarginMetadata and call its members.
var instance = new dnSpy.Hex.MEF.IWpfHexViewMarginMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 66)

### Properties

- `GridUnitType GridUnitType { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GridUnitType;
    ```
- `IEnumerable<string> Replaces { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Replaces;
    ```
- `double GridCellLength { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GridCellLength;
    ```
- `string MarginContainer { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MarginContainer;
    ```
- `string OptionName { get; }`
  - Defined in: `dnSpy/dnSpy/Hex/MEF/Metadata.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OptionName;
    ```

