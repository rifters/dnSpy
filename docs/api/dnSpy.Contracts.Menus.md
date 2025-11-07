# Namespace `dnSpy.Contracts.Menus`

## Class `CommandTargetMenuItemBase`

A menu item base class for commands

**Inherits/Implements:** `MenuItemBase`

**Example**

```csharp
var instance = new dnSpy.Contracts.Menus.CommandTargetMenuItemBase(cmdId: /* StandardIds */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 27)

### Constructors

- `protected CommandTargetMenuItemBase(Guid group, int cmdId)`
  - Summary: Constructor
  - Parameters:
    - `Guid group`: Command group, eg.
    - `int cmdId`: Command ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 52)
- `protected CommandTargetMenuItemBase(StandardIds cmdId)`
  - Summary: Constructor
  - Parameters:
    - `StandardIds cmdId`: Command id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 35)
- `protected CommandTargetMenuItemBase(TextEditorIds cmdId)`
  - Summary: Constructor
  - Parameters:
    - `TextEditorIds cmdId`: Command id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 43)

### Methods

- `protected abstract ICommandTarget GetCommandTarget(IMenuItemContext context)`
  - Summary: Returns the or null if none
  - Parameters:
    - `IMenuItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCommandTarget(context: /* IMenuItemContext */);
    ```
- `public override bool IsEnabled(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* IMenuItemContext */);
    ```
- `public override bool IsVisible(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.IsVisible(context: /* IMenuItemContext */);
    ```
- `public override void Execute(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(context: /* IMenuItemContext */);
    ```

## Class `CommandTargetMenuItemBase<TContext>`

A menu item base class for commands

**Inherits/Implements:** `MenuItemBase<TContext>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Menus.CommandTargetMenuItemBase<TContext>(cmdId: /* StandardIds */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 77)

### Constructors

- `protected CommandTargetMenuItemBase(Guid group, int cmdId)`
  - Summary: Constructor
  - Parameters:
    - `Guid group`: Command group, eg.
    - `int cmdId`: Command ID
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 102)
- `protected CommandTargetMenuItemBase(StandardIds cmdId)`
  - Summary: Constructor
  - Parameters:
    - `StandardIds cmdId`: Command id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 85)
- `protected CommandTargetMenuItemBase(TextEditorIds cmdId)`
  - Summary: Constructor
  - Parameters:
    - `TextEditorIds cmdId`: Command id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 93)

### Methods

- `protected abstract ICommandTarget GetCommandTarget(TContext context)`
  - Summary: Returns the or null if none
  - Parameters:
    - `TContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 112)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCommandTarget(context: /* TContext */);
    ```
- `public override bool IsEnabled(TContext context)`
  - Parameters:
    - `TContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 118)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* TContext */);
    ```
- `public override bool IsVisible(TContext context)`
  - Parameters:
    - `TContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.IsVisible(context: /* TContext */);
    ```
- `public override void Execute(TContext context)`
  - Parameters:
    - `TContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CommandTargetMenuItemBase.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(context: /* TContext */);
    ```

## Struct `CreatedMenuItem`

info

**Example**

```csharp
var instance = new dnSpy.Contracts.Menus.CreatedMenuItem(md: /* IMenuItemMetadata */, menuItem: /* IMenuItem */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/CreatedMenuItem.cs` (line 24)

### Constructors

- `public CreatedMenuItem(IMenuItemMetadata md, IMenuItem menuItem)`
  - Summary: Constructor
  - Parameters:
    - `IMenuItemMetadata md`: Metadata, eg. an instance
    - `IMenuItem menuItem`: Menu item
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CreatedMenuItem.cs` (line 40)

### Properties

- `public IMenuItem MenuItem { get; }`
  - Summary: Menu item
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CreatedMenuItem.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MenuItem;
    ```
- `public IMenuItemMetadata Metadata { get; }`
  - Summary: Metadata, eg. an instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/CreatedMenuItem.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Metadata;
    ```

## Class `ExportMenuAttribute`

Exports a menu ()

**Inherits/Implements:** `ExportAttribute`, `IMenuMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Menus.ExportMenuAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 45)

### Constructors

- `public ExportMenuAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 48)

### Properties

- `public double Order { get; set; }`
  - Summary: Order within the menu, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string Guid { get; set; }`
  - Summary: Guid of this item
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public string Header { get; set; }`
  - Summary: Menu header, eg. "_File"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Header;
    ```
- `public string OwnerGuid { get; set; }`
  - Summary: Guid of menu or null to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OwnerGuid;
    ```

## Class `ExportMenuItemAttribute`

Exports a menu item ()

**Inherits/Implements:** `ExportAttribute`, `IMenuItemMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Menus.ExportMenuItemAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 102)

### Constructors

- `public ExportMenuItemAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 105)

### Properties

- `public double Order { get; set; }`
  - Summary: Order within the menu group ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 128)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `public string Group { get; set; }`
  - Summary: Group name, must be of the format "order,name" where order is a decimal number and the order of the group in this menu.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 123)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Group;
    ```
- `public string Guid { get; set; }`
  - Summary: Guid of this item or null if it can't contain any child items
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 117)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public string Header { get; set; }`
  - Summary: Menu item header property value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 133)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Header;
    ```
- `public string Icon { get; set; }`
  - Summary: Icon name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 143)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Icon;
    ```
- `public string InputGestureText { get; set; }`
  - Summary: Menu item input gesture text property value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 138)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InputGestureText;
    ```
