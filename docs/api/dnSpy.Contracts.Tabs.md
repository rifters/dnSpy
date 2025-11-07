# Namespace `dnSpy.Contracts.Tabs`

## Interface `ITabContent`

Tab content

**Example**

```csharp
// Instantiate dnSpy.Contracts.Tabs.ITabContent and call its members.
var instance = new dnSpy.Contracts.Tabs.ITabContent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabContent.cs` (line 28)

### Methods

- `void OnVisibilityChanged(TabContentVisibilityEvent visEvent)`
  - Summary: Called when the visibility changes
  - Parameters:
    - `TabContentVisibilityEvent visEvent`: Event
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabContent.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.OnVisibilityChanged(visEvent: /* TabContentVisibilityEvent */);
    ```

### Properties

- `IInputElement FocusedElement { get; }`
  - Summary: Gets the element that should get focus when the tab is selected or null to use . Implement to set focus yourself.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabContent.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FocusedElement;
    ```
- `object ToolTip { get; }`
  - Summary: ToolTip or null. If this property can change, you must implement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabContent.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTip;
    ```
- `object UIObject { get; }`
  - Summary: The UI object. If this property can change, you must implement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabContent.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIObject;
    ```
- `string Title { get; }`
  - Summary: Title. If this property can change, you must implement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabContent.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Title;
    ```

## Interface `ITabGroup`

Contains 0 or more tabs

**Example**

```csharp
// Instantiate dnSpy.Contracts.Tabs.ITabGroup and call its members.
var instance = new dnSpy.Contracts.Tabs.ITabGroup(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 28)

### Methods

- `void Add(ITabContent content)`
  - Summary: Adds tab content
  - Parameters:
    - `ITabContent content`: Content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(content: /* ITabContent */);
    ```
- `void Close(ITabContent content)`
  - Summary: Closes the tab
  - Parameters:
    - `ITabContent content`: Content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(content: /* ITabContent */);
    ```
- `void CloseActiveTab()`
  - Summary: Closes the active tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseActiveTab();
    ```
- `void CloseAllButActiveTab()`
  - Summary: Closes all tabs except the active tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseAllButActiveTab();
    ```
- `void CloseAllTabs()`
  - Summary: Closes all tabs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseAllTabs();
    ```
- `void SelectNextTab()`
  - Summary: Selects the next tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 116)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectNextTab();
    ```
- `void SelectPreviousTab()`
  - Summary: Selects the previous tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectPreviousTab();
    ```
- `void SetFocus(ITabContent content)`
  - Summary: Sets keyboard focus
  - Parameters:
    - `ITabContent content`: Content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.SetFocus(content: /* ITabContent */);
    ```

### Properties

- `IContextMenuProvider ContextMenuProvider { get; }`
  - Summary: Gets the context menu provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 131)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContextMenuProvider;
    ```
- `IEnumerable<ITabContent> TabContents { get; }`
  - Summary: Gets all instances
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabContents;
    ```
- `ITabContent ActiveTabContent { get; set; }`
  - Summary: Gets the active or null if is empty
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveTabContent;
    ```
- `ITabGroupService TabGroupService { get; }`
  - Summary: Gets the owner instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabGroupService;
    ```
- `bool CloseActiveTabCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CloseActiveTabCanExecute;
    ```
- `bool CloseAllButActiveTabCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CloseAllButActiveTabCanExecute;
    ```
- `bool CloseAllTabsCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CloseAllTabsCanExecute;
    ```
- `bool IsKeyboardFocusWithin { get; }`
  - Summary: true if keyboard focus is within the tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsKeyboardFocusWithin;
    ```
- `bool SelectNextTabCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectNextTabCanExecute;
    ```
- `bool SelectPreviousTabCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 121)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectPreviousTabCanExecute;
    ```
- `object Tag { get; set; }`
  - Summary: Any value can be written here. It's ignored by this instance.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```

### Events

- `event EventHandler<TabContentAttachedEventArgs> TabContentAttached`
  - Summary: Raised when a is attached/detached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroup.cs` (line 52)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TabContentAttached += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `ITabGroupService`

manager

**Example**

```csharp
// Instantiate dnSpy.Contracts.Tabs.ITabGroupService and call its members.
var instance = new dnSpy.Contracts.Tabs.ITabGroupService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 27)

