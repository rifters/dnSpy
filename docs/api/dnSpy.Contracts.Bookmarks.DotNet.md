# Namespace `dnSpy.Contracts.Bookmarks.DotNet`

## Class `DotNetBookmarkFactory`

Creates bookmarks

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.DotNet.DotNetBookmarkFactory and call its members.
var instance = new dnSpy.Contracts.Bookmarks.DotNet.DotNetBookmarkFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 27)

### Methods

- `public Bookmark Create(ModuleId module, uint token)`
  - Summary: Creates an enabled bookmark. If there's already a bookmark at the location, null is returned.
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a definition (type, method, field, property, event)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleId */, token: /* uint */);
    ```
- `public Bookmark Create(ModuleId module, uint token, BookmarkSettings settings)`
  - Summary: Creates a bookmark. If there's already a bookmark at the location, null is returned.
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a definition (type, method, field, property, event)
    - `BookmarkSettings settings`: Bookmark settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleId */, token: /* uint */, settings: /* BookmarkSettings */);
    ```
- `public Bookmark Create(ModuleId module, uint token, uint offset)`
  - Summary: Creates an enabled bookmark. If there's already a bookmark at the location, null is returned.
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a method within the module
    - `uint offset`: IL offset of the bookmark within the method body
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleId */, token: /* uint */, offset: /* uint */);
    ```
- `public Bookmark Create(ModuleId module, uint token, uint offset, BookmarkSettings settings)`
  - Summary: Creates a bookmark. If there's already a bookmark at the location, null is returned.
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a method within the module
    - `uint offset`: IL offset of the bookmark within the method body
    - `BookmarkSettings settings`: Bookmark settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleId */, token: /* uint */, offset: /* uint */, settings: /* BookmarkSettings */);
    ```
- `public abstract Bookmark[] Create(DotNetMethodBodyBookmarkInfo[] bookmarks)`
  - Summary: Creates bookmarks. Duplicate bookmarks are ignored.
  - Parameters:
    - `DotNetMethodBodyBookmarkInfo[] bookmarks`: Bookmark infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(bookmarks: /* DotNetMethodBodyBookmarkInfo[] */);
    ```
- `public abstract Bookmark[] Create(DotNetTokenBookmarkInfo[] bookmarks)`
  - Summary: Creates bookmarks. Duplicate bookmarks are ignored.
  - Parameters:
    - `DotNetTokenBookmarkInfo[] bookmarks`: Bookmark infos
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(bookmarks: /* DotNetTokenBookmarkInfo[] */);
    ```

## Struct `DotNetMethodBodyBookmarkInfo`

Contains all required data to create a bookmark in a .NET method body

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.DotNet.DotNetMethodBodyBookmarkInfo(module: /* ModuleId */, token: /* uint */, offset: /* uint */, settings: /* BookmarkSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 86)

### Constructors

- `public DotNetMethodBodyBookmarkInfo(ModuleId module, uint token, uint offset, BookmarkSettings settings)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a method within the module
    - `uint offset`: IL offset of the bookmark within the method body
    - `BookmarkSettings settings`: Bookmark settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 114)

### Properties

- `public BookmarkSettings Settings { get; }`
  - Summary: Bookmark settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 105)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```
- `public ModuleId Module { get; }`
  - Summary: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 90)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public uint Offset { get; }`
  - Summary: IL offset of the bookmark within the method body
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 100)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```
- `public uint Token { get; }`
  - Summary: Token of a method within the module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 95)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

## Class `DotNetMethodBodyBookmarkLocation`

.NET method body bookmark location

**Inherits/Implements:** `BookmarkLocation`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.DotNet.DotNetMethodBodyBookmarkLocation and call its members.
var instance = new dnSpy.Contracts.Bookmarks.DotNet.DotNetMethodBodyBookmarkLocation(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkLocation.cs` (line 26)

### Properties

- `public abstract ModuleId Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkLocation.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public abstract uint Offset { get; }`
  - Summary: Gets the IL offset of the bookmark within the method body
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkLocation.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```
- `public abstract uint Token { get; }`
  - Summary: Gets the token of a method within the module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkLocation.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

## Struct `DotNetTokenBookmarkInfo`

Contains all required data to create a bookmark that references a definition (type, method, field, property, event)

**Example**

```csharp
var instance = new dnSpy.Contracts.Bookmarks.DotNet.DotNetTokenBookmarkInfo(module: /* ModuleId */, token: /* uint */, settings: /* BookmarkSettings */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 125)

### Constructors

- `public DotNetTokenBookmarkInfo(ModuleId module, uint token, BookmarkSettings settings)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of a definition (type, method, field, property, event)
    - `BookmarkSettings settings`: Bookmark settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 147)

### Properties

- `public BookmarkSettings Settings { get; }`
  - Summary: Bookmark settings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 139)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```
- `public ModuleId Module { get; }`
  - Summary: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public uint Token { get; }`
  - Summary: Token of a definition (type, method, field, property, event)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkFactory.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

## Class `DotNetTokenBookmarkLocation`

.NET definition (type, method, field, property, event) bookmark location

**Inherits/Implements:** `BookmarkLocation`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Bookmarks.DotNet.DotNetTokenBookmarkLocation and call its members.
var instance = new dnSpy.Contracts.Bookmarks.DotNet.DotNetTokenBookmarkLocation(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkLocation.cs` (line 46)

### Properties

- `public abstract ModuleId Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkLocation.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public abstract uint Token { get; }`
  - Summary: Gets the token of the definition (type, method, field, property, event)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Bookmarks/DotNet/DotNetBookmarkLocation.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

