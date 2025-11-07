# Namespace `dnSpy.Decompiler`

## Class `DecompilerBase`

Base class for language-specific decompiler implementations.

**Inherits/Implements:** `IDecompiler`

**Example**

```csharp
// Instantiate dnSpy.Decompiler.DecompilerBase and call its members.
var instance = new dnSpy.Decompiler.DecompilerBase(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 35)

### Methods

- `protected static string GetPlatformDisplayName(ModuleDef module)`
  - Parameters:
    - `ModuleDef module`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 247)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Decompiler.DecompilerBase.GetPlatformDisplayName(module: /* ModuleDef */);
    ```
- `protected static string GetRuntimeDisplayName(ModuleDef module)`
  - Parameters:
    - `ModuleDef module`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 248)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Decompiler.DecompilerBase.GetRuntimeDisplayName(module: /* ModuleDef */);
    ```
- `protected virtual void FormatPropertyName(IDecompilerOutput output, PropertyDef property, bool? isIndexer = null)`
  - Parameters:
    - `IDecompilerOutput output`: Description not provided.
    - `PropertyDef property`: Description not provided.
    - `bool? isIndexer` (default: `null`): Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 234)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatPropertyName(output: /* IDecompilerOutput */, property: /* PropertyDef */, isIndexer: /* bool? */);
    ```
- `protected virtual void FormatTypeName(IDecompilerOutput output, TypeDef type)`
  - Parameters:
    - `IDecompilerOutput output`: Description not provided.
    - `TypeDef type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 240)
  - Example:
    ```csharp
    // Example invocation
    instance.FormatTypeName(output: /* IDecompilerOutput */, type: /* TypeDef */);
    ```
- `protected virtual void TypeToString(IDecompilerOutput output, ITypeDefOrRef type, bool includeNamespace, IHasCustomAttribute typeAttributes = null)`
  - Parameters:
    - `IDecompilerOutput output`: Description not provided.
    - `ITypeDefOrRef type`: Description not provided.
    - `bool includeNamespace`: Description not provided.
    - `IHasCustomAttribute typeAttributes` (default: `null`): Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 215)
  - Example:
    ```csharp
    // Example invocation
    instance.TypeToString(output: /* IDecompilerOutput */, type: /* ITypeDefOrRef */, includeNamespace: /* bool */, typeAttributes: /* IHasCustomAttribute */);
    ```
- `protected void PrintEntryPoint(ModuleDef mod, IDecompilerOutput output)`
  - Parameters:
    - `ModuleDef mod`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 150)
  - Example:
    ```csharp
    // Example invocation
    instance.PrintEntryPoint(mod: /* ModuleDef */, output: /* IDecompilerOutput */);
    ```
- `protected void WriteAssembly(AssemblyDef asm, IDecompilerOutput output, DecompilationContext ctx)`
  - Parameters:
    - `AssemblyDef asm`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
    - `DecompilationContext ctx`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteAssembly(asm: /* AssemblyDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `protected void WriteCommentLineDeclaringType(IDecompilerOutput output, IMemberDef member)`
  - Parameters:
    - `IDecompilerOutput output`: Description not provided.
    - `IMemberDef member`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteCommentLineDeclaringType(output: /* IDecompilerOutput */, member: /* IMemberDef */);
    ```
- `protected void WriteModule(ModuleDef mod, IDecompilerOutput output, DecompilationContext ctx)`
  - Parameters:
    - `ModuleDef mod`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
    - `DecompilationContext ctx`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 110)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteModule(mod: /* ModuleDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `public virtual bool CanDecompile(DecompilationType decompilationType)`
  - Parameters:
    - `DecompilationType decompilationType`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 249)
  - Example:
    ```csharp
    // Example invocation
    instance.CanDecompile(decompilationType: /* DecompilationType */);
    ```
- `public virtual bool ShowMember(IMemberRef member)`
  - Parameters:
    - `IMemberRef member`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 246)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowMember(member: /* IMemberRef */);
    ```