### Methods

- `ITabGroup Create()`
  - Summary: Creates a new instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```
- `void Close(ITabGroup tabGroup)`
  - Summary: Closes the tab group
  - Parameters:
    - `ITabGroup tabGroup`: Tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(tabGroup: /* ITabGroup */);
    ```
- `void CloseAllTabGroupsButThis()`
  - Summary: Closes all tab groups except the active one
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseAllTabGroupsButThis();
    ```
- `void CloseAllTabs()`
  - Summary: Closes all tabs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseAllTabs();
    ```
- `void CloseTabGroup()`
  - Summary: Closes the tab group and all its tabs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 165)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseTabGroup();
    ```
- `void MergeAllTabGroups()`
  - Summary: Moves all tabs to one tab group and closes the remaining (empty) tab groups
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 205)
  - Example:
    ```csharp
    // Example invocation
    instance.MergeAllTabGroups();
    ```
- `void MoveAllToNextTabGroup()`
  - Summary: Moves all tabs in the current tab group to the next tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 145)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveAllToNextTabGroup();
    ```
- `void MoveAllToPreviousTabGroup()`
  - Summary: Moves all tabs in the current tab group to the previous tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 155)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveAllToPreviousTabGroup();
    ```
- `void MoveTabGroupAfterNextTabGroup()`
  - Summary: Moves the active tab group after the next one
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 185)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTabGroupAfterNextTabGroup();
    ```
- `void MoveTabGroupBeforePreviousTabGroup()`
  - Summary: Moves the active tab group before the previous one
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 195)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTabGroupBeforePreviousTabGroup();
    ```
- `void MoveToNextTabGroup()`
  - Summary: Moves active tab to the next tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToNextTabGroup();
    ```
- `void MoveToPreviousTabGroup()`
  - Summary: Moves the active tab to the previous tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToPreviousTabGroup();
    ```
- `void NewHorizontalTabGroup(Action<ITabGroup> onCreated = null)`
  - Summary: Moves the active tab to a new horizontal tab group
  - Parameters:
    - `Action<ITabGroup> onCreated` (default: `null`): Called after the instance has been created
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    instance.NewHorizontalTabGroup(onCreated: /* Action<ITabGroup> */);
    ```
- `void NewVerticalTabGroup(Action<ITabGroup> onCreated = null)`
  - Summary: Moves the active tab to a new vertical tab group
  - Parameters:
    - `Action<ITabGroup> onCreated` (default: `null`): Called after the instance has been created
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.NewVerticalTabGroup(onCreated: /* Action<ITabGroup> */);
    ```
- `void UseHorizontalTabGroups()`
  - Summary: Stacks all tab groups horizontally
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 225)
  - Example:
    ```csharp
    // Example invocation
    instance.UseHorizontalTabGroups();
    ```
- `void UseVerticalTabGroups()`
  - Summary: Stacks all tab groups vertically
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 215)
  - Example:
    ```csharp
    // Example invocation
    instance.UseVerticalTabGroups();
    ```

### Properties

- `IEnumerable<ITabGroup> TabGroups { get; }`
  - Summary: Gets all instances
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabGroups;
    ```
- `ITabGroup ActiveTabGroup { get; set; }`
  - Summary: Gets the active or null if is empty
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveTabGroup;
    ```
- `ITabService TabService { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabService;
    ```
- `bool CloseAllTabGroupsButThisCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 170)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CloseAllTabGroupsButThisCanExecute;
    ```
- `bool CloseAllTabsCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CloseAllTabsCanExecute;
    ```
- `bool CloseTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 160)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CloseTabGroupCanExecute;
    ```
- `bool IsHorizontal { get; set; }`
  - Summary: true if the s are lined up horizontally, else vertically
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsHorizontal;
    ```
- `bool MergeAllTabGroupsCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 200)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MergeAllTabGroupsCanExecute;
    ```
- `bool MoveAllToNextTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 140)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveAllToNextTabGroupCanExecute;
    ```
