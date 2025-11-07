# Namespace `dnSpy.Contracts.AsmEditor.Compiler`

## Enum `CompilationKind`

Compilation kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.AsmEditor.Compiler.CompilationKind and call its members.
var instance = new dnSpy.Contracts.AsmEditor.Compiler.CompilationKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilationKind.cs` (line 24)

### Members

- `EditAssembly`: Edit assembly and module attributes
- `EditMethod`: Edit method
- `AddClass`: Add class
- `EditClass`: Edit an existing class
- `AddMembers`: Add members

## Struct `CompilationResult`

Compilation result

**Example**

```csharp
var instance = new dnSpy.Contracts.AsmEditor.Compiler.CompilationResult(rawFile: /* byte[] */, debugFile: /* DebugFileResult? */, diagnostics: /* CompilerDiagnostic[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilationResult.cs` (line 27)

### Constructors

- `public CompilationResult(CompilerDiagnostic[] diagnostics)`
  - Summary: Constructor
  - Parameters:
    - `CompilerDiagnostic[] diagnostics`: Diagnostics
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilationResult.cs` (line 64)
- `public CompilationResult(byte[] rawFile, DebugFileResult? debugFile = null, CompilerDiagnostic[] diagnostics = null)`
  - Summary: Constructor
  - Parameters:
    - `byte[] rawFile`: Raw file data
    - `DebugFileResult? debugFile` (default: `null`): Debug file result or null
    - `CompilerDiagnostic[] diagnostics` (default: `null`): Diagnostics or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilationResult.cs` (line 54)

### Properties

- `public CompilerDiagnostic[] Diagnostics { get; }`
  - Summary: Gets the diagnostics
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilationResult.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Diagnostics;
    ```
- `public DebugFileResult DebugFile { get; }`
  - Summary: Debug file data (eg. PDB data)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilationResult.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DebugFile;
    ```
- `public bool Success => RawFile != null`
  - Summary: true if the compilation succeeded
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilationResult.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Success;
    ```
- `public byte[] RawFile { get; }`
  - Summary: Result of compilation or null if compilation failed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilationResult.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RawFile;
    ```

## Class `CompilerDiagnostic`

Compiler diagnostic

**Example**

```csharp
var instance = new dnSpy.Contracts.AsmEditor.Compiler.CompilerDiagnostic(severity: /* CompilerDiagnosticSeverity */, description: /* string */, id: /* string */, helpUri: /* string */, filename: /* string */, lineLocationSpan: /* LineLocationSpan? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDiagnostic.cs` (line 27)

### Constructors

- `public CompilerDiagnostic(CompilerDiagnosticSeverity severity, string description, string id, string helpUri, string filename, LineLocationSpan? lineLocationSpan)`
  - Summary: Constructor
  - Parameters:
    - `CompilerDiagnosticSeverity severity`: Severity
    - `string description`: Description
    - `string id`: Id
    - `string helpUri`: Help URI or null if none
    - `string filename`: Filename
    - `LineLocationSpan? lineLocationSpan`: Line location or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDiagnostic.cs` (line 67)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDiagnostic.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public CompilerDiagnosticSeverity Severity { get; }`
  - Summary: Gets the severity
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDiagnostic.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Severity;
    ```
- `public LineLocationSpan? LineLocationSpan { get; }`
  - Summary: Location in the file or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDiagnostic.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LineLocationSpan;
    ```
- `public string Description { get; }`
  - Summary: Description
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDiagnostic.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Description;
    ```
- `public string Filename { get; }`
  - Summary: Filename or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDiagnostic.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public string HelpUri { get; }`
  - Summary: Gets the help URI or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDiagnostic.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HelpUri;
    ```
- `public string Id { get; }`
  - Summary: Id, eg. CS0001
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDiagnostic.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Enum `CompilerDiagnosticSeverity`

Severity

**Example**

```csharp
// Instantiate dnSpy.Contracts.AsmEditor.Compiler.CompilerDiagnosticSeverity and call its members.
var instance = new dnSpy.Contracts.AsmEditor.Compiler.CompilerDiagnosticSeverity(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDiagnosticSeverity.cs` (line 24)

### Members

- `Hidden`: Hidden
- `Info`: Info
- `Warning`: Warning
- `Error`: Error

## Struct `CompilerDocumentInfo`

Document info

**Example**

```csharp
var instance = new dnSpy.Contracts.AsmEditor.Compiler.CompilerDocumentInfo(code: /* string */, name: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDocumentInfo.cs` (line 26)

### Constructors

- `public CompilerDocumentInfo(string code, string name)`
  - Summary: Constructor
  - Parameters:
    - `string code`: All code
    - `string name`: Name of document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDocumentInfo.cs` (line 42)

### Properties

- `public string Code { get; }`
  - Summary: All code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDocumentInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Code;
    ```
- `public string Name { get; }`
  - Summary: Name of document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerDocumentInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Struct `CompilerMetadataReference`

Metadata reference

**Example**

```csharp
// Instantiate dnSpy.Contracts.AsmEditor.Compiler.CompilerMetadataReference and call its members.
var instance = new dnSpy.Contracts.AsmEditor.Compiler.CompilerMetadataReference(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerMetadataReference.cs` (line 27)

### Methods

- `public static CompilerMetadataReference CreateAssemblyReference(void* data, int size, IAssembly assembly, string filename = null)`
  - Summary: Creates an assembly metadata reference
  - Parameters:
    - `void* data`: File data
    - `int size`: Size of data
    - `IAssembly assembly`: Assembly owner or null
    - `string filename` (default: `null`): Filename or null if it doesn't exist on disk
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerMetadataReference.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.AsmEditor.Compiler.CompilerMetadataReference.CreateAssemblyReference(data: /* void* */, size: /* int */, assembly: /* IAssembly */, filename: /* string */);
    ```
- `public static CompilerMetadataReference CreateModuleReference(void* data, int size, IAssembly assembly, string filename = null)`
  - Summary: Creates a module metadata reference
  - Parameters:
    - `void* data`: File data
    - `int size`: Size of data
    - `IAssembly assembly`: Assembly owner or null
    - `string filename` (default: `null`): Filename or null if it doesn't exist on disk
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerMetadataReference.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.AsmEditor.Compiler.CompilerMetadataReference.CreateModuleReference(data: /* void* */, size: /* int */, assembly: /* IAssembly */, filename: /* string */);
    ```

### Properties

- `public IAssembly Assembly { get; }`
  - Summary: Gets the assembly or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerMetadataReference.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Assembly;
    ```
- `public bool IsAssemblyReference { get; }`
  - Summary: true if it's an assembly reference, false if it's a module reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerMetadataReference.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsAssemblyReference;
    ```
- `public int Size { get; }`
  - Summary: Gets the size of
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerMetadataReference.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Size;
    ```
- `public string Filename { get; }`
  - Summary: Gets the filename or null if it doesn't exist on disk
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerMetadataReference.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public void* Data { get; }`
  - Summary: Raw bytes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerMetadataReference.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```

## Struct `CompilerProjectInfo`

Project info passed to the compiler

**Example**

```csharp
var instance = new dnSpy.Contracts.AsmEditor.Compiler.CompilerProjectInfo(assemblyName: /* string */, publicKey: /* byte[] */, assemblyReferences: /* CompilerMetadataReference[] */, assemblyReferenceResolver: /* IAssemblyReferenceResolver */, platform: /* TargetPlatform */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerProjectInfo.cs` (line 26)

### Constructors

- `public CompilerProjectInfo(string assemblyName, byte[] publicKey, CompilerMetadataReference[] assemblyReferences, IAssemblyReferenceResolver assemblyReferenceResolver, TargetPlatform platform)`
  - Summary: Constructor
  - Parameters:
    - `string assemblyName`: Name of the edited assembly. It's only the simple name (eg. "MyAssembly"), and doesn't contain the public key token, version, etc
    - `byte[] publicKey`: The public key or null if none
    - `CompilerMetadataReference[] assemblyReferences`: Assembly and module references
    - `IAssemblyReferenceResolver assemblyReferenceResolver`: Reference resolver
    - `TargetPlatform platform`: Platform
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerProjectInfo.cs` (line 60)

### Properties

- `public CompilerMetadataReference[] AssemblyReferences { get; }`
  - Summary: Assembly and module references
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerProjectInfo.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyReferences;
    ```
- `public IAssemblyReferenceResolver AssemblyReferenceResolver { get; }`
  - Summary: Reference resolver
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerProjectInfo.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyReferenceResolver;
    ```
- `public TargetPlatform Platform { get; }`
  - Summary: Platform
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerProjectInfo.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Platform;
    ```
- `public byte[] PublicKey { get; }`
  - Summary: The public key or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerProjectInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.PublicKey;
    ```
- `public string AssemblyName { get; }`
  - Summary: Name of the edited assembly. It's only the simple name (eg. "MyAssembly"), and doesn't contain the public key token, version, etc
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/CompilerProjectInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AssemblyName;
    ```

## Enum `DebugFileFormat`

Debug file format

**Example**

```csharp
// Instantiate dnSpy.Contracts.AsmEditor.Compiler.DebugFileFormat and call its members.
var instance = new dnSpy.Contracts.AsmEditor.Compiler.DebugFileFormat(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/DebugFileFormat.cs` (line 24)

### Members

- `None`: None
- `Pdb`: PDB
- `PortablePdb`: Portable PDB
- `Embedded`: embedded in metadata

## Struct `DebugFileResult`

PDB file

**Example**

```csharp
var instance = new dnSpy.Contracts.AsmEditor.Compiler.DebugFileResult(format: /* DebugFileFormat */, rawFile: /* byte[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/DebugFileResult.cs` (line 24)

### Constructors

- `public DebugFileResult(DebugFileFormat format, byte[] rawFile)`
  - Summary: Constructor
  - Parameters:
    - `DebugFileFormat format`: Debug file format
    - `byte[] rawFile`: Debug file data or null if it's an embedded PDB file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/DebugFileResult.cs` (line 40)

### Properties

- `public DebugFileFormat Format { get; }`
  - Summary: Debug file format
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/DebugFileResult.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Format;
    ```
- `public byte[] RawFile { get; }`
  - Summary: PDB file or null if it's an embedded PDB file
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/DebugFileResult.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RawFile;
    ```

## Interface `IAssemblyReferenceResolver`

Resolves assemblies

**Example**

```csharp
// Instantiate dnSpy.Contracts.AsmEditor.Compiler.IAssemblyReferenceResolver and call its members.
var instance = new dnSpy.Contracts.AsmEditor.Compiler.IAssemblyReferenceResolver(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/IAssemblyReferenceResolver.cs` (line 26)

### Methods

- `CompilerMetadataReference? Resolve(IAssembly asmRef)`
  - Summary: Resolves a reference
  - Parameters:
    - `IAssembly asmRef`: Assembly reference
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/IAssemblyReferenceResolver.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve(asmRef: /* IAssembly */);
    ```

## Interface `ICodeDocument`

Code document

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.AsmEditor.Compiler.ICodeDocument and call its members.
var instance = new dnSpy.Contracts.AsmEditor.Compiler.ICodeDocument(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ICodeDocument.cs` (line 27)

### Properties

- `IDsWpfTextView TextView { get; }`
  - Summary: Gets the text view
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ICodeDocument.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextView;
    ```
- `IDsWpfTextViewHost TextViewHost { get; }`
  - Summary: Gets the text view host
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ICodeDocument.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextViewHost;
    ```
- `string Name { get; }`
  - Summary: Name of document
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ICodeDocument.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `ILanguageCompiler`

Compiles source code

**Inherits/Implements:** `IDisposable`

**Example**

```csharp
// Instantiate dnSpy.Contracts.AsmEditor.Compiler.ILanguageCompiler and call its members.
var instance = new dnSpy.Contracts.AsmEditor.Compiler.ILanguageCompiler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompiler.cs` (line 30)

### Methods

- `ICodeDocument[] AddDocuments(CompilerDocumentInfo[] documents)`
  - Summary: Adds more documents
  - Parameters:
    - `CompilerDocumentInfo[] documents`: Documents to add to the compilation
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompiler.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.AddDocuments(documents: /* CompilerDocumentInfo[] */);
    ```
- `IEnumerable<string> GetRequiredAssemblyReferences(ModuleDef editedModule)`
  - Summary: Assembly references that must be included when compiling the code, even if the references aren't part of the edited assembly. This is usually empty unless the language uses types from certain language specific assemblies, eg. Visual Basic usually needs Microsoft.VisualBasic.
  - Parameters:
    - `ModuleDef editedModule`: The module the user is editing
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompiler.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    instance.GetRequiredAssemblyReferences(editedModule: /* ModuleDef */);
    ```
- `Task<CompilationResult> CompileAsync(CancellationToken cancellationToken)`
  - Summary: Compiles the code
  - Parameters:
    - `CancellationToken cancellationToken`: Cancellation token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompiler.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.CompileAsync(cancellationToken: /* CancellationToken */);
    ```
- `bool AddMetadataReferences(CompilerMetadataReference[] metadataReferences)`
  - Summary: Adds new metadata references
  - Parameters:
    - `CompilerMetadataReference[] metadataReferences`: Metadata references
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompiler.cs` (line 71)
  - Example:
    ```csharp
    // Example invocation
    instance.AddMetadataReferences(metadataReferences: /* CompilerMetadataReference[] */);
    ```
- `void InitializeProject(CompilerProjectInfo projectInfo)`
  - Summary: Initializes the project
  - Parameters:
    - `CompilerProjectInfo projectInfo`: Project info
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompiler.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.InitializeProject(projectInfo: /* CompilerProjectInfo */);
    ```

### Properties

- `string FileExtension { get; }`
  - Summary: Gets the file extension, including the period, eg. ".cs"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompiler.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FileExtension;
    ```

## Interface `ILanguageCompilerProvider`

Creates instances

**Example**

```csharp
// Instantiate dnSpy.Contracts.AsmEditor.Compiler.ILanguageCompilerProvider and call its members.
var instance = new dnSpy.Contracts.AsmEditor.Compiler.ILanguageCompilerProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompilerProvider.cs` (line 28)

### Methods

- `ILanguageCompiler Create(CompilationKind kind)`
  - Summary: Creates a new instance
  - Parameters:
    - `CompilationKind kind`: Compilation kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompilerProvider.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.Create(kind: /* CompilationKind */);
    ```
- `bool CanCompile(CompilationKind kind)`
  - Summary: Returns true if it supports
  - Parameters:
    - `CompilationKind kind`: Compilation kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompilerProvider.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.CanCompile(kind: /* CompilationKind */);
    ```

### Properties

- `Guid Language { get; }`
  - Summary: Language it supports, eg. . This property is compared against .
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompilerProvider.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Language;
    ```
- `ImageReference? Icon { get; }`
  - Summary: Gets the icon shown in menus or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompilerProvider.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Icon;
    ```
- `double Order { get; }`
  - Summary: Order of this provider
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/ILanguageCompilerProvider.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Struct `LineLocation`

Line location

**Example**

```csharp
var instance = new dnSpy.Contracts.AsmEditor.Compiler.LineLocation(line: /* int */, character: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/LineLocation.cs` (line 26)

### Constructors

- `public LineLocation(int line, int character)`
  - Summary: Constructor
  - Parameters:
    - `int line`: Line, 0-based
    - `int character`: Column, 0-based
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/LineLocation.cs` (line 42)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/LineLocation.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public int Character { get; }`
  - Summary: Column, 0-based
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/LineLocation.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Character;
    ```
- `public int Line { get; }`
  - Summary: Line, 0-based
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/LineLocation.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Line;
    ```

## Struct `LineLocationSpan`

Line location span

**Example**

```csharp
var instance = new dnSpy.Contracts.AsmEditor.Compiler.LineLocationSpan(startLinePosition: /* LineLocation */, endLinePosition: /* LineLocation */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/LineLocationSpan.cs` (line 24)

### Constructors

- `public LineLocationSpan(LineLocation startLinePosition, LineLocation endLinePosition)`
  - Summary: Constructor
  - Parameters:
    - `LineLocation startLinePosition`: Start line position
    - `LineLocation endLinePosition`: End line position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/LineLocationSpan.cs` (line 40)

### Methods

- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/LineLocationSpan.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public LineLocation EndLinePosition { get; }`
  - Summary: End line position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/LineLocationSpan.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EndLinePosition;
    ```
- `public LineLocation StartLinePosition { get; }`
  - Summary: Start line position
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/LineLocationSpan.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StartLinePosition;
    ```

## Enum `TargetPlatform`

Platform

**Example**

```csharp
// Instantiate dnSpy.Contracts.AsmEditor.Compiler.TargetPlatform and call its members.
var instance = new dnSpy.Contracts.AsmEditor.Compiler.TargetPlatform(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/AsmEditor/Compiler/TargetPlatform.cs` (line 24)

### Members

- `AnyCpu`: Any CPU
- `X86`: x86
- `X64`: x64
- `Itanium`: IA-64
- `AnyCpu32BitPreferred`: Any CPU, but prefer 32-bit
- `Arm`: ARM
- `Arm64`: ARM64

