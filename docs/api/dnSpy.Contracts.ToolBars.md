# Namespace `dnSpy.Contracts.ToolBars`

## Class `ExportToolBarButtonAttribute`

Exports a toolbar button ()

**Inherits/Implements:** `ExportToolBarItemAttribute`, `IToolBarButtonMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.ToolBars.ExportToolBarButtonAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 80)

### Constructors

- `public ExportToolBarButtonAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 83)

### Properties

- `public bool IsToggleButton { get; set; }`
  - Summary: true if it's a toggle button. If true, you must implement .
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 105)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsToggleButton;
    ```
- `public string Header { get; set; }`
  - Summary: Toolbar button header property value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 90)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Header;
    ```
- `public string Icon { get; set; }`
  - Summary: Icon name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 95)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Icon;
    ```
- `public string ToolTip { get; set; }`
  - Summary: Tooltip
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 100)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTip;
    ```

## Class `ExportToolBarItemAttribute`

ToolBar export attribute base class

**Inherits/Implements:** `ExportAttribute`, `IToolBarItemMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.ToolBars.ExportToolBarItemAttribute(contractType: /* Type */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 49)

### Constructors

- `protected ExportToolBarItemAttribute(Type contractType)`
  - Summary: Constructor
  - Parameters:
    - `Type contractType`: Contract type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 54)

### Properties

- `public double Order { get; set; }`
  - Summary: Order within the toolbar group ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string Group { get; set; }`
  - Summary: Group name, must be of the format "order,name" where order is a decimal number and the order of the group in this toolbar.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Group;
    ```
- `public string OwnerGuid { get; set; }`
  - Summary: Guid of owner toolbar or null to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OwnerGuid;
    ```

## Class `ExportToolBarObjectAttribute`

Exports a toolbar object ()

**Inherits/Implements:** `ExportToolBarItemAttribute`, `IToolBarObjectMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.ToolBars.ExportToolBarObjectAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarObject.cs` (line 46)

### Constructors

- `public ExportToolBarObjectAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarObject.cs` (line 49)

## Interface `IToolBarButton`

A button in the toolbar

**Inherits/Implements:** `IToolBarItem`

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolBars.IToolBarButton and call its members.
var instance = new dnSpy.Contracts.ToolBars.IToolBarButton(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 28)

### Methods

- `ImageReference? GetIcon(IToolBarItemContext context)`
  - Summary: Gets the icon or null to use the icon from the attribute
  - Parameters:
    - `IToolBarItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon(context: /* IToolBarItemContext */);
    ```
- `bool IsEnabled(IToolBarItemContext context)`
  - Summary: Returns true if the toolbar item is enabled and its method can be called.
  - Parameters:
    - `IToolBarItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* IToolBarItemContext */);
    ```
- `string GetHeader(IToolBarItemContext context)`
  - Summary: Gets the header or null to use the header from the attribute
  - Parameters:
    - `IToolBarItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHeader(context: /* IToolBarItemContext */);
    ```
- `string GetToolTip(IToolBarItemContext context)`
  - Summary: Gets the tooltip or null to use the tooltip from the attribute
  - Parameters:
    - `IToolBarItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.GetToolTip(context: /* IToolBarItemContext */);
    ```
- `void Execute(IToolBarItemContext context)`
  - Summary: Executes the command
  - Parameters:
    - `IToolBarItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(context: /* IToolBarItemContext */);
    ```

## Interface `IToolBarButtonMetadata`

Metadata

**Inherits/Implements:** `IToolBarItemMetadata`

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolBars.IToolBarButtonMetadata and call its members.
var instance = new dnSpy.Contracts.ToolBars.IToolBarButtonMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 66)

### Properties

- `bool IsToggleButton { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsToggleButton;
    ```
- `string Header { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Header;
    ```
- `string Icon { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Icon;
    ```
- `string ToolTip { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarButton.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTip;
    ```

## Interface `IToolBarItem`

A ToolBar item command

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolBars.IToolBarItem and call its members.
var instance = new dnSpy.Contracts.ToolBars.IToolBarItem(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 27)

### Methods

- `bool IsVisible(IToolBarItemContext context)`
  - Summary: Returns true if the toolbar item is visible in the toolbar
  - Parameters:
    - `IToolBarItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.IsVisible(context: /* IToolBarItemContext */);
    ```

## Interface `IToolBarItemContext`

