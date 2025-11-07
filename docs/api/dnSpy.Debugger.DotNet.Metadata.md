# Namespace `dnSpy.Debugger.DotNet.Metadata`

## Class `DmdAppDomain`

A .NET AppDomain

**Inherits/Implements:** `DmdObject`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdAppDomain and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdAppDomain(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 27)

### Methods

- `private protected abstract void YouCantDeriveFromThisClass()`
  - Summary: Dummy abstract method to make sure no-one outside this assembly can create their own
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.YouCantDeriveFromThisClass();
    ```
- `public DmdAssembly CreateAssembly(Func<DmdLazyMetadataBytes> getMetadata, bool isInMemory, bool isDynamic, string fullyQualifiedName, string assemblyLocation)`
  - Summary: Creates an assembly and adds it to the AppDomain. The first created assembly must be the corlib ()
  - Parameters:
    - `Func<DmdLazyMetadataBytes> getMetadata`: Called to provide the metadata
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
    - `string assemblyLocation`: Location of the assembly or an empty string ()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAssembly(getMetadata: /* Func<DmdLazyMetadataBytes> */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */, assemblyLocation: /* string */);
    ```
- `public DmdAssembly CreateAssembly(Func<DmdLazyMetadataBytes> getMetadata, bool isInMemory, bool isDynamic, string fullyQualifiedName, string assemblyLocation, string assemblySimpleName, bool isSynthetic, bool addAssembly)`
  - Summary: Creates an assembly and optionally adds it to the AppDomain. The first created assembly must be the corlib ()
  - Parameters:
    - `Func<DmdLazyMetadataBytes> getMetadata`: Called to provide the metadata
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
    - `string assemblyLocation`: Location of the assembly or an empty string ()
    - `string assemblySimpleName`: The assembly's simple name or null if it's unknown
    - `bool isSynthetic`: true if it's a synthetic assembly; it's not loaded in the debugged process
    - `bool addAssembly`: true if the assembly should be added to the AppDomain
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAssembly(getMetadata: /* Func<DmdLazyMetadataBytes> */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */, assemblyLocation: /* string */, assemblySimpleName: /* string */, isSynthetic: /* bool */, addAssembly: /* bool */);
    ```
- `public DmdAssembly CreateAssembly(IntPtr address, uint size, bool isFileLayout, bool isInMemory, bool isDynamic, string fullyQualifiedName, string assemblyLocation)`
  - Summary: Creates an assembly. The first created assembly must be the corlib ()
  - Parameters:
    - `IntPtr address`: Address of PE file
    - `uint size`: Size of PE file
    - `bool isFileLayout`: true if file layout, false if memory layout
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
    - `string assemblyLocation`: Location of the assembly or an empty string ()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 118)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAssembly(address: /* IntPtr */, size: /* uint */, isFileLayout: /* bool */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */, assemblyLocation: /* string */);
    ```
- `public DmdAssembly CreateAssembly(byte[] assemblyBytes, bool isFileLayout, bool isInMemory, bool isDynamic, string fullyQualifiedName, string assemblyLocation)`
  - Summary: Creates an assembly. The first created assembly must be the corlib ()
  - Parameters:
    - `byte[] assemblyBytes`: Raw PE file bytes
    - `bool isFileLayout`: true if file layout, false if memory layout
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
    - `string assemblyLocation`: Location of the assembly or an empty string ()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 131)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAssembly(assemblyBytes: /* byte[] */, isFileLayout: /* bool */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */, assemblyLocation: /* string */);
    ```
- `public DmdAssembly CreateAssembly(object comMetadata, DmdDynamicModuleHelper dynamicModuleHelper, DmdDispatcher dispatcher, bool isInMemory, bool isDynamic, string fullyQualifiedName, string assemblyLocation = null)`
  - Summary: Creates an assembly. The first created assembly must be the corlib ()
  - Parameters:
    - `object comMetadata`: COM IMetaDataImport instance
    - `DmdDynamicModuleHelper dynamicModuleHelper`: Helper class
    - `DmdDispatcher dispatcher`: Dispatcher to use when accessing
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
    - `string assemblyLocation` (default: `null`): Location of the assembly or an empty string ()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 148)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAssembly(comMetadata: /* object */, dynamicModuleHelper: /* DmdDynamicModuleHelper */, dispatcher: /* DmdDispatcher */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */, assemblyLocation: /* string */);
    ```
- `public DmdAssembly CreateAssembly(string filename, bool isFileLayout = true, bool isInMemory = false, bool isDynamic = false, string fullyQualifiedName = null, string assemblyLocation = null)`
  - Summary: Creates an assembly. The first created assembly must be the corlib ()
  - Parameters:
    - `string filename`: Filename
    - `bool isFileLayout` (default: `true`): true if file layout, false if memory layout
    - `bool isInMemory` (default: `false`): true if the module is in memory ()
    - `bool isDynamic` (default: `false`): true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName` (default: `null`): The fully qualified name of the module (). See
    - `string assemblyLocation` (default: `null`): Location of the assembly or an empty string ()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAssembly(filename: /* string */, isFileLayout: /* bool */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */, assemblyLocation: /* string */);
    ```
- `public DmdAssembly CreateSyntheticAssembly(Func<DmdLazyMetadataBytes> getMetadata, bool isInMemory, bool isDynamic, string fullyQualifiedName, string assemblyLocation, string assemblySimpleName)`
  - Summary: Creates a synthetic assembly but does not add it to the AppDomain
  - Parameters:
    - `Func<DmdLazyMetadataBytes> getMetadata`: Called to provide the metadata
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
    - `string assemblyLocation`: Location of the assembly or an empty string ()
    - `string assemblySimpleName`: The assembly's simple name or null if it's unknown
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateSyntheticAssembly(getMetadata: /* Func<DmdLazyMetadataBytes> */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */, assemblyLocation: /* string */, assemblySimpleName: /* string */);
    ```
- `public DmdAssembly Load(object context, string assemblyName)`
  - Summary: Loads an assembly
  - Parameters:
    - `object context`: Evaluation context
    - `string assemblyName`: Full assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 306)
  - Example:
    ```csharp
    // Example invocation
    instance.Load(context: /* object */, assemblyName: /* string */);
    ```
- `public DmdAssembly[] GetAssemblies()`
  - Summary: Gets all assemblies
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 277)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAssemblies();
    ```
- `public DmdModule CreateModule(DmdAssembly assembly, IntPtr address, uint size, bool isFileLayout, bool isInMemory, bool isDynamic, string fullyQualifiedName)`
  - Summary: Adds a module to an existing assembly
  - Parameters:
    - `DmdAssembly assembly`: Assembly
    - `IntPtr address`: Address of the PE file
    - `uint size`: Size of the PE file
    - `bool isFileLayout`: true if file layout, false if memory layout
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 197)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateModule(assembly: /* DmdAssembly */, address: /* IntPtr */, size: /* uint */, isFileLayout: /* bool */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */);
    ```
- `public DmdModule CreateModule(DmdAssembly assembly, byte[] moduleBytes, bool isFileLayout, bool isInMemory, bool isDynamic, string fullyQualifiedName)`
  - Summary: Adds a module to an existing assembly
  - Parameters:
    - `DmdAssembly assembly`: Assembly
    - `byte[] moduleBytes`: Raw PE file bytes
    - `bool isFileLayout`: true if file layout, false if memory layout
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 210)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateModule(assembly: /* DmdAssembly */, moduleBytes: /* byte[] */, isFileLayout: /* bool */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */);
    ```
- `public DmdModule CreateModule(DmdAssembly assembly, object comMetadata, DmdDynamicModuleHelper dynamicModuleHelper, DmdDispatcher dispatcher, bool isInMemory, bool isDynamic, string fullyQualifiedName)`
  - Summary: Adds a module to an existing assembly
  - Parameters:
    - `DmdAssembly assembly`: Assembly
    - `object comMetadata`: COM IMetaDataImport instance
    - `DmdDynamicModuleHelper dynamicModuleHelper`: Helper class
    - `DmdDispatcher dispatcher`: Dispatcher to use when accessing
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 227)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateModule(assembly: /* DmdAssembly */, comMetadata: /* object */, dynamicModuleHelper: /* DmdDynamicModuleHelper */, dispatcher: /* DmdDispatcher */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */);
    ```
- `public DmdModule CreateModule(DmdAssembly assembly, string filename, bool isFileLayout = true, bool isInMemory = false, bool isDynamic = false, string fullyQualifiedName = null)`
  - Summary: Adds a module to an existing assembly
  - Parameters:
    - `DmdAssembly assembly`: Assembly
    - `string filename`: Filename
    - `bool isFileLayout` (default: `true`): true if file layout, false if memory layout
    - `bool isInMemory` (default: `false`): true if the module is in memory ()
    - `bool isDynamic` (default: `false`): true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName` (default: `null`): The fully qualified name of the module (). See
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 180)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateModule(assembly: /* DmdAssembly */, filename: /* string */, isFileLayout: /* bool */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */);
    ```
- `public DmdType GetType(Type type)`
  - Summary: Gets a type
  - Parameters:
    - `Type type`: Type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 542)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(type: /* Type */);
    ```
- `public DmdType GetType(Type type, DmdGetTypeOptions options)`
  - Summary: Gets a type
  - Parameters:
    - `Type type`: Type
    - `DmdGetTypeOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 557)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(type: /* Type */, options: /* DmdGetTypeOptions */);
    ```
- `public DmdType GetType(string typeName)`
  - Summary: Gets a type
  - Parameters:
    - `string typeName`: Full name of the type () or the assembly qualified name (). Version, public key token and culture are optional.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 578)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(typeName: /* string */);
    ```
- `public DmdType GetTypeThrow(Type type)`
  - Summary: Gets a type and throws if it couldn't be found
  - Parameters:
    - `Type type`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 549)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTypeThrow(type: /* Type */);
    ```
- `public DmdType GetTypeThrow(string typeName)`
  - Summary: Gets a type and throws if it couldn't be found
  - Parameters:
    - `string typeName`: Full name of the type () or the assembly qualified name (). Version, public key token and culture are optional.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 586)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTypeThrow(typeName: /* string */);
    ```
- `public DmdType GetWellKnownType(DmdWellKnownType wellKnownType)`
  - Summary: Gets a well known type
  - Parameters:
    - `DmdWellKnownType wellKnownType`: Well known type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 349)
  - Example:
    ```csharp
    // Example invocation
    instance.GetWellKnownType(wellKnownType: /* DmdWellKnownType */);
    ```
- `public DmdType GetWellKnownType(DmdWellKnownType wellKnownType, bool isOptional)`
  - Summary: Gets a well known type
  - Parameters:
    - `DmdWellKnownType wellKnownType`: Well known type
    - `bool isOptional`: Used if the type couldn't be found. If true, null is returned, and if false, an exception is thrown
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 357)
  - Example:
    ```csharp
    // Example invocation
    instance.GetWellKnownType(wellKnownType: /* DmdWellKnownType */, isOptional: /* bool */);
    ```
- `public DmdType MakeGenericMethodParameter(int position, DmdMethodBase declaringMethod)`
  - Summary: Makes a generic method parameter
  - Parameters:
    - `int position`: Position
    - `DmdMethodBase declaringMethod`: Declaring method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 523)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericMethodParameter(position: /* int */, declaringMethod: /* DmdMethodBase */);
    ```
- `public DmdType MakeGenericTypeParameter(int position, DmdType declaringType)`
  - Summary: Makes a generic type parameter
  - Parameters:
    - `int position`: Position
    - `DmdType declaringType`: Declaring type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 503)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericTypeParameter(position: /* int */, declaringType: /* DmdType */);
    ```
- `public TemporaryAssemblyDisposable AddTemporaryAssembly(DmdAssembly assembly)`
  - Summary: Adds an assembly. It gets removed when the return value's method gets called
  - Parameters:
    - `DmdAssembly assembly`: Assembly to add
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 255)
  - Example:
    ```csharp
    // Example invocation
    instance.AddTemporaryAssembly(assembly: /* DmdAssembly */);
    ```
- `public abstract DmdAssembly CreateAssembly(Func<DmdLazyMetadataBytes> getMetadata, DmdCreateAssemblyInfo assemblyInfo)`
  - Summary: Creates an assembly and optionally adds it to the AppDomain. The first created assembly must be the corlib ()
  - Parameters:
    - `Func<DmdLazyMetadataBytes> getMetadata`: Called to provide the metadata
    - `DmdCreateAssemblyInfo assemblyInfo`: Assembly info
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAssembly(getMetadata: /* Func<DmdLazyMetadataBytes> */, assemblyInfo: /* DmdCreateAssemblyInfo */);
    ```
- `public abstract DmdAssembly GetAssembly(IDmdAssemblyName name)`
  - Summary: Gets an assembly or returns null if there's no such assembly
  - Parameters:
    - `IDmdAssemblyName name`: Assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 298)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAssembly(name: /* IDmdAssemblyName */);
    ```
- `public abstract DmdAssembly GetAssembly(string simpleName)`
  - Summary: Gets an assembly or returns null if there's no such assembly
  - Parameters:
    - `string simpleName`: Simple name of the assembly, eg. "System"
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 291)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAssembly(simpleName: /* string */);
    ```
- `public abstract DmdAssembly Load(object context, IDmdAssemblyName name)`
  - Summary: Loads an assembly
  - Parameters:
    - `object context`: Evaluation context
    - `IDmdAssemblyName name`: Assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 314)
  - Example:
    ```csharp
    // Example invocation
    instance.Load(context: /* object */, name: /* IDmdAssemblyName */);
    ```
- `public abstract DmdAssembly LoadFile(object context, string path)`
  - Summary: Loads an assembly. Will fail on .NET Core 1.x (but not on .NET Core 2.x or later)
  - Parameters:
    - `object context`: Evaluation context
    - `string path`: Path to assembly
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 330)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadFile(context: /* object */, path: /* string */);
    ```
- `public abstract DmdAssembly LoadFrom(object context, string assemblyFile)`
  - Summary: Loads an assembly. Will fail on .NET Core 1.x (but not on .NET Core 2.x or later)
  - Parameters:
    - `object context`: Evaluation context
    - `string assemblyFile`: Assembly name or path to assembly
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 322)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadFrom(context: /* object */, assemblyFile: /* string */);
    ```
- `public abstract DmdAssembly[] GetAssemblies(bool includeSyntheticAssemblies)`
  - Summary: Gets all assemblies
  - Parameters:
    - `bool includeSyntheticAssemblies`: true to include synthetic assemblies
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 284)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAssemblies(includeSyntheticAssemblies: /* bool */);
    ```
- `public abstract DmdMethodInfo MakeGenericMethod(DmdMethodInfo genericMethodDefinition, IList<DmdType> typeArguments, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Makes a generic method
  - Parameters:
    - `DmdMethodInfo genericMethodDefinition`: Generic method definition
    - `IList<DmdType> typeArguments`: Generic arguments
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 473)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericMethod(genericMethodDefinition: /* DmdMethodInfo */, typeArguments: /* IList<DmdType> */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract DmdModule CreateModule(DmdAssembly assembly, Func<DmdLazyMetadataBytes> getMetadata, bool isInMemory, bool isDynamic, string fullyQualifiedName)`
  - Summary: Adds a module to an existing assembly
  - Parameters:
    - `DmdAssembly assembly`: Assembly
    - `Func<DmdLazyMetadataBytes> getMetadata`: Called to provide the metadata
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 168)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateModule(assembly: /* DmdAssembly */, getMetadata: /* Func<DmdLazyMetadataBytes> */, isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */);
    ```
- `public abstract DmdType GetType(string typeName, DmdGetTypeOptions options)`
  - Summary: Gets a type
  - Parameters:
    - `string typeName`: Full name of the type () or the assembly qualified name (). Version, public key token and culture are optional.
    - `DmdGetTypeOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 570)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(typeName: /* string */, options: /* DmdGetTypeOptions */);
    ```
- `public abstract DmdType Intern(DmdType type, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Returns a cached type if present else the input type
  - Parameters:
    - `DmdType type`: Type
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 415)
  - Example:
    ```csharp
    // Example invocation
    instance.Intern(type: /* DmdType */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract DmdType MakeArrayType(DmdType elementType, IList<DmdCustomModifier> customModifiers, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Makes a SZ array type
  - Parameters:
    - `DmdType elementType`: Element type
    - `IList<DmdCustomModifier> customModifiers`: Custom modifiers or null
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 442)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeArrayType(elementType: /* DmdType */, customModifiers: /* IList<DmdCustomModifier> */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract DmdType MakeArrayType(DmdType elementType, int rank, IList<int> sizes, IList<int> lowerBounds, IList<DmdCustomModifier> customModifiers, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Makes a multi-dimensional array type
  - Parameters:
    - `DmdType elementType`: Element type
    - `int rank`: Number of dimensions
    - `IList<int> sizes`: Sizes
    - `IList<int> lowerBounds`: Lower bounds
    - `IList<DmdCustomModifier> customModifiers`: Custom modifiers or null
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 454)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeArrayType(elementType: /* DmdType */, rank: /* int */, sizes: /* IList<int> */, lowerBounds: /* IList<int> */, customModifiers: /* IList<DmdCustomModifier> */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract DmdType MakeByRefType(DmdType elementType, IList<DmdCustomModifier> customModifiers, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Makes a by-ref type
  - Parameters:
    - `DmdType elementType`: Element type
    - `IList<DmdCustomModifier> customModifiers`: Custom modifiers or null
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 433)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeByRefType(elementType: /* DmdType */, customModifiers: /* IList<DmdCustomModifier> */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract DmdType MakeFunctionPointerType(DmdMethodSignature methodSignature, IList<DmdCustomModifier> customModifiers, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Makes a function pointer type
  - Parameters:
    - `DmdMethodSignature methodSignature`: Method signature
    - `IList<DmdCustomModifier> customModifiers`: Custom modifiers or null
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 482)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeFunctionPointerType(methodSignature: /* DmdMethodSignature */, customModifiers: /* IList<DmdCustomModifier> */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract DmdType MakeFunctionPointerType(DmdSignatureCallingConvention flags, int genericParameterCount, DmdType returnType, IList<DmdType> parameterTypes, IList<DmdType> varArgsParameterTypes, IList<DmdCustomModifier> customModifiers, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Makes a function pointer type
  - Parameters:
    - `DmdSignatureCallingConvention flags`: Flags
    - `int genericParameterCount`: Number of generic parameters
    - `DmdType returnType`: Return type
    - `IList<DmdType> parameterTypes`: Parameter types
    - `IList<DmdType> varArgsParameterTypes`: VarArgs parameter types
    - `IList<DmdCustomModifier> customModifiers`: Custom modifiers or null
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 495)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeFunctionPointerType(flags: /* DmdSignatureCallingConvention */, genericParameterCount: /* int */, returnType: /* DmdType */, parameterTypes: /* IList<DmdType> */, varArgsParameterTypes: /* IList<DmdType> */, customModifiers: /* IList<DmdCustomModifier> */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract DmdType MakeGenericMethodParameter(int position, DmdMethodBase declaringMethod, string name, DmdGenericParameterAttributes attributes, IList<DmdCustomModifier> customModifiers, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Makes a generic method parameter
  - Parameters:
    - `int position`: Position
    - `DmdMethodBase declaringMethod`: Declaring method
    - `string name`: Name
    - `DmdGenericParameterAttributes attributes`: Attributes
    - `IList<DmdCustomModifier> customModifiers`: Custom modifiers or null
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 535)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericMethodParameter(position: /* int */, declaringMethod: /* DmdMethodBase */, name: /* string */, attributes: /* DmdGenericParameterAttributes */, customModifiers: /* IList<DmdCustomModifier> */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract DmdType MakeGenericType(DmdType genericTypeDefinition, IList<DmdType> typeArguments, IList<DmdCustomModifier> customModifiers, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Makes a generic type
  - Parameters:
    - `DmdType genericTypeDefinition`: Generic type definition
    - `IList<DmdType> typeArguments`: Generic arguments
    - `IList<DmdCustomModifier> customModifiers`: Custom modifiers or null
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 464)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericType(genericTypeDefinition: /* DmdType */, typeArguments: /* IList<DmdType> */, customModifiers: /* IList<DmdCustomModifier> */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract DmdType MakeGenericTypeParameter(int position, DmdType declaringType, string name, DmdGenericParameterAttributes attributes, IList<DmdCustomModifier> customModifiers, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Makes a generic type parameter
  - Parameters:
    - `int position`: Position
    - `DmdType declaringType`: Declaring type
    - `string name`: Name
    - `DmdGenericParameterAttributes attributes`: Attributes
    - `IList<DmdCustomModifier> customModifiers`: Custom modifiers or null
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 515)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericTypeParameter(position: /* int */, declaringType: /* DmdType */, name: /* string */, attributes: /* DmdGenericParameterAttributes */, customModifiers: /* IList<DmdCustomModifier> */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract DmdType MakePointerType(DmdType elementType, IList<DmdCustomModifier> customModifiers, DmdMakeTypeOptions options = DmdMakeTypeOptions.None)`
  - Summary: Makes a pointer type
  - Parameters:
    - `DmdType elementType`: Element type
    - `IList<DmdCustomModifier> customModifiers`: Custom modifiers or null
    - `DmdMakeTypeOptions options` (default: `DmdMakeTypeOptions.None`): Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 424)
  - Example:
    ```csharp
    // Example invocation
    instance.MakePointerType(elementType: /* DmdType */, customModifiers: /* IList<DmdCustomModifier> */, options: /* DmdMakeTypeOptions */);
    ```
- `public abstract object CreateInstance(object context, DmdConstructorInfo ctor, object[] parameters)`
  - Summary: Creates a new instance of a type
  - Parameters:
    - `object context`: Evaluation context
    - `DmdConstructorInfo ctor`: Constructor
    - `object[] parameters`: Parameters passed to the method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 595)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInstance(context: /* object */, ctor: /* DmdConstructorInfo */, parameters: /* object[] */);
    ```
- `public abstract object Invoke(object context, DmdMethodBase method, object obj, object[] parameters)`
  - Summary: Executes a method
  - Parameters:
    - `object context`: Evaluation context
    - `DmdMethodBase method`: Method to call
    - `object obj`: Instance object or null if it's a static method
    - `object[] parameters`: Parameters passed to the method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 605)
  - Example:
    ```csharp
    // Example invocation
    instance.Invoke(context: /* object */, method: /* DmdMethodBase */, obj: /* object */, parameters: /* object[] */);
    ```
- `public abstract object LoadField(object context, DmdFieldInfo field, object obj)`
  - Summary: Loads a field
  - Parameters:
    - `object context`: Evaluation context
    - `DmdFieldInfo field`: Field
    - `object obj`: Instance object or null if it's a static field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 614)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadField(context: /* object */, field: /* DmdFieldInfo */, obj: /* object */);
    ```
- `public abstract void Add(DmdAssembly assembly)`
  - Summary: Adds an assembly
  - Parameters:
    - `DmdAssembly assembly`: Assembly to add
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 242)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(assembly: /* DmdAssembly */);
    ```
- `public abstract void Remove(DmdAssembly assembly)`
  - Summary: Removes an assembly
  - Parameters:
    - `DmdAssembly assembly`: Assembly to remove
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 248)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(assembly: /* DmdAssembly */);
    ```
- `public abstract void StoreField(object context, DmdFieldInfo field, object obj, object value)`
  - Summary: Stores a value in a field
  - Parameters:
    - `object context`: Evaluation context
    - `DmdFieldInfo field`: Field
    - `object obj`: Instance object or null if it's a static field
    - `object value`: Value to store in the field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 623)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreField(context: /* object */, field: /* DmdFieldInfo */, obj: /* object */, value: /* object */);
    ```
- `public bool HasWellKnownType(DmdWellKnownType wellKnownType)`
  - Summary: Checks if a well known type exists in one of the loaded assemblies
  - Parameters:
    - `DmdWellKnownType wellKnownType`: Well known type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 342)
  - Example:
    ```csharp
    // Example invocation
    instance.HasWellKnownType(wellKnownType: /* DmdWellKnownType */);
    ```

### Properties

- `public DmdType System_ArgIterator => GetWellKnownType(DmdWellKnownType.System_ArgIterator)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 399)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_ArgIterator;
    ```
- `public DmdType System_Array => GetWellKnownType(DmdWellKnownType.System_Array)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 385)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Array;
    ```
- `public DmdType System_AsyncCallback => GetWellKnownType(DmdWellKnownType.System_AsyncCallback)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 405)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_AsyncCallback;
    ```
- `public DmdType System_Boolean => GetWellKnownType(DmdWellKnownType.System_Boolean)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 369)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Boolean;
    ```
- `public DmdType System_Byte => GetWellKnownType(DmdWellKnownType.System_Byte)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 372)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Byte;
    ```
- `public DmdType System_Char => GetWellKnownType(DmdWellKnownType.System_Char)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 370)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Char;
    ```
- `public DmdType System_Collections_Generic_ICollection_T => GetWellKnownType(DmdWellKnownType.System_Collections_Generic_ICollection_T)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 389)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Collections_Generic_ICollection_T;
    ```
- `public DmdType System_Collections_Generic_IEnumerable_T => GetWellKnownType(DmdWellKnownType.System_Collections_Generic_IEnumerable_T)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 387)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Collections_Generic_IEnumerable_T;
    ```
- `public DmdType System_Collections_Generic_IEnumerator_T => GetWellKnownType(DmdWellKnownType.System_Collections_Generic_IEnumerator_T)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 391)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Collections_Generic_IEnumerator_T;
    ```
- `public DmdType System_Collections_Generic_IList_T => GetWellKnownType(DmdWellKnownType.System_Collections_Generic_IList_T)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 388)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Collections_Generic_IList_T;
    ```
- `public DmdType System_Collections_Generic_IReadOnlyCollection_T => GetWellKnownType(DmdWellKnownType.System_Collections_Generic_IReadOnlyCollection_T)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 393)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Collections_Generic_IReadOnlyCollection_T;
    ```
- `public DmdType System_Collections_Generic_IReadOnlyList_T => GetWellKnownType(DmdWellKnownType.System_Collections_Generic_IReadOnlyList_T)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 392)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Collections_Generic_IReadOnlyList_T;
    ```
- `public DmdType System_Collections_IEnumerable => GetWellKnownType(DmdWellKnownType.System_Collections_IEnumerable)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 386)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Collections_IEnumerable;
    ```
- `public DmdType System_Collections_IEnumerator => GetWellKnownType(DmdWellKnownType.System_Collections_IEnumerator)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 390)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Collections_IEnumerator;
    ```
- `public DmdType System_DateTime => GetWellKnownType(DmdWellKnownType.System_DateTime)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 395)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_DateTime;
    ```
- `public DmdType System_Decimal => GetWellKnownType(DmdWellKnownType.System_Decimal)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 379)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Decimal;
    ```
- `public DmdType System_Delegate => GetWellKnownType(DmdWellKnownType.System_Delegate)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 366)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Delegate;
    ```
- `public DmdType System_Double => GetWellKnownType(DmdWellKnownType.System_Double)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 381)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Double;
    ```
- `public DmdType System_Enum => GetWellKnownType(DmdWellKnownType.System_Enum)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 364)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Enum;
    ```
- `public DmdType System_IAsyncResult => GetWellKnownType(DmdWellKnownType.System_IAsyncResult)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 404)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_IAsyncResult;
    ```
- `public DmdType System_IDisposable => GetWellKnownType(DmdWellKnownType.System_IDisposable)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 397)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_IDisposable;
    ```
- `public DmdType System_Int16 => GetWellKnownType(DmdWellKnownType.System_Int16)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 373)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Int16;
    ```
- `public DmdType System_Int32 => GetWellKnownType(DmdWellKnownType.System_Int32)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 375)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Int32;
    ```
- `public DmdType System_Int64 => GetWellKnownType(DmdWellKnownType.System_Int64)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 377)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Int64;
    ```
- `public DmdType System_IntPtr => GetWellKnownType(DmdWellKnownType.System_IntPtr)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 383)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_IntPtr;
    ```
- `public DmdType System_MulticastDelegate => GetWellKnownType(DmdWellKnownType.System_MulticastDelegate)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 365)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_MulticastDelegate;
    ```
- `public DmdType System_Nullable_T => GetWellKnownType(DmdWellKnownType.System_Nullable_T)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 394)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Nullable_T;
    ```
- `public DmdType System_Object => GetWellKnownType(DmdWellKnownType.System_Object)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 363)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Object;
    ```
- `public DmdType System_RuntimeArgumentHandle => GetWellKnownType(DmdWellKnownType.System_RuntimeArgumentHandle)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 400)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_RuntimeArgumentHandle;
    ```
- `public DmdType System_RuntimeFieldHandle => GetWellKnownType(DmdWellKnownType.System_RuntimeFieldHandle)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 401)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_RuntimeFieldHandle;
    ```
- `public DmdType System_RuntimeMethodHandle => GetWellKnownType(DmdWellKnownType.System_RuntimeMethodHandle)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 402)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_RuntimeMethodHandle;
    ```
- `public DmdType System_RuntimeTypeHandle => GetWellKnownType(DmdWellKnownType.System_RuntimeTypeHandle)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 403)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_RuntimeTypeHandle;
    ```
- `public DmdType System_Runtime_CompilerServices_IsVolatile => GetWellKnownType(DmdWellKnownType.System_Runtime_CompilerServices_IsVolatile)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 396)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Runtime_CompilerServices_IsVolatile;
    ```
- `public DmdType System_SByte => GetWellKnownType(DmdWellKnownType.System_SByte)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 371)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_SByte;
    ```
- `public DmdType System_Single => GetWellKnownType(DmdWellKnownType.System_Single)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 380)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Single;
    ```
- `public DmdType System_String => GetWellKnownType(DmdWellKnownType.System_String)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 382)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_String;
    ```
- `public DmdType System_Type => GetWellKnownType(DmdWellKnownType.System_Type)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 406)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Type;
    ```
- `public DmdType System_TypedReference => GetWellKnownType(DmdWellKnownType.System_TypedReference)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 398)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_TypedReference;
    ```
- `public DmdType System_UInt16 => GetWellKnownType(DmdWellKnownType.System_UInt16)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 374)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_UInt16;
    ```
- `public DmdType System_UInt32 => GetWellKnownType(DmdWellKnownType.System_UInt32)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 376)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_UInt32;
    ```
- `public DmdType System_UInt64 => GetWellKnownType(DmdWellKnownType.System_UInt64)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 378)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_UInt64;
    ```
- `public DmdType System_UIntPtr => GetWellKnownType(DmdWellKnownType.System_UIntPtr)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 384)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_UIntPtr;
    ```
- `public DmdType System_ValueType => GetWellKnownType(DmdWellKnownType.System_ValueType)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 367)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_ValueType;
    ```
- `public DmdType System_Void => GetWellKnownType(DmdWellKnownType.System_Void)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 368)
  - Example:
    ```csharp
    // Read the property
    var value = instance.System_Void;
    ```
- `public abstract DmdAssembly CorLib { get; }`
  - Summary: Gets the core library (eg. mscorlib if it's .NET Framework)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 335)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CorLib;
    ```
- `public abstract DmdRuntime Runtime { get; }`
  - Summary: Gets the runtime
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract int Id { get; }`
  - Summary: Gets the unique AppDomain id
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Struct `TemporaryAssemblyDisposable`

Adds and removes an assembly

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdAppDomain.TemporaryAssemblyDisposable and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdAppDomain.TemporaryAssemblyDisposable(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 260)

### Methods

- `public void Dispose()`
  - Summary: Dispose()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 270)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

## Class `DmdAppDomainExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Debugger.DotNet.Metadata.DmdAppDomainExtensions members directly without instantiation.
dnSpy.Debugger.DotNet.Metadata.DmdAppDomainExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DmdAppDomainExtensions.cs` (line 26)

### Methods

- `public static DbgAppDomain GetDebuggerAppDomain(this DmdAppDomain appDomain)`
  - Summary: Gets the debugger AppDomain object
  - Parameters:
    - `this DmdAppDomain appDomain`: Debugger metadata AppDomain object
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DmdAppDomainExtensions.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Metadata.DmdAppDomainExtensions.GetDebuggerAppDomain(appDomain: /* DmdAppDomain */);
    ```

## Class `DmdAssembly`

A .NET assembly

**Inherits/Implements:** `DmdObject`, `IDmdCustomAttributeProvider`, `IDmdSecurityAttributeProvider`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdAssembly and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdAssembly(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 29)

### Methods

- `private protected abstract void YouCantDeriveFromThisClass()`
  - Summary: Dummy abstract method to make sure no-one outside this assembly can create their own
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.YouCantDeriveFromThisClass();
    ```
- `public DmdCustomAttributeData FindCustomAttribute(DmdType attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 260)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public DmdCustomAttributeData FindCustomAttribute(Type attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `Type attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 268)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* Type */, inherit: /* bool */);
    ```
- `public DmdCustomAttributeData FindCustomAttribute(string attributeTypeFullName, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 252)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `public DmdType GetType(Type type)`
  - Summary: Gets a type
  - Parameters:
    - `Type type`: Type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(type: /* Type */);
    ```
- `public DmdType GetType(Type type, DmdGetTypeOptions options)`
  - Summary: Gets a type
  - Parameters:
    - `Type type`: Type
    - `DmdGetTypeOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 124)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(type: /* Type */, options: /* DmdGetTypeOptions */);
    ```
- `public DmdType GetType(string name)`
  - Summary: Gets a type in this assembly or null if it doesn't exist
  - Parameters:
    - `string name`: Name of type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(name: /* string */);
    ```
- `public DmdType GetType(string name, bool throwOnError)`
  - Summary: Gets a type in this assembly
  - Parameters:
    - `string name`: Name of type
    - `bool throwOnError`: true to throw if the type doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 150)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(name: /* string */, throwOnError: /* bool */);
    ```
- `public DmdType GetType(string name, bool throwOnError, bool ignoreCase)`
  - Summary: Gets a type in this assembly
  - Parameters:
    - `string name`: Name of type
    - `bool throwOnError`: true to throw if the type doesn't exist
    - `bool ignoreCase`: true if case insensitive comparisons
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 159)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(name: /* string */, throwOnError: /* bool */, ignoreCase: /* bool */);
    ```
- `public DmdType GetTypeThrow(Type type)`
  - Summary: Gets a type and throws if it couldn't be found
  - Parameters:
    - `Type type`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 116)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTypeThrow(type: /* Type */);
    ```
- `public DmdType GetTypeThrow(string name)`
  - Summary: Gets a type and throws if it couldn't be found
  - Parameters:
    - `string name`: Name of type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 142)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTypeThrow(name: /* string */);
    ```
- `public DmdType[] GetTypes()`
  - Summary: Gets all types in this assembly
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 190)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTypes();
    ```
- `public abstract DmdModule GetModule(string name)`
  - Summary: Gets a module
  - Parameters:
    - `string name`: Name of module
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 363)
  - Example:
    ```csharp
    // Example invocation
    instance.GetModule(name: /* string */);
    ```
- `public abstract DmdModule[] GetLoadedModules()`
  - Summary: Gets all loaded modules
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 350)
  - Example:
    ```csharp
    // Example invocation
    instance.GetLoadedModules();
    ```
- `public abstract DmdModule[] GetModules()`
  - Summary: Gets all modules
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 356)
  - Example:
    ```csharp
    // Example invocation
    instance.GetModules();
    ```
- `public abstract DmdReadOnlyAssemblyName GetName()`
  - Summary: Gets the assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetName();
    ```
- `public abstract DmdReadOnlyAssemblyName[] GetReferencedAssemblies()`
  - Summary: Gets all referenced assemblies
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 369)
  - Example:
    ```csharp
    // Example invocation
    instance.GetReferencedAssemblies();
    ```
- `public abstract DmdType GetType(string typeName, DmdGetTypeOptions options)`
  - Summary: Gets a type
  - Parameters:
    - `string typeName`: Full name of the type ()
    - `DmdGetTypeOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 168)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(typeName: /* string */, options: /* DmdGetTypeOptions */);
    ```
- `public abstract DmdType[] GetExportedTypes()`
  - Summary: Gets all public types in this assembly
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 178)
  - Example:
    ```csharp
    // Example invocation
    instance.GetExportedTypes();
    ```
- `public abstract DmdType[] GetForwardedTypes()`
  - Summary: Gets all forwarded types (types that now exist in another assembly)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 184)
  - Example:
    ```csharp
    // Example invocation
    instance.GetForwardedTypes();
    ```
- `public abstract ReadOnlyCollection<DmdCustomAttributeData> GetCustomAttributesData()`
  - Summary: Gets the custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 220)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCustomAttributesData();
    ```
- `public abstract ReadOnlyCollection<DmdCustomAttributeData> GetSecurityAttributesData()`
  - Summary: Gets the security attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 209)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSecurityAttributesData();
    ```
- `public abstract void Remove(DmdModule module)`
  - Summary: Removes a module from the assembly
  - Parameters:
    - `DmdModule module`: Module to remove
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 375)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(module: /* DmdModule */);
    ```
- `public bool IsDefined(DmdType attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 236)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public bool IsDefined(Type attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `Type attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 244)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* Type */, inherit: /* bool */);
    ```
- `public bool IsDefined(string attributeTypeFullName, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 228)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `public object CreateInstance(object context, string typeName)`
  - Summary: Creates an instance of a type
  - Parameters:
    - `object context`: Evaluation context
    - `string typeName`: Fully qualified name of type to create
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 275)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInstance(context: /* object */, typeName: /* string */);
    ```
- `public object CreateInstance(object context, string typeName, bool ignoreCase)`
  - Summary: Creates an instance of a type
  - Parameters:
    - `object context`: Evaluation context
    - `string typeName`: Fully qualified name of type to create
    - `bool ignoreCase`: true to ignore case
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 283)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInstance(context: /* object */, typeName: /* string */, ignoreCase: /* bool */);
    ```
