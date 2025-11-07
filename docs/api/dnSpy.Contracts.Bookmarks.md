# Namespace `dnSpy.Contracts.Bookmarks`

## Class `BMObject`

Base class of bookmark objects

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.BMObject();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 29)

### Constructors

- `protected BMObject()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 36)

### Methods

- `protected abstract void CloseCore()`
  - Summary: Called by after it has raised and before it disposes of all data.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.CloseCore();
    ```
- `public T GetData<T>() where T : class`
  - Summary: Gets existing data or throws if the data doesn't exist
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    instance.GetData();
    ```
- `public T GetOrCreateData<T>() where T : class, new()`
  - Summary: Gets or creates data. If it implements , it will get disposed when this object gets closed.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateData();
    ```
- `public T GetOrCreateData<T>(Func<T> create) where T : class`
  - Summary: Gets or creates data. If it implements , it will get disposed when this object gets closed.
  - Parameters:
    - `Func<T> create`: Creates the data if it doesn't exist
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 148)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateData(create: /* Func<T> */);
    ```
- `public bool HasData<T>() where T : class`
  - Summary: Checks if the data exists or is null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    instance.HasData();
    ```
- `public bool TryGetData<T>(out T value) where T : class`
  - Summary: Gets data
  - Parameters:
    - `out T value`: Result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 114)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetData(value: /* T */);
    ```
- `public void Close()`
  - Summary: Closes the instance. This method must only be executed on the dispatcher thread This method must only be called by the owner object.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```

### Properties

- `public bool IsClosed => isClosed != 0`
  - Summary: true if the instance has been closed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsClosed;
    ```

### Events

- `public event EventHandler Closed`
  - Summary: Raised when it's closed. Data methods eg. can be called but some other methods could throw or can't be called. After all handlers have been notified, all data get disposed (if they implement ).
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BMObject.cs` (line 58)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.Closed += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `Bookmark`

Bookmark

**Inherits/Implements:** `BMObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.Bookmark and call its members.
var instance = new dnSpy.Contracts.Bookmarks.Bookmark(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Bookmark.cs` (line 26)

### Methods

- `public abstract void Remove()`
  - Summary: Removes the bookmark
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Bookmark.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove();
    ```

### Properties

- `public abstract BookmarkLocation Location { get; }`
  - Summary: Gets the bookmark location
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Bookmark.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Location;
    ```
- `public abstract BookmarkSettings Settings { get; set; }`
  - Summary: Gets/sets the current settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Bookmark.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```
- `public abstract ReadOnlyCollection<string> Labels { get; set; }`
  - Summary: Labels
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Bookmark.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Labels;
    ```
- `public abstract bool IsEnabled { get; set; }`
  - Summary: true if the bookmark is enabled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Bookmark.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnabled;
    ```
- `public abstract int Id { get; }`
  - Summary: Gets the unique bookmark id
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Bookmark.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```
- `public abstract string Name { get; set; }`
  - Summary: Name of the bookmark
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Bookmark.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Struct `BookmarkAndOldSettings`

Bookmark and old settings

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.BookmarkAndOldSettings(bookmark: /* Bookmark */, oldSettings: /* BookmarkSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 105)

### Constructors

- `public BookmarkAndOldSettings(Bookmark bookmark, BookmarkSettings oldSettings)`
  - Summary: Constructor
  - Parameters:
    - `Bookmark bookmark`: Bookmark
    - `BookmarkSettings oldSettings`: Old settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 121)

### Properties

- `public Bookmark Bookmark { get; }`
  - Summary: Gets the bookmark
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 109)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Bookmark;
    ```
- `public BookmarkSettings OldSettings { get; }`
  - Summary: Gets the old settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 114)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OldSettings;
    ```

## Struct `BookmarkAndSettings`

Bookmark and settings

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.BookmarkAndSettings(bookmark: /* Bookmark */, settings: /* BookmarkSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 147)

### Constructors

- `public BookmarkAndSettings(Bookmark bookmark, BookmarkSettings settings)`
  - Summary: Constructor
  - Parameters:
    - `Bookmark bookmark`: Bookmark
    - `BookmarkSettings settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 163)

### Properties

- `public Bookmark Bookmark { get; }`
  - Summary: Gets the bookmark
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 151)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Bookmark;
    ```
- `public BookmarkSettings Settings { get; }`
  - Summary: Gets the new settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 156)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```

## Class `BookmarkDisplaySettings`

Bookmark display settings

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.BookmarkDisplaySettings and call its members.
var instance = new dnSpy.Contracts.Bookmarks.BookmarkDisplaySettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 26)

### Methods

- `protected void OnPropertyChanged(string propName)`
  - Summary: Raises
  - Parameters:
    - `string propName`: Name of property that got changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propName: /* string */);
    ```

### Properties

- `public abstract bool ShowDeclaringTypes { get; set; }`
  - Summary: Show declaring types
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowDeclaringTypes;
    ```
