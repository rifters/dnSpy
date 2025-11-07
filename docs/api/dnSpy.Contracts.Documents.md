# Namespace `dnSpy.Contracts.Documents`

## Class `DocumentConstants`

Constants

**Example**

```csharp
// Access dnSpy.Contracts.Documents.DocumentConstants members directly without instantiation.
dnSpy.Contracts.Documents.DocumentConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/DocumentConstants.cs` (line 26)

### Fields

- `public const double ORDER_DEFAULT_DOCUMENT_PROVIDER = double.MaxValue`
  - Summary: Order of default instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DocumentConstants.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.DocumentConstants.ORDER_DEFAULT_DOCUMENT_PROVIDER;
    ```
- `public static readonly Guid DOCUMENTTYPE_FILE = new Guid("57E89016-3E28-43A2-88C0-42D067520C14")`
  - Summary: A normal created from a file. is the filename.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DocumentConstants.cs` (line 36)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.DocumentConstants.DOCUMENTTYPE_FILE;
    ```
- `public static readonly Guid DOCUMENTTYPE_GAC = new Guid("1A7BE658-FD95-46A9-BA03-A05D87161342")`
  - Summary: A created from a file in the GAC. is the assembly name.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DocumentConstants.cs` (line 42)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.DocumentConstants.DOCUMENTTYPE_GAC;
    ```
- `public static readonly Guid DOCUMENTTYPE_REFASM = new Guid("75AB0E5C-D1D7-4811-93E1-0AF26CE3856C")`
  - Summary: A created from a file in the GAC or the reference assemblies folder. is the assembly name followed by followed by the path to the reference file in case it's not found in the GAC.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DocumentConstants.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.DocumentConstants.DOCUMENTTYPE_REFASM;
    ```
- `public static readonly string REFERENCE_ASSEMBLY_SEPARATOR = "|"`
  - Summary: String separating assembly full name and reference assembly path
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DocumentConstants.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.DocumentConstants.REFERENCE_ASSEMBLY_SEPARATOR;
    ```

## Class `DotNetMethodBodyReference`

A reference to a .NET method body offset

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.DotNetMethodBodyReference(module: /* ModuleId */, token: /* uint */, offset: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 26)

### Constructors

- `public DotNetMethodBodyReference(ModuleId module, uint token, uint offset)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token of method
    - `uint offset`: IL offset in method body, or one of ,
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 58)

### Properties

- `public ModuleId Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public uint Offset { get; }`
  - Summary: Gets the IL offset in method body, or one of ,
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```
- `public uint Token { get; }`
  - Summary: Gets the token of a method within the module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

### Fields

- `public const uint EPILOG = 0xFFFFFFFF`
  - Summary: The offset is in an epilog
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 30)
  - Example:
    ```csharp
    var value = instance.EPILOG;
    ```
- `public const uint PROLOG = 0xFFFFFFFE`
  - Summary: The offset is in the prolog
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 35)
  - Example:
    ```csharp
    var value = instance.PROLOG;
    ```

## Class `DotNetTokenReference`

A reference to a .NET definition (type, method, field, property, event, parameter)

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.DotNetTokenReference(module: /* ModuleId */, token: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 68)

### Constructors

- `public DotNetTokenReference(ModuleId module, uint token)`
  - Summary: Constructor
  - Parameters:
    - `ModuleId module`: Module
    - `uint token`: Token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 84)

### Properties

- `public ModuleId Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public uint Token { get; }`
  - Summary: Gets the token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DotNetReferences.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

## Class `DsDocument`

Document base class

**Inherits/Implements:** `IDsDocument2`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.DsDocument();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 31)

### Constructors

- `protected DsDocument()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 96)

### Methods

- `protected virtual TList<IDsDocument> CreateChildren()`
  - Summary: Creates the children
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateChildren();
    ```
- `protected virtual void OnPropertyChanged(string propName)`
  - Summary: Gets called when a property has changed
  - Parameters:
    - `string propName`: Name of property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propName: /* string */);
    ```
- `public IEnumerable<T> Annotations<T>() where T : class`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.Annotations();
    ```
- `public T AddAnnotation<T>(T annotation) where T : class`
  - Parameters:
    - `T annotation`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.AddAnnotation(annotation: /* T */);
    ```
