# Namespace `dnSpy.Contracts.Hex.Classification.DnSpy`

## Class `HexTextElementCreator`

Creates text elements that can be shown in tooltips

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Classification.DnSpy.HexTextElementCreator();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/DnSpy/HexTextElementCreator.cs` (line 28)

### Constructors

- `protected HexTextElementCreator()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/DnSpy/HexTextElementCreator.cs` (line 32)

### Methods

- `public abstract FrameworkElement CreateTextElement(bool colorize = true, string tag = null)`
  - Summary: Creates the text element
  - Parameters:
    - `bool colorize` (default: `true`): true if it should be colorized
    - `string tag` (default: `null`): Tag (), can be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/DnSpy/HexTextElementCreator.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateTextElement(colorize: /* bool */, tag: /* string */);
    ```

### Properties

- `public abstract ITextColorWriter Writer { get; }`
  - Summary: Gets the writer
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/DnSpy/HexTextElementCreator.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Writer;
    ```
- `public abstract bool IsEmpty { get; }`
  - Summary: true if no text has been written to
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/DnSpy/HexTextElementCreator.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```

## Class `HexTextElementCreatorProvider`

Creates instances that can be used to create text elements shown in tooltips

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Classification.DnSpy.HexTextElementCreatorProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/DnSpy/HexTextElementCreatorProvider.cs` (line 25)

### Constructors

- `protected HexTextElementCreatorProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/DnSpy/HexTextElementCreatorProvider.cs` (line 29)

### Methods

- `public abstract HexTextElementCreator Create()`
  - Summary: Creates a using the default content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/DnSpy/HexTextElementCreatorProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```
- `public abstract HexTextElementCreator Create(string contentType)`
  - Summary: Creates a
  - Parameters:
    - `string contentType`: Content type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Classification/DnSpy/HexTextElementCreatorProvider.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(contentType: /* string */);
    ```