- `public object CreateInstance(object context, string typeName, bool ignoreCase, DmdBindingFlags bindingAttr, object[] args)`
  - Summary: Creates an instance of a type
  - Parameters:
    - `object context`: Evaluation context
    - `string typeName`: Fully qualified name of type to create
    - `bool ignoreCase`: true to ignore case
    - `DmdBindingFlags bindingAttr`: Binding attributes
    - `object[] args`: Constructor arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 293)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInstance(context: /* object */, typeName: /* string */, ignoreCase: /* bool */, bindingAttr: /* DmdBindingFlags */, args: /* object[] */);
    ```
- `public object CreateInstance(object context, string typeName, bool ignoreCase, DmdBindingFlags bindingAttr, object[] args, IList<DmdType> argTypes)`
  - Summary: Creates an instance of a type
  - Parameters:
    - `object context`: Evaluation context
    - `string typeName`: Fully qualified name of type to create
    - `bool ignoreCase`: true to ignore case
    - `DmdBindingFlags bindingAttr`: Binding attributes
    - `object[] args`: Constructor arguments or null
    - `IList<DmdType> argTypes`: Constructor parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 305)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInstance(context: /* object */, typeName: /* string */, ignoreCase: /* bool */, bindingAttr: /* DmdBindingFlags */, args: /* object[] */, argTypes: /* IList<DmdType> */);
    ```
- `public object CreateInstance(object context, string typeName, bool ignoreCase, DmdBindingFlags bindingAttr, object[] args, IList<Type> argTypes)`
  - Summary: Creates an instance of a type
  - Parameters:
    - `object context`: Evaluation context
    - `string typeName`: Fully qualified name of type to create
    - `bool ignoreCase`: true to ignore case
    - `DmdBindingFlags bindingAttr`: Binding attributes
    - `object[] args`: Constructor arguments or null
    - `IList<Type> argTypes`: Constructor parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 338)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInstance(context: /* object */, typeName: /* string */, ignoreCase: /* bool */, bindingAttr: /* DmdBindingFlags */, args: /* object[] */, argTypes: /* IList<Type> */);
    ```
- `public sealed override string ToString()`
  - Summary: Gets the full name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 381)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static string CreateQualifiedName(string assemblyName, string typeName)`
  - Summary: Creates a qualified type name
  - Parameters:
    - `string assemblyName`: Full assembly name of the type
    - `string typeName`: Full type name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Metadata.DmdAssembly.CreateQualifiedName(assemblyName: /* string */, typeName: /* string */);
    ```

### Properties

- `public IEnumerable<DmdModule> Modules => GetLoadedModules()`
  - Summary: Gets all loaded modules
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 344)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Modules;
    ```
- `public IEnumerable<DmdType> ExportedTypes => GetExportedTypes()`
  - Summary: Gets all public types in this assembly
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 173)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExportedTypes;
    ```
- `public ReadOnlyCollection<DmdCustomAttributeData> CustomAttributes => GetCustomAttributesData()`
  - Summary: Gets the custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 214)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CustomAttributes;
    ```
- `public ReadOnlyCollection<DmdCustomAttributeData> SecurityAttributes => GetSecurityAttributesData()`
  - Summary: Gets the security attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 203)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SecurityAttributes;
    ```
- `public abstract DmdAppDomain AppDomain { get; }`
  - Summary: Gets the AppDomain
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public abstract DmdMethodInfo EntryPoint { get; }`
  - Summary: Gets the entry point or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EntryPoint;
    ```
- `public abstract DmdModule ManifestModule { get; }`
  - Summary: Gets the first module of this assembly
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ManifestModule;
    ```
- `public abstract bool IsLoaded { get; }`
  - Summary: true if the assembly has been added to its AppDomain
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsLoaded;
    ```
- `public abstract string ImageRuntimeVersion { get; }`
  - Summary: Gets the runtime version found in the metadata
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ImageRuntimeVersion;
    ```
- `public abstract string Location { get; }`
  - Summary: Gets the assembly location or an empty string
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Location;
    ```
- `public bool IsCorLib => this == AppDomain.CorLib`
  - Summary: true if this is the corlib assembly
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsCorLib;
    ```
- `public bool IsDynamic => ManifestModule.IsDynamic`
  - Summary: true if it's a dynamic assembly (types can be added at runtime)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDynamic;
    ```
- `public bool IsInMemory => ManifestModule.IsInMemory`
  - Summary: true if it's an in-memory assembly (eg. loaded from a array)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInMemory;
    ```
- `public bool IsSynthetic => ManifestModule.IsSynthetic`
  - Summary: true if it's a synthetic assembly; it's not loaded in the debugged process
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSynthetic;
    ```
- `public string FullName => GetName().ToString()`
  - Summary: Gets the full name of the assembly
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssembly.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FullName;
    ```

## Enum `DmdAssemblyContentType`

Assembly content type

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdAssemblyContentType and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdAssemblyContentType(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyContentType.cs` (line 24)

### Members

- `Default`: Default content type
- `WindowsRuntime`: Windows runtime content type

## Enum `DmdAssemblyHashAlgorithm`

Assembly hash algorithm

**Inherits/Implements:** `uint`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdAssemblyHashAlgorithm and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdAssemblyHashAlgorithm(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyHashAlgorithm.cs` (line 24)

### Members

- `None`
- `MD5` = `x8003`
- `SHA1` = `x8004`
- `SHA256` = `x800C`
- `SHA384` = `x800D`
- `SHA512` = `x800E`

## Class `DmdAssemblyName`

Assembly name

**Inherits/Implements:** `IDmdAssemblyName`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdAssemblyName();
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 27)

### Constructors

- `public DmdAssemblyName()`
  - Summary: Constructor
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 131)
- `public DmdAssemblyName(IDmdAssemblyName name)`
  - Summary: Constructor
  - Parameters:
    - `IDmdAssemblyName name`: Assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 173)
- `public DmdAssemblyName(string assemblyName)`
  - Summary: Constructor
  - Parameters:
    - `string assemblyName`: Assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 158)

### Methods

- `public DmdAssemblyName Clone()`
  - Summary: Clones this instance
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 195)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```
- `public DmdReadOnlyAssemblyName AsReadOnly()`
  - Summary: Creates a read only assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 189)
  - Example:
    ```csharp
    // Example invocation
    instance.AsReadOnly();
    ```
- `public byte[] GetPublicKey()`
  - Summary: Gets the public key
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPublicKey();
    ```
- `public byte[] GetPublicKeyToken()`
  - Summary: Gets the public key token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPublicKeyToken();
    ```
- `public override string ToString()`
  - Summary: Gets the full assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public void SetPublicKey(byte[] publicKey)`
  - Summary: Sets the public key
  - Parameters:
    - `byte[] publicKey`: Public key or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.SetPublicKey(publicKey: /* byte[] */);
    ```
- `public void SetPublicKeyToken(byte[] publicKeyToken)`
  - Summary: Sets the public key token
  - Parameters:
    - `byte[] publicKeyToken`: Public key token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 110)
  - Example:
    ```csharp
    // Example invocation
    instance.SetPublicKeyToken(publicKeyToken: /* byte[] */);
    ```

### Properties

- `public DmdAssemblyContentType ContentType {
			get => (DmdAssemblyContentType)((int)(RawFlags & DmdAssemblyNameFlags.ContentType_Mask) >> 9);
			set => RawFlags = (RawFlags & ~DmdAssemblyNameFlags.ContentType_Mask) | ((DmdAssemblyNameFlags)((int)value << 9) & DmdAssemblyNameFlags.ContentType_Mask);
		}`
  - Summary: Gets/sets the content type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentType;
    ```
- `public DmdAssemblyHashAlgorithm HashAlgorithm { get; set; }`
  - Summary: Gets/sets the hash algorithm
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 115)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HashAlgorithm;
    ```
- `public DmdAssemblyNameFlags Flags {
			get => RawFlags & ~(DmdAssemblyNameFlags.ContentType_Mask | DmdAssemblyNameFlags.PA_FullMask);
			set => RawFlags = (RawFlags & (DmdAssemblyNameFlags.ContentType_Mask | DmdAssemblyNameFlags.PA_FullMask)) | (value & ~(DmdAssemblyNameFlags.ContentType_Mask | DmdAssemblyNameFlags.PA_FullMask));
		}`
  - Summary: Gets/sets the flags. The content type and processor architecture bits are ignored, use instead
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public DmdAssemblyNameFlags RawFlags { get; set; }`
  - Summary: Gets/sets the flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RawFlags;
    ```
- `public DmdProcessorArchitecture ProcessorArchitecture {
			get => (DmdProcessorArchitecture)((int)(RawFlags & DmdAssemblyNameFlags.PA_Mask) >> 4);
			set => RawFlags = (RawFlags & ~DmdAssemblyNameFlags.PA_FullMask) | ((DmdAssemblyNameFlags)((int)value << 4) & DmdAssemblyNameFlags.PA_Mask);
		}`
  - Summary: Gets/sets the processor architecture
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessorArchitecture;
    ```
- `public Version Version { get; set; }`
  - Summary: Gets/sets the version
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Version;
    ```
- `public string CultureName { get; set; }`
  - Summary: Gets/sets the culture name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CultureName;
    ```
- `public string FullName => DmdAssemblyNameFormatter.Format(Name, Version, CultureName, GetPublicKeyToken(), RawFlags, isPublicKeyToken: true)`
  - Summary: Gets the full assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 120)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FullName;
    ```
- `public string Name { get; set; }`
  - Summary: Gets/sets the simple name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyName.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Enum `DmdAssemblyNameFlags`

Assembly name flags

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdAssemblyNameFlags and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdAssemblyNameFlags(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAssemblyNameFlags.cs` (line 26)

### Members

- `None`
- `PublicKey`
- `PA_None` = `x0000`
- `PA_MSIL` = `x0010`
- `PA_x86` = `x0020`
- `PA_IA64` = `x0030`
- `PA_AMD64` = `x0040`
- `PA_ARM` = `x0050`
- `PA_NoPlatform` = `x0070`
- `PA_Specified` = `x0080`
- `PA_Mask` = `x0070`
- `PA_FullMask` = `x00F0`
- `PA_Shift` = `x0004`
- `EnableJITcompileTracking` = `x8000`
- `DisableJITcompileOptimizer` = `x4000`
- `Retargetable` = `x0100`
- `ContentType_Default` = `x0000`
- `ContentType_WindowsRuntime` = `x0200`
- `ContentType_Mask` = `x0E00`

## Enum `DmdBindingFlags`

Member binding flags

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdBindingFlags and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdBindingFlags(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdBindingFlags.cs` (line 26)

### Members

- `Default`
- `IgnoreCase` = `x00000001`
- `DeclaredOnly` = `x00000002`
- `Instance` = `x00000004`
- `Static` = `x00000008`
- `Public` = `x00000010`
- `NonPublic` = `x00000020`
- `FlattenHierarchy` = `x00000040`
- `InvokeMethod` = `x00000100`
- `CreateInstance` = `x00000200`
- `GetField` = `x00000400`
- `SetField` = `x00000800`
- `GetProperty` = `x00001000`
- `SetProperty` = `x00002000`
- `PutDispProperty` = `x00004000`
- `PutRefDispProperty` = `x00008000`
- `ExactBinding` = `x00010000`
- `SuppressChangeType` = `x00020000`
- `OptionalParamBinding` = `x00040000`
- `IgnoreReturn` = `x01000000`
- `Inaccessible` = `nt.MinValue`

## Enum `DmdCallingConventions`

Calling convention flags

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdCallingConventions and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdCallingConventions(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCallingConventions.cs` (line 26)

### Members

- `Standard` = `x00000001`
- `VarArgs` = `x00000002`
- `Any` = `x00000003`
- `HasThis` = `x00000020`
- `ExplicitThis` = `x00000040`

## Class `DmdConstructorInfo`

A .NET constructor

**Inherits/Implements:** `DmdMethodBase`, `IEquatable<DmdConstructorInfo>`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdConstructorInfo and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdConstructorInfo(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 26)

### Methods

- `public DmdConstructorInfo Resolve()`
  - Summary: Resolves a constructor reference and throws if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve();
    ```
- `public DmdConstructorInfo ResolveNoThrow()`
  - Summary: Resolves a constructor reference and returns null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveNoThrow();
    ```
- `public abstract DmdConstructorInfo Resolve(bool throwOnError)`
  - Summary: Resolves a constructor reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 63)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve(throwOnError: /* bool */);
    ```
- `public abstract object Invoke(object context, DmdBindingFlags invokeAttr, object[] parameters)`
  - Summary: Calls the method
  - Parameters:
    - `object context`: Evaluation context
    - `DmdBindingFlags invokeAttr`: Binding flags
    - `object[] parameters`: Parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.Invoke(context: /* object */, invokeAttr: /* DmdBindingFlags */, parameters: /* object[] */);
    ```
- `public bool Equals(DmdConstructorInfo other)`
  - Summary: Equals()
  - Parameters:
    - `DmdConstructorInfo other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdConstructorInfo */);
    ```
- `public object Invoke(object context, object[] parameters)`
  - Summary: Calls the method
  - Parameters:
    - `object context`: Evaluation context
    - `object[] parameters`: Parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.Invoke(context: /* object */, parameters: /* object[] */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 110)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public sealed override DmdMemberInfo ResolveMember(bool throwOnError)`
  - Summary: Resolves a constructor reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(throwOnError: /* bool */);
    ```
- `public sealed override DmdMethodBase ResolveMethodBase(bool throwOnError)`
  - Summary: Resolves a constructor reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethodBase(throwOnError: /* bool */);
    ```

### Properties

- `public override bool ContainsGenericParameters => DeclaringType.ContainsGenericParameters`
  - Summary: true if it contains generic parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContainsGenericParameters;
    ```
- `public sealed override DmdMemberTypes MemberType => DmdMemberTypes.Constructor`
  - Summary: Gets the member type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberType;
    ```

### Fields

- `public static readonly string ConstructorName = ".ctor"`
  - Summary: Gets the name of instance constructors
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 115)
  - Example:
    ```csharp
    var value = dnSpy.Debugger.DotNet.Metadata.DmdConstructorInfo.ConstructorName;
    ```
- `public static readonly string TypeConstructorName = ".cctor"`
  - Summary: Gets the name of type initializers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 120)
  - Example:
    ```csharp
    var value = dnSpy.Debugger.DotNet.Metadata.DmdConstructorInfo.TypeConstructorName;
    ```

### Operators

- `public static bool operator !=(DmdConstructorInfo left, DmdConstructorInfo right) => !DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 89)
- `public static bool operator ==(DmdConstructorInfo left, DmdConstructorInfo right) => DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdConstructorInfo.cs` (line 88)

## Struct `DmdCreateAssemblyInfo`

Info needed when creating an assembly

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdCreateAssemblyInfo(options: /* DmdCreateAssemblyOptions */, fullyQualifiedName: /* string */, assemblyLocation: /* string */, assemblySimpleName: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 706)

### Constructors

- `public DmdCreateAssemblyInfo(DmdCreateAssemblyOptions options, string fullyQualifiedName, string assemblyLocation, string assemblySimpleName)`
  - Summary: Constructor
  - Parameters:
    - `DmdCreateAssemblyOptions options`: Options
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
    - `string assemblyLocation`: Location of the assembly or an empty string ()
    - `string assemblySimpleName`: The assembly's simple name or null if it's unknown
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 734)
- `public DmdCreateAssemblyInfo(bool isInMemory, bool isDynamic, bool isSynthetic, bool addAssembly, string fullyQualifiedName, string assemblyLocation, string assemblySimpleName)`
  - Summary: Constructor
  - Parameters:
    - `bool isInMemory`: true if the module is in memory ()
    - `bool isDynamic`: true if it's a dynamic module (types can be added at runtime) ()
    - `bool isSynthetic`: true if it's a synthetic assembly, eg. created by the expression compiler
    - `bool addAssembly`: true if the assembly should be added to the AppDomain
    - `string fullyQualifiedName`: The fully qualified name of the module (). See
    - `string assemblyLocation`: Location of the assembly or an empty string ()
    - `string assemblySimpleName`: The assembly's simple name or null if it's unknown
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 753)

### Properties

- `public DmdCreateAssemblyOptions Options { get; }`
  - Summary: Gets the options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 710)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```
- `public string AssemblyLocation { get; }`
  - Summary: Location of the assembly or an empty string ()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 720)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyLocation;
    ```
- `public string AssemblySimpleName { get; }`
  - Summary: Gets the assembly's simple name or null if it's unknown
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 725)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblySimpleName;
    ```
- `public string FullyQualifiedName { get; }`
  - Summary: The fully qualified name of the module (). See
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 715)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FullyQualifiedName;
    ```

## Enum `DmdCreateAssemblyOptions`

Create-assembly-options

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdCreateAssemblyOptions and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdCreateAssemblyOptions(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 666)

### Members

- `None`: No bit is set
- `InMemory` = `x00000001`: Set if the module is in memory ()
- `Dynamic` = `x00000002`: Set if it's a dynamic module (types can be added at runtime) ()
- `Synthetic` = `x00000004`: Synthetic assembly, eg. created by the expression compiler
- `DontAddAssembly` = `x00000008`: Don't add the assembly to the AppDomain
- `IsEXE` = `x00000010`: It's an exe file. If it's not set, it's either a DLL or it's unknown
- `IsDLL` = `x00000020`: It's a dll file. If it's not set, it's either an EXE or it's unknown

## Class `DmdCustomAttributeData`

Custom attribute data

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdCustomAttributeData(constructor: /* DmdConstructorInfo */, constructorArguments: /* IList<DmdCustomAttributeTypedArgument> */, namedArguments: /* IList<DmdCustomAttributeNamedArgument> */, isPseudoCustomAttribute: /* bool */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 28)

### Constructors

- `public DmdCustomAttributeData(DmdConstructorInfo constructor, IList<DmdCustomAttributeTypedArgument> constructorArguments, IList<DmdCustomAttributeNamedArgument> namedArguments, bool isPseudoCustomAttribute)`
  - Summary: Constructor
  - Parameters:
    - `DmdConstructorInfo constructor`: Custom attribute constructor
    - `IList<DmdCustomAttributeTypedArgument> constructorArguments`: Constructor arguments or null
    - `IList<DmdCustomAttributeNamedArgument> namedArguments`: Custom attribute named arguments (fields and properties) or null
    - `bool isPseudoCustomAttribute`: true if this custom attribute was not part of the #Blob but created from some other info
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 61)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdConstructorInfo Constructor { get; }`
  - Summary: Gets the custom attribute constructor
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Constructor;
    ```
- `public DmdType AttributeType => Constructor.DeclaringType`
  - Summary: Gets the custom attribute type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AttributeType;
    ```
- `public IList<DmdCustomAttributeNamedArgument> NamedArguments { get; }`
  - Summary: Gets all named arguments (properties and fields)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NamedArguments;
    ```
- `public IList<DmdCustomAttributeTypedArgument> ConstructorArguments { get; }`
  - Summary: Gets the constructor arguments
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ConstructorArguments;
    ```
- `public bool IsPseudoCustomAttribute { get; }`
  - Summary: true if this custom attribute was not part of the #Blob but created from some other info
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPseudoCustomAttribute;
    ```

## Struct `DmdCustomAttributeNamedArgument`

Custom attribute named argument

**Inherits/Implements:** `IEquatable<DmdCustomAttributeNamedArgument>`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdCustomAttributeNamedArgument(memberInfo: /* DmdMemberInfo */, typedArgument: /* DmdCustomAttributeTypedArgument */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 209)

### Constructors

- `public DmdCustomAttributeNamedArgument(DmdMemberInfo memberInfo, DmdCustomAttributeTypedArgument typedArgument)`
  - Summary: Constructor
  - Parameters:
    - `DmdMemberInfo memberInfo`: A property or a field
    - `DmdCustomAttributeTypedArgument typedArgument`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 235)

### Methods

- `public bool Equals(DmdCustomAttributeNamedArgument other)`
  - Summary: Equals()
  - Parameters:
    - `DmdCustomAttributeNamedArgument other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 252)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdCustomAttributeNamedArgument */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 259)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 265)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 271)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdCustomAttributeTypedArgument TypedValue { get; }`
  - Summary: Gets the value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 218)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypedValue;
    ```
- `public DmdMemberInfo MemberInfo { get; }`
  - Summary: Gets the member (a property or a field)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 213)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberInfo;
    ```
- `public bool IsField => MemberInfo.MemberType == DmdMemberTypes.Field`
  - Summary: true if it's a field, false if it's a property
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 228)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsField;
    ```
- `public string MemberName => MemberInfo.Name`
  - Summary: Gets the member name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 223)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberName;
    ```

### Operators

- `public static bool operator !=(DmdCustomAttributeNamedArgument left, DmdCustomAttributeNamedArgument right) => !left.Equals(right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 244)
- `public static bool operator ==(DmdCustomAttributeNamedArgument left, DmdCustomAttributeNamedArgument right) => left.Equals(right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 243)

## Struct `DmdCustomAttributeTypedArgument`

Custom attribute typed argument

**Inherits/Implements:** `IEquatable<DmdCustomAttributeTypedArgument>`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdCustomAttributeTypedArgument(argumentType: /* DmdType */, value: /* object */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 98)

### Constructors

- `public DmdCustomAttributeTypedArgument(DmdType argumentType, object value)`
  - Summary: Constructor
  - Parameters:
    - `DmdType argumentType`: Argument type
    - `object value`: Argument value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 114)

### Methods

- `public bool Equals(DmdCustomAttributeTypedArgument other)`
  - Summary: Equals()
  - Parameters:
    - `DmdCustomAttributeTypedArgument other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 190)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdCustomAttributeTypedArgument */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 197)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 203)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 147)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdType ArgumentType { get; }`
  - Summary: Gets the argument type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ArgumentType;
    ```
- `public object Value { get; }`
  - Summary: Gets the argument value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```

### Operators