- `public T Annotation<T>() where T : class`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.Annotation();
    ```
- `public virtual void OnAdded()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    instance.OnAdded();
    ```
- `public void RemoveAnnotations<T>() where T : class`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAnnotations();
    ```

### Properties

- `public AssemblyDef AssemblyDef => ModuleDef?.Assembly`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyDef;
    ```
- `public TList<IDsDocument> Children {
			get {
				if (children == null) {
					lock (lockObj) {
						if (children == null) {
							children = CreateChildren();
							Debug.Assert(children != null);
							if (children == null)
								children = new TList<IDsDocument>();
						}
					}
				}
				return children;
			}
		}`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Children;
    ```
- `public abstract DsDocumentInfo? SerializedDocument { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SerializedDocument;
    ```
- `public abstract IDsDocumentNameKey Key { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Key;
    ```
- `public bool ChildrenLoaded => children != null`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 85)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ChildrenLoaded;
    ```
- `public bool IsAutoLoaded { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAutoLoaded;
    ```
- `public string Filename {
			get => filename;
			set {
				if (filename != value) {
					filename = value;
					OnPropertyChanged(nameof(Filename));
				}
			}
		}`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public virtual IPEImage PEImage => (ModuleDef as ModuleDefMD)?.Metadata?.PEImage`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PEImage;
    ```
- `public virtual ModuleDef ModuleDef => null`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleDef;
    ```

## Class `DsDocumentExtensionMethods`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Documents.DsDocumentExtensionMethods members directly without instantiation.
dnSpy.Contracts.Documents.DsDocumentExtensionMethods./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 93)

### Methods

- `public static IEnumerable<IDsDocument> GetAllChildren(this IDsDocument self)`
  - Summary: Gets all its children and their children
  - Parameters:
    - `this IDsDocument self`: This
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 192)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDocumentExtensionMethods.GetAllChildren(self: /* IDsDocument */);
    ```
- `public static IEnumerable<IDsDocument> GetAllChildrenAndSelf(this IDsDocument self)`
  - Summary: Gets self and all its children
  - Parameters:
    - `this IDsDocument self`: This
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDocumentExtensionMethods.GetAllChildrenAndSelf(self: /* IDsDocument */);
    ```
- `public static IEnumerable<IDsDocument> NonLoadedDescendantsAndSelf(this IDsDocument document)`
  - Summary: Gets self and all descendants that have been loaded
  - Parameters:
    - `this IDsDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDocumentExtensionMethods.NonLoadedDescendantsAndSelf(document: /* IDsDocument */);
    ```
- `public static IEnumerable<T> GetModules<T>(this IDsDocument document) where T : ModuleDef`
  - Summary: Gets all modules in this instance and any children
  - Parameters:
    - `this IDsDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 148)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDocumentExtensionMethods.GetModules(document: /* IDsDocument */);
    ```
- `public static IEnumerable<T> GetModules<T>(this IEnumerable<IDsDocument> documents) where T : ModuleDef`
  - Summary: Gets all modules in this instance and any children
  - Parameters:
    - `this IEnumerable<IDsDocument> documents`: Documents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 156)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDocumentExtensionMethods.GetModules(documents: /* IEnumerable<IDsDocument> */);
    ```
- `public static string GetShortName(this IDsDocument document)`
  - Summary: Gets the short name of , which is usually the filename without the extension.
  - Parameters:
    - `this IDsDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDocumentExtensionMethods.GetShortName(document: /* IDsDocument */);
    ```

## Struct `DsDocumentInfo`

Document info

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.DsDocumentInfo(name: /* string */, type: /* Guid */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocumentInfo.cs` (line 27)

### Constructors

- `public DsDocumentInfo(string name, Guid type)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name, see
    - `Guid type`: Type, see
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocumentInfo.cs` (line 70)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocumentInfo.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static DsDocumentInfo CreateDocument(string filename)`
  - Summary: Creates a used by files on disk
  - Parameters:
    - `string filename`: Filename
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocumentInfo.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDocumentInfo.CreateDocument(filename: /* string */);
    ```