- `public string OwnerGuid { get; set; }`
  - Summary: Guid of owner menu or menu item. null if it's a context menu ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 112)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OwnerGuid;
    ```

## Struct `GuidObject`

Object with a

**Example**

```csharp
var instance = new dnSpy.Contracts.Menus.GuidObject(guid: /* string */, obj: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/GuidObject.cs` (line 26)

### Constructors

- `public GuidObject(Guid guid, object obj)`
  - Summary: Constructor
  - Parameters:
    - `Guid guid`: Guid of object (eg. )
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/GuidObject.cs` (line 48)
- `public GuidObject(string guid, object obj)`
  - Summary: Constructor
  - Parameters:
    - `string guid`: Guid of object (eg. )
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/GuidObject.cs` (line 38)

### Properties

- `public Guid Guid { get; }`
  - Summary: Guid of object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/GuidObject.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public object Object { get; }`
  - Summary: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/GuidObject.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Object;
    ```

## Struct `GuidObjectsProviderArgs`

Data passed to

**Example**

```csharp
var instance = new dnSpy.Contracts.Menus.GuidObjectsProviderArgs(creatorObject: /* GuidObject */, openedFromKeyboard: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/GuidObjectsProviderArgs.cs` (line 24)

### Constructors

- `public GuidObjectsProviderArgs(GuidObject creatorObject, bool openedFromKeyboard)`
  - Summary: Constructor
  - Parameters:
    - `GuidObject creatorObject`: The owner object ()
    - `bool openedFromKeyboard`: true if it was opened from the keyboard
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/GuidObjectsProviderArgs.cs` (line 40)

### Properties

- `public GuidObject CreatorObject { get; }`
  - Summary: The owner object ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/GuidObjectsProviderArgs.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CreatorObject;
    ```
- `public bool OpenedFromKeyboard { get; }`
  - Summary: true if it was opened from the keyboard
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/GuidObjectsProviderArgs.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OpenedFromKeyboard;
    ```

## Interface `IContextMenuInitializer`

Implement it to change where the context menu should appear inside of a control

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.IContextMenuInitializer and call its members.
var instance = new dnSpy.Contracts.Menus.IContextMenuInitializer(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IContextMenuInitializer.cs` (line 26)

### Methods

- `void Initialize(IMenuItemContext context, ContextMenu menu)`
  - Summary: Initializes a context menu
  - Parameters:
    - `IMenuItemContext context`: Context
    - `ContextMenu menu`: Context menu
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IContextMenuInitializer.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Initialize(context: /* IMenuItemContext */, menu: /* ContextMenu */);
    ```

## Interface `IContextMenuProvider`

Shows context menus

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.IContextMenuProvider and call its members.
var instance = new dnSpy.Contracts.Menus.IContextMenuProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IContextMenuProvider.cs` (line 26)

### Methods

- `void Show(FrameworkElement elem)`
  - Summary: Shows the context menu
  - Parameters:
    - `FrameworkElement elem`: Element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IContextMenuProvider.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.Show(elem: /* FrameworkElement */);
    ```

## Interface `IGuidObjectsProvider`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.IGuidObjectsProvider and call its members.
var instance = new dnSpy.Contracts.Menus.IGuidObjectsProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IGuidObjectsProvider.cs` (line 26)

### Methods

- `IEnumerable<GuidObject> GetGuidObjects(GuidObjectsProviderArgs args)`
  - Summary: Gets extra s to add to
  - Parameters:
    - `GuidObjectsProviderArgs args`: Args
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IGuidObjectsProvider.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGuidObjects(args: /* GuidObjectsProviderArgs */);
    ```

## Interface `IMenu`

A menu

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.IMenu and call its members.
var instance = new dnSpy.Contracts.Menus.IMenu(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 27)

## Interface `IMenuItem`

A menu item command

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.IMenuItem and call its members.
var instance = new dnSpy.Contracts.Menus.IMenuItem(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 28)

### Methods

- `ImageReference? GetIcon(IMenuItemContext context)`
  - Summary: Gets the menu item icon or null if the default icon from the attribute should be used.
  - Parameters:
    - `IMenuItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon(context: /* IMenuItemContext */);
    ```
- `bool IsChecked(IMenuItemContext context)`
  - Summary: Returns true if the menu item is checked
  - Parameters:
    - `IMenuItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.IsChecked(context: /* IMenuItemContext */);
    ```
- `bool IsEnabled(IMenuItemContext context)`
  - Summary: Returns true if the menu item is enabled and its method can be called.
  - Parameters:
    - `IMenuItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* IMenuItemContext */);
    ```
- `bool IsVisible(IMenuItemContext context)`
  - Summary: Returns true if the menu item is visible in the menu
  - Parameters:
    - `IMenuItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.IsVisible(context: /* IMenuItemContext */);
    ```
- `string GetHeader(IMenuItemContext context)`
  - Summary: Gets the menu item header or null if the default header from the attribute should be used.
  - Parameters:
    - `IMenuItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHeader(context: /* IMenuItemContext */);
    ```
- `string GetInputGestureText(IMenuItemContext context)`
  - Summary: Gets the menu item input gesture text or null if the default input gesture text from the attribute should be used.
  - Parameters:
    - `IMenuItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.GetInputGestureText(context: /* IMenuItemContext */);
    ```
- `void Execute(IMenuItemContext context)`
  - Summary: Executes the command
  - Parameters:
    - `IMenuItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(context: /* IMenuItemContext */);
    ```

## Interface `IMenuItemContext`

context

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.IMenuItemContext and call its members.
var instance = new dnSpy.Contracts.Menus.IMenuItemContext(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItemContext.cs` (line 27)

### Methods

- `T Find<T>()`
  - Summary: Finds the first object of a certain type. Returns default({T}) if none was found
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItemContext.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.Find();
    ```
- `T GetOrCreateState<T>(object key, Func<T> createState) where T : class`
  - Summary: Gets or creates user state that can be saved in the context to prevent re-generating the same state when various methods get called.
  - Parameters:
    - `object key`: Key, eg. a guid or a static key in some base command class
    - `Func<T> createState`: Delegate that creates a new value if it hasn't been created yet
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItemContext.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateState(key: /* object */, createState: /* Func<T> */);
    ```

### Properties

- `Guid MenuGuid { get; }`
  - Summary: Gets the guid of the top-level menu, eg. or
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItemContext.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MenuGuid;
    ```
- `GuidObject CreatorObject { get; }`
  - Summary: Creator object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItemContext.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CreatorObject;
    ```
- `IEnumerable<GuidObject> GuidObjects { get; }`
  - Summary: All objects. is always the first one
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItemContext.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GuidObjects;
    ```
- `bool OpenedFromKeyboard { get; }`
  - Summary: true if it was opened from the keyboard, else mouse. If it's the main menu (and not a context menu), this will always be true.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItemContext.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OpenedFromKeyboard;
    ```

## Interface `IMenuItemMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.IMenuItemMetadata and call its members.
var instance = new dnSpy.Contracts.Menus.IMenuItemMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 82)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 90)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string Group { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Group;
    ```
- `string Guid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `string Header { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Header;
    ```
- `string Icon { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Icon;
    ```
- `string InputGestureText { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InputGestureText;
    ```
- `string OwnerGuid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItem.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OwnerGuid;
    ```

## Interface `IMenuItemProvider`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.IMenuItemProvider and call its members.
var instance = new dnSpy.Contracts.Menus.IMenuItemProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItemProvider.cs` (line 26)

### Methods

- `IEnumerable<CreatedMenuItem> Create(IMenuItemContext context)`
  - Summary: Returns an enumerable of s
  - Parameters:
    - `IMenuItemContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuItemProvider.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(context: /* IMenuItemContext */);
    ```

## Interface `IMenuMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.IMenuMetadata and call its members.
var instance = new dnSpy.Contracts.Menus.IMenuMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 31)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```
- `string Guid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `string Header { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Header;
    ```
- `string OwnerGuid { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenu.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OwnerGuid;
    ```

## Interface `IMenuService`

Menu manager

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.IMenuService and call its members.
var instance = new dnSpy.Contracts.Menus.IMenuService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuService.cs` (line 28)

### Methods

- `IContextMenuProvider InitializeContextMenu(FrameworkElement elem, Guid guid, IGuidObjectsProvider provider = null, IContextMenuInitializer initCtxMenu = null, Guid? ctxMenuGuid = null)`
  - Summary: Initializes a context menu. Should be called when has been created.
  - Parameters:
    - `FrameworkElement elem`: Element that needs a context menu
    - `Guid guid`: Guid of
    - `IGuidObjectsProvider provider` (default: `null`): A instance or null
    - `IContextMenuInitializer initCtxMenu` (default: `null`): A instance or null
    - `Guid? ctxMenuGuid` (default: `null`): Guid of context menu, default is
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuService.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializeContextMenu(elem: /* FrameworkElement */, guid: /* Guid */, provider: /* IGuidObjectsProvider */, initCtxMenu: /* IContextMenuInitializer */, ctxMenuGuid: /* Guid? */);
    ```
- `IContextMenuProvider InitializeContextMenu(FrameworkElement elem, string guid, IGuidObjectsProvider provider = null, IContextMenuInitializer initCtxMenu = null, string ctxMenuGuid = null)`
  - Summary: Initializes a context menu. Should be called when has been created.
  - Parameters:
    - `FrameworkElement elem`: Element that needs a context menu
    - `string guid`: Guid of
    - `IGuidObjectsProvider provider` (default: `null`): A instance or null
    - `IContextMenuInitializer initCtxMenu` (default: `null`): A instance or null
    - `string ctxMenuGuid` (default: `null`): Guid of context menu, default is
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuService.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializeContextMenu(elem: /* FrameworkElement */, guid: /* string */, provider: /* IGuidObjectsProvider */, initCtxMenu: /* IContextMenuInitializer */, ctxMenuGuid: /* string */);
    ```
- `Menu CreateMenu(Guid menuGuid, IInputElement commandTarget)`
  - Summary: Creates a
  - Parameters:
    - `Guid menuGuid`: Guid of menu, eg.
    - `IInputElement commandTarget`: Command target for menu items, eg. the owner window, or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/IMenuService.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateMenu(menuGuid: /* Guid */, commandTarget: /* IInputElement */);
    ```

## Class `MenuConstants`

Constants

**Example**

```csharp
// Access dnSpy.Contracts.Menus.MenuConstants members directly without instantiation.
dnSpy.Contracts.Menus.MenuConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 36)

### Fields

- `public const double ORDER_APP_MENU_DEBUG = 10000`
  - Summary: App menu order: Debug
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 80)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.ORDER_APP_MENU_DEBUG;
    ```
- `public const double ORDER_APP_MENU_EDIT = 1000`
  - Summary: App menu order: Edit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 74)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.ORDER_APP_MENU_EDIT;
    ```
- `public const double ORDER_APP_MENU_FILE = 0`
  - Summary: App menu order: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 71)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.ORDER_APP_MENU_FILE;
    ```
- `public const double ORDER_APP_MENU_HELP = 1001000`
  - Summary: App menu order: Help
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 86)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.ORDER_APP_MENU_HELP;
    ```
- `public const double ORDER_APP_MENU_VIEW = 2000`
  - Summary: App menu order: View
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 77)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.ORDER_APP_MENU_VIEW;
    ```
- `public const double ORDER_APP_MENU_WINDOW = 1000000`
  - Summary: App menu order: Window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 83)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.ORDER_APP_MENU_WINDOW;
    ```
- `public const string APP_MENU_DEBUG_GUID = "62B311D0-D77E-4718-86C3-14BA031C47DF"`
  - Summary: Guid of app menu: Debug
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.APP_MENU_DEBUG_GUID;
    ```
- `public const string APP_MENU_DEBUG_WINDOWS_GUID = "7F95892B-975D-4217-A497-2EB0504489F4"`
  - Summary: Guid of app menu: Debug \ Windows
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 62)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.APP_MENU_DEBUG_WINDOWS_GUID;
    ```
- `public const string APP_MENU_EDIT_GUID = "BC6AE088-F941-4F4B-B976-42A09866C94A"`
  - Summary: Guid of app menu: Edit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 47)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.APP_MENU_EDIT_GUID;
    ```
- `public const string APP_MENU_FILE_GUID = "DC3B8109-21BB-40E8-9999-FC6526C3DD15"`
  - Summary: Guid of app menu: File
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.APP_MENU_FILE_GUID;
    ```
- `public const string APP_MENU_GUID = "3D87660F-DA21-48B9-9022-C76F0E588E1F"`
  - Summary: Guid of app menu
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.APP_MENU_GUID;
    ```
- `public const string APP_MENU_HELP_GUID = "52504C1B-7C35-464A-A35D-6D9F59E035D9"`
  - Summary: Guid of app menu: Help
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 59)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.APP_MENU_HELP_GUID;
    ```
- `public const string APP_MENU_VIEW_BOOKMARKS_GUID = "69DBE925-ED20-43D5-B1EF-EBAB0BAE9E9A"`
  - Summary: Guid of app menu: View \ Bookmarks
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 65)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.APP_MENU_VIEW_BOOKMARKS_GUID;
    ```
