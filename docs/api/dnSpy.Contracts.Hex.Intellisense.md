# Namespace `dnSpy.Contracts.Hex.Intellisense`

## Class `HexIntellisenseController`

Intellisense controller

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexIntellisenseController();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseController.cs` (line 26)

### Constructors

- `protected HexIntellisenseController()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseController.cs` (line 30)

### Methods

- `public abstract void Detach(HexView hexView)`
  - Summary: Detaches from
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseController.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Detach(hexView: /* HexView */);
    ```

## Class `HexIntellisenseControllerProvider`

Provides

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexIntellisenseControllerProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseControllerProvider.cs` (line 26)

### Constructors

- `protected HexIntellisenseControllerProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseControllerProvider.cs` (line 30)

### Methods

- `public abstract HexIntellisenseController TryCreateIntellisenseController(HexView hexView)`
  - Summary: Creates a or returns null
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseControllerProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.TryCreateIntellisenseController(hexView: /* HexView */);
    ```

## Class `HexIntellisensePresenter`

Intellisense presenter

**Inherits/Implements:** `IHexIntellisensePresenter`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexIntellisensePresenter();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisensePresenter.cs` (line 24)

### Constructors

- `protected HexIntellisensePresenter()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisensePresenter.cs` (line 28)

### Properties

- `public abstract HexIntellisenseSession Session { get; }`
  - Summary: Gets the session
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisensePresenter.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Session;
    ```

## Class `HexIntellisensePresenterProvider`

Provides

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexIntellisensePresenterProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisensePresenterProvider.cs` (line 24)

### Constructors

- `protected HexIntellisensePresenterProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisensePresenterProvider.cs` (line 28)

### Methods

- `public abstract HexIntellisensePresenter TryCreateIntellisensePresenter(HexIntellisenseSession session)`
  - Summary: Creates a or returns null
  - Parameters:
    - `HexIntellisenseSession session`: Session
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisensePresenterProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.TryCreateIntellisensePresenter(session: /* HexIntellisenseSession */);
    ```

## Class `HexIntellisenseSession`

Intellisense session

**Inherits/Implements:** `VSUTIL.IPropertyOwner`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexIntellisenseSession();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 28)

### Constructors

- `protected HexIntellisenseSession()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 32)

### Methods

- `public abstract bool Match()`
  - Summary: Tries to get a match
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.Match();
    ```
- `public abstract void Collapse()`
  - Summary: Collapses the UI, or if it's not collapsible, closes the UI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    instance.Collapse();
    ```
- `public abstract void Dismiss()`
  - Summary: Dismisses the session
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.Dismiss();
    ```
- `public abstract void Recalculate()`
  - Summary: Recalculates the state
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.Recalculate();
    ```
- `public abstract void Start()`
  - Summary: Starts the session
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.Start();
    ```

### Properties

- `public VSUTIL.PropertyCollection Properties { get; }`
  - Summary: Gets all properties
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Properties;
    ```
- `public abstract HexCellPosition TriggerPoint { get; }`
  - Summary: Gets the trigger point
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TriggerPoint;
    ```
- `public abstract HexIntellisensePresenter Presenter { get; }`
  - Summary: Gets the presenter
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Presenter;
    ```
- `public abstract HexView HexView { get; }`
  - Summary: Gets the hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexView;
    ```
- `public abstract bool IsDismissed { get; }`
  - Summary: true if the session has been dismissed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDismissed;
    ```

### Events

- `public abstract event EventHandler Dismissed`
  - Summary: Raised after is called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 72)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Dismissed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler PresenterChanged`
  - Summary: Raised after is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 57)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PresenterChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler Recalculated`
  - Summary: Raised after is called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSession.cs` (line 87)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Recalculated += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexIntellisenseSessionStack`

Intellisense session stack

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexIntellisenseSessionStack();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStack.cs` (line 26)

### Constructors

- `protected HexIntellisenseSessionStack()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStack.cs` (line 30)

### Methods

- `public abstract HexIntellisenseSession PopSession()`
  - Summary: Removes the session from the top of the stack
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStack.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.PopSession();
    ```
- `public abstract void CollapseAllSessions()`
  - Summary: Collapses all sessions
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStack.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.CollapseAllSessions();
    ```
- `public abstract void MoveSessionToTop(HexIntellisenseSession session)`
  - Summary: Moves a session to the top of the stack
  - Parameters:
    - `HexIntellisenseSession session`: Session
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStack.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.MoveSessionToTop(session: /* HexIntellisenseSession */);
    ```
- `public abstract void PushSession(HexIntellisenseSession session)`
  - Summary: Adds a session to the top of the stack
  - Parameters:
    - `HexIntellisenseSession session`: Session
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStack.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.PushSession(session: /* HexIntellisenseSession */);
    ```

### Properties

- `public abstract HexIntellisenseSession TopSession { get; }`
  - Summary: Gets the session at the top of the stack or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStack.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TopSession;
    ```
- `public abstract ReadOnlyObservableCollection<HexIntellisenseSession> Sessions { get; }`
  - Summary: Gets all sessions
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStack.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Sessions;
    ```