- `public static DsDocumentInfo CreateGacDocument(string asmFullName)`
  - Summary: Creates a used by files in the GAC
  - Parameters:
    - `string asmFullName`: Full name of assembly
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocumentInfo.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDocumentInfo.CreateGacDocument(asmFullName: /* string */);
    ```
- `public static DsDocumentInfo CreateReferenceAssembly(string asmFullName, string refFilePath)`
  - Summary: Creates a used by reference assemblies
  - Parameters:
    - `string asmFullName`: Full name of assembly
    - `string refFilePath`: Path to the reference assembly. It's used if it's not found in the GAC.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocumentInfo.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDocumentInfo.CreateReferenceAssembly(asmFullName: /* string */, refFilePath: /* string */);
    ```

### Properties

- `public Guid Type { get; }`
  - Summary: Document type, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocumentInfo.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public string Name => name ?? string.Empty`
  - Summary: Name, eg. filename if is
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocumentInfo.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `DsDotNetDocument`

.NET file

**Inherits/Implements:** `DsDotNetDocumentBase`, `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.DsDotNetDocument(documentInfo: /* DsDocumentInfo */, module: /* ModuleDef */, loadSyms: /* bool */, isAsmNode: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 219)

### Constructors

- `protected DsDotNetDocument(DsDocumentInfo documentInfo, ModuleDef module, bool loadSyms, bool isAsmNode)`
  - Summary: Constructor
  - Parameters:
    - `DsDocumentInfo documentInfo`: Document info
    - `ModuleDef module`: Module
    - `bool loadSyms`: true to load symbols
    - `bool isAsmNode`: true if it's an assembly node, false if it's a module node
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 235)

### Methods

- `protected override TList<IDsDocument> CreateChildren()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 274)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateChildren();
    ```
- `protected override void OnPropertyChanged(string propName)`
  - Parameters:
    - `string propName`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 242)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propName: /* string */);
    ```
- `public static DsDotNetDocument CreateAssembly(DsDocumentInfo documentInfo, ModuleDef module, bool loadSyms)`
  - Summary: Creates an assembly
  - Parameters:
    - `DsDocumentInfo documentInfo`: Document info
    - `ModuleDef module`: Module
    - `bool loadSyms`: true to load symbols
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 255)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDotNetDocument.CreateAssembly(documentInfo: /* DsDocumentInfo */, module: /* ModuleDef */, loadSyms: /* bool */);
    ```
- `public static DsDotNetDocument CreateAssembly(IDsDotNetDocument module)`
  - Summary: Creates an assembly
  - Parameters:
    - `IDsDotNetDocument module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 271)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDotNetDocument.CreateAssembly(module: /* IDsDotNetDocument */);
    ```
- `public static DsDotNetDocument CreateModule(DsDocumentInfo documentInfo, ModuleDef module, bool loadSyms)`
  - Summary: Creates a module
  - Parameters:
    - `DsDocumentInfo documentInfo`: Document info
    - `ModuleDef module`: Module
    - `bool loadSyms`: true to load symbols
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 264)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDotNetDocument.CreateModule(documentInfo: /* DsDocumentInfo */, module: /* ModuleDef */, loadSyms: /* bool */);
    ```
- `public void Dispose()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 292)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Properties

- `public override DsDocumentInfo? SerializedDocument => documentInfo`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 225)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SerializedDocument;
    ```
- `public override IDsDocumentNameKey Key => FilenameKey.CreateFullPath(Filename)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 223)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Key;
    ```

## Class `DsDotNetDocumentBase`

.NET file base class

**Inherits/Implements:** `DsDocument`, `IDsDotNetDocument`, `IInMemoryDocument`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.DsDotNetDocumentBase(module: /* ModuleDef */, loadSyms: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 155)

### Constructors

- `protected DsDotNetDocumentBase(ModuleDef module, bool loadSyms)`
  - Summary: Constructor
  - Parameters:
    - `ModuleDef module`: Module
    - `bool loadSyms`: true if symbols should be loaded
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 169)

### Methods

- `public override void OnAdded()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 177)
  - Example:
    ```csharp
    // Example invocation
    instance.OnAdded();
    ```