- `public const string APP_MENU_VIEW_GUID = "235BDFD8-A065-4E89-B041-C40A90526AF9"`
  - Summary: Guid of app menu: View
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.APP_MENU_VIEW_GUID;
    ```
- `public const string APP_MENU_WINDOW_GUID = "5904BD1D-1EF3-424F-B531-FE6BCF2FC9D4"`
  - Summary: Guid of app menu: Window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 56)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.APP_MENU_WINDOW_GUID;
    ```
- `public const string CTX_MENU_GUID = "CB53CCAF-9EE3-411E-A03A-561E7D8470EC"`
  - Summary: Guid of context menu
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.CTX_MENU_GUID;
    ```
- `public const string GLYPHMARGIN_GUID = "53F9F2FF-5AF8-4FC6-B849-74AB88EFB367"`
  - Summary: Guid of glyph margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GLYPHMARGIN_GUID;
    ```
- `public const string GROUP_APP_MENU_BOOKMARKS_COMMANDS1 = "1000,F6008A3C-8EBF-459F-8446-6D96D02060DC"`
  - Summary: Group: App Menu: View \ Bookmarks, Group: Commands #1
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 245)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_BOOKMARKS_COMMANDS1;
    ```
- `public const string GROUP_APP_MENU_BOOKMARKS_COMMANDS2 = "2000,10E117AF-68CF-47ED-AEA9-80CDDEDA3C16"`
  - Summary: Group: App Menu: View \ Bookmarks, Group: Commands #2
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 248)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_BOOKMARKS_COMMANDS2;
    ```
- `public const string GROUP_APP_MENU_BOOKMARKS_COMMANDS3 = "3000,2E6C9563-FF9F-433B-B03A-A5CFA4228A78"`
  - Summary: Group: App Menu: View \ Bookmarks, Group: Commands #3
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 251)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_BOOKMARKS_COMMANDS3;
    ```
- `public const string GROUP_APP_MENU_BOOKMARKS_WINDOWS = "0,73401CB5-1573-4868-96C9-6141EF39F44F"`
  - Summary: Group: App Menu: View \ Bookmarks, Group: Windows
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 242)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_BOOKMARKS_WINDOWS;
    ```
- `public const string GROUP_APP_MENU_DEBUG_BREAKPOINTS = "3000,2684EC1B-45A7-4412-BCBF-81345845FF54"`
  - Summary: Group: App Menu: Debug, Group: Breakpoint commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 272)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_BREAKPOINTS;
    ```
- `public const string GROUP_APP_MENU_DEBUG_CONTINUE = "1000,E9AEB324-1425-4CBF-8998-B1796A16AA06"`
  - Summary: Group: App Menu: Debug, Group: Continue/Stop/etc commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 263)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_CONTINUE;
    ```
- `public const string GROUP_APP_MENU_DEBUG_OPTIONS = "1000000,F3B4A871-C8D8-40CA-A881-7BEF2328145C"`
  - Summary: Group: App Menu: Debug, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 275)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_OPTIONS;
    ```
- `public const string GROUP_APP_MENU_DEBUG_START = "0,118A7201-7560-443E-B2F6-7F6369A253A2"`
  - Summary: Group: App Menu: Debug, Group: Start
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 260)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_START;
    ```
- `public const string GROUP_APP_MENU_DEBUG_STEP = "2000,5667E48E-5E33-46E9-9661-98B979D65F5D"`
  - Summary: Group: App Menu: Debug, Group: Step commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 269)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_STEP;
    ```
- `public const string GROUP_APP_MENU_DEBUG_STEP_CURRENTPROCESS = "1999,D7C0F536-DD76-428C-8E87-A9D27D4C19A9"`
  - Summary: Group: App Menu: Debug, Group: Step (Current Process) commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 266)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_STEP_CURRENTPROCESS;
    ```
- `public const string GROUP_APP_MENU_DEBUG_WINDOWS = "-1000,B4D89733-91AC-4C2F-8808-3AEBD2A686C9"`
  - Summary: Group: App Menu: Debug, Group: Windows
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 257)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_WINDOWS;
    ```
- `public const string GROUP_APP_MENU_DEBUG_WINDOWS_INFO = "6000,2721D995-74E5-4AA8-9E32-FBB2EDCE768F"`
  - Summary: Group: App Menu: Debug \ Windows, Group: Info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 287)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_WINDOWS_INFO;
    ```
- `public const string GROUP_APP_MENU_DEBUG_WINDOWS_MEMORY = "7000,246D698C-04F2-4998-88FB-46853D62E290"`
  - Summary: Group: App Menu: Debug \ Windows, Group: Memory
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 290)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_WINDOWS_MEMORY;
    ```
- `public const string GROUP_APP_MENU_DEBUG_WINDOWS_MEMORY_SUB = "0,3B088B70-F2D6-4388-8B5D-397372CEAC9F"`
  - Summary: Group: App Menu: Debug \ Windows \ Memory, Group: Memory N
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 293)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_WINDOWS_MEMORY_SUB;
    ```
- `public const string GROUP_APP_MENU_DEBUG_WINDOWS_SETTINGS = "0,37136731-930E-4D87-8144-03DB3217668D"`
  - Summary: Group: App Menu: Debug \ Windows, Group: Settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 278)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_WINDOWS_SETTINGS;
    ```
- `public const string GROUP_APP_MENU_DEBUG_WINDOWS_VALUES = "3000,BC7F81CF-49A1-4F59-B789-56EEDAA375BE"`
  - Summary: Group: App Menu: Debug \ Windows, Group: Values
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 281)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_WINDOWS_VALUES;
    ```
- `public const string GROUP_APP_MENU_DEBUG_WINDOWS_WATCH_SUB = "0,2248FFD3-0377-4434-B293-378DDD605DF3"`
  - Summary: Group: App Menu: Debug \ Windows \ Watch, Group: Watch N
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 284)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_DEBUG_WINDOWS_WATCH_SUB;
    ```
- `public const string GROUP_APP_MENU_EDIT_ASMED_DELETE = "2000,F483414D-5CA0-4CE3-9FB2-BFB21987D9F4"`
  - Summary: Group: App Menu: Edit, Group: AsmEditor Delete
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 209)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_EDIT_ASMED_DELETE;
    ```
- `public const string GROUP_APP_MENU_EDIT_ASMED_MISC = "3000,3DCA360E-3CCD-4F27-AF50-A254CD5F9C83"`
  - Summary: Group: App Menu: Edit, Group: AsmEditor Misc
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 212)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_EDIT_ASMED_MISC;
    ```
- `public const string GROUP_APP_MENU_EDIT_ASMED_NEW = "4000,178A6FD0-2F22-466D-8F2E-664E5531F50B"`
  - Summary: Group: App Menu: Edit, Group: AsmEditor New
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 215)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_EDIT_ASMED_NEW;
    ```
- `public const string GROUP_APP_MENU_EDIT_ASMED_SETTINGS = "5000,69EA4DD7-8220-43A5-9812-F1EC221AD7D8"`
  - Summary: Group: App Menu: Edit, Group: AsmEditor Settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 218)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_EDIT_ASMED_SETTINGS;
    ```
- `public const string GROUP_APP_MENU_EDIT_FIND = "1000,240D24B1-1A37-41B8-8A9A-94CD72C08145"`
  - Summary: Group: App Menu: Edit, Group: Find
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 206)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_EDIT_FIND;
    ```
- `public const string GROUP_APP_MENU_EDIT_HEX = "6000,6D8CA476-8D3D-468E-A895-40F3A9D5A25C"`
  - Summary: Group: App Menu: Edit, Group: Hex
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 221)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_EDIT_HEX;
    ```
- `public const string GROUP_APP_MENU_EDIT_HEX_COPY = "9000,32791A7F-4CFC-49D2-B066-A611A9E362DB"`
  - Summary: Group: App Menu: Edit, Group: Hex Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 230)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_EDIT_HEX_COPY;
    ```
- `public const string GROUP_APP_MENU_EDIT_HEX_GOTO_MD = "8000,1E0213F3-0578-43D9-A12D-14AE30EFD0EA"`
  - Summary: Group: App Menu: Edit, Group: Hex MD Go To
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 227)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_EDIT_HEX_GOTO_MD;
    ```
- `public const string GROUP_APP_MENU_EDIT_HEX_MD = "7000,36F0A9CA-5D14-4F56-8F64-ED3628FB5F30"`
  - Summary: Group: App Menu: Edit, Group: Hex MD
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 224)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_EDIT_HEX_MD;
    ```
- `public const string GROUP_APP_MENU_EDIT_UNDO = "0,3DFFD4E1-CFD9-442D-B1E5-E1E98AB8766B"`
  - Summary: Group: App Menu: Edit, Group: Undo/Redo
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 203)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_EDIT_UNDO;
    ```
- `public const string GROUP_APP_MENU_FILE_EXIT = "1000000,6EBA065B-5A1E-4DD4-B91A-339F2D2ED66E"`
  - Summary: Group: App Menu: File, Group: Exit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 200)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_FILE_EXIT;
    ```
- `public const string GROUP_APP_MENU_FILE_OPEN = "1000,636D9C45-00A9-461F-8947-E01755929A5B"`
  - Summary: Group: App Menu: File, Group: Open
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 197)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_FILE_OPEN;
    ```
- `public const string GROUP_APP_MENU_FILE_SAVE = "0,557C4B2D-5966-41AF-BFCA-D0A36DB5D6D8"`
  - Summary: Group: App Menu: File, Group: Save
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 194)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_FILE_SAVE;
    ```
