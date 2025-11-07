# Namespace `dnSpy.Contracts.Documents.TreeView.Resources`

## Class `BuiltInResourceElementNode`

A resource created from a

**Inherits/Implements:** `ResourceElementNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.BuiltInResourceElementNode(treeNodeGroup: /* ITreeNodeGroup */, resourceElement: /* ResourceElement */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/BuiltInResourceElementNode.cs` (line 27)

### Constructors

- `protected BuiltInResourceElementNode(ITreeNodeGroup treeNodeGroup, ResourceElement resourceElement)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `ResourceElement resourceElement`: Resource element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/BuiltInResourceElementNode.cs` (line 33)

## Class `ExportResourceNodeProviderAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IResourceNodeProviderMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.ExportResourceNodeProviderAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeProvider.cs` (line 60)

### Constructors

- `public ExportResourceNodeProviderAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeProvider.cs` (line 63)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeProvider.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IResourceDataProvider`

Implemented by all resource nodes, and contains all raw data, RVA, and size

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.Resources.IResourceDataProvider and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.IResourceDataProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceDataProvider.cs` (line 28)

### Methods

- `IEnumerable<ResourceData> GetResourceData(ResourceDataType type)`
  - Summary: Gets the resource data
  - Parameters:
    - `ResourceDataType type`: Type of data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceDataProvider.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResourceData(type: /* ResourceDataType */);
    ```
- `string ToString(CancellationToken token, bool canDecompile)`
  - Summary: Used by the searcher. Should only return a string if the data is text or compiled text. I.e., null should be returned if it's an , but a string if it's eg. an XML doc.
  - Parameters:
    - `CancellationToken token`: Cancellation token
    - `bool canDecompile`: true if the callee can decompile (eg. XAML), false otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceDataProvider.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString(token: /* CancellationToken */, canDecompile: /* bool */);
    ```
- `void WriteShort(IDecompilerOutput output, IDecompiler decompiler, bool showOffset)`
  - Summary: Write a short string (typically one line) to
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `IDecompiler decompiler`: Decompiler
    - `bool showOffset`: true to write offset and size of resource in the PE image, if that info is available
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceDataProvider.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteShort(output: /* IDecompilerOutput */, decompiler: /* IDecompiler */, showOffset: /* bool */);
    ```

### Properties

- `uint FileOffset { get; }`
  - Summary: File offset of resource or 0
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceDataProvider.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FileOffset;
    ```
- `uint Length { get; }`
  - Summary: Length of the resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceDataProvider.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `uint RVA { get; }`
  - Summary: RVA of resource or 0
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceDataProvider.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RVA;
    ```

## Interface `IResourceNodeFactory`

Creates resource nodes

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.Resources.IResourceNodeFactory and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.IResourceNodeFactory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeFactory.cs` (line 28)

### Methods

- `ResourceElementNode Create(ModuleDef module, ResourceElement resourceElement, ITreeNodeGroup treeNodeGroup)`
  - Summary: Creates a instance. Pass it to
  - Parameters:
    - `ModuleDef module`: Owner module
    - `ResourceElement resourceElement`: Resource
    - `ITreeNodeGroup treeNodeGroup`: Group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeFactory.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleDef */, resourceElement: /* ResourceElement */, treeNodeGroup: /* ITreeNodeGroup */);
    ```
- `ResourceNode Create(ModuleDef module, Resource resource, ITreeNodeGroup treeNodeGroup)`
  - Summary: Creates a instance. Pass it to
  - Parameters:
    - `ModuleDef module`: Owner module
    - `Resource resource`: Resource
    - `ITreeNodeGroup treeNodeGroup`: Group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeFactory.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleDef */, resource: /* Resource */, treeNodeGroup: /* ITreeNodeGroup */);
    ```

## Interface `IResourceNodeProvider`

Creates resource nodes. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.Resources.IResourceNodeProvider and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.IResourceNodeProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeProvider.cs` (line 31)

### Methods

- `ResourceElementNode Create(ModuleDef module, ResourceElement resourceElement, ITreeNodeGroup treeNodeGroup)`
  - Summary: Creates a instance or returns null
  - Parameters:
    - `ModuleDef module`: Owner module
    - `ResourceElement resourceElement`: Resource
    - `ITreeNodeGroup treeNodeGroup`: Group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeProvider.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleDef */, resourceElement: /* ResourceElement */, treeNodeGroup: /* ITreeNodeGroup */);
    ```