- `public static ModuleContext CreateModuleContext(IAssemblyResolver asmResolver)`
  - Summary: Creates a module context
  - Parameters:
    - `IAssemblyResolver asmResolver`: Assembly resolver
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.DsDotNetDocumentBase.CreateModuleContext(asmResolver: /* IAssemblyResolver */);
    ```

### Properties

- `public override ModuleDef ModuleDef { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 157)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleDef;
    ```
- `public virtual bool IsActive => true`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 159)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsActive;
    ```

### Fields

- `protected bool loadedSymbols`
  - Summary: true if the symbols have been loaded
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 162)
  - Example:
    ```csharp
    var value = instance.loadedSymbols;
    ```

## Class `DsPEDocument`

PE file

**Inherits/Implements:** `DsDocument`, `IDsPEDocument`, `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.DsPEDocument(peImage: /* IPEImage */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 131)

### Constructors

- `public DsPEDocument(IPEImage peImage)`
  - Summary: Constructor
  - Parameters:
    - `IPEImage peImage`: PE image
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 143)

### Methods

- `public void Dispose()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 149)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Properties

- `public override DsDocumentInfo? SerializedDocument => DsDocumentInfo.CreateDocument(Filename)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 133)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SerializedDocument;
    ```
- `public override IDsDocumentNameKey Key => FilenameKey.CreateFullPath(Filename)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 135)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Key;
    ```
- `public override IPEImage PEImage { get; }`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 137)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PEImage;
    ```

## Class `DsUnknownDocument`

Unknown type of file

**Inherits/Implements:** `DsDocument`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.DsUnknownDocument(filename: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 114)

### Constructors

- `public DsUnknownDocument(string filename)`
  - Summary: Constructor
  - Parameters:
    - `string filename`: Filename
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 125)

### Properties

- `public override DsDocumentInfo? SerializedDocument => DsDocumentInfo.CreateDocument(Filename)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SerializedDocument;
    ```
- `public override IDsDocumentNameKey Key => new FilenameKey(Filename)`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/DsDocument.cs` (line 119)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Key;
    ```

## Class `ExportReferenceConverterAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IReferenceConverterMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.ExportReferenceConverterAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 106)

### Constructors

- `public ExportReferenceConverterAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 109)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 115)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `ExportReferenceNavigatorAttribute`

Exports a instance

**Inherits/Implements:** `ExportAttribute`, `IReferenceNavigatorMetadata`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.ExportReferenceNavigatorAttribute();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 70)

### Constructors

- `public ExportReferenceNavigatorAttribute()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 73)

### Properties