- `public static bool operator !=(DmdCustomAttributeTypedArgument left, DmdCustomAttributeTypedArgument right) => !left.Equals(right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 182)
- `public static bool operator ==(DmdCustomAttributeTypedArgument left, DmdCustomAttributeTypedArgument right) => left.Equals(right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomAttributeData.cs` (line 181)

## Struct `DmdCustomModifier`

A required or optional custom modifier

**Inherits/Implements:** `IEquatable<DmdCustomModifier>`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdCustomModifier(type: /* DmdType */, isRequired: /* bool */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 26)

### Constructors

- `public DmdCustomModifier(DmdType type, bool isRequired)`
  - Summary: Constructor
  - Parameters:
    - `DmdType type`: Type
    - `bool isRequired`: true if it's a required C modifier, false if it's an optional C modifier
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 47)

### Methods

- `public bool Equals(DmdCustomModifier other)`
  - Summary: Equals()
  - Parameters:
    - `DmdCustomModifier other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdCustomModifier */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdType Type { get; }`
  - Summary: Gets the type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public bool IsOptional => !IsRequired`
  - Summary: true if it's an optional C modifier
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOptional;
    ```
- `public bool IsRequired { get; }`
  - Summary: true if it's a required C modifier
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRequired;
    ```

### Operators

- `public static bool operator !=(DmdCustomModifier left, DmdCustomModifier right) => !DmdMemberInfoEqualityComparer.DefaultCustomModifier.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 54)
- `public static bool operator ==(DmdCustomModifier left, DmdCustomModifier right) => DmdMemberInfoEqualityComparer.DefaultCustomModifier.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdCustomModifier.cs` (line 53)

## Class `DmdDataStream`

Data stream

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdDataStream and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdDataStream(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 27)

### Methods

- `public abstract byte ReadByte()`
  - Summary: Reads a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadByte();
    ```
- `public abstract byte[] ReadBytes(int length)`
  - Summary: Reads bytes
  - Parameters:
    - `int length`: Number of bytes to read
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadBytes(length: /* int */);
    ```
- `public abstract double ReadDouble()`
  - Summary: Reads a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadDouble();
    ```
- `public abstract float ReadSingle()`
  - Summary: Reads a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadSingle();
    ```
- `public abstract uint ReadUInt32()`
  - Summary: Reads a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt32();
    ```
- `public abstract ulong ReadUInt64()`
  - Summary: Reads a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt64();
    ```
- `public abstract ushort ReadUInt16()`
  - Summary: Reads a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadUInt16();
    ```
- `public abstract void Dispose()`
  - Summary: Disposes this instance
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```
- `public int ReadCompressedInt32()`
  - Summary: Reads a compressed
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 124)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadCompressedInt32();
    ```
- `public int ReadInt32()`
  - Summary: Reads a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt32();
    ```
- `public long ReadInt64()`
  - Summary: Reads a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt64();
    ```
- `public sbyte ReadSByte()`
  - Summary: Reads a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadSByte();
    ```
- `public short ReadInt16()`
  - Summary: Reads a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadInt16();
    ```
- `public uint ReadCompressedUInt32()`
  - Summary: Reads a compressed
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadCompressedUInt32();
    ```

### Properties

- `public abstract long Length { get; }`
  - Summary: Gets the stream length
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public abstract long Position { get; set; }`
  - Summary: Gets/sets the position
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDataStream.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Position;
    ```

## Class `DmdDispatcher`

Invokes code on another thread. It's used if the underlying .NET metadata reader is a COM interface.

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdDispatcher and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdDispatcher(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDispatcher.cs` (line 27)

### Methods

- `public abstract T Invoke<T>(Func<T> callback)`
  - Summary: Switches to the dispatcher thread and executes
  - Parameters:
    - `Func<T> callback`: Code to execute
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDispatcher.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.Invoke(callback: /* Func<T> */);
    ```
- `public abstract bool CheckAccess()`
  - Summary: Checks whether the current thread is the dispatcher thread
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDispatcher.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.CheckAccess();
    ```
- `public abstract void Invoke(Action callback)`
  - Summary: Switches to the dispatcher thread and executes
  - Parameters:
    - `Action callback`: Code to execute
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDispatcher.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.Invoke(callback: /* Action */);
    ```
- `public void VerifyAccess()`
  - Summary: Throws if the current thread isn't the dispatcher thread
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDispatcher.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.VerifyAccess();
    ```

## Class `DmdDynamicModuleHelper`

Returns info to the COM MetaDataImport reader code that isn't made available by the COM MetaDataImport API

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdDynamicModuleHelper and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdDynamicModuleHelper(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDynamicModuleHelper.cs` (line 26)

### Methods

- `public abstract DmdDataStream TryGetMethodBody(DmdModule module, int metadataToken, uint rva)`
  - Summary: Called to get the method body stream or null if there's no method body. This method should use the CLR debugger API to get the address of the method body. This method is only called on the COM thread.
  - Parameters:
    - `DmdModule module`: Module
    - `int metadataToken`: Metadata token of the method
    - `uint rva`: RVA of method body
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDynamicModuleHelper.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetMethodBody(module: /* DmdModule */, metadataToken: /* int */, rva: /* uint */);
    ```

### Events

- `public abstract event EventHandler<DmdTypeLoadedEventArgs> TypeLoaded`
  - Summary: Raised when a new type in this module is loaded. It must be raised on the COM thread.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDynamicModuleHelper.cs` (line 43)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.TypeLoaded += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DmdEvaluator`

Executes methods and loads/stores fields

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdEvaluator and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdEvaluator(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEvaluator.cs` (line 24)

### Methods

- `public abstract object CreateInstance(object context, DmdConstructorInfo ctor, object[] arguments)`
  - Summary: Creates a new instance of a type
  - Parameters:
    - `object context`: Evaluation context
    - `DmdConstructorInfo ctor`: Constructor
    - `object[] arguments`: Arguments passed to the constructor
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEvaluator.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateInstance(context: /* object */, ctor: /* DmdConstructorInfo */, arguments: /* object[] */);
    ```
- `public abstract object Invoke(object context, DmdMethodBase method, object obj, object[] arguments)`
  - Summary: Executes a method
  - Parameters:
    - `object context`: Evaluation context
    - `DmdMethodBase method`: Method to call
    - `object obj`: Instance object or null if it's a constructor or a static method
    - `object[] arguments`: Arguments passed to the method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEvaluator.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.Invoke(context: /* object */, method: /* DmdMethodBase */, obj: /* object */, arguments: /* object[] */);
    ```
- `public abstract object LoadField(object context, DmdFieldInfo field, object obj)`
  - Summary: Loads a field
  - Parameters:
    - `object context`: Evaluation context
    - `DmdFieldInfo field`: Field
    - `object obj`: Instance object or null if it's a static field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEvaluator.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.LoadField(context: /* object */, field: /* DmdFieldInfo */, obj: /* object */);
    ```
- `public abstract void StoreField(object context, DmdFieldInfo field, object obj, object value)`
  - Summary: Stores a value in a field
  - Parameters:
    - `object context`: Evaluation context
    - `DmdFieldInfo field`: Field
    - `object obj`: Instance object or null if it's a static field
    - `object value`: Value to store in the field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEvaluator.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.StoreField(context: /* object */, field: /* DmdFieldInfo */, obj: /* object */, value: /* object */);
    ```

## Enum `DmdEventAttributes`

Event attributes

**Inherits/Implements:** `ushort`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdEventAttributes and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdEventAttributes(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventAttributes.cs` (line 26)

### Members

- `SpecialName` = `x0200`
- `RTSpecialName` = `x0400`

## Class `DmdEventInfo`

A .NET event

**Inherits/Implements:** `DmdMemberInfo`, `IEquatable<DmdEventInfo>`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdEventInfo and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdEventInfo(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 26)

### Methods

- `public DmdMethodInfo GetAddMethod()`
  - Summary: Gets the public add method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAddMethod();
    ```
- `public DmdMethodInfo GetAddMethod(bool nonPublic)`
  - Summary: Gets the add method
  - Parameters:
    - `bool nonPublic`: true to return any method, false to only return a public method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAddMethod(nonPublic: /* bool */);
    ```
- `public DmdMethodInfo GetRaiseMethod()`
  - Summary: Gets the public raise method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 111)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRaiseMethod();
    ```
- `public DmdMethodInfo GetRaiseMethod(bool nonPublic)`
  - Summary: Gets the raise method
  - Parameters:
    - `bool nonPublic`: true to return any method, false to only return a public method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 160)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRaiseMethod(nonPublic: /* bool */);
    ```
- `public DmdMethodInfo GetRemoveMethod()`
  - Summary: Gets the public remove method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRemoveMethod();
    ```
- `public DmdMethodInfo GetRemoveMethod(bool nonPublic)`
  - Summary: Gets the remove method
  - Parameters:
    - `bool nonPublic`: true to return any method, false to only return a public method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRemoveMethod(nonPublic: /* bool */);
    ```
- `public DmdMethodInfo[] GetOtherMethods()`
  - Summary: Gets all public 'other' methods
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOtherMethods();
    ```
- `public DmdMethodInfo[] GetOtherMethods(bool nonPublic)`
  - Summary: Gets 'other' methods
  - Parameters:
    - `bool nonPublic`: true to include all methods, false to only include public methods
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 118)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOtherMethods(nonPublic: /* bool */);
    ```
- `public abstract DmdMethodInfo GetAddMethod(DmdGetAccessorOptions options)`
  - Summary: Gets the add method
  - Parameters:
    - `DmdGetAccessorOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAddMethod(options: /* DmdGetAccessorOptions */);
    ```
- `public abstract DmdMethodInfo GetRaiseMethod(DmdGetAccessorOptions options)`
  - Summary: Gets the raise method
  - Parameters:
    - `DmdGetAccessorOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 167)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRaiseMethod(options: /* DmdGetAccessorOptions */);
    ```
- `public abstract DmdMethodInfo GetRemoveMethod(DmdGetAccessorOptions options)`
  - Summary: Gets the remove method
  - Parameters:
    - `DmdGetAccessorOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRemoveMethod(options: /* DmdGetAccessorOptions */);
    ```
- `public abstract DmdMethodInfo[] GetOtherMethods(DmdGetAccessorOptions options)`
  - Summary: Gets 'other' methods
  - Parameters:
    - `DmdGetAccessorOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOtherMethods(options: /* DmdGetAccessorOptions */);
    ```
- `public bool Equals(DmdEventInfo other)`
  - Summary: Equals()
  - Parameters:
    - `DmdEventInfo other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 179)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdEventInfo */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 186)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 192)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public sealed override DmdMemberInfo ResolveMember(bool throwOnError)`
  - Summary: Resolves a member reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(throwOnError: /* bool */);
    ```
- `public sealed override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 198)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdMethodInfo AddMethod => GetAddMethod(nonPublic: true)`
  - Summary: Gets the add method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AddMethod;
    ```
- `public DmdMethodInfo RaiseMethod => GetRaiseMethod(nonPublic: true)`
  - Summary: Gets the raise method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RaiseMethod;
    ```
- `public DmdMethodInfo RemoveMethod => GetRemoveMethod(nonPublic: true)`
  - Summary: Gets the remove method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RemoveMethod;
    ```
- `public abstract DmdEventAttributes Attributes { get; }`
  - Summary: Gets the event attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Attributes;
    ```
- `public abstract DmdType EventHandlerType { get; }`
  - Summary: Gets the event handler type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EventHandlerType;
    ```
- `public bool IsMulticast {
			get {
				var multicastDelegate = DeclaringType.Assembly.AppDomain.System_MulticastDelegate;
				return multicastDelegate.IsAssignableFrom(EventHandlerType);
			}
		}`
  - Summary: true if it's a multi-cast delegate
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMulticast;
    ```
- `public bool IsRTSpecialName => (Attributes & DmdEventAttributes.RTSpecialName) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRTSpecialName;
    ```
- `public bool IsSpecialName => (Attributes & DmdEventAttributes.SpecialName) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSpecialName;
    ```
- `public sealed override DmdAppDomain AppDomain => DeclaringType.AppDomain`
  - Summary: Gets the AppDomain
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public sealed override DmdMemberTypes MemberType => DmdMemberTypes.Event`
  - Summary: Gets the member type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberType;
    ```
- `public sealed override bool IsMetadataReference => false`
  - Summary: Returns false since there are no event references
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMetadataReference;
    ```

### Operators

- `public static bool operator !=(DmdEventInfo left, DmdEventInfo right) => !DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 171)
- `public static bool operator ==(DmdEventInfo left, DmdEventInfo right) => DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdEventInfo.cs` (line 170)

## Class `DmdExceptionHandlingClause`

Exception clause

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdExceptionHandlingClause(flags: /* DmdExceptionHandlingClauseOptions */, tryOffset: /* int */, tryLength: /* int */, handlerOffset: /* int */, handlerLength: /* int */, filterOffset: /* int */, catchType: /* DmdType */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 130)

### Constructors

- `public DmdExceptionHandlingClause(DmdExceptionHandlingClauseOptions flags, int tryOffset, int tryLength, int handlerOffset, int handlerLength, int filterOffset, DmdType catchType)`
  - Summary: Constructor
  - Parameters:
    - `DmdExceptionHandlingClauseOptions flags`: Flags
    - `int tryOffset`: Try offset
    - `int tryLength`: Try length
    - `int handlerOffset`: Handler offset
    - `int handlerLength`: Handler length
    - `int filterOffset`: Filter offset
    - `DmdType catchType`: Catch type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 190)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 204)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdExceptionHandlingClauseOptions Flags { get; }`
  - Summary: Gets the clause kind
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public DmdType CatchType {
			get {
				if (Flags != DmdExceptionHandlingClauseOptions.Clause)
					throw new InvalidOperationException();
				return catchType;
			}
		}`
  - Summary: Catch type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 171)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CatchType;
    ```
- `public int FilterOffset {
			get {
				if (Flags != DmdExceptionHandlingClauseOptions.Filter)
					throw new InvalidOperationException();
				return filterOffset;
			}
		}`
  - Summary: Filter offset
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 159)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FilterOffset;
    ```
- `public int HandlerLength { get; }`
  - Summary: Handler length
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 154)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HandlerLength;
    ```
- `public int HandlerOffset { get; }`
  - Summary: Handler offset
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 149)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HandlerOffset;
    ```
- `public int TryLength { get; }`
  - Summary: Try length
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 144)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TryLength;
    ```
- `public int TryOffset { get; }`
  - Summary: Try offset
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 139)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TryOffset;
    ```

## Enum `DmdExceptionHandlingClauseOptions`

Exception clause kind

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdExceptionHandlingClauseOptions and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdExceptionHandlingClauseOptions(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 117)

### Members

- `Clause`
- `Filter`
- `Finally`
- `Fault`

## Enum `DmdFieldAttributes`

Field attributes

**Inherits/Implements:** `ushort`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdFieldAttributes and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdFieldAttributes(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldAttributes.cs` (line 26)

### Members

- `FieldAccessMask` = `x0007`
- `PrivateScope` = `x0000`
- `Private` = `x0001`
- `FamANDAssem` = `x0002`
- `Assembly` = `x0003`
- `Family` = `x0004`
- `FamORAssem` = `x0005`
- `Public` = `x0006`
- `Static` = `x0010`
- `InitOnly` = `x0020`
- `Literal` = `x0040`
- `NotSerialized` = `x0080`
- `SpecialName` = `x0200`
- `PinvokeImpl` = `x2000`
- `RTSpecialName` = `x0400`
- `HasFieldMarshal` = `x1000`
- `HasDefault` = `x8000`
- `HasFieldRVA` = `x0100`

## Class `DmdFieldInfo`

A .NET field

**Inherits/Implements:** `DmdMemberInfo`, `IEquatable<DmdFieldInfo>`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdFieldInfo and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdFieldInfo(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 27)

### Methods

- `public DmdFieldInfo Resolve()`
  - Summary: Resolves a field reference and throws if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve();
    ```
- `public DmdFieldInfo ResolveNoThrow()`
  - Summary: Resolves a field reference and returns null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveNoThrow();
    ```
- `public DmdType[] GetOptionalCustomModifiers()`
  - Summary: Gets all optional custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptionalCustomModifiers();
    ```
- `public DmdType[] GetRequiredCustomModifiers()`
  - Summary: Gets all required custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 103)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRequiredCustomModifiers();
    ```
- `public ReadOnlyCollection<DmdCustomModifier> GetCustomModifiers()`
  - Summary: Gets all custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCustomModifiers();
    ```
- `public abstract DmdFieldInfo Resolve(bool throwOnError)`
  - Summary: Resolves a field reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve(throwOnError: /* bool */);
    ```
- `public abstract object GetRawConstantValue()`
  - Summary: Gets the constant value stored in metadata if any exists
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 121)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRawConstantValue();
    ```
- `public abstract object GetValue(object context, object obj)`
  - Summary: Gets the current value
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 129)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValue(context: /* object */, obj: /* object */);
    ```
- `public abstract void SetValue(object context, object obj, object value, DmdBindingFlags invokeAttr)`
  - Summary: Sets a new value
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static field
    - `object value`: New value
    - `DmdBindingFlags invokeAttr`: Binding attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 138)
  - Example:
    ```csharp
    // Example invocation
    instance.SetValue(context: /* object */, obj: /* object */, value: /* object */, invokeAttr: /* DmdBindingFlags */);
    ```
- `public bool Equals(DmdFieldInfo other)`
  - Summary: Equals()
  - Parameters:
    - `DmdFieldInfo other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 158)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdFieldInfo */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 165)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 171)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public sealed override DmdMemberInfo ResolveMember(bool throwOnError)`
  - Summary: Resolves a field reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(throwOnError: /* bool */);
    ```
- `public sealed override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 177)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public void SetValue(object context, object obj, object value)`
  - Summary: Sets a new value
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static field
    - `object value`: New value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.SetValue(context: /* object */, obj: /* object */, value: /* object */);
    ```

### Properties

- `public abstract DmdFieldAttributes Attributes { get; }`
  - Summary: Gets the field attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Attributes;
    ```
- `public abstract DmdType FieldType { get; }`
  - Summary: Gets the field type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FieldType;
    ```
- `public abstract uint FieldRVA { get; }`
  - Summary: Gets the RVA of the data if is true
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FieldRVA;
    ```
- `public bool HasDefault => (Attributes & DmdFieldAttributes.HasDefault) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasDefault;
    ```
- `public bool HasFieldMarshal => (Attributes & DmdFieldAttributes.HasFieldMarshal) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasFieldMarshal;
    ```
- `public bool HasFieldRVA => (Attributes & DmdFieldAttributes.HasFieldRVA) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasFieldRVA;
    ```
- `public bool IsAssembly => (Attributes & DmdFieldAttributes.FieldAccessMask) == DmdFieldAttributes.Assembly`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAssembly;
    ```
- `public bool IsFamily => (Attributes & DmdFieldAttributes.FieldAccessMask) == DmdFieldAttributes.Family`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFamily;
    ```
- `public bool IsFamilyAndAssembly => (Attributes & DmdFieldAttributes.FieldAccessMask) == DmdFieldAttributes.FamANDAssem`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFamilyAndAssembly;
    ```
- `public bool IsFamilyOrAssembly => (Attributes & DmdFieldAttributes.FieldAccessMask) == DmdFieldAttributes.FamORAssem`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFamilyOrAssembly;
    ```
- `public bool IsInitOnly => (Attributes & DmdFieldAttributes.InitOnly) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInitOnly;
    ```
- `public bool IsLiteral => (Attributes & DmdFieldAttributes.Literal) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsLiteral;
    ```
- `public bool IsNotSerialized => (Attributes & DmdFieldAttributes.NotSerialized) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNotSerialized;
    ```
- `public bool IsPinvokeImpl => (Attributes & DmdFieldAttributes.PinvokeImpl) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPinvokeImpl;
    ```
- `public bool IsPrivate => (Attributes & DmdFieldAttributes.FieldAccessMask) == DmdFieldAttributes.Private`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPrivate;
    ```
- `public bool IsPrivateScope => (Attributes & DmdFieldAttributes.FieldAccessMask) == DmdFieldAttributes.PrivateScope`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPrivateScope;
    ```
- `public bool IsPublic => (Attributes & DmdFieldAttributes.FieldAccessMask) == DmdFieldAttributes.Public`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPublic;
    ```
- `public bool IsRTSpecialName => (Attributes & DmdFieldAttributes.RTSpecialName) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRTSpecialName;
    ```
- `public bool IsSpecialName => (Attributes & DmdFieldAttributes.SpecialName) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSpecialName;
    ```
- `public bool IsStatic => (Attributes & DmdFieldAttributes.Static) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsStatic;
    ```
- `public override DmdAppDomain AppDomain => DeclaringType.AppDomain`
  - Summary: Gets the AppDomain
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public sealed override DmdMemberTypes MemberType => DmdMemberTypes.Field`
  - Summary: Gets the member type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberType;
    ```

### Operators

- `public static bool operator !=(DmdFieldInfo left, DmdFieldInfo right) => !DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 150)
- `public static bool operator ==(DmdFieldInfo left, DmdFieldInfo right) => DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdFieldInfo.cs` (line 149)

## Enum `DmdGenericParameterAttributes`

Generic parameter attributes

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdGenericParameterAttributes and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdGenericParameterAttributes(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdGenericParameterAttributes.cs` (line 26)

### Members

- `None`
- `VarianceMask` = `x00000003`
- `Covariant` = `x00000001`
- `Contravariant` = `x00000002`
- `SpecialConstraintMask` = `x0000001C`
- `ReferenceTypeConstraint` = `x00000004`
- `NotNullableValueTypeConstraint` = `x00000008`
- `DefaultConstructorConstraint` = `x00000010`

## Enum `DmdGetAccessorOptions`

Get property/event accessor options

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdGetAccessorOptions and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdGetAccessorOptions(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdGetAccessorOptions.cs` (line 24)

### Members

- `None`: No bit is set
- `NonPublic` = `x00000001`: Return non-public accessors (doesn't include private accessors in base classes)
- `All` = `x00000002`: Return all accessors, even if they're in a base class and private

## Enum `DmdGetTypeOptions`

Options used when finding a type

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdGetTypeOptions and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdGetTypeOptions(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 645)

### Members

- `None`: No bit is set
- `ThrowOnError` = `x00000001`: Throw if the type couldn't be found
- `IgnoreCase` = `x00000002`: Ignore case

## Enum `DmdImageFileMachine`

Machine

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdImageFileMachine and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdImageFileMachine(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdImageFileMachine.cs` (line 24)

### Members

- `Unknown`
- `I386` = `x014C`
- `R3000` = `x0162`
- `R4000` = `x0166`
- `R10000` = `x0168`
- `WCEMIPSV2` = `x0169`
- `ALPHA` = `x0184`
- `SH3` = `x01A2`
- `SH3DSP` = `x01A3`
- `SH3E` = `x01A4`
- `SH4` = `x01A6`
- `SH5` = `x01A8`
- `ARM` = `x01C0`
- `THUMB` = `x01C2`
- `ARMNT` = `x01C4`
- `AM33` = `x01D3`
- `POWERPC` = `x01F0`
- `POWERPCFP` = `x01F1`
- `IA64` = `x0200`
- `MIPS16` = `x0266`
- `ALPHA64` = `x0284`
- `MIPSFPU` = `x0366`
- `MIPSFPU16` = `x0466`
- `TRICORE` = `x0520`
- `CEF` = `x0CEF`
- `EBC` = `x0EBC`
- `AMD64` = `x8664`
- `M32R` = `x9041`
- `ARM64` = `xAA64`
- `CEE` = `xC0EE`

## Class `DmdLazyMetadataBytes`

Base class of all classes that contain metadata

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdLazyMetadataBytes and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdLazyMetadataBytes(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 26)

## Class `DmdLazyMetadataBytesArray`

Metadata in a array

**Inherits/Implements:** `DmdLazyMetadataBytes`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdLazyMetadataBytesArray(bytes: /* byte[] */, isFileLayout: /* bool */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 32)

### Constructors

- `public DmdLazyMetadataBytesArray(byte[] bytes, bool isFileLayout)`
  - Summary: Constructor
  - Parameters:
    - `byte[] bytes`: Raw PE file bytes
    - `bool isFileLayout`: true if file layout, false if memory layout
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 48)

### Properties

- `public bool IsFileLayout { get; }`
  - Summary: true if file layout, false if memory layout
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFileLayout;
    ```
- `public byte[] Bytes { get; }`
  - Summary: Gets the raw PE file bytes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Bytes;
    ```

## Class `DmdLazyMetadataBytesCom`

COM IMetaDataImport metadata

**Inherits/Implements:** `DmdLazyMetadataBytes`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdLazyMetadataBytesCom(comMetadata: /* object */, dynamicModuleHelper: /* DmdDynamicModuleHelper */, dispatcher: /* DmdDispatcher */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 118)

### Constructors

- `public DmdLazyMetadataBytesCom(object comMetadata, DmdDynamicModuleHelper dynamicModuleHelper, DmdDispatcher dispatcher)`
  - Summary: Constructor
  - Parameters:
    - `object comMetadata`: COM IMetaDataImport instance
    - `DmdDynamicModuleHelper dynamicModuleHelper`: Helper class
    - `DmdDispatcher dispatcher`: Dispatcher to use when accessing
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 142)

### Properties

- `public DmdDispatcher Dispatcher { get; }`
  - Summary: Gets the dispatcher to use when accessing
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Dispatcher;
    ```
- `public DmdDynamicModuleHelper DynamicModuleHelper { get; }`
  - Summary: Gets the helper class
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 134)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DynamicModuleHelper;
    ```
- `public object ComMetadata => MetaDataImport`
  - Summary: Gets the COM IMetaDataImport instance
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 122)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ComMetadata;
    ```

## Class `DmdLazyMetadataBytesFile`

Metadata in a file

**Inherits/Implements:** `DmdLazyMetadataBytes`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdLazyMetadataBytesFile(filename: /* string */, isFileLayout: /* bool */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 57)

### Constructors

- `public DmdLazyMetadataBytesFile(string filename, bool isFileLayout = true)`
  - Summary: Constructor
  - Parameters:
    - `string filename`: Filename
    - `bool isFileLayout` (default: `true`): true if file layout, false if memory layout
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 73)

### Properties

- `public bool IsFileLayout { get; }`
  - Summary: true if file layout, false if memory layout
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFileLayout;
    ```
- `public string Filename { get; }`
  - Summary: Gets the filename
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```

## Class `DmdLazyMetadataBytesPtr`

Metadata in memory

**Inherits/Implements:** `DmdLazyMetadataBytes`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdLazyMetadataBytesPtr(address: /* IntPtr */, size: /* uint */, isFileLayout: /* bool */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 82)

### Constructors

- `public DmdLazyMetadataBytesPtr(IntPtr address, uint size, bool isFileLayout)`
  - Summary: Constructor
  - Parameters:
    - `IntPtr address`: Address of the PE file
    - `uint size`: Size of the PE file
    - `bool isFileLayout`: true if file layout, false if memory layout
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 104)

### Properties

- `public IntPtr Address { get; }`
  - Summary: Gets the address of the PE file
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```
- `public bool IsFileLayout { get; }`
  - Summary: true if file layout, false if memory layout
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFileLayout;
    ```
- `public uint Size { get; }`
  - Summary: Gets the size of the PE file
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdLazyMetadataBytes.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Size;
    ```

## Class `DmdLocalVariableInfo`

Local variable info

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdLocalVariableInfo(localType: /* DmdType */, localIndex: /* int */, isPinned: /* bool */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 73)

### Constructors

- `public DmdLocalVariableInfo(DmdType localType, int localIndex, bool isPinned)`
  - Summary: Constructor
  - Parameters:
    - `DmdType localType`: Type of the local
    - `int localIndex`: Index of local
    - `bool isPinned`: True if it's a pinned local
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 95)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 107)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdType LocalType { get; }`
  - Summary: Gets the type of the local
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LocalType;
    ```
- `public bool IsPinned { get; }`
  - Summary: true if it's a pinned local
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPinned;
    ```
- `public int LocalIndex { get; }`
  - Summary: Index of the local in the locals signature
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LocalIndex;
    ```

## Enum `DmdMakeTypeOptions`

Options used when creating types

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdMakeTypeOptions and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdMakeTypeOptions(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdAppDomain.cs` (line 629)

### Members

- `None`: No bit is set
- `NoResolve` = `x00000001`: Don't try to resolve a reference

## Class `DmdMemberInfo`

Base class of all types, fields, methods, constructors, properties, events

**Inherits/Implements:** `DmdObject`, `IDmdCustomAttributeProvider`, `IDmdSecurityAttributeProvider`, `IEquatable<DmdMemberInfo>`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdMemberInfo and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdMemberInfo(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 28)

### Methods

- `private protected abstract void YouCantDeriveFromThisClass()`
  - Summary: Dummy abstract method to make sure no-one outside this assembly can create their own
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.YouCantDeriveFromThisClass();
    ```
- `public DmdMemberInfo ResolveMember()`
  - Summary: Resolves a member reference and throws if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember();
    ```
- `public DmdMemberInfo ResolveMemberNoThrow()`
  - Summary: Resolves a member reference and returns null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMemberNoThrow();
    ```
- `public abstract DmdMemberInfo ResolveMember(bool throwOnError)`
  - Summary: Resolves a member reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(throwOnError: /* bool */);
    ```
- `public abstract ReadOnlyCollection<DmdCustomAttributeData> GetCustomAttributesData()`
  - Summary: Gets the custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 124)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCustomAttributesData();
    ```
- `public abstract override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 191)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public abstract override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 197)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public abstract override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 203)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public bool Equals(DmdMemberInfo other)`
  - Summary: Equals()
  - Parameters:
    - `DmdMemberInfo other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 184)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdMemberInfo */);
    ```
- `public bool HasSameMetadataDefinitionAs(DmdMemberInfo other)`
  - Summary: Checks if this instance and have the same metadata definition
  - Parameters:
    - `DmdMemberInfo other`: Other member
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    instance.HasSameMetadataDefinitionAs(other: /* DmdMemberInfo */);
    ```
- `public virtual DmdCustomAttributeData FindCustomAttribute(DmdType attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 164)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public virtual DmdCustomAttributeData FindCustomAttribute(Type attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `Type attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 172)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* Type */, inherit: /* bool */);
    ```
- `public virtual DmdCustomAttributeData FindCustomAttribute(string attributeTypeFullName, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 156)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `public virtual ReadOnlyCollection<DmdCustomAttributeData> GetSecurityAttributesData()`
  - Summary: Gets the security attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSecurityAttributesData();
    ```
- `public virtual bool IsDefined(DmdType attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public virtual bool IsDefined(Type attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `Type attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 148)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* Type */, inherit: /* bool */);
    ```
- `public virtual bool IsDefined(string attributeTypeFullName, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```

### Properties

- `public ReadOnlyCollection<DmdCustomAttributeData> CustomAttributes => GetCustomAttributesData()`
  - Summary: Gets the custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 118)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CustomAttributes;
    ```
- `public ReadOnlyCollection<DmdCustomAttributeData> SecurityAttributes => GetSecurityAttributesData()`
  - Summary: Gets the security attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SecurityAttributes;
    ```
- `public abstract DmdAppDomain AppDomain { get; }`
  - Summary: Gets the AppDomain
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public abstract DmdMemberTypes MemberType { get; }`
  - Summary: Gets the member type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberType;
    ```
- `public abstract DmdModule Module { get; }`
  - Summary: Gets the module
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public abstract DmdType DeclaringType { get; }`
  - Summary: Gets the declaring type. This is the type that declares the member, see also
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DeclaringType;
    ```
- `public abstract DmdType ReflectedType { get; }`
  - Summary: Gets the reflected type. This is the type that owns this member, see also
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReflectedType;
    ```
- `public abstract bool IsMetadataReference { get; }`
  - Summary: true if it's a reference to another type or member, eg. a TypeRef, MemberRef
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMetadataReference;
    ```
- `public abstract int MetadataToken { get; }`
  - Summary: Gets the metadata token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataToken;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the member name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

### Operators

- `public static bool operator !=(DmdMemberInfo left, DmdMemberInfo right) => !(left is DmdType ? DmdMemberInfoEqualityComparer.DefaultType.Equals(left, right) : DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right));`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 176)
- `public static bool operator ==(DmdMemberInfo left, DmdMemberInfo right) => left is DmdType ? DmdMemberInfoEqualityComparer.DefaultType.Equals(left, right) : DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfo.cs` (line 175)

## Class `DmdMemberInfoEqualityComparer`

Compares types, members, parameters

**Inherits/Implements:** `IEqualityComparer<DmdMemberInfo>`, `IEqualityComparer<DmdType>`, `IEqualityComparer<DmdFieldInfo>`, `IEqualityComparer<DmdMethodBase>`, `IEqualityComparer<DmdConstructorInfo>`, `IEqualityComparer<DmdMethodInfo>`, `IEqualityComparer<DmdPropertyInfo>`, `IEqualityComparer<DmdEventInfo>`, `IEqualityComparer<DmdParameterInfo>`, `IEqualityComparer<DmdMethodSignature>`, `IEqualityComparer<IDmdAssemblyName>`, `IEqualityComparer<DmdCustomModifier>`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdMemberInfoEqualityComparer(options: /* DmdSigComparerOptions */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 26)

### Constructors

- `public DmdMemberInfoEqualityComparer(DmdSigComparerOptions options)`
  - Summary: Constructor
  - Parameters:
    - `DmdSigComparerOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 74)

### Methods

- `public bool Equals(DmdConstructorInfo x, DmdConstructorInfo y)`
  - Parameters:
    - `DmdConstructorInfo x`: Description not provided.
    - `DmdConstructorInfo y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdConstructorInfo */, y: /* DmdConstructorInfo */);
    ```
- `public bool Equals(DmdCustomModifier x, DmdCustomModifier y)`
  - Parameters:
    - `DmdCustomModifier x`: Description not provided.
    - `DmdCustomModifier y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdCustomModifier */, y: /* DmdCustomModifier */);
    ```
- `public bool Equals(DmdEventInfo x, DmdEventInfo y)`
  - Parameters:
    - `DmdEventInfo x`: Description not provided.
    - `DmdEventInfo y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdEventInfo */, y: /* DmdEventInfo */);
    ```
- `public bool Equals(DmdFieldInfo x, DmdFieldInfo y)`
  - Parameters:
    - `DmdFieldInfo x`: Description not provided.
    - `DmdFieldInfo y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdFieldInfo */, y: /* DmdFieldInfo */);
    ```
- `public bool Equals(DmdMemberInfo x, DmdMemberInfo y)`
  - Parameters:
    - `DmdMemberInfo x`: Description not provided.
    - `DmdMemberInfo y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdMemberInfo */, y: /* DmdMemberInfo */);
    ```
- `public bool Equals(DmdMethodBase x, DmdMethodBase y)`
  - Parameters:
    - `DmdMethodBase x`: Description not provided.
    - `DmdMethodBase y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdMethodBase */, y: /* DmdMethodBase */);
    ```
- `public bool Equals(DmdMethodInfo x, DmdMethodInfo y)`
  - Parameters:
    - `DmdMethodInfo x`: Description not provided.
    - `DmdMethodInfo y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdMethodInfo */, y: /* DmdMethodInfo */);
    ```
- `public bool Equals(DmdMethodSignature x, DmdMethodSignature y)`
  - Parameters:
    - `DmdMethodSignature x`: Description not provided.
    - `DmdMethodSignature y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdMethodSignature */, y: /* DmdMethodSignature */);
    ```
- `public bool Equals(DmdParameterInfo x, DmdParameterInfo y)`
  - Parameters:
    - `DmdParameterInfo x`: Description not provided.
    - `DmdParameterInfo y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdParameterInfo */, y: /* DmdParameterInfo */);
    ```
- `public bool Equals(DmdPropertyInfo x, DmdPropertyInfo y)`
  - Parameters:
    - `DmdPropertyInfo x`: Description not provided.
    - `DmdPropertyInfo y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdPropertyInfo */, y: /* DmdPropertyInfo */);
    ```