- `public const string GROUP_APP_MENU_HELP_ABOUT = "1000000,835F06B5-67FB-4D01-8920-9D9E2FED9238"`
  - Summary: Group: App Menu: Help, Group: About
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 314)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_HELP_ABOUT;
    ```
- `public const string GROUP_APP_MENU_HELP_LINKS = "0,35CCC7A7-D1C0-4F70-AAFC-7E7CD90B4735"`
  - Summary: Group: App Menu: Help, Group: Links
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 311)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_HELP_LINKS;
    ```
- `public const string GROUP_APP_MENU_THEMES_THEMES = "0,AAE0CE90-DB6E-4E8D-9E1B-9BF7ABBDBB32"`
  - Summary: Group: App Menu: Themes, Group: Themes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 254)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_THEMES_THEMES;
    ```
- `public const string GROUP_APP_MENU_VIEW_OPTS = "0,FCBA133F-F62B-4DB2-BEC9-5AE11C95873B"`
  - Summary: Group: App Menu: View, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 233)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_VIEW_OPTS;
    ```
- `public const string GROUP_APP_MENU_VIEW_OPTSDLG = "1000000,AAA7FF98-47CD-4ABF-8824-EE20A283EEB3"`
  - Summary: Group: App Menu: View, Group: Options dlg
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 239)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_VIEW_OPTSDLG;
    ```
- `public const string GROUP_APP_MENU_VIEW_WINDOWS = "1000,599D070A-521E-4A1B-80DB-62C9B0AB48FA"`
  - Summary: Group: App Menu: View, Group: Tool Windows
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 236)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_VIEW_WINDOWS;
    ```
- `public const string GROUP_APP_MENU_WINDOW_ALLWINDOWS = "1000000,0BBFA4E5-3C54-41E9-BC74-69ADDC09CECC"`
  - Summary: Group: App Menu: Window, Group: All Windows
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 308)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_WINDOW_ALLWINDOWS;
    ```
- `public const string GROUP_APP_MENU_WINDOW_TABGROUPS = "1000,3890B3CB-2DE5-4745-A8F8-61A379485345"`
  - Summary: Group: App Menu: Window, Group: Tab Groups
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 299)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_WINDOW_TABGROUPS;
    ```
- `public const string GROUP_APP_MENU_WINDOW_TABGROUPSCLOSE = "2000,11548593-C399-4EA8-B944-60603BE1FD4B"`
  - Summary: Group: App Menu: Window, Group: Tab Groups Close commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 302)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_WINDOW_TABGROUPSCLOSE;
    ```
- `public const string GROUP_APP_MENU_WINDOW_TABGROUPSVERT = "3000,7E948EE4-59EA-47F2-B1C8-C5A5DB6F13B9"`
  - Summary: Group: App Menu: Window, Group: Tab Groups Vert/Horiz commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 305)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_WINDOW_TABGROUPSVERT;
    ```
- `public const string GROUP_APP_MENU_WINDOW_WINDOW = "0,27A8834B-D6BF-4267-803D-15DECAFAEA05"`
  - Summary: Group: App Menu: Window, Group: Window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 296)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_APP_MENU_WINDOW_WINDOW;
    ```
- `public const string GROUP_CTX_ANALYZER_DEBUG = "2000,9DE7F11A-7F72-43E2-AB6E-E8E8587B956F"`
  - Summary: Group: Context Menu, Type: Analyzer, Group: Debug
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 422)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_ANALYZER_DEBUG;
    ```
- `public const string GROUP_CTX_ANALYZER_OPTIONS = "10000,FD6E5D84-A83C-4D0A-8A77-EE755DE76999"`
  - Summary: Group: Context Menu, Type: Analyzer, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 428)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_ANALYZER_OPTIONS;
    ```
- `public const string GROUP_CTX_ANALYZER_OTHER = "5000,A766D535-4069-4AF7-801E-F4B87A2D0F84"`
  - Summary: Group: Context Menu, Type: Analyzer, Group: Other
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 425)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_ANALYZER_OTHER;
    ```
- `public const string GROUP_CTX_ANALYZER_TABS = "0,BC8D4C75-B5BC-4964-9A3C-E9EE33F928B0"`
  - Summary: Group: Context Menu, Type: Analyzer, Group: Tabs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 416)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_ANALYZER_TABS;
    ```
- `public const string GROUP_CTX_ANALYZER_TOKENS = "1000,E3FB23EB-EFA8-4C80-ACCD-DCB714BBAFC7"`
  - Summary: Group: Context Menu, Type: Analyzer, Group: Tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 419)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_ANALYZER_TOKENS;
    ```
- `public const string GROUP_CTX_BOOKMARKS_CMDS1 = "3000,4287B6E2-256F-4A8A-9041-EA7BE393C18A"`
  - Summary: Group: Context Menu, Type: Bookmarks, Group: Commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 473)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_BOOKMARKS_CMDS1;
    ```
- `public const string GROUP_CTX_BOOKMARKS_CODE = "1000,3932F616-AD0B-4310-A4DE-678AF7E9C149"`
  - Summary: Group: Context Menu, Type: Bookmarks, Group: Code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 467)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_BOOKMARKS_CODE;
    ```
- `public const string GROUP_CTX_BOOKMARKS_COPY = "0,1633C2A1-5A65-41FF-B83D-E6B0E1B565EC"`
  - Summary: Group: Context Menu, Type: Bookmarks, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 464)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_BOOKMARKS_COPY;
    ```
- `public const string GROUP_CTX_BOOKMARKS_EXPORT = "5000,565EDE0D-4139-486E-A486-CD6B3657E5FF"`
  - Summary: Group: Context Menu, Type: Bookmarks, Group: Export
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 476)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_BOOKMARKS_EXPORT;
    ```
- `public const string GROUP_CTX_BOOKMARKS_OPTS = "10000,1D7EEE8F-CD29-4F4E-A4A8-6906680B0601"`
  - Summary: Group: Context Menu, Type: Bookmarks, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 479)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_BOOKMARKS_OPTS;
    ```
- `public const string GROUP_CTX_BOOKMARKS_SETTINGS = "2000,12AFA15C-7D72-41FB-A65C-92367D8091A2"`
  - Summary: Group: Context Menu, Type: Bookmarks, Group: Settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 470)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_BOOKMARKS_SETTINGS;
    ```
- `public const string GROUP_CTX_CODEEDITOR_COMPILE = "0,3920F03E-3345-4557-AEBC-11EF272C6D62"`
  - Summary: Group: Context Menu, Type: Code editor, Group: Compile
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 614)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_CODEEDITOR_COMPILE;
    ```
- `public const string GROUP_CTX_CODEEDITOR_COPY = "5000,3B7890A7-AF3C-4FA2-9554-B0FA65B9F767"`
  - Summary: Group: Context Menu, Type: Code editor, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 617)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_CODEEDITOR_COPY;
    ```
- `public const string GROUP_CTX_CODEEDITOR_FIND = "6000,CDE742E8-31DA-4D96-A641-73A36CCF0DC0"`
  - Summary: Group: Context Menu, Type: Code editor, Group: Find
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 620)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_CODEEDITOR_FIND;
    ```
- `public const string GROUP_CTX_DBG_CALLSTACK_BPS = "1500,C3FC3901-808B-472F-BB71-9AC7E75F1413"`
  - Summary: Group: Context Menu, Type: Debugger/CallStack, Group: Breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 518)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CALLSTACK_BPS;
    ```
- `public const string GROUP_CTX_DBG_CALLSTACK_COPY = "0,FA7DD7BA-CC6B-46F4-8838-F8015B586911"`
  - Summary: Group: Context Menu, Type: Debugger/CallStack, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 512)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CALLSTACK_COPY;
    ```
- `public const string GROUP_CTX_DBG_CALLSTACK_FRAME = "1000,5F24F714-41CB-4111-89C1-BCA9734115B0"`
  - Summary: Group: Context Menu, Type: Debugger/CallStack, Group: Frame
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 515)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CALLSTACK_FRAME;
    ```
- `public const string GROUP_CTX_DBG_CALLSTACK_HEXOPTS = "2000,66C60524-E129-491D-A8A8-7939B567BC3A"`
  - Summary: Group: Context Menu, Type: Debugger/CallStack, Group: Hex Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 521)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CALLSTACK_HEXOPTS;
    ```
- `public const string GROUP_CTX_DBG_CALLSTACK_OPTS = "3000,8B40E062-CACD-4BF0-BFE2-6003400E9DC8"`
  - Summary: Group: Context Menu, Type: Debugger/CallStack, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 524)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CALLSTACK_OPTS;
    ```
- `public const string GROUP_CTX_DBG_CODEBPS_CMDS1 = "2000,3F86C3D0-9FCF-4DF8-93D7-2C1D202DC22D"`
  - Summary: Group: Context Menu, Type: Debugger/Breakpoints, Group: Commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 491)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CODEBPS_CMDS1;
    ```
- `public const string GROUP_CTX_DBG_CODEBPS_CODE = "1000,5918522A-B51A-430D-8351-561FF0618AB3"`
  - Summary: Group: Context Menu, Type: Debugger/Breakpoints, Group: Code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 485)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CODEBPS_CODE;
    ```
