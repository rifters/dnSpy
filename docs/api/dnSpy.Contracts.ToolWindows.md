# Namespace `dnSpy.Contracts.ToolWindows`

## Interface `IToolWindowGroup`

Tool window tab group

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolWindows.IToolWindowGroup and call its members.
var instance = new dnSpy.Contracts.ToolWindows.IToolWindowGroup(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroup.cs` (line 26)

### Methods

- `void Add(ToolWindowContent content)`
  - Summary: Adds the content
  - Parameters:
    - `ToolWindowContent content`: Content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroup.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(content: /* ToolWindowContent */);
    ```
- `void Close(ToolWindowContent content)`
  - Summary: Closes the content
  - Parameters:
    - `ToolWindowContent content`: Content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroup.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(content: /* ToolWindowContent */);
    ```
- `void CloseActiveTab()`
  - Summary: Closes the active tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroup.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseActiveTab();
    ```
- `void MoveTo(IToolWindowGroup destGroup, ToolWindowContent content)`
  - Summary: Moves from this group to
  - Parameters:
    - `IToolWindowGroup destGroup`: Destination group
    - `ToolWindowContent content`: Content in this group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroup.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTo(destGroup: /* IToolWindowGroup */, content: /* ToolWindowContent */);
    ```
- `void SetFocus(ToolWindowContent content)`
  - Summary: Sets keyboard focus
  - Parameters:
    - `ToolWindowContent content`: Content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroup.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.SetFocus(content: /* ToolWindowContent */);
    ```

### Properties

- `IEnumerable<ToolWindowContent> TabContents { get; }`
  - Summary: Gets all instances
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroup.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabContents;
    ```
- `IToolWindowGroupService ToolWindowGroupService { get; }`
  - Summary: Gets the owner instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroup.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolWindowGroupService;
    ```
- `ToolWindowContent ActiveTabContent { get; set; }`
  - Summary: Gets the active or null if is empty
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroup.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveTabContent;
    ```
- `bool CloseActiveTabCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroup.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CloseActiveTabCanExecute;
    ```

## Interface `IToolWindowGroupService`

Tool window group manager

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolWindows.IToolWindowGroupService and call its members.
var instance = new dnSpy.Contracts.ToolWindows.IToolWindowGroupService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 27)

### Methods

- `IToolWindowGroup Create()`
  - Summary: Creates a new instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```
- `void Close(IToolWindowGroup group)`
  - Summary: Closes the group
  - Parameters:
    - `IToolWindowGroup group`: Group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(group: /* IToolWindowGroup */);
    ```
- `void CloseAllTabGroupsButThis()`
  - Summary: Closes all tab groups except the active one
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 163)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseAllTabGroupsButThis();
    ```
- `void CloseAllTabs()`
  - Summary: Closes all tabs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseAllTabs();
    ```
- `void CloseTabGroup()`
  - Summary: Closes the tab group and all its tabs
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseTabGroup();
    ```
- `void MergeAllTabGroups()`
  - Summary: Moves all tabs to one tab group and closes the remaining (empty) tab groups
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.MergeAllTabGroups();
    ```
- `void MoveAllToNextTabGroup()`
  - Summary: Moves all tabs in the current tab group to the next tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveAllToNextTabGroup();
    ```
- `void MoveAllToPreviousTabGroup()`
  - Summary: Moves all tabs in the current tab group to the previous tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveAllToPreviousTabGroup();
    ```
- `void MoveTabGroupAfterNextTabGroup()`
  - Summary: Moves the active tab group after the next one
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 173)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTabGroupAfterNextTabGroup();
    ```
- `void MoveTabGroupBeforePreviousTabGroup()`
  - Summary: Moves the active tab group before the previous one
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 183)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveTabGroupBeforePreviousTabGroup();
    ```
- `void MoveToNextTabGroup()`
  - Summary: Moves active tab to the next tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToNextTabGroup();
    ```
- `void MoveToPreviousTabGroup()`
  - Summary: Moves the active tab to the previous tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 123)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveToPreviousTabGroup();
    ```
- `void NewHorizontalTabGroup()`
  - Summary: Moves the active tab to a new horizontal tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.NewHorizontalTabGroup();
    ```
- `void NewVerticalTabGroup()`
  - Summary: Moves the active tab to a new vertical tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.NewVerticalTabGroup();
    ```
- `void UseHorizontalTabGroups()`
  - Summary: Stacks all tab groups horizontally
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 213)
  - Example:
    ```csharp
    // Example invocation
    instance.UseHorizontalTabGroups();
    ```
- `void UseVerticalTabGroups()`
  - Summary: Stacks all tab groups vertically
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 203)
  - Example:
    ```csharp
    // Example invocation
    instance.UseVerticalTabGroups();
    ```

### Properties

- `IEnumerable<IToolWindowGroup> TabGroups { get; }`
  - Summary: Gets all instances
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabGroups;
    ```