- `public bool Equals(DmdType x, DmdType y)`
  - Parameters:
    - `DmdType x`: Description not provided.
    - `DmdType y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdType */, y: /* DmdType */);
    ```
- `public bool Equals(IDmdAssemblyName x, IDmdAssemblyName y)`
  - Parameters:
    - `IDmdAssemblyName x`: Description not provided.
    - `IDmdAssemblyName y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* IDmdAssemblyName */, y: /* IDmdAssemblyName */);
    ```
- `public int GetHashCode(DmdConstructorInfo obj)`
  - Parameters:
    - `DmdConstructorInfo obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdConstructorInfo */);
    ```
- `public int GetHashCode(DmdCustomModifier obj)`
  - Parameters:
    - `DmdCustomModifier obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdCustomModifier */);
    ```
- `public int GetHashCode(DmdEventInfo obj)`
  - Parameters:
    - `DmdEventInfo obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 92)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdEventInfo */);
    ```
- `public int GetHashCode(DmdFieldInfo obj)`
  - Parameters:
    - `DmdFieldInfo obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdFieldInfo */);
    ```
- `public int GetHashCode(DmdMemberInfo obj)`
  - Parameters:
    - `DmdMemberInfo obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdMemberInfo */);
    ```
- `public int GetHashCode(DmdMethodBase obj)`
  - Parameters:
    - `DmdMethodBase obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdMethodBase */);
    ```
- `public int GetHashCode(DmdMethodInfo obj)`
  - Parameters:
    - `DmdMethodInfo obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdMethodInfo */);
    ```
- `public int GetHashCode(DmdMethodSignature obj)`
  - Parameters:
    - `DmdMethodSignature obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdMethodSignature */);
    ```
- `public int GetHashCode(DmdParameterInfo obj)`
  - Parameters:
    - `DmdParameterInfo obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdParameterInfo */);
    ```
- `public int GetHashCode(DmdPropertyInfo obj)`
  - Parameters:
    - `DmdPropertyInfo obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdPropertyInfo */);
    ```
- `public int GetHashCode(DmdType obj)`
  - Parameters:
    - `DmdType obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdType */);
    ```
- `public int GetHashCode(IDmdAssemblyName obj)`
  - Parameters:
    - `IDmdAssemblyName obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 98)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* IDmdAssemblyName */);
    ```

### Properties

- `public DmdSigComparerOptions Options => options`
  - Summary: Gets the options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```

### Fields

- `public const DmdSigComparerOptions DefaultTypeOptions = DmdSigComparerOptions.CompareDeclaringType | DmdSigComparerOptions.IgnoreMultiDimensionalArrayLowerBoundsAndSizes`
  - Summary: Gets the default options used by
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 61)
  - Example:
    ```csharp
    var value = instance.DefaultTypeOptions;
    ```
- `public static readonly DmdMemberInfoEqualityComparer DefaultMember = new DmdMemberInfoEqualityComparer(DmdSigComparerOptions.CompareDeclaringType | DmdSigComparerOptions.CompareCustomModifiers | DmdSigComparerOptions.CheckTypeEquivalence)`
  - Summary: Should be used when comparing member signatures or when comparing types in member signatures. Custom modifiers are compared and types are checked for equivalence.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 41)
  - Example:
    ```csharp
    var value = dnSpy.Debugger.DotNet.Metadata.DmdMemberInfoEqualityComparer.DefaultMember;
    ```
- `public static readonly DmdMemberInfoEqualityComparer DefaultParameter = new DmdMemberInfoEqualityComparer(DefaultTypeOptions)`
  - Summary: Should be used when comparing parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Debugger.DotNet.Metadata.DmdMemberInfoEqualityComparer.DefaultParameter;
    ```
- `public static readonly DmdMemberInfoEqualityComparer DefaultType = new DmdMemberInfoEqualityComparer(DefaultTypeOptions)`
  - Summary: Should be used when comparing types that aren't part of a member signature. Custom modifiers and MD arrays' lower bounds and sizes are ignored.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberInfoEqualityComparer.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Debugger.DotNet.Metadata.DmdMemberInfoEqualityComparer.DefaultType;
    ```

## Enum `DmdMemberTypes`

Member types

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdMemberTypes and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdMemberTypes(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMemberTypes.cs` (line 26)

### Members

- `Constructor` = `x00000001`
- `Event` = `x00000002`
- `Field` = `x00000004`
- `Method` = `x00000008`
- `Property` = `x00000010`
- `TypeInfo` = `x00000020`
- `Custom` = `x00000040`
- `NestedType` = `x00000080`
- `All` = `onstructor | Event | Field | Method | Property | TypeInfo | Custom | NestedType`

## Enum `DmdMethodAttributes`

Method attributes

**Inherits/Implements:** `ushort`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdMethodAttributes and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdMethodAttributes(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodAttributes.cs` (line 26)

### Members

- `MemberAccessMask` = `x0007`
- `PrivateScope` = `x0000`
- `Private` = `x0001`
- `FamANDAssem` = `x0002`
- `Assembly` = `x0003`
- `Family` = `x0004`
- `FamORAssem` = `x0005`
- `Public` = `x0006`
- `Static` = `x0010`
- `Final` = `x0020`
- `Virtual` = `x0040`
- `HideBySig` = `x0080`
- `VtableLayoutMask` = `x0100`
- `ReuseSlot` = `x0000`
- `NewSlot` = `x0100`
- `CheckAccessOnOverride` = `x0200`
- `Abstract` = `x0400`
- `SpecialName` = `x0800`
- `PinvokeImpl` = `x2000`
- `UnmanagedExport` = `x0008`
- `RTSpecialName` = `x1000`
- `HasSecurity` = `x4000`
- `RequireSecObject` = `x8000`

## Class `DmdMethodBase`

Base class of .NET methods

**Inherits/Implements:** `DmdMemberInfo`, `IDmdSecurityAttributeProvider`, `IEquatable<DmdMethodBase>`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdMethodBase and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdMethodBase(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 29)

### Methods

- `public DmdMethodBase ResolveMethodBase()`
  - Summary: Resolves a method reference and throws if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 143)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethodBase();
    ```
- `public DmdMethodBase ResolveMethodBaseNoThrow()`
  - Summary: Resolves a method reference and returns null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 149)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethodBaseNoThrow();
    ```
- `public DmdMethodSignature GetMethodSignature(IList<Type> genericMethodArguments)`
  - Summary: Gets the method signature
  - Parameters:
    - `IList<Type> genericMethodArguments`: Generic method arguments
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 194)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethodSignature(genericMethodArguments: /* IList<Type> */);
    ```
- `public abstract DmdMethodBase ResolveMethodBase(bool throwOnError)`
  - Summary: Resolves a method reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 156)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethodBase(throwOnError: /* bool */);
    ```
- `public abstract DmdMethodBody GetMethodBody()`
  - Summary: Gets the method body
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 174)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethodBody();
    ```
- `public abstract DmdMethodSignature GetMethodSignature()`
  - Summary: Gets the method signature
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 180)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethodSignature();
    ```
- `public abstract DmdMethodSignature GetMethodSignature(IList<DmdType> genericMethodArguments)`
  - Summary: Gets the method signature
  - Parameters:
    - `IList<DmdType> genericMethodArguments`: Generic method arguments
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethodSignature(genericMethodArguments: /* IList<DmdType> */);
    ```
- `public abstract ReadOnlyCollection<DmdParameterInfo> GetParameters()`
  - Summary: Gets all parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 162)
  - Example:
    ```csharp
    // Example invocation
    instance.GetParameters();
    ```
- `public abstract ReadOnlyCollection<DmdType> GetGenericArguments()`
  - Summary: Gets all generic arguments if it's a generic method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 168)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGenericArguments();
    ```
- `public abstract object Invoke(object context, object obj, DmdBindingFlags invokeAttr, object[] parameters)`
  - Summary: Calls the method
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static method
    - `DmdBindingFlags invokeAttr`: Binding flags
    - `object[] parameters`: Parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 219)
  - Example:
    ```csharp
    // Example invocation
    instance.Invoke(context: /* object */, obj: /* object */, invokeAttr: /* DmdBindingFlags */, parameters: /* object[] */);
    ```
- `public abstract override ReadOnlyCollection<DmdCustomAttributeData> GetSecurityAttributesData()`
  - Summary: Gets the security attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 200)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSecurityAttributesData();
    ```
- `public abstract override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 238)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public abstract override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 244)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public bool Equals(DmdMethodBase other)`
  - Summary: Equals()
  - Parameters:
    - `DmdMethodBase other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 231)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdMethodBase */);
    ```
- `public object Invoke(object context, object obj, object[] parameters)`
  - Summary: Calls the method
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static method
    - `object[] parameters`: Parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 209)
  - Example:
    ```csharp
    // Example invocation
    instance.Invoke(context: /* object */, obj: /* object */, parameters: /* object[] */);
    ```
- `public sealed override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 250)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdCallingConventions CallingConvention {
			get {
				// See SignatureNative::SetCallingConvention() in coreclr/src/vm/runtimehandles.h
				var sig = GetMethodSignature();
				DmdCallingConventions res = 0;
				if ((sig.Flags & DmdSignatureCallingConvention.Mask) == DmdSignatureCallingConvention.VarArg)
					res |= DmdCallingConventions.VarArgs;
				else
					res |= DmdCallingConventions.Standard;
				if (sig.HasThis)
					res |= DmdCallingConventions.HasThis;
				if (sig.ExplicitThis)
					res |= DmdCallingConventions.ExplicitThis;
				return res;
			}
		}`
  - Summary: Gets the calling convention flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CallingConvention;
    ```
- `public abstract DmdMethodAttributes Attributes { get; }`
  - Summary: Gets the method attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Attributes;
    ```
- `public abstract DmdMethodImplAttributes MethodImplementationFlags { get; }`
  - Summary: Gets the method impl flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MethodImplementationFlags;
    ```
- `public abstract bool ContainsGenericParameters { get; }`
  - Summary: true if it contains generic parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContainsGenericParameters;
    ```
- `public abstract bool IsGenericMethod { get; }`
  - Summary: true if it's a generic method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsGenericMethod;
    ```
- `public abstract bool IsGenericMethodDefinition { get; }`
  - Summary: true if it's a generic method definition
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsGenericMethodDefinition;
    ```
- `public abstract uint RVA { get; }`
  - Summary: Gets the RVA of the method body or native code or 0 if none
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 132)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RVA;
    ```
- `public bool CheckAccessOnOverride => (Attributes & DmdMethodAttributes.CheckAccessOnOverride) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 117)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CheckAccessOnOverride;
    ```
- `public bool HasSecurity => (Attributes & DmdMethodAttributes.HasSecurity) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 123)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasSecurity;
    ```
- `public bool IsAbstract => (Attributes & DmdMethodAttributes.Abstract) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 118)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAbstract;
    ```
- `public bool IsAggressiveInlining => (MethodImplementationFlags & DmdMethodImplAttributes.AggressiveInlining) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAggressiveInlining;
    ```
- `public bool IsAggressiveOptimization => (MethodImplementationFlags & DmdMethodImplAttributes.AggressiveOptimization) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 104)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAggressiveOptimization;
    ```
- `public bool IsAssembly => (Attributes & DmdMethodAttributes.MemberAccessMask) == DmdMethodAttributes.Assembly`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 109)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAssembly;
    ```
- `public bool IsConstructedGenericMethod => IsGenericMethod && !IsGenericMethodDefinition`
  - Summary: true if it's a constructed generic method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsConstructedGenericMethod;
    ```
- `public bool IsConstructor => this is DmdConstructorInfo && !IsStatic`
  - Summary: true if this is an instance constructor
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 137)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsConstructor;
    ```
- `public bool IsFamily => (Attributes & DmdMethodAttributes.MemberAccessMask) == DmdMethodAttributes.Family`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 108)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFamily;
    ```
- `public bool IsFamilyAndAssembly => (Attributes & DmdMethodAttributes.MemberAccessMask) == DmdMethodAttributes.FamANDAssem`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 110)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFamilyAndAssembly;
    ```
- `public bool IsFamilyOrAssembly => (Attributes & DmdMethodAttributes.MemberAccessMask) == DmdMethodAttributes.FamORAssem`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFamilyOrAssembly;
    ```
- `public bool IsFinal => (Attributes & DmdMethodAttributes.Final) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 114)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFinal;
    ```
- `public bool IsForwardRef => (MethodImplementationFlags & DmdMethodImplAttributes.ForwardRef) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsForwardRef;
    ```
- `public bool IsHideBySig => (Attributes & DmdMethodAttributes.HideBySig) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsHideBySig;
    ```
- `public bool IsIL => (MethodImplementationFlags & DmdMethodImplAttributes.CodeTypeMask) == DmdMethodImplAttributes.IL`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsIL;
    ```
- `public bool IsInternalCall => (MethodImplementationFlags & DmdMethodImplAttributes.InternalCall) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 99)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInternalCall;
    ```
- `public bool IsManaged => (MethodImplementationFlags & DmdMethodImplAttributes.ManagedMask) == DmdMethodImplAttributes.Managed`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsManaged;
    ```
- `public bool IsNative => (MethodImplementationFlags & DmdMethodImplAttributes.CodeTypeMask) == DmdMethodImplAttributes.Native`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNative;
    ```
- `public bool IsNewSlot => (Attributes & DmdMethodAttributes.VtableLayoutMask) == DmdMethodAttributes.NewSlot`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 126)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNewSlot;
    ```
- `public bool IsNoInlining => (MethodImplementationFlags & DmdMethodImplAttributes.NoInlining) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNoInlining;
    ```
- `public bool IsNoOptimization => (MethodImplementationFlags & DmdMethodImplAttributes.NoOptimization) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 103)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNoOptimization;
    ```
- `public bool IsOPTIL => (MethodImplementationFlags & DmdMethodImplAttributes.CodeTypeMask) == DmdMethodImplAttributes.OPTIL`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOPTIL;
    ```
- `public bool IsPinvokeImpl => (Attributes & DmdMethodAttributes.PinvokeImpl) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 120)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPinvokeImpl;
    ```
- `public bool IsPreserveSig => (MethodImplementationFlags & DmdMethodImplAttributes.PreserveSig) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 98)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPreserveSig;
    ```
- `public bool IsPrivate => (Attributes & DmdMethodAttributes.MemberAccessMask) == DmdMethodAttributes.Private`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPrivate;
    ```
- `public bool IsPrivateScope => (Attributes & DmdMethodAttributes.MemberAccessMask) == DmdMethodAttributes.PrivateScope`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 112)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPrivateScope;
    ```
- `public bool IsPublic => (Attributes & DmdMethodAttributes.MemberAccessMask) == DmdMethodAttributes.Public`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPublic;
    ```
- `public bool IsRTSpecialName => (Attributes & DmdMethodAttributes.RTSpecialName) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 122)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRTSpecialName;
    ```
- `public bool IsReuseSlot => (Attributes & DmdMethodAttributes.VtableLayoutMask) == DmdMethodAttributes.ReuseSlot`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 125)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsReuseSlot;
    ```
- `public bool IsRuntime => (MethodImplementationFlags & DmdMethodImplAttributes.CodeTypeMask) == DmdMethodImplAttributes.Runtime`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 94)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRuntime;
    ```
- `public bool IsSpecialName => (Attributes & DmdMethodAttributes.SpecialName) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 119)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSpecialName;
    ```
- `public bool IsStatic => (Attributes & DmdMethodAttributes.Static) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 113)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsStatic;
    ```
- `public bool IsSynchronized => (MethodImplementationFlags & DmdMethodImplAttributes.Synchronized) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 100)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSynchronized;
    ```
- `public bool IsUnmanaged => (MethodImplementationFlags & DmdMethodImplAttributes.ManagedMask) == DmdMethodImplAttributes.Unmanaged`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 95)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsUnmanaged;
    ```
- `public bool IsUnmanagedExport => (Attributes & DmdMethodAttributes.UnmanagedExport) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 121)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsUnmanagedExport;
    ```
- `public bool IsVirtual => (Attributes & DmdMethodAttributes.Virtual) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 115)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsVirtual;
    ```
- `public bool RequireSecObject => (Attributes & DmdMethodAttributes.RequireSecObject) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 124)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RequireSecObject;
    ```
- `public override DmdAppDomain AppDomain => DeclaringType.AppDomain`
  - Summary: Gets the AppDomain
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public virtual DmdSpecialMethodKind SpecialMethodKind => DmdSpecialMethodKind.Metadata`
  - Summary: Gets the method kind
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SpecialMethodKind;
    ```

### Operators

- `public static bool operator !=(DmdMethodBase left, DmdMethodBase right) => !DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 223)
- `public static bool operator ==(DmdMethodBase left, DmdMethodBase right) => DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 222)

## Class `DmdMethodBody`

.NET method body

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdMethodBody and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdMethodBody(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 27)

### Methods

- `public abstract byte[] GetILAsByteArray()`
  - Summary: Gets the IL bytes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.GetILAsByteArray();
    ```

### Properties

- `public abstract ReadOnlyCollection<DmdExceptionHandlingClause> ExceptionHandlingClauses { get; }`
  - Summary: Gets the exception clauses
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExceptionHandlingClauses;
    ```
- `public abstract ReadOnlyCollection<DmdLocalVariableInfo> LocalVariables { get; }`
  - Summary: Gets all locals
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LocalVariables;
    ```
- `public abstract ReadOnlyCollection<DmdType> GenericMethodArguments { get; }`
  - Summary: Gets the generic method arguments that were used to create this method body
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericMethodArguments;
    ```
- `public abstract ReadOnlyCollection<DmdType> GenericTypeArguments { get; }`
  - Summary: Gets the generic type arguments that were used to create this method body
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericTypeArguments;
    ```
- `public abstract bool InitLocals { get; }`
  - Summary: true if locals are automatically initialized
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InitLocals;
    ```
- `public abstract int LocalSignatureMetadataToken { get; }`
  - Summary: Gets the token of the locals signature
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LocalSignatureMetadataToken;
    ```
- `public abstract int MaxStackSize { get; }`
  - Summary: Gets max stack size
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBody.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MaxStackSize;
    ```

## Enum `DmdMethodImplAttributes`

Method implementation attributes

**Inherits/Implements:** `ushort`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdMethodImplAttributes and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdMethodImplAttributes(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodImplAttributes.cs` (line 26)

### Members

- `CodeTypeMask` = `x0003`
- `IL` = `x0000`
- `Native` = `x0001`
- `OPTIL` = `x0002`
- `Runtime` = `x0003`
- `ManagedMask` = `x0004`
- `Unmanaged` = `x0004`
- `Managed` = `x0000`
- `ForwardRef` = `x0010`
- `PreserveSig` = `x0080`
- `InternalCall` = `x1000`
- `Synchronized` = `x0020`
- `NoInlining` = `x0008`
- `AggressiveInlining` = `x0100`
- `NoOptimization` = `x0040`
- `AggressiveOptimization` = `x0200`

## Class `DmdMethodInfo`

A .NET method

**Inherits/Implements:** `DmdMethodBase`, `IEquatable<DmdMethodInfo>`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdMethodInfo and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdMethodInfo(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 30)

### Methods

- `public DmdMethodInfo GetBaseDefinition()`
  - Summary: Gets the base method definition or itself if it doesn't override a method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 105)
  - Example:
    ```csharp
    // Example invocation
    instance.GetBaseDefinition();
    ```
- `public DmdMethodInfo MakeGenericMethod(IList<Type> typeArguments)`
  - Summary: Creates a generic method
  - Parameters:
    - `IList<Type> typeArguments`: Generic arguments
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 167)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericMethod(typeArguments: /* IList<Type> */);
    ```
- `public DmdMethodInfo MakeGenericMethod(params DmdType[] typeArguments)`
  - Summary: Creates a generic method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericMethod();
    ```
- `public DmdMethodInfo MakeGenericMethod(params Type[] typeArguments)`
  - Summary: Creates a generic method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericMethod();
    ```
- `public DmdMethodInfo Resolve()`
  - Summary: Resolves a method reference and throws if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve();
    ```
- `public DmdMethodInfo ResolveNoThrow()`
  - Summary: Resolves a method reference and returns null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 60)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveNoThrow();
    ```
- `public abstract DmdMethodInfo GetGenericMethodDefinition()`
  - Summary: Gets the generic method definition
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGenericMethodDefinition();
    ```
- `public abstract DmdMethodInfo MakeGenericMethod(IList<DmdType> typeArguments)`
  - Summary: Creates a generic method
  - Parameters:
    - `IList<DmdType> typeArguments`: Generic arguments
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 160)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericMethod(typeArguments: /* IList<DmdType> */);
    ```
- `public abstract DmdMethodInfo Resolve(bool throwOnError)`
  - Summary: Resolves a method reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve(throwOnError: /* bool */);
    ```
- `public abstract override ReadOnlyCollection<DmdType> GetGenericArguments()`
  - Summary: Gets all generic arguments if it's a generic method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGenericArguments();
    ```
- `public bool Equals(DmdMethodInfo other)`
  - Summary: Equals()
  - Parameters:
    - `DmdMethodInfo other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 211)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdMethodInfo */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 218)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 224)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public sealed override DmdCustomAttributeData FindCustomAttribute(DmdType attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public sealed override DmdCustomAttributeData FindCustomAttribute(string attributeTypeFullName, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 191)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `public sealed override DmdMemberInfo ResolveMember(bool throwOnError)`
  - Summary: Resolves a member reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(throwOnError: /* bool */);
    ```
- `public sealed override DmdMethodBase ResolveMethodBase(bool throwOnError)`
  - Summary: Resolves a method reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethodBase(throwOnError: /* bool */);
    ```
- `public sealed override bool IsDefined(DmdType attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 183)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public sealed override bool IsDefined(string attributeTypeFullName, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```

### Properties

- `public IDmdCustomAttributeProvider ReturnTypeCustomAttributes => ReturnParameter`
  - Summary: Gets the return type's custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReturnTypeCustomAttributes;
    ```
- `public abstract DmdParameterInfo ReturnParameter { get; }`
  - Summary: Gets the return parameter
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReturnParameter;
    ```
- `public abstract DmdType ReturnType { get; }`
  - Summary: Gets the return type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReturnType;
    ```
- `public override bool ContainsGenericParameters {
			get {
				if (DeclaringType.ContainsGenericParameters)
					return true;
				if (!IsGenericMethod)
					return false;
				foreach (var genArg in GetGenericArguments()) {
					if (genArg.ContainsGenericParameters)
						return true;
				}
				return false;
			}
		}`
  - Summary: true if it contains generic parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContainsGenericParameters;
    ```
- `public sealed override DmdMemberTypes MemberType => DmdMemberTypes.Method`
  - Summary: Gets the member type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberType;
    ```

### Operators

- `public static bool operator !=(DmdMethodInfo left, DmdMethodInfo right) => !DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 203)
- `public static bool operator ==(DmdMethodInfo left, DmdMethodInfo right) => DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodInfo.cs` (line 202)

## Class `DmdMethodSignature`

.NET method signature

**Inherits/Implements:** `IEquatable<DmdMethodSignature>`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdMethodSignature(flags: /* DmdSignatureCallingConvention */, genericParameterCount: /* int */, returnType: /* DmdType */, parameterTypes: /* IList<DmdType> */, varArgsParameterTypes: /* IList<DmdType> */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 28)

### Constructors

- `public DmdMethodSignature(DmdSignatureCallingConvention flags, int genericParameterCount, DmdType returnType, IList<DmdType> parameterTypes, IList<DmdType> varArgsParameterTypes)`
  - Summary: Constructor
  - Parameters:
    - `DmdSignatureCallingConvention flags`: Flags
    - `int genericParameterCount`: Number of generic parameters
    - `DmdType returnType`: Return type
    - `IList<DmdType> parameterTypes`: Parameter types or null
    - `IList<DmdType> varArgsParameterTypes`: Var args parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 88)

### Methods

- `public ReadOnlyCollection<DmdType> GetParameterTypes()`
  - Summary: Gets the parameter types, see also
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.GetParameterTypes();
    ```
- `public ReadOnlyCollection<DmdType> GetVarArgsParameterTypes()`
  - Summary: Gets the var args parameter types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    instance.GetVarArgsParameterTypes();
    ```
- `public bool Equals(DmdMethodSignature other)`
  - Summary: Equals()
  - Parameters:
    - `DmdMethodSignature other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 120)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdMethodSignature */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 127)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public sealed override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdSignatureCallingConvention Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public DmdType ReturnType { get; }`
  - Summary: Gets the return type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReturnType;
    ```
- `public bool ExplicitThis => (Flags & DmdSignatureCallingConvention.ExplicitThis) != 0`
  - Summary: true if 'this' is an explicit parameter
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExplicitThis;
    ```
- `public bool HasThis => (Flags & DmdSignatureCallingConvention.HasThis) != 0`
  - Summary: true if 'this' is a hidden parameter
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasThis;
    ```
- `public bool IsGeneric => (Flags & DmdSignatureCallingConvention.Generic) != 0`
  - Summary: true if it's a generic method signature
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsGeneric;
    ```
- `public int GenericParameterCount { get; }`
  - Summary: Generic parameter count
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericParameterCount;
    ```

### Operators

- `public static bool operator !=(DmdMethodSignature left, DmdMethodSignature right) => !DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 112)
- `public static bool operator ==(DmdMethodSignature left, DmdMethodSignature right) => DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodSignature.cs` (line 111)

## Class `DmdModule`

A .NET module

**Inherits/Implements:** `DmdObject`, `IDmdCustomAttributeProvider`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdModule and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdModule(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 30)

### Methods

- `private protected abstract void YouCantDeriveFromThisClass()`
  - Summary: Dummy abstract method to make sure no-one outside this assembly can create their own
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.YouCantDeriveFromThisClass();
    ```
- `public DmdCustomAttributeData FindCustomAttribute(DmdType attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 197)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public DmdCustomAttributeData FindCustomAttribute(Type attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `Type attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 205)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* Type */, inherit: /* bool */);
    ```
- `public DmdCustomAttributeData FindCustomAttribute(string attributeTypeFullName, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 189)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `public DmdFieldInfo GetField(string name)`
  - Summary: Gets a global public static or instance field
  - Parameters:
    - `string name`: Field name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 577)
  - Example:
    ```csharp
    // Example invocation
    instance.GetField(name: /* string */);
    ```
- `public DmdFieldInfo GetField(string name, DmdBindingFlags bindingAttr)`
  - Summary: Gets a global field
  - Parameters:
    - `string name`: Field name
    - `DmdBindingFlags bindingAttr`: Binding attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 585)
  - Example:
    ```csharp
    // Example invocation
    instance.GetField(name: /* string */, bindingAttr: /* DmdBindingFlags */);
    ```
- `public DmdFieldInfo ResolveField(int metadataToken)`
  - Summary: Resolves a field
  - Parameters:
    - `int metadataToken`: Token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 268)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveField(metadataToken: /* int */);
    ```
- `public DmdFieldInfo ResolveField(int metadataToken, DmdResolveOptions options)`
  - Summary: Resolves a field
  - Parameters:
    - `int metadataToken`: Token
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 276)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveField(metadataToken: /* int */, options: /* DmdResolveOptions */);
    ```
- `public DmdFieldInfo ResolveField(int metadataToken, IList<DmdType> genericTypeArguments, IList<DmdType> genericMethodArguments)`
  - Summary: Resolves a field
  - Parameters:
    - `int metadataToken`: Token
    - `IList<DmdType> genericTypeArguments`: Generic type arguments or null
    - `IList<DmdType> genericMethodArguments`: Generic method arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 285)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveField(metadataToken: /* int */, genericTypeArguments: /* IList<DmdType> */, genericMethodArguments: /* IList<DmdType> */);
    ```
- `public DmdFieldInfo ResolveField(int metadataToken, IList<Type> genericTypeArguments, IList<Type> genericMethodArguments)`
  - Summary: Resolves a field
  - Parameters:
    - `int metadataToken`: Token
    - `IList<Type> genericTypeArguments`: Generic type arguments or null
    - `IList<Type> genericMethodArguments`: Generic method arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 295)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveField(metadataToken: /* int */, genericTypeArguments: /* IList<Type> */, genericMethodArguments: /* IList<Type> */);
    ```
- `public DmdFieldInfo ResolveField(int metadataToken, IList<Type> genericTypeArguments, IList<Type> genericMethodArguments, DmdResolveOptions options)`
  - Summary: Resolves a field
  - Parameters:
    - `int metadataToken`: Token
    - `IList<Type> genericTypeArguments`: Generic type arguments or null
    - `IList<Type> genericMethodArguments`: Generic method arguments or null
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 316)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveField(metadataToken: /* int */, genericTypeArguments: /* IList<Type> */, genericMethodArguments: /* IList<Type> */, options: /* DmdResolveOptions */);
    ```
- `public DmdFieldInfo[] GetFields()`
  - Summary: Gets all global public static and instance fields
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 563)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFields();
    ```
- `public DmdFieldInfo[] GetFields(DmdBindingFlags bindingFlags)`
  - Summary: Gets all global fields
  - Parameters:
    - `DmdBindingFlags bindingFlags`: Binding attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 570)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFields(bindingFlags: /* DmdBindingFlags */);
    ```
- `public DmdMemberInfo ResolveMember(int metadataToken)`
  - Summary: Resolves a member
  - Parameters:
    - `int metadataToken`: Token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 380)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(metadataToken: /* int */);
    ```
- `public DmdMemberInfo ResolveMember(int metadataToken, DmdResolveOptions options)`
  - Summary: Resolves a member
  - Parameters:
    - `int metadataToken`: Token
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 388)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(metadataToken: /* int */, options: /* DmdResolveOptions */);
    ```
- `public DmdMemberInfo ResolveMember(int metadataToken, IList<DmdType> genericTypeArguments, IList<DmdType> genericMethodArguments)`
  - Summary: Resolves a member
  - Parameters:
    - `int metadataToken`: Token
    - `IList<DmdType> genericTypeArguments`: Generic type arguments or null
    - `IList<DmdType> genericMethodArguments`: Generic method arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 397)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(metadataToken: /* int */, genericTypeArguments: /* IList<DmdType> */, genericMethodArguments: /* IList<DmdType> */);
    ```
- `public DmdMemberInfo ResolveMember(int metadataToken, IList<Type> genericTypeArguments, IList<Type> genericMethodArguments)`
  - Summary: Resolves a member
  - Parameters:
    - `int metadataToken`: Token
    - `IList<Type> genericTypeArguments`: Generic type arguments or null
    - `IList<Type> genericMethodArguments`: Generic method arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 407)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(metadataToken: /* int */, genericTypeArguments: /* IList<Type> */, genericMethodArguments: /* IList<Type> */);
    ```
- `public DmdMemberInfo ResolveMember(int metadataToken, IList<Type> genericTypeArguments, IList<Type> genericMethodArguments, DmdResolveOptions options)`
  - Summary: Resolves a member
  - Parameters:
    - `int metadataToken`: Token
    - `IList<Type> genericTypeArguments`: Generic type arguments or null
    - `IList<Type> genericMethodArguments`: Generic method arguments or null
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 428)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(metadataToken: /* int */, genericTypeArguments: /* IList<Type> */, genericMethodArguments: /* IList<Type> */, options: /* DmdResolveOptions */);
    ```
- `public DmdMethodBase ResolveMethod(int metadataToken)`
  - Summary: Resolves a method
  - Parameters:
    - `int metadataToken`: Token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 212)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethod(metadataToken: /* int */);
    ```
- `public DmdMethodBase ResolveMethod(int metadataToken, DmdResolveOptions options)`
  - Summary: Resolves a method
  - Parameters:
    - `int metadataToken`: Token
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 220)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethod(metadataToken: /* int */, options: /* DmdResolveOptions */);
    ```