context

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolBars.IToolBarItemContext and call its members.
var instance = new dnSpy.Contracts.ToolBars.IToolBarItemContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItemContext.cs` (line 26)

### Properties

- `Guid ToolBarGuid { get; }`
  - Summary: Gets the guid of the toolbar, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItemContext.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolBarGuid;
    ```

## Interface `IToolBarItemMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolBars.IToolBarItemMetadata and call its members.
var instance = new dnSpy.Contracts.ToolBars.IToolBarItemMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 37)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string Group { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Group;
    ```
- `string OwnerGuid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarItem.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OwnerGuid;
    ```

## Interface `IToolBarObject`

A toolbar object

**Inherits/Implements:** `IToolBarItem`

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolBars.IToolBarObject and call its members.
var instance = new dnSpy.Contracts.ToolBars.IToolBarObject(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarObject.cs` (line 29)

### Methods

- `object GetUIObject(IToolBarItemContext context, IInputElement commandTarget)`
  - Summary: Gets the UI object to place in the
  - Parameters:
    - `IToolBarItemContext context`: Context
    - `IInputElement commandTarget`: Command target for toolbar items, eg. the owner window, or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarObject.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetUIObject(context: /* IToolBarItemContext */, commandTarget: /* IInputElement */);
    ```

## Interface `IToolBarObjectMetadata`

Metadata

**Inherits/Implements:** `IToolBarItemMetadata`

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolBars.IToolBarObjectMetadata and call its members.
var instance = new dnSpy.Contracts.ToolBars.IToolBarObjectMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarObject.cs` (line 40)

## Interface `IToolBarToggleButton`

Implement this interface if is true

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolBars.IToolBarToggleButton and call its members.
var instance = new dnSpy.Contracts.ToolBars.IToolBarToggleButton(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarToggleButton.cs` (line 26)

### Methods

- `Binding GetBinding(IToolBarItemContext context)`
  - Summary: Gets the binding
  - Parameters:
    - `IToolBarItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/IToolBarToggleButton.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.GetBinding(context: /* IToolBarItemContext */);
    ```

## Class `ToolBarButtonBase`

Toolbar button base class (implements

**Inherits/Implements:** `IToolBarButton`

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolBars.ToolBarButtonBase and call its members.
var instance = new dnSpy.Contracts.ToolBars.ToolBarButtonBase(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonBase.cs` (line 26)

### Methods

- `public abstract void Execute(IToolBarItemContext context)`
  - Parameters:
    - `IToolBarItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonBase.cs` (line 28)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(context: /* IToolBarItemContext */);
    ```
- `public virtual ImageReference? GetIcon(IToolBarItemContext context)`
  - Parameters:
    - `IToolBarItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonBase.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon(context: /* IToolBarItemContext */);
    ```
- `public virtual bool IsEnabled(IToolBarItemContext context)`
  - Parameters:
    - `IToolBarItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonBase.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* IToolBarItemContext */);
    ```
- `public virtual bool IsVisible(IToolBarItemContext context)`
  - Parameters:
    - `IToolBarItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonBase.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.IsVisible(context: /* IToolBarItemContext */);
    ```
- `public virtual string GetHeader(IToolBarItemContext context)`
  - Parameters:
    - `IToolBarItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonBase.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHeader(context: /* IToolBarItemContext */);
    ```
- `public virtual string GetToolTip(IToolBarItemContext context)`
  - Parameters:
    - `IToolBarItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonBase.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetToolTip(context: /* IToolBarItemContext */);
    ```

## Class `ToolBarButtonCommand`

Toolbar button base class

**Inherits/Implements:** `ToolBarButtonBase`, `ICommandHolder`

**Example**

```csharp
var instance = new dnSpy.Contracts.ToolBars.ToolBarButtonCommand(realCommand: /* ICommand */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonCommand.cs` (line 27)

### Constructors

- `protected ToolBarButtonCommand(ICommand realCommand)`
  - Summary: Constructor
  - Parameters:
    - `ICommand realCommand`: Real command that gets executed the button is pressed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonCommand.cs` (line 37)

### Methods

- `public override bool IsEnabled(IToolBarItemContext context)`
  - Parameters:
    - `IToolBarItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonCommand.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* IToolBarItemContext */);
    ```
- `public override void Execute(IToolBarItemContext context)`
  - Parameters:
    - `IToolBarItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonCommand.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(context: /* IToolBarItemContext */);
    ```

### Properties

- `public ICommand Command { get; }`
  - Summary: Gets the real command
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarButtonCommand.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Command;
    ```

## Class `ToolBarConstants`

Constants

**Example**

```csharp
// Access dnSpy.Contracts.ToolBars.ToolBarConstants members directly without instantiation.
dnSpy.Contracts.ToolBars.ToolBarConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 24)

### Fields

- `public const string APP_TB_GUID = "DCDABF16-B5AF-484F-92FD-E852918BF367"`
  - Summary: Guid of app toolbar
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 26)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.APP_TB_GUID;
    ```
- `public const string GROUP_APP_TB_MAIN_ASMED_UNDO = "4000,6351DBFC-6D8D-4847-B3F2-BC376912B9C2"`
  - Summary: Group: App ToolBar: Main, Group: AsmEditor Undo/Redo
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.GROUP_APP_TB_MAIN_ASMED_UNDO;
    ```