- `ResourceNode Create(ModuleDef module, Resource resource, ITreeNodeGroup treeNodeGroup)`
  - Summary: Creates a instance or returns null
  - Parameters:
    - `ModuleDef module`: Owner module
    - `Resource resource`: Resource
    - `ITreeNodeGroup treeNodeGroup`: Group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeProvider.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(module: /* ModuleDef */, resource: /* Resource */, treeNodeGroup: /* ITreeNodeGroup */);
    ```

## Interface `IResourceNodeProviderMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.Resources.IResourceNodeProviderMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.IResourceNodeProviderMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeProvider.cs` (line 52)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/IResourceNodeProvider.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ImageListOptions`

options

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.ImageListOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageListOptions.cs` (line 29)

### Constructors

- `public ImageListOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageListOptions.cs` (line 59)
- `public ImageListOptions(ImageListOptions other)`
  - Summary: Constructor
  - Parameters:
    - `ImageListOptions other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageListOptions.cs` (line 70)

### Properties

- `public ColorDepth ColorDepth { get; set; }`
  - Summary: Gets/sets the color depth
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageListOptions.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ColorDepth;
    ```
- `public List<ImageSource> ImageSources => imageSources`
  - Summary: Gets the images
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageListOptions.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageSources;
    ```
- `public Size ImageSize { get; set; }`
  - Summary: Gets/sets the image size
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageListOptions.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageSize;
    ```
- `public System.Drawing.Color TransparentColor { get; set; }`
  - Summary: Gets/sets the transparent color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageListOptions.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TransparentColor;
    ```
- `public string Name { get; set; }`
  - Summary: Gets/sets the name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageListOptions.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `ImageResourceElementNode`

A resource node created from an image

**Inherits/Implements:** `ResourceElementNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.ImageResourceElementNode(treeNodeGroup: /* ITreeNodeGroup */, resourceElement: /* ResourceElement */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageResourceElementNode.cs` (line 27)

### Constructors

- `protected ImageResourceElementNode(ITreeNodeGroup treeNodeGroup, ResourceElement resourceElement)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `ResourceElement resourceElement`: Resource element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageResourceElementNode.cs` (line 33)

## Class `ImageResourceNode`

A resource node created from an image

**Inherits/Implements:** `ResourceNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.ImageResourceNode(treeNodeGroup: /* ITreeNodeGroup */, resource: /* EmbeddedResource */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageResourceNode.cs` (line 27)

### Constructors

- `protected ImageResourceNode(ITreeNodeGroup treeNodeGroup, EmbeddedResource resource)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `EmbeddedResource resource`: Resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageResourceNode.cs` (line 33)

## Class `ImageResourceUtilities`

Resource image utils

**Example**

```csharp
// Access dnSpy.Contracts.Documents.TreeView.Resources.ImageResourceUtilities members directly without instantiation.
dnSpy.Contracts.Documents.TreeView.Resources.ImageResourceUtilities./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageResourceUtilities.cs` (line 29)

### Methods

- `public static ImageSource CreateImageSource(byte[] data)`
  - Summary: Creates a
  - Parameters:
    - `byte[] data`: Data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ImageResourceUtilities.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.ImageResourceUtilities.CreateImageSource(data: /* byte[] */);
    ```

## Class `ResourceData`

Raw resource data

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.ResourceData(name: /* string */, getStream: /* Func<CancellationToken, Stream> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceData.cs` (line 28)

### Constructors

- `public ResourceData(string name, Func<CancellationToken, Stream> getStream)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name
    - `Func<CancellationToken, Stream> getStream`: Returns the stream. It can be called in any thread.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceData.cs` (line 47)

### Methods

- `public Stream GetStream(CancellationToken token)`
  - Summary: Gets the stream. Can be called in any thread.
  - Parameters:
    - `CancellationToken token`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceData.cs` (line 39)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStream(token: /* CancellationToken */);
    ```

### Properties

- `public string Name { get; }`
  - Summary: Name of resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceData.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Enum `ResourceDataType`

type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.TreeView.Resources.ResourceDataType and call its members.
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.ResourceDataType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceDataType.cs` (line 24)

### Members

- `Deserialized`: Deserialized data
- `Serialized`: Serialized data

## Class `ResourceElementNode`

Resource element node base class

**Inherits/Implements:** `DocumentTreeNodeData`, `IResourceDataProvider`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.ResourceElementNode(treeNodeGroup: /* ITreeNodeGroup */, resourceElement: /* ResourceElement */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 38)

### Constructors

- `protected ResourceElementNode(ITreeNodeGroup treeNodeGroup, ResourceElement resourceElement)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `ResourceElement resourceElement`: Resource element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 122)

### Methods

- `protected abstract IEnumerable<ResourceData> GetDeserializedData()`
  - Summary: Gets the deserialized data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 233)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDeserializedData();
    ```
- `protected sealed override ImageReference GetIcon(IDotNetImageService dnImgMgr)`
  - Parameters:
    - `IDotNetImageService dnImgMgr`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon(dnImgMgr: /* IDotNetImageService */);
    ```
- `protected sealed override ImageReference? GetExpandedIcon(IDotNetImageService dnImgMgr)`
  - Parameters:
    - `IDotNetImageService dnImgMgr`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetExpandedIcon(dnImgMgr: /* IDotNetImageService */);
    ```
- `protected sealed override void WriteCore(ITextColorWriter output, IDecompiler decompiler, DocumentNodeWriteOptions options)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `IDecompiler decompiler`: Description not provided.
    - `DocumentNodeWriteOptions options`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteCore(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, options: /* DocumentNodeWriteOptions */);
    ```
- `protected virtual ImageReference GetIcon()`
  - Summary: Gets the icon to use
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon();
    ```
- `public IEnumerable<ResourceData> GetResourceData(ResourceDataType type)`
  - Parameters:
    - `ResourceDataType type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 218)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResourceData(type: /* ResourceDataType */);
    ```
- `public sealed override FilterType GetFilterType(IDocumentTreeNodeFilter filter)`
  - Parameters:
    - `IDocumentTreeNodeFilter filter`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 347)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFilterType(filter: /* IDocumentTreeNodeFilter */);
    ```
- `public virtual string CheckCanUpdateData(ResourceElement newResElem)`
  - Summary: Checks whether can execute. Used by the assembly editor. Returns null or an empty string if the data can be updated, else an error string that can be shown to the user.
  - Parameters:
    - `ResourceElement newResElem`: New data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 331)
  - Example:
    ```csharp
    // Example invocation
    instance.CheckCanUpdateData(newResElem: /* ResourceElement */);
    ```