- `public DmdMethodBase ResolveMethod(int metadataToken, IList<DmdType> genericTypeArguments, IList<DmdType> genericMethodArguments)`
  - Summary: Resolves a method
  - Parameters:
    - `int metadataToken`: Token
    - `IList<DmdType> genericTypeArguments`: Generic type arguments or null
    - `IList<DmdType> genericMethodArguments`: Generic method arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 229)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethod(metadataToken: /* int */, genericTypeArguments: /* IList<DmdType> */, genericMethodArguments: /* IList<DmdType> */);
    ```
- `public DmdMethodBase ResolveMethod(int metadataToken, IList<Type> genericTypeArguments, IList<Type> genericMethodArguments)`
  - Summary: Resolves a method
  - Parameters:
    - `int metadataToken`: Token
    - `IList<Type> genericTypeArguments`: Generic type arguments or null
    - `IList<Type> genericMethodArguments`: Generic method arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 239)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethod(metadataToken: /* int */, genericTypeArguments: /* IList<Type> */, genericMethodArguments: /* IList<Type> */);
    ```
- `public DmdMethodBase ResolveMethod(int metadataToken, IList<Type> genericTypeArguments, IList<Type> genericMethodArguments, DmdResolveOptions options)`
  - Summary: Resolves a method
  - Parameters:
    - `int metadataToken`: Token
    - `IList<Type> genericTypeArguments`: Generic type arguments or null
    - `IList<Type> genericMethodArguments`: Generic method arguments or null
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 260)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethod(metadataToken: /* int */, genericTypeArguments: /* IList<Type> */, genericMethodArguments: /* IList<Type> */, options: /* DmdResolveOptions */);
    ```
- `public DmdMethodInfo GetMethod(string name)`
  - Summary: Gets a global public static or instance method
  - Parameters:
    - `string name`: Method name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 646)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */);
    ```
- `public DmdMethodInfo GetMethod(string name, DmdBindingFlags bindingAttr, DmdCallingConventions callConvention, IList<DmdType> types)`
  - Summary: Gets a global method
  - Parameters:
    - `string name`: Method name
    - `DmdBindingFlags bindingAttr`: Binding attributes
    - `DmdCallingConventions callConvention`: Calling convention
    - `IList<DmdType> types`: Method parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 608)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, bindingAttr: /* DmdBindingFlags */, callConvention: /* DmdCallingConventions */, types: /* IList<DmdType> */);
    ```
- `public DmdMethodInfo GetMethod(string name, DmdBindingFlags bindingAttr, DmdCallingConventions callConvention, IList<Type> types)`
  - Summary: Gets a global method
  - Parameters:
    - `string name`: Method name
    - `DmdBindingFlags bindingAttr`: Binding attributes
    - `DmdCallingConventions callConvention`: Calling convention
    - `IList<Type> types`: Method parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 622)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, bindingAttr: /* DmdBindingFlags */, callConvention: /* DmdCallingConventions */, types: /* IList<Type> */);
    ```
- `public DmdMethodInfo GetMethod(string name, IList<DmdType> types)`
  - Summary: Gets a global public static or instance method
  - Parameters:
    - `string name`: Method name
    - `IList<DmdType> types`: Method parameter types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 631)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, types: /* IList<DmdType> */);
    ```
- `public DmdMethodInfo GetMethod(string name, IList<Type> types)`
  - Summary: Gets a global public static or instance method
  - Parameters:
    - `string name`: Method name
    - `IList<Type> types`: Method parameter types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 639)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, types: /* IList<Type> */);
    ```
- `public DmdMethodInfo[] GetMethods()`
  - Summary: Gets all global public static or instance methods
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 591)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethods();
    ```
- `public DmdMethodInfo[] GetMethods(DmdBindingFlags bindingFlags)`
  - Summary: Gets global methods
  - Parameters:
    - `DmdBindingFlags bindingFlags`: Binding attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 598)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethods(bindingFlags: /* DmdBindingFlags */);
    ```
- `public DmdMethodSignature ResolveMethodSignature(int metadataToken, IList<DmdType> genericTypeArguments, IList<DmdType> genericMethodArguments)`
  - Summary: Resolves a method signature
  - Parameters:
    - `int metadataToken`: StandaloneSig token from a method body
    - `IList<DmdType> genericTypeArguments`: Generic type arguments or null
    - `IList<DmdType> genericMethodArguments`: Generic method arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 438)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethodSignature(metadataToken: /* int */, genericTypeArguments: /* IList<DmdType> */, genericMethodArguments: /* IList<DmdType> */);
    ```
- `public DmdMethodSignature ResolveMethodSignature(int metadataToken, IList<Type> genericTypeArguments, IList<Type> genericMethodArguments)`
  - Summary: Resolves a method signature
  - Parameters:
    - `int metadataToken`: StandaloneSig token from a method body
    - `IList<Type> genericTypeArguments`: Generic type arguments or null
    - `IList<Type> genericMethodArguments`: Generic method arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 448)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethodSignature(metadataToken: /* int */, genericTypeArguments: /* IList<Type> */, genericMethodArguments: /* IList<Type> */);
    ```
- `public DmdMethodSignature ResolveMethodSignature(int metadataToken, IList<Type> genericTypeArguments, IList<Type> genericMethodArguments, DmdResolveOptions options)`
  - Summary: Resolves a method signature
  - Parameters:
    - `int metadataToken`: StandaloneSig token from a method body
    - `IList<Type> genericTypeArguments`: Generic type arguments or null
    - `IList<Type> genericMethodArguments`: Generic method arguments or null
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 469)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethodSignature(metadataToken: /* int */, genericTypeArguments: /* IList<Type> */, genericMethodArguments: /* IList<Type> */, options: /* DmdResolveOptions */);
    ```
- `public DmdType GetType(Type type)`
  - Summary: Gets a type
  - Parameters:
    - `Type type`: Type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 498)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(type: /* Type */);
    ```
- `public DmdType GetType(Type type, DmdGetTypeOptions options)`
  - Summary: Gets a type
  - Parameters:
    - `Type type`: Type
    - `DmdGetTypeOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 513)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(type: /* Type */, options: /* DmdGetTypeOptions */);
    ```
- `public DmdType GetType(string className)`
  - Summary: Gets a type
  - Parameters:
    - `string className`: Name of type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 532)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(className: /* string */);
    ```
- `public DmdType GetType(string className, bool ignoreCase)`
  - Summary: Gets a type
  - Parameters:
    - `string className`: Name of type
    - `bool ignoreCase`: true to ignore case
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 525)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(className: /* string */, ignoreCase: /* bool */);
    ```
- `public DmdType GetType(string className, bool throwOnError, bool ignoreCase)`
  - Summary: Gets a type
  - Parameters:
    - `string className`: Name of type
    - `bool throwOnError`: true to throw if the type couldn't be found
    - `bool ignoreCase`: true to ignore case
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 548)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(className: /* string */, throwOnError: /* bool */, ignoreCase: /* bool */);
    ```
- `public DmdType GetTypeThrow(Type type)`
  - Summary: Gets a type and throws if it couldn't be found
  - Parameters:
    - `Type type`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 505)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTypeThrow(type: /* Type */);
    ```
- `public DmdType GetTypeThrow(string className)`
  - Summary: Gets a type and throws if it couldn't be found
  - Parameters:
    - `string className`: Name of type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 539)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTypeThrow(className: /* string */);
    ```
- `public DmdType ResolveType(int metadataToken)`
  - Summary: Resolves a type
  - Parameters:
    - `int metadataToken`: Token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 324)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveType(metadataToken: /* int */);
    ```
- `public DmdType ResolveType(int metadataToken, DmdResolveOptions options)`
  - Summary: Resolves a type
  - Parameters:
    - `int metadataToken`: Token
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 332)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveType(metadataToken: /* int */, options: /* DmdResolveOptions */);
    ```
- `public DmdType ResolveType(int metadataToken, IList<DmdType> genericTypeArguments, IList<DmdType> genericMethodArguments)`
  - Summary: Resolves a type
  - Parameters:
    - `int metadataToken`: Token
    - `IList<DmdType> genericTypeArguments`: Generic type arguments or null
    - `IList<DmdType> genericMethodArguments`: Generic method arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 341)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveType(metadataToken: /* int */, genericTypeArguments: /* IList<DmdType> */, genericMethodArguments: /* IList<DmdType> */);
    ```
- `public DmdType ResolveType(int metadataToken, IList<Type> genericTypeArguments, IList<Type> genericMethodArguments)`
  - Summary: Resolves a type
  - Parameters:
    - `int metadataToken`: Token
    - `IList<Type> genericTypeArguments`: Generic type arguments or null
    - `IList<Type> genericMethodArguments`: Generic method arguments or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 351)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveType(metadataToken: /* int */, genericTypeArguments: /* IList<Type> */, genericMethodArguments: /* IList<Type> */);
    ```
- `public DmdType ResolveType(int metadataToken, IList<Type> genericTypeArguments, IList<Type> genericMethodArguments, DmdResolveOptions options)`
  - Summary: Resolves a type
  - Parameters:
    - `int metadataToken`: Token
    - `IList<Type> genericTypeArguments`: Generic type arguments or null
    - `IList<Type> genericMethodArguments`: Generic method arguments or null
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 372)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveType(metadataToken: /* int */, genericTypeArguments: /* IList<Type> */, genericMethodArguments: /* IList<Type> */, options: /* DmdResolveOptions */);
    ```
- `public abstract DmdFieldInfo ResolveField(int metadataToken, IList<DmdType> genericTypeArguments, IList<DmdType> genericMethodArguments, DmdResolveOptions options)`
  - Summary: Resolves a field
  - Parameters:
    - `int metadataToken`: Token
    - `IList<DmdType> genericTypeArguments`: Generic type arguments or null
    - `IList<DmdType> genericMethodArguments`: Generic method arguments or null
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 306)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveField(metadataToken: /* int */, genericTypeArguments: /* IList<DmdType> */, genericMethodArguments: /* IList<DmdType> */, options: /* DmdResolveOptions */);
    ```
- `public abstract DmdMemberInfo ResolveMember(int metadataToken, IList<DmdType> genericTypeArguments, IList<DmdType> genericMethodArguments, DmdResolveOptions options)`
  - Summary: Resolves a member
  - Parameters:
    - `int metadataToken`: Token
    - `IList<DmdType> genericTypeArguments`: Generic type arguments or null
    - `IList<DmdType> genericMethodArguments`: Generic method arguments or null
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 418)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(metadataToken: /* int */, genericTypeArguments: /* IList<DmdType> */, genericMethodArguments: /* IList<DmdType> */, options: /* DmdResolveOptions */);
    ```
- `public abstract DmdMethodBase ResolveMethod(int metadataToken, IList<DmdType> genericTypeArguments, IList<DmdType> genericMethodArguments, DmdResolveOptions options)`
  - Summary: Resolves a method
  - Parameters:
    - `int metadataToken`: Token
    - `IList<DmdType> genericTypeArguments`: Generic type arguments or null
    - `IList<DmdType> genericMethodArguments`: Generic method arguments or null
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 250)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethod(metadataToken: /* int */, genericTypeArguments: /* IList<DmdType> */, genericMethodArguments: /* IList<DmdType> */, options: /* DmdResolveOptions */);
    ```
- `public abstract DmdMethodSignature ResolveMethodSignature(int metadataToken, IList<DmdType> genericTypeArguments, IList<DmdType> genericMethodArguments, DmdResolveOptions options)`
  - Summary: Resolves a method signature
  - Parameters:
    - `int metadataToken`: StandaloneSig token from a method body
    - `IList<DmdType> genericTypeArguments`: Generic type arguments or null
    - `IList<DmdType> genericMethodArguments`: Generic method arguments or null
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 459)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMethodSignature(metadataToken: /* int */, genericTypeArguments: /* IList<DmdType> */, genericMethodArguments: /* IList<DmdType> */, options: /* DmdResolveOptions */);
    ```
- `public abstract DmdReadOnlyAssemblyName[] GetReferencedAssemblies()`
  - Summary: Gets all referenced assemblies
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 652)
  - Example:
    ```csharp
    // Example invocation
    instance.GetReferencedAssemblies();
    ```
- `public abstract DmdType GetType(string typeName, DmdGetTypeOptions options)`
  - Summary: Gets a type
  - Parameters:
    - `string typeName`: Full name of the type ()
    - `DmdGetTypeOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 557)
  - Example:
    ```csharp
    // Example invocation
    instance.GetType(typeName: /* string */, options: /* DmdGetTypeOptions */);
    ```
- `public abstract DmdType ResolveType(int metadataToken, IList<DmdType> genericTypeArguments, IList<DmdType> genericMethodArguments, DmdResolveOptions options)`
  - Summary: Resolves a type
  - Parameters:
    - `int metadataToken`: Token
    - `IList<DmdType> genericTypeArguments`: Generic type arguments or null
    - `IList<DmdType> genericMethodArguments`: Generic method arguments or null
    - `DmdResolveOptions options`: Resolve options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 362)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveType(metadataToken: /* int */, genericTypeArguments: /* IList<DmdType> */, genericMethodArguments: /* IList<DmdType> */, options: /* DmdResolveOptions */);
    ```
- `public abstract DmdType[] GetExportedTypes()`
  - Summary: Gets all types that exist in the ExportedType table. This includes types that have been forwarded to other assemblies.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.GetExportedTypes();
    ```
- `public abstract DmdType[] GetTypes()`
  - Summary: Gets all types in this module
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 70)
  - Example:
    ```csharp
    // Example invocation
    instance.GetTypes();
    ```
- `public abstract ReadOnlyCollection<DmdCustomAttributeData> GetCustomAttributesData()`
  - Summary: Gets the custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCustomAttributesData();
    ```
- `public abstract byte[] ResolveSignature(int metadataToken)`
  - Summary: Resolves a signature
  - Parameters:
    - `int metadataToken`: Token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 477)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveSignature(metadataToken: /* int */);
    ```
- `public abstract string ResolveString(int metadataToken)`
  - Summary: Resolves a string
  - Parameters:
    - `int metadataToken`: String token (0x70xxxxxx)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 484)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveString(metadataToken: /* int */);
    ```
- `public abstract unsafe bool ReadMemory(uint rva, void* destination, int size)`
  - Summary: Reads memory. Returns false if data couldn't be read.
  - Parameters:
    - `uint rva`: RVA of data
    - `void* destination`: Destination address
    - `int size`: Number of bytes to read
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 661)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadMemory(rva: /* uint */, destination: /* void* */, size: /* int */);
    ```
- `public abstract void GetPEKind(out DmdPortableExecutableKinds peKind, out DmdImageFileMachine machine)`
  - Summary: Gets PE information
  - Parameters:
    - `out DmdPortableExecutableKinds peKind`: PE Kind
    - `out DmdImageFileMachine machine`: Machine
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 491)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPEKind(peKind: /* DmdPortableExecutableKinds */, machine: /* DmdImageFileMachine */);
    ```
- `public bool IsDefined(DmdType attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 173)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public bool IsDefined(Type attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `Type attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* Type */, inherit: /* bool */);
    ```
- `public bool IsDefined(string attributeTypeFullName, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 165)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `public byte[] ReadMemory(uint rva, int size)`
  - Summary: Reads memory. Returns null if data couldn't be read.
  - Parameters:
    - `uint rva`: RVA of data
    - `int size`: Number of bytes to read
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 692)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadMemory(rva: /* uint */, size: /* int */);
    ```
- `public sealed override string ToString()`
  - Summary: Returns the metadata name ()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 705)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static string GetFullyQualifiedName(bool isInMemory, bool isDynamic, string fullyQualifiedName)`
  - Summary: Returns the fully qualified name
  - Parameters:
    - `bool isInMemory`: true if the module is in memory
    - `bool isDynamic`: true if it's a dynamic module
    - `string fullyQualifiedName`: Module filename or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Metadata.DmdModule.GetFullyQualifiedName(isInMemory: /* bool */, isDynamic: /* bool */, fullyQualifiedName: /* string */);
    ```
- `public unsafe bool ReadMemory(uint rva, byte[] destination, int destinationIndex, int size)`
  - Summary: Reads memory. Returns false if data couldn't be read.
  - Parameters:
    - `uint rva`: RVA of data
    - `byte[] destination`: Destination buffer
    - `int destinationIndex`: Destination index
    - `int size`: Number of bytes to read
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 671)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadMemory(rva: /* uint */, destination: /* byte[] */, destinationIndex: /* int */, size: /* int */);
    ```

### Properties

- `public ReadOnlyCollection<DmdCustomAttributeData> CustomAttributes => GetCustomAttributesData()`
  - Summary: Gets the custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 151)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CustomAttributes;
    ```
- `public abstract DmdAppDomain AppDomain { get; }`
  - Summary: Gets the AppDomain
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public abstract DmdAssembly Assembly { get; }`
  - Summary: Gets the assembly
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 131)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Assembly;
    ```
- `public abstract DmdType GlobalType { get; }`
  - Summary: Gets the global type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GlobalType;
    ```
- `public abstract Guid ModuleVersionId { get; }`
  - Summary: Gets the module version ID
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleVersionId;
    ```
- `public abstract bool IsDynamic { get; }`
  - Summary: true if it's a dynamic module (types can be added at runtime)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 136)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDynamic;
    ```
- `public abstract bool IsInMemory { get; }`
  - Summary: true if it's an in-memory module (eg. loaded from a array)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 141)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInMemory;
    ```
- `public abstract bool IsSynthetic { get; }`
  - Summary: true if it's a synthetic module; it's not loaded in the debugged process
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 146)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSynthetic;
    ```
- `public abstract int DynamicModuleVersion { get; }`
  - Summary: Gets a dynamic module's version number. It gets incremented each time a new type gets added to the dynamic module.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DynamicModuleVersion;
    ```
- `public abstract int MDStreamVersion { get; }`
  - Summary: Gets the metadata stream version
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 97)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MDStreamVersion;
    ```
- `public abstract int MetadataToken { get; }`
  - Summary: Gets the metadata token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataToken;
    ```
- `public abstract string FullyQualifiedName { get; }`
  - Summary: Gets the fully qualified name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FullyQualifiedName;
    ```
- `public abstract string ScopeName { get; set; }`
  - Summary: Gets the metadata name of the module
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ScopeName;
    ```
- `public bool IsCorLib => this == AppDomain.CorLib.ManifestModule`
  - Summary: true if this is the corlib module
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 64)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsCorLib;
    ```
- `public string Name {
			get {
				var fqn = FullyQualifiedName;
				// Don't use Path.GetFileName() since fqn could contain invalid characters
				int index = fqn.LastIndexOfAny(dirSepChars);
				if (index >= 0)
					fqn = fqn.Substring(index + 1);
				if (fqn.EndsWith(".ni.dll", StringComparison.OrdinalIgnoreCase))
					fqn = fqn.Substring(0, fqn.Length - ".ni.dll".Length) + fqn.Substring(fqn.Length - ".dll".Length);
				else if (fqn.EndsWith(".ni.exe", StringComparison.OrdinalIgnoreCase))
					fqn = fqn.Substring(0, fqn.Length - ".ni.exe".Length) + fqn.Substring(fqn.Length - ".exe".Length);
				return fqn;
			}
		}`
  - Summary: Gets the module name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 112)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `DmdModuleExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Debugger.DotNet.Metadata.DmdModuleExtensions members directly without instantiation.
dnSpy.Debugger.DotNet.Metadata.DmdModuleExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DmdModuleExtensions.cs` (line 26)

### Methods

- `public static DbgModule GetDebuggerModule(this DmdModule module)`
  - Summary: Gets the debugger module object or returns null if there is none (eg. it's a synthetic module)
  - Parameters:
    - `this DmdModule module`: Debugger metadata module object
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DmdModuleExtensions.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Metadata.DmdModuleExtensions.GetDebuggerModule(module: /* DmdModule */);
    ```

## Class `DmdObject`

Base class of types, members, assemblies, modules that allows you to attach data to instances

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdObject();
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdObject.cs` (line 28)

### Constructors

- `protected DmdObject()`
  - Summary: Constructor
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdObject.cs` (line 40)

### Methods

- `public T GetData<T>() where T : class`
  - Summary: Gets existing data or throws if the data doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdObject.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.GetData();
    ```
- `public T GetOrCreateData<T>() where T : class, new()`
  - Summary: Gets or creates data
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdObject.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateData();
    ```
- `public T GetOrCreateData<T>(Func<T> create) where T : class`
  - Summary: Gets or creates data
  - Parameters:
    - `Func<T> create`: Creates the data if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdObject.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreateData(create: /* Func<T> */);
    ```
- `public bool HasData<T>() where T : class`
  - Summary: Checks if the data exists or is null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdObject.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.HasData();
    ```
- `public bool TryGetData<T>(out T value) where T : class`
  - Summary: Gets data
  - Parameters:
    - `out T value`: Result
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdObject.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetData(value: /* T */);
    ```

### Properties

- `protected object LockObject => lockObj`
  - Summary: Gets the lock object used by this instance
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdObject.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LockObject;
    ```

## Enum `DmdParameterAttributes`

Parameter attributes

**Inherits/Implements:** `ushort`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdParameterAttributes and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdParameterAttributes(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterAttributes.cs` (line 26)

### Members

- `None`
- `In` = `x0001`
- `Out` = `x0002`
- `Lcid` = `x0004`
- `Retval` = `x0008`
- `Optional` = `x0010`
- `HasDefault` = `x1000`
- `HasFieldMarshal` = `x2000`

## Class `DmdParameterInfo`

A .NET method parameter

**Inherits/Implements:** `DmdObject`, `IDmdCustomAttributeProvider`, `IEquatable<DmdParameterInfo>`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdParameterInfo and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdParameterInfo(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 28)

### Methods

- `private protected abstract void YouCantDeriveFromThisClass()`
  - Summary: Dummy abstract method to make sure no-one outside this assembly can create their own
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.YouCantDeriveFromThisClass();
    ```
- `public DmdCustomAttributeData FindCustomAttribute(DmdType attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public DmdCustomAttributeData FindCustomAttribute(Type attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `Type attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 165)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* Type */, inherit: /* bool */);
    ```
- `public DmdCustomAttributeData FindCustomAttribute(string attributeTypeFullName, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 149)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `public DmdType[] GetOptionalCustomModifiers()`
  - Summary: Gets all optional custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 100)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptionalCustomModifiers();
    ```
- `public DmdType[] GetRequiredCustomModifiers()`
  - Summary: Gets all required custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRequiredCustomModifiers();
    ```
- `public ReadOnlyCollection<DmdCustomModifier> GetCustomModifiers()`
  - Summary: Gets all custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCustomModifiers();
    ```
- `public abstract ReadOnlyCollection<DmdCustomAttributeData> GetCustomAttributesData()`
  - Summary: Gets the custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCustomAttributesData();
    ```
- `public bool Equals(DmdParameterInfo other)`
  - Summary: Equals()
  - Parameters:
    - `DmdParameterInfo other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 177)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdParameterInfo */);
    ```
- `public bool IsDefined(DmdType attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 133)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public bool IsDefined(Type attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `Type attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 141)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* Type */, inherit: /* bool */);
    ```
- `public bool IsDefined(string attributeTypeFullName, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 184)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 190)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public sealed override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 196)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public ReadOnlyCollection<DmdCustomAttributeData> CustomAttributes => GetCustomAttributesData()`
  - Summary: Gets the custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CustomAttributes;
    ```
- `public abstract DmdMemberInfo Member { get; }`
  - Summary: Gets the owner method or property
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Member;
    ```
- `public abstract DmdParameterAttributes Attributes { get; }`
  - Summary: Gets the parameter attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Attributes;
    ```
- `public abstract DmdType ParameterType { get; }`
  - Summary: Gets the parameter type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ParameterType;
    ```
- `public abstract bool HasDefaultValue { get; }`
  - Summary: true if is valid
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasDefaultValue;
    ```
- `public abstract int MetadataToken { get; }`
  - Summary: Gets the metadata token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataToken;
    ```
- `public abstract int Position { get; }`
  - Summary: Gets the parameter index
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Position;
    ```
- `public abstract object RawDefaultValue { get; }`
  - Summary: Gets the default value, see also
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RawDefaultValue;
    ```
- `public abstract string Name { get; }`
  - Summary: Gets the parameter name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public bool HasDefault => (Attributes & DmdParameterAttributes.HasDefault) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasDefault;
    ```
- `public bool HasFieldMarshal => (Attributes & DmdParameterAttributes.HasFieldMarshal) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasFieldMarshal;
    ```
- `public bool IsIn => (Attributes & DmdParameterAttributes.In) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsIn;
    ```
- `public bool IsLcid => (Attributes & DmdParameterAttributes.Lcid) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsLcid;
    ```
- `public bool IsMetadataReference => Member.IsMetadataReference`
  - Summary: true if this is not the real method parameter since the declaring method is just a reference. Resolve the method to get the real method parameters.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMetadataReference;
    ```
- `public bool IsOptional => (Attributes & DmdParameterAttributes.Optional) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 69)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOptional;
    ```
- `public bool IsOut => (Attributes & DmdParameterAttributes.Out) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOut;
    ```
- `public bool IsRetval => (Attributes & DmdParameterAttributes.Retval) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRetval;
    ```

### Operators

- `public static bool operator !=(DmdParameterInfo left, DmdParameterInfo right) => !DmdMemberInfoEqualityComparer.DefaultParameter.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 169)
- `public static bool operator ==(DmdParameterInfo left, DmdParameterInfo right) => DmdMemberInfoEqualityComparer.DefaultParameter.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdParameterInfo.cs` (line 168)

## Enum `DmdPortableExecutableKinds`

PE flags

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdPortableExecutableKinds and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdPortableExecutableKinds(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPortableExecutableKinds.cs` (line 26)

### Members

- `NotAPortableExecutableImage`
- `ILOnly` = `x00000001`
- `Required32Bit` = `x00000002`
- `PE32Plus` = `x00000004`
- `Unmanaged32Bit` = `x00000008`
- `Preferred32Bit` = `x00000010`

## Enum `DmdProcessorArchitecture`

Processor architecture

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdProcessorArchitecture and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdProcessorArchitecture(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdProcessorArchitecture.cs` (line 24)

### Members

- `None`
- `MSIL`
- `X86`
- `IA64`
- `Amd64`
- `Arm`

## Enum `DmdPropertyAttributes`

Property attributes

**Inherits/Implements:** `ushort`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdPropertyAttributes and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdPropertyAttributes(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyAttributes.cs` (line 26)

### Members

- `SpecialName` = `x0200`
- `RTSpecialName` = `x0400`
- `HasDefault` = `x1000`

## Class `DmdPropertyInfo`

A .NET property

**Inherits/Implements:** `DmdMemberInfo`, `IEquatable<DmdPropertyInfo>`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdPropertyInfo and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdPropertyInfo(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 27)

### Methods

- `public DmdMethodInfo GetGetMethod()`
  - Summary: Gets the public get method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 168)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGetMethod();
    ```
- `public DmdMethodInfo GetGetMethod(bool nonPublic)`
  - Summary: Gets the get method
  - Parameters:
    - `bool nonPublic`: true to return any get method, false to only return a public get method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGetMethod(nonPublic: /* bool */);
    ```
- `public DmdMethodInfo GetSetMethod()`
  - Summary: Gets the public set method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 174)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSetMethod();
    ```
- `public DmdMethodInfo GetSetMethod(bool nonPublic)`
  - Summary: Gets the set method
  - Parameters:
    - `bool nonPublic`: true to return any set method, false to only return a public set method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSetMethod(nonPublic: /* bool */);
    ```
- `public DmdMethodInfo[] GetAccessors()`
  - Summary: Gets all public accessors
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 152)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAccessors();
    ```
- `public DmdMethodInfo[] GetAccessors(bool nonPublic)`
  - Summary: Gets all accessors
  - Parameters:
    - `bool nonPublic`: true to include all accessors, false to only include public accessors
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAccessors(nonPublic: /* bool */);
    ```
- `public DmdType[] GetOptionalCustomModifiers()`
  - Summary: Gets all optional custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 140)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptionalCustomModifiers();
    ```
- `public DmdType[] GetRequiredCustomModifiers()`
  - Summary: Gets all required custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 134)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRequiredCustomModifiers();
    ```
- `public ReadOnlyCollection<DmdCustomModifier> GetCustomModifiers()`
  - Summary: Gets all custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCustomModifiers();
    ```
- `public abstract DmdMethodInfo GetGetMethod(DmdGetAccessorOptions options)`
  - Summary: Gets the get method
  - Parameters:
    - `DmdGetAccessorOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGetMethod(options: /* DmdGetAccessorOptions */);
    ```
- `public abstract DmdMethodInfo GetSetMethod(DmdGetAccessorOptions options)`
  - Summary: Gets the set method
  - Parameters:
    - `DmdGetAccessorOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 122)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSetMethod(options: /* DmdGetAccessorOptions */);
    ```
- `public abstract DmdMethodInfo[] GetAccessors(DmdGetAccessorOptions options)`
  - Summary: Gets all accessors
  - Parameters:
    - `DmdGetAccessorOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAccessors(options: /* DmdGetAccessorOptions */);
    ```
- `public abstract DmdMethodSignature GetMethodSignature()`
  - Summary: Gets the method signature
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 180)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethodSignature();
    ```
- `public abstract ReadOnlyCollection<DmdParameterInfo> GetIndexParameters()`
  - Summary: Gets the index parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 128)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIndexParameters();
    ```
- `public abstract object GetRawConstantValue()`
  - Summary: Gets the constant stored in metadata
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRawConstantValue();
    ```
- `public bool Equals(DmdPropertyInfo other)`
  - Summary: Equals()
  - Parameters:
    - `DmdPropertyInfo other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 266)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdPropertyInfo */);
    ```
- `public object GetValue(object context, object obj)`
  - Summary: Gets the property value
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static property
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValue(context: /* object */, obj: /* object */);
    ```
- `public object GetValue(object context, object obj, DmdBindingFlags invokeAttr, object[] index)`
  - Summary: Gets the property value
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static property
    - `DmdBindingFlags invokeAttr`: Binding flags
    - `object[] index`: Property indexes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 207)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValue(context: /* object */, obj: /* object */, invokeAttr: /* DmdBindingFlags */, index: /* object[] */);
    ```
- `public object GetValue(object context, object obj, object[] index)`
  - Summary: Gets the property value
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static property
    - `object[] index`: Property indexes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 197)
  - Example:
    ```csharp
    // Example invocation
    instance.GetValue(context: /* object */, obj: /* object */, index: /* object[] */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 273)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 279)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public sealed override DmdMemberInfo ResolveMember(bool throwOnError)`
  - Summary: Resolves a property reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(throwOnError: /* bool */);
    ```
- `public sealed override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 285)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public void SetValue(object context, object obj, object value)`
  - Summary: Writes a new property value
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static property
    - `object value`: New value
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 220)
  - Example:
    ```csharp
    // Example invocation
    instance.SetValue(context: /* object */, obj: /* object */, value: /* object */);
    ```
- `public void SetValue(object context, object obj, object value, DmdBindingFlags invokeAttr, object[] index)`
  - Summary: Writes a new property value
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static property
    - `object value`: New value
    - `DmdBindingFlags invokeAttr`: Binding flags
    - `object[] index`: Property indexes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 239)
  - Example:
    ```csharp
    // Example invocation
    instance.SetValue(context: /* object */, obj: /* object */, value: /* object */, invokeAttr: /* DmdBindingFlags */, index: /* object[] */);
    ```
- `public void SetValue(object context, object obj, object value, object[] index)`
  - Summary: Writes a new property value
  - Parameters:
    - `object context`: Evaluation context
    - `object obj`: Instance or null if it's a static property
    - `object value`: New value
    - `object[] index`: Property indexes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 229)
  - Example:
    ```csharp
    // Example invocation
    instance.SetValue(context: /* object */, obj: /* object */, value: /* object */, index: /* object[] */);
    ```

### Properties

- `public DmdMethodInfo GetMethod => GetGetMethod(nonPublic: true)`
  - Summary: Gets the get method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 157)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GetMethod;
    ```