- `public double Order { get; set; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 79)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `FilenameKey`

Compares filenames

**Inherits/Implements:** `IDsDocumentNameKey`, `IEquatable<FilenameKey>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.FilenameKey(filename: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/FilenameKey.cs` (line 27)

### Constructors

- `public FilenameKey(string filename)`
  - Summary: Constructor
  - Parameters:
    - `string filename`: Filename
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/FilenameKey.cs` (line 34)

### Methods

- `public bool Equals(FilenameKey other)`
  - Summary: Equals()
  - Parameters:
    - `FilenameKey other`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/FilenameKey.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* FilenameKey */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Other instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/FilenameKey.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/FilenameKey.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/FilenameKey.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

## Interface `IAnnotations`

Add/remove annotations

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IAnnotations and call its members.
var instance = new dnSpy.Contracts.Documents.IAnnotations(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IAnnotations.cs` (line 26)

### Methods

- `IEnumerable<T> Annotations<T>() where T : class`
  - Summary: Gets all annotations of a certain type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IAnnotations.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.Annotations();
    ```
- `T AddAnnotation<T>(T annotation) where T : class`
  - Summary: Adds an annotation and returns it
  - Parameters:
    - `T annotation`: Value to add
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IAnnotations.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.AddAnnotation(annotation: /* T */);
    ```
- `T Annotation<T>() where T : class`
  - Summary: Gets the first annotation of a certain type or null if none was found
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IAnnotations.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Annotation();
    ```
- `void RemoveAnnotations<T>() where T : class`
  - Summary: Removes all annotations of a certain type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IAnnotations.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAnnotations();
    ```

## Interface `IDsDocument`

A document, see also and

**Inherits/Implements:** `IAnnotations`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IDsDocument and call its members.
var instance = new dnSpy.Contracts.Documents.IDsDocument(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 31)

### Properties

- `AssemblyDef AssemblyDef { get; }`
  - Summary: Gets the assembly or null if it's not a .NET file or if it's a netmodule
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyDef;
    ```
- `DsDocumentInfo? SerializedDocument { get; }`
  - Summary: Used to serialize this instance. Null if it can't be serialized.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SerializedDocument;
    ```
- `IDsDocumentNameKey Key { get; }`
  - Summary: Gets a key for this document. Eg. a instance if it's a file loaded from disk. It's used to detect duplicate documents when adding a new document.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Key;
    ```
- `IPEImage PEImage { get; }`
  - Summary: Gets the PE image or null if it's not available
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PEImage;
    ```
- `ModuleDef ModuleDef { get; }`
  - Summary: Gets the module or null if it's not a .NET file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleDef;
    ```
- `TList<IDsDocument> Children { get; }`
  - Summary: Gets any children. Eg. if it's a .NET assembly, the children would be modules of the assembly.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Children;
    ```
- `bool ChildrenLoaded { get; }`
  - Summary: true if has been initialized
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ChildrenLoaded;
    ```
- `bool IsAutoLoaded { get; set; }`
  - Summary: true if it was not loaded by the user
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAutoLoaded;
    ```
- `string Filename { get; set; }`
  - Summary: Gets/sets the filename
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```

## Interface `IDsDocument2`

A document

**Inherits/Implements:** `IDsDocument`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IDsDocument2 and call its members.
var instance = new dnSpy.Contracts.Documents.IDsDocument2(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 83)

### Methods

- `void OnAdded()`
  - Summary: Called after it's been added to the documents list
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocument.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.OnAdded();
    ```

## Interface `IDsDocumentNameKey`

A document name key

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IDsDocumentNameKey and call its members.
var instance = new dnSpy.Contracts.Documents.IDsDocumentNameKey(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentNameKey.cs` (line 24)

## Interface `IDsDocumentProvider`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IDsDocumentProvider and call its members.
var instance = new dnSpy.Contracts.Documents.IDsDocumentProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentProvider.cs` (line 24)

### Methods

- `IDsDocument Create(IDsDocumentService documentService, DsDocumentInfo documentInfo)`
  - Summary: Creates a new instance or returns null. This method can be called in any thread so the code must be thread safe.
  - Parameters:
    - `IDsDocumentService documentService`: Document manager
    - `DsDocumentInfo documentInfo`: Document to create
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(documentService: /* IDsDocumentService */, documentInfo: /* DsDocumentInfo */);
    ```
- `IDsDocumentNameKey CreateKey(IDsDocumentService documentService, DsDocumentInfo documentInfo)`
  - Summary: Creates a instance
  - Parameters:
    - `IDsDocumentService documentService`: Document manager
    - `DsDocumentInfo documentInfo`: Document to create
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentProvider.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateKey(documentService: /* IDsDocumentService */, documentInfo: /* DsDocumentInfo */);
    ```

### Properties

- `double Order { get; }`
  - Summary: Order of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentProvider.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IDsDocumentService`

Manages all loaded documents (which are shown in the treeview)

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IDsDocumentService and call its members.
var instance = new dnSpy.Contracts.Documents.IDsDocumentService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 28)

### Methods

- `IDisposable DisableAssemblyLoad()`
  - Summary: Call this to disable loading assemblies in the document list until the return value's method has been called.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.DisableAssemblyLoad();
    ```
- `IDsDocument CreateDocument(DsDocumentInfo documentInfo, string filename, bool isModule = false)`
  - Summary: Creates a
  - Parameters:
    - `DsDocumentInfo documentInfo`: Document info
    - `string filename`: Filename
    - `bool isModule` (default: `false`): true if it's a module, false if it's an assembly
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 137)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateDocument(documentInfo: /* DsDocumentInfo */, filename: /* string */, isModule: /* bool */);
    ```
- `IDsDocument Find(IDsDocumentNameKey key)`
  - Summary: Returns an inserted instance or null
  - Parameters:
    - `IDsDocumentNameKey key`: Key
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.Find(key: /* IDsDocumentNameKey */);
    ```
- `IDsDocument FindAssembly(IAssembly assembly)`
  - Summary: Returns an assembly or null if it's not in the list
  - Parameters:
    - `IAssembly assembly`: Assembly
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.FindAssembly(assembly: /* IAssembly */);
    ```
- `IDsDocument ForceAdd(IDsDocument document, bool delayLoad, object data)`
  - Summary: Adds to the list, even if another instance has already been inserted. Returns the input.
  - Parameters:
    - `IDsDocument document`: Document
    - `bool delayLoad`: true to delay load
    - `object data`: Data passed to listeners
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.ForceAdd(document: /* IDsDocument */, delayLoad: /* bool */, data: /* object */);
    ```
- `IDsDocument GetOrAdd(IDsDocument document)`
  - Summary: Adds a new instance if it hasn't already been added. Returns the input or the existing instance.
  - Parameters:
    - `IDsDocument document`: Document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrAdd(document: /* IDsDocument */);
    ```
- `IDsDocument Resolve(IAssembly asm, ModuleDef sourceModule)`
  - Summary: Resolves an assembly. Returns null if it couldn't be resolved.
  - Parameters:
    - `IAssembly asm`: Assembly
    - `ModuleDef sourceModule`: The module that needs to resolve an assembly or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve(asm: /* IAssembly */, sourceModule: /* ModuleDef */);
    ```
- `IDsDocument TryCreateOnly(DsDocumentInfo info)`
  - Summary: Tries to create a new without adding it to the list. null is returned if it couldn't be created.
  - Parameters:
    - `DsDocumentInfo info`: Document info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.TryCreateOnly(info: /* DsDocumentInfo */);
    ```
- `IDsDocument TryGetOrCreate(DsDocumentInfo info, bool isAutoLoaded = false)`
  - Summary: Creates a new instance or returns an existing one. null is returned if it couldn't be created.
  - Parameters:
    - `DsDocumentInfo info`: Document info
    - `bool isAutoLoaded` (default: `false`): New value of if the document gets created.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetOrCreate(info: /* DsDocumentInfo */, isAutoLoaded: /* bool */);
    ```
- `IDsDocument[] GetDocuments()`
  - Summary: Gets all documents. Doesn't include any children.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDocuments();
    ```
- `void Clear()`
  - Summary: Clears all documents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 120)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```
- `void Remove(IDsDocumentNameKey key)`
  - Summary: Removes a document
  - Parameters:
    - `IDsDocumentNameKey key`: Key of document to remove. See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(key: /* IDsDocumentNameKey */);
    ```
