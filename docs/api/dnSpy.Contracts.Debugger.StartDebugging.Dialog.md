# Namespace `dnSpy.Contracts.Debugger.StartDebugging.Dialog`

## Class `PredefinedGenericDebugEngineOrders`

Returned by

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedGenericDebugEngineOrders members directly without instantiation.
dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedGenericDebugEngineOrders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 133)

### Fields

- `public const double DotNetCore = 1000000`
  - Summary: .NET Core
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 142)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedGenericDebugEngineOrders.DotNetCore;
    ```
- `public const double DotNetFramework = 1000000`
  - Summary: .NET Framework
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 137)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedGenericDebugEngineOrders.DotNetFramework;
    ```
- `public const double DotNetMono = DotNetFramework + 1`
  - Summary: .NET Mono
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 147)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedGenericDebugEngineOrders.DotNetMono;
    ```
- `public const double DotNetUnity = 1000000`
  - Summary: .NET Unity
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 152)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedGenericDebugEngineOrders.DotNetUnity;
    ```

## Class `PredefinedStartDebuggingOptionsPageDisplayOrders`

Predefined options page display order constants

**Example**

```csharp
// Access dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedStartDebuggingOptionsPageDisplayOrders members directly without instantiation.
dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedStartDebuggingOptionsPageDisplayOrders./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/PredefinedStartDebuggingOptionsPageDisplayOrders.cs` (line 24)

### Fields

- `public static readonly double DotNetCore = 101000`
  - Summary: .NET Core debug engine
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/PredefinedStartDebuggingOptionsPageDisplayOrders.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedStartDebuggingOptionsPageDisplayOrders.DotNetCore;
    ```
- `public static readonly double DotNetFramework = 100000`
  - Summary: .NET Framework debug engine
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/PredefinedStartDebuggingOptionsPageDisplayOrders.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedStartDebuggingOptionsPageDisplayOrders.DotNetFramework;
    ```
- `public static readonly double DotNetMono = 110000`
  - Summary: Mono debug engine (start executable)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/PredefinedStartDebuggingOptionsPageDisplayOrders.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedStartDebuggingOptionsPageDisplayOrders.DotNetMono;
    ```
- `public static readonly double DotNetMonoConnect = 111000`
  - Summary: Mono debug engine (connect to a waiting executable)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/PredefinedStartDebuggingOptionsPageDisplayOrders.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedStartDebuggingOptionsPageDisplayOrders.DotNetMonoConnect;
    ```
- `public static readonly double DotNetUnity = 102000`
  - Summary: Unity debug engine (start executable)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/PredefinedStartDebuggingOptionsPageDisplayOrders.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedStartDebuggingOptionsPageDisplayOrders.DotNetUnity;
    ```
- `public static readonly double DotNetUnityConnect = 103000`
  - Summary: Unity debug engine (connect to a waiting executable)
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/PredefinedStartDebuggingOptionsPageDisplayOrders.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Debugger.StartDebugging.Dialog.PredefinedStartDebuggingOptionsPageDisplayOrders.DotNetUnityConnect;
    ```

## Struct `StartDebuggingOptionsInfo`

Contains the options and an optional filename

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.StartDebugging.Dialog.StartDebuggingOptionsInfo(options: /* StartDebuggingOptions */, filename: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 108)

### Constructors

- `public StartDebuggingOptionsInfo(StartDebuggingOptions options, string filename = null)`
  - Summary: Constructor
  - Parameters:
    - `StartDebuggingOptions options`: Options
    - `string filename` (default: `null`): Filename or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 124)

### Properties

- `public StartDebuggingOptions Options { get; }`
  - Summary: Gets the options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 112)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```
- `public string Filename { get; }`
  - Summary: Filename or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 117)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```

## Class `StartDebuggingOptionsPage`