- `public DmdMethodInfo SetMethod => GetSetMethod(nonPublic: true)`
  - Summary: Gets the set method
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 162)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SetMethod;
    ```
- `public abstract DmdPropertyAttributes Attributes { get; }`
  - Summary: Gets the property attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Attributes;
    ```
- `public abstract DmdType PropertyType { get; }`
  - Summary: Gets the property type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PropertyType;
    ```
- `public bool CanRead => (object)GetMethod != null`
  - Summary: true if the property can be read
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanRead;
    ```
- `public bool CanWrite => (object)SetMethod != null`
  - Summary: true if the property can be written to
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CanWrite;
    ```
- `public bool HasDefault => (Attributes & DmdPropertyAttributes.HasDefault) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasDefault;
    ```
- `public bool IsRTSpecialName => (Attributes & DmdPropertyAttributes.RTSpecialName) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRTSpecialName;
    ```
- `public bool IsSpecialName => (Attributes & DmdPropertyAttributes.SpecialName) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSpecialName;
    ```
- `public sealed override DmdAppDomain AppDomain => DeclaringType.AppDomain`
  - Summary: Gets the AppDomain
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public sealed override DmdMemberTypes MemberType => DmdMemberTypes.Property`
  - Summary: Gets the member type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberType;
    ```
- `public sealed override bool IsMetadataReference => false`
  - Summary: Returns false since there are no property references
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMetadataReference;
    ```

### Operators

- `public static bool operator !=(DmdPropertyInfo left, DmdPropertyInfo right) => !DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 258)
- `public static bool operator ==(DmdPropertyInfo left, DmdPropertyInfo right) => DmdMemberInfoEqualityComparer.DefaultMember.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdPropertyInfo.cs` (line 257)

## Class `DmdReadOnlyAssemblyName`

A read only assembly name

**Inherits/Implements:** `IDmdAssemblyName`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdReadOnlyAssemblyName(assemblyName: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 27)

### Constructors

- `public DmdReadOnlyAssemblyName(IDmdAssemblyName name)`
  - Summary: Constructor
  - Parameters:
    - `IDmdAssemblyName name`: Assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 155)
- `public DmdReadOnlyAssemblyName(string assemblyName)`
  - Summary: Constructor
  - Parameters:
    - `string assemblyName`: Assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 99)
- `public DmdReadOnlyAssemblyName(string name, Version version, string cultureName, DmdAssemblyNameFlags flags, byte[] publicKey, byte[] publicKeyToken, DmdAssemblyHashAlgorithm hashAlgorithm)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Simple name
    - `Version version`: Version
    - `string cultureName`: Culture or null
    - `DmdAssemblyNameFlags flags`: Flags
    - `byte[] publicKey`: Public key or null
    - `byte[] publicKeyToken`: Public key token or null
    - `DmdAssemblyHashAlgorithm hashAlgorithm`: Hash algorithm
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 120)
- `public DmdReadOnlyAssemblyName(string name, Version version, string cultureName, DmdAssemblyNameFlags flags, byte[] publicKeyOrToken, DmdAssemblyHashAlgorithm hashAlgorithm)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Simple name
    - `Version version`: Version
    - `string cultureName`: Culture or null
    - `DmdAssemblyNameFlags flags`: Flags
    - `byte[] publicKeyOrToken`: Public key or public key token or null
    - `DmdAssemblyHashAlgorithm hashAlgorithm`: Hash algorithm
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 139)

### Methods

- `public DmdAssemblyName AsMutable()`
  - Summary: Converts it to a mutable assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 171)
  - Example:
    ```csharp
    // Example invocation
    instance.AsMutable();
    ```
- `public DmdReadOnlyAssemblyName AsReadOnly()`
  - Summary: Creates a read only assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 177)
  - Example:
    ```csharp
    // Example invocation
    instance.AsReadOnly();
    ```
- `public byte[] GetPublicKey()`
  - Summary: Gets the public key
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPublicKey();
    ```
- `public byte[] GetPublicKeyToken()`
  - Summary: Gets the public key token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPublicKeyToken();
    ```
- `public override string ToString()`
  - Summary: Gets the full assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 183)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdAssemblyContentType ContentType => (DmdAssemblyContentType)((int)(RawFlags & DmdAssemblyNameFlags.ContentType_Mask) >> 9)`
  - Summary: Gets the content type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentType;
    ```
- `public DmdAssemblyHashAlgorithm HashAlgorithm { get; }`
  - Summary: Gets the hash algorithm
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 88)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HashAlgorithm;
    ```
- `public DmdAssemblyNameFlags Flags => RawFlags & ~(DmdAssemblyNameFlags.ContentType_Mask | DmdAssemblyNameFlags.PA_FullMask)`
  - Summary: Gets the flags. The content type and processor architecture bits are ignored, use instead
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public DmdAssemblyNameFlags RawFlags { get; }`
  - Summary: Gets the flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RawFlags;
    ```
- `public DmdProcessorArchitecture ProcessorArchitecture => (DmdProcessorArchitecture)((int)(RawFlags & DmdAssemblyNameFlags.PA_Mask) >> 4)`
  - Summary: Gets the processor architecture
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessorArchitecture;
    ```
- `public Version Version { get; }`
  - Summary: Gets the version
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Version;
    ```
- `public string CultureName { get; }`
  - Summary: Gets the culture name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CultureName;
    ```
- `public string FullName => DmdAssemblyNameFormatter.Format(Name, Version, CultureName, GetPublicKeyToken(), RawFlags, isPublicKeyToken: true)`
  - Summary: Gets the full assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FullName;
    ```
- `public string Name { get; }`
  - Summary: Gets the simple name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdReadOnlyAssemblyName.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Enum `DmdResolveOptions`

Type/member resolve options

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdResolveOptions and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdResolveOptions(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdModule.cs` (line 711)

### Members

- `None`: No bit is set
- `ThrowOnError` = `x00000001`: Throw if the type or member couldn't be resolved
- `NoTryResolveRefs` = `x00000002`: Don't try to resolve type refs, field refs, method refs

## Class `DmdRuntime`

A .NET runtime

**Inherits/Implements:** `DmdObject`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdRuntime and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdRuntime(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdRuntime.cs` (line 24)

### Methods

- `private protected abstract void YouCantDeriveFromThisClass()`
  - Summary: Dummy abstract method to make sure no-one outside this assembly can create their own
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdRuntime.cs` (line 28)
  - Example:
    ```csharp
    // Example invocation
    instance.YouCantDeriveFromThisClass();
    ```
- `public abstract DmdAppDomain CreateAppDomain(int id)`
  - Summary: Creates an AppDomain
  - Parameters:
    - `int id`: AppDomain id, must be a unique identifier
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdRuntime.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    instance.CreateAppDomain(id: /* int */);
    ```
- `public abstract DmdAppDomain GetAppDomain(int id)`
  - Summary: Returns an AppDomain or null if it doesn't exist
  - Parameters:
    - `int id`: AppDomain id
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdRuntime.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAppDomain(id: /* int */);
    ```
- `public abstract DmdAppDomain[] GetAppDomains()`
  - Summary: Gets all AppDomains
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdRuntime.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.GetAppDomains();
    ```
- `public abstract void Remove(DmdAppDomain appDomain)`
  - Summary: Removes an AppDomain
  - Parameters:
    - `DmdAppDomain appDomain`: AppDomain to remove
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdRuntime.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.Remove(appDomain: /* DmdAppDomain */);
    ```

### Properties

- `public abstract DmdImageFileMachine Machine { get; }`
  - Summary: Gets the machine
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdRuntime.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Machine;
    ```
- `public abstract int PointerSize { get; }`
  - Summary: Gets the size of a pointer in bytes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdRuntime.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PointerSize;
    ```

## Class `DmdRuntimeExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Debugger.DotNet.Metadata.DmdRuntimeExtensions members directly without instantiation.
dnSpy.Debugger.DotNet.Metadata.DmdRuntimeExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DmdRuntimeExtensions.cs` (line 26)

### Methods

- `public static DbgRuntime GetDebuggerRuntime(this DmdRuntime runtime)`
  - Summary: Gets the debugger runtime object
  - Parameters:
    - `this DmdRuntime runtime`: Debugger metadata runtime object
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger.DotNet/Extensions/DmdRuntimeExtensions.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Metadata.DmdRuntimeExtensions.GetDebuggerRuntime(runtime: /* DmdRuntime */);
    ```

## Class `DmdRuntimeFactory`

Creates runtimes

**Example**

```csharp
// Access dnSpy.Debugger.DotNet.Metadata.DmdRuntimeFactory members directly without instantiation.
dnSpy.Debugger.DotNet.Metadata.DmdRuntimeFactory./* member */
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdRuntimeFactory.cs` (line 27)

### Methods

- `public static DmdRuntime CreateRuntime(DmdEvaluator evaluator, DmdImageFileMachine machine)`
  - Summary: Creates a runtime
  - Parameters:
    - `DmdEvaluator evaluator`: Evaluator
    - `DmdImageFileMachine machine`: Machine
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdRuntimeFactory.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Metadata.DmdRuntimeFactory.CreateRuntime(evaluator: /* DmdEvaluator */, machine: /* DmdImageFileMachine */);
    ```

## Struct `DmdSigComparer`

Compares types and members

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdSigComparer(options: /* DmdSigComparerOptions */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 84)

### Constructors

- `public DmdSigComparer(DmdSigComparerOptions options)`
  - Summary: Constructor
  - Parameters:
    - `DmdSigComparerOptions options`: Options
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 115)

### Methods

- `public bool Equals(DmdCustomModifier a, DmdCustomModifier b)`
  - Summary: Compares two custom modifiers
  - Parameters:
    - `DmdCustomModifier a`: First custom modifier
    - `DmdCustomModifier b`: Second custom modifier
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 400)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* DmdCustomModifier */, b: /* DmdCustomModifier */);
    ```
- `public bool Equals(DmdEventInfo a, DmdEventInfo b)`
  - Summary: Compares two events
  - Parameters:
    - `DmdEventInfo a`: First event
    - `DmdEventInfo b`: Second event
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 321)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* DmdEventInfo */, b: /* DmdEventInfo */);
    ```
- `public bool Equals(DmdFieldInfo a, DmdFieldInfo b)`
  - Summary: Compares two fields
  - Parameters:
    - `DmdFieldInfo a`: First field
    - `DmdFieldInfo b`: Second field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 270)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* DmdFieldInfo */, b: /* DmdFieldInfo */);
    ```
- `public bool Equals(DmdMemberInfo a, DmdMemberInfo b)`
  - Summary: Compares two members
  - Parameters:
    - `DmdMemberInfo a`: First member
    - `DmdMemberInfo b`: Second member
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 148)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* DmdMemberInfo */, b: /* DmdMemberInfo */);
    ```
- `public bool Equals(DmdMethodBase a, DmdMethodBase b)`
  - Summary: Compares two methods or constructors
  - Parameters:
    - `DmdMethodBase a`: First method or constructor
    - `DmdMethodBase b`: Second method or constructor
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 287)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* DmdMethodBase */, b: /* DmdMethodBase */);
    ```
- `public bool Equals(DmdMethodSignature a, DmdMethodSignature b)`
  - Summary: Compares two method signatures
  - Parameters:
    - `DmdMethodSignature a`: First method signature
    - `DmdMethodSignature b`: Second method signature
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 381)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* DmdMethodSignature */, b: /* DmdMethodSignature */);
    ```
- `public bool Equals(DmdParameterInfo a, DmdParameterInfo b)`
  - Summary: Compares two method parameters
  - Parameters:
    - `DmdParameterInfo a`: First method parameter
    - `DmdParameterInfo b`: Second method parameter
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 338)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* DmdParameterInfo */, b: /* DmdParameterInfo */);
    ```
- `public bool Equals(DmdPropertyInfo a, DmdPropertyInfo b)`
  - Summary: Compares two properties
  - Parameters:
    - `DmdPropertyInfo a`: First property
    - `DmdPropertyInfo b`: Second property
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 304)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* DmdPropertyInfo */, b: /* DmdPropertyInfo */);
    ```
- `public bool Equals(DmdType a, DmdType b)`
  - Summary: Compares two types
  - Parameters:
    - `DmdType a`: First type
    - `DmdType b`: Second type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* DmdType */, b: /* DmdType */);
    ```
- `public bool Equals(IDmdAssemblyName a, IDmdAssemblyName b)`
  - Summary: Compares two assembly names
  - Parameters:
    - `IDmdAssemblyName a`: First assembly name
    - `IDmdAssemblyName b`: Second assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 355)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(a: /* IDmdAssemblyName */, b: /* IDmdAssemblyName */);
    ```
- `public int GetHashCode(DmdCustomModifier a)`
  - Summary: Gets the hash code of a custom modifier
  - Parameters:
    - `DmdCustomModifier a`: Custom modifier
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 730)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(a: /* DmdCustomModifier */);
    ```
- `public int GetHashCode(DmdEventInfo a)`
  - Summary: Gets the hash code of an event
  - Parameters:
    - `DmdEventInfo a`: Event
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 670)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(a: /* DmdEventInfo */);
    ```
- `public int GetHashCode(DmdFieldInfo a)`
  - Summary: Gets the hash code of a field
  - Parameters:
    - `DmdFieldInfo a`: Field
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 622)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(a: /* DmdFieldInfo */);
    ```
- `public int GetHashCode(DmdMemberInfo a)`
  - Summary: Gets the hash code of a member
  - Parameters:
    - `DmdMemberInfo a`: Member
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 512)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(a: /* DmdMemberInfo */);
    ```
- `public int GetHashCode(DmdMethodBase a)`
  - Summary: Gets the hash code of a method or constructor
  - Parameters:
    - `DmdMethodBase a`: Method or constructor
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 638)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(a: /* DmdMethodBase */);
    ```
- `public int GetHashCode(DmdMethodSignature a)`
  - Summary: Gets the hash code of a method signature
  - Parameters:
    - `DmdMethodSignature a`: Method signature
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 713)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(a: /* DmdMethodSignature */);
    ```
- `public int GetHashCode(DmdParameterInfo a)`
  - Summary: Gets the hash code of a method parameter
  - Parameters:
    - `DmdParameterInfo a`: Method parameter
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 686)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(a: /* DmdParameterInfo */);
    ```
- `public int GetHashCode(DmdPropertyInfo a)`
  - Summary: Gets the hash code of a property
  - Parameters:
    - `DmdPropertyInfo a`: Property
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 654)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(a: /* DmdPropertyInfo */);
    ```
- `public int GetHashCode(DmdType a)`
  - Summary: Gets the hash code of a type
  - Parameters:
    - `DmdType a`: Type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 544)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(a: /* DmdType */);
    ```
- `public int GetHashCode(IDmdAssemblyName a)`
  - Summary: Gets the hash code of an assembly name
  - Parameters:
    - `IDmdAssemblyName a`: Assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 702)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(a: /* IDmdAssemblyName */);
    ```

## Enum `DmdSigComparerOptions`

Type and member comparer options

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdSigComparerOptions and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdSigComparerOptions(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSigComparer.cs` (line 28)

### Members

- `None`: No bit is set
- `DontCompareTypeScope`: Don't compare type scope (assembly / module)
- `CompareDeclaringType`: Compare declaring type. It's ignored if it's a nested type and only used if it's a field, constructor, method, property, event, parameter
- `DontCompareReturnType`: Don't compare return types
- `CaseInsensitiveMemberNames`: Case insensitive member names
- `ProjectWinMDReferences` = `x10`: Project WinMD references
- `CheckTypeEquivalence` = `x20`: Check type equivalence
- `CompareCustomModifiers` = `x40`: Compare optional and required C modifiers
- `CompareGenericParameterDeclaringMember` = `x80`: Compare generic type/method parameter's declaring member
- `IgnoreMultiDimensionalArrayLowerBoundsAndSizes` = `x100`: When comparing types, don't compare a multi-dimensional array's lower bounds and sizes

## Enum `DmdSignatureCallingConvention`

Signature calling convention flags

**Inherits/Implements:** `byte`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdSignatureCallingConvention and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdSignatureCallingConvention(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdSignatureCallingConvention.cs` (line 26)

### Members

- `Default` = `x00`
- `C` = `x01`
- `StdCall` = `x02`
- `ThisCall` = `x03`
- `FastCall` = `x04`
- `VarArg` = `x05`
- `Field` = `x06`
- `LocalSig` = `x07`
- `Property` = `x08`
- `Unmanaged` = `x09`
- `GenericInst` = `x0A`
- `NativeVarArg` = `x0B`
- `Mask` = `x0F`
- `Generic` = `x10`
- `HasThis` = `x20`
- `ExplicitThis` = `x40`

## Enum `DmdSpecialMethodKind`

Special methods created by the CLR

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdSpecialMethodKind and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdSpecialMethodKind(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdMethodBase.cs` (line 256)

### Members

- `Metadata`: It was read from metadata
- `Array_Set`: SZArray/MDArray Set method: void Set(int, ..., ElementType)
- `Array_Address`: SZArray/MDArray Address method: ElementType& Address(int, ...)
- `Array_Get`: SZArray/MDArray Get method: ElementType Get(int, ...)
- `Array_Constructor1`: SZArray/MDArray constructor that takes args specifying the sizes of all dimensions. Lower bound is assumed to be zero.
- `Array_Constructor2`: MDArray constructor that takes args in pairs, one per dimension. The first is the lower bound for the dimension and the following is the size.

## Class `DmdType`

A .NET type

**Inherits/Implements:** `DmdMemberInfo`, `IEquatable<DmdType>`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdType and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdType(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 31)

### Methods

- `public DmdConstructorInfo GetConstructor(DmdBindingFlags bindingAttr, DmdCallingConventions callConvention, IList<Type> types)`
  - Summary: Gets a constructor
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Binding flags
    - `DmdCallingConventions callConvention`: Calling convention
    - `IList<Type> types`: Parameter types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 632)
  - Example:
    ```csharp
    // Example invocation
    instance.GetConstructor(bindingAttr: /* DmdBindingFlags */, callConvention: /* DmdCallingConventions */, types: /* IList<Type> */);
    ```
- `public DmdConstructorInfo GetConstructor(DmdBindingFlags bindingAttr, IList<DmdType> types)`
  - Summary: Gets a constructor
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Binding flags
    - `IList<DmdType> types`: Parameter types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 641)
  - Example:
    ```csharp
    // Example invocation
    instance.GetConstructor(bindingAttr: /* DmdBindingFlags */, types: /* IList<DmdType> */);
    ```
- `public DmdConstructorInfo GetConstructor(DmdBindingFlags bindingAttr, IList<Type> types)`
  - Summary: Gets a constructor
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Binding flags
    - `IList<Type> types`: Parameter types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 649)
  - Example:
    ```csharp
    // Example invocation
    instance.GetConstructor(bindingAttr: /* DmdBindingFlags */, types: /* IList<Type> */);
    ```
- `public DmdConstructorInfo GetConstructor(IList<DmdType> types)`
  - Summary: Gets a public constructor
  - Parameters:
    - `IList<DmdType> types`: Parameter types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 656)
  - Example:
    ```csharp
    // Example invocation
    instance.GetConstructor(types: /* IList<DmdType> */);
    ```
- `public DmdConstructorInfo GetConstructor(IList<Type> types)`
  - Summary: Gets a public constructor
  - Parameters:
    - `IList<Type> types`: Parameter types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 663)
  - Example:
    ```csharp
    // Example invocation
    instance.GetConstructor(types: /* IList<Type> */);
    ```
- `public DmdConstructorInfo[] GetConstructors()`
  - Summary: Gets all public constructors
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 669)
  - Example:
    ```csharp
    // Example invocation
    instance.GetConstructors();
    ```
- `public DmdEventInfo GetEvent(DmdModule module, int metadataToken)`
  - Summary: Gets an event or returns null if it doesn't exist
  - Parameters:
    - `DmdModule module`: Module
    - `int metadataToken`: Metadata token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 469)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEvent(module: /* DmdModule */, metadataToken: /* int */);
    ```
- `public DmdEventInfo GetEvent(string name)`
  - Summary: Gets a public static or instance event
  - Parameters:
    - `string name`: Name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 820)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEvent(name: /* string */);
    ```
- `public DmdEventInfo GetEvent(string name, Type eventHandlerType, bool throwOnError)`
  - Summary: Gets an event
  - Parameters:
    - `string name`: Name
    - `Type eventHandlerType`: Event handler type
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 613)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEvent(name: /* string */, eventHandlerType: /* Type */, throwOnError: /* bool */);
    ```
- `public DmdEventInfo[] GetEvents()`
  - Summary: Gets all public static or instance events
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 834)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEvents();
    ```
- `public DmdFieldInfo GetField(DmdModule module, int metadataToken)`
  - Summary: Gets a field or returns null if it doesn't exist
  - Parameters:
    - `DmdModule module`: Module
    - `int metadataToken`: Metadata token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 435)
  - Example:
    ```csharp
    // Example invocation
    instance.GetField(module: /* DmdModule */, metadataToken: /* int */);
    ```
- `public DmdFieldInfo GetField(string name)`
  - Summary: Gets a public static or instance field
  - Parameters:
    - `string name`: Name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 779)
  - Example:
    ```csharp
    // Example invocation
    instance.GetField(name: /* string */);
    ```
- `public DmdFieldInfo GetField(string name, Type fieldType, bool throwOnError)`
  - Summary: Gets a field
  - Parameters:
    - `string name`: Name
    - `Type fieldType`: Field type
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 556)
  - Example:
    ```csharp
    // Example invocation
    instance.GetField(name: /* string */, fieldType: /* Type */, throwOnError: /* bool */);
    ```
- `public DmdFieldInfo[] GetFields()`
  - Summary: Gets all public static or instance fields
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 785)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFields();
    ```
- `public DmdMemberInfo[] GetMember(string name)`
  - Summary: Gets a public static or instance member
  - Parameters:
    - `string name`: Name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 975)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMember(name: /* string */);
    ```
- `public DmdMemberInfo[] GetMember(string name, DmdBindingFlags bindingAttr)`
  - Summary: Gets a public static or instance member
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 983)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMember(name: /* string */, bindingAttr: /* DmdBindingFlags */);
    ```
- `public DmdMemberInfo[] GetMembers()`
  - Summary: Gets all public static or instance members
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 998)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMembers();
    ```
- `public DmdMethodBase GetMethod(DmdModule module, int metadataToken)`
  - Summary: Gets a method or returns null if it doesn't exist
  - Parameters:
    - `DmdModule module`: Module
    - `int metadataToken`: Metadata token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 418)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(module: /* DmdModule */, metadataToken: /* int */);
    ```
- `public DmdMethodBase GetMethod(string name, DmdMethodSignature methodSignature, bool throwOnError)`
  - Summary: Gets a method
  - Parameters:
    - `string name`: Method name
    - `DmdMethodSignature methodSignature`: Method signature
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 487)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, methodSignature: /* DmdMethodSignature */, throwOnError: /* bool */);
    ```
- `public DmdMethodBase GetMethod(string name, DmdSignatureCallingConvention flags, int genericParameterCount, Type returnType, IList<Type> parameterTypes, bool throwOnError)`
  - Summary: Gets a method
  - Parameters:
    - `string name`: Method name
    - `DmdSignatureCallingConvention flags`: Method signature flags
    - `int genericParameterCount`: Generic parameter count
    - `Type returnType`: Return type or null to ignore it
    - `IList<Type> parameterTypes`: Parameter types
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 515)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, flags: /* DmdSignatureCallingConvention */, genericParameterCount: /* int */, returnType: /* Type */, parameterTypes: /* IList<Type> */, throwOnError: /* bool */);
    ```
- `public DmdMethodBase GetMethod(string name, DmdType returnType, IList<DmdType> parameterTypes, bool throwOnError)`
  - Summary: Gets a method
  - Parameters:
    - `string name`: Method name
    - `DmdType returnType`: Return type or null to ignore it
    - `IList<DmdType> parameterTypes`: Parameter types
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 526)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, returnType: /* DmdType */, parameterTypes: /* IList<DmdType> */, throwOnError: /* bool */);
    ```
- `public DmdMethodBase GetMethod(string name, Type returnType, IList<Type> parameterTypes, bool throwOnError)`
  - Summary: Gets a method
  - Parameters:
    - `string name`: Method name
    - `Type returnType`: Return type or null to ignore it
    - `IList<Type> parameterTypes`: Parameter types
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 537)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, returnType: /* Type */, parameterTypes: /* IList<Type> */, throwOnError: /* bool */);
    ```
- `public DmdMethodInfo GetMethod(string name)`
  - Summary: Gets a public static or instance method
  - Parameters:
    - `string name`: Name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 751)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */);
    ```
- `public DmdMethodInfo GetMethod(string name, DmdBindingFlags bindingAttr)`
  - Summary: Gets a method
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 744)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, bindingAttr: /* DmdBindingFlags */);
    ```
- `public DmdMethodInfo GetMethod(string name, DmdBindingFlags bindingAttr, DmdCallingConventions callConvention, IList<Type> types)`
  - Summary: Gets a method
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
    - `DmdCallingConventions callConvention`: Calling convention
    - `IList<Type> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 701)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, bindingAttr: /* DmdBindingFlags */, callConvention: /* DmdCallingConventions */, types: /* IList<Type> */);
    ```
- `public DmdMethodInfo GetMethod(string name, DmdBindingFlags bindingAttr, IList<DmdType> types)`
  - Summary: Gets a method
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
    - `IList<DmdType> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 711)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, bindingAttr: /* DmdBindingFlags */, types: /* IList<DmdType> */);
    ```
- `public DmdMethodInfo GetMethod(string name, DmdBindingFlags bindingAttr, IList<Type> types)`
  - Summary: Gets a method
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
    - `IList<Type> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 720)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, bindingAttr: /* DmdBindingFlags */, types: /* IList<Type> */);
    ```
- `public DmdMethodInfo GetMethod(string name, IList<DmdType> types)`
  - Summary: Gets a public static or instance method
  - Parameters:
    - `string name`: Name
    - `IList<DmdType> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 728)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, types: /* IList<DmdType> */);
    ```
- `public DmdMethodInfo GetMethod(string name, IList<Type> types)`
  - Summary: Gets a public static or instance method
  - Parameters:
    - `string name`: Name
    - `IList<Type> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 736)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, types: /* IList<Type> */);
    ```
- `public DmdMethodInfo[] GetMethods()`
  - Summary: Gets all public static or instance methods
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 757)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethods();
    ```
- `public DmdPropertyInfo GetProperty(DmdModule module, int metadataToken)`
  - Summary: Gets a property or returns null if it doesn't exist
  - Parameters:
    - `DmdModule module`: Module
    - `int metadataToken`: Metadata token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 452)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(module: /* DmdModule */, metadataToken: /* int */);
    ```
- `public DmdPropertyInfo GetProperty(string name)`
  - Summary: Gets a public static or instance property
  - Parameters:
    - `string name`: Name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 927)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */);
    ```
- `public DmdPropertyInfo GetProperty(string name, DmdBindingFlags bindingAttr)`
  - Summary: Gets a property
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 870)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, bindingAttr: /* DmdBindingFlags */);
    ```
- `public DmdPropertyInfo GetProperty(string name, DmdBindingFlags bindingAttr, Type returnType, IList<Type> types)`
  - Summary: Gets a property
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
    - `Type returnType`: Return type
    - `IList<Type> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 861)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, bindingAttr: /* DmdBindingFlags */, returnType: /* Type */, types: /* IList<Type> */);
    ```
- `public DmdPropertyInfo GetProperty(string name, DmdMethodSignature methodSignature, bool throwOnError)`
  - Summary: Gets a property
  - Parameters:
    - `string name`: Name
    - `DmdMethodSignature methodSignature`: Method signature
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 566)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, methodSignature: /* DmdMethodSignature */, throwOnError: /* bool */);
    ```
- `public DmdPropertyInfo GetProperty(string name, DmdSignatureCallingConvention flags, int genericParameterCount, Type returnType, IList<Type> parameterTypes, bool throwOnError)`
  - Summary: Gets a property
  - Parameters:
    - `string name`: Property name
    - `DmdSignatureCallingConvention flags`: Property signature flags
    - `int genericParameterCount`: Generic parameter count
    - `Type returnType`: Return type or null to ignore it
    - `IList<Type> parameterTypes`: Parameter types
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 594)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, flags: /* DmdSignatureCallingConvention */, genericParameterCount: /* int */, returnType: /* Type */, parameterTypes: /* IList<Type> */, throwOnError: /* bool */);
    ```
- `public DmdPropertyInfo GetProperty(string name, DmdType returnType)`
  - Summary: Gets a public static or instance property
  - Parameters:
    - `string name`: Name
    - `DmdType returnType`: Return type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 912)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, returnType: /* DmdType */);
    ```
- `public DmdPropertyInfo GetProperty(string name, DmdType returnType, IList<DmdType> types)`
  - Summary: Gets a public static or instance property
  - Parameters:
    - `string name`: Name
    - `DmdType returnType`: Return type
    - `IList<DmdType> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 879)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, returnType: /* DmdType */, types: /* IList<DmdType> */);
    ```
- `public DmdPropertyInfo GetProperty(string name, IList<DmdType> types)`
  - Summary: Gets a public static or instance property
  - Parameters:
    - `string name`: Name
    - `IList<DmdType> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 896)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, types: /* IList<DmdType> */);
    ```
- `public DmdPropertyInfo GetProperty(string name, IList<Type> types)`
  - Summary: Gets a public static or instance property
  - Parameters:
    - `string name`: Name
    - `IList<Type> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 904)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, types: /* IList<Type> */);
    ```
- `public DmdPropertyInfo GetProperty(string name, Type returnType)`
  - Summary: Gets a public static or instance property
  - Parameters:
    - `string name`: Name
    - `Type returnType`: Return type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 920)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, returnType: /* Type */);
    ```
- `public DmdPropertyInfo GetProperty(string name, Type returnType, IList<Type> types)`
  - Summary: Gets a public static or instance property
  - Parameters:
    - `string name`: Name
    - `Type returnType`: Return type
    - `IList<Type> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 888)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, returnType: /* Type */, types: /* IList<Type> */);
    ```
- `public DmdPropertyInfo[] GetProperties()`
  - Summary: Gets all public static or instance properties
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 940)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperties();
    ```
- `public DmdType GetEnumUnderlyingType()`
  - Summary: Gets the underlying type of an enum (a primitive type)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1259)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEnumUnderlyingType();
    ```
- `public DmdType GetInterface(string name)`
  - Summary: Gets an interface
  - Parameters:
    - `string name`: Name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 799)
  - Example:
    ```csharp
    // Example invocation
    instance.GetInterface(name: /* string */);
    ```
- `public DmdType GetNestedType(string name)`
  - Summary: Gets a public nested type
  - Parameters:
    - `string name`: Name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 960)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNestedType(name: /* string */);
    ```
- `public DmdType GetNullableElementType()`
  - Summary: Gets the nullable value type, eg. if it's a nullable
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 209)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNullableElementType();
    ```
- `public DmdType MakeArrayType(int rank)`
  - Summary: Makes a multi-dimensional array type
  - Parameters:
    - `int rank`: Number of dimensions
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 292)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeArrayType(rank: /* int */);
    ```
- `public DmdType MakeGenericType(IList<Type> typeArguments)`
  - Summary: Makes a generic type
  - Parameters:
    - `IList<Type> typeArguments`: Generic arguments
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 329)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericType(typeArguments: /* IList<Type> */);
    ```
- `public DmdType MakeGenericType(params DmdType[] typeArguments)`
  - Summary: Makes a generic type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 308)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericType();
    ```
- `public DmdType MakeGenericType(params Type[] typeArguments)`
  - Summary: Makes a generic type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 315)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericType();
    ```
- `public DmdType Resolve()`
  - Summary: Resolves a type reference and throws if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 254)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve();
    ```