- `IToolWindowGroup ActiveTabGroup { get; set; }`
  - Summary: Gets the active or null if is empty
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveTabGroup;
    ```
- `bool CloseAllTabGroupsButThisCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 158)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CloseAllTabGroupsButThisCanExecute;
    ```
- `bool CloseAllTabsCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CloseAllTabsCanExecute;
    ```
- `bool CloseTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 148)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CloseTabGroupCanExecute;
    ```
- `bool IsHorizontal { get; set; }`
  - Summary: true if the s are lined up horizontally, else vertically
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsHorizontal;
    ```
- `bool MergeAllTabGroupsCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 188)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MergeAllTabGroupsCanExecute;
    ```
- `bool MoveAllToNextTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 128)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveAllToNextTabGroupCanExecute;
    ```
- `bool MoveAllToPreviousTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 138)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveAllToPreviousTabGroupCanExecute;
    ```
- `bool MoveTabGroupAfterNextTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 168)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveTabGroupAfterNextTabGroupCanExecute;
    ```
- `bool MoveTabGroupBeforePreviousTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 178)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveTabGroupBeforePreviousTabGroupCanExecute;
    ```
- `bool MoveToNextTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 108)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveToNextTabGroupCanExecute;
    ```
- `bool MoveToPreviousTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 118)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MoveToPreviousTabGroupCanExecute;
    ```
- `bool NewHorizontalTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewHorizontalTabGroupCanExecute;
    ```
- `bool NewVerticalTabGroupCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 98)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewVerticalTabGroupCanExecute;
    ```
- `bool UseHorizontalTabGroupsCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 208)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseHorizontalTabGroupsCanExecute;
    ```
- `bool UseVerticalTabGroupsCanExecute { get; }`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 198)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseVerticalTabGroupsCanExecute;
    ```
- `object UIObject { get; }`
  - Summary: Gets the UI object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIObject;
    ```

### Events

- `event EventHandler<ToolWindowGroupCollectionChangedEventArgs> TabGroupCollectionChanged`
  - Summary: Raised when a tab group has been added or removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 67)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TabGroupCollectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<ToolWindowGroupSelectedEventArgs> TabGroupSelectionChanged`
  - Summary: Raised when a new tab group has been selected
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 62)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TabGroupSelectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<ToolWindowSelectedEventArgs> TabSelectionChanged`
  - Summary: Raised when a new tab has been selected
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowGroupService.cs` (line 57)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TabSelectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IToolWindowService`

Tool window manager

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolWindows.IToolWindowService and call its members.
var instance = new dnSpy.Contracts.ToolWindows.IToolWindowService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowService.cs` (line 24)

### Methods

- `IToolWindowGroupService Create(ToolWindowGroupServiceOptions options)`
  - Summary: Creates a new instance
  - Parameters:
    - `ToolWindowGroupServiceOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/IToolWindowService.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(options: /* ToolWindowGroupServiceOptions */);
    ```

## Class `ToolWindowContent`

Tool window content. If any of the properties can change, you must implement

**Inherits/Implements:** `IUIObjectProvider`

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolWindows.ToolWindowContent and call its members.
var instance = new dnSpy.Contracts.ToolWindows.ToolWindowContent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowContent.cs` (line 30)

### Methods

- `public virtual void OnVisibilityChanged(ToolWindowContentVisibilityEvent visEvent)`
  - Summary: Called when the visibility changes
  - Parameters:
    - `ToolWindowContentVisibilityEvent visEvent`: Event
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowContent.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.OnVisibilityChanged(visEvent: /* ToolWindowContentVisibilityEvent */);
    ```

### Properties

- `public abstract FrameworkElement ZoomElement { get; }`
  - Summary: Gets the element that gets the or null if none, see also and . If this property can change, you must implement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowContent.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ZoomElement;
    ```
- `public abstract Guid Guid { get; }`
  - Summary: Gets the guid of this content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowContent.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public abstract IInputElement FocusedElement { get; }`
  - Summary: The element that gets focus or null if none, see also
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowContent.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FocusedElement;
    ```
- `public abstract object UIObject { get; }`
  - Summary: UI object; a WPF UI element or an object with a . If this property can change, you must implement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowContent.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIObject;
    ```
- `public abstract string Title { get; }`
  - Summary: Title. If this property can change, you must implement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowContent.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Title;
    ```
