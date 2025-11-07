# Namespace `dnSpy.Contracts.Bookmarks.Navigator`

## Class `BookmarkDocument`

Bookmark document

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.Navigator.BookmarkDocument and call its members.
var instance = new dnSpy.Contracts.Bookmarks.Navigator.BookmarkDocument(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkDocument.cs` (line 24)

### Methods

- `public abstract override bool Equals(object obj)`
  - Summary: Compares this instance to
  - Parameters:
    - `object obj`: Object
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkDocument.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public abstract override int GetHashCode()`
  - Summary: Gets the hash code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkDocument.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

## Class `BookmarkDocumentProvider`

Creates s. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.Navigator.BookmarkDocumentProvider and call its members.
var instance = new dnSpy.Contracts.Bookmarks.Navigator.BookmarkDocumentProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkDocumentProvider.cs` (line 28)

### Methods

- `public abstract BookmarkDocument GetDocument(Bookmark bookmark)`
  - Summary: Gets the document or null if it's unknown. This method is called on the UI thread.
  - Parameters:
    - `Bookmark bookmark`: Bookmark
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkDocumentProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDocument(bookmark: /* Bookmark */);
    ```

## Class `BookmarkNavigator`

Selects the next or previous bookmark

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.Navigator.BookmarkNavigator and call its members.
var instance = new dnSpy.Contracts.Bookmarks.Navigator.BookmarkNavigator(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 26)

### Methods

- `public abstract void SelectNextBookmark()`
  - Summary: Select the next bookmark
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectNextBookmark();
    ```
- `public abstract void SelectNextBookmarkInDocument()`
  - Summary: Select the next bookmark in the document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectNextBookmarkInDocument();
    ```
- `public abstract void SelectNextBookmarkWithSameLabel()`
  - Summary: Select the next bookmark with the same label
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectNextBookmarkWithSameLabel();
    ```
- `public abstract void SelectPreviousBookmark()`
  - Summary: Select the previous bookmark
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectPreviousBookmark();
    ```
- `public abstract void SelectPreviousBookmarkInDocument()`
  - Summary: Select the previous bookmark in the document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectPreviousBookmarkInDocument();
    ```
- `public abstract void SelectPreviousBookmarkWithSameLabel()`
  - Summary: Select the previous bookmark with the same label
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.SelectPreviousBookmarkWithSameLabel();
    ```

### Properties

- `public abstract Bookmark ActiveBookmark { get; set; }`
  - Summary: Current active bookmark. It's null if there are no bookmarks or no bookmarks are visible in the UI
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveBookmark;
    ```
- `public abstract bool CanSelectNextBookmark { get; }`
  - Summary: true if can be called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanSelectNextBookmark;
    ```
- `public abstract bool CanSelectNextBookmarkInDocument { get; }`
  - Summary: true if can be called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanSelectNextBookmarkInDocument;
    ```
- `public abstract bool CanSelectNextBookmarkWithSameLabel { get; }`
  - Summary: true if can be called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 90)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanSelectNextBookmarkWithSameLabel;
    ```
- `public abstract bool CanSelectPreviousBookmark { get; }`
  - Summary: true if can be called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanSelectPreviousBookmark;
    ```
- `public abstract bool CanSelectPreviousBookmarkInDocument { get; }`
  - Summary: true if can be called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanSelectPreviousBookmarkInDocument;
    ```
- `public abstract bool CanSelectPreviousBookmarkWithSameLabel { get; }`
  - Summary: true if can be called
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanSelectPreviousBookmarkWithSameLabel;
    ```

### Events

- `public abstract event EventHandler ActiveBookmarkChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkNavigator.cs` (line 35)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.ActiveBookmarkChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `ExportBookmarkDocumentProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IBookmarkDocumentProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.Navigator.ExportBookmarkDocumentProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkDocumentProvider.cs` (line 46)

### Constructors

- `public ExportBookmarkDocumentProviderAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkDocumentProvider.cs` (line 52)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkDocumentProvider.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IBookmarkDocumentProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.Navigator.IBookmarkDocumentProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Bookmarks.Navigator.IBookmarkDocumentProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkDocumentProvider.cs` (line 38)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/Navigator/BookmarkDocumentProvider.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