- `public DmdType ResolveNoThrow()`
  - Summary: Resolves a type reference and returns null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 260)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveNoThrow();
    ```
- `public DmdType[] GetNestedTypes()`
  - Summary: Gets all public nested types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 946)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNestedTypes();
    ```
- `public DmdType[] GetOptionalCustomModifiers()`
  - Summary: Gets all optional custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1228)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOptionalCustomModifiers();
    ```
- `public DmdType[] GetRequiredCustomModifiers()`
  - Summary: Gets all required custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1222)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRequiredCustomModifiers();
    ```
- `public DmdWellKnownType GetWellKnownType()`
  - Summary: Gets the value or if it's not a well known type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1187)
  - Example:
    ```csharp
    // Example invocation
    instance.GetWellKnownType();
    ```
- `public abstract DmdConstructorInfo GetConstructor(DmdBindingFlags bindingAttr, DmdCallingConventions callConvention, IList<DmdType> types)`
  - Summary: Gets a constructor
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Binding flags
    - `DmdCallingConventions callConvention`: Calling convention
    - `IList<DmdType> types`: Parameter types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 623)
  - Example:
    ```csharp
    // Example invocation
    instance.GetConstructor(bindingAttr: /* DmdBindingFlags */, callConvention: /* DmdCallingConventions */, types: /* IList<DmdType> */);
    ```
- `public abstract DmdConstructorInfo[] GetConstructors(DmdBindingFlags bindingAttr)`
  - Summary: Gets constructors
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 676)
  - Example:
    ```csharp
    // Example invocation
    instance.GetConstructors(bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract DmdEventInfo GetEvent(DmdModule module, int metadataToken, bool throwOnError)`
  - Summary: Gets an event
  - Parameters:
    - `DmdModule module`: Module
    - `int metadataToken`: Metadata token
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 478)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEvent(module: /* DmdModule */, metadataToken: /* int */, throwOnError: /* bool */);
    ```
- `public abstract DmdEventInfo GetEvent(string name, DmdBindingFlags bindingAttr)`
  - Summary: Gets an event
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 828)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEvent(name: /* string */, bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract DmdEventInfo GetEvent(string name, DmdType eventHandlerType, bool throwOnError)`
  - Summary: Gets an event
  - Parameters:
    - `string name`: Name
    - `DmdType eventHandlerType`: Event handler type
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 604)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEvent(name: /* string */, eventHandlerType: /* DmdType */, throwOnError: /* bool */);
    ```
- `public abstract DmdEventInfo[] GetEvents(DmdBindingFlags bindingAttr)`
  - Summary: Gets all events
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 841)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEvents(bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract DmdFieldInfo GetField(DmdModule module, int metadataToken, bool throwOnError)`
  - Summary: Gets a field
  - Parameters:
    - `DmdModule module`: Module
    - `int metadataToken`: Metadata token
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 444)
  - Example:
    ```csharp
    // Example invocation
    instance.GetField(module: /* DmdModule */, metadataToken: /* int */, throwOnError: /* bool */);
    ```
- `public abstract DmdFieldInfo GetField(string name, DmdBindingFlags bindingAttr)`
  - Summary: Gets a field
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 772)
  - Example:
    ```csharp
    // Example invocation
    instance.GetField(name: /* string */, bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract DmdFieldInfo GetField(string name, DmdType fieldType, bool throwOnError)`
  - Summary: Gets a field
  - Parameters:
    - `string name`: Name
    - `DmdType fieldType`: Field type
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 547)
  - Example:
    ```csharp
    // Example invocation
    instance.GetField(name: /* string */, fieldType: /* DmdType */, throwOnError: /* bool */);
    ```
- `public abstract DmdFieldInfo[] GetFields(DmdBindingFlags bindingAttr)`
  - Summary: Gets all fields
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 792)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFields(bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract DmdMemberInfo[] GetDefaultMembers()`
  - Summary: Gets all default members
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1011)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDefaultMembers();
    ```
- `public abstract DmdMemberInfo[] GetMember(string name, DmdMemberTypes type, DmdBindingFlags bindingAttr)`
  - Summary: Gets members
  - Parameters:
    - `string name`: Name
    - `DmdMemberTypes type`: Member type
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 992)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMember(name: /* string */, type: /* DmdMemberTypes */, bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract DmdMemberInfo[] GetMembers(DmdBindingFlags bindingAttr)`
  - Summary: Gets all members
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1005)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMembers(bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract DmdMethodBase GetMethod(DmdModule module, int metadataToken, bool throwOnError)`
  - Summary: Gets a method
  - Parameters:
    - `DmdModule module`: Module
    - `int metadataToken`: Metadata token
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 427)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(module: /* DmdModule */, metadataToken: /* int */, throwOnError: /* bool */);
    ```
- `public abstract DmdMethodBase GetMethod(string name, DmdSignatureCallingConvention flags, int genericParameterCount, DmdType returnType, IList<DmdType> parameterTypes, bool throwOnError)`
  - Summary: Gets a method
  - Parameters:
    - `string name`: Method name
    - `DmdSignatureCallingConvention flags`: Method signature flags
    - `int genericParameterCount`: Generic parameter count
    - `DmdType returnType`: Return type or null to ignore it
    - `IList<DmdType> parameterTypes`: Parameter types
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 503)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, flags: /* DmdSignatureCallingConvention */, genericParameterCount: /* int */, returnType: /* DmdType */, parameterTypes: /* IList<DmdType> */, throwOnError: /* bool */);
    ```
- `public abstract DmdMethodInfo GetMethod(string name, DmdBindingFlags bindingAttr, DmdCallingConventions callConvention, IList<DmdType> types)`
  - Summary: Gets a method
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
    - `DmdCallingConventions callConvention`: Calling convention
    - `IList<DmdType> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 691)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethod(name: /* string */, bindingAttr: /* DmdBindingFlags */, callConvention: /* DmdCallingConventions */, types: /* IList<DmdType> */);
    ```
- `public abstract DmdMethodInfo[] GetMethods(DmdBindingFlags bindingAttr)`
  - Summary: Gets all methods
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 764)
  - Example:
    ```csharp
    // Example invocation
    instance.GetMethods(bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract DmdMethodSignature GetFunctionPointerMethodSignature()`
  - Summary: Gets the method signature if this is a function pointer type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1131)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFunctionPointerMethodSignature();
    ```
- `public abstract DmdPropertyInfo GetProperty(DmdModule module, int metadataToken, bool throwOnError)`
  - Summary: Gets a property
  - Parameters:
    - `DmdModule module`: Module
    - `int metadataToken`: Metadata token
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 461)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(module: /* DmdModule */, metadataToken: /* int */, throwOnError: /* bool */);
    ```
- `public abstract DmdPropertyInfo GetProperty(string name, DmdBindingFlags bindingAttr, DmdType returnType, IList<DmdType> types)`
  - Summary: Gets a property
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
    - `DmdType returnType`: Return type
    - `IList<DmdType> types`: Parameter types or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 851)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, bindingAttr: /* DmdBindingFlags */, returnType: /* DmdType */, types: /* IList<DmdType> */);
    ```
- `public abstract DmdPropertyInfo GetProperty(string name, DmdSignatureCallingConvention flags, int genericParameterCount, DmdType returnType, IList<DmdType> parameterTypes, bool throwOnError)`
  - Summary: Gets a property
  - Parameters:
    - `string name`: Property name
    - `DmdSignatureCallingConvention flags`: Property signature flags
    - `int genericParameterCount`: Generic parameter count
    - `DmdType returnType`: Return type or null to ignore it
    - `IList<DmdType> parameterTypes`: Parameter types
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 582)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperty(name: /* string */, flags: /* DmdSignatureCallingConvention */, genericParameterCount: /* int */, returnType: /* DmdType */, parameterTypes: /* IList<DmdType> */, throwOnError: /* bool */);
    ```
- `public abstract DmdPropertyInfo[] GetProperties(DmdBindingFlags bindingAttr)`
  - Summary: Gets all properties
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Bindig flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 934)
  - Example:
    ```csharp
    // Example invocation
    instance.GetProperties(bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract DmdType GetElementType()`
  - Summary: Gets the element type if it's an array, a by-ref or a pointer type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1199)
  - Example:
    ```csharp
    // Example invocation
    instance.GetElementType();
    ```
- `public abstract DmdType GetGenericTypeDefinition()`
  - Summary: Gets the generic type definition if it's a generic type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1216)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGenericTypeDefinition();
    ```
- `public abstract DmdType GetInterface(string name, bool ignoreCase)`
  - Summary: Gets an interface
  - Parameters:
    - `string name`: Name
    - `bool ignoreCase`: true if ignore case
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 807)
  - Example:
    ```csharp
    // Example invocation
    instance.GetInterface(name: /* string */, ignoreCase: /* bool */);
    ```
- `public abstract DmdType GetNestedType(string name, DmdBindingFlags bindingAttr)`
  - Summary: Gets a nested type
  - Parameters:
    - `string name`: Name
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 968)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNestedType(name: /* string */, bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract DmdType MakeArrayType()`
  - Summary: Makes a SZ array type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 285)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeArrayType();
    ```
- `public abstract DmdType MakeArrayType(int rank, IList<int> sizes, IList<int> lowerBounds)`
  - Summary: Makes a multi-dimensional array type
  - Parameters:
    - `int rank`: Number of dimensions
    - `IList<int> sizes`: Sizes
    - `IList<int> lowerBounds`: Lower bounds
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 301)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeArrayType(rank: /* int */, sizes: /* IList<int> */, lowerBounds: /* IList<int> */);
    ```
- `public abstract DmdType MakeByRefType()`
  - Summary: Makes a by-ref type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 279)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeByRefType();
    ```
- `public abstract DmdType MakeGenericType(IList<DmdType> typeArguments)`
  - Summary: Makes a generic type
  - Parameters:
    - `IList<DmdType> typeArguments`: Generic arguments
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 322)
  - Example:
    ```csharp
    // Example invocation
    instance.MakeGenericType(typeArguments: /* IList<DmdType> */);
    ```
- `public abstract DmdType MakePointerType()`
  - Summary: Makes a pointer type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 273)
  - Example:
    ```csharp
    // Example invocation
    instance.MakePointerType();
    ```
- `public abstract DmdType Resolve(bool throwOnError)`
  - Summary: Resolves a type reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 267)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve(throwOnError: /* bool */);
    ```
- `public abstract DmdType WithCustomModifiers(IList<DmdCustomModifier> customModifiers)`
  - Summary: Returns a type with the specified custom modifiers
  - Parameters:
    - `IList<DmdCustomModifier> customModifiers`: New custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1241)
  - Example:
    ```csharp
    // Example invocation
    instance.WithCustomModifiers(customModifiers: /* IList<DmdCustomModifier> */);
    ```
- `public abstract DmdType WithoutCustomModifiers()`
  - Summary: Returns a type without custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1247)
  - Example:
    ```csharp
    // Example invocation
    instance.WithoutCustomModifiers();
    ```
- `public abstract DmdType[] GetNestedTypes(DmdBindingFlags bindingAttr)`
  - Summary: Gets all nested types
  - Parameters:
    - `DmdBindingFlags bindingAttr`: Binding flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 953)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNestedTypes(bindingAttr: /* DmdBindingFlags */);
    ```
- `public abstract ReadOnlyCollection<DmdCustomModifier> GetCustomModifiers()`
  - Summary: Gets all custom modifiers
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1234)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCustomModifiers();
    ```
- `public abstract ReadOnlyCollection<DmdType> GetGenericArguments()`
  - Summary: Gets the generic arguments
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1205)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGenericArguments();
    ```
- `public abstract ReadOnlyCollection<DmdType> GetGenericParameterConstraints()`
  - Summary: Gets all generic parameter constraints
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1110)
  - Example:
    ```csharp
    // Example invocation
    instance.GetGenericParameterConstraints();
    ```
- `public abstract ReadOnlyCollection<DmdType> GetInterfaces()`
  - Summary: Gets all interfaces
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 813)
  - Example:
    ```csharp
    // Example invocation
    instance.GetInterfaces();
    ```
- `public abstract ReadOnlyCollection<int> GetArrayLowerBounds()`
  - Summary: Gets the lower bounds of each dimension of an array. The returned list could have less elements than the rank of the array.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1031)
  - Example:
    ```csharp
    // Example invocation
    instance.GetArrayLowerBounds();
    ```
- `public abstract ReadOnlyCollection<int> GetArraySizes()`
  - Summary: Gets the array sizes of each dimension of an array. The returned list could have less elements than the rank of the array.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1024)
  - Example:
    ```csharp
    // Example invocation
    instance.GetArraySizes();
    ```
- `public abstract int GetArrayRank()`
  - Summary: Gets the number of dimensions if this is an array
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1017)
  - Example:
    ```csharp
    // Example invocation
    instance.GetArrayRank();
    ```
- `public abstract string[] GetEnumNames()`
  - Summary: Returns the names of the members of the enum type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1253)
  - Example:
    ```csharp
    // Example invocation
    instance.GetEnumNames();
    ```
- `public bool CanCastTo(DmdType target)`
  - Summary: Returns true if it's possible to cast this type to
  - Parameters:
    - `DmdType target`: Target type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1317)
  - Example:
    ```csharp
    // Example invocation
    instance.CanCastTo(target: /* DmdType */);
    ```
- `public bool CanCastTo(Type target)`
  - Summary: Returns true if it's possible to cast this type to
  - Parameters:
    - `Type target`: Target type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1328)
  - Example:
    ```csharp
    // Example invocation
    instance.CanCastTo(target: /* Type */);
    ```
- `public bool Equals(DmdType other)`
  - Summary: Equals()
  - Parameters:
    - `DmdType other`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1416)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* DmdType */);
    ```
- `public bool IsAssignableFrom(DmdType c)`
  - Summary: Returns true if an instance of can be assigned to an instance of this type
  - Parameters:
    - `DmdType c`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1299)
  - Example:
    ```csharp
    // Example invocation
    instance.IsAssignableFrom(c: /* DmdType */);
    ```
- `public bool IsAssignableFrom(Type c)`
  - Summary: Returns true if an instance of can be assigned to an instance of this type
  - Parameters:
    - `Type c`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1310)
  - Example:
    ```csharp
    // Example invocation
    instance.IsAssignableFrom(c: /* Type */);
    ```
- `public bool IsEquivalentTo(DmdType other)`
  - Summary: Returns true if this type is equivalent to
  - Parameters:
    - `DmdType other`: Other types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1357)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEquivalentTo(other: /* DmdType */);
    ```
- `public bool IsEquivalentTo(Type other)`
  - Summary: Returns true if this type is equivalent to
  - Parameters:
    - `Type other`: Other types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1364)
  - Example:
    ```csharp
    // Example invocation
    instance.IsEquivalentTo(other: /* Type */);
    ```
- `public bool IsSubclassOf(DmdType type)`
  - Summary: Returns true if this instance derives from . Also returns true if this type is an interface and is .
  - Parameters:
    - `DmdType type`: Other type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1274)
  - Example:
    ```csharp
    // Example invocation
    instance.IsSubclassOf(type: /* DmdType */);
    ```
- `public bool IsSubclassOf(Type type)`
  - Summary: Returns true if this instance derives from . Also returns true if this type is an interface and is .
  - Parameters:
    - `Type type`: Other type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1292)
  - Example:
    ```csharp
    // Example invocation
    instance.IsSubclassOf(type: /* Type */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1423)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1429)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public sealed override DmdCustomAttributeData FindCustomAttribute(DmdType attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1404)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public sealed override DmdCustomAttributeData FindCustomAttribute(string attributeTypeFullName, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1396)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `public sealed override DmdMemberInfo ResolveMember(bool throwOnError)`
  - Summary: Resolves a member reference
  - Parameters:
    - `bool throwOnError`: true to throw if it doesn't exist, false to return null if it doesn't exist
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 248)
  - Example:
    ```csharp
    // Example invocation
    instance.ResolveMember(throwOnError: /* bool */);
    ```
- `public sealed override bool IsDefined(DmdType attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1388)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `public sealed override bool IsDefined(string attributeTypeFullName, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1380)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `public sealed override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1435)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static TypeCode GetTypeCode(DmdType type)`
  - Summary: Gets the type code
  - Parameters:
    - `DmdType type`: Type or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 336)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Metadata.DmdType.GetTypeCode(type: /* DmdType */);
    ```

### Properties

- `public DmdConstructorInfo TypeInitializer => GetConstructor(DmdBindingFlags.Static | DmdBindingFlags.Public | DmdBindingFlags.NonPublic, DmdCallingConventions.Any, Array.Empty<DmdType>())`
  - Summary: Gets the type initializer
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 681)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeInitializer;
    ```
- `public ReadOnlyCollection<DmdType> GenericTypeArguments => IsConstructedGenericType ? GetGenericArguments() : ReadOnlyCollectionHelpers.Empty<DmdType>()`
  - Summary: Gets all generic arguments if it's a constructed generic type ()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1210)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericTypeArguments;
    ```
- `public abstract DmdAssembly Assembly { get; }`
  - Summary: Gets the assembly
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Assembly;
    ```
- `public abstract DmdGenericParameterAttributes GenericParameterAttributes { get; }`
  - Summary: Gets the generic parameter attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 121)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericParameterAttributes;
    ```
- `public abstract DmdMethodBase DeclaringMethod { get; }`
  - Summary: Gets the declaring method or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DeclaringMethod;
    ```
- `public abstract DmdType BaseType { get; }`
  - Summary: Gets the base type or null if none
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BaseType;
    ```
- `public abstract DmdTypeAttributes Attributes { get; }`
  - Summary: Gets the type attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 154)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Attributes;
    ```
- `public abstract DmdTypeScope TypeScope { get; }`
  - Summary: Gets the type scope. This property is only valid if it's a TypeDef or TypeRef (i.e., not an array, generic instance, etc)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeScope;
    ```
- `public abstract DmdTypeSignatureKind TypeSignatureKind { get; }`
  - Summary: Gets the type signature kind
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TypeSignatureKind;
    ```
- `public abstract IEnumerable<DmdEventInfo> Events { get; }`
  - Summary: Gets all events
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 385)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Events;
    ```
- `public abstract IEnumerable<DmdFieldInfo> Fields { get; }`
  - Summary: Gets all fields
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 370)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Fields;
    ```
- `public abstract IEnumerable<DmdMethodBase> Methods { get; }`
  - Summary: Gets all methods and constructors
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 375)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Methods;
    ```
- `public abstract IEnumerable<DmdPropertyInfo> Properties { get; }`
  - Summary: Gets all properties
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 380)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Properties;
    ```
- `public abstract ReadOnlyCollection<DmdEventInfo> DeclaredEvents { get; }`
  - Summary: Gets all declared events
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 405)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DeclaredEvents;
    ```
- `public abstract ReadOnlyCollection<DmdFieldInfo> DeclaredFields { get; }`
  - Summary: Gets all declared fields
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 390)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DeclaredFields;
    ```
- `public abstract ReadOnlyCollection<DmdMethodBase> DeclaredMethods { get; }`
  - Summary: Gets all declared methods and constructors
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 395)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DeclaredMethods;
    ```
- `public abstract ReadOnlyCollection<DmdPropertyInfo> DeclaredProperties { get; }`
  - Summary: Gets all declared properties
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 400)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DeclaredProperties;
    ```
- `public abstract ReadOnlyCollection<DmdType> NestedTypes { get; }`
  - Summary: Gets all nested types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 410)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NestedTypes;
    ```
- `public abstract StructLayoutAttribute StructLayoutAttribute { get; }`
  - Summary: Gets the struct layout attribute
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StructLayoutAttribute;
    ```
- `public abstract bool HasElementType { get; }`
  - Summary: true if it has an element type, i.e., it's an array, a by-ref or a pointer type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1171)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasElementType;
    ```
- `public abstract bool IsGenericType { get; }`
  - Summary: true if it's a generic type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1051)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsGenericType;
    ```
- `public abstract bool IsGenericTypeDefinition { get; }`
  - Summary: true if it's a generic type definition
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1056)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsGenericTypeDefinition;
    ```
- `public abstract int GenericParameterPosition { get; }`
  - Summary: Gets the generic parameter position if this is a generic parameter
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1071)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericParameterPosition;
    ```
- `public abstract override DmdModule Module { get; }`
  - Summary: Gets the module
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public abstract string MetadataName { get; }`
  - Summary: Gets the name stored in the metadata. It's not escaped like
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataName;
    ```
- `public abstract string MetadataNamespace { get; }`
  - Summary: Gets the namespace or null. This is the namespace stored in the metadata. is the namespace of the non-declaring type.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataNamespace;
    ```
- `public abstract string Namespace { get; }`
  - Summary: Gets the namespace or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Namespace;
    ```
- `public bool ContainsGenericParameters => CalculateContainsGenericParameters(this)`
  - Summary: true if this type contains generic parameters
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1091)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContainsGenericParameters;
    ```
- `public bool HasSecurity => (Attributes & DmdTypeAttributes.HasSecurity) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 180)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasSecurity;
    ```
- `public bool IsAbstract => (Attributes & DmdTypeAttributes.Abstract) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 171)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAbstract;
    ```
- `public bool IsAnsiClass => (Attributes & DmdTypeAttributes.StringFormatMask) == DmdTypeAttributes.AnsiClass`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 181)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAnsiClass;
    ```
- `public bool IsArray => TypeSignatureKind == DmdTypeSignatureKind.SZArray || TypeSignatureKind == DmdTypeSignatureKind.MDArray`
  - Summary: true if it's an array (SZ array or MD array)
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1036)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsArray;
    ```
- `public bool IsAutoClass => (Attributes & DmdTypeAttributes.StringFormatMask) == DmdTypeAttributes.AutoClass`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 183)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAutoClass;
    ```
- `public bool IsAutoLayout => (Attributes & DmdTypeAttributes.LayoutMask) == DmdTypeAttributes.AutoLayout`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 165)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAutoLayout;
    ```
- `public bool IsBeforeFieldInit => (Attributes & DmdTypeAttributes.BeforeFieldInit) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 177)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsBeforeFieldInit;
    ```
- `public bool IsByRef => TypeSignatureKind == DmdTypeSignatureKind.ByRef`
  - Summary: true if this is a by-ref type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1115)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsByRef;
    ```
- `public bool IsByRefLike =>
			//TODO: .NET Core adds this attribute to by ref like types, but .NET Framework does not, eg.
			//		ArgIterator, RuntimeArgumentHandle, TypedReference
			CustomAttributesHelper.IsDefined(this, "System.Runtime.CompilerServices.IsByRefLikeAttribute", inherit: false)`
  - Summary: true if this is a by-ref like value type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1369)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsByRefLike;
    ```
- `public bool IsCOMObject => CanCastTo(AppDomain.GetWellKnownType(DmdWellKnownType.System___ComObject, isOptional: true))`
  - Summary: true if it's a COM object
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1166)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsCOMObject;
    ```
- `public bool IsClass => (Attributes & DmdTypeAttributes.ClassSemanticsMask) == DmdTypeAttributes.Class && !IsValueType`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 168)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsClass;
    ```
- `public bool IsConstructedGenericType => IsGenericType && !IsGenericTypeDefinition`
  - Summary: true if it's a constructed generic type. These types can be instantiated.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1061)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsConstructedGenericType;
    ```
- `public bool IsContextful => CanCastTo(AppDomain.GetWellKnownType(DmdWellKnownType.System_ContextBoundObject, isOptional: true))`
  - Summary: true if it's a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1176)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsContextful;
    ```
- `public bool IsCustomFormatClass => (Attributes & DmdTypeAttributes.StringFormatMask) == DmdTypeAttributes.CustomFormatClass`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 184)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsCustomFormatClass;
    ```
- `public bool IsEnum => BaseType == AppDomain.System_Enum`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 173)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEnum;
    ```
- `public bool IsExplicitLayout => (Attributes & DmdTypeAttributes.LayoutMask) == DmdTypeAttributes.ExplicitLayout`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 167)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsExplicitLayout;
    ```
- `public bool IsForwarder => (Attributes & DmdTypeAttributes.Forwarder) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 178)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsForwarder;
    ```
- `public bool IsFunctionPointer => TypeSignatureKind == DmdTypeSignatureKind.FunctionPointer`
  - Summary: true if this is a function pointer type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1125)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsFunctionPointer;
    ```
- `public bool IsGenericMethodParameter => TypeSignatureKind == DmdTypeSignatureKind.MethodGenericParameter`
  - Summary: true if it's a generic method parameter
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1086)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsGenericMethodParameter;
    ```
- `public bool IsGenericParameter => TypeSignatureKind == DmdTypeSignatureKind.TypeGenericParameter || TypeSignatureKind == DmdTypeSignatureKind.MethodGenericParameter`
  - Summary: true if it's a generic type or method parameter
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1066)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsGenericParameter;
    ```
- `public bool IsGenericTypeParameter => TypeSignatureKind == DmdTypeSignatureKind.TypeGenericParameter`
  - Summary: true if it's a generic type parameter
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1081)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsGenericTypeParameter;
    ```
- `public bool IsImport => (Attributes & DmdTypeAttributes.Import) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 175)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsImport;
    ```
- `public bool IsInterface => (Attributes & DmdTypeAttributes.ClassSemanticsMask) == DmdTypeAttributes.Interface`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 169)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsInterface;
    ```
- `public bool IsLayoutSequential => (Attributes & DmdTypeAttributes.LayoutMask) == DmdTypeAttributes.SequentialLayout`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 166)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsLayoutSequential;
    ```
- `public bool IsMarshalByRef => CanCastTo(AppDomain.GetWellKnownType(DmdWellKnownType.System_MarshalByRefObject, isOptional: true))`
  - Summary: true if it's a
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1181)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsMarshalByRef;
    ```
- `public bool IsNested => (object)DeclaringType != null`
  - Summary: true if it's a nested type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 116)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNested;
    ```
- `public bool IsNestedAssembly => (Attributes & DmdTypeAttributes.VisibilityMask) == DmdTypeAttributes.NestedAssembly`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 162)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNestedAssembly;
    ```
- `public bool IsNestedFamANDAssem => (Attributes & DmdTypeAttributes.VisibilityMask) == DmdTypeAttributes.NestedFamANDAssem`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 163)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNestedFamANDAssem;
    ```
- `public bool IsNestedFamORAssem => (Attributes & DmdTypeAttributes.VisibilityMask) == DmdTypeAttributes.NestedFamORAssem`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 164)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNestedFamORAssem;
    ```
- `public bool IsNestedFamily => (Attributes & DmdTypeAttributes.VisibilityMask) == DmdTypeAttributes.NestedFamily`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 161)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNestedFamily;
    ```
- `public bool IsNestedPrivate => (Attributes & DmdTypeAttributes.VisibilityMask) == DmdTypeAttributes.NestedPrivate`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 160)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNestedPrivate;
    ```
- `public bool IsNestedPublic => (Attributes & DmdTypeAttributes.VisibilityMask) == DmdTypeAttributes.NestedPublic`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 159)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNestedPublic;
    ```
- `public bool IsNotPublic => (Attributes & DmdTypeAttributes.VisibilityMask) == DmdTypeAttributes.NotPublic`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 157)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNotPublic;
    ```
- `public bool IsNullable {
			get {
				switch (TypeSignatureKind) {
				case DmdTypeSignatureKind.GenericInstance:
					return GetGenericTypeDefinition() == AppDomain.System_Nullable_T;

				case DmdTypeSignatureKind.Type:
					return this == AppDomain.System_Nullable_T;

				default:
					return false;
				}
			}
		}`
  - Summary: true if this type is
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 190)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNullable;
    ```
- `public bool IsPointer => TypeSignatureKind == DmdTypeSignatureKind.Pointer`
  - Summary: true if this is a pointer type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1120)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPointer;
    ```
- `public bool IsPrimitive {
			get {
				if (MetadataNamespace != "System" || IsNested)
					return false;
				switch (MetadataName) {
				case "Boolean":	return this == AppDomain.System_Boolean;
				case "Char":	return this == AppDomain.System_Char;
				case "SByte":	return this == AppDomain.System_SByte;
				case "Byte":	return this == AppDomain.System_Byte;
				case "Int16":	return this == AppDomain.System_Int16;
				case "UInt16":	return this == AppDomain.System_UInt16;
				case "Int32":	return this == AppDomain.System_Int32;
				case "UInt32":	return this == AppDomain.System_UInt32;
				case "Int64":	return this == AppDomain.System_Int64;
				case "UInt64":	return this == AppDomain.System_UInt64;
				case "Single":	return this == AppDomain.System_Single;
				case "Double":	return this == AppDomain.System_Double;
				case "IntPtr":	return this == AppDomain.System_IntPtr;
				case "UIntPtr":	return this == AppDomain.System_UIntPtr;
				}
				return false;
			}
		}`
  - Summary: true if this is a primitive type (, , , , , , , , , , , , , )
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1139)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPrimitive;
    ```
- `public bool IsPublic => (Attributes & DmdTypeAttributes.VisibilityMask) == DmdTypeAttributes.Public`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 158)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsPublic;
    ```
- `public bool IsRTSpecialName => (Attributes & DmdTypeAttributes.RTSpecialName) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 179)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRTSpecialName;
    ```
- `public bool IsSZArray => TypeSignatureKind == DmdTypeSignatureKind.SZArray`
  - Summary: true if it's an SZ array
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1041)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSZArray;
    ```
- `public bool IsSealed => (Attributes & DmdTypeAttributes.Sealed) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 172)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSealed;
    ```
- `public bool IsSerializable {
			get {
				if ((Attributes & DmdTypeAttributes.Serializable) != 0)
					return true;
				var systemDelegate = AppDomain.System_Delegate;
				var systemEnum = AppDomain.System_Enum;
				for (var type = this; (object)type != null; type = type.BaseType) {
					if (type == systemDelegate || type == systemEnum)
						return true;
				}
				return false;
			}
		}`
  - Summary: true if it's a serializable type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 222)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSerializable;
    ```
- `public bool IsSpecialName => (Attributes & DmdTypeAttributes.SpecialName) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 174)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsSpecialName;
    ```
- `public bool IsTypeDefinition => TypeSignatureKind == DmdTypeSignatureKind.Type`
  - Summary: true if it's a non constructed type with a TypeDef token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1076)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsTypeDefinition;
    ```
- `public bool IsUnicodeClass => (Attributes & DmdTypeAttributes.StringFormatMask) == DmdTypeAttributes.UnicodeClass`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 182)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsUnicodeClass;
    ```
- `public bool IsValueType => BaseType is DmdType baseType && (baseType == AppDomain.System_ValueType ? this != AppDomain.System_Enum : baseType == AppDomain.System_Enum)`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 170)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsValueType;
    ```
- `public bool IsVariableBoundArray => TypeSignatureKind == DmdTypeSignatureKind.MDArray`
  - Summary: true if it's a multi-dimensional array
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1046)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsVariableBoundArray;
    ```
- `public bool IsVisible => CalculateIsVisible(this)`
  - Summary: true if this is a public type and all its declaring types are public
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 126)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsVisible;
    ```
- `public bool IsWindowsRuntime => (Attributes & DmdTypeAttributes.WindowsRuntime) != 0`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 176)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsWindowsRuntime;
    ```
- `public override DmdAppDomain AppDomain => Assembly.AppDomain`
  - Summary: Gets the AppDomain
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public override DmdType ReflectedType => DeclaringType`
  - Summary: Gets the reflected type. This is the type that owns this member, see also
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ReflectedType;
    ```
- `public sealed override DmdMemberTypes MemberType => (TypeSignatureKind == DmdTypeSignatureKind.Type || TypeSignatureKind == DmdTypeSignatureKind.GenericInstance) && (object)DeclaringType != null ? DmdMemberTypes.NestedType : DmdMemberTypes.TypeInfo`
  - Summary: Gets the member type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemberType;
    ```
- `public sealed override string Name => DmdMemberFormatter.FormatName(this)`
  - Summary: Gets the name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 85)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public string AssemblyQualifiedName => DmdMemberFormatter.FormatAssemblyQualifiedName(this)`
  - Summary: Gets the assembly qualified name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyQualifiedName;
    ```
