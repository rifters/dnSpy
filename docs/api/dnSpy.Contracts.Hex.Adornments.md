# Namespace `dnSpy.Contracts.Hex.Adornments`

## Class `HexToolTipProvider`

Shows tooltips

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Adornments.HexToolTipProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Adornments/HexToolTipProvider.cs` (line 26)

### Constructors

- `protected HexToolTipProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Adornments/HexToolTipProvider.cs` (line 30)

### Methods

- `public abstract void ClearToolTip()`
  - Summary: Closes the tooltip
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Adornments/HexToolTipProvider.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.ClearToolTip();
    ```
- `public abstract void ShowToolTip(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags, object toolTipContent, VSTA.PopupStyles style)`
  - Summary: Shows a tooltip
  - Parameters:
    - `HexBufferSpan bufferSpan`: Buffer span
    - `HexSpanSelectionFlags flags`: Selection flags
    - `object toolTipContent`: Tooltip content
    - `VSTA.PopupStyles style`: Popup style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Adornments/HexToolTipProvider.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowToolTip(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */, toolTipContent: /* object */, style: /* VSTA.PopupStyles */);
    ```
- `public void ShowToolTip(HexBufferSpan bufferSpan, HexSpanSelectionFlags flags, object toolTipContent)`
  - Summary: Shows a tooltip
  - Parameters:
    - `HexBufferSpan bufferSpan`: Buffer span
    - `HexSpanSelectionFlags flags`: Selection flags
    - `object toolTipContent`: Tooltip content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Adornments/HexToolTipProvider.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowToolTip(bufferSpan: /* HexBufferSpan */, flags: /* HexSpanSelectionFlags */, toolTipContent: /* object */);
    ```
- `public void ShowToolTip(HexBufferSpanSelection span, object toolTipContent)`
  - Summary: Shows a tooltip
  - Parameters:
    - `HexBufferSpanSelection span`: Span and selection flags
    - `object toolTipContent`: Tooltip content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Adornments/HexToolTipProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowToolTip(span: /* HexBufferSpanSelection */, toolTipContent: /* object */);
    ```
- `public void ShowToolTip(HexBufferSpanSelection span, object toolTipContent, VSTA.PopupStyles style)`
  - Summary: Shows a tooltip
  - Parameters:
    - `HexBufferSpanSelection span`: Span and selection flags
    - `object toolTipContent`: Tooltip content
    - `VSTA.PopupStyles style`: Popup style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Adornments/HexToolTipProvider.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowToolTip(span: /* HexBufferSpanSelection */, toolTipContent: /* object */, style: /* VSTA.PopupStyles */);
    ```

## Class `HexToolTipProviderFactory`

factory

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Adornments.HexToolTipProviderFactory();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Adornments/HexToolTipProviderFactory.cs` (line 26)

### Constructors

- `protected HexToolTipProviderFactory()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Adornments/HexToolTipProviderFactory.cs` (line 30)

### Methods

- `public abstract HexToolTipProvider GetToolTipProvider(HexView hexView)`
  - Summary: Gets the tooltip provider
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Adornments/HexToolTipProviderFactory.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetToolTipProvider(hexView: /* HexView */);
    ```