- `public virtual void Decompile(AssemblyDef asm, IDecompilerOutput output, DecompilationContext ctx)`
  - Parameters:
    - `AssemblyDef asm`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
    - `DecompilationContext ctx`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 134)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(asm: /* AssemblyDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `public virtual void Decompile(DecompilationType decompilationType, object data)`
  - Parameters:
    - `DecompilationType decompilationType`: Description not provided.
    - `object data`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 251)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(decompilationType: /* DecompilationType */, data: /* object */);
    ```
- `public virtual void Decompile(EventDef ev, IDecompilerOutput output, DecompilationContext ctx)`
  - Parameters:
    - `EventDef ev`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
    - `DecompilationContext ctx`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(ev: /* EventDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `public virtual void Decompile(FieldDef field, IDecompilerOutput output, DecompilationContext ctx)`
  - Parameters:
    - `FieldDef field`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
    - `DecompilationContext ctx`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(field: /* FieldDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `public virtual void Decompile(MethodDef method, IDecompilerOutput output, DecompilationContext ctx)`
  - Parameters:
    - `MethodDef method`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
    - `DecompilationContext ctx`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(method: /* MethodDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `public virtual void Decompile(ModuleDef mod, IDecompilerOutput output, DecompilationContext ctx)`
  - Parameters:
    - `ModuleDef mod`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
    - `DecompilationContext ctx`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(mod: /* ModuleDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `public virtual void Decompile(PropertyDef property, IDecompilerOutput output, DecompilationContext ctx)`
  - Parameters:
    - `PropertyDef property`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
    - `DecompilationContext ctx`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(property: /* PropertyDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `public virtual void Decompile(TypeDef type, IDecompilerOutput output, DecompilationContext ctx)`
  - Parameters:
    - `TypeDef type`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
    - `DecompilationContext ctx`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(type: /* TypeDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `public virtual void DecompileNamespace(string @namespace, IEnumerable<TypeDef> types, IDecompilerOutput output, DecompilationContext ctx)`
  - Parameters:
    - `string @namespace`: Description not provided.
    - `IEnumerable<TypeDef> types`: Description not provided.
    - `IDecompilerOutput output`: Description not provided.
    - `DecompilationContext ctx`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.DecompileNamespace(@namespace: /* string */, types: /* IEnumerable<TypeDef> */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `public virtual void Write(ITextColorWriter output, IMemberRef member, FormatterOptions flags)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `IMemberRef member`: Description not provided.
    - `FormatterOptions flags`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 231)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, member: /* IMemberRef */, flags: /* FormatterOptions */);
    ```
- `public virtual void WriteCommentBegin(IDecompilerOutput output, bool addSpace)`
  - Parameters:
    - `IDecompilerOutput output`: Description not provided.
    - `bool addSpace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 200)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteCommentBegin(output: /* IDecompilerOutput */, addSpace: /* bool */);
    ```
- `public virtual void WriteCommentEnd(IDecompilerOutput output, bool addSpace)`
  - Parameters:
    - `IDecompilerOutput output`: Description not provided.
    - `bool addSpace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 207)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteCommentEnd(output: /* IDecompilerOutput */, addSpace: /* bool */);
    ```
- `public virtual void WriteNamespaceToolTip(ITextColorWriter output, string @namespace)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 229)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteNamespaceToolTip(output: /* ITextColorWriter */, @namespace: /* string */);
    ```
- `public virtual void WriteToolTip(ITextColorWriter output, IMemberRef member, IHasCustomAttribute typeAttributes)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `IMemberRef member`: Description not provided.
    - `IHasCustomAttribute typeAttributes`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 225)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteToolTip(output: /* ITextColorWriter */, member: /* IMemberRef */, typeAttributes: /* IHasCustomAttribute */);
    ```
- `public virtual void WriteToolTip(ITextColorWriter output, ISourceVariable variable)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `ISourceVariable variable`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 227)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteToolTip(output: /* ITextColorWriter */, variable: /* ISourceVariable */);
    ```
- `public void WriteName(ITextColorWriter output, PropertyDef property, bool? isIndexer)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `PropertyDef property`: Description not provided.
    - `bool? isIndexer`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(output: /* ITextColorWriter */, property: /* PropertyDef */, isIndexer: /* bool? */);
    ```
- `public void WriteName(ITextColorWriter output, TypeDef type)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `TypeDef type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(output: /* ITextColorWriter */, type: /* TypeDef */);
    ```
- `public void WriteType(ITextColorWriter output, ITypeDefOrRef type, bool includeNamespace, ParamDef pd = null)`
  - Parameters:
    - `ITextColorWriter output`: Description not provided.
    - `ITypeDefOrRef type`: Description not provided.
    - `bool includeNamespace`: Description not provided.
    - `ParamDef pd` (default: `null`): Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 49)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteType(output: /* ITextColorWriter */, type: /* ITypeDefOrRef */, includeNamespace: /* bool */, pd: /* ParamDef */);
    ```

### Properties

- `public abstract DecompilerSettingsBase Settings { get; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```
- `public abstract Guid GenericGuid { get; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericGuid;
    ```
- `public abstract Guid UniqueGuid { get; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UniqueGuid;
    ```
- `public abstract double OrderUI { get; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OrderUI;
    ```
- `public abstract string ContentTypeString { get; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentTypeString;
    ```
- `public abstract string FileExtension { get; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FileExtension;
    ```
- `public abstract string GenericNameUI { get; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericNameUI;
    ```
- `public abstract string UniqueNameUI { get; }`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UniqueNameUI;
    ```
- `public virtual MetadataTextColorProvider MetadataTextColorProvider => CSharpMetadataTextColorProvider.Instance`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataTextColorProvider;
    ```
- `public virtual string ProjectFileExtension => null`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProjectFileExtension;
    ```

### Fields

- `protected const FormatterOptions DefaultFormatterOptions = FormatterOptions.Default | FormatterOptions.ShowParameterLiteralValues`
  - Defined in: `dnSpy/dnSpy.Decompiler/DecompilerBase.cs` (line 224)
  - Example:
    ```csharp
    var value = instance.DefaultFormatterOptions;
    ```

## Class `FilenameUtils`

**Example**

```csharp
// Access dnSpy.Decompiler.FilenameUtils members directly without instantiation.
dnSpy.Decompiler.FilenameUtils./* member */
```

*Defined in* `dnSpy/dnSpy.Decompiler/FilenameUtils.cs` (line 25)

### Methods

- `public static string CleanName(string text)`
  - Parameters:
    - `string text`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Decompiler/FilenameUtils.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Decompiler.FilenameUtils.CleanName(text: /* string */);
    ```