- `public abstract bool ShowIntrinsicTypeKeywords { get; set; }`
  - Summary: Show intrinsic type keywords (eg. int instead of Int32)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowIntrinsicTypeKeywords;
    ```
- `public abstract bool ShowModuleNames { get; set; }`
  - Summary: Show module names
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowModuleNames;
    ```
- `public abstract bool ShowNamespaces { get; set; }`
  - Summary: Show namespaces
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowNamespaces;
    ```
- `public abstract bool ShowParameterNames { get; set; }`
  - Summary: Show parameter names
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowParameterNames;
    ```
- `public abstract bool ShowParameterTypes { get; set; }`
  - Summary: Show parameter types
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowParameterTypes;
    ```
- `public abstract bool ShowReturnTypes { get; set; }`
  - Summary: Show return types
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowReturnTypes;
    ```
- `public abstract bool ShowTokens { get; set; }`
  - Summary: Show metadata tokens
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowTokens;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkDisplaySettings.cs` (line 30)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `BookmarkInfo`

Info needed to add a bookmark

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.BookmarkInfo(location: /* BookmarkLocation */, settings: /* BookmarkSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 172)

### Constructors

- `public BookmarkInfo(BookmarkLocation location, BookmarkSettings settings)`
  - Summary: Constructor
  - Parameters:
    - `BookmarkLocation location`: Bookmark location
    - `BookmarkSettings settings`: Bookmark settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 188)

### Properties

- `public BookmarkLocation Location { get; }`
  - Summary: Bookmark location
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 176)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Location;
    ```