- `void Remove(IEnumerable<IDsDocument> documents)`
  - Summary: Removes documents
  - Parameters:
    - `IEnumerable<IDsDocument> documents`: Documents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(documents: /* IEnumerable<IDsDocument> */);
    ```
- `void SetDispatcher(Action<Action> action)`
  - Summary: Can be called once to set a delegate instance that will execute code in a certain thread. can be called in any thread unless this method gets called.
  - Parameters:
    - `Action<Action> action`: Action
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 128)
  - Example:
    ```csharp
    // Example invocation
    instance.SetDispatcher(action: /* Action<Action> */);
    ```

### Properties

- `IAssemblyResolver AssemblyResolver { get; }`
  - Summary: The assembly resolver it uses
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 142)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyResolver;
    ```

### Events

- `event EventHandler<NotifyDocumentCollectionChangedEventArgs> CollectionChanged`
  - Summary: Notified when the collection gets changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentService.cs` (line 39)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.CollectionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IDsDocumentServiceProvider`

creator

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IDsDocumentServiceProvider and call its members.
var instance = new dnSpy.Contracts.Documents.IDsDocumentServiceProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentServiceProvider.cs` (line 24)

### Methods

- `IDsDocumentService Create()`
  - Summary: Creates a new instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDocumentServiceProvider.cs` (line 29)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

## Interface `IDsDotNetDocument`

A .NET file