## Class `HexIntellisenseSessionStackMapService`

service

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexIntellisenseSessionStackMapService();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStackMapService.cs` (line 26)

### Constructors

- `protected HexIntellisenseSessionStackMapService()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStackMapService.cs` (line 30)

### Methods

- `public abstract HexIntellisenseSessionStack GetStackForHexView(HexView hexView)`
  - Summary: Gets the instance
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSessionStackMapService.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStackForHexView(hexView: /* HexView */);
    ```

## Class `HexIntellisenseSpaceReservationManagerNames`

Intellisense names

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Intellisense.HexIntellisenseSpaceReservationManagerNames members directly without instantiation.
dnSpy.Contracts.Hex.Intellisense.HexIntellisenseSpaceReservationManagerNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSpaceReservationManagerNames.cs` (line 26)

### Fields

- `public const string QuickInfoSpaceReservationManagerName = nameof(QuickInfoSpaceReservationManagerName)`
  - Summary: Quick info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisenseSpaceReservationManagerNames.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Intellisense.HexIntellisenseSpaceReservationManagerNames.QuickInfoSpaceReservationManagerName;
    ```

## Class `HexQuickInfoBroker`

Quick info broker

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexQuickInfoBroker();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoBroker.cs` (line 27)

### Constructors

- `protected HexQuickInfoBroker()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoBroker.cs` (line 31)

### Methods

- `public abstract HexQuickInfoSession CreateQuickInfoSession(HexView hexView, HexCellPosition triggerPoint, bool trackMouse)`
  - Summary: Creates a quick info session
  - Parameters:
    - `HexView hexView`: Hex view
    - `HexCellPosition triggerPoint`: Trigger point
    - `bool trackMouse`: true to track the mouse
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoBroker.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateQuickInfoSession(hexView: /* HexView */, triggerPoint: /* HexCellPosition */, trackMouse: /* bool */);
    ```
- `public abstract HexQuickInfoSession TriggerQuickInfo(HexView hexView)`
  - Summary: Triggers a quick info session
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoBroker.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.TriggerQuickInfo(hexView: /* HexView */);
    ```
- `public abstract HexQuickInfoSession TriggerQuickInfo(HexView hexView, HexCellPosition triggerPoint, bool trackMouse)`
  - Summary: Triggers a quick info session
  - Parameters:
    - `HexView hexView`: Hex view
    - `HexCellPosition triggerPoint`: Trigger point
    - `bool trackMouse`: true to track the mouse
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoBroker.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.TriggerQuickInfo(hexView: /* HexView */, triggerPoint: /* HexCellPosition */, trackMouse: /* bool */);
    ```
- `public abstract ReadOnlyCollection<HexQuickInfoSession> GetSessions(HexView hexView)`
  - Summary: Gets all active quick info sessions in
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoBroker.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSessions(hexView: /* HexView */);
    ```
- `public abstract bool IsQuickInfoActive(HexView hexView)`
  - Summary: Returns true if quick info is active in
  - Parameters:
    - `HexView hexView`: Hex view to check
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoBroker.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.IsQuickInfoActive(hexView: /* HexView */);
    ```

## Class `HexQuickInfoSession`

Quick info session

**Inherits/Implements:** `HexIntellisenseSession`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexQuickInfoSession();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSession.cs` (line 27)

### Constructors

- `protected HexQuickInfoSession()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSession.cs` (line 31)

### Properties

- `public abstract HexBufferSpanSelection ApplicableToSpan { get; }`
  - Summary: Gets the applicable-to span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSession.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ApplicableToSpan;
    ```
- `public abstract VSLI.BulkObservableCollection<object> QuickInfoContent { get; }`
  - Summary: Gets the quick info content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSession.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.QuickInfoContent;
    ```
- `public abstract bool TrackMouse { get; }`
  - Summary: true if the mouse is tracked
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSession.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TrackMouse;
    ```
- `public virtual bool HasInteractiveContent => false`
  - Summary: true if it has interactive content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSession.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasInteractiveContent;
    ```

### Events

- `public abstract event EventHandler ApplicableToSpanChanged`
  - Summary: Raised after is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSession.cs` (line 46)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ApplicableToSpanChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `HexQuickInfoSource`

Quick info source

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexQuickInfoSource();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSource.cs` (line 27)

### Constructors

- `protected HexQuickInfoSource()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSource.cs` (line 31)

### Methods

- `protected virtual void DisposeCore()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSource.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.DisposeCore();
    ```
- `public abstract void AugmentQuickInfoSession(HexQuickInfoSession session, IList<object> quickInfoContent, out HexBufferSpanSelection applicableToSpan)`
  - Summary: Augments the quick info session
  - Parameters:
    - `HexQuickInfoSession session`: Session
    - `IList<object> quickInfoContent`: Updated with new content
    - `out HexBufferSpanSelection applicableToSpan`: Updated with applicable-to span or the default value if nothing was added to
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSource.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.AugmentQuickInfoSession(session: /* HexQuickInfoSession */, quickInfoContent: /* IList<object> */, applicableToSpan: /* HexBufferSpanSelection */);
    ```