- `public const string GROUP_CTX_DBG_CODEBPS_COPY = "0,FB604477-5E55-4B55-91A4-0E06762FED83"`
  - Summary: Group: Context Menu, Type: Debugger/Breakpoints, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 482)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CODEBPS_COPY;
    ```
- `public const string GROUP_CTX_DBG_CODEBPS_EXPORT = "4000,51A2286D-423B-447D-82B7-4A8AAE9D1203"`
  - Summary: Group: Context Menu, Type: Debugger/Breakpoints, Group: Export
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 494)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CODEBPS_EXPORT;
    ```
- `public const string GROUP_CTX_DBG_CODEBPS_OPTS = "10000,E326374F-8D4F-4CC4-B454-BB3F2C585299"`
  - Summary: Group: Context Menu, Type: Debugger/Breakpoints, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 497)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CODEBPS_OPTS;
    ```
- `public const string GROUP_CTX_DBG_CODEBPS_SETTINGS = "1500,466C6110-9CD4-4D64-B532-8DCFC61C01EC"`
  - Summary: Group: Context Menu, Type: Debugger/Breakpoints, Group: Settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 488)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_CODEBPS_SETTINGS;
    ```
- `public const string GROUP_CTX_DBG_EXCEPTIONS_ADD = "1000,27050687-6367-48C4-A036-E6E368965BB4"`
  - Summary: Group: Context Menu, Type: Debugger/Exceptions, Group: Add
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 530)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_EXCEPTIONS_ADD;
    ```
- `public const string GROUP_CTX_DBG_EXCEPTIONS_COPY = "0,836ECA3F-DD93-4843-B752-B81D4A67F1A7"`
  - Summary: Group: Context Menu, Type: Debugger/Exceptions, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 527)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_EXCEPTIONS_COPY;
    ```
- `public const string GROUP_CTX_DBG_EXCEPTIONS_OPTIONS = "5000,64A4FCD8-64BD-4435-84E3-5FD0F78BFFCF"`
  - Summary: Group: Context Menu, Type: Debugger/Exceptions, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 533)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_EXCEPTIONS_OPTIONS;
    ```
- `public const string GROUP_CTX_DBG_MODULEBPS_CMDS1 = "1000,F07E3763-5827-4DE1-95A3-EEBD224B711A"`
  - Summary: Group: Context Menu, Type: Debugger/Module Breakpoints, Group: Commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 503)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_MODULEBPS_CMDS1;
    ```
- `public const string GROUP_CTX_DBG_MODULEBPS_CMDS2 = "2000,2AE615AA-3786-424A-8C90-B028032DFD6C"`
  - Summary: Group: Context Menu, Type: Debugger/Module Breakpoints, Group: Commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 506)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_MODULEBPS_CMDS2;
    ```
- `public const string GROUP_CTX_DBG_MODULEBPS_COPY = "0,648E5B4C-BADE-4226-9B18-EE983438728E"`
  - Summary: Group: Context Menu, Type: Debugger/Module Breakpoints, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 500)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_MODULEBPS_COPY;
    ```
- `public const string GROUP_CTX_DBG_MODULEBPS_EXPORT = "4000,B6A97E72-7CAD-4C36-951A-A8BF1F9BCFBA"`
  - Summary: Group: Context Menu, Type: Debugger/Module Breakpoints, Group: Export
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 509)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_MODULEBPS_EXPORT;
    ```
- `public const string GROUP_CTX_DBG_MODULES_COPY = "0,A43EAAA4-2729-418A-B5B8-39237D2E998D"`
  - Summary: Group: Context Menu, Type: Debugger/Modules, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 551)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_MODULES_COPY;
    ```
- `public const string GROUP_CTX_DBG_MODULES_DIRS = "3000,84F6531F-567B-43F8-9251-5566244F00A7"`
  - Summary: Group: Context Menu, Type: Debugger/Modules, Group: Directories
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 560)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_MODULES_DIRS;
    ```
- `public const string GROUP_CTX_DBG_MODULES_GOTO = "1000,D981D937-B196-42F9-8AB8-FED62E3C4C43"`
  - Summary: Group: Context Menu, Type: Debugger/Modules, Group: Go To
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 554)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_MODULES_GOTO;
    ```
- `public const string GROUP_CTX_DBG_MODULES_HEXOPTS = "2000,4ABA3476-C88E-47F4-B299-46FE12C38AA3"`
  - Summary: Group: Context Menu, Type: Debugger/Modules, Group: Hex Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 557)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_MODULES_HEXOPTS;
    ```
- `public const string GROUP_CTX_DBG_MODULES_SAVE = "4000,1B07EE10-60B5-442A-9EC5-63C3D20F5A9E"`
  - Summary: Group: Context Menu, Type: Debugger/Modules, Group: Save
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 563)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_MODULES_SAVE;
    ```
- `public const string GROUP_CTX_DBG_PROCESSES_ATTACH = "4000,1F9D28D0-282B-46BB-9E2D-59703E28A5FF"`
  - Summary: Group: Context Menu, Type: Debugger/Processes, Group: Attach
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 587)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_PROCESSES_ATTACH;
    ```
- `public const string GROUP_CTX_DBG_PROCESSES_CONTINUE = "1000,3F9F65B7-A18C-4657-AED7-CBB521196C34"`
  - Summary: Group: Context Menu, Type: Debugger/Processes, Group: Continue/Break
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 578)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_PROCESSES_CONTINUE;
    ```
- `public const string GROUP_CTX_DBG_PROCESSES_COPY = "0,CC3C28D9-E9F7-448B-9299-31038143439F"`
  - Summary: Group: Context Menu, Type: Debugger/Processes, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 575)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_PROCESSES_COPY;
    ```
- `public const string GROUP_CTX_DBG_PROCESSES_OPTIONS = "3000,09039E26-03A2-453C-B164-F43DF8154D3F"`
  - Summary: Group: Context Menu, Type: Debugger/Processes, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 584)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_PROCESSES_OPTIONS;
    ```
- `public const string GROUP_CTX_DBG_PROCESSES_TERMINATE = "2000,276A37FE-50C8-4B56-BF56-4A0F414207DF"`
  - Summary: Group: Context Menu, Type: Debugger/Processes, Group: Detach/Terminate
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 581)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_PROCESSES_TERMINATE;
    ```
- `public const string GROUP_CTX_DBG_THREADS_CMDS = "2000,B7B20F2D-6FE1-4415-BC4A-D92B31EE9342"`
  - Summary: Group: Context Menu, Type: Debugger/Threads, Group: Commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 572)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_THREADS_CMDS;
    ```
- `public const string GROUP_CTX_DBG_THREADS_COPY = "0,F11E427D-6B88-44B9-ACFF-4D8AD8131DC0"`
  - Summary: Group: Context Menu, Type: Debugger/Threads, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 566)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_THREADS_COPY;
    ```
- `public const string GROUP_CTX_DBG_THREADS_HEXOPTS = "1000,960A6F14-846D-42EE-BD1E-4C1C91ECB21F"`
  - Summary: Group: Context Menu, Type: Debugger/Threads, Group: Hex Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 569)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_THREADS_HEXOPTS;
    ```
- `public const string GROUP_CTX_DBG_VARIABLES_WINDOW_COPY = "0,5DE1C544-8079-4C4E-ABB1-7CE34BDF6A94"`
  - Summary: Group: Context Menu, Type: Debugger/Variables window, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 536)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_VARIABLES_WINDOW_COPY;
    ```
- `public const string GROUP_CTX_DBG_VARIABLES_WINDOW_HEXOPTS = "2000,72E9B097-DD72-411E-B9FC-B01AE30EF24F"`
  - Summary: Group: Context Menu, Type: Debugger/Variables window, Group: Hex Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 542)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_VARIABLES_WINDOW_HEXOPTS;
    ```
- `public const string GROUP_CTX_DBG_VARIABLES_WINDOW_OPTS = "4000,93573019-549D-40EC-8B3C-D515DACB3C47"`
  - Summary: Group: Context Menu, Type: Debugger/Variables window, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 548)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_VARIABLES_WINDOW_OPTS;
    ```
- `public const string GROUP_CTX_DBG_VARIABLES_WINDOW_TREE = "3000,877A4CC7-3074-4EFF-9C6B-96D1203F55F5"`
  - Summary: Group: Context Menu, Type: Debugger/Variables window, Group: Tree
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 545)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_VARIABLES_WINDOW_TREE;
    ```
- `public const string GROUP_CTX_DBG_VARIABLES_WINDOW_VALUES = "1000,1A0FDB51-7DCC-4B18-A4BA-0A6A45A8B14A"`
  - Summary: Group: Context Menu, Type: Debugger/Variables window, Group: Values
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 539)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DBG_VARIABLES_WINDOW_VALUES;
    ```
- `public const string GROUP_CTX_DOCUMENTS_ASMED_DELETE = "2000,17B24EE5-C1C0-441D-9B6F-C7632AF4C539"`
  - Summary: Group: Context Menu, Type: Documents, Group: AsmEditor Delete
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 437)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_ASMED_DELETE;
    ```
- `public const string GROUP_CTX_DOCUMENTS_ASMED_ILED = "6000,9E0E8539-751E-47EA-A0E9-EAB3A45724E3"`
  - Summary: Group: Context Menu, Type: Documents, Group: AsmEditor IL ED
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 449)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_ASMED_ILED;
    ```
- `public const string GROUP_CTX_DOCUMENTS_ASMED_MISC = "3000,928EDD44-E4A9-4EA9-93FF-55709943A088"`
  - Summary: Group: Context Menu, Type: Documents, Group: AsmEditor Misc
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 440)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_ASMED_MISC;
    ```