**Inherits/Implements:** `IDsDocument`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IDsDotNetDocument and call its members.
var instance = new dnSpy.Contracts.Documents.IDsDotNetDocument(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsDotNetDocument.cs` (line 24)

## Interface `IDsPEDocument`

A PE file (NOTE: not a .NET file, see )

**Inherits/Implements:** `IDsDocument`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IDsPEDocument and call its members.
var instance = new dnSpy.Contracts.Documents.IDsPEDocument(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IDsPEDocument.cs` (line 24)

## Interface `IInMemoryDocument`

In-memory document

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IInMemoryDocument and call its members.
var instance = new dnSpy.Contracts.Documents.IInMemoryDocument(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/IInMemoryDocument.cs` (line 24)

### Properties

- `bool IsActive { get; }`
  - Summary: true if the document is still being used (eg. the user is debugging something and the document is loaded in the debugged process)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/IInMemoryDocument.cs` (line 29)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsActive;
    ```

## Interface `IReferenceConverterMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IReferenceConverterMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.IReferenceConverterMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 98)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 100)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `IReferenceNavigatorMetadata`

Metadata

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.IReferenceNavigatorMetadata and call its members.
var instance = new dnSpy.Contracts.Documents.IReferenceNavigatorMetadata(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 62)

### Properties

- `double Order { get; }`
  - Summary: See
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Class `NotifyDocumentCollectionChangedEventArgs`

Event args

**Inherits/Implements:** `EventArgs`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.NotifyDocumentCollectionChangedEventArgs and call its members.
var instance = new dnSpy.Contracts.Documents.NotifyDocumentCollectionChangedEventArgs(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/NotifyDocumentCollectionChangedEventArgs.cs` (line 26)

### Methods

- `public static NotifyDocumentCollectionChangedEventArgs CreateAdd(IDsDocument document, object data)`
  - Summary: Creates a instance
  - Parameters:
    - `IDsDocument document`: Added document
    - `object data`: Data to send to listeners
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/NotifyDocumentCollectionChangedEventArgs.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.NotifyDocumentCollectionChangedEventArgs.CreateAdd(document: /* IDsDocument */, data: /* object */);
    ```
- `public static NotifyDocumentCollectionChangedEventArgs CreateClear(IDsDocument[] clearedDocuments, object data)`
  - Summary: Creates a instance
  - Parameters:
    - `IDsDocument[] clearedDocuments`: All cleared documents
    - `object data`: Data to send to listeners
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/NotifyDocumentCollectionChangedEventArgs.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.NotifyDocumentCollectionChangedEventArgs.CreateClear(clearedDocuments: /* IDsDocument[] */, data: /* object */);
    ```
- `public static NotifyDocumentCollectionChangedEventArgs CreateRemove(IDsDocument document, object data)`
  - Summary: Creates a instance
  - Parameters:
    - `IDsDocument document`: Removed document
    - `object data`: Data to send to listeners
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/NotifyDocumentCollectionChangedEventArgs.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.NotifyDocumentCollectionChangedEventArgs.CreateRemove(document: /* IDsDocument */, data: /* object */);
    ```
- `public static NotifyDocumentCollectionChangedEventArgs CreateRemove(IDsDocument[] documents, object data)`
  - Summary: Creates a instance
  - Parameters:
    - `IDsDocument[] documents`: Removed documents
    - `object data`: Data to send to listeners
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/NotifyDocumentCollectionChangedEventArgs.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Documents.NotifyDocumentCollectionChangedEventArgs.CreateRemove(documents: /* IDsDocument[] */, data: /* object */);
    ```

### Properties

- `public IDsDocument[] Documents { get; private set; }`
  - Summary: All documents
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/NotifyDocumentCollectionChangedEventArgs.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Documents;
    ```
- `public NotifyDocumentCollectionType Type { get; private set; }`
  - Summary: Event type
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/NotifyDocumentCollectionChangedEventArgs.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public object Data { get; private set; }`
  - Summary: User data
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/NotifyDocumentCollectionChangedEventArgs.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```

## Enum `NotifyDocumentCollectionType`

Event type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.NotifyDocumentCollectionType and call its members.
var instance = new dnSpy.Contracts.Documents.NotifyDocumentCollectionType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/NotifyDocumentCollectionType.cs` (line 24)

### Members

- `Clear`: All documents have been cleared
- `Add`: A new document was added
- `Remove`: A document was removed

## Class `PredefinedReferenceNavigatorOptions`

Predefined options

**Example**

```csharp
// Access dnSpy.Contracts.Documents.PredefinedReferenceNavigatorOptions members directly without instantiation.
dnSpy.Contracts.Documents.PredefinedReferenceNavigatorOptions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 40)