- `public BookmarkSettings Settings { get; }`
  - Summary: Bookmark settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 181)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```

## Class `BookmarkLocation`

Bookmark location

**Inherits/Implements:** `BMObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.BookmarkLocation and call its members.
var instance = new dnSpy.Contracts.Bookmarks.BookmarkLocation(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocation.cs` (line 24)

### Methods

- `public abstract override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocation.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public abstract override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocation.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public abstract string Type { get; }`
  - Summary: Unique type, see . There should be a 1-1 correspondence between this string and the derived type.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocation.cs` (line 29)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```

## Class `BookmarkLocationFormatter`

Formats some columns in the bookmarks window

**Inherits/Implements:** `INotifyPropertyChanged`, `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.BookmarkLocationFormatter and call its members.
var instance = new dnSpy.Contracts.Bookmarks.BookmarkLocationFormatter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatter.cs` (line 28)

### Methods

- `protected void RaiseLocationChanged()`
  - Summary: Called when the location needs to be reformatted
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatter.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.RaiseLocationChanged();
    ```
- `protected void RaiseModuleChanged()`
  - Summary: Called when the module needs to be reformatted
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatter.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.RaiseModuleChanged();
    ```
- `public abstract void Dispose()`
  - Summary: Called when this instance isn't needed anymore
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatter.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```
- `public abstract void WriteLocation(ITextColorWriter output, BookmarkLocationFormatterOptions options)`
  - Summary: Writes the location shown in the Location column
  - Parameters:
    - `ITextColorWriter output`: Output
    - `BookmarkLocationFormatterOptions options`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatter.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLocation(output: /* ITextColorWriter */, options: /* BookmarkLocationFormatterOptions */);
    ```
- `public abstract void WriteModule(ITextColorWriter output)`
  - Summary: Writes the module shown in the Module column
  - Parameters:
    - `ITextColorWriter output`: Output
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatter.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteModule(output: /* ITextColorWriter */);
    ```

### Fields

- `public const string LocationProperty = nameof(LocationProperty)`
  - Summary: Name of the Location property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatter.cs` (line 32)
  - Example:
    ```csharp
    var value = instance.LocationProperty;
    ```
- `public const string ModuleProperty = nameof(ModuleProperty)`
  - Summary: Name of the Module property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatter.cs` (line 37)
  - Example:
    ```csharp
    var value = instance.ModuleProperty;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatter.cs` (line 42)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Enum `BookmarkLocationFormatterOptions`

Formatter options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.BookmarkLocationFormatterOptions and call its members.
var instance = new dnSpy.Contracts.Bookmarks.BookmarkLocationFormatterOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatter.cs` (line 78)

### Members

- `None`: No bit is set
- `Tokens` = `x00000001`: Show metadata tokens
- `ModuleNames` = `x00000002`: Show module names
- `ParameterTypes` = `x00000004`: Show parameter types
- `ParameterNames` = `x00000008`: Show parameter names
- `DeclaringTypes` = `x00000010`: Show declaring types
- `ReturnTypes` = `x00000020`: Show return types
- `Namespaces` = `x00000040`: Show namespaces
- `IntrinsicTypeKeywords` = `x00000080`: Show intrinsic type keywords (eg. int instead of Int32)
- `DigitSeparators` = `x00000100`: Use digit separators
- `Decimal` = `x00000200`: Use decimal instead of hexadecimal

## Class `BookmarkLocationFormatterProvider`

Creates formatters. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.BookmarkLocationFormatterProvider and call its members.
var instance = new dnSpy.Contracts.Bookmarks.BookmarkLocationFormatterProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatterProvider.cs` (line 28)

### Methods

- `public abstract BookmarkLocationFormatter Create(BookmarkLocation location)`
  - Summary: Returns a formatter or null
  - Parameters:
    - `BookmarkLocation location`: Bookmark location
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatterProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(location: /* BookmarkLocation */);
    ```

## Class `BookmarkLocationSerializer`

serializer. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.BookmarkLocationSerializer and call its members.
var instance = new dnSpy.Contracts.Bookmarks.BookmarkLocationSerializer(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationSerializer.cs` (line 29)

### Methods

- `public abstract BookmarkLocation Deserialize(ISettingsSection section)`
  - Summary: Deserializes a bookmark location or returns null if it failed
  - Parameters:
    - `ISettingsSection section`: Serialized section
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationSerializer.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Deserialize(section: /* ISettingsSection */);
    ```
- `public abstract void Serialize(ISettingsSection section, BookmarkLocation location)`
  - Summary: Serializes
  - Parameters:
    - `ISettingsSection section`: Destination section
    - `BookmarkLocation location`: Bookmark location
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationSerializer.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Serialize(section: /* ISettingsSection */, location: /* BookmarkLocation */);
    ```

## Struct `BookmarkSettings`

Bookmark settings

**Inherits/Implements:** `IEquatable<BookmarkSettings>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.BookmarkSettings and call its members.
var instance = new dnSpy.Contracts.Bookmarks.BookmarkSettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkSettings.cs` (line 27)

### Methods

- `public bool Equals(BookmarkSettings other)`
  - Summary: Compares this instance to
  - Parameters:
    - `BookmarkSettings other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkSettings.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* BookmarkSettings */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkSettings.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkSettings.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public ReadOnlyCollection<string> Labels { get; set; }`
  - Summary: Labels
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkSettings.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Labels;
    ```
- `public bool IsEnabled { get; set; }`
  - Summary: true if the bookmark is enabled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkSettings.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnabled;
    ```
- `public string Name { get; set; }`
  - Summary: Name of the bookmark
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkSettings.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

### Operators

- `public static bool operator !=(BookmarkSettings left, BookmarkSettings right) => !left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkSettings.cs` (line 45)
- `public static bool operator ==(BookmarkSettings left, BookmarkSettings right) => left.Equals(right);`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkSettings.cs` (line 44)

## Struct `BookmarksModifiedEventArgs`

Bookmarks modified event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.BookmarksModifiedEventArgs(bookmarks: /* ReadOnlyCollection<BookmarkAndOldSettings> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 130)

### Constructors

- `public BookmarksModifiedEventArgs(ReadOnlyCollection<BookmarkAndOldSettings> bookmarks)`
  - Summary: Constructor
  - Parameters:
    - `ReadOnlyCollection<BookmarkAndOldSettings> bookmarks`: Bookmarks and old settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 140)

### Properties

- `public ReadOnlyCollection<BookmarkAndOldSettings> Bookmarks { get; }`
  - Summary: Gets the bookmarks
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Bookmarks;
    ```

## Class `BookmarksService`

Bookmarks service

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.BookmarksService and call its members.
var instance = new dnSpy.Contracts.Bookmarks.BookmarksService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 28)