- `public const string GROUP_CTX_DOCUMENTS_ASMED_NEW = "4000,05FD56B0-CAF9-48E1-9CED-5221E8A13140"`
  - Summary: Group: Context Menu, Type: Documents, Group: AsmEditor New
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 443)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_ASMED_NEW;
    ```
- `public const string GROUP_CTX_DOCUMENTS_ASMED_SAVE = "1000,9495E6B9-0C5C-484A-9354-A5D19A5010DE"`
  - Summary: Group: Context Menu, Type: Documents, Group: AsmEditor Save
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 434)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_ASMED_SAVE;
    ```
- `public const string GROUP_CTX_DOCUMENTS_ASMED_SETTINGS = "5000,2247C4DB-73B8-4926-96EB-1C16EAF4A3E4"`
  - Summary: Group: Context Menu, Type: Documents, Group: AsmEditor Settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 446)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_ASMED_SETTINGS;
    ```
- `public const string GROUP_CTX_DOCUMENTS_DEBUG = "10000,080A553F-F066-41DC-9CC6-B4CCF2C48675"`
  - Summary: Group: Context Menu, Type: Documents, Group: Debug
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 458)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_DEBUG;
    ```
- `public const string GROUP_CTX_DOCUMENTS_DEBUGRT = "9000,9A151E30-AC16-4745-A819-24AA199E82CB"`
  - Summary: Group: Context Menu, Type: Documents, Group: Debug RT
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 455)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_DEBUGRT;
    ```
- `public const string GROUP_CTX_DOCUMENTS_OTHER = "11000,15776535-8A1D-4255-8C3D-331163324C7C"`
  - Summary: Group: Context Menu, Type: Document, Group: Other
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 461)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_OTHER;
    ```
- `public const string GROUP_CTX_DOCUMENTS_TABS = "0,3FEF128B-8320-4ED0-B03B-0932FCCDA98E"`
  - Summary: Group: Context Menu, Type: Documents, Group: Tabs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 431)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_TABS;
    ```
- `public const string GROUP_CTX_DOCUMENTS_TOKENS = "7000,C98101AD-1A59-42AE-B446-16545F39DC7A"`
  - Summary: Group: Context Menu, Type: Documents, Group: Tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 452)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCUMENTS_TOKENS;
    ```
- `public const string GROUP_CTX_DOCVIEWER_ASMED_DELETE = "3000,7A3E4F42-37A5-4A85-B403-62E6CD091E1D"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: AsmEditor Delete
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 326)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_ASMED_DELETE;
    ```
- `public const string GROUP_CTX_DOCVIEWER_ASMED_ILED = "6000,5DD87F08-FB00-4D00-9503-29590A8079CE"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: AsmEditor IL ED
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 335)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_ASMED_ILED;
    ```
- `public const string GROUP_CTX_DOCVIEWER_ASMED_NEW = "4000,15776B90-55EF-4ABE-9EC8-FB4A1E49A76F"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: AsmEditor New
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 329)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_ASMED_NEW;
    ```
- `public const string GROUP_CTX_DOCVIEWER_ASMED_SAVE = "2000,57ED92C1-3292-47DD-99CD-FB777DDF1276"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: AsmEditor Save
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 323)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_ASMED_SAVE;
    ```
- `public const string GROUP_CTX_DOCVIEWER_ASMED_SETTINGS = "5000,4E4FF711-D262-452D-BA1A-38A6D9951CE2"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: AsmEditor Settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 332)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_ASMED_SETTINGS;
    ```
- `public const string GROUP_CTX_DOCVIEWER_DEBUG = "1000,46C39BDA-35F5-4416-AAE2-A2FE05645F79"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: Debug
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 320)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_DEBUG;
    ```
- `public const string GROUP_CTX_DOCVIEWER_DEBUGRT = "13000,5A9207C0-C0E5-464D-B7A2-FB29ADA9C090"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: Debug RT
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 350)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_DEBUGRT;
    ```
- `public const string GROUP_CTX_DOCVIEWER_EDITOR = "15000,FD52ABD1-6DB2-48C3-A5DB-809ECE5EBBB2"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: Editor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 356)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_EDITOR;
    ```
- `public const string GROUP_CTX_DOCVIEWER_HEX = "9000,81BEEEAD-9498-4AD5-B387-006E93FD4014"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: Hex
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 341)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_HEX;
    ```
- `public const string GROUP_CTX_DOCVIEWER_HEX_COPY = "12000,E18271DD-7571-4509-9A7D-37E283BCF7C2"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: Hex Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 347)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_HEX_COPY;
    ```
- `public const string GROUP_CTX_DOCVIEWER_HEX_MD = "10000,0BE33A51-E400-4E3D-9B48-FF91E4A78303"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: Hex MD
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 344)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_HEX_MD;
    ```
- `public const string GROUP_CTX_DOCVIEWER_OTHER = "14000,47308D41-FCAD-4518-9859-AD67C2B912BB"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: Other
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 353)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_OTHER;
    ```
- `public const string GROUP_CTX_DOCVIEWER_TABS = "0,3576E74B-8D4D-47EE-9925-462B1007C879"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: Tabs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 317)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_TABS;
    ```
- `public const string GROUP_CTX_DOCVIEWER_TOKENS = "7000,096957CB-B94D-4A47-AC6D-DBF4C63C6955"`
  - Summary: Group: Context Menu, Type: Document Viewer, Group: Tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 338)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_DOCVIEWER_TOKENS;
    ```
- `public const string GROUP_CTX_HEXVIEW_COPY = "99000,34DCFAE6-7D6A-428A-8E71-5151616A08A3"`
  - Summary: Group: Context Menu, Type: HexView, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 368)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_HEXVIEW_COPY;
    ```
- `public const string GROUP_CTX_HEXVIEW_EDIT = "1000,63AE7AC9-B507-4474-9BB3-9B64B2036D34"`
  - Summary: Group: Context Menu, Type: HexView, Group: Edit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 362)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_HEXVIEW_EDIT;
    ```
- `public const string GROUP_CTX_HEXVIEW_FIND = "101000,8BD504DA-A927-4CBC-9E77-C873560C530F"`
  - Summary: Group: Context Menu, Type: HexView, Group: Find
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 374)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_HEXVIEW_FIND;
    ```
- `public const string GROUP_CTX_HEXVIEW_MISC = "10000,73D6E16B-6AF4-4F6D-8515-6D63ECDBFA3F"`
  - Summary: Group: Context Menu, Type: HexView, Group: Misc
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 365)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_HEXVIEW_MISC;
    ```
- `public const string GROUP_CTX_HEXVIEW_OPTS = "100000,0794156A-1EDE-45EC-9C41-48E27DE14085"`
  - Summary: Group: Context Menu, Type: HexView, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 371)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_HEXVIEW_OPTS;
    ```
- `public const string GROUP_CTX_HEXVIEW_SHOW = "0,261BB98C-6C43-4258-9C4E-7A3702298DE0"`
  - Summary: Group: Context Menu, Type: HexView, Group: Show commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 359)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_HEXVIEW_SHOW;
    ```
- `public const string GROUP_CTX_OUTPUT_COPY = "0,7E2D36F5-9F04-411C-81B6-DD92B53A9D57"`
  - Summary: Group: Context Menu, Type: Output text editor, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 605)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_OUTPUT_COPY;
    ```
- `public const string GROUP_CTX_OUTPUT_SETTINGS = "1000,DF1E714B-B1E3-4B6F-948E-36C4B69AA649"`
  - Summary: Group: Context Menu, Type: Output text editor, Group: Settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 608)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_OUTPUT_SETTINGS;
    ```
- `public const string GROUP_CTX_OUTPUT_USER_COMMANDS = "2000,A48F98FE-5BA6-4023-A7E5-0C3D6AFCC10B"`
  - Summary: Group: Context Menu, Type: Output text editor, Group: User Commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 611)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_OUTPUT_USER_COMMANDS;
    ```
- `public const string GROUP_CTX_REPL_CLEAR = "2000,1B3A6F12-AB30-4750-AB62-BB34DE4D9D0C"`
  - Summary: Group: Context Menu, Type: REPL text editor, Group: Clear
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 596)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_REPL_CLEAR;
    ```
- `public const string GROUP_CTX_REPL_COPY = "1000,E246D458-5DBD-41A6-866B-948793A1D125"`
  - Summary: Group: Context Menu, Type: REPL text editor, Group: Copy
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 593)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_REPL_COPY;
    ```
- `public const string GROUP_CTX_REPL_RESET = "0,407111D9-B090-4151-83FF-2C01C3816DF3"`
  - Summary: Group: Context Menu, Type: REPL text editor, Group: Reset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 590)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_REPL_RESET;
    ```
- `public const string GROUP_CTX_REPL_SAVE = "3000,F2D18E19-FBA7-4DFF-A72D-B88C44DBFC43"`
  - Summary: Group: Context Menu, Type: REPL text editor, Group: Save
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 599)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_REPL_SAVE;
    ```
- `public const string GROUP_CTX_REPL_SETTINGS = "4000,0585159F-E555-433D-B854-42A36487B7C4"`
  - Summary: Group: Context Menu, Type: REPL text editor, Group: Settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 602)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_REPL_SETTINGS;
    ```
- `public const string GROUP_CTX_SEARCH_DEBUG = "2000,AC4A027D-7C4C-422A-A619-BF6DFF4DE7F9"`
  - Summary: Group: Context Menu, Type: Search, Group: Debug
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 407)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_SEARCH_DEBUG;
    ```