A page shown in the 'debug an application' dialog box. It provides a UI object and creates a instance that is used to start the application.

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.StartDebugging.Dialog.StartDebuggingOptionsPage and call its members.
var instance = new dnSpy.Contracts.Debugger.StartDebugging.Dialog.StartDebuggingOptionsPage(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 29)

### Methods

- `protected void OnPropertyChanged(string propName)`
  - Summary: Raises
  - Parameters:
    - `string propName`: Name of property that got changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propName: /* string */);
    ```
- `public abstract StartDebuggingOptionsInfo GetOptions()`
  - Summary: Gets all options. This method is only called if returns true
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptions();
    ```
- `public abstract bool SupportsDebugEngine(Guid engineGuid, out double order)`
  - Summary: Returns true if this is a debug engine page that is compatible with a debug engine (see eg. )
  - Parameters:
    - `Guid engineGuid`: Generic debug engine guid (see )
    - `out double order`: Only used if the method returns true and is the order to use if more than one instance returns true. (see )
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.SupportsDebugEngine(engineGuid: /* Guid */, order: /* double */);
    ```
- `public abstract void InitializeDefaultOptions(string filename, string breakKind, StartDebuggingOptions options)`
  - Summary: Initializes this instance to default options. If is not an EXE file, then should be used to initialize this instance, else should be ignored.
  - Parameters:
    - `string filename`: Filename
    - `string breakKind`: Default break kind, see
    - `StartDebuggingOptions options`: Options or null
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializeDefaultOptions(filename: /* string */, breakKind: /* string */, options: /* StartDebuggingOptions */);
    ```
- `public abstract void InitializePreviousOptions(StartDebuggingOptions options)`
  - Summary: Initializes this instance to previous options
  - Parameters:
    - `StartDebuggingOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializePreviousOptions(options: /* StartDebuggingOptions */);
    ```
- `public virtual void OnClose()`
  - Summary: Called when the dialog box gets closed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.OnClose();
    ```

### Properties

- `public abstract Guid Guid { get; }`
  - Summary: Guid of this page
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `public abstract bool IsValid { get; }`
  - Summary: true if all options are valid and can be called. gets raised when this property is changed.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsValid;
    ```
- `public abstract double DisplayOrder { get; }`
  - Summary: Display order of the UI object compared to other instances, see
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DisplayOrder;
    ```
- `public abstract object UIObject { get; }`
  - Summary: Gets the UI object
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UIObject;
    ```
- `public abstract string DisplayName { get; }`
  - Summary: Name of debug engine shown in the UI, eg. ".NET Framework" or ".NET Core" or "Mono"
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DisplayName;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised after a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPage.cs` (line 33)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `StartDebuggingOptionsPageContext`

Passed to a instance

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.StartDebugging.Dialog.StartDebuggingOptionsPageContext(currentFilename: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPageContext.cs` (line 26)

### Constructors

- `public StartDebuggingOptionsPageContext(string currentFilename)`
  - Summary: Constructor
  - Parameters:
    - `string currentFilename`: Filename of the current selected file or an empty string
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPageContext.cs` (line 36)

### Properties

- `public string CurrentFilename { get; }`
  - Summary: Filename of the current selected file or an empty string
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPageContext.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CurrentFilename;
    ```

## Class `StartDebuggingOptionsPageProvider`

Creates instances. See also

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.StartDebugging.Dialog.StartDebuggingOptionsPageProvider and call its members.
var instance = new dnSpy.Contracts.Debugger.StartDebugging.Dialog.StartDebuggingOptionsPageProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPageProvider.cs` (line 26)

### Methods

- `public abstract IEnumerable<StartDebuggingOptionsPage> Create(StartDebuggingOptionsPageContext context)`
  - Summary: Creates new instances
  - Parameters:
    - `StartDebuggingOptionsPageContext context`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/StartDebugging/Dialog/StartDebuggingOptionsPageProvider.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(context: /* StartDebuggingOptionsPageContext */);
    ```