### Methods

- `public Bookmark Add(BookmarkInfo bookmark)`
  - Summary: Adds a bookmark. If the bookmark already exists, null is returned.
  - Parameters:
    - `BookmarkInfo bookmark`: Bookmark info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(bookmark: /* BookmarkInfo */);
    ```
- `public abstract Bookmark[] Add(BookmarkInfo[] bookmarks)`
  - Summary: Adds bookmarks. Duplicate bookmarks are ignored.
  - Parameters:
    - `BookmarkInfo[] bookmarks`: Bookmarks
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(bookmarks: /* BookmarkInfo[] */);
    ```
- `public abstract void Clear()`
  - Summary: Removes all bookmarks
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```
- `public abstract void Close(BMObject[] objs)`
  - Summary: Closes
  - Parameters:
    - `BMObject[] objs`: Objects to close
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(objs: /* BMObject[] */);
    ```
- `public abstract void Modify(BookmarkAndSettings[] settings)`
  - Summary: Modifies bookmarks
  - Parameters:
    - `BookmarkAndSettings[] settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.Modify(settings: /* BookmarkAndSettings[] */);
    ```
- `public abstract void Remove(Bookmark[] bookmarks)`
  - Summary: Removes bookmarks
  - Parameters:
    - `Bookmark[] bookmarks`: Bookmarks to remove
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(bookmarks: /* Bookmark[] */);
    ```
- `public void Close(BMObject obj)`
  - Summary: Closes
  - Parameters:
    - `BMObject obj`: Object to close
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.Close(obj: /* BMObject */);
    ```
- `public void Modify(Bookmark bookmark, BookmarkSettings settings)`
  - Summary: Modifies a bookmark
  - Parameters:
    - `Bookmark bookmark`: Bookmark
    - `BookmarkSettings settings`: New settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.Modify(bookmark: /* Bookmark */, settings: /* BookmarkSettings */);
    ```
- `public void Remove(Bookmark bookmark)`
  - Summary: Removes a bookmark
  - Parameters:
    - `Bookmark bookmark`: Bookmark to remove
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(bookmark: /* Bookmark */);
    ```

### Properties

- `public abstract Bookmark[] Bookmarks { get; }`
  - Summary: Gets all bookmarks
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Bookmarks;
    ```

### Events

- `public abstract event EventHandler<BookmarksModifiedEventArgs> BookmarksModified`
  - Summary: Raised when bookmarks are modified
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 46)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BookmarksModified += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```
- `public abstract event EventHandler<CollectionChangedEventArgs<Bookmark>> BookmarksChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 56)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.BookmarksChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `BookmarksSettings`

Global bookmarks settings. This class is thread safe. Listeners will be notified on a random thread.

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.BookmarksSettings and call its members.
var instance = new dnSpy.Contracts.Bookmarks.BookmarksSettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksSettings.cs` (line 27)

### Methods

- `protected void OnPropertyChanged(string propName)`
  - Summary: Raises
  - Parameters:
    - `string propName`: Name of property that got changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksSettings.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propName: /* string */);
    ```

### Properties

- `public abstract bool SyntaxHighlight { get; set; }`
  - Summary: true to colorize bookmark tool windows and other bookmark UI objects
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksSettings.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SyntaxHighlight;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Summary: Raised when a property is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksSettings.cs` (line 31)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Struct `CollectionChangedEventArgs<T>`