- `public void Dispose()`
  - Summary: Disposes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSource.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

## Class `HexQuickInfoSourceProvider`

Provides

**Example**

```csharp
var instance = new dnSpy.Contracts.Hex.Intellisense.HexQuickInfoSourceProvider();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSourceProvider.cs` (line 26)

### Constructors

- `protected HexQuickInfoSourceProvider()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSourceProvider.cs` (line 30)

### Methods

- `public abstract HexQuickInfoSource TryCreateQuickInfoSource(HexView hexView)`
  - Summary: Creates a or returns null
  - Parameters:
    - `HexView hexView`: Hex view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexQuickInfoSourceProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.TryCreateQuickInfoSource(hexView: /* HexView */);
    ```

## Interface `IHexCustomIntellisensePresenter`

Custom

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Intellisense.IHexCustomIntellisensePresenter and call its members.
var instance = new dnSpy.Contracts.Hex.Intellisense.IHexCustomIntellisensePresenter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexCustomIntellisensePresenter.cs` (line 24)

### Methods

- `void Render()`
  - Summary: Renders the UI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexCustomIntellisensePresenter.cs` (line 28)
  - Example:
    ```csharp
    // Example invocation
    instance.Render();
    ```

## Interface `IHexIntellisensePresenter`

Intellisense presenter

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Intellisense.IHexIntellisensePresenter and call its members.
var instance = new dnSpy.Contracts.Hex.Intellisense.IHexIntellisensePresenter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisensePresenter.cs` (line 39)

### Properties

- `HexIntellisenseSession Session { get; }`
  - Summary: Gets the session
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/HexIntellisensePresenter.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Session;
    ```

## Interface `IHexInteractiveQuickInfoContent`

Can be implemented by quick info content

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Intellisense.IHexInteractiveQuickInfoContent and call its members.
var instance = new dnSpy.Contracts.Hex.Intellisense.IHexInteractiveQuickInfoContent(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexInteractiveQuickInfoContent.cs` (line 24)

### Properties

- `bool IsMouseOverAggregated { get; }`
  - Summary: true if mouse is over the content
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexInteractiveQuickInfoContent.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMouseOverAggregated;
    ```
- `bool KeepQuickInfoOpen { get; }`
  - Summary: true to keep quick info open
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexInteractiveQuickInfoContent.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.KeepQuickInfoOpen;
    ```

## Interface `IHexPopupIntellisensePresenter`

Popup

**Inherits/Implements:** `IHexIntellisensePresenter`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Hex.Intellisense.IHexPopupIntellisensePresenter and call its members.
var instance = new dnSpy.Contracts.Hex.Intellisense.IHexPopupIntellisensePresenter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexPopupIntellisensePresenter.cs` (line 30)

### Properties

- `HexBufferSpanSelection PresentationSpan { get; }`
  - Summary: Gets the presentation span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexPopupIntellisensePresenter.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PresentationSpan;
    ```
- `UIElement SurfaceElement { get; }`
  - Summary: Gets the UI element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexPopupIntellisensePresenter.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SurfaceElement;
    ```
- `VSTA.PopupStyles PopupStyles { get; }`
  - Summary: Gets the popup style
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexPopupIntellisensePresenter.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PopupStyles;
    ```
- `double Opacity { get; set; }`
  - Summary: Gets/sets the opacity
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexPopupIntellisensePresenter.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Opacity;
    ```
- `string SpaceReservationManagerName { get; }`
  - Summary: Gets the name of the
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexPopupIntellisensePresenter.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SpaceReservationManagerName;
    ```

### Events

- `event EventHandler PresentationSpanChanged`
  - Summary: Raised after is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexPopupIntellisensePresenter.cs` (line 49)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PresentationSpanChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler SurfaceElementChanged`
  - Summary: Raised after is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexPopupIntellisensePresenter.cs` (line 39)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.SurfaceElementChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `event EventHandler<VSLI.ValueChangedEventArgs<VSTA.PopupStyles>> PopupStylesChanged`
  - Summary: Raised after is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/IHexPopupIntellisensePresenter.cs` (line 59)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PopupStylesChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `PredefinedHexIntellisensePresenterProviders`

Names of s

**Example**

```csharp
// Access dnSpy.Contracts.Hex.Intellisense.PredefinedHexIntellisensePresenterProviders members directly without instantiation.
dnSpy.Contracts.Hex.Intellisense.PredefinedHexIntellisensePresenterProviders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/PredefinedHexIntellisensePresenterProviders.cs` (line 24)

### Fields

- `public const string DefaultQuickInfoPresenter = "Default Quick Info Presenter"`
  - Summary: Name of default quick info presenter provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Hex/Intellisense/PredefinedHexIntellisensePresenterProviders.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Hex.Intellisense.PredefinedHexIntellisensePresenterProviders.DefaultQuickInfoPresenter;
    ```