- `bool MoveAllToPreviousTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 150)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveAllToPreviousTabGroupCanExecute;
    ```
- `bool MoveTabGroupAfterNextTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 180)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveTabGroupAfterNextTabGroupCanExecute;
    ```
- `bool MoveTabGroupBeforePreviousTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 190)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveTabGroupBeforePreviousTabGroupCanExecute;
    ```
- `bool MoveToNextTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 120)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveToNextTabGroupCanExecute;
    ```
- `bool MoveToPreviousTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 130)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveToPreviousTabGroupCanExecute;
    ```
- `bool NewHorizontalTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 98)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewHorizontalTabGroupCanExecute;
    ```
- `bool NewVerticalTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 109)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewVerticalTabGroupCanExecute;
    ```
- `bool UseHorizontalTabGroupsCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 220)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseHorizontalTabGroupsCanExecute;
    ```
- `bool UseVerticalTabGroupsCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 210)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseVerticalTabGroupsCanExecute;
    ```
- `object Tag { get; set; }`
  - Summary: Any value can be written here. It's ignored by this instance.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Tag;
    ```
- `object UIObject { get; }`
  - Summary: Gets the UI object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIObject;
    ```

### Events

- `event EventHandler<TabGroupCollectionChangedEventArgs> TabGroupCollectionChanged`
  - Summary: Raised when a tab group has been added or removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 77)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TabGroupCollectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<TabGroupSelectedEventArgs> TabGroupSelectionChanged`
  - Summary: Raised when a new tab group has been selected
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 72)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TabGroupSelectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<TabSelectedEventArgs> TabSelectionChanged`
  - Summary: Raised when a new tab has been selected
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabGroupService.cs` (line 67)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TabSelectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `ITabService`

Creates instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.Tabs.ITabService and call its members.
var instance = new dnSpy.Contracts.Tabs.ITabService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabService.cs` (line 26)

### Methods

- `ITabGroupService Create(TabGroupServiceOptions options)`
  - Summary: Creates a new instance
  - Parameters:
    - `TabGroupServiceOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabService.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(options: /* TabGroupServiceOptions */);
    ```
- `void Remove(ITabGroupService mgr)`
  - Summary: Removes a instance
  - Parameters:
    - `ITabGroupService mgr`: Instance to remove
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabService.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(mgr: /* ITabGroupService */);
    ```

### Properties

- `IEnumerable<ITabGroupService> TabGroupServices { get; }`
  - Summary: Gets all instances
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabService.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabGroupServices;
    ```
- `ITabGroupService ActiveTabGroupService { get; }`
  - Summary: Gets the active instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/ITabService.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveTabGroupService;
    ```

## Class `TabContentAttachedEventArgs`

attached/detached event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Tabs.TabContentAttachedEventArgs(attached: /* bool */, tabContent: /* ITabContent */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabContentAttachedEventArgs.cs` (line 26)

### Constructors

- `public TabContentAttachedEventArgs(bool attached, ITabContent tabContent)`
  - Summary: Constructor
  - Parameters:
    - `bool attached`: true if attached, false if detached
    - `ITabContent tabContent`: Tab content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabContentAttachedEventArgs.cs` (line 42)

### Properties

- `public ITabContent TabContent { get; }`
  - Summary: The attached/detached tab content instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabContentAttachedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabContent;
    ```
- `public bool Attached { get; }`
  - Summary: true if attached, false if detached
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabContentAttachedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Attached;
    ```

## Enum `TabContentVisibilityEvent`

Event type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Tabs.TabContentVisibilityEvent and call its members.
var instance = new dnSpy.Contracts.Tabs.TabContentVisibilityEvent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabContentVisibilityEvent.cs` (line 24)

### Members

- `Added`: It's been added to the UI. It may or may not be visible.
- `Removed`: It's been removed from the UI
- `Visible`: It's open and visible
- `Hidden`: It's open but hidden
- `GotKeyboardFocus`: The content got keyboard focus
- `LostKeyboardFocus`: The content lost keyboard focus

## Class `TabGroupCollectionChangedEventArgs`

