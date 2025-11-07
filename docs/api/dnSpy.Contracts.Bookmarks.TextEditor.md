# Namespace `dnSpy.Contracts.Bookmarks.TextEditor`

## Class `BookmarkGlyphTextMarkerLocationProvider`

Creates s. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.TextEditor.BookmarkGlyphTextMarkerLocationProvider and call its members.
var instance = new dnSpy.Contracts.Bookmarks.TextEditor.BookmarkGlyphTextMarkerLocationProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/BookmarkGlyphTextMarkerLocationProvider.cs` (line 29)

### Methods

- `public abstract GlyphTextMarkerLocationInfo GetLocation(Bookmark bookmark)`
  - Summary: Gets the location of the bookmark or null
  - Parameters:
    - `Bookmark bookmark`: Bookmark
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/BookmarkGlyphTextMarkerLocationProvider.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLocation(bookmark: /* Bookmark */);
    ```

## Class `ExportBookmarkGlyphTextMarkerLocationProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IBookmarkGlyphTextMarkerLocationProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.TextEditor.ExportBookmarkGlyphTextMarkerLocationProviderAttribute(order: /* double */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/BookmarkGlyphTextMarkerLocationProvider.cs` (line 47)

### Constructors

- `public ExportBookmarkGlyphTextMarkerLocationProviderAttribute(double order = double.MaxValue)`
  - Summary: Constructor
  - Parameters:
    - `double order` (default: `double.MaxValue`): Order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/BookmarkGlyphTextMarkerLocationProvider.cs` (line 53)

### Properties

- `public double Order { get; }`
  - Summary: Order
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/BookmarkGlyphTextMarkerLocationProvider.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IBookmarkGlyphTextMarkerLocationProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.TextEditor.IBookmarkGlyphTextMarkerLocationProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Bookmarks.TextEditor.IBookmarkGlyphTextMarkerLocationProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/BookmarkGlyphTextMarkerLocationProvider.cs` (line 39)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/BookmarkGlyphTextMarkerLocationProvider.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `TextViewBookmarkLocationProvider`

Creates bookmark locations in text views

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.TextEditor.TextViewBookmarkLocationProvider and call its members.
var instance = new dnSpy.Contracts.Bookmarks.TextEditor.TextViewBookmarkLocationProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/TextViewBookmarkLocationProvider.cs` (line 29)

### Methods

- `public abstract TextViewBookmarkLocationResult? CreateLocation(IDocumentTab tab, ITextView textView, VirtualSnapshotPoint position)`
  - Summary: Creates a new instance whose text view span is >=
  - Parameters:
    - `IDocumentTab tab`: Tab
    - `ITextView textView`: Text view
    - `VirtualSnapshotPoint position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/TextViewBookmarkLocationProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateLocation(tab: /* IDocumentTab */, textView: /* ITextView */, position: /* VirtualSnapshotPoint */);
    ```

## Struct `TextViewBookmarkLocationResult`

Text view location

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.TextEditor.TextViewBookmarkLocationResult(location: /* BookmarkLocation */, span: /* SnapshotSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/TextViewBookmarkLocationProvider.cs` (line 43)

### Constructors

- `public TextViewBookmarkLocationResult(BookmarkLocation location, SnapshotSpan span)`
  - Summary: Constructor
  - Parameters:
    - `BookmarkLocation location`: Location
    - `SnapshotSpan span`: Text view span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/TextViewBookmarkLocationProvider.cs` (line 59)
- `public TextViewBookmarkLocationResult(BookmarkLocation location, VirtualSnapshotSpan span)`
  - Summary: Constructor
  - Parameters:
    - `BookmarkLocation location`: Location
    - `VirtualSnapshotSpan span`: Text view span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/TextViewBookmarkLocationProvider.cs` (line 71)

### Properties

- `public BookmarkLocation Location { get; }`
  - Summary: Gets the bookmark location
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/TextViewBookmarkLocationProvider.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Location;
    ```
- `public VirtualSnapshotSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/TextEditor/TextViewBookmarkLocationProvider.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