- `public string FullName => DmdMemberFormatter.FormatFullName(this)`
  - Summary: Gets the full name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FullName;
    ```

### Operators

- `public static bool operator !=(DmdType left, DmdType right) => !DmdMemberInfoEqualityComparer.DefaultType.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1408)
- `public static bool operator ==(DmdType left, DmdType right) => DmdMemberInfoEqualityComparer.DefaultType.Equals(left, right);`
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdType.cs` (line 1407)

## Enum `DmdTypeAttributes`

Type attributes

**Inherits/Implements:** `uint`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdTypeAttributes and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdTypeAttributes(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeAttributes.cs` (line 26)

### Members

- `VisibilityMask` = `x00000007`
- `NotPublic` = `x00000000`
- `Public` = `x00000001`
- `NestedPublic` = `x00000002`
- `NestedPrivate` = `x00000003`
- `NestedFamily` = `x00000004`
- `NestedAssembly` = `x00000005`
- `NestedFamANDAssem` = `x00000006`
- `NestedFamORAssem` = `x00000007`
- `LayoutMask` = `x00000018`
- `AutoLayout` = `x00000000`
- `SequentialLayout` = `x00000008`
- `ExplicitLayout` = `x00000010`
- `ClassSemanticsMask` = `x00000020`
- `Class` = `x00000000`
- `Interface` = `x00000020`
- `Abstract` = `x00000080`
- `Sealed` = `x00000100`
- `SpecialName` = `x00000400`
- `Import` = `x00001000`
- `Serializable` = `x00002000`
- `WindowsRuntime` = `x00004000`
- `StringFormatMask` = `x00030000`
- `AnsiClass` = `x00000000`
- `UnicodeClass` = `x00010000`
- `AutoClass` = `x00020000`
- `CustomFormatClass` = `x00030000`
- `CustomFormatMask` = `x00C00000`
- `BeforeFieldInit` = `x00100000`
- `Forwarder` = `x00200000`
- `ReservedMask` = `x00040800`
- `RTSpecialName` = `x00000800`
- `HasSecurity` = `x00040000`

## Struct `DmdTypeLoadedEventArgs`

Class loaded event args

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdTypeLoadedEventArgs(metadataToken: /* int */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDynamicModuleHelper.cs` (line 49)

### Constructors

- `public DmdTypeLoadedEventArgs(int metadataToken)`
  - Summary: Constructor
  - Parameters:
    - `int metadataToken`: Metadata token of the type that got loaded
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDynamicModuleHelper.cs` (line 59)

### Properties

- `public int MetadataToken { get; }`
  - Summary: Gets the metadata token of the type that got loaded
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdDynamicModuleHelper.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataToken;
    ```

## Struct `DmdTypeName`

Type name

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdTypeName(@namespace: /* string */, name: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 27)

### Constructors

- `public DmdTypeName(string @namespace, string name)`
  - Summary: Constructor
  - Parameters:
    - `string @namespace`: Description not provided.
    - `string name`: Name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 48)
- `public DmdTypeName(string @namespace, string name, string extra)`
  - Summary: Constructor
  - Parameters:
    - `string @namespace`: Description not provided.
    - `string name`: Name
    - `string extra`: Nested type names, separated with '+'
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 60)

### Methods

- `public override string ToString()`
  - Summary: Gets the type name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static DmdTypeName Create(DmdType type)`
  - Summary: Creates a
  - Parameters:
    - `DmdType type`: Type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Metadata.DmdTypeName.Create(type: /* DmdType */);
    ```

### Fields

- `public readonly string Extra`
  - Summary: Nested type names, separated with '+'
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 41)
  - Example:
    ```csharp
    var value = instance.Extra;
    ```
- `public readonly string Name`
  - Summary: Name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 36)
  - Example:
    ```csharp
    var value = instance.Name;
    ```
- `public readonly string Namespace`
  - Summary: Namespace or null
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 31)
  - Example:
    ```csharp
    var value = instance.Namespace;
    ```

## Class `DmdTypeNameEqualityComparer`

equality comparer

**Inherits/Implements:** `IEqualityComparer<DmdTypeName>`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdTypeNameEqualityComparer and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdTypeNameEqualityComparer(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 119)

### Methods

- `public bool Equals(DmdTypeName x, DmdTypeName y)`
  - Summary: Equals()
  - Parameters:
    - `DmdTypeName x`: Description not provided.
    - `DmdTypeName y`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(x: /* DmdTypeName */, y: /* DmdTypeName */);
    ```
- `public int GetHashCode(DmdTypeName obj)`
  - Summary: GetHashCode()
  - Parameters:
    - `DmdTypeName obj`: Description not provided.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 142)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode(obj: /* DmdTypeName */);
    ```

### Fields

- `public static readonly DmdTypeNameEqualityComparer Instance = new DmdTypeNameEqualityComparer()`
  - Summary: Gets the single instance
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeName.cs` (line 123)
  - Example:
    ```csharp
    var value = dnSpy.Debugger.DotNet.Metadata.DmdTypeNameEqualityComparer.Instance;
    ```

## Struct `DmdTypeScope`

A scope

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdTypeScope(module: /* DmdModule */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeScope.cs` (line 51)

### Constructors

- `public DmdTypeScope(DmdModule module)`
  - Summary: Constructor
  - Parameters:
    - `DmdModule module`: Module
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeScope.cs` (line 84)
- `public DmdTypeScope(IDmdAssemblyName assembly, string moduleName)`
  - Summary: Constructor
  - Parameters:
    - `IDmdAssemblyName assembly`: Assembly
    - `string moduleName`: Module name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeScope.cs` (line 95)
- `public DmdTypeScope(IDmdAssemblyName assemblyRef)`
  - Summary: Constructor
  - Parameters:
    - `IDmdAssemblyName assemblyRef`: Assembly reference
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeScope.cs` (line 105)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeScope.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public DmdTypeScopeKind Kind { get; }`
  - Summary: Gets the kind
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeScope.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public object Data { get; }`
  - Summary: Gets the data: , (),
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeScope.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```
- `public object Data2 { get; }`
  - Summary: Used if it's a module reference. This is the assembly name ()
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeScope.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data2;
    ```

### Fields

- `public static readonly DmdTypeScope Invalid = new DmdTypeScope(DmdTypeScopeKind.Invalid)`
  - Summary: An instance whose equals
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeScope.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Debugger.DotNet.Metadata.DmdTypeScope.Invalid;
    ```

## Enum `DmdTypeScopeKind`

Type scope kind

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdTypeScopeKind and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdTypeScopeKind(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeScope.cs` (line 26)

### Members

- `Invalid`: It's not a TypeDef or TypeRef so it doesn't have a type scope
- `Module`: Same module as the reference
- `ModuleRef`: A reference to another module in the same assembly
- `AssemblyRef`: A reference to another assembly

## Enum `DmdTypeSignatureKind`

Type signature code

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdTypeSignatureKind and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdTypeSignatureKind(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdTypeSignatureKind.cs` (line 24)

### Members

- `Type`: A normal type (TypeDef or TypeRef)
- `Pointer`: Pointer type
- `ByRef`: By-ref type
- `TypeGenericParameter`: Generic parameter (type)
- `MethodGenericParameter`: Generic parameter (method)
- `SZArray`: SZ array type
- `MDArray`: Multi-dimensional array type
- `GenericInstance`: Generic instance type
- `FunctionPointer`: Function pointer type

## Enum `DmdWellKnownType`

Well known types

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.DmdWellKnownType and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.DmdWellKnownType(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdWellKnownType.cs` (line 7)

### Members

- `System_Object`
- `System_Enum`
- `System_MulticastDelegate`
- `System_Delegate`
- `System_ValueType`
- `System_Void`
- `System_Boolean`
- `System_Char`
- `System_SByte`
- `System_Byte`
- `System_Int16`
- `System_UInt16`
- `System_Int32`
- `System_UInt32`
- `System_Int64`
- `System_UInt64`
- `System_Decimal`
- `System_Single`
- `System_Double`
- `System_String`
- `System_IntPtr`
- `System_UIntPtr`
- `System_Array`
- `System_Collections_IEnumerable`
- `System_Collections_Generic_IEnumerable_T`
- `System_Collections_Generic_IList_T`
- `System_Collections_Generic_ICollection_T`
- `System_Collections_IEnumerator`
- `System_Collections_Generic_IEnumerator_T`
- `System_Collections_Generic_IReadOnlyList_T`
- `System_Collections_Generic_IReadOnlyCollection_T`
- `System_Nullable_T`
- `System_DateTime`
- `System_Runtime_CompilerServices_IsVolatile`
- `System_IDisposable`
- `System_TypedReference`
- `System_ArgIterator`
- `System_RuntimeArgumentHandle`
- `System_RuntimeFieldHandle`
- `System_RuntimeMethodHandle`
- `System_RuntimeTypeHandle`
- `System_IAsyncResult`
- `System_AsyncCallback`
- `System_Math`
- `System_Attribute`
- `System_CLSCompliantAttribute`
- `System_Convert`
- `System_Exception`
- `System_FlagsAttribute`
- `System_FormattableString`
- `System_Guid`
- `System_IFormattable`
- `System_MarshalByRefObject`
- `System_Type`
- `System_Reflection_AssemblyKeyFileAttribute`
- `System_Reflection_AssemblyKeyNameAttribute`
- `System_Reflection_MethodInfo`
- `System_Reflection_ConstructorInfo`
- `System_Reflection_MethodBase`
- `System_Reflection_FieldInfo`
- `System_Reflection_MemberInfo`
- `System_Reflection_Missing`
- `System_Runtime_CompilerServices_FormattableStringFactory`
- `System_Runtime_CompilerServices_RuntimeHelpers`
- `System_Runtime_ExceptionServices_ExceptionDispatchInfo`
- `System_Runtime_InteropServices_StructLayoutAttribute`
- `System_Runtime_InteropServices_UnknownWrapper`
- `System_Runtime_InteropServices_DispatchWrapper`
- `System_Runtime_InteropServices_CallingConvention`
- `System_Runtime_InteropServices_ClassInterfaceAttribute`
- `System_Runtime_InteropServices_ClassInterfaceType`
- `System_Runtime_InteropServices_CoClassAttribute`
- `System_Runtime_InteropServices_ComAwareEventInfo`
- `System_Runtime_InteropServices_ComEventInterfaceAttribute`
- `System_Runtime_InteropServices_ComInterfaceType`
- `System_Runtime_InteropServices_ComSourceInterfacesAttribute`
- `System_Runtime_InteropServices_ComVisibleAttribute`
- `System_Runtime_InteropServices_DispIdAttribute`
- `System_Runtime_InteropServices_GuidAttribute`
- `System_Runtime_InteropServices_InterfaceTypeAttribute`
- `System_Runtime_InteropServices_Marshal`
- `System_Runtime_InteropServices_TypeIdentifierAttribute`
- `System_Runtime_InteropServices_BestFitMappingAttribute`
- `System_Runtime_InteropServices_DefaultParameterValueAttribute`
- `System_Runtime_InteropServices_LCIDConversionAttribute`
- `System_Runtime_InteropServices_UnmanagedFunctionPointerAttribute`
- `System_Activator`
- `System_Threading_Tasks_Task`
- `System_Threading_Tasks_Task_T`
- `System_Threading_Interlocked`
- `System_Threading_Monitor`
- `System_Threading_Thread`
- `Microsoft_CSharp_RuntimeBinder_Binder`
- `Microsoft_CSharp_RuntimeBinder_CSharpArgumentInfo`
- `Microsoft_CSharp_RuntimeBinder_CSharpArgumentInfoFlags`
- `Microsoft_CSharp_RuntimeBinder_CSharpBinderFlags`
- `Microsoft_VisualBasic_CallType`
- `Microsoft_VisualBasic_Embedded`
- `Microsoft_VisualBasic_CompilerServices_Conversions`
- `Microsoft_VisualBasic_CompilerServices_Operators`
- `Microsoft_VisualBasic_CompilerServices_NewLateBinding`
- `Microsoft_VisualBasic_CompilerServices_EmbeddedOperators`
- `Microsoft_VisualBasic_CompilerServices_StandardModuleAttribute`
- `Microsoft_VisualBasic_CompilerServices_Utils`
- `Microsoft_VisualBasic_CompilerServices_LikeOperator`
- `Microsoft_VisualBasic_CompilerServices_ProjectData`
- `Microsoft_VisualBasic_CompilerServices_ObjectFlowControl`
- `Microsoft_VisualBasic_CompilerServices_ObjectFlowControl_ForLoopControl`
- `Microsoft_VisualBasic_CompilerServices_StaticLocalInitFlag`
- `Microsoft_VisualBasic_CompilerServices_StringType`
- `Microsoft_VisualBasic_CompilerServices_IncompleteInitialization`
- `Microsoft_VisualBasic_CompilerServices_Versioned`
- `Microsoft_VisualBasic_CompareMethod`
- `Microsoft_VisualBasic_Strings`
- `Microsoft_VisualBasic_ErrObject`
- `Microsoft_VisualBasic_FileSystem`
- `Microsoft_VisualBasic_ApplicationServices_ApplicationBase`
- `Microsoft_VisualBasic_ApplicationServices_WindowsFormsApplicationBase`
- `Microsoft_VisualBasic_Information`
- `Microsoft_VisualBasic_Interaction`
- `System_Func_T`
- `System_Func_T2`
- `System_Func_T3`
- `System_Func_T4`
- `System_Func_T5`
- `System_Func_T6`
- `System_Func_T7`
- `System_Func_T8`
- `System_Func_T9`
- `System_Func_T10`
- `System_Func_T11`
- `System_Func_T12`
- `System_Func_T13`
- `System_Func_T14`
- `System_Func_T15`
- `System_Func_T16`
- `System_Func_T17`
- `System_Action`
- `System_Action_T`
- `System_Action_T2`
- `System_Action_T3`
- `System_Action_T4`
- `System_Action_T5`
- `System_Action_T6`
- `System_Action_T7`
- `System_Action_T8`
- `System_Action_T9`
- `System_Action_T10`
- `System_Action_T11`
- `System_Action_T12`
- `System_Action_T13`
- `System_Action_T14`
- `System_Action_T15`
- `System_Action_T16`
- `System_AttributeUsageAttribute`
- `System_ParamArrayAttribute`
- `System_NonSerializedAttribute`
- `System_STAThreadAttribute`
- `System_Reflection_DefaultMemberAttribute`
- `System_Runtime_CompilerServices_DateTimeConstantAttribute`
- `System_Runtime_CompilerServices_DecimalConstantAttribute`
- `System_Runtime_CompilerServices_IUnknownConstantAttribute`
- `System_Runtime_CompilerServices_IDispatchConstantAttribute`
- `System_Runtime_CompilerServices_ExtensionAttribute`
- `System_Runtime_CompilerServices_INotifyCompletion`
- `System_Runtime_CompilerServices_InternalsVisibleToAttribute`
- `System_Runtime_CompilerServices_CompilerGeneratedAttribute`
- `System_Runtime_CompilerServices_AccessedThroughPropertyAttribute`
- `System_Runtime_CompilerServices_CompilationRelaxationsAttribute`
- `System_Runtime_CompilerServices_RuntimeCompatibilityAttribute`
- `System_Runtime_CompilerServices_UnsafeValueTypeAttribute`
- `System_Runtime_CompilerServices_FixedBufferAttribute`
- `System_Runtime_CompilerServices_DynamicAttribute`
- `System_Runtime_CompilerServices_CallSiteBinder`
- `System_Runtime_CompilerServices_CallSite`
- `System_Runtime_CompilerServices_CallSite_T`
- `System_Runtime_InteropServices_WindowsRuntime_EventRegistrationToken`
- `System_Runtime_InteropServices_WindowsRuntime_EventRegistrationTokenTable_T`
- `System_Runtime_InteropServices_WindowsRuntime_WindowsRuntimeMarshal`
- `Windows_Foundation_IAsyncAction`
- `Windows_Foundation_IAsyncActionWithProgress_T`
- `Windows_Foundation_IAsyncOperation_T`
- `Windows_Foundation_IAsyncOperationWithProgress_T2`
- `System_Diagnostics_Debugger`
- `System_Diagnostics_DebuggerDisplayAttribute`
- `System_Diagnostics_DebuggerNonUserCodeAttribute`
- `System_Diagnostics_DebuggerHiddenAttribute`
- `System_Diagnostics_DebuggerBrowsableAttribute`
- `System_Diagnostics_DebuggerStepThroughAttribute`
- `System_Diagnostics_DebuggerBrowsableState`
- `System_Diagnostics_DebuggableAttribute`
- `System_Diagnostics_DebuggableAttribute__DebuggingModes`
- `System_ComponentModel_DesignerSerializationVisibilityAttribute`
- `System_IEquatable_T`
- `System_Collections_IList`
- `System_Collections_ICollection`
- `System_Collections_Generic_EqualityComparer_T`
- `System_Collections_Generic_List_T`
- `System_Collections_Generic_IDictionary_KV`
- `System_Collections_Generic_IReadOnlyDictionary_KV`
- `System_Collections_ObjectModel_Collection_T`
- `System_Collections_ObjectModel_ReadOnlyCollection_T`
- `System_Collections_Specialized_INotifyCollectionChanged`
- `System_ComponentModel_INotifyPropertyChanged`
- `System_ComponentModel_EditorBrowsableAttribute`
- `System_ComponentModel_EditorBrowsableState`
- `System_Linq_Enumerable`
- `System_Linq_Expressions_Expression`
- `System_Linq_Expressions_Expression_T`
- `System_Linq_Expressions_ParameterExpression`
- `System_Linq_Expressions_ElementInit`
- `System_Linq_Expressions_MemberBinding`
- `System_Linq_Expressions_ExpressionType`
- `System_Linq_IQueryable`
- `System_Linq_IQueryable_T`
- `System_Xml_Linq_Extensions`
- `System_Xml_Linq_XAttribute`
- `System_Xml_Linq_XCData`
- `System_Xml_Linq_XComment`
- `System_Xml_Linq_XContainer`
- `System_Xml_Linq_XDeclaration`
- `System_Xml_Linq_XDocument`
- `System_Xml_Linq_XElement`
- `System_Xml_Linq_XName`
- `System_Xml_Linq_XNamespace`
- `System_Xml_Linq_XObject`
- `System_Xml_Linq_XProcessingInstruction`
- `System_Security_UnverifiableCodeAttribute`
- `System_Security_Permissions_SecurityAction`
- `System_Security_Permissions_SecurityAttribute`
- `System_Security_Permissions_SecurityPermissionAttribute`
- `System_NotSupportedException`
- `System_Runtime_CompilerServices_ICriticalNotifyCompletion`
- `System_Runtime_CompilerServices_IAsyncStateMachine`
- `System_Runtime_CompilerServices_AsyncVoidMethodBuilder`
- `System_Runtime_CompilerServices_AsyncTaskMethodBuilder`
- `System_Runtime_CompilerServices_AsyncTaskMethodBuilder_T`
- `System_Runtime_CompilerServices_AsyncStateMachineAttribute`
- `System_Runtime_CompilerServices_IteratorStateMachineAttribute`
- `System_Windows_Forms_Form`
- `System_Windows_Forms_Application`
- `System_Environment`
- `System_Runtime_GCLatencyMode`
- `System_IFormatProvider`
- `System_ValueTuple_T1`
- `System_ValueTuple_T2`
- `System_ValueTuple_T3`
- `System_ValueTuple_T4`
- `System_ValueTuple_T5`
- `System_ValueTuple_T6`
- `System_ValueTuple_T7`
- `System_ValueTuple_TRest`
- `System_Runtime_CompilerServices_TupleElementNamesAttribute`
- `System_Runtime_CompilerServices_ReferenceAssemblyAttribute`
- `System_ContextBoundObject`
- `System_Runtime_CompilerServices_TypeForwardedToAttribute`
- `System_Runtime_InteropServices_ComImportAttribute`
- `System_Runtime_InteropServices_DllImportAttribute`
- `System_Runtime_InteropServices_FieldOffsetAttribute`
- `System_Runtime_InteropServices_InAttribute`
- `System_Runtime_InteropServices_MarshalAsAttribute`
- `System_Runtime_InteropServices_OptionalAttribute`
- `System_Runtime_InteropServices_OutAttribute`
- `System_Runtime_InteropServices_PreserveSigAttribute`
- `System_SerializableAttribute`
- `System_Runtime_InteropServices_CharSet`
- `System_Reflection_Assembly`
- `System_RuntimeMethodHandleInternal`
- `System_ByReference_T`
- `System_Runtime_InteropServices_UnmanagedType`
- `System_Runtime_InteropServices_VarEnum`
- `System___ComObject`
- `System_Runtime_InteropServices_WindowsRuntime_RuntimeClass`
- `System_DBNull`
- `System_Security_Permissions_PermissionSetAttribute`
- `System_Diagnostics_Debugger_CrossThreadDependencyNotification`
- `System_Diagnostics_DebuggerTypeProxyAttribute`
- `System_Collections_Generic_KeyValuePair_T2`
- `System_Linq_SystemCore_EnumerableDebugView`
- `System_Linq_SystemCore_EnumerableDebugView_T`
- `System_Text_Encoding`
- `System_Runtime_CompilerServices_IsReadOnlyAttribute`
- `System_Runtime_CompilerServices_IsByRefLikeAttribute`
- `System_ObsoleteAttribute`
- `System_Span_T`
- `System_Runtime_InteropServices_GCHandle`
- `System_Runtime_CompilerServices_NullableAttribute`
- `System_ReadOnlySpan_T`
- `System_Runtime_CompilerServices_IsUnmanagedAttribute`
- `Microsoft_VisualBasic_Conversion`
- `System_Index`
- `System_Range`
- `System_Runtime_CompilerServices_AsyncIteratorStateMachineAttribute`
- `System_IAsyncDisposable`
- `System_Collections_Generic_IAsyncEnumerable_T`
- `System_Collections_Generic_IAsyncEnumerator_T`
- `System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_T`
- `System_Threading_Tasks_Sources_ValueTaskSourceStatus`
- `System_Threading_Tasks_Sources_ValueTaskSourceOnCompletedFlags`
- `System_Threading_Tasks_Sources_IValueTaskSource_T`
- `System_Threading_Tasks_Sources_IValueTaskSource`
- `System_Threading_Tasks_ValueTask_T`
- `System_Threading_Tasks_ValueTask`
- `System_Runtime_CompilerServices_AsyncIteratorMethodBuilder`
- `System_Threading_CancellationToken`
- `None` = `1`

## Class `DmdWellKnownTypeUtils`

utils

**Example**

```csharp
// Access dnSpy.Debugger.DotNet.Metadata.DmdWellKnownTypeUtils members directly without instantiation.
dnSpy.Debugger.DotNet.Metadata.DmdWellKnownTypeUtils./* member */
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdWellKnownTypeUtils.cs` (line 27)

### Methods

- `public static DmdTypeName GetTypeName(DmdWellKnownType wellKnownType)`
  - Summary: Gets the name
  - Parameters:
    - `DmdWellKnownType wellKnownType`: Well known type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdWellKnownTypeUtils.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Metadata.DmdWellKnownTypeUtils.GetTypeName(wellKnownType: /* DmdWellKnownType */);
    ```
- `public static bool TryGetWellKnownType(in DmdTypeName name, out DmdWellKnownType wellKnownType)`
  - Summary: Gets the well known type
  - Parameters:
    - `in DmdTypeName name`: Name
    - `out DmdWellKnownType wellKnownType`: Updated with well known type if successful
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdWellKnownTypeUtils.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Debugger.DotNet.Metadata.DmdWellKnownTypeUtils.TryGetWellKnownType(name: /* DmdTypeName */, wellKnownType: /* DmdWellKnownType */);
    ```

### Properties

- `public static int WellKnownTypesCount => 305`
  - Summary: Gets the number of well known types
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/DmdWellKnownTypeUtils.cs` (line 59)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Metadata.DmdWellKnownTypeUtils.WellKnownTypesCount;
    ```

## Class `EventNotFoundException`

Thrown when an event couldn't be found

**Inherits/Implements:** `MemberNotFoundException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.EventNotFoundException(eventName: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 86)

### Constructors

- `public EventNotFoundException(string eventName)`
  - Summary: Constructor
  - Parameters:
    - `string eventName`: Event that couldn't be found
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 92)

## Class `FieldNotFoundException`

Thrown when a field couldn't be found

**Inherits/Implements:** `MemberNotFoundException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.FieldNotFoundException(fieldName: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 50)

### Constructors

- `public FieldNotFoundException(string fieldName)`
  - Summary: Constructor
  - Parameters:
    - `string fieldName`: Field that couldn't be found
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 56)

## Class `FieldResolveException`

Thrown when a field couldn't be resolved

**Inherits/Implements:** `ResolveException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.FieldResolveException(field: /* DmdFieldInfo */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 55)

### Constructors

- `public FieldResolveException(DmdFieldInfo field)`
  - Summary: Constructor
  - Parameters:
    - `DmdFieldInfo field`: Field that couldn't be resolved
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 66)

### Properties

- `public DmdFieldInfo Field { get; }`
  - Summary: Gets the field that couldn't be resolved
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Field;
    ```

## Interface `IDmdAssemblyName`

A read only assembly name

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.IDmdAssemblyName and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.IDmdAssemblyName(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 27)

### Methods

- `DmdReadOnlyAssemblyName AsReadOnly()`
  - Summary: Creates a read only assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.AsReadOnly();
    ```
- `byte[] GetPublicKey()`
  - Summary: Gets the public key
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPublicKey();
    ```
- `byte[] GetPublicKeyToken()`
  - Summary: Gets the public key token
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.GetPublicKeyToken();
    ```

### Properties

- `DmdAssemblyContentType ContentType { get; }`
  - Summary: Gets the content type
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentType;
    ```
- `DmdAssemblyHashAlgorithm HashAlgorithm { get; }`
  - Summary: Gets the hash algorithm
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HashAlgorithm;
    ```
- `DmdAssemblyNameFlags Flags { get; }`
  - Summary: Gets the flags. The content type and processor architecture bits are ignored, use instead
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `DmdAssemblyNameFlags RawFlags { get; }`
  - Summary: Gets the flags
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RawFlags;
    ```
- `DmdProcessorArchitecture ProcessorArchitecture { get; }`
  - Summary: Gets the processor architecture
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProcessorArchitecture;
    ```
- `Version Version { get; }`
  - Summary: Gets the version
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Version;
    ```
- `string CultureName { get; }`
  - Summary: Gets the culture name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CultureName;
    ```
- `string FullName { get; }`
  - Summary: Gets the full assembly name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FullName;
    ```
- `string Name { get; }`
  - Summary: Gets the simple name
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdAssemblyName.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `IDmdCustomAttributeProvider`

Implemented by classes that can have custom attributes, eg. types, members, parameters, assemblies, modules

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.IDmdCustomAttributeProvider and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.IDmdCustomAttributeProvider(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdCustomAttributeProvider.cs` (line 27)

### Methods

- `DmdCustomAttributeData FindCustomAttribute(DmdType attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdCustomAttributeProvider.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `DmdCustomAttributeData FindCustomAttribute(Type attributeType, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `Type attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdCustomAttributeProvider.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeType: /* Type */, inherit: /* bool */);
    ```
- `DmdCustomAttributeData FindCustomAttribute(string attributeTypeFullName, bool inherit)`
  - Summary: Finds a custom attribute
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdCustomAttributeProvider.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.FindCustomAttribute(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```
- `ReadOnlyCollection<DmdCustomAttributeData> GetCustomAttributesData()`
  - Summary: Gets the custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdCustomAttributeProvider.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetCustomAttributesData();
    ```
- `bool IsDefined(DmdType attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `DmdType attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdCustomAttributeProvider.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* DmdType */, inherit: /* bool */);
    ```
- `bool IsDefined(Type attributeType, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `Type attributeType`: Custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdCustomAttributeProvider.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeType: /* Type */, inherit: /* bool */);
    ```
- `bool IsDefined(string attributeTypeFullName, bool inherit)`
  - Summary: Checks if a custom attribute is present
  - Parameters:
    - `string attributeTypeFullName`: Full name of the custom attribute type
    - `bool inherit`: true to check custom attributes in all base classes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdCustomAttributeProvider.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.IsDefined(attributeTypeFullName: /* string */, inherit: /* bool */);
    ```

### Properties

- `ReadOnlyCollection<DmdCustomAttributeData> CustomAttributes { get; }`
  - Summary: Gets the custom attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdCustomAttributeProvider.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CustomAttributes;
    ```

## Interface `IDmdSecurityAttributeProvider`

Implemented by classes that can have security attributes, eg. assemblies, types, constructors, methods

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Metadata.IDmdSecurityAttributeProvider and call its members.
var instance = new dnSpy.Debugger.DotNet.Metadata.IDmdSecurityAttributeProvider(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdSecurityAttributeProvider.cs` (line 26)

### Methods

- `ReadOnlyCollection<DmdCustomAttributeData> GetSecurityAttributesData()`
  - Summary: Gets the security attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdSecurityAttributeProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSecurityAttributesData();
    ```

### Properties

- `ReadOnlyCollection<DmdCustomAttributeData> SecurityAttributes { get; }`
  - Summary: Gets the security attributes
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/IDmdSecurityAttributeProvider.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SecurityAttributes;
    ```

## Class `MemberNotFoundException`

Thrown when a type or a member couldn't be found

**Inherits/Implements:** `Exception`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.MemberNotFoundException(message: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 26)

### Constructors

- `public MemberNotFoundException(string message)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 32)

## Class `MethodNotFoundException`

Thrown when a method couldn't be found

**Inherits/Implements:** `MemberNotFoundException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.MethodNotFoundException(methodName: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 62)

### Constructors

- `public MethodNotFoundException(string methodName)`
  - Summary: Constructor
  - Parameters:
    - `string methodName`: Method that couldn't be found
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 68)

## Class `MethodResolveException`

Thrown when a method couldn't be resolved

**Inherits/Implements:** `ResolveException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.MethodResolveException(method: /* DmdMethodBase */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 72)

### Constructors

- `public MethodResolveException(DmdMethodBase method)`
  - Summary: Constructor
  - Parameters:
    - `DmdMethodBase method`: Method that couldn't be resolved
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 83)

### Properties

- `public DmdMethodBase Method { get; }`
  - Summary: Gets the method that couldn't be resolved
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Method;
    ```

## Class `PropertyNotFoundException`

Thrown when a property couldn't be found

**Inherits/Implements:** `MemberNotFoundException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.PropertyNotFoundException(propertyName: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 74)

### Constructors

- `public PropertyNotFoundException(string propertyName)`
  - Summary: Constructor
  - Parameters:
    - `string propertyName`: Property that couldn't be found
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 80)

## Class `ResolveException`

Thrown when a type or member couldn't be resolved

**Inherits/Implements:** `Exception`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.ResolveException(message: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 26)

### Constructors

- `public ResolveException(string message)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 32)

## Class `TypeNotFoundException`

Thrown when a type couldn't be found

**Inherits/Implements:** `MemberNotFoundException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.TypeNotFoundException(typeName: /* string */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 38)

### Constructors

- `public TypeNotFoundException(string typeName)`
  - Summary: Constructor
  - Parameters:
    - `string typeName`: Type that couldn't be found
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/MemberNotFoundException.cs` (line 44)

## Class `TypeResolveException`

Thrown when a type couldn't be resolved

**Inherits/Implements:** `ResolveException`

**Example**

```csharp
var instance = new dnSpy.Debugger.DotNet.Metadata.TypeResolveException(type: /* DmdType */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 38)

### Constructors

- `public TypeResolveException(DmdType type)`
  - Summary: Constructor
  - Parameters:
    - `DmdType type`: Type that couldn't be resolved
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 49)

### Properties

- `public DmdType Type { get; }`
  - Summary: Gets the type that couldn't be resolved
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Metadata/ResolveException.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```