- `public const string GROUP_APP_TB_MAIN_DEBUG = "5000,A0AFBC69-B6D1-46FE-96C8-EC380DEBE9AA"`
  - Summary: Group: App ToolBar: Main, Group: Debug
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.GROUP_APP_TB_MAIN_DEBUG;
    ```
- `public const string GROUP_APP_TB_MAIN_DEBUG_CONTINUE = "6000,47DB0753-CEB2-4D83-A5F2-4DBCFF108E67"`
  - Summary: Group: App ToolBar: Main, Group: Debug / Continue
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.GROUP_APP_TB_MAIN_DEBUG_CONTINUE;
    ```
- `public const string GROUP_APP_TB_MAIN_DEBUG_STEP = "7000,5B9EF354-4FB6-4C7D-A700-80A8BEC7FC52"`
  - Summary: Group: App ToolBar: Main, Group: Debug / Step
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.GROUP_APP_TB_MAIN_DEBUG_STEP;
    ```
- `public const string GROUP_APP_TB_MAIN_FULLSCREEN = "1000000,F32C7B0E-B9A6-4435-9C75-3FE653ED02AC"`
  - Summary: Group: App ToolBar: Main, Group: Full Screen
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.GROUP_APP_TB_MAIN_FULLSCREEN;
    ```
- `public const string GROUP_APP_TB_MAIN_LANGUAGE = "3000,C94CA2F0-3039-4BDD-BE67-B354E2A36CD6"`
  - Summary: Group: App ToolBar: Main, Group: Language
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.GROUP_APP_TB_MAIN_LANGUAGE;
    ```
- `public const string GROUP_APP_TB_MAIN_MENU = "0,03D902EE-D1E3-4F5E-B05C-982F6B3438B3"`
  - Summary: Group: App ToolBar: Main, Group: Menu
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.GROUP_APP_TB_MAIN_MENU;
    ```
- `public const string GROUP_APP_TB_MAIN_NAVIGATION = "1000,CB78D3F7-1CB1-4AC2-BDD2-731805C4DB5D"`
  - Summary: Group: App ToolBar: Main, Group: Back/Forward
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.GROUP_APP_TB_MAIN_NAVIGATION;
    ```
- `public const string GROUP_APP_TB_MAIN_OPEN = "2000,B9D638D4-E58A-4737-9F3F-47DCDADEDFE9"`
  - Summary: Group: App ToolBar: Main, Group: Open
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.GROUP_APP_TB_MAIN_OPEN;
    ```
- `public const string GROUP_APP_TB_MAIN_SEARCH = "8000,F8FB775B-7999-4A48-BE1C-C4314D009715"`
  - Summary: Group: App ToolBar: Main, Group: Search
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarConstants.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.ToolBars.ToolBarConstants.GROUP_APP_TB_MAIN_SEARCH;
    ```

## Class `ToolBarObjectBase`

Toolbar object base class

**Inherits/Implements:** `IToolBarObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolBars.ToolBarObjectBase and call its members.
var instance = new dnSpy.Contracts.ToolBars.ToolBarObjectBase(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarObjectBase.cs` (line 26)

### Methods

- `public abstract object GetUIObject(IToolBarItemContext context, IInputElement commandTarget)`
  - Parameters:
    - `IToolBarItemContext context`: Description not provided.
    - `IInputElement commandTarget`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarObjectBase.cs` (line 28)
  - Example:
    ```csharp
    // Example invocation
    instance.GetUIObject(context: /* IToolBarItemContext */, commandTarget: /* IInputElement */);
    ```
- `public bool IsVisible(IToolBarItemContext context)`
  - Parameters:
    - `IToolBarItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolBars/ToolBarObjectBase.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.IsVisible(context: /* IToolBarItemContext */);
    ```