- `public virtual object ToolTip => null`
  - Summary: ToolTip or null. If this property can change, you must implement
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowContent.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolTip;
    ```

## Enum `ToolWindowContentVisibilityEvent`

Event type

**Example**

```csharp
// Instantiate dnSpy.Contracts.ToolWindows.ToolWindowContentVisibilityEvent and call its members.
var instance = new dnSpy.Contracts.ToolWindows.ToolWindowContentVisibilityEvent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowContentVisibilityEvent.cs` (line 24)

### Members

- `Added`: It's been added to the UI. It may or may not be visible.
- `Removed`: It's been removed from the UI
- `Visible`: It's open and visible
- `Hidden`: It's open but hidden
- `GotKeyboardFocus`: The content got keyboard focus
- `LostKeyboardFocus`: The content lost keyboard focus

## Class `ToolWindowGroupCollectionChangedEventArgs`

Collection changed event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.ToolWindows.ToolWindowGroupCollectionChangedEventArgs(added: /* bool */, tabGroup: /* IToolWindowGroup */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupCollectionChangedEventArgs.cs` (line 26)

### Constructors

- `public ToolWindowGroupCollectionChangedEventArgs(bool added, IToolWindowGroup tabGroup)`
  - Summary: Constructor
  - Parameters:
    - `bool added`: true if it was added
    - `IToolWindowGroup tabGroup`: Tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupCollectionChangedEventArgs.cs` (line 42)

### Properties

- `public IToolWindowGroup TabGroup { get; }`
  - Summary: The tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupCollectionChangedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabGroup;
    ```
- `public bool Added { get; }`
  - Summary: true if was added, false if it was removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupCollectionChangedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Added;
    ```

## Class `ToolWindowGroupSelectedEventArgs`

Tab group selected event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.ToolWindows.ToolWindowGroupSelectedEventArgs(selected: /* IToolWindowGroup */, unselected: /* IToolWindowGroup */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupSelectedEventArgs.cs` (line 26)

### Constructors

- `public ToolWindowGroupSelectedEventArgs(IToolWindowGroup selected, IToolWindowGroup unselected)`
  - Summary: Constructor
  - Parameters:
    - `IToolWindowGroup selected`: Selected tab group or null
    - `IToolWindowGroup unselected`: Unselected tab group or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupSelectedEventArgs.cs` (line 42)

### Properties

- `public IToolWindowGroup Selected { get; }`
  - Summary: Selected tab group or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupSelectedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Selected;
    ```
- `public IToolWindowGroup Unselected { get; }`
  - Summary: Unselected tab group or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupSelectedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Unselected;
    ```

## Class `ToolWindowGroupServiceOptions`

options

**Example**

```csharp
var instance = new dnSpy.Contracts.ToolWindows.ToolWindowGroupServiceOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupServiceOptions.cs` (line 27)

### Constructors

- `public ToolWindowGroupServiceOptions()`
  - Summary: Default constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupServiceOptions.cs` (line 46)
- `public ToolWindowGroupServiceOptions(Guid groupGuid)`
  - Summary: Constructor
  - Parameters:
    - `Guid groupGuid`: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupServiceOptions.cs` (line 61)
- `public ToolWindowGroupServiceOptions(string groupGuid)`
  - Summary: Constructor
  - Parameters:
    - `string groupGuid`: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupServiceOptions.cs` (line 53)

### Methods

- `public ToolWindowGroupServiceOptions Clone()`
  - Summary: Clones this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupServiceOptions.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```

### Properties

- `public Guid ToolWindowGroupGuid { get; set; }`
  - Summary: Tool window group guid, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupServiceOptions.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ToolWindowGroupGuid;
    ```
- `public object TabControlStyle { get; set; }`
  - Summary: A style or a resource key or null to use the default style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupServiceOptions.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabControlStyle;
    ```
- `public object TabItemStyle { get; set; }`
  - Summary: A style or a resource key or null to use the default style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowGroupServiceOptions.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabItemStyle;
    ```

## Class `ToolWindowSelectedEventArgs`

Tab selected event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
var instance = new dnSpy.Contracts.ToolWindows.ToolWindowSelectedEventArgs(tabGroup: /* IToolWindowGroup */, selected: /* ToolWindowContent */, unselected: /* ToolWindowContent */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowSelectedEventArgs.cs` (line 26)

### Constructors

- `public ToolWindowSelectedEventArgs(IToolWindowGroup tabGroup, ToolWindowContent selected, ToolWindowContent unselected)`
  - Summary: Constructor
  - Parameters:
    - `IToolWindowGroup tabGroup`: Tab group
    - `ToolWindowContent selected`: Selected content or null
    - `ToolWindowContent unselected`: Unselected content or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowSelectedEventArgs.cs` (line 48)

### Properties

- `public IToolWindowGroup TabGroup { get; }`
  - Summary: Tab group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowSelectedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabGroup;
    ```
- `public ToolWindowContent Selected { get; }`
  - Summary: Selected tab content or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowSelectedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Selected;
    ```
- `public ToolWindowContent Unselected { get; }`
  - Summary: Unselected tab content or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/ToolWindows/ToolWindowSelectedEventArgs.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Unselected;
    ```