Collection changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Tabs.TabGroupCollectionChangedEventArgs(added: /* bool */, tabGroup: /* ITabGroup */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupCollectionChangedEventArgs.cs` (line 26)

### Constructors

- `public TabGroupCollectionChangedEventArgs(bool added, ITabGroup tabGroup)`
  - Summary: Constructor
  - Parameters:
    - `bool added`: true if it was added
    - `ITabGroup tabGroup`: Tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupCollectionChangedEventArgs.cs` (line 42)

### Properties

- `public ITabGroup TabGroup { get; }`
  - Summary: The tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupCollectionChangedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabGroup;
    ```
- `public bool Added { get; }`
  - Summary: true if was added, false if it was removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupCollectionChangedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Added;
    ```

## Class `TabGroupSelectedEventArgs`

Tab group selected event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Tabs.TabGroupSelectedEventArgs(selected: /* ITabGroup */, unselected: /* ITabGroup */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupSelectedEventArgs.cs` (line 26)

### Constructors

- `public TabGroupSelectedEventArgs(ITabGroup selected, ITabGroup unselected)`
  - Summary: Constructor
  - Parameters:
    - `ITabGroup selected`: Selected tab group or null
    - `ITabGroup unselected`: Unselected tab group or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupSelectedEventArgs.cs` (line 42)

### Properties

- `public ITabGroup Selected { get; }`
  - Summary: Selected tab group or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupSelectedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Selected;
    ```
- `public ITabGroup Unselected { get; }`
  - Summary: Unselected tab group or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupSelectedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Unselected;
    ```

## Class `TabGroupServiceOptions`

options

**Example**

```csharp
var instance = new dnSpy.Contracts.Tabs.TabGroupServiceOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupServiceOptions.cs` (line 28)

### Constructors

- `public TabGroupServiceOptions()`
  - Summary: Default constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupServiceOptions.cs` (line 53)
- `public TabGroupServiceOptions(Guid tabGroupGuid)`
  - Summary: Constructor
  - Parameters:
    - `Guid tabGroupGuid`: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupServiceOptions.cs` (line 68)
- `public TabGroupServiceOptions(string tabGroupGuid)`
  - Summary: Constructor
  - Parameters:
    - `string tabGroupGuid`: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupServiceOptions.cs` (line 60)

### Methods

- `public TabGroupServiceOptions Clone()`
  - Summary: Clones this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupServiceOptions.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

### Properties

- `public Guid TabGroupGuid { get; set; }`
  - Summary: Guid to use to initialize the context menu if is null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupServiceOptions.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabGroupGuid;
    ```
- `public object TabControlStyle { get; set; }`
  - Summary: A style or a resource key or null to use the default style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupServiceOptions.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabControlStyle;
    ```
- `public object TabItemStyle { get; set; }`
  - Summary: A style or a resource key or null to use the default style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupServiceOptions.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabItemStyle;
    ```

### Fields

- `public Func<IMenuService, ITabGroup, FrameworkElement, IContextMenuProvider> InitializeContextMenu`
  - Summary: Called in the constructor to initialize the context menu. If null, the instance itself initializes it using
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabGroupServiceOptions.cs` (line 48)
  - Example:
    ```csharp
    var value = instance.InitializeContextMenu;
    ```

## Class `TabSelectedEventArgs`

Tab selected event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.Tabs.TabSelectedEventArgs(tabGroup: /* ITabGroup */, selected: /* ITabContent */, unselected: /* ITabContent */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabSelectedEventArgs.cs` (line 26)

### Constructors

- `public TabSelectedEventArgs(ITabGroup tabGroup, ITabContent selected, ITabContent unselected)`
  - Summary: Constructor
  - Parameters:
    - `ITabGroup tabGroup`: Tab group
    - `ITabContent selected`: Selected content or null
    - `ITabContent unselected`: Unselected content or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabSelectedEventArgs.cs` (line 48)

### Properties

- `public ITabContent Selected { get; }`
  - Summary: Selected tab content or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabSelectedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Selected;
    ```
- `public ITabContent Unselected { get; }`
  - Summary: Unselected tab content or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabSelectedEventArgs.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Unselected;
    ```
- `public ITabGroup TabGroup { get; }`
  - Summary: Tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Tabs/TabSelectedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabGroup;
    ```