### Fields

- `public const string NewTab = nameof(NewTab)`
  - Summary: Show the reference in a new tab
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 44)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Documents.PredefinedReferenceNavigatorOptions.NewTab;
    ```

## Class `ReferenceConverter`

Converts a reference passed to . This new reference is passed to . Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.ReferenceConverter and call its members.
var instance = new dnSpy.Contracts.Documents.ReferenceConverter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 87)

### Methods

- `public abstract void Convert(ref object reference)`
  - Summary: Converts a reference. If null is written to , won't get called. This method is called on the UI thread.
  - Parameters:
    - `ref object reference`: Reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.Convert(reference: /* object */);
    ```

## Class `ReferenceNavigator`

Shows a reference. Use to export an instance.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.ReferenceNavigator and call its members.
var instance = new dnSpy.Contracts.Documents.ReferenceNavigator(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 50)

### Methods

- `public abstract bool GoTo(object reference, ReadOnlyCollection<object> options)`
  - Summary: Returns true if it showed the reference, and false if the next handler should get called. This method is called on the UI thread.
  - Parameters:
    - `object reference`: Reference. MEF exported s can convert this reference to another reference.
    - `ReadOnlyCollection<object> options`: Options passed to s, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.GoTo(reference: /* object */, options: /* ReadOnlyCollection<object> */);
    ```

## Class `ReferenceNavigatorService`

Shows a reference

**Example**

```csharp
// Instantiate dnSpy.Contracts.Documents.ReferenceNavigatorService and call its members.
var instance = new dnSpy.Contracts.Documents.ReferenceNavigatorService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 28)

### Methods

- `public abstract void GoTo(object reference, object[] options = null)`
  - Summary: Shows a reference. It can be called from any thread.
  - Parameters:
    - `object reference`: Reference. MEF exported s can convert this to another reference.
    - `object[] options` (default: `null`): Options passed to s, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/ReferenceNavigator.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GoTo(reference: /* object */, options: /* object[] */);
    ```

## Class `TList<T>`

**Inherits/Implements:** `IEnumerable<T>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Documents.TList<T>();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 28)

### Constructors

- `public TList()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 75)
- `public TList(int capacity)`
  - Parameters:
    - `int capacity`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 84)

### Methods

- `public IEnumerator<T> GetEnumerator()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 158)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEnumerator();
    ```
- `public T[] GetElements()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.GetElements();
    ```
- `public bool Remove(T item)`
  - Parameters:
    - `T item`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 122)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(item: /* T */);
    ```
- `public int IndexOf(T item)`
  - Parameters:
    - `T item`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 141)
  - Example:
    ```csharp
    // Example invocation
    instance.IndexOf(item: /* T */);
    ```
- `public void Add(T item)`
  - Parameters:
    - `T item`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(item: /* T */);
    ```
- `public void AddRange(IEnumerable<T> collection)`
  - Parameters:
    - `IEnumerable<T> collection`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.AddRange(collection: /* IEnumerable<T> */);
    ```
- `public void Clear()`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 149)
  - Example:
    ```csharp
    // Example invocation
    instance.Clear();
    ```
- `public void Insert(int index, T item)`
  - Parameters:
    - `int index`: Description not provided.
    - `T item`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 112)
  - Example:
    ```csharp
    // Example invocation
    instance.Insert(index: /* int */, item: /* T */);
    ```
- `public void RemoveAt(int index)`
  - Parameters:
    - `int index`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 131)
  - Example:
    ```csharp
    // Example invocation
    instance.RemoveAt(index: /* int */);
    ```

### Properties

- `public int Count {
			get {
				lock (lockObj)
					return list.Count;
			}
		}`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Count;
    ```
- `public object SyncRoot => lockObj`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SyncRoot;
    ```

### Indexers

- `public T this[int index]`
  - Parameters:
    - `int index`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Documents/TList.cs` (line 42)
  - Example:
    ```csharp
    // Access via indexer
    var value = instance[/* index */];
    ```