Contains added or removed objects

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.CollectionChangedEventArgs<T>(objects: /* ReadOnlyCollection<T> */, added: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/CollectionChangedEventArgs.cs` (line 28)

### Constructors

- `public CollectionChangedEventArgs(IList<T> objects, bool added)`
  - Summary: Constructor
  - Parameters:
    - `IList<T> objects`: The objects that got added or removed (see )
    - `bool added`: true if were added, false if they were removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/CollectionChangedEventArgs.cs` (line 54)
- `public CollectionChangedEventArgs(ReadOnlyCollection<T> objects, bool added)`
  - Summary: Constructor
  - Parameters:
    - `ReadOnlyCollection<T> objects`: The objects that got added or removed (see )
    - `bool added`: true if were added, false if they were removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/CollectionChangedEventArgs.cs` (line 44)
- `public CollectionChangedEventArgs(T obj, bool added)`
  - Summary: Constructor
  - Parameters:
    - `T obj`: The object that got added or removed (see )
    - `bool added`: true if was added, false if it was removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/CollectionChangedEventArgs.cs` (line 64)

### Properties

- `public ReadOnlyCollection<T> Objects { get; }`
  - Summary: The objects that got added or removed (see )
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/CollectionChangedEventArgs.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Objects;
    ```
- `public bool Added { get; }`
  - Summary: true if were added, false if they were removed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/CollectionChangedEventArgs.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Added;
    ```

## Class `ExportBookmarkLocationFormatterProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IBookmarkLocationFormatterProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.ExportBookmarkLocationFormatterProviderAttribute(type: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatterProvider.cs` (line 46)

### Constructors

- `public ExportBookmarkLocationFormatterProviderAttribute(string type)`
  - Summary: Constructor
  - Parameters:
    - `string type`: Type (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatterProvider.cs` (line 52)
- `public ExportBookmarkLocationFormatterProviderAttribute(string[] types)`
  - Summary: Constructor
  - Parameters:
    - `string[] types`: Types (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatterProvider.cs` (line 59)

### Properties

- `public string[] Types { get; }`
  - Summary: Types (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatterProvider.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Types;
    ```

## Class `ExportBookmarkLocationSerializerAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IBookmarkLocationSerializerMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.ExportBookmarkLocationSerializerAttribute(type: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationSerializer.cs` (line 54)

### Constructors

- `public ExportBookmarkLocationSerializerAttribute(string type)`
  - Summary: Constructor
  - Parameters:
    - `string type`: Type (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationSerializer.cs` (line 60)
- `public ExportBookmarkLocationSerializerAttribute(string[] types)`
  - Summary: Constructor
  - Parameters:
    - `string[] types`: Types (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationSerializer.cs` (line 67)

### Properties

- `public string[] Types { get; }`
  - Summary: Types (compared against ), see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationSerializer.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Types;
    ```

## Interface `IBookmarkLocationFormatterProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.IBookmarkLocationFormatterProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Bookmarks.IBookmarkLocationFormatterProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatterProvider.cs` (line 38)

### Properties

- `string[] Types { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationFormatterProvider.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Types;
    ```

## Interface `IBookmarkLocationSerializerMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.IBookmarkLocationSerializerMetadata and call its members.
var instance = new dnSpy.Contracts.Bookmarks.IBookmarkLocationSerializerMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationSerializer.cs` (line 46)

### Properties

- `string[] Types { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarkLocationSerializer.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Types;
    ```

## Interface `IBookmarksServiceListener`

Export an instance to get created when gets created

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.IBookmarksServiceListener and call its members.
var instance = new dnSpy.Contracts.Bookmarks.IBookmarksServiceListener(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 197)

### Methods

- `void Initialize(BookmarksService bookmarksService)`
  - Summary: Called once by
  - Parameters:
    - `BookmarksService bookmarksService`: Bookmarks service
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/BookmarksService.cs` (line 202)
  - Example:
    ```csharp
    // Example invocation
    instance.Initialize(bookmarksService: /* BookmarksService */);
    ```

## Class `PredefinedBookmarkLocationTypes`

Predefined types

**Example**

```csharp
// Access dnSpy.Contracts.Bookmarks.PredefinedBookmarkLocationTypes members directly without instantiation.
dnSpy.Contracts.Bookmarks.PredefinedBookmarkLocationTypes./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/PredefinedBookmarkLocationTypes.cs` (line 24)

### Fields

- `public const string DotNetBody = nameof(DotNetBody)`
  - Summary: .NET method body location (module, method token, IL offset)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/PredefinedBookmarkLocationTypes.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Bookmarks.PredefinedBookmarkLocationTypes.DotNetBody;
    ```
- `public const string DotNetToken = nameof(DotNetToken)`
  - Summary: .NET member definition (module, token)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/PredefinedBookmarkLocationTypes.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Bookmarks.PredefinedBookmarkLocationTypes.DotNetToken;
    ```