- `public const string GROUP_CTX_SEARCH_OPTIONS = "10000,2A261412-7DCD-4CD1-B936-783C67476E99"`
  - Summary: Group: Context Menu, Type: Search, Group: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 413)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_SEARCH_OPTIONS;
    ```
- `public const string GROUP_CTX_SEARCH_OTHER = "5000,255AE50D-3638-4128-808D-FC8910BA9279"`
  - Summary: Group: Context Menu, Type: Search, Group: Other
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 410)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_SEARCH_OTHER;
    ```
- `public const string GROUP_CTX_SEARCH_TABS = "0,249A0912-68BE-4468-931A-055726958EA4"`
  - Summary: Group: Context Menu, Type: Search, Group: Tabs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 401)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_SEARCH_TABS;
    ```
- `public const string GROUP_CTX_SEARCH_TOKENS = "1000,8B57D21D-8109-424A-A337-DB61BE361ED4"`
  - Summary: Group: Context Menu, Type: Search, Group: Tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 404)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_SEARCH_TOKENS;
    ```
- `public const string GROUP_CTX_TABS_CLOSE = "0,FABC0864-6B57-4C49-A1AF-6015F7CFB5F4"`
  - Summary: Group: Context Menu, Type: Tabs, Group: Close/New commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 377)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_TABS_CLOSE;
    ```
- `public const string GROUP_CTX_TABS_GROUPS = "1000,1F89B1F4-8A1F-41FC-8B19-AF3F36AE806E"`
  - Summary: Group: Context Menu, Type: Tabs, Group: Tab Groups
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 380)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_TABS_GROUPS;
    ```
- `public const string GROUP_CTX_TABS_GROUPSCLOSE = "2000,80871274-20F2-4A51-8697-C3439781CA40"`
  - Summary: Group: Context Menu, Type: Tabs, Group: Tab Groups Close commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 383)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_TABS_GROUPSCLOSE;
    ```
- `public const string GROUP_CTX_TABS_GROUPSVERT = "3000,15174C91-6EA8-47E3-880E-FCDF607974F1"`
  - Summary: Group: Context Menu, Type: Tabs, Group: Tab Groups Vert/Horiz commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 386)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_TABS_GROUPSVERT;
    ```
- `public const string GROUP_CTX_TOOLWINS_CLOSE = "0,D6F31BC9-2474-44B9-8786-D3044F6F402C"`
  - Summary: Group: Context Menu, Type: Tool Windows, Group: Close commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 389)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_TOOLWINS_CLOSE;
    ```
- `public const string GROUP_CTX_TOOLWINS_GROUPS = "1000,32E1C678-7889-499D-8BC3-C22160E7E2AC"`
  - Summary: Group: Context Menu, Type: Tool Windows, Group: Tab Groups
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 392)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_TOOLWINS_GROUPS;
    ```
- `public const string GROUP_CTX_TOOLWINS_GROUPSCLOSE = "2000,61D665C4-B55D-45BF-B592-85D174C0A1E7"`
  - Summary: Group: Context Menu, Type: Tool Windows, Group: Tab Groups Close commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 395)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_TOOLWINS_GROUPSCLOSE;
    ```
- `public const string GROUP_CTX_TOOLWINS_GROUPSVERT = "3000,3F438576-672F-4865-B581-759D5DC678D5"`
  - Summary: Group: Context Menu, Type: Tool Windows, Group: Tab Groups Vert/Horiz commands
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 398)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_CTX_TOOLWINS_GROUPSVERT;
    ```
- `public const string GROUP_GLYPHMARGIN_DEBUG_CODEBPS_EDIT = "5000,B31BDBFD-3C44-4D14-92E8-85141167696F"`
  - Summary: Group: Glyph margin, Type: Debugger/Breakpoints, Group: Edit
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 626)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_GLYPHMARGIN_DEBUG_CODEBPS_EDIT;
    ```
- `public const string GROUP_GLYPHMARGIN_DEBUG_CODEBPS_EXPORT = "10000,EEC8041B-DC23-4E50-BEBC-BB71AB36631D"`
  - Summary: Group: Glyph margin, Type: Debugger/Breakpoints, Group: Breakpoints
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 629)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_GLYPHMARGIN_DEBUG_CODEBPS_EXPORT;
    ```
- `public const string GROUP_GLYPHMARGIN_DEBUG_CODEBPS_SETTINGS = "0,FB70F59F-7507-43C1-AD7B-BCBDD60375F6"`
  - Summary: Group: Glyph margin, Type: Debugger/Breakpoints, Group: Settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 623)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GROUP_GLYPHMARGIN_DEBUG_CODEBPS_SETTINGS;
    ```
- `public static readonly string GUIDOBJ_ACTIVE_OUTPUT_TEXTPANE_GUID = "5787A5D8-80DE-437F-A44A-6FD0138DBB57"`
  - Summary: Active
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 179)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_ACTIVE_OUTPUT_TEXTPANE_GUID;
    ```
- `public static readonly string GUIDOBJ_ANALYZER_TREEVIEW_GUID = "4C7D6317-C84A-42E6-A582-FCE3ED35EBE6"`
  - Summary: Analyzer's treeview
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 95)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_ANALYZER_TREEVIEW_GUID;
    ```
- `public static readonly string GUIDOBJ_ASMEDITOR_HEXVIEW_GUID = "95F0CEE5-44D0-468A-B214-69F91B76A84C"`
  - Summary: Asm editor's hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 134)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_ASMEDITOR_HEXVIEW_GUID;
    ```
- `public static readonly string GUIDOBJ_BOOKMARK_GUID = "71BD1A39-50A8-43C2-B88A-8986D0C674B4"`
  - Summary: Bookmark
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 188)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_BOOKMARK_GUID;
    ```
- `public static readonly string GUIDOBJ_BREAKPOINT_GUID = "A229BFE6-0445-4B5C-9D4B-E590995B9D93"`
  - Summary: Breakpoint
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 185)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_BREAKPOINT_GUID;
    ```
- `public static readonly string GUIDOBJ_CODE_EDITOR_GUID = "297907F8-38BE-4C8C-90D1-3400BB0EB36E"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 182)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_CODE_EDITOR_GUID;
    ```
- `public static readonly string GUIDOBJ_CODE_REFERENCE_GUID = "751F4075-D420-4196-BCF0-A0149A8948A4"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 107)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_CODE_REFERENCE_GUID;
    ```
- `public static readonly string GUIDOBJ_DEBUGGER_MEMORY_HEXVIEW_GUID = "8AD6778E-015E-4520-8B77-A6A2E23FFCFF"`
  - Summary: Debugger's memory hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 137)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_DEBUGGER_MEMORY_HEXVIEW_GUID;
    ```
- `public static readonly string GUIDOBJ_DOCUMENTS_TABCONTROL_GUID = "AB1B4BCE-D8C1-43BE-8822-C124FBCAC260"`
  - Summary: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 110)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_DOCUMENTS_TABCONTROL_GUID;
    ```
- `public static readonly string GUIDOBJ_DOCUMENTS_TREEVIEW_GUID = "F64505EB-6D8B-4332-B697-73B2D1EE6C37"`
  - Summary: Documents treeview
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 92)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_DOCUMENTS_TREEVIEW_GUID;
    ```
- `public static readonly string GUIDOBJ_DOCUMENTVIEWERCONTROL_GUID = "FF1980C8-049C-4B9C-8298-5B5C30558A97"`
  - Summary: 's UI control
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 122)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_DOCUMENTVIEWERCONTROL_GUID;
    ```
- `public static readonly string GUIDOBJ_DOCUMENTVIEWER_GUID = "F7088928-7BF0-4044-B631-201F6565077A"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 125)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_DOCUMENTVIEWER_GUID;
    ```
- `public static readonly string GUIDOBJ_GLYPHMARGIN_GUID = "60A3ECC3-3714-418E-8C26-D33F00EA31B4"`
  - Summary: Glyph margin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 140)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_GLYPHMARGIN_GUID;
    ```
- `public static readonly string GUIDOBJ_HEXEDITORPOSITION_GUID = "DF87FB1F-D902-4365-BA52-655A7B27C94A"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 131)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_HEXEDITORPOSITION_GUID;
    ```
- `public static readonly string GUIDOBJ_LOG_EDITOR_GUID = "7ED3CA27-F8F2-4EB8-B9CA-690B27243403"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 173)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_LOG_EDITOR_GUID;
    ```
- `public static readonly string GUIDOBJ_LOG_TEXTEDITORCONTROL_GUID = "898C7BE5-EDAE-42E5-A97F-1FA73C18ED36"`
  - Summary: Log text editor control
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 170)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_LOG_TEXTEDITORCONTROL_GUID;
    ```
- `public static readonly string GUIDOBJ_MARGIN_POINT_GUID = "FEAC116C-FA91-42D9-A646-BD8F3A6A6EFD"`
  - Summary: Point of mouse relative to a or a
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 167)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_MARGIN_POINT_GUID;
    ```
- `public static readonly string GUIDOBJ_OUTPUT_SERVICE_GUID = "FB4F524A-7096-46CD-BCE2-EC2550EFCC92"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 176)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_OUTPUT_SERVICE_GUID;
    ```
- `public static readonly string GUIDOBJ_REPL_EDITOR_GUID = "530F5283-6FCF-49EC-A7D1-52D456C9C846"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 146)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_REPL_EDITOR_GUID;
    ```
- `public static readonly string GUIDOBJ_REPL_TEXTEDITORCONTROL_GUID = "18953907-F276-43F8-B267-DFEA192DD9B8"`
  - Summary: REPL text editor control
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 143)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_REPL_TEXTEDITORCONTROL_GUID;
    ```