- `public virtual string ToString(CancellationToken token, bool canDecompile)`
  - Summary: Converts the value to a string
  - Parameters:
    - `CancellationToken token`: Cancellation token
    - `bool canDecompile`: true if the data can be decompiled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 215)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString(token: /* CancellationToken */, canDecompile: /* bool */);
    ```
- `public virtual void UpdateData(ResourceElement newResElem)`
  - Summary: Updates the internal resource data. Must only be called if returned true. Used by the assembly editor.
  - Parameters:
    - `ResourceElement newResElem`: New data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 344)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateData(newResElem: /* ResourceElement */);
    ```
- `public virtual void WriteShort(IDecompilerOutput output, IDecompiler decompiler, bool showOffset)`
  - Parameters:
    - `IDecompilerOutput output`: Description not provided.
    - `IDecompiler decompiler`: Description not provided.
    - `bool showOffset`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 128)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteShort(output: /* IDecompilerOutput */, decompiler: /* IDecompiler */, showOffset: /* bool */);
    ```

### Properties

- `protected virtual string ValueString {
			get {
				switch (resourceElement.ResourceData.Code) {
				case ResourceTypeCode.Null:
					return "null";

				case ResourceTypeCode.String:
					return SimpleTypeConverter.ToString((string)((BuiltInResourceData)resourceElement.ResourceData).Data, false);

				case ResourceTypeCode.Boolean:
					return SimpleTypeConverter.ToString((bool)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.Char:
					return SimpleTypeConverter.ToString((char)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.Byte:
					return SimpleTypeConverter.ToString((byte)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.SByte:
					return SimpleTypeConverter.ToString((sbyte)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.Int16:
					return SimpleTypeConverter.ToString((short)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.UInt16:
					return SimpleTypeConverter.ToString((ushort)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.Int32:
					return SimpleTypeConverter.ToString((int)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.UInt32:
					return SimpleTypeConverter.ToString((uint)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.Int64:
					return SimpleTypeConverter.ToString((long)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.UInt64:
					return SimpleTypeConverter.ToString((ulong)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.Single:
					return SimpleTypeConverter.ToString((float)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.Double:
					return SimpleTypeConverter.ToString((double)((BuiltInResourceData)resourceElement.ResourceData).Data);

				case ResourceTypeCode.Decimal:
					return ((decimal)((BuiltInResourceData)resourceElement.ResourceData).Data).ToString();

				case ResourceTypeCode.DateTime:
					return ((DateTime)((BuiltInResourceData)resourceElement.ResourceData).Data).ToString();

				case ResourceTypeCode.TimeSpan:
					return ((TimeSpan)((BuiltInResourceData)resourceElement.ResourceData).Data).ToString();

				case ResourceTypeCode.ByteArray:
				case ResourceTypeCode.Stream:
					var ary = (byte[])((BuiltInResourceData)resourceElement.ResourceData).Data;
					return string.Format(dnSpy_Contracts_DnSpy_Resources.NumberOfBytes, ary.Length);

				default:
					var binData = resourceElement.ResourceData as BinaryResourceData;
					if (binData != null)
						return string.Format(dnSpy_Contracts_DnSpy_Resources.NumberOfBytesAndType, binData.Data.Length, binData.TypeName);
					return resourceElement.ResourceData.ToString();
				}
			}
		}`
  - Summary: Gets the value as a string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 141)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueString;
    ```
- `public ResourceElement ResourceElement => resourceElement`
  - Summary: Gets the resource element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResourceElement;
    ```
- `public override ITreeNodeGroup TreeNodeGroup => treeNodeGroup`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 114)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TreeNodeGroup;
    ```
- `public sealed override NodePathName NodePathName => new NodePathName(Guid, NameUtilities.CleanName(resourceElement.Name))`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NodePathName;
    ```
- `public string Name => resourceElement.Name`
  - Summary: Gets the name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public uint FileOffset {
			get {
				GetModuleOffset(out var fo);
				return (uint)fo;
			}
		}`
  - Summary: Gets the file offset of the resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FileOffset;
    ```
- `public uint Length => resourceElement.ResourceData.EndOffset - resourceElement.ResourceData.StartOffset`
  - Summary: Gets the length of the resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public uint RVA {
			get {
				var module = GetModuleOffset(out var fo);
				if (module == null)
					return 0;

				return (uint)module.Metadata.PEImage.ToRVA(fo);
			}
		}`
  - Summary: Gets the RVA of the resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementNode.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RVA;
    ```

## Class `ResourceElementSetNode`

A resource node created from a

**Inherits/Implements:** `ResourceNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.ResourceElementSetNode(treeNodeGroup: /* ITreeNodeGroup */, resource: /* Resource */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementSetNode.cs` (line 28)

### Constructors

- `protected ResourceElementSetNode(ITreeNodeGroup treeNodeGroup, Resource resource)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `Resource resource`: Resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementSetNode.cs` (line 34)

### Methods

- `public abstract void RegenerateEmbeddedResource()`
  - Summary: Regenerate the . Used by the assembly editor.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceElementSetNode.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.RegenerateEmbeddedResource();
    ```

## Class `ResourceNode`

Resource node base class

**Inherits/Implements:** `DocumentTreeNodeData`, `IResourceDataProvider`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.ResourceNode(treeNodeGroup: /* ITreeNodeGroup */, resource: /* Resource */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 36)

### Constructors

- `protected ResourceNode(ITreeNodeGroup treeNodeGroup, Resource resource)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `Resource resource`: Resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 128)

### Methods

- `protected sealed override ImageReference GetIcon(IDotNetImageService dnImgMgr)`
  - Parameters:
    - `IDotNetImageService dnImgMgr`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon(dnImgMgr: /* IDotNetImageService */);
    ```
- `protected sealed override ImageReference? GetExpandedIcon(IDotNetImageService dnImgMgr)`
  - Parameters:
    - `IDotNetImageService dnImgMgr`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.GetExpandedIcon(dnImgMgr: /* IDotNetImageService */);
    ```
- `protected sealed override void WriteCore(ITextColorWriter output, IDecompiler decompiler, DocumentNodeWriteOptions options)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `IDecompiler decompiler`: Description not provided.
    - `DocumentNodeWriteOptions options`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteCore(output: /* ITextColorWriter */, decompiler: /* IDecompiler */, options: /* DocumentNodeWriteOptions */);
    ```
- `protected virtual IEnumerable<ResourceData> GetDeserializedData()`
  - Summary: Gets the deserialized data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDeserializedData();
    ```
- `protected virtual IEnumerable<ResourceData> GetSerializedData()`
  - Summary: Gets the serialized data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSerializedData();
    ```
- `protected virtual ImageReference GetIcon()`
  - Summary: Gets the icon
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon();
    ```
- `protected void Save()`
  - Summary: Saves the resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 136)
  - Example:
    ```csharp
    // Example invocation
    instance.Save();
    ```
- `public IEnumerable<ResourceData> GetResourceData(ResourceDataType type)`
  - Parameters:
    - `ResourceDataType type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 172)
  - Example:
    ```csharp
    // Example invocation
    instance.GetResourceData(type: /* ResourceDataType */);
    ```
- `public sealed override FilterType GetFilterType(IDocumentTreeNodeFilter filter)`
  - Parameters:
    - `IDocumentTreeNodeFilter filter`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFilterType(filter: /* IDocumentTreeNodeFilter */);
    ```
- `public virtual string ToString(CancellationToken token, bool canDecompile)`
  - Summary: Converts the value to a string
  - Parameters:
    - `CancellationToken token`: Cancellation token
    - `bool canDecompile`: true if the data can be decompiled
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 169)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString(token: /* CancellationToken */, canDecompile: /* bool */);
    ```
- `public virtual void WriteShort(IDecompilerOutput output, IDecompiler decompiler, bool showOffset)`
  - Parameters:
    - `IDecompilerOutput output`: Description not provided.
    - `IDecompiler decompiler`: Description not provided.
    - `bool showOffset`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteShort(output: /* IDecompilerOutput */, decompiler: /* IDecompiler */, showOffset: /* bool */);
    ```

### Properties

- `public Resource Resource { get; set; }`
  - Summary: Gets the resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Resource;
    ```
- `public override ITreeNodeGroup TreeNodeGroup => treeNodeGroup`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 120)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TreeNodeGroup;
    ```
- `public sealed override NodePathName NodePathName => new NodePathName(Guid, NameUtilities.CleanName(Resource.Name))`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NodePathName;
    ```
- `public string Name => Resource.Name`
  - Summary: Gets the name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public uint FileOffset {
			get {
				GetModuleOffset(out var fo);
				return (uint)fo;
			}
		}`
  - Summary: Gets the offset of the resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FileOffset;
    ```
- `public uint Length {
			get {
				var er = Resource as EmbeddedResource;
				return er == null ? 0 : er.Length;
			}
		}`
  - Summary: Gets the length of the resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public uint RVA {
			get {
				var module = GetModuleOffset(out var fo);
				if (module == null)
					return 0;

				return (uint)module.Metadata.PEImage.ToRVA(fo);
			}
		}`
  - Summary: Gets the RVA of the resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceNode.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RVA;
    ```

## Class `ResourceUtilities`

Resource utilities

**Example**

```csharp
// Access dnSpy.Contracts.Documents.TreeView.Resources.ResourceUtilities members directly without instantiation.
dnSpy.Contracts.Documents.TreeView.Resources.ResourceUtilities./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceUtilities.cs` (line 34)

### Methods

- `public static ImageReference? TryGetImageReference(Assembly dnSpyAsm, string name)`
  - Summary: Creates an image reference
  - Parameters:
    - `Assembly dnSpyAsm`: dnSpy assembly
    - `string name`: Name of resource element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceUtilities.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.ResourceUtilities.TryGetImageReference(dnSpyAsm: /* Assembly */, name: /* string */);
    ```
- `public static MemoryStream StringToStream(string s)`
  - Summary: Converts a string to a stream
  - Parameters:
    - `string s`: String
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceUtilities.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.ResourceUtilities.StringToStream(s: /* string */);
    ```
- `public static ResourceTypeCode FixUserType(this ResourceTypeCode code)`
  - Summary: Returns if it's a user type, else is returned
  - Parameters:
    - `this ResourceTypeCode code`: Resource type code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceUtilities.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.ResourceUtilities.FixUserType(code: /* ResourceTypeCode */);
    ```
- `public static bool Decompile(IDecompileNodeContext context, Stream stream, string name)`
  - Summary: "Decompiles" the data
  - Parameters:
    - `IDecompileNodeContext context`: Context
    - `Stream stream`: Stream
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceUtilities.cs` (line 136)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.ResourceUtilities.Decompile(context: /* IDecompileNodeContext */, stream: /* Stream */, name: /* string */);
    ```
- `public static string TryGetString(Stream stream)`
  - Summary: Returns the string contents of if it's text, else null is returned
  - Parameters:
    - `Stream stream`: Stream
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceUtilities.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.ResourceUtilities.TryGetString(stream: /* Stream */);
    ```
- `public static void WriteOffsetComment(this IDecompilerOutput output, IResourceDataProvider node, bool showOffsetComment)`
  - Summary: Writes the offset
  - Parameters:
    - `this IDecompilerOutput output`: Output
    - `IResourceDataProvider node`: Node
    - `bool showOffsetComment`: true if the offset and comment should be written
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/ResourceUtilities.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.ResourceUtilities.WriteOffsetComment(output: /* IDecompilerOutput */, node: /* IResourceDataProvider */, showOffsetComment: /* bool */);
    ```

## Class `SaveResources`

Saves resources

**Example**

```csharp
// Access dnSpy.Contracts.Documents.TreeView.Resources.SaveResources members directly without instantiation.
dnSpy.Contracts.Documents.TreeView.Resources.SaveResources./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SaveResources.cs` (line 38)

### Methods

- `public static ResourceData[] GetResourceData(IResourceDataProvider[] nodes, ResourceDataType resourceDataType)`
  - Summary: Gets all resource data
  - Parameters:
    - `IResourceDataProvider[] nodes`: Nodes
    - `ResourceDataType resourceDataType`: Type of data to get
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SaveResources.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SaveResources.GetResourceData(nodes: /* IResourceDataProvider[] */, resourceDataType: /* ResourceDataType */);
    ```
- `public static void Save(IResourceDataProvider[] nodes, bool useSubDirs, ResourceDataType resourceDataType, Window ownerWindow = null)`
  - Summary: Saves the nodes
  - Parameters:
    - `IResourceDataProvider[] nodes`: Nodes
    - `bool useSubDirs`: true to create sub directories, false to dump everything in the same folder
    - `ResourceDataType resourceDataType`: Type of data to save
    - `Window ownerWindow` (default: `null`): Owner window
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SaveResources.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SaveResources.Save(nodes: /* IResourceDataProvider[] */, useSubDirs: /* bool */, resourceDataType: /* ResourceDataType */, ownerWindow: /* Window */);
    ```

## Class `SerializationUtilities`

Serialization utilities

**Example**

```csharp
// Access dnSpy.Contracts.Documents.TreeView.Resources.SerializationUtilities members directly without instantiation.
dnSpy.Contracts.Documents.TreeView.Resources.SerializationUtilities./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializationUtilities.cs` (line 32)

### Methods

- `public static ResourceElement CreateSerializedImage(string filename)`
  - Summary: Creates a serialized image
  - Parameters:
    - `string filename`: Filename of image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializationUtilities.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializationUtilities.CreateSerializedImage(filename: /* string */);
    ```
- `public static byte[] Serialize(object obj)`
  - Summary: Serializes the object
  - Parameters:
    - `object obj`: Data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializationUtilities.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializationUtilities.Serialize(obj: /* object */);
    ```
- `public static string ConvertObjectToString(object obj)`
  - Summary: Converts data to a string
  - Parameters:
    - `object obj`: Data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializationUtilities.cs` (line 119)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializationUtilities.ConvertObjectToString(obj: /* object */);
    ```
- `public static string CreateObjectFromString(Type targetType, string typeAsString, out object obj)`
  - Summary: Creates an object from a string
  - Parameters:
    - `Type targetType`: Target type
    - `string typeAsString`: Data as a string
    - `out object obj`: Updated with the deserialized data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializationUtilities.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializationUtilities.CreateObjectFromString(targetType: /* Type */, typeAsString: /* string */, obj: /* object */);
    ```
- `public static string Deserialize(byte[] data, out object obj)`
  - Summary: Deserializes the data
  - Parameters:
    - `byte[] data`: Serialized data
    - `out object obj`: Deserialized data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializationUtilities.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializationUtilities.Deserialize(data: /* byte[] */, obj: /* object */);
    ```

## Class `SerializedImageListStreamerResourceElementNode`

A resource node created from a serialized

**Inherits/Implements:** `ResourceElementNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageListStreamerResourceElementNode(treeNodeGroup: /* ITreeNodeGroup */, resourceElement: /* ResourceElement */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageListStreamerResourceElementNode.cs` (line 28)

### Constructors

- `protected SerializedImageListStreamerResourceElementNode(ITreeNodeGroup treeNodeGroup, ResourceElement resourceElement)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `ResourceElement resourceElement`: Resource element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageListStreamerResourceElementNode.cs` (line 39)

### Properties

- `public abstract ImageListOptions ImageListOptions { get; }`
  - Summary: Gets the options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageListStreamerResourceElementNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageListOptions;
    ```

## Class `SerializedImageListStreamerUtilities`

Serialized image list streamer utilities

**Example**

```csharp
// Access dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageListStreamerUtilities members directly without instantiation.
dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageListStreamerUtilities./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageListStreamerUtilities.cs` (line 35)

### Methods

- `public static ImageListOptions ReadImageData(byte[] imageData)`
  - Summary: Reads an image list
  - Parameters:
    - `byte[] imageData`: Serialized image list
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageListStreamerUtilities.cs` (line 124)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageListStreamerUtilities.ReadImageData(imageData: /* byte[] */);
    ```
- `public static ResourceElement Serialize(ImageListOptions opts)`
  - Summary: Serialize an image list
  - Parameters:
    - `ImageListOptions opts`: Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageListStreamerUtilities.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageListStreamerUtilities.Serialize(opts: /* ImageListOptions */);
    ```
- `public static bool GetImageData(ModuleDef module, string typeName, byte[] serializedData, out byte[] imageData)`
  - Summary: Gets the image data
  - Parameters:
    - `ModuleDef module`: Module
    - `string typeName`: Name of type
    - `byte[] serializedData`: Serialized data
    - `out byte[] imageData`: Updated with image data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageListStreamerUtilities.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageListStreamerUtilities.GetImageData(module: /* ModuleDef */, typeName: /* string */, serializedData: /* byte[] */, imageData: /* byte[] */);
    ```
- `public static string CheckCanUpdateData(ModuleDef module, ResourceElement newResElem)`
  - Summary: Checks whether the data can be updated
  - Parameters:
    - `ModuleDef module`: Module
    - `ResourceElement newResElem`: New data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageListStreamerUtilities.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageListStreamerUtilities.CheckCanUpdateData(module: /* ModuleDef */, newResElem: /* ResourceElement */);
    ```

## Class `SerializedImageResourceElementNode`

A resource node created from a serialized image (BMP or ICO)

**Inherits/Implements:** `ResourceElementNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageResourceElementNode(treeNodeGroup: /* ITreeNodeGroup */, resourceElement: /* ResourceElement */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageResourceElementNode.cs` (line 27)

### Constructors

- `protected SerializedImageResourceElementNode(ITreeNodeGroup treeNodeGroup, ResourceElement resourceElement)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `ResourceElement resourceElement`: Resource element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageResourceElementNode.cs` (line 33)

### Methods

- `public abstract ResourceElement GetAsRawImage()`
  - Summary: Gets the raw
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageResourceElementNode.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAsRawImage();
    ```

## Class `SerializedImageUtilities`

Serialized image utilities

**Example**

```csharp
// Access dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageUtilities members directly without instantiation.
dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageUtilities./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageUtilities.cs` (line 29)

### Methods

- `public static ResourceElement Serialize(ResourceElement resElem)`
  - Summary: Serializes the image
  - Parameters:
    - `ResourceElement resElem`: Resource element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageUtilities.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageUtilities.Serialize(resElem: /* ResourceElement */);
    ```
- `public static bool CheckType(ModuleDef module, string name, TypeRef expectedType)`
  - Summary: Checks whether the type matches an expected type
  - Parameters:
    - `ModuleDef module`: Module
    - `string name`: Type name
    - `TypeRef expectedType`: Expected type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageUtilities.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageUtilities.CheckType(module: /* ModuleDef */, name: /* string */, expectedType: /* TypeRef */);
    ```
- `public static bool GetImageData(ModuleDef module, string typeName, byte[] serializedData, out byte[] imageData)`
  - Summary: Gets the image data
  - Parameters:
    - `ModuleDef module`: Module
    - `string typeName`: Name of type
    - `byte[] serializedData`: Serialized data
    - `out byte[] imageData`: Updated with the image data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedImageUtilities.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.TreeView.Resources.SerializedImageUtilities.GetImageData(module: /* ModuleDef */, typeName: /* string */, serializedData: /* byte[] */, imageData: /* byte[] */);
    ```

## Class `SerializedResourceElementNode`

Serialized resource element node base class

**Inherits/Implements:** `ResourceElementNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.SerializedResourceElementNode(treeNodeGroup: /* ITreeNodeGroup */, resourceElement: /* ResourceElement */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 33)

### Constructors

- `protected SerializedResourceElementNode(ITreeNodeGroup treeNodeGroup, ResourceElement resourceElement)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `ResourceElement resourceElement`: Resource element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 56)

### Methods

- `protected override IEnumerable<ResourceData> GetDeserializedData()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDeserializedData();
    ```
- `protected override ImageReference GetIcon()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIcon();
    ```
- `protected virtual void OnDeserialized()`
  - Summary: Called after it's been deserialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.OnDeserialized();
    ```
- `public override string ToString(CancellationToken token, bool canDecompile)`
  - Parameters:
    - `CancellationToken token`: Description not provided.
    - `bool canDecompile`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString(token: /* CancellationToken */, canDecompile: /* bool */);
    ```
- `public override void Initialize()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.Initialize();
    ```
- `public override void UpdateData(ResourceElement newResElem)`
  - Parameters:
    - `ResourceElement newResElem`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 123)
  - Example:
    ```csharp
    // Example invocation
    instance.UpdateData(newResElem: /* ResourceElement */);
    ```
- `public void Deserialize()`
  - Summary: Deserializes the data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.Deserialize();
    ```

### Properties

- `protected override string ValueString {
			get {
				if (deserializedData == null)
					return base.ValueString;
				return ConvertObjectToString(deserializedData);
			}
		}`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ValueString;
    ```
- `public bool CanDeserialize => IsSerialized`
  - Summary: true if can execute
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/SerializedResourceElementNode.cs` (line 85)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanDeserialize;
    ```

## Class `UnknownResourceNode`

A created from an unknown resource

**Inherits/Implements:** `ResourceNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.UnknownResourceNode(treeNodeGroup: /* ITreeNodeGroup */, resource: /* Resource */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/UnknownResourceNode.cs` (line 27)

### Constructors

- `protected UnknownResourceNode(ITreeNodeGroup treeNodeGroup, Resource resource)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `Resource resource`: Resource
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/UnknownResourceNode.cs` (line 33)

## Class `UnknownSerializedResourceElementNode`

Unknown serialized

**Inherits/Implements:** `SerializedResourceElementNode`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TreeView.Resources.UnknownSerializedResourceElementNode(treeNodeGroup: /* ITreeNodeGroup */, resourceElement: /* ResourceElement */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/UnknownSerializedResourceElementNode.cs` (line 28)

### Constructors

- `public UnknownSerializedResourceElementNode(ITreeNodeGroup treeNodeGroup, ResourceElement resourceElement)`
  - Summary: Constructor
  - Parameters:
    - `ITreeNodeGroup treeNodeGroup`: Treenode group
    - `ResourceElement resourceElement`: Resource element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/UnknownSerializedResourceElementNode.cs` (line 39)

### Properties

- `public override Guid Guid => new Guid(DocumentTreeViewConstants.UNKNOWN_SERIALIZED_RESOURCE_ELEMENT_NODE_GUID)`
  - Summary: Guid of this node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TreeView/Resources/UnknownSerializedResourceElementNode.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```