- `public static readonly string GUIDOBJ_SEARCHRESULT_GUID = "50CD0058-6406-4ACA-A386-1A4E07561C62"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 104)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_SEARCHRESULT_GUID;
    ```
- `public static readonly string GUIDOBJ_SEARCH_GUID = "7B460F9C-424D-48B3-8FD3-72CEE8DD58E5"`
  - Summary: Search ListBox
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 98)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_SEARCH_GUID;
    ```
- `public static readonly string GUIDOBJ_TABGROUP_GUID = "87B2F94A-D80B-45FD-BB31-71E390CA6C01"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 113)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_TABGROUP_GUID;
    ```
- `public static readonly string GUIDOBJ_TEXTEDITORPOSITION_GUID = "F093458D-C95B-4745-8388-047DE348B500"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 128)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_TEXTEDITORPOSITION_GUID;
    ```
- `public static readonly string GUIDOBJ_TOOLWINDOWGROUP_GUID = "3E9743F1-A2E0-4C5A-B463-3E8CF6D677E4"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 116)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_TOOLWINDOWGROUP_GUID;
    ```
- `public static readonly string GUIDOBJ_TOOLWINDOW_TABCONTROL_GUID = "33FEE79F-7998-4D63-8E6F-B3AD86134960"`
  - Summary: Tool window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 119)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_TOOLWINDOW_TABCONTROL_GUID;
    ```
- `public static readonly string GUIDOBJ_TREEVIEW_NODES_ARRAY_GUID = "B116BABD-BD8B-4870-968A-D1871CC21638"`
  - Summary: Treeview nodes array ([])
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 101)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_TREEVIEW_NODES_ARRAY_GUID;
    ```
- `public static readonly string GUIDOBJ_UNKNOWN_GUID = "9BD7C228-91A0-4140-8E8B-AB0450B418CA"`
  - Summary: An unknown object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 89)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_UNKNOWN_GUID;
    ```
- `public static readonly string GUIDOBJ_VARIABLES_WINDOW_TREEVIEW_GUID = "6415325D-11CC-48C7-9E7B-15D363B7D18E"`
  - Summary: Variables window treeview (autos, locals, watch)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 191)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_VARIABLES_WINDOW_TREEVIEW_GUID;
    ```
- `public static readonly string GUIDOBJ_WPF_HEXVIEW_GUID = "2A57190E-B129-4083-8427-EC2DC6C53D55"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 161)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_WPF_HEXVIEW_GUID;
    ```
- `public static readonly string GUIDOBJ_WPF_HEXVIEW_HOST_GUID = "D63537FA-9D09-44E0-A345-41B7457CFD69"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 158)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_WPF_HEXVIEW_HOST_GUID;
    ```
- `public static readonly string GUIDOBJ_WPF_HEXVIEW_MARGIN_GUID = "9CFD1794-C39A-4529-89BF-03C0C6E1714F"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 164)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_WPF_HEXVIEW_MARGIN_GUID;
    ```
- `public static readonly string GUIDOBJ_WPF_TEXTVIEW_GUID = "2579A07D-C6F5-4A13-B0FB-2C8828278C0C"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 149)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_WPF_TEXTVIEW_GUID;
    ```
- `public static readonly string GUIDOBJ_WPF_TEXTVIEW_HOST_GUID = "C1F6C5AB-1E0F-4BF3-A787-39AA78F0F7A1"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 152)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_WPF_TEXTVIEW_HOST_GUID;
    ```
- `public static readonly string GUIDOBJ_WPF_TEXTVIEW_MARGIN_GUID = "36C94DC4-05AA-4F2B-A6C4-02EFE187AAA3"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuConstants.cs` (line 155)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Menus.MenuConstants.GUIDOBJ_WPF_TEXTVIEW_MARGIN_GUID;
    ```

## Class `MenuItemBase`

Menu item base class, implements

**Inherits/Implements:** `IMenuItem`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.MenuItemBase and call its members.
var instance = new dnSpy.Contracts.Menus.MenuItemBase(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 26)

### Methods

- `public abstract void Execute(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 28)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(context: /* IMenuItemContext */);
    ```
- `public virtual ImageReference? GetIcon(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon(context: /* IMenuItemContext */);
    ```
- `public virtual bool IsChecked(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.IsChecked(context: /* IMenuItemContext */);
    ```
- `public virtual bool IsEnabled(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* IMenuItemContext */);
    ```
- `public virtual bool IsVisible(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.IsVisible(context: /* IMenuItemContext */);
    ```
- `public virtual string GetHeader(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHeader(context: /* IMenuItemContext */);
    ```
- `public virtual string GetInputGestureText(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetInputGestureText(context: /* IMenuItemContext */);
    ```

## Class `MenuItemBase<TContext>`

Menu item base class, implements

**Inherits/Implements:** `IMenuItem`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Menus.MenuItemBase<TContext> and call its members.
var instance = new dnSpy.Contracts.Menus.MenuItemBase<TContext>(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 47)

### Methods

- `protected TContext GetCachedContext(IMenuItemContext context)`
  - Summary: Gets the cached context
  - Parameters:
    - `IMenuItemContext context`: Menu item context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCachedContext(context: /* IMenuItemContext */);
    ```
- `protected abstract TContext CreateContext(IMenuItemContext context)`
  - Summary: Creates the context
  - Parameters:
    - `IMenuItemContext context`: Menu item context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateContext(context: /* IMenuItemContext */);
    ```
- `public abstract void Execute(TContext context)`
  - Summary: Executes the command
  - Parameters:
    - `TContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(context: /* TContext */);
    ```
- `public virtual ImageReference? GetIcon(TContext context)`
  - Summary: Returns the icon or null to use the default value from the attribute
  - Parameters:
    - `TContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 141)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon(context: /* TContext */);
    ```
- `public virtual bool IsChecked(TContext context)`
  - Summary: Returns true if it's checked
  - Parameters:
    - `TContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 155)
  - Example:
    ```csharp
    // Example invocation
    instance.IsChecked(context: /* TContext */);
    ```
- `public virtual bool IsEnabled(TContext context)`
  - Summary: Returns true if it's enabled
  - Parameters:
    - `TContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 120)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* TContext */);
    ```
- `public virtual bool IsVisible(TContext context)`
  - Summary: Returns true if it's visible. If false, none of the other methods get called
  - Parameters:
    - `TContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 127)
  - Example:
    ```csharp
    // Example invocation
    instance.IsVisible(context: /* TContext */);
    ```
- `public virtual string GetHeader(TContext context)`
  - Summary: Returns the header or null to use the default value from the attribute
  - Parameters:
    - `TContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 134)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHeader(context: /* TContext */);
    ```
- `public virtual string GetInputGestureText(TContext context)`
  - Summary: Returns the input gesture text or null to use the default value from the attribute
  - Parameters:
    - `TContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 148)
  - Example:
    ```csharp
    // Example invocation
    instance.GetInputGestureText(context: /* TContext */);
    ```

### Properties

- `protected abstract object CachedContextKey { get; }`
  - Summary: Gets the context key. Should be a unique value per class, eg. an
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemBase.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CachedContextKey;
    ```

## Class `MenuItemCommand`

A menu item that executes an

**Inherits/Implements:** `MenuItemBase`, `ICommandHolder`

**Example**

```csharp
var instance = new dnSpy.Contracts.Menus.MenuItemCommand(realCommand: /* ICommand */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemCommand.cs` (line 28)

### Constructors

- `protected MenuItemCommand(ICommand realCommand)`
  - Summary: Constructor
  - Parameters:
    - `ICommand realCommand`: The real command that gets executed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemCommand.cs` (line 39)

### Methods

- `public override bool IsEnabled(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemCommand.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* IMenuItemContext */);
    ```
- `public override void Execute(IMenuItemContext context)`
  - Parameters:
    - `IMenuItemContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemCommand.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(context: /* IMenuItemContext */);
    ```

### Properties

- `public ICommand Command => realCommand`
  - Summary: Gets the real command
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemCommand.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Command;
    ```

## Class `MenuItemCommand<TContext>`

A menu item that executes an

**Inherits/Implements:** `MenuItemBase<TContext>`, `ICommandHolder`

**Example**

```csharp
var instance = new dnSpy.Contracts.Menus.MenuItemCommand<TContext>(realCommand: /* ICommand */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemCommand.cs` (line 50)

### Constructors

- `protected MenuItemCommand(ICommand realCommand)`
  - Summary: Constructor
  - Parameters:
    - `ICommand realCommand`: The real command that gets executed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemCommand.cs` (line 61)

### Methods

- `public override bool IsEnabled(TContext context)`
  - Parameters:
    - `TContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemCommand.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEnabled(context: /* TContext */);
    ```
- `public sealed override void Execute(TContext context)`
  - Parameters:
    - `TContext context`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemCommand.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.Execute(context: /* TContext */);
    ```

### Properties

- `public ICommand Command => realCommand`
  - Summary: Gets the real command
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Menus/MenuItemCommand.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Command;
    ```

