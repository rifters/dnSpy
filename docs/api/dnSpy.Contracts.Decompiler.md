# Namespace `dnSpy.Contracts.Decompiler`

## Class `AddressReference`

An address reference

**Inherits/Implements:** `IEquatable<AddressReference>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.AddressReference(filename: /* string */, isRva: /* bool */, address: /* ulong */, length: /* ulong */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/AddressReference.cs` (line 26)

### Constructors

- `public AddressReference(string filename, bool isRva, ulong address, ulong length)`
  - Summary: Constructor
  - Parameters:
    - `string filename`: Filename
    - `bool isRva`: true if is an RVA, false if it's a file offset
    - `ulong address`: Address
    - `ulong length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AddressReference.cs` (line 54)

### Methods

- `public bool Equals(AddressReference other)`
  - Summary: Equals()
  - Parameters:
    - `AddressReference other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AddressReference.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* AddressReference */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AddressReference.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AddressReference.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public bool IsRVA { get; }`
  - Summary: true if is an RVA, false if it's a file offset
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AddressReference.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsRVA;
    ```
- `public string Filename { get; }`
  - Summary: Filename
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AddressReference.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Filename;
    ```
- `public ulong Address { get; }`
  - Summary: Address, either an RVA or a file offset ()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AddressReference.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```
- `public ulong Length { get; }`
  - Summary: Length of range
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AddressReference.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```

## Class `AsyncMethodDebugInfo`

Async method debug info

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.AsyncMethodDebugInfo(stepInfos: /* AsyncStepInfo[] */, builderField: /* FieldDef */, catchHandlerOffset: /* uint */, setResultOffset: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncMethodDebugInfo.cs` (line 27)

### Constructors

- `public AsyncMethodDebugInfo(AsyncStepInfo[] stepInfos, FieldDef builderField, uint catchHandlerOffset, uint setResultOffset)`
  - Summary: Constructor
  - Parameters:
    - `AsyncStepInfo[] stepInfos`: Async step infos
    - `FieldDef builderField`: Async method builder field or null if it's unknown
    - `uint catchHandlerOffset`: Catch handler offset or . Only used if it's a async void method
    - `uint setResultOffset`: Offset of SetResult() call, or if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncMethodDebugInfo.cs` (line 55)

### Properties

- `public AsyncStepInfo[] StepInfos { get; }`
  - Summary: Async step infos
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncMethodDebugInfo.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StepInfos;
    ```
- `public FieldDef BuilderFieldOrNull { get; }`
  - Summary: Async method builder field or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncMethodDebugInfo.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BuilderFieldOrNull;
    ```
- `public uint CatchHandlerOffset { get; }`
  - Summary: Catch handler offset or . Only used if it's an async void method
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncMethodDebugInfo.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CatchHandlerOffset;
    ```
- `public uint SetResultOffset { get; }`
  - Summary: Offset of SetResult() call, or if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncMethodDebugInfo.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SetResultOffset;
    ```

## Struct `AsyncStepInfo`

Async method step info

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.AsyncStepInfo(yieldOffset: /* uint */, resumeMethod: /* MethodDef */, resumeOffset: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncStepInfo.cs` (line 27)

### Constructors

- `public AsyncStepInfo(uint yieldOffset, MethodDef resumeMethod, uint resumeOffset)`
  - Summary: Constructor
  - Parameters:
    - `uint yieldOffset`: Offset in where it starts waiting for the result
    - `MethodDef resumeMethod`: Resume method
    - `uint resumeOffset`: Offset in where it resumes after the result is available
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncStepInfo.cs` (line 49)

### Properties

- `public MethodDef ResumeMethod { get; }`
  - Summary: Resume method
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncStepInfo.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResumeMethod;
    ```
- `public uint ResumeOffset { get; }`
  - Summary: Offset in where it resumes after the result is available
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncStepInfo.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ResumeOffset;
    ```
- `public uint YieldOffset { get; }`
  - Summary: Offset in method where it starts waiting for the result
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/AsyncStepInfo.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.YieldOffset;
    ```

## Class `BamlDecompilerOptions`

Baml decompiler options

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.BamlDecompilerOptions();
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/BamlDecompilerOptions.cs` (line 24)

### Constructors

- `public BamlDecompilerOptions()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/BamlDecompilerOptions.cs` (line 60)

### Methods

- `public static BamlDecompilerOptions Create(IDecompiler decompiler)`
  - Summary: Creates a new instance
  - Parameters:
    - `IDecompiler decompiler`: Decompiler
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/BamlDecompilerOptions.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.BamlDecompilerOptions.Create(decompiler: /* IDecompiler */);
    ```
- `public static BamlDecompilerOptions CreateCSharp()`
  - Summary: Creates a new instance with C# values
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/BamlDecompilerOptions.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.BamlDecompilerOptions.CreateCSharp();
    ```
- `public static BamlDecompilerOptions CreateVisualBasic()`
  - Summary: Creates a new instance with VB values
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/BamlDecompilerOptions.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.BamlDecompilerOptions.CreateVisualBasic();
    ```

### Properties

- `public string InternalClassModifier { get; set; }`
  - Summary: x:ClassModifier value string when type is internal
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/BamlDecompilerOptions.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InternalClassModifier;
    ```

## Class `CSharpMetadataTextColorProvider`

C# provider

**Inherits/Implements:** `MetadataTextColorProvider`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.CSharpMetadataTextColorProvider and call its members.
var instance = new dnSpy.Contracts.Decompiler.CSharpMetadataTextColorProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 274)

### Fields

- `public static readonly CSharpMetadataTextColorProvider Instance = new CSharpMetadataTextColorProvider()`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 278)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.CSharpMetadataTextColorProvider.Instance;
    ```

## Struct `CodeBracesRange`

Brace pair

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.CodeBracesRange(left: /* TextSpan */, right: /* TextSpan */, flags: /* CodeBracesRangeFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRange.cs` (line 24)

### Constructors

- `public CodeBracesRange(TextSpan left, TextSpan right, CodeBracesRangeFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `TextSpan left`: Span of left brace
    - `TextSpan right`: Span of right brace
    - `CodeBracesRangeFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRange.cs` (line 46)

### Properties

- `public CodeBracesRangeFlags Flags { get; }`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRange.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public TextSpan Left { get; }`
  - Summary: Span of start brace
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRange.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Left;
    ```
- `public TextSpan Right { get; }`
  - Summary: Span of end brace
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRange.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Right;
    ```

## Enum `CodeBracesRangeFlags`

flags, see also

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.CodeBracesRangeFlags and call its members.
var instance = new dnSpy.Contracts.Decompiler.CodeBracesRangeFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRangeFlags.cs` (line 26)

### Members

- `BraceKind_None`
- `BraceKind_Parentheses` = `x00000001`
- `BraceKind_CurlyBraces` = `x00000002`
- `BraceKind_SquareBrackets` = `x00000003`
- `BraceKind_AngleBrackets` = `x00000004`
- `BraceKind_DoubleQuotes` = `x00000005`
- `BraceKind_SingleQuotes` = `x00000006`
- `BraceKind_OtherBraces` = `x00000007`
- `BlockKind_None`
- `BlockKind_Namespace` = `x00000100`
- `BlockKind_Type` = `x00000200`
- `BlockKind_Module` = `x00000300`
- `BlockKind_ValueType` = `x00000400`
- `BlockKind_Interface` = `x00000500`
- `BlockKind_Method` = `x00000600`
- `BlockKind_Accessor` = `x00000700`
- `BlockKind_AnonymousMethod` = `x00000800`
- `BlockKind_Constructor` = `x00000900`
- `BlockKind_Destructor` = `x00000A00`
- `BlockKind_Operator` = `x00000B00`
- `BlockKind_Conditional` = `x00000C00`
- `BlockKind_Loop` = `x00000D00`
- `BlockKind_Property` = `x00000E00`
- `BlockKind_Event` = `x00000F00`
- `BlockKind_Try` = `x00001000`
- `BlockKind_Catch` = `x00001100`
- `BlockKind_Filter` = `x00001200`
- `BlockKind_Finally` = `x00001300`
- `BlockKind_Fault` = `x00001400`
- `BlockKind_Lock` = `x00001500`
- `BlockKind_Using` = `x00001600`
- `BlockKind_Fixed` = `x00001700`
- `BlockKind_Switch` = `x00001800`
- `BlockKind_Case` = `x00001900`
- `BlockKind_LocalFunction` = `x00001A00`
- `BlockKind_Other` = `x00001B00`
- `BlockKind_Xml` = `x00001C00`
- `BlockKind_Xaml` = `x00001D00`
- `NamespaceBraces` = `raceKind_CurlyBraces | BlockKind_Namespace`
- `TypeBraces` = `raceKind_CurlyBraces | BlockKind_Type`
- `ModuleBraces` = `raceKind_CurlyBraces | BlockKind_Module`
- `ValueTypeBraces` = `raceKind_CurlyBraces | BlockKind_ValueType`
- `InterfaceBraces` = `raceKind_CurlyBraces | BlockKind_Interface`
- `MethodBraces` = `raceKind_CurlyBraces | BlockKind_Method`
- `AccessorBraces` = `raceKind_CurlyBraces | BlockKind_Accessor`
- `AnonymousMethodBraces` = `raceKind_CurlyBraces | BlockKind_AnonymousMethod`
- `ConstructorBraces` = `raceKind_CurlyBraces | BlockKind_Constructor`
- `DestructorBraces` = `raceKind_CurlyBraces | BlockKind_Destructor`
- `OperatorBraces` = `raceKind_CurlyBraces | BlockKind_Operator`
- `ConditionalBraces` = `raceKind_CurlyBraces | BlockKind_Conditional`
- `LoopBraces` = `raceKind_CurlyBraces | BlockKind_Loop`
- `PropertyBraces` = `raceKind_CurlyBraces | BlockKind_Property`
- `EventBraces` = `raceKind_CurlyBraces | BlockKind_Event`
- `TryBraces` = `raceKind_CurlyBraces | BlockKind_Try`
- `CatchBraces` = `raceKind_CurlyBraces | BlockKind_Catch`
- `FilterBraces` = `raceKind_CurlyBraces | BlockKind_Filter`
- `FinallyBraces` = `raceKind_CurlyBraces | BlockKind_Finally`
- `FaultBraces` = `raceKind_CurlyBraces | BlockKind_Fault`
- `LockBraces` = `raceKind_CurlyBraces | BlockKind_Lock`
- `UsingBraces` = `raceKind_CurlyBraces | BlockKind_Using`
- `FixedBraces` = `raceKind_CurlyBraces | BlockKind_Fixed`
- `SwitchBraces` = `raceKind_CurlyBraces | BlockKind_Switch`
- `CaseBraces` = `raceKind_CurlyBraces | BlockKind_Case`
- `LocalFunctionBraces` = `raceKind_CurlyBraces | BlockKind_LocalFunction`
- `OtherBlockBraces` = `raceKind_CurlyBraces | BlockKind_Other`
- `XmlBlockBraces` = `raceKind_OtherBraces | BlockKind_Xml`
- `XamlBlockBraces` = `raceKind_OtherBraces | BlockKind_Xaml`
- `SingleQuotes` = `raceKind_SingleQuotes | BlockKind_None`
- `DoubleQuotes` = `raceKind_DoubleQuotes | BlockKind_None`
- `Parentheses` = `raceKind_Parentheses | BlockKind_None`
- `AngleBrackets` = `raceKind_AngleBrackets | BlockKind_None`
- `SquareBrackets` = `raceKind_SquareBrackets | BlockKind_None`
- `CurlyBraces` = `raceKind_CurlyBraces | BlockKind_None`
- `OtherBraces` = `raceKind_OtherBraces | BlockKind_None`

## Class `CodeBracesRangeFlagsHelper`

helper methods

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.CodeBracesRangeFlagsHelper members directly without instantiation.
dnSpy.Contracts.Decompiler.CodeBracesRangeFlagsHelper./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRangeFlags.cs` (line 114)

### Methods

- `public static CodeBracesRangeFlags ToBlockKind(this CodeBracesRangeFlags flags)`
  - Summary: Extracts the block kind
  - Parameters:
    - `this CodeBracesRangeFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRangeFlags.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.CodeBracesRangeFlagsHelper.ToBlockKind(flags: /* CodeBracesRangeFlags */);
    ```
- `public static CodeBracesRangeFlags ToBraceKind(this CodeBracesRangeFlags flags)`
  - Summary: Extracts the brace kind
  - Parameters:
    - `this CodeBracesRangeFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRangeFlags.cs` (line 123)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.CodeBracesRangeFlagsHelper.ToBraceKind(flags: /* CodeBracesRangeFlags */);
    ```
- `public static bool IsBlock(this CodeBracesRangeFlags flags)`
  - Summary: Returns true if it's a block
  - Parameters:
    - `this CodeBracesRangeFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRangeFlags.cs` (line 144)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.CodeBracesRangeFlagsHelper.IsBlock(flags: /* CodeBracesRangeFlags */);
    ```
- `public static bool IsBraces(this CodeBracesRangeFlags flags)`
  - Summary: Returns true if it's braces
  - Parameters:
    - `this CodeBracesRangeFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/CodeBracesRangeFlags.cs` (line 137)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.CodeBracesRangeFlagsHelper.IsBraces(flags: /* CodeBracesRangeFlags */);
    ```

## Class `DecompilationContext`

Decompilation options

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.DecompilationContext();
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationContext.cs` (line 29)

### Constructors

- `public DecompilationContext()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationContext.cs` (line 60)

### Methods

- `public IDisposable DisableAssemblyLoad()`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationContext.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.DisableAssemblyLoad();
    ```
- `public T GetOrCreate<T>() where T : class, new()`
  - Summary: Gets or creates a cached object
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationContext.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreate();
    ```
- `public T GetOrCreate<T>(Func<T> creator) where T : class`
  - Summary: Gets or creates a cached object
  - Parameters:
    - `Func<T> creator`: Creates the object if necessary
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationContext.cs` (line 92)
  - Example:
    ```csharp
    // Example invocation
    instance.GetOrCreate(creator: /* Func<T> */);
    ```

### Properties

- `public CancellationToken CancellationToken { get; set; }`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationContext.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CancellationToken;
    ```
- `public Func<IDisposable> GetDisableAssemblyLoad { get; set; }`
  - Summary: Disables assembly loading until Dispose() gets called
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationContext.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GetDisableAssemblyLoad;
    ```
- `public Func<MethodDef, bool> IsBodyModified { get; set; }`
  - Summary: Returns true if the method body has been modified
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationContext.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsBodyModified;
    ```
- `public bool AsyncMethodBodyDecompilation { get; set; }`
  - Summary: true to decompile method bodies asynchronously. Should not be enabled when decompiling to a project since that code already decompiles one type per CPU core. Should also not be enabled when only one method body is decompiled since the code won't be faster.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationContext.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsyncMethodBodyDecompilation;
    ```
- `public bool CalculateILSpans { get; set; }`
  - Summary: true to calculate ILSpans. Used when debugging
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationContext.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CalculateILSpans;
    ```

## Enum `DecompilationType`

Decompilation type

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.DecompilationType and call its members.
var instance = new dnSpy.Contracts.Decompiler.DecompilationType(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilationType.cs` (line 24)

### Members

- `PartialType`: Decompiles a partial type, data is a instance
- `AssemblyInfo`: Decompiles AssemblyInfo.{cs,vb}, data is a instance
- `TypeMethods`: Decompiles selected methods, the other ones have empty bodies, data is a

## Class `DecompileAssemblyInfo`

Decompiles AssemblyInfo.{cs,vb}

**Inherits/Implements:** `DecompileTypeBase`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.DecompileAssemblyInfo(output: /* IDecompilerOutput */, ctx: /* DecompilationContext */, module: /* ModuleDef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileAssemblyInfo.cs` (line 28)

### Constructors

- `public DecompileAssemblyInfo(IDecompilerOutput output, DecompilationContext ctx, ModuleDef module)`
  - Summary: Constructor
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
    - `ModuleDef module`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileAssemblyInfo.cs` (line 46)

### Properties

- `public ModuleDef Module { get; }`
  - Summary: Gets the module
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileAssemblyInfo.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public bool KeepAllAttributes { get; set; }`
  - Summary: true to keep all attributes, false to remove attributes that are normally added by MSBuild tasks, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileAssemblyInfo.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.KeepAllAttributes;
    ```

## Class `DecompilePartialType`

Decompiles a partial type

**Inherits/Implements:** `DecompileTypeBase`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.DecompilePartialType(output: /* IDecompilerOutput */, ctx: /* DecompilationContext */, type: /* TypeDef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilePartialType.cs` (line 28)

### Constructors

- `public DecompilePartialType(IDecompilerOutput output, DecompilationContext ctx, TypeDef type)`
  - Summary: Constructor
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilePartialType.cs` (line 66)

### Properties

- `public HashSet<IMemberDef> Definitions { get; }`
  - Summary: All definitions that must be hidden or shown must be added here
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilePartialType.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Definitions;
    ```
- `public List<ITypeDefOrRef> InterfacesToRemove { get; }`
  - Summary: Interfaces to remove from the type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilePartialType.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.InterfacesToRemove;
    ```
- `public TypeDef Type { get; }`
  - Summary: Type to decompile
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilePartialType.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public bool AddPartialKeyword { get; set; }`
  - Summary: true to add the 'partial' keyword. It's true by default.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilePartialType.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AddPartialKeyword;
    ```
- `public bool ShowDefinitions { get; set; }`
  - Summary: true if members in should be shown, false if they should be removed
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilePartialType.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowDefinitions;
    ```
- `public bool UseUsingDeclarations { get; set; }`
  - Summary: true to use using declarations, false to use full namespaces (eg. useful when decompiling WinForms designer files)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilePartialType.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseUsingDeclarations;
    ```

## Class `DecompileTypeBase`

Base class of data

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.DecompileTypeBase(output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeBase.cs` (line 26)

### Constructors

- `protected DecompileTypeBase(IDecompilerOutput output, DecompilationContext ctx)`
  - Summary: Constructor
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeBase.cs` (line 42)

### Properties

- `public DecompilationContext Context { get; }`
  - Summary: Options
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeBase.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Context;
    ```
- `public IDecompilerOutput Output { get; }`
  - Summary: Output
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeBase.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Output;
    ```

## Class `DecompileTypeMethods`

Decompiles some methods

**Inherits/Implements:** `DecompileTypeBase`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.DecompileTypeMethods(output: /* IDecompilerOutput */, ctx: /* DecompilationContext */, type: /* TypeDef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeMethods.cs` (line 28)

### Constructors

- `public DecompileTypeMethods(IDecompilerOutput output, DecompilationContext ctx, TypeDef type)`
  - Summary: Constructor
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeMethods.cs` (line 62)

### Properties

- `public HashSet<MethodDef> Methods { get; }`
  - Summary: Methods to decompile. All the other methods will have an empty body, except for possible return default(XXX); statements and other code to keep the compiler happy.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeMethods.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Methods;
    ```
- `public HashSet<TypeDef> Types { get; }`
  - Summary: All nested types to show, not including their members
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeMethods.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Types;
    ```
- `public TypeDef Type { get; }`
  - Summary: Type to decompile
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeMethods.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public bool DecompileHidden { get; set; }`
  - Summary: true to only decompile methods and members not stored in , false to only decompile methods and members stored in .
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeMethods.cs` (line 54)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DecompileHidden;
    ```
- `public bool ShowAll { get; set; }`
  - Summary: true to decompile everything
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompileTypeMethods.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowAll;
    ```

## Class `DecompilerConstants`

Decompiler constants

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.DecompilerConstants members directly without instantiation.
dnSpy.Contracts.Decompiler.DecompilerConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 26)

### Fields

- `public static readonly Guid LANGUAGE_CSHARP = new Guid("F5A318D4-4B2A-48D2-AE33-F4D2B1EFF4B0")`
  - Summary: C# language
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 52)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.LANGUAGE_CSHARP;
    ```
- `public static readonly Guid LANGUAGE_CSHARP_ILSPY = new Guid("4162DADA-67C3-4DE4-A5F3-6552C8353ECE")`
  - Summary: C# language (ILSpy)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.LANGUAGE_CSHARP_ILSPY;
    ```
- `public static readonly Guid LANGUAGE_IL = new Guid("9EF276FD-3293-42A4-B48A-1D6A69086B3D")`
  - Summary: IL language
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.LANGUAGE_IL;
    ```
- `public static readonly Guid LANGUAGE_ILAST_ILSPY = new Guid("CA52A515-12AE-4182-BC88-81ED037C3D32")`
  - Summary: ILAst language (ILSpy)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 49)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.LANGUAGE_ILAST_ILSPY;
    ```
- `public static readonly Guid LANGUAGE_IL_ILSPY = new Guid("A4F35508-691F-4BD0-B74D-D5D5D1D0E8E6")`
  - Summary: IL language (ILSpy)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 46)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.LANGUAGE_IL_ILSPY;
    ```
- `public static readonly Guid LANGUAGE_VISUALBASIC = new Guid("B6849618-8239-4FBB-8DFF-D45EB023C193")`
  - Summary: Visual Basic language
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.LANGUAGE_VISUALBASIC;
    ```
- `public static readonly Guid LANGUAGE_VISUALBASIC_ILSPY = new Guid("BBA40092-76B2-4184-8E81-0F1E3ED14E72")`
  - Summary: Visual Basic language (ILSpy)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 61)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.LANGUAGE_VISUALBASIC_ILSPY;
    ```
- `public static readonly double CSHARP_ILSPY_DEBUG_ORDERUI = 10000`
  - Summary: Order of C# debug languages (ILSpy)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 37)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.CSHARP_ILSPY_DEBUG_ORDERUI;
    ```
- `public static readonly double CSHARP_ILSPY_ORDERUI = 0`
  - Summary: Order of C# language (ILSpy)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.CSHARP_ILSPY_ORDERUI;
    ```
- `public static readonly double ILAST_ILSPY_DEBUG_ORDERUI = 20000`
  - Summary: Order of ILAst debug languages (ILSpy)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.ILAST_ILSPY_DEBUG_ORDERUI;
    ```
- `public static readonly double IL_ILSPY_ORDERUI = 200`
  - Summary: Order of IL language (ILSpy)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.IL_ILSPY_ORDERUI;
    ```
- `public static readonly double VISUALBASIC_ILSPY_ORDERUI = 100`
  - Summary: Order of Visual Basic language (ILSpy)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.VISUALBASIC_ILSPY_ORDERUI;
    ```
- `public static readonly string GENERIC_NAMEUI_CSHARP = "C#"`
  - Summary: Name of C# language returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 67)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.GENERIC_NAMEUI_CSHARP;
    ```
- `public static readonly string GENERIC_NAMEUI_IL = "IL"`
  - Summary: Name of IL language returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 64)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.GENERIC_NAMEUI_IL;
    ```
- `public static readonly string GENERIC_NAMEUI_VISUALBASIC = "Visual Basic"`
  - Summary: Name of Visual Basic language returned by
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerConstants.cs` (line 70)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerConstants.GENERIC_NAMEUI_VISUALBASIC;
    ```

## Class `DecompilerExtensionMethods`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.DecompilerExtensionMethods members directly without instantiation.
dnSpy.Contracts.Decompiler.DecompilerExtensionMethods./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 242)

### Methods

- `public static void WriteCommentLine(this IDecompiler self, IDecompilerOutput output, string comment)`
  - Summary: Writes a comment and a new line
  - Parameters:
    - `this IDecompiler self`: This
    - `IDecompilerOutput output`: Output
    - `string comment`: Comment
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 249)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.DecompilerExtensionMethods.WriteCommentLine(self: /* IDecompiler */, output: /* IDecompilerOutput */, comment: /* string */);
    ```

## Class `DecompilerOptionConstants`

constants

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.DecompilerOptionConstants members directly without instantiation.
dnSpy.Contracts.Decompiler.DecompilerOptionConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 26)

### Fields

- `public static readonly Guid AllowFieldInitializers_GUID = new Guid("148CE5B9-95EC-441A-BDC8-1EAFFC02B097")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 193)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AllowFieldInitializers_GUID;
    ```
- `public static readonly Guid AlwaysGenerateExceptionVariableForCatchBlocksUnlessTypeIsObject_GUID = new Guid("5303AAB5-CAFF-469A-B19C-CE4FBAC88CC3")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 163)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AlwaysGenerateExceptionVariableForCatchBlocksUnlessTypeIsObject_GUID;
    ```
- `public static readonly Guid AnonymousMethods_GUID = new Guid("74BBA9E7-CD43-4C81-9A7C-9F49D4BDA3D9")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 68)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AnonymousMethods_GUID;
    ```
- `public static readonly Guid AsyncAwait_GUID = new Guid("A85EDBC5-88C4-417F-9BE0-3AC3CB8107B7")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 83)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AsyncAwait_GUID;
    ```
- `public static readonly Guid AutomaticEvents_GUID = new Guid("36D8D33E-4E5B-44E4-B638-6A4791F16024")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 93)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AutomaticEvents_GUID;
    ```
- `public static readonly Guid AutomaticProperties_GUID = new Guid("F6B11911-94BF-486B-AB8E-100B6A1B71FC")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 88)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AutomaticProperties_GUID;
    ```
- `public static readonly Guid ExpressionTrees_GUID = new Guid("DDF1B2BA-AD71-4A7A-ADCB-690D5F54FAF8")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 73)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ExpressionTrees_GUID;
    ```
- `public static readonly Guid ForEachStatement_GUID = new Guid("60ADA4EC-B7D1-407A-AE07-35D651956014")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 103)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ForEachStatement_GUID;
    ```
- `public static readonly Guid ForceShowAllMembers_GUID = new Guid("237BFCDA-07A5-493C-9ACF-8698EBF395FA")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 168)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ForceShowAllMembers_GUID;
    ```
- `public static readonly Guid FullyQualifyAllTypes_GUID = new Guid("916F3D3C-00E1-4D1D-ABFD-EA7092DF5028")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 133)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.FullyQualifyAllTypes_GUID;
    ```
- `public static readonly Guid FullyQualifyAmbiguousTypeNames_GUID = new Guid("C60EA9B7-D469-4FA4-BF85-4DF755B521A3")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 128)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.FullyQualifyAmbiguousTypeNames_GUID;
    ```
- `public static readonly Guid IntroduceIncrementAndDecrement_GUID = new Guid("A7A2255B-3089-448E-BF3E-CB2AB2050D8F")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 153)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.IntroduceIncrementAndDecrement_GUID;
    ```
- `public static readonly Guid LockStatement_GUID = new Guid("E1BD857F-B895-43C7-8844-5CF9F874E8C0")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 108)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.LockStatement_GUID;
    ```
- `public static readonly Guid MakeAssignmentExpressions_GUID = new Guid("6FFF99B5-D59A-4EB0-87A9-D297176D51B9")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 158)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.MakeAssignmentExpressions_GUID;
    ```
- `public static readonly Guid MaxArrayElements_GUID = new Guid("E0DEC360-EE40-4F61-9106-D9F142F4CC9A")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 178)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.MaxArrayElements_GUID;
    ```
- `public static readonly Guid MaxStringLength_GUID = new Guid("405901FA-47E5-497F-A4DF-0FE5C3677287")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 58)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.MaxStringLength_GUID;
    ```
- `public static readonly Guid MemberAddPrivateModifier_GUID = new Guid("2E764781-2075-47DC-BEE5-7F5F560BA726")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 208)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.MemberAddPrivateModifier_GUID;
    ```
- `public static readonly Guid MemberOrder_GUID = new Guid("8E6FE77A-2BCB-4F34-A41B-7F097560A211")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 63)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.MemberOrder_GUID;
    ```
- `public static readonly Guid ObjectOrCollectionInitializers_GUID = new Guid("1CD4E962-2DF0-4681-A631-E0A2F6DD641E")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 143)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ObjectOrCollectionInitializers_GUID;
    ```
- `public static readonly Guid OneCustomAttributePerLine_GUID = new Guid("DFFAF5AE-2A25-4A3A-A82E-779B58DA734A")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 198)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.OneCustomAttributePerLine_GUID;
    ```
- `public static readonly Guid QueryExpressions_GUID = new Guid("CFB4D69F-0A98-4763-A863-6227159A0BD6")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 123)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.QueryExpressions_GUID;
    ```
- `public static readonly Guid RemoveEmptyDefaultConstructors_GUID = new Guid("79DEF757-13D3-413A-9524-4104F2F179BE")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 148)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.RemoveEmptyDefaultConstructors_GUID;
    ```
- `public static readonly Guid RemoveNewDelegateClass_GUID = new Guid("BEC534D0-A231-4F65-BE2E-5CCC4A7CE1B2")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 213)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.RemoveNewDelegateClass_GUID;
    ```
- `public static readonly Guid ShowILBytes_GUID = new Guid("E03DA52E-927C-4AA0-8FDE-9607125B606C")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ShowILBytes_GUID;
    ```
- `public static readonly Guid ShowILComments_GUID = new Guid("241A61B8-0F12-438C-A431-029B9FAEB124")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ShowILComments_GUID;
    ```
- `public static readonly Guid ShowPdbInfo_GUID = new Guid("2E19D17C-1994-4CA3-914B-1D690E3EA29E")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 53)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ShowPdbInfo_GUID;
    ```
- `public static readonly Guid ShowTokenAndRvaComments_GUID = new Guid("99475485-C462-4D60-AF90-C14008577A9D")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ShowTokenAndRvaComments_GUID;
    ```
- `public static readonly Guid ShowXmlDocumentation_GUID = new Guid("6D50BA49-D76C-4EDD-BF5A-F81B894CCD2C")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ShowXmlDocumentation_GUID;
    ```
- `public static readonly Guid SortCustomAttributes_GUID = new Guid("8E3E8009-AC00-436E-B476-08B2E697AD32")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 183)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.SortCustomAttributes_GUID;
    ```
- `public static readonly Guid SortMembers_GUID = new Guid("51FEEFED-5353-4637-A75E-7CA87EFA3998")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 48)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.SortMembers_GUID;
    ```
- `public static readonly Guid SortSystemUsingStatementsFirst_GUID = new Guid("48BF91F6-A186-45B9-8A79-EEFEA5E5BAB1")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 173)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.SortSystemUsingStatementsFirst_GUID;
    ```
- `public static readonly Guid SwitchStatementOnString_GUID = new Guid("E0FC32C0-74DA-4D8C-886C-3182D7A77C16")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 113)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.SwitchStatementOnString_GUID;
    ```
- `public static readonly Guid TypeAddInternalModifier_GUID = new Guid("354FAA68-7CDC-478E-9414-5C066C45C3F3")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 203)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.TypeAddInternalModifier_GUID;
    ```
- `public static readonly Guid UseDebugSymbols_GUID = new Guid("D8E085BF-9A1B-463C-96C6-894979DD131D")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 138)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.UseDebugSymbols_GUID;
    ```
- `public static readonly Guid UseSourceCodeOrder_GUID = new Guid("11B1D294-1D85-4A5B-B9E9-B2A8AB889F51")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 188)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.UseSourceCodeOrder_GUID;
    ```
- `public static readonly Guid UsingDeclarations_GUID = new Guid("DAC40A5C-C867-4EF2-8DA3-9AFA285A47CE")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 118)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.UsingDeclarations_GUID;
    ```
- `public static readonly Guid UsingStatement_GUID = new Guid("24511B87-F19D-4AAC-80FC-A7E67D92A40E")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 98)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.UsingStatement_GUID;
    ```
- `public static readonly Guid YieldReturn_GUID = new Guid("07FD6290-2B5B-424E-B7E5-B64B32881F81")`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 78)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.YieldReturn_GUID;
    ```
- `public static readonly string AllowFieldInitializers_NAME = "field-initializers"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 195)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AllowFieldInitializers_NAME;
    ```
- `public static readonly string AlwaysGenerateExceptionVariableForCatchBlocksUnlessTypeIsObject_NAME = "always-create-ex-var"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 165)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AlwaysGenerateExceptionVariableForCatchBlocksUnlessTypeIsObject_NAME;
    ```
- `public static readonly string AnonymousMethods_NAME = "anon-methods"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 70)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AnonymousMethods_NAME;
    ```
- `public static readonly string AsyncAwait_NAME = "async"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 85)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AsyncAwait_NAME;
    ```
- `public static readonly string AutomaticEvents_NAME = "auto-events"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 95)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AutomaticEvents_NAME;
    ```
- `public static readonly string AutomaticProperties_NAME = "auto-props"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 90)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.AutomaticProperties_NAME;
    ```
- `public static readonly string ExpressionTrees_NAME = "expr-trees"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 75)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ExpressionTrees_NAME;
    ```
- `public static readonly string ForEachStatement_NAME = "foreach-stmt"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 105)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ForEachStatement_NAME;
    ```
- `public static readonly string ForceShowAllMembers_NAME = "show-all"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 170)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ForceShowAllMembers_NAME;
    ```
- `public static readonly string FullyQualifyAllTypes_NAME = "full-names"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 135)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.FullyQualifyAllTypes_NAME;
    ```
- `public static readonly string FullyQualifyAmbiguousTypeNames_NAME = "ambig-full-names"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 130)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.FullyQualifyAmbiguousTypeNames_NAME;
    ```
- `public static readonly string IntroduceIncrementAndDecrement_NAME = "inc-dec"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 155)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.IntroduceIncrementAndDecrement_NAME;
    ```
- `public static readonly string LockStatement_NAME = "lock-stmt"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 110)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.LockStatement_NAME;
    ```
- `public static readonly string MakeAssignmentExpressions_NAME = "make-assign-expr"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 160)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.MakeAssignmentExpressions_NAME;
    ```
- `public static readonly string MaxArrayElements_NAME = "max-array-elems"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 180)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.MaxArrayElements_NAME;
    ```
- `public static readonly string MaxStringLength_NAME = "max-string-length"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 60)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.MaxStringLength_NAME;
    ```
- `public static readonly string MemberAddPrivateModifier_NAME = "private-modifier-member"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 210)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.MemberAddPrivateModifier_NAME;
    ```
- `public static readonly string MemberOrder_NAME = "member-order"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 65)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.MemberOrder_NAME;
    ```
- `public static readonly string ObjectOrCollectionInitializers_NAME = "obj-inits"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 145)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ObjectOrCollectionInitializers_NAME;
    ```
- `public static readonly string OneCustomAttributePerLine_NAME = "one-ca-per-line"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 200)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.OneCustomAttributePerLine_NAME;
    ```
- `public static readonly string QueryExpressions_NAME = "query-expr"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 125)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.QueryExpressions_NAME;
    ```
- `public static readonly string RemoveEmptyDefaultConstructors_NAME = "remove-emtpy-ctors"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 150)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.RemoveEmptyDefaultConstructors_NAME;
    ```
- `public static readonly string RemoveNewDelegateClass_NAME = "remove-new-delegate-class"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 215)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.RemoveNewDelegateClass_NAME;
    ```
- `public static readonly string ShowILBytes_NAME = "bytes"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 45)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ShowILBytes_NAME;
    ```
- `public static readonly string ShowILComments_NAME = "comments"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ShowILComments_NAME;
    ```
- `public static readonly string ShowPdbInfo_NAME = "pdb-info"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 55)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ShowPdbInfo_NAME;
    ```
- `public static readonly string ShowTokenAndRvaComments_NAME = "tokens"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ShowTokenAndRvaComments_NAME;
    ```
- `public static readonly string ShowXmlDocumentation_NAME = "xml-doc"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.ShowXmlDocumentation_NAME;
    ```
- `public static readonly string SortCustomAttributes_NAME = "sort-custom-attrs"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 185)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.SortCustomAttributes_NAME;
    ```
- `public static readonly string SortMembers_NAME = "sort-members"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 50)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.SortMembers_NAME;
    ```
- `public static readonly string SortSystemUsingStatementsFirst_NAME = "system-first"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 175)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.SortSystemUsingStatementsFirst_NAME;
    ```
- `public static readonly string SwitchStatementOnString_NAME = "switch-string"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 115)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.SwitchStatementOnString_NAME;
    ```
- `public static readonly string TypeAddInternalModifier_NAME = "internal-modifier-type"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 205)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.TypeAddInternalModifier_NAME;
    ```
- `public static readonly string UseDebugSymbols_NAME = "use-debug-syms"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 140)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.UseDebugSymbols_NAME;
    ```
- `public static readonly string UseSourceCodeOrder_NAME = "src-order"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 190)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.UseSourceCodeOrder_NAME;
    ```
- `public static readonly string UsingDeclarations_NAME = "using-decl"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 120)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.UsingDeclarations_NAME;
    ```
- `public static readonly string UsingStatement_NAME = "using-stmt"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 100)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.UsingStatement_NAME;
    ```
- `public static readonly string YieldReturn_NAME = "yield"`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerOptionConstants.cs` (line 80)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.DecompilerOptionConstants.YieldReturn_NAME;
    ```

## Class `DecompilerOutputExtensions`

extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.DecompilerOutputExtensions members directly without instantiation.
dnSpy.Contracts.Decompiler.DecompilerOutputExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 109)

### Methods

- `public static void AddBracePair(this IDecompilerOutput output, TextSpan start, TextSpan end, CodeBracesRangeFlags flags)`
  - Summary: Adds a
  - Parameters:
    - `this IDecompilerOutput output`: Output
    - `TextSpan start`: Start span
    - `TextSpan end`: End span
    - `CodeBracesRangeFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 155)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.DecompilerOutputExtensions.AddBracePair(output: /* IDecompilerOutput */, start: /* TextSpan */, end: /* TextSpan */, flags: /* CodeBracesRangeFlags */);
    ```
- `public static void AddCodeBracesRange(this IDecompilerOutput output, CodeBracesRange range)`
  - Summary: Adds a
  - Parameters:
    - `this IDecompilerOutput output`: Output
    - `CodeBracesRange range`: Range
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 145)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.DecompilerOutputExtensions.AddCodeBracesRange(output: /* IDecompilerOutput */, range: /* CodeBracesRange */);
    ```
- `public static void AddDebugInfo(this IDecompilerOutput output, MethodDebugInfo methodDebugInfo)`
  - Summary: Adds debug info to the custom data collection, see also
  - Parameters:
    - `this IDecompilerOutput output`: Output
    - `MethodDebugInfo methodDebugInfo`: Debug info
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.DecompilerOutputExtensions.AddDebugInfo(output: /* IDecompilerOutput */, methodDebugInfo: /* MethodDebugInfo */);
    ```
- `public static void AddLineSeparator(this IDecompilerOutput output, int position)`
  - Summary: Adds a
  - Parameters:
    - `this IDecompilerOutput output`: Output
    - `int position`: Position of the line that gets a line separator
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 163)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.DecompilerOutputExtensions.AddLineSeparator(output: /* IDecompilerOutput */, position: /* int */);
    ```
- `public static void AddSpanReference(this IDecompilerOutput output, SpanReference spanReference)`
  - Summary: Adds a
  - Parameters:
    - `this IDecompilerOutput output`: Output
    - `SpanReference spanReference`: Data
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.DecompilerOutputExtensions.AddSpanReference(output: /* IDecompilerOutput */, spanReference: /* SpanReference */);
    ```
- `public static void AddSpanReference(this IDecompilerOutput output, object reference, int start, int end, string id)`
  - Summary: Adds a
  - Parameters:
    - `this IDecompilerOutput output`: Output
    - `object reference`: Reference
    - `int start`: Start position
    - `int end`: End position
    - `string id`: Reference id or null, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 137)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.DecompilerOutputExtensions.AddSpanReference(output: /* IDecompilerOutput */, reference: /* object */, start: /* int */, end: /* int */, id: /* string */);
    ```
- `public static void WriteLine(this IDecompilerOutput output, string text, object color)`
  - Summary: Writes text and a new line
  - Parameters:
    - `this IDecompilerOutput output`: Output
    - `string text`: Text
    - `object color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 172)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.DecompilerOutputExtensions.WriteLine(output: /* IDecompilerOutput */, text: /* string */, color: /* object */);
    ```
- `public static void WriteXmlDoc(this IDecompilerOutput output, string xmlDocText)`
  - Summary: Writes XML documentation
  - Parameters:
    - `this IDecompilerOutput output`: Output
    - `string xmlDocText`: XML documentation
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.DecompilerOutputExtensions.WriteXmlDoc(output: /* IDecompilerOutput */, xmlDocText: /* string */);
    ```

## Enum `DecompilerReferenceFlags`

Flags used by

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.DecompilerReferenceFlags and call its members.
var instance = new dnSpy.Contracts.Decompiler.DecompilerReferenceFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerReferenceFlags.cs` (line 26)

### Members

- `None`: No bit is set
- `Definition` = `x00000001`: It's a definition (method declaration, field declaration etc) if set, else it's a reference to the definition
- `Local` = `x00000002`: It's a local definition or reference, eg. a method parameter, method local, method label.
- `IsWrite` = `x00000004`: The code writes to the reference
- `Hidden` = `x00000008`: Reference shouldn't be highlighted

## Class `DecompilerSettingsBase`

Decompiler settings

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.DecompilerSettingsBase and call its members.
var instance = new dnSpy.Contracts.Decompiler.DecompilerSettingsBase(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 28)

### Methods

- `public IDecompilerOption TryGetOption(Guid guid)`
  - Summary: Returns an option or null
  - Parameters:
    - `Guid guid`: Guid
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetOption(guid: /* Guid */);
    ```
- `public IDecompilerOption TryGetOption(string name)`
  - Summary: Returns an option or null
  - Parameters:
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetOption(name: /* string */);
    ```
- `public abstract DecompilerSettingsBase Clone()`
  - Summary: Clones the settings
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Clone();
    ```
- `public abstract override bool Equals(object obj)`
  - Summary: Returns true if this instance equals
  - Parameters:
    - `object obj`: Other object, may be null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public abstract override int GetHashCode()`
  - Summary: Gets the hash code of this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public bool GetBoolean(Guid guid)`
  - Summary: Returns a boolean or false if the option doesn't exist
  - Parameters:
    - `Guid guid`: Guid
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.GetBoolean(guid: /* Guid */);
    ```
- `public bool GetBoolean(string name)`
  - Summary: Returns a boolean or false if the option doesn't exist
  - Parameters:
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.GetBoolean(name: /* string */);
    ```

### Properties

- `public abstract IEnumerable<IDecompilerOption> Options { get; }`
  - Summary: Gets all options
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Options;
    ```
- `public abstract int Version { get; }`
  - Summary: Version number that gets incremented whenever the options change
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Version;
    ```

### Events

- `public abstract event EventHandler VersionChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/DecompilerSettingsBase.cs` (line 43)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.VersionChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `EventDefComparer`

comparer

**Inherits/Implements:** `MemberRefComparer<EventDef>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.EventDefComparer and call its members.
var instance = new dnSpy.Contracts.Decompiler.EventDefComparer(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 70)

### Fields

- `public static readonly EventDefComparer Instance = new EventDefComparer()`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 74)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.EventDefComparer.Instance;
    ```

## Class `Extensions`

Extensions

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.Extensions members directly without instantiation.
dnSpy.Contracts.Decompiler.Extensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 30)

### Methods

- `public static HashSet<MethodDef> GetPropertyAndEventMethods(this TypeDef type)`
  - Summary: Gets all methods that are part of properties or events
  - Parameters:
    - `this TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 151)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.GetPropertyAndEventMethods(type: /* TypeDef */);
    ```
- `public static IEnumerable<IMemberDef> GetNonSortedMethodsPropertiesEvents(this TypeDef type)`
  - Summary: Gets all methods, properties and events. They're returned in the original metadata order.
  - Parameters:
    - `this TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 235)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.GetNonSortedMethodsPropertiesEvents(type: /* TypeDef */);
    ```
- `public static IList<Parameter> GetParameters(this IMethod method)`
  - Summary: Gets all parameters
  - Parameters:
    - `this IMethod method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.GetParameters(method: /* IMethod */);
    ```
- `public static TypeDef Resolve(this IType type)`
  - Summary: Resolves a type
  - Parameters:
    - `this IType type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 214)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.Resolve(type: /* IType */);
    ```
- `public static bool CanSortFields(this TypeDef type)`
  - Summary: Returns true if the fields can be sorted and false if the original metadata order must be used
  - Parameters:
    - `this TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 221)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.CanSortFields(type: /* TypeDef */);
    ```
- `public static bool CanSortMethods(this TypeDef type)`
  - Summary: Returns true if the methods can be sorted and false if the original metadata order must be used
  - Parameters:
    - `this TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 228)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.CanSortMethods(type: /* TypeDef */);
    ```
- `public static bool GetRVA(this IMemberDef member, out uint rva, out long fileOffset)`
  - Summary: Gets the RVA and file offset of a member definition. Returns false if the RVA and file offsets aren't known or if there's no RVA (eg. there's no method body)
  - Parameters:
    - `this IMemberDef member`: Member
    - `out uint rva`: Updated with the RVA
    - `out long fileOffset`: Updated with the file offset
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.GetRVA(member: /* IMemberDef */, rva: /* uint */, fileOffset: /* long */);
    ```
- `public static bool IsDefined(this IHasCustomAttribute provider, UTF8String @namespace, UTF8String name)`
  - Summary: Checks whether a custom attribute exists
  - Parameters:
    - `this IHasCustomAttribute provider`: Custom attribute provider
    - `UTF8String @namespace`: Description not provided.
    - `UTF8String name`: Name of custom attribute
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.IsDefined(provider: /* IHasCustomAttribute */, @namespace: /* UTF8String */, name: /* UTF8String */);
    ```
- `public static bool IsIndexer(this PropertyDef property)`
  - Summary: Checks whether is an indexer property
  - Parameters:
    - `this PropertyDef property`: Property to check
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 170)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.IsIndexer(property: /* PropertyDef */);
    ```
- `public static int GetCodeSize(this CilBody body)`
  - Summary: Gets the size of the code in the method body
  - Parameters:
    - `this CilBody body`: Method body, can be null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 101)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.GetCodeSize(body: /* CilBody */);
    ```
- `public static uint? ToFileOffset(this ModuleDef module, uint rva)`
  - Summary: Converts an RVA to a file offset
  - Parameters:
    - `this ModuleDef module`: Module
    - `uint rva`: RVA
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/Extensions.cs` (line 89)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.Extensions.ToFileOffset(module: /* ModuleDef */, rva: /* uint */);
    ```

## Class `FieldDefComparer`

comparer

**Inherits/Implements:** `MemberRefComparer<FieldDef>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.FieldDefComparer and call its members.
var instance = new dnSpy.Contracts.Decompiler.FieldDefComparer(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 60)

### Fields

- `public static readonly FieldDefComparer Instance = new FieldDefComparer()`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 64)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.FieldDefComparer.Instance;
    ```

## Enum `FindByTextPositionOptions`

Find options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.FindByTextPositionOptions and call its members.
var instance = new dnSpy.Contracts.Decompiler.FindByTextPositionOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 86)

### Members

- `None`: No bit is set
- `SameMethod` = `x00000001`: If set, only return statements within the method that contains the text position
- `OuterMostStatement` = `x00000002`: If there are nested methods or delegates in the method, return the outer most statement. If it's not set, the statement inside the nested method / delegate is returned.

## Enum `FormatterOptions`

Formatter options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.FormatterOptions and call its members.
var instance = new dnSpy.Contracts.Decompiler.FormatterOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/FormatterOptions.cs` (line 26)

### Members

- `ShowModuleNames` = `x00000001`
- `ShowParameterTypes` = `x00000002`
- `ShowParameterNames` = `x00000004`
- `ShowDeclaringTypes` = `x00000008`
- `ShowReturnTypes` = `x00000010`
- `ShowNamespaces` = `x00000020`
- `ShowIntrinsicTypeKeywords` = `x00000040`
- `UseDecimal` = `x00000080`
- `ShowTokens` = `x00000100`
- `ShowArrayValueSizes` = `x00000200`
- `ShowFieldLiteralValues` = `x00000400`
- `ShowParameterLiteralValues` = `x00000800`
- `DigitSeparators` = `x00001000`
- `Default` = `howParameterTypes |
			ShowParameterNames |
			ShowDeclaringTypes |
			ShowReturnTypes |
			ShowIntrinsicTypeKeywords |
			ShowFieldLiteralValues`

## Struct `GenericArgumentResolver`

Resolves generic arguments

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.GenericArgumentResolver and call its members.
var instance = new dnSpy.Contracts.Decompiler.GenericArgumentResolver(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/GenericArgumentResolver.cs` (line 9)

### Methods

- `public static MethodBaseSig Resolve(MethodBaseSig methodSig, IList<TypeSig> typeGenArgs, IList<TypeSig> methodGenArgs)`
  - Summary: Resolves the method signature with the specified generic arguments.
  - Parameters:
    - `MethodBaseSig methodSig`: The method signature.
    - `IList<TypeSig> typeGenArgs`: The type generic arguments.
    - `IList<TypeSig> methodGenArgs`: The method generic arguments.
  - Returns: Resolved method signature.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/GenericArgumentResolver.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.GenericArgumentResolver.Resolve(methodSig: /* MethodBaseSig */, typeGenArgs: /* IList<TypeSig> */, methodGenArgs: /* IList<TypeSig> */);
    ```
- `public static TypeSig Resolve(TypeSig typeSig, IList<TypeSig> typeGenArgs, IList<TypeSig> methodGenArgs)`
  - Summary: Resolves the type signature with the specified generic arguments.
  - Parameters:
    - `TypeSig typeSig`: The type signature.
    - `IList<TypeSig> typeGenArgs`: The type generic arguments.
    - `IList<TypeSig> methodGenArgs`: The method generic arguments.
  - Returns: Resolved type signature.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/GenericArgumentResolver.cs` (line 28)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.GenericArgumentResolver.Resolve(typeSig: /* TypeSig */, typeGenArgs: /* IList<TypeSig> */, methodGenArgs: /* IList<TypeSig> */);
    ```

## Interface `IBamlDecompiler`

Baml to xaml decompiler

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.IBamlDecompiler and call its members.
var instance = new dnSpy.Contracts.Decompiler.IBamlDecompiler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IBamlDecompiler.cs` (line 29)

### Methods

- `IList<string> Decompile(ModuleDef module, byte[] data, CancellationToken token, BamlDecompilerOptions bamlDecompilerOptions, Stream output, XamlOutputOptions outputOptions)`
  - Summary: Decompiles baml to xaml. Returns all assembly references.
  - Parameters:
    - `ModuleDef module`: Module
    - `byte[] data`: Baml data
    - `CancellationToken token`: Cancellation token
    - `BamlDecompilerOptions bamlDecompilerOptions`: Options
    - `Stream output`: Output stream
    - `XamlOutputOptions outputOptions`: Output options
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IBamlDecompiler.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(module: /* ModuleDef */, data: /* byte[] */, token: /* CancellationToken */, bamlDecompilerOptions: /* BamlDecompilerOptions */, output: /* Stream */, outputOptions: /* XamlOutputOptions */);
    ```

## Interface `IDecompiler`

A decompiler

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.IDecompiler and call its members.
var instance = new dnSpy.Contracts.Decompiler.IDecompiler(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 29)

### Methods

- `bool CanDecompile(DecompilationType decompilationType)`
  - Summary: Returns true if is supported and can be called.
  - Parameters:
    - `DecompilationType decompilationType`: Decompilation type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 228)
  - Example:
    ```csharp
    // Example invocation
    instance.CanDecompile(decompilationType: /* DecompilationType */);
    ```
- `bool ShowMember(IMemberRef member)`
  - Summary: Returns true if the member is visible. Can be used to hide compiler generated types, methods etc
  - Parameters:
    - `IMemberRef member`: Member
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 220)
  - Example:
    ```csharp
    // Example invocation
    instance.ShowMember(member: /* IMemberRef */);
    ```
- `void Decompile(AssemblyDef asm, IDecompilerOutput output, DecompilationContext ctx)`
  - Summary: Decompiles an assembly
  - Parameters:
    - `AssemblyDef asm`: Assembly
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 161)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(asm: /* AssemblyDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `void Decompile(DecompilationType decompilationType, object data)`
  - Summary: Decompiles some data. Should only be called if returns true
  - Parameters:
    - `DecompilationType decompilationType`: Decompilation type
    - `object data`: Data, see
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 236)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(decompilationType: /* DecompilationType */, data: /* object */);
    ```
- `void Decompile(EventDef ev, IDecompilerOutput output, DecompilationContext ctx)`
  - Summary: Decompiles an event
  - Parameters:
    - `EventDef ev`: Event
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 136)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(ev: /* EventDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `void Decompile(FieldDef field, IDecompilerOutput output, DecompilationContext ctx)`
  - Summary: Decompiles a field
  - Parameters:
    - `FieldDef field`: Field
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 128)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(field: /* FieldDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `void Decompile(MethodDef method, IDecompilerOutput output, DecompilationContext ctx)`
  - Summary: Decompiles a method
  - Parameters:
    - `MethodDef method`: Method
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 112)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(method: /* MethodDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `void Decompile(ModuleDef mod, IDecompilerOutput output, DecompilationContext ctx)`
  - Summary: Decompiles a module
  - Parameters:
    - `ModuleDef mod`: Module
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 169)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(mod: /* ModuleDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `void Decompile(PropertyDef property, IDecompilerOutput output, DecompilationContext ctx)`
  - Summary: Decompiles a property
  - Parameters:
    - `PropertyDef property`: Property
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 120)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(property: /* PropertyDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `void Decompile(TypeDef type, IDecompilerOutput output, DecompilationContext ctx)`
  - Summary: Decompiles a type
  - Parameters:
    - `TypeDef type`: Type
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 144)
  - Example:
    ```csharp
    // Example invocation
    instance.Decompile(type: /* TypeDef */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `void DecompileNamespace(string @namespace, IEnumerable<TypeDef> types, IDecompilerOutput output, DecompilationContext ctx)`
  - Summary: Decompiles a namespace
  - Parameters:
    - `string @namespace`: Description not provided.
    - `IEnumerable<TypeDef> types`: Types in namespace
    - `IDecompilerOutput output`: Output
    - `DecompilationContext ctx`: Context
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 153)
  - Example:
    ```csharp
    // Example invocation
    instance.DecompileNamespace(@namespace: /* string */, types: /* IEnumerable<TypeDef> */, output: /* IDecompilerOutput */, ctx: /* DecompilationContext */);
    ```
- `void Write(ITextColorWriter output, IMemberRef member, FormatterOptions flags)`
  - Summary: Writes to
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IMemberRef member`: Member
    - `FormatterOptions flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* ITextColorWriter */, member: /* IMemberRef */, flags: /* FormatterOptions */);
    ```
- `void WriteCommentBegin(IDecompilerOutput output, bool addSpace)`
  - Summary: Writes a comment prefix
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `bool addSpace`: true to add a space before the comment prefix
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 206)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteCommentBegin(output: /* IDecompilerOutput */, addSpace: /* bool */);
    ```
- `void WriteCommentEnd(IDecompilerOutput output, bool addSpace)`
  - Summary: Writes a comment suffix
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `bool addSpace`: true to add a space before the comment suffix (if it's written)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 213)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteCommentEnd(output: /* IDecompilerOutput */, addSpace: /* bool */);
    ```
- `void WriteName(ITextColorWriter output, PropertyDef property, bool? isIndexer)`
  - Summary: Writes a property name
  - Parameters:
    - `ITextColorWriter output`: Output
    - `PropertyDef property`: Type
    - `bool? isIndexer`: true if it's an indexer
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(output: /* ITextColorWriter */, property: /* PropertyDef */, isIndexer: /* bool? */);
    ```
- `void WriteName(ITextColorWriter output, TypeDef type)`
  - Summary: Writes a type name
  - Parameters:
    - `ITextColorWriter output`: Output
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 87)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteName(output: /* ITextColorWriter */, type: /* TypeDef */);
    ```
- `void WriteNamespaceToolTip(ITextColorWriter output, string @namespace)`
  - Summary: Writes a namespace tooltip
  - Parameters:
    - `ITextColorWriter output`: Output
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 191)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteNamespaceToolTip(output: /* ITextColorWriter */, @namespace: /* string */);
    ```
- `void WriteToolTip(ITextColorWriter output, IMemberRef member, IHasCustomAttribute typeAttributes)`
  - Summary: Writes a tooltip
  - Parameters:
    - `ITextColorWriter output`: Output
    - `IMemberRef member`: Member
    - `IHasCustomAttribute typeAttributes`: Type containing attributes, used to detect the dynamic types and out/ref params
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 177)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteToolTip(output: /* ITextColorWriter */, member: /* IMemberRef */, typeAttributes: /* IHasCustomAttribute */);
    ```
- `void WriteToolTip(ITextColorWriter output, ISourceVariable variable)`
  - Summary: Writes a tooltip
  - Parameters:
    - `ITextColorWriter output`: Output
    - `ISourceVariable variable`: Local or argument
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 184)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteToolTip(output: /* ITextColorWriter */, variable: /* ISourceVariable */);
    ```
- `void WriteType(ITextColorWriter output, ITypeDefOrRef type, bool includeNamespace, ParamDef pd = null)`
  - Summary: Writes a type name
  - Parameters:
    - `ITextColorWriter output`: Output
    - `ITypeDefOrRef type`: Type
    - `bool includeNamespace`: true to include namespace
    - `ParamDef pd` (default: `null`): or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteType(output: /* ITextColorWriter */, type: /* ITypeDefOrRef */, includeNamespace: /* bool */, pd: /* ParamDef */);
    ```

### Properties

- `DecompilerSettingsBase Settings { get; }`
  - Summary: Gets the settings
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Settings;
    ```
- `Guid GenericGuid { get; }`
  - Summary: Language guid, eg. , see also
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericGuid;
    ```
- `Guid UniqueGuid { get; }`
  - Summary: Unique language guid, see also
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UniqueGuid;
    ```
- `MetadataTextColorProvider MetadataTextColorProvider { get; }`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MetadataTextColorProvider;
    ```
- `double OrderUI { get; }`
  - Summary: Order of language when shown to the user, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OrderUI;
    ```
- `string ContentTypeString { get; }`
  - Summary: Gets the content type string
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ContentTypeString;
    ```
- `string FileExtension { get; }`
  - Summary: File extension, eg. .cs, can't be null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FileExtension;
    ```
- `string GenericNameUI { get; }`
  - Summary: Real name of the language, eg. "C#" if it's C#. See also . It's used when the real language name must be shown to the user.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.GenericNameUI;
    ```
- `string ProjectFileExtension { get; }`
  - Summary: Project file extension, eg. .csproj or null if it's not supported
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ProjectFileExtension;
    ```
- `string UniqueNameUI { get; }`
  - Summary: Language name shown to the user, and can contain extra info eg. "C# XYZ", see also .
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompiler.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UniqueNameUI;
    ```

## Interface `IDecompilerCreator`

Creates s

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.IDecompilerCreator and call its members.
var instance = new dnSpy.Contracts.Decompiler.IDecompilerCreator(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerCreator.cs` (line 26)

### Methods

- `IEnumerable<IDecompiler> Create()`
  - Summary: Creates all decompilers
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerCreator.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

## Interface `IDecompilerOption`

Decompiler option

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.IDecompilerOption and call its members.
var instance = new dnSpy.Contracts.Decompiler.IDecompilerOption(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOption.cs` (line 26)

### Properties

- `Guid Guid { get; }`
  - Summary: Guid, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOption.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Guid;
    ```
- `Type Type { get; }`
  - Summary: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOption.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `object Value { get; set; }`
  - Summary: Gets/sets the value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOption.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `string Description { get; }`
  - Summary: Description or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOption.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Description;
    ```
- `string Name { get; }`
  - Summary: Name or null, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOption.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `IDecompilerOutput`

Interface used by decompilers to write text

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.IDecompilerOutput and call its members.
var instance = new dnSpy.Contracts.Decompiler.IDecompilerOutput(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 27)

### Methods

- `void AddCustomData<TData>(string id, TData data)`
  - Summary: Adds custom data to a list
  - Parameters:
    - `string id`: Key, eg.,
    - `TData data`: Data to add. If a span is needed, see
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.AddCustomData(id: /* string */, data: /* TData */);
    ```
- `void DecreaseIndent()`
  - Summary: Decrements the indentation level. Nothing is added to the output stream.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 47)
  - Example:
    ```csharp
    // Example invocation
    instance.DecreaseIndent();
    ```
- `void IncreaseIndent()`
  - Summary: Increments the indentation level. Nothing is added to the output stream.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.IncreaseIndent();
    ```
- `void Write(string text, int index, int length, object color)`
  - Summary: Writes text and color. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `int index`: Index in
    - `int length`: Number of characters to write
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, index: /* int */, length: /* int */, color: /* object */);
    ```
- `void Write(string text, int index, int length, object reference, DecompilerReferenceFlags flags, object color)`
  - Summary: Writes text, color and a reference. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `int index`: Index in
    - `int length`: Number of characters to write
    - `object reference`: Reference
    - `DecompilerReferenceFlags flags`: Flags
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, index: /* int */, length: /* int */, reference: /* object */, flags: /* DecompilerReferenceFlags */, color: /* object */);
    ```
- `void Write(string text, object color)`
  - Summary: Writes text and color. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, color: /* object */);
    ```
- `void Write(string text, object reference, DecompilerReferenceFlags flags, object color)`
  - Summary: Writes text, color and a reference. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `object reference`: Reference
    - `DecompilerReferenceFlags flags`: Flags
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, reference: /* object */, flags: /* DecompilerReferenceFlags */, color: /* object */);
    ```
- `void WriteLine()`
  - Summary: Writes a new line without writing any indentation
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLine();
    ```

### Properties

- `bool UsesCustomData { get; }`
  - Summary: true if custom data added by is used and isn't ignored. If this is false, doesn't have to be called.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 103)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UsesCustomData;
    ```
- `int Length { get; }`
  - Summary: Gets the total number of written characters
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `int NextPosition { get; }`
  - Summary: This equals plus any indentation that must be written before the next text.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerOutput.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NextPosition;
    ```

## Interface `IDecompilerProvider`

Returns decompilers. It must have a default constructor.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.IDecompilerProvider and call its members.
var instance = new dnSpy.Contracts.Decompiler.IDecompilerProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerProvider.cs` (line 26)

### Methods

- `IEnumerable<IDecompiler> Create()`
  - Summary: Creates all decompilers it can create
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IDecompilerProvider.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```

## Interface `IDecompilerService`

Decompiler manager

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.IDecompilerService and call its members.
var instance = new dnSpy.Contracts.Decompiler.IDecompilerService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IDecompilerService.cs` (line 27)

### Methods

- `IDecompiler Find(Guid guid)`
  - Summary: Finds a instance. null is returned if it wasn't found
  - Parameters:
    - `Guid guid`: Language guid, see and
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IDecompilerService.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.Find(guid: /* Guid */);
    ```
- `IDecompiler FindOrDefault(Guid guid)`
  - Summary: Finds a instance. Returns the first one if the language wasn't found
  - Parameters:
    - `Guid guid`: Language guid, see and
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IDecompilerService.cs` (line 55)
  - Example:
    ```csharp
    // Example invocation
    instance.FindOrDefault(guid: /* Guid */);
    ```

### Properties

- `IDecompiler Decompiler { get; set; }`
  - Summary: Current default decompiler
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IDecompilerService.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Decompiler;
    ```
- `IEnumerable<IDecompiler> AllDecompilers { get; }`
  - Summary: Gets all languages
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IDecompilerService.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AllDecompilers;
    ```

### Events

- `event EventHandler<EventArgs> DecompilerChanged`
  - Summary: Raised when has been updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IDecompilerService.cs` (line 41)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.DecompilerChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Interface `IInstructionBytesReader`

Instruction bytes reader

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.IInstructionBytesReader and call its members.
var instance = new dnSpy.Contracts.Decompiler.IInstructionBytesReader(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IInstructionBytesReader.cs` (line 24)

### Methods

- `int ReadByte()`
  - Summary: Reads the next byte or returns a value less than 0 if the byte is unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IInstructionBytesReader.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.ReadByte();
    ```
- `void SetInstruction(int index, uint offset)`
  - Summary: Initializes the next instruction that should be read
  - Parameters:
    - `int index`: Index of the instruction in the method body
    - `uint offset`: Offset of the instruction in the stream
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IInstructionBytesReader.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.SetInstruction(index: /* int */, offset: /* uint */);
    ```

### Properties

- `bool IsOriginalBytes { get; }`
  - Summary: true if it's reading the original bytes, false if the method has been modified
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IInstructionBytesReader.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsOriginalBytes;
    ```

## Struct `ILSpan`

IL span

**Inherits/Implements:** `IEquatable<ILSpan>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.ILSpan(start: /* uint */, length: /* uint */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 28)

### Constructors

- `public ILSpan(uint start, uint length)`
  - Summary: Constructor
  - Parameters:
    - `uint start`: Start offset
    - `uint length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 56)

### Methods

- `public bool Equals(ILSpan other)`
  - Summary: Equals()
  - Parameters:
    - `ILSpan other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 139)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* ILSpan */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 152)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 158)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static ILSpan FromBounds(uint start, uint end)`
  - Summary: Creates a new instance
  - Parameters:
    - `uint start`: Start offset
    - `uint end`: End offset
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ILSpan.FromBounds(start: /* uint */, end: /* uint */);
    ```
- `public static List<ILSpan> OrderAndCompact(IEnumerable<ILSpan> input)`
  - Summary: Sorts and compacts
  - Parameters:
    - `IEnumerable<ILSpan> input`: Input values
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 78)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ILSpan.OrderAndCompact(input: /* IEnumerable<ILSpan> */);
    ```
- `public static List<ILSpan> OrderAndCompactList(List<ILSpan> input)`
  - Summary: Sorts and compacts
  - Parameters:
    - `List<ILSpan> input`: Input list. It can be sorted, and it can also be returned to the caller.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 85)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ILSpan.OrderAndCompactList(input: /* List<ILSpan> */);
    ```

### Properties

- `public bool IsEmpty => end == start`
  - Summary: true if it's empty ( is 0)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public uint End => end`
  - Summary: End offset, exclusive
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 39)
  - Example:
    ```csharp
    // Read the property
    var value = instance.End;
    ```
- `public uint Length => end - start`
  - Summary: Length ( - )
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 44)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public uint Start => start`
  - Summary: Start offset
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Start;
    ```

### Operators

- `public static bool operator !=(ILSpan left, ILSpan right) => !left.Equals(right);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 132)
- `public static bool operator ==(ILSpan left, ILSpan right) => left.Equals(right);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ILSpan.cs` (line 124)

## Interface `IMethodDebugService`

Method debug info service

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.IMethodDebugService and call its members.
var instance = new dnSpy.Contracts.Decompiler.IMethodDebugService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 31)

### Methods

- `IEnumerable<MethodSourceStatement> GetStatementsByTextSpan(Span span)`
  - Summary: Gets all s that intersect a span
  - Parameters:
    - `Span span`: Span
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.GetStatementsByTextSpan(span: /* Span */);
    ```
- `IList<MethodSourceStatement> FindByTextPosition(int textPosition, FindByTextPositionOptions options = FindByTextPositionOptions.None)`
  - Summary: Gets s
  - Parameters:
    - `int textPosition`: Text position
    - `FindByTextPositionOptions options` (default: `FindByTextPositionOptions.None`): Options
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    instance.FindByTextPosition(textPosition: /* int */, options: /* FindByTextPositionOptions */);
    ```
- `MethodDebugInfo TryGetMethodDebugInfo(MethodDef method)`
  - Summary: Gets a or null if it doesn't exist
  - Parameters:
    - `MethodDef method`: Method
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 66)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetMethodDebugInfo(method: /* MethodDef */);
    ```
- `MethodDebugInfo TryGetMethodDebugInfo(ModuleTokenId token)`
  - Summary: Gets a or null if it doesn't exist
  - Parameters:
    - `ModuleTokenId token`: Token
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 73)
  - Example:
    ```csharp
    // Example invocation
    instance.TryGetMethodDebugInfo(token: /* ModuleTokenId */);
    ```
- `MethodSourceStatement? FindByCodeOffset(MethodDef method, uint codeOffset)`
  - Summary: Gets a code
  - Parameters:
    - `MethodDef method`: Method
    - `uint codeOffset`: Code offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 51)
  - Example:
    ```csharp
    // Example invocation
    instance.FindByCodeOffset(method: /* MethodDef */, codeOffset: /* uint */);
    ```
- `MethodSourceStatement? FindByCodeOffset(ModuleTokenId token, uint codeOffset)`
  - Summary: Gets a code
  - Parameters:
    - `ModuleTokenId token`: Token
    - `uint codeOffset`: Code offset
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.FindByCodeOffset(token: /* ModuleTokenId */, codeOffset: /* uint */);
    ```

### Properties

- `int Count { get; }`
  - Summary: Gets the number of s
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Count;
    ```

## Interface `ISimpleILPrinter`

Simple IL printer. Only used by the asm editor

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.ISimpleILPrinter and call its members.
var instance = new dnSpy.Contracts.Decompiler.ISimpleILPrinter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISimpleILPrinter.cs` (line 26)

### Methods

- `bool Write(IDecompilerOutput output, IMemberRef member)`
  - Summary: Writes a line to
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `IMemberRef member`: Member
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISimpleILPrinter.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* IDecompilerOutput */, member: /* IMemberRef */);
    ```
- `void Write(IDecompilerOutput output, MethodSig sig)`
  - Summary: Writes a method signature
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `MethodSig sig`: Signature
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISimpleILPrinter.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* IDecompilerOutput */, sig: /* MethodSig */);
    ```
- `void Write(IDecompilerOutput output, TypeSig type)`
  - Summary: Writes a type
  - Parameters:
    - `IDecompilerOutput output`: Output
    - `TypeSig type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISimpleILPrinter.cs` (line 52)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(output: /* IDecompilerOutput */, type: /* TypeSig */);
    ```

### Properties

- `double Order { get; }`
  - Summary: Gets the order
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISimpleILPrinter.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Order;
    ```

## Interface `ISourceVariable`

A local or parameter present in decompiled code

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.ISourceVariable and call its members.
var instance = new dnSpy.Contracts.Decompiler.ISourceVariable(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISourceVariable.cs` (line 27)

### Properties

- `FieldDef HoistedField { get; }`
  - Summary: Gets the hoisted field or null if it's not a hoisted local/parameter
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISourceVariable.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HoistedField;
    ```
- `IVariable Variable { get; }`
  - Summary: Gets the real local or parameter or null if it's a decompiler generated variable
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISourceVariable.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Variable;
    ```
- `SourceVariableFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISourceVariable.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `TypeSig Type { get; }`
  - Summary: Gets the type of the variable
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISourceVariable.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `bool IsDecompilerGenerated { get; }`
  - Summary: true if this is a decompiler generated variable
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISourceVariable.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDecompilerGenerated;
    ```
- `bool IsLocal { get; }`
  - Summary: true if this is a local
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISourceVariable.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsLocal;
    ```
- `bool IsParameter { get; }`
  - Summary: true if this is a parameter
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISourceVariable.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsParameter;
    ```
- `string Name { get; }`
  - Summary: Gets the name of the variable the decompiler used. It could be different from the real name if the decompiler renamed it.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISourceVariable.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Interface `IXamlOutputOptionsProvider`

Provides

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.IXamlOutputOptionsProvider and call its members.
var instance = new dnSpy.Contracts.Decompiler.IXamlOutputOptionsProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IBamlDecompiler.cs` (line 46)

### Properties

- `XamlOutputOptions Default { get; }`
  - Summary: Gets the default options that gets changed by the user
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IBamlDecompiler.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Default;
    ```

## Class `IdentifierEscaper`

Escapes identifiers

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.IdentifierEscaper members directly without instantiation.
dnSpy.Contracts.Decompiler.IdentifierEscaper./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IdentifierEscaper.cs` (line 27)

### Methods

- `public static string Escape(string id)`
  - Summary: Escapes an identifier
  - Parameters:
    - `string id`: Identifier
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IdentifierEscaper.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.IdentifierEscaper.Escape(id: /* string */);
    ```
- `public static string Escape(string id, int maxLength, bool allowSpaces)`
  - Summary: Escapes an identifier
  - Parameters:
    - `string id`: Identifier
    - `int maxLength`: Max length
    - `bool allowSpaces`: true to allow spaces
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IdentifierEscaper.cs` (line 65)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.IdentifierEscaper.Escape(id: /* string */, maxLength: /* int */, allowSpaces: /* bool */);
    ```
- `public static string Truncate(string s)`
  - Summary: Truncates the length of if it's too long
  - Parameters:
    - `string s`: Identifier string
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IdentifierEscaper.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.IdentifierEscaper.Truncate(s: /* string */);
    ```
- `public static string Truncate(string s, int maxLength)`
  - Summary: Truncates the length of if it's too long
  - Parameters:
    - `string s`: Identifier string
    - `int maxLength`: Max length
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IdentifierEscaper.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.IdentifierEscaper.Truncate(s: /* string */, maxLength: /* int */);
    ```

## Struct `ImportInfo`

Import info

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.ImportInfo(targetKind: /* ImportInfoKind */, target: /* string */, alias: /* string */, externAlias: /* string */, importScopeKind: /* VBImportScopeKind */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 138)

### Constructors

- `public ImportInfo(ImportInfoKind targetKind, string target = null, string alias = null, string externAlias = null, VBImportScopeKind importScopeKind = VBImportScopeKind.None)`
  - Summary: Constructor
  - Parameters:
    - `ImportInfoKind targetKind`: Target kind
    - `string target` (default: `null`): Target string
    - `string alias` (default: `null`): Alias
    - `string externAlias` (default: `null`): Extern alias
    - `VBImportScopeKind importScopeKind` (default: `VBImportScopeKind.None`): VB import scope kind
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 172)

### Methods

- `public static ImportInfo CreateAssembly(string externAlias)`
  - Parameters:
    - `string externAlias`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 187)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateAssembly(externAlias: /* string */);
    ```
- `public static ImportInfo CreateAssembly(string externAlias, string assembly)`
  - Parameters:
    - `string externAlias`: Description not provided.
    - `string assembly`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateAssembly(externAlias: /* string */, assembly: /* string */);
    ```
- `public static ImportInfo CreateCurrentNamespace()`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 189)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateCurrentNamespace();
    ```
- `public static ImportInfo CreateDefaultNamespace(string @namespace)`
  - Parameters:
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 195)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateDefaultNamespace(@namespace: /* string */);
    ```
- `public static ImportInfo CreateMethodToken(string token, VBImportScopeKind importScopeKind)`
  - Parameters:
    - `string token`: Description not provided.
    - `VBImportScopeKind importScopeKind`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 194)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateMethodToken(token: /* string */, importScopeKind: /* VBImportScopeKind */);
    ```
- `public static ImportInfo CreateNamespace(string @namespace)`
  - Parameters:
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateNamespace(@namespace: /* string */);
    ```
- `public static ImportInfo CreateNamespace(string @namespace, VBImportScopeKind importScopeKind)`
  - Parameters:
    - `string @namespace`: Description not provided.
    - `VBImportScopeKind importScopeKind`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 193)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateNamespace(@namespace: /* string */, importScopeKind: /* VBImportScopeKind */);
    ```
- `public static ImportInfo CreateNamespace(string @namespace, string externAlias)`
  - Parameters:
    - `string @namespace`: Description not provided.
    - `string externAlias`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 182)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateNamespace(@namespace: /* string */, externAlias: /* string */);
    ```
- `public static ImportInfo CreateNamespaceAlias(string @namespace, string alias)`
  - Parameters:
    - `string @namespace`: Description not provided.
    - `string alias`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 184)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateNamespaceAlias(@namespace: /* string */, alias: /* string */);
    ```
- `public static ImportInfo CreateNamespaceAlias(string @namespace, string alias, string externAlias)`
  - Parameters:
    - `string @namespace`: Description not provided.
    - `string alias`: Description not provided.
    - `string externAlias`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 186)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateNamespaceAlias(@namespace: /* string */, alias: /* string */, externAlias: /* string */);
    ```
- `public static ImportInfo CreateNamespaceOrType(string namespaceOrType, string alias, VBImportScopeKind importScopeKind)`
  - Parameters:
    - `string namespaceOrType`: Description not provided.
    - `string alias`: Description not provided.
    - `VBImportScopeKind importScopeKind`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 190)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateNamespaceOrType(namespaceOrType: /* string */, alias: /* string */, importScopeKind: /* VBImportScopeKind */);
    ```
- `public static ImportInfo CreateType(string type)`
  - Parameters:
    - `string type`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 183)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateType(type: /* string */);
    ```
- `public static ImportInfo CreateType(string type, VBImportScopeKind importScopeKind)`
  - Parameters:
    - `string type`: Description not provided.
    - `VBImportScopeKind importScopeKind`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 192)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateType(type: /* string */, importScopeKind: /* VBImportScopeKind */);
    ```
- `public static ImportInfo CreateTypeAlias(string type, string alias)`
  - Parameters:
    - `string type`: Description not provided.
    - `string alias`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 185)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateTypeAlias(type: /* string */, alias: /* string */);
    ```
- `public static ImportInfo CreateXmlNamespace(string xmlNamespace, string alias, VBImportScopeKind importScopeKind)`
  - Parameters:
    - `string xmlNamespace`: Description not provided.
    - `string alias`: Description not provided.
    - `VBImportScopeKind importScopeKind`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 191)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.ImportInfo.CreateXmlNamespace(xmlNamespace: /* string */, alias: /* string */, importScopeKind: /* VBImportScopeKind */);
    ```

### Properties

- `public ImportInfoKind TargetKind { get; }`
  - Summary: Target kind
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 142)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TargetKind;
    ```
- `public VBImportScopeKind VBImportScopeKind { get; }`
  - Summary: Gets the VB import scope kind
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 147)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VBImportScopeKind;
    ```
- `public string Alias { get; }`
  - Summary: Alias
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 157)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Alias;
    ```
- `public string ExternAlias { get; }`
  - Summary: Extern alias
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 162)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ExternAlias;
    ```
- `public string Target { get; }`
  - Summary: Target
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 152)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Target;
    ```

## Enum `ImportInfoKind`

Import kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.ImportInfoKind and call its members.
var instance = new dnSpy.Contracts.Decompiler.ImportInfoKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 73)

### Members

- `Namespace`: Namespace import
- `Type`: Type import
- `NamespaceOrType`: Namespace or type import
- `Assembly`: C#: extern alias
- `XmlNamespace`: VB: XML import
- `MethodToken`: VB: token of method with imports
- `CurrentNamespace`: VB: containing namespace
- `DefaultNamespace`: VB: root namespace

## Class `InstructionReference`

Instruction reference

**Inherits/Implements:** `IEquatable<InstructionReference>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.InstructionReference(method: /* MethodDef */, instruction: /* Instruction */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/InstructionReference.cs` (line 28)

### Constructors

- `public InstructionReference(MethodDef method, Instruction instruction)`
  - Summary: Constructor
  - Parameters:
    - `MethodDef method`: Method
    - `Instruction instruction`: Instruction
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/InstructionReference.cs` (line 44)

### Methods

- `public bool Equals(InstructionReference other)`
  - Summary: Equals()
  - Parameters:
    - `InstructionReference other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/InstructionReference.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* InstructionReference */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/InstructionReference.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/InstructionReference.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public Instruction Instruction { get; }`
  - Summary: Instruction
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/InstructionReference.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Instruction;
    ```
- `public MethodDef Method { get; }`
  - Summary: Method
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/InstructionReference.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Method;
    ```

## Struct `LineSeparator`

Line separator

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.LineSeparator(position: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/LineSeparator.cs` (line 24)

### Constructors

- `public LineSeparator(int position)`
  - Summary: Constructor
  - Parameters:
    - `int position`: Position of the line that gets a line separator
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/LineSeparator.cs` (line 34)

### Properties

- `public int Position { get; }`
  - Summary: Gets the position of the line that gets a line separator
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/LineSeparator.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Position;
    ```

## Class `MemberRefComparer<T>`

Member comparer base class

**Inherits/Implements:** `IComparer<T>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.MemberRefComparer<T> and call its members.
var instance = new dnSpy.Contracts.Decompiler.MemberRefComparer<T>(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 29)

### Methods

- `public int Compare(T x, T y)`
  - Summary: Compares two instances
  - Parameters:
    - `T x`: First instance to compare
    - `T y`: Second instance to compare
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    instance.Compare(x: /* T */, y: /* T */);
    ```

## Class `MetadataTextColorProvider`

Provides text colors

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.MetadataTextColorProvider and call its members.
var instance = new dnSpy.Contracts.Decompiler.MetadataTextColorProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 28)

### Methods

- `public virtual object GetColor(ExportedType exportedType)`
  - Summary: Gets an exported type color
  - Parameters:
    - `ExportedType exportedType`: Exported type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 198)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColor(exportedType: /* ExportedType */);
    ```
- `public virtual object GetColor(GenericParam genericParam)`
  - Summary: Gets a generic parameter color
  - Parameters:
    - `GenericParam genericParam`: Generic parameter
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 172)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColor(genericParam: /* GenericParam */);
    ```
- `public virtual object GetColor(GenericSig genericSig)`
  - Summary: Gets a generic signature color
  - Parameters:
    - `GenericSig genericSig`: Generic signature
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 160)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColor(genericSig: /* GenericSig */);
    ```
- `public virtual object GetColor(IMemberRef memberRef)`
  - Summary: Gets a member color
  - Parameters:
    - `IMemberRef memberRef`: Member
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColor(memberRef: /* IMemberRef */);
    ```
- `public virtual object GetColor(TypeDef type)`
  - Summary: Gets a type color
  - Parameters:
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 34)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColor(type: /* TypeDef */);
    ```
- `public virtual object GetColor(TypeRef type)`
  - Summary: Gets a type color
  - Parameters:
    - `TypeRef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 75)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColor(type: /* TypeRef */);
    ```
- `public virtual object GetColor(TypeSig typeSig)`
  - Summary: Gets a type signature color
  - Parameters:
    - `TypeSig typeSig`: Type signature
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 210)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColor(typeSig: /* TypeSig */);
    ```
- `public virtual object GetColor(object obj)`
  - Summary: Gets a color
  - Parameters:
    - `object obj`: Object, eg. an instruction operand
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 229)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColor(obj: /* object */);
    ```

## Struct `MethodDebugConstant`

A constant value

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.MethodDebugConstant(name: /* string */, type: /* TypeSig */, value: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 202)

### Constructors

- `public MethodDebugConstant(string name, TypeSig type, object value)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name of constant
    - `TypeSig type`: Type of constant
    - `object value`: Constant value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 224)

### Properties

- `public TypeSig Type { get; }`
  - Summary: Gets the type of the constant
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 211)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public object Value { get; }`
  - Summary: Gets the constant value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 216)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public string Name { get; }`
  - Summary: Gets the name of the constant
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 206)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `MethodDebugInfo`

Method debug info

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.MethodDebugInfo(compilerName: /* string */, decompilerSettingsVersion: /* int */, stateMachineKind: /* StateMachineKind */, method: /* MethodDef */, kickoffMethod: /* MethodDef */, parameters: /* SourceParameter[] */, statements: /* SourceStatement[] */, scope: /* MethodDebugScope */, methodSpan: /* TextSpan? */, asyncMethodDebugInfo: /* AsyncMethodDebugInfo */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 28)

### Constructors

- `public MethodDebugInfo(string compilerName, int decompilerSettingsVersion, StateMachineKind stateMachineKind, MethodDef method, MethodDef kickoffMethod, SourceParameter[] parameters, SourceStatement[] statements, MethodDebugScope scope, TextSpan? methodSpan, AsyncMethodDebugInfo asyncMethodDebugInfo)`
  - Summary: Constructor
  - Parameters:
    - `string compilerName`: Compiler name () or null
    - `int decompilerSettingsVersion`: Decompiler settings version number. This version number should get incremented when the settings change.
    - `StateMachineKind stateMachineKind`: State machine kind
    - `MethodDef method`: Method
    - `MethodDef kickoffMethod`: Kickoff method or null
    - `SourceParameter[] parameters`: Parameters or null
    - `SourceStatement[] statements`: Statements
    - `MethodDebugScope scope`: Root scope
    - `TextSpan? methodSpan`: Method span or null to calculate it from
    - `AsyncMethodDebugInfo asyncMethodDebugInfo`: Async info or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 97)

### Methods

- `public SourceStatement? GetSourceStatementByCodeOffset(uint ilOffset)`
  - Summary: Gets a
  - Parameters:
    - `uint ilOffset`: IL offset
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 174)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSourceStatementByCodeOffset(ilOffset: /* uint */);
    ```
- `public SourceStatement? GetSourceStatementByTextOffset(int lineStart, int lineEnd, int textPosition)`
  - Summary: Gets a
  - Parameters:
    - `int lineStart`: Offset of start of line
    - `int lineEnd`: Offset of end of line
    - `int textPosition`: Position in text document
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 132)
  - Example:
    ```csharp
    // Example invocation
    instance.GetSourceStatementByTextOffset(lineStart: /* int */, lineEnd: /* int */, textPosition: /* int */);
    ```

### Properties

- `public AsyncMethodDebugInfo AsyncInfo { get; }`
  - Summary: Gets async info or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 67)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsyncInfo;
    ```
- `public MethodDebugScope Scope { get; }`
  - Summary: Gets the root scope
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Scope;
    ```
- `public MethodDef KickoffMethod { get; }`
  - Summary: Gets the kickoff method or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.KickoffMethod;
    ```
- `public MethodDef Method { get; }`
  - Summary: Gets the method
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Method;
    ```
- `public SourceParameter[] Parameters { get; }`
  - Summary: Gets the parameters. There could be missing parameters, in which case use . This array isn't sorted.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Parameters;
    ```
- `public SourceStatement[] Statements { get; }`
  - Summary: Gets all statements, sorted by
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Statements;
    ```
- `public StateMachineKind StateMachineKind { get; }`
  - Summary: Gets the state machine kind
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StateMachineKind;
    ```
- `public TextSpan Span { get; }`
  - Summary: Method span or the default value (position 0, length 0) if it's not known
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 77)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public bool HasSpan => Span.Start != 0 && Span.End != 0`
  - Summary: true if is a valid method span
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 82)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasSpan;
    ```
- `public int DecompilerSettingsVersion { get; }`
  - Summary: Decompiler options version number
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DecompilerSettingsVersion;
    ```
- `public string CompilerName { get; }`
  - Summary: Compiler name () or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CompilerName;
    ```

## Class `MethodDebugInfoBuilder`

Builds instances

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.MethodDebugInfoBuilder(decompilerSettingsVersion: /* int */, stateMachineKind: /* StateMachineKind */, method: /* MethodDef */, kickoffMethod: /* MethodDef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 28)

### Constructors

- `public MethodDebugInfoBuilder(int decompilerSettingsVersion, StateMachineKind stateMachineKind, MethodDef method, MethodDef kickoffMethod)`
  - Summary: Constructor
  - Parameters:
    - `int decompilerSettingsVersion`: Decompiler settings version number. This version number should get incremented when the settings change.
    - `StateMachineKind stateMachineKind`: State machine kind
    - `MethodDef method`: Method
    - `MethodDef kickoffMethod`: Kickoff method or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 73)
- `public MethodDebugInfoBuilder(int decompilerSettingsVersion, StateMachineKind stateMachineKind, MethodDef method, MethodDef kickoffMethod, SourceLocal[] locals, SourceParameter[] parameters, AsyncMethodDebugInfo asyncInfo)`
  - Summary: Constructor
  - Parameters:
    - `int decompilerSettingsVersion`: Decompiler settings version number. This version number should get incremented when the settings change.
    - `StateMachineKind stateMachineKind`: State machine kind
    - `MethodDef method`: Method
    - `MethodDef kickoffMethod`: Kickoff method or null
    - `SourceLocal[] locals`: Locals
    - `SourceParameter[] parameters`: Parameters or null
    - `AsyncMethodDebugInfo asyncInfo`: Async method info or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 95)

### Methods

- `public MethodDebugInfo Create()`
  - Summary: Creates a
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 112)
  - Example:
    ```csharp
    // Example invocation
    instance.Create();
    ```
- `public void Add(SourceStatement statement)`
  - Summary: Adds a
  - Parameters:
    - `SourceStatement statement`: Statement
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.Add(statement: /* SourceStatement */);
    ```

### Properties

- `public AsyncMethodDebugInfo AsyncInfo { get; set; }`
  - Summary: Async method debug info or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AsyncInfo;
    ```
- `public MethodDebugScopeBuilder Scope { get; }`
  - Summary: Gets the scope builder
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Scope;
    ```
- `public SourceParameter[] Parameters { get; set; }`
  - Summary: Gets/sets the parameters
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Parameters;
    ```
- `public int? EndPosition { get; set; }`
  - Summary: End of method (eg. after the last brace)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.EndPosition;
    ```
- `public int? StartPosition { get; set; }`
  - Summary: Start of method (eg. position of the first character of the modifier or return type)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StartPosition;
    ```
- `public string CompilerName { get; set; }`
  - Summary: Compiler name () or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfoBuilder.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CompilerName;
    ```

## Class `MethodDebugScope`

Method scope

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.MethodDebugScope(span: /* ILSpan */, scopes: /* MethodDebugScope[] */, locals: /* SourceLocal[] */, imports: /* ImportInfo[] */, constants: /* MethodDebugConstant[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 27)

### Constructors

- `public MethodDebugScope(ILSpan span, MethodDebugScope[] scopes, SourceLocal[] locals, ImportInfo[] imports, MethodDebugConstant[] constants)`
  - Summary: Constructor
  - Parameters:
    - `ILSpan span`: Scope span
    - `MethodDebugScope[] scopes`: Child scopes
    - `SourceLocal[] locals`: Locals
    - `ImportInfo[] imports`: Imports
    - `MethodDebugConstant[] constants`: Constants
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 61)

### Properties

- `public ILSpan Span { get; }`
  - Summary: Gets the span of this scope
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public ImportInfo[] Imports { get; }`
  - Summary: Gets all new imports in the scope
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Imports;
    ```
- `public MethodDebugConstant[] Constants { get; }`
  - Summary: Gets all new constants in the scope
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Constants;
    ```
- `public MethodDebugScope[] Scopes { get; }`
  - Summary: Gets all child scopes
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Scopes;
    ```
- `public SourceLocal[] Locals { get; }`
  - Summary: Gets all new locals in the scope
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Locals;
    ```

## Class `MethodDebugScopeBuilder`

builder

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.MethodDebugScopeBuilder();
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScopeBuilder.cs` (line 27)

### Constructors

- `public MethodDebugScopeBuilder()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScopeBuilder.cs` (line 84)

### Methods

- `public MethodDebugScope ToScope()`
  - Summary: Creates a new instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScopeBuilder.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.ToScope();
    ```

### Properties

- `public ILSpan Span { get; set; }`
  - Summary: Gets the span of this scope
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScopeBuilder.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public List<ImportInfo> Imports {
			get {
				if (imports == null)
					imports = new List<ImportInfo>();
				return imports;
			}
		}`
  - Summary: Gets all new imports in the scope
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScopeBuilder.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Imports;
    ```
- `public List<MethodDebugConstant> Constants {
			get {
				if (constants == null)
					constants = new List<MethodDebugConstant>();
				return constants;
			}
		}`
  - Summary: Gets all new constants in the scope
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScopeBuilder.cs` (line 72)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Constants;
    ```
- `public List<MethodDebugScopeBuilder> Scopes {
			get {
				if (scopes == null)
					scopes = new List<MethodDebugScopeBuilder>();
				return scopes;
			}
		}`
  - Summary: Gets all child scopes
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScopeBuilder.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Scopes;
    ```
- `public List<SourceLocal> Locals {
			get {
				if (locals == null)
					locals = new List<SourceLocal>();
				return locals;
			}
		}`
  - Summary: Gets all new locals in the scope
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScopeBuilder.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Locals;
    ```

## Class `MethodDebugServiceExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.MethodDebugServiceExtensions members directly without instantiation.
dnSpy.Contracts.Decompiler.MethodDebugServiceExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 117)

### Methods

- `public static IMethodDebugService GetMethodDebugService(this IDocumentViewer self)`
  - Summary: Gets a instance
  - Parameters:
    - `this IDocumentViewer self`: This
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 123)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.MethodDebugServiceExtensions.GetMethodDebugService(self: /* IDocumentViewer */);
    ```
- `public static IMethodDebugService TryGetMethodDebugService(this IDocumentViewer self)`
  - Summary: Gets a or null if none exists
  - Parameters:
    - `this IDocumentViewer self`: This
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Decompiler/IMethodDebugService.cs` (line 130)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.MethodDebugServiceExtensions.TryGetMethodDebugService(self: /* IDocumentViewer */);
    ```

## Class `MethodDefComparer`

comparer

**Inherits/Implements:** `IComparer<MethodDef>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.MethodDefComparer and call its members.
var instance = new dnSpy.Contracts.Decompiler.MethodDefComparer(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 90)

### Methods

- `public int Compare(MethodDef x, MethodDef y)`
  - Summary: Compares two instances
  - Parameters:
    - `MethodDef x`: First instance to compare
    - `MethodDef y`: Second instance to compare
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 102)
  - Example:
    ```csharp
    // Example invocation
    instance.Compare(x: /* MethodDef */, y: /* MethodDef */);
    ```

### Fields

- `public static readonly MethodDefComparer Instance = new MethodDefComparer()`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 94)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.MethodDefComparer.Instance;
    ```

## Struct `MethodSourceStatement`

Method and statement

**Inherits/Implements:** `IEquatable<MethodSourceStatement>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.MethodSourceStatement(method: /* MethodDef */, statement: /* SourceStatement */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodSourceStatement.cs` (line 27)

### Constructors

- `public MethodSourceStatement(MethodDef method, SourceStatement statement)`
  - Summary: Constructor
  - Parameters:
    - `MethodDef method`: Method
    - `SourceStatement statement`: Statement
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodSourceStatement.cs` (line 43)

### Methods

- `public bool Equals(MethodSourceStatement other)`
  - Summary: Equals()
  - Parameters:
    - `MethodSourceStatement other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodSourceStatement.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* MethodSourceStatement */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodSourceStatement.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodSourceStatement.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodSourceStatement.cs` (line 88)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public MethodDef Method { get; }`
  - Summary: Gets the method
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodSourceStatement.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Method;
    ```
- `public SourceStatement Statement { get; }`
  - Summary: Gets the statement
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodSourceStatement.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Statement;
    ```

### Operators

- `public static bool operator !=(MethodSourceStatement left, MethodSourceStatement right) => !left.Equals(right);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodSourceStatement.cs` (line 62)
- `public static bool operator ==(MethodSourceStatement left, MethodSourceStatement right) => left.Equals(right);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodSourceStatement.cs` (line 54)

## Class `MethodStatementReference`

Method statement reference

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.MethodStatementReference(method: /* MethodDef */, offset: /* uint? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodStatementReference.cs` (line 27)

### Constructors

- `public MethodStatementReference(MethodDef method, uint? offset)`
  - Summary: Constructor
  - Parameters:
    - `MethodDef method`: Method
    - `uint? offset`: Offset or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodStatementReference.cs` (line 43)

### Methods

- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodStatementReference.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodStatementReference.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public MethodDef Method { get; }`
  - Summary: Gets the method
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodStatementReference.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Method;
    ```
- `public uint? Offset { get; }`
  - Summary: Gets the offset or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodStatementReference.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Offset;
    ```

## Class `NamespaceReference`

Namespace reference

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.NamespaceReference(assembly: /* IAssembly */, @namespace: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/NamespaceReference.cs` (line 27)

### Constructors

- `public NamespaceReference(IAssembly assembly, string @namespace)`
  - Summary: Constructor
  - Parameters:
    - `IAssembly assembly`: Target assembly
    - `string @namespace`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/NamespaceReference.cs` (line 43)

### Methods

- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/NamespaceReference.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/NamespaceReference.cs` (line 59)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```

### Properties

- `public AssemblyRef Assembly { get; }`
  - Summary: Gets the assembly, could be null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/NamespaceReference.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Assembly;
    ```
- `public string Namespace { get; }`
  - Summary: Gets the namespace or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/NamespaceReference.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Namespace;
    ```

## Class `PredefinedCompilerNames`

Compiler names

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.PredefinedCompilerNames members directly without instantiation.
dnSpy.Contracts.Decompiler.PredefinedCompilerNames./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedCompilerNames.cs` (line 24)

### Fields

- `public const string MicrosoftCSharp = nameof(MicrosoftCSharp)`
  - Summary: Microsoft C# compiler
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedCompilerNames.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.PredefinedCompilerNames.MicrosoftCSharp;
    ```
- `public const string MicrosoftVisualBasic = nameof(MicrosoftVisualBasic)`
  - Summary: Microsoft Visual Basic compiler
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedCompilerNames.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.PredefinedCompilerNames.MicrosoftVisualBasic;
    ```
- `public const string MonoCSharp = nameof(MonoCSharp)`
  - Summary: Mono C# compiler
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedCompilerNames.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.PredefinedCompilerNames.MonoCSharp;
    ```

## Class `PredefinedCustomDataIds`

Predefined custom data IDs passed to

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.PredefinedCustomDataIds members directly without instantiation.
dnSpy.Contracts.Decompiler.PredefinedCustomDataIds./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedCustomDataIds.cs` (line 24)

### Fields

- `public const string CodeBracesRange = nameof(CodeBracesRange)`
  - Summary: TData =
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedCustomDataIds.cs` (line 38)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.PredefinedCustomDataIds.CodeBracesRange;
    ```
- `public const string DebugInfo = nameof(DebugInfo)`
  - Summary: TData =
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedCustomDataIds.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.PredefinedCustomDataIds.DebugInfo;
    ```
- `public const string LineSeparator = nameof(LineSeparator)`
  - Summary: TData =
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedCustomDataIds.cs` (line 43)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.PredefinedCustomDataIds.LineSeparator;
    ```
- `public const string SpanReference = nameof(SpanReference)`
  - Summary: TData =
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedCustomDataIds.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.PredefinedCustomDataIds.SpanReference;
    ```

## Class `PredefinedSpanReferenceIds`

Ids used by

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.PredefinedSpanReferenceIds members directly without instantiation.
dnSpy.Contracts.Decompiler.PredefinedSpanReferenceIds./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedSpanReferenceIds.cs` (line 24)

### Fields

- `public const string HighlightRelatedKeywords = nameof(HighlightRelatedKeywords)`
  - Summary: Highlighted keyword reference, eg. related keywords are highlighted by default in Visual Basic, eg. 'If' and 'End If'.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/PredefinedSpanReferenceIds.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.PredefinedSpanReferenceIds.HighlightRelatedKeywords;
    ```

## Class `PropertyDefComparer`

comparer

**Inherits/Implements:** `MemberRefComparer<PropertyDef>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.PropertyDefComparer and call its members.
var instance = new dnSpy.Contracts.Decompiler.PropertyDefComparer(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 80)

### Fields

- `public static readonly PropertyDefComparer Instance = new PropertyDefComparer()`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 84)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.PropertyDefComparer.Instance;
    ```

## Class `SourceLocal`

A local present in decompiled code

**Inherits/Implements:** `ISourceVariable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.SourceLocal(local: /* Local */, name: /* string */, type: /* TypeSig */, flags: /* SourceVariableFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceLocal.cs` (line 29)

### Constructors

- `public SourceLocal(Local local, string name, FieldDef hoistedField, SourceVariableFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `Local local`: Local or null
    - `string name`: Name used by the decompiler
    - `FieldDef hoistedField`: Hoisted field
    - `SourceVariableFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceLocal.cs` (line 91)
- `public SourceLocal(Local local, string name, TypeSig type, SourceVariableFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `Local local`: Local or null
    - `string name`: Name used by the decompiler
    - `TypeSig type`: Type of local
    - `SourceVariableFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceLocal.cs` (line 71)

### Properties

- `public FieldDef HoistedField { get; }`
  - Summary: Gets the hoisted field or null if it's not a hoisted local
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceLocal.cs` (line 52)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HoistedField;
    ```
- `public Local Local { get; }`
  - Summary: The local or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceLocal.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Local;
    ```
- `public SourceVariableFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceLocal.cs` (line 57)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public TypeSig Type { get; }`
  - Summary: Gets the type of the local
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceLocal.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public bool IsDecompilerGenerated => (Flags & SourceVariableFlags.DecompilerGenerated) != 0`
  - Summary: true if this is a decompiler generated local
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceLocal.cs` (line 62)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDecompilerGenerated;
    ```
- `public string Name { get; }`
  - Summary: Gets the name of the local the decompiler used. It could be different from the real name if the decompiler renamed it.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceLocal.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `SourceParameter`

A parameter present in decompiled code

**Inherits/Implements:** `ISourceVariable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.SourceParameter(parameter: /* Parameter */, name: /* string */, type: /* TypeSig */, flags: /* SourceVariableFlags */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceParameter.cs` (line 27)

### Constructors

- `public SourceParameter(Parameter parameter, string name, FieldDef hoistedField, SourceVariableFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `Parameter parameter`: Parameter
    - `string name`: Name used by the decompiler
    - `FieldDef hoistedField`: Hoisted field
    - `SourceVariableFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceParameter.cs` (line 79)
- `public SourceParameter(Parameter parameter, string name, TypeSig type, SourceVariableFlags flags)`
  - Summary: Constructor
  - Parameters:
    - `Parameter parameter`: Parameter
    - `string name`: Name used by the decompiler
    - `TypeSig type`: Type of local
    - `SourceVariableFlags flags`: Flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceParameter.cs` (line 65)

### Properties

- `public FieldDef HoistedField { get; }`
  - Summary: Gets the hoisted field or null if it's not a hoisted parameter
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceParameter.cs` (line 51)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HoistedField;
    ```
- `public Parameter Parameter { get; }`
  - Summary: The parameter
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceParameter.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Parameter;
    ```
- `public SourceVariableFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceParameter.cs` (line 56)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public TypeSig Type { get; }`
  - Summary: Gets the type of the parameter
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceParameter.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Type;
    ```
- `public string Name { get; }`
  - Summary: Gets the name of the parameter the decompiler used. It could be different from the real name if the decompiler renamed it.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceParameter.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Struct `SourceStatement`

Source statement

**Inherits/Implements:** `IEquatable<SourceStatement>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.SourceStatement(ilSpan: /* ILSpan */, textSpan: /* TextSpan */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceStatement.cs` (line 27)

### Constructors

- `public SourceStatement(ILSpan ilSpan, TextSpan textSpan)`
  - Summary: Constructor
  - Parameters:
    - `ILSpan ilSpan`: IL span
    - `TextSpan textSpan`: Text span
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceStatement.cs` (line 51)

### Methods

- `public bool Equals(SourceStatement other)`
  - Summary: Equals()
  - Parameters:
    - `SourceStatement other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceStatement.cs` (line 77)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* SourceStatement */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceStatement.cs` (line 84)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceStatement.cs` (line 90)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceStatement.cs` (line 96)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public ILSpan ILSpan => ilSpan`
  - Summary: IL span
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceStatement.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ILSpan;
    ```
- `public TextSpan TextSpan => textSpan`
  - Summary: Text span
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceStatement.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TextSpan;
    ```

### Operators

- `public static bool operator !=(SourceStatement left, SourceStatement right) => !left.Equals(right);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceStatement.cs` (line 70)
- `public static bool operator ==(SourceStatement left, SourceStatement right) => left.Equals(right);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SourceStatement.cs` (line 62)

## Enum `SourceVariableFlags`

flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.SourceVariableFlags and call its members.
var instance = new dnSpy.Contracts.Decompiler.SourceVariableFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/ISourceVariable.cs` (line 72)

### Members

- `None`: No bit is set
- `DecompilerGenerated` = `x00000001`: Decompiler generated variable
- `ReadOnlyReference` = `x00000002`: Readonly reference, eg. a 'ref readonly' local

## Struct `SpanReference`

Contains a span, a reference and a reference id. Should be used for references to eg. keywords and is used by the Visual Basic decompiler to highlight eg. 'While', 'End While', etc. Normal clickable references should be created by calling . Use to add an instance.

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.SpanReference(reference: /* object */, span: /* TextSpan */, id: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/SpanReference.cs` (line 31)

### Constructors

- `public SpanReference(object reference, TextSpan span, string id)`
  - Summary: Constructor
  - Parameters:
    - `object reference`: Reference
    - `TextSpan span`: Span
    - `string id`: Reference id or null, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SpanReference.cs` (line 54)

### Properties

- `public TextSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SpanReference.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```
- `public object Reference { get; }`
  - Summary: Gets the reference
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SpanReference.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Reference;
    ```
- `public string Id { get; }`
  - Summary: Id or null (eg. ). This is used to enable or disable the reference. If null, it's always enabled.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/SpanReference.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Id;
    ```

## Enum `StateMachineKind`

State machine kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.StateMachineKind and call its members.
var instance = new dnSpy.Contracts.Decompiler.StateMachineKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugInfo.cs` (line 186)

### Members

- `None`: Not a state machine
- `IteratorMethod`: Iterator method state machine
- `AsyncMethod`: Async method state machine

## Class `StringBuilderDecompilerOutput`

Implements and writes the text to a

**Inherits/Implements:** `IDecompilerOutput`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.StringBuilderDecompilerOutput();
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 28)

### Constructors

- `public StringBuilderDecompilerOutput()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 49)
- `public StringBuilderDecompilerOutput(Indenter indenter)`
  - Summary: Constructor
  - Parameters:
    - `Indenter indenter`: Indenter
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 58)
- `public StringBuilderDecompilerOutput(StringBuilder stringBuilder, Indenter indenter = null)`
  - Summary: Constructor
  - Parameters:
    - `StringBuilder stringBuilder`: String builder to use. Its method gets called by the constructor
    - `Indenter indenter` (default: `null`): Indenter or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 68)

### Methods

- `public override string ToString()`
  - Summary: Gets the text
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 175)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public string GetText()`
  - Summary: Gets the text
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 169)
  - Example:
    ```csharp
    // Example invocation
    instance.GetText();
    ```
- `public virtual void DecreaseIndent()`
  - Summary: Decrements the indentation level. Nothing is added to the output stream.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 86)
  - Example:
    ```csharp
    // Example invocation
    instance.DecreaseIndent();
    ```
- `public virtual void IncreaseIndent()`
  - Summary: Increments the indentation level. Nothing is added to the output stream.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 81)
  - Example:
    ```csharp
    // Example invocation
    instance.IncreaseIndent();
    ```
- `public virtual void Write(string text)`
  - Summary: Writes text. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 119)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */);
    ```
- `public virtual void Write(string text, int index, int length, object color)`
  - Summary: Writes text and color. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `int index`: Index in
    - `int length`: Number of characters to write
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, index: /* int */, length: /* int */, color: /* object */);
    ```
- `public virtual void Write(string text, int index, int length, object reference, DecompilerReferenceFlags flags, object color)`
  - Summary: Writes text, color and a reference. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `int index`: Index in
    - `int length`: Number of characters to write
    - `object reference`: Reference
    - `DecompilerReferenceFlags flags`: Flags
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 159)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, index: /* int */, length: /* int */, reference: /* object */, flags: /* DecompilerReferenceFlags */, color: /* object */);
    ```
- `public virtual void Write(string text, object color)`
  - Summary: Writes text and color. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, color: /* object */);
    ```
- `public virtual void Write(string text, object reference, DecompilerReferenceFlags flags, object color)`
  - Summary: Writes text, color and a reference. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `object reference`: Reference
    - `DecompilerReferenceFlags flags`: Flags
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 144)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, reference: /* object */, flags: /* DecompilerReferenceFlags */, color: /* object */);
    ```
- `public virtual void WriteLine()`
  - Summary: Writes a new line without writing any indentation
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 91)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLine();
    ```

### Properties

- `public virtual int Length => sb.Length`
  - Summary: Gets the total length of the written text
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public virtual int NextPosition => sb.Length + (addIndent ? indenter.String.Length : 0)`
  - Summary: This equals plus any indentation that must be written before the next text.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/StringBuilderDecompilerOutput.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NextPosition;
    ```

## Class `TextColorWriterToDecompilerOutput`

Converts a to a

**Inherits/Implements:** `IDecompilerOutput`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.TextColorWriterToDecompilerOutput and call its members.
var instance = new dnSpy.Contracts.Decompiler.TextColorWriterToDecompilerOutput(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextColorWriterToDecompilerOutput.cs` (line 27)

### Methods

- `public static IDecompilerOutput Create(ITextColorWriter output)`
  - Summary: Creates a new instance
  - Parameters:
    - `ITextColorWriter output`: Output to use
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextColorWriterToDecompilerOutput.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TextColorWriterToDecompilerOutput.Create(output: /* ITextColorWriter */);
    ```

## Struct `TextSpan`

Text span

**Inherits/Implements:** `IEquatable<TextSpan>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.TextSpan(start: /* int */, length: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 26)

### Constructors

- `public TextSpan(int start, int length)`
  - Summary: Constructor
  - Parameters:
    - `int start`: Start offset
    - `int length`: Length
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 54)

### Methods

- `public bool Contains(int position)`
  - Summary: Checks if is inside this span
  - Parameters:
    - `int position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 92)
  - Example:
    ```csharp
    // Example invocation
    instance.Contains(position: /* int */);
    ```
- `public bool Equals(TextSpan other)`
  - Summary: Equals()
  - Parameters:
    - `TextSpan other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 106)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* TextSpan */);
    ```
- `public bool Intersects(int position)`
  - Summary: Checks if is inside this span
  - Parameters:
    - `int position`: Position
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 99)
  - Example:
    ```csharp
    // Example invocation
    instance.Intersects(position: /* int */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 113)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: GetHashCode()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 119)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 125)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static TextSpan FromBounds(int start, int end)`
  - Summary: Creates a new instance
  - Parameters:
    - `int start`: Start offset
    - `int end`: End offset
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TextSpan.FromBounds(start: /* int */, end: /* int */);
    ```

### Properties

- `public bool IsEmpty => end == start`
  - Summary: true if it's empty ( is 0)
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsEmpty;
    ```
- `public int End => end`
  - Summary: End offset, exclusive
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.End;
    ```
- `public int Length => end - start`
  - Summary: Length ( - )
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public int Start => start`
  - Summary: Start offset
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Start;
    ```

### Operators

- `public static bool operator !=(TextSpan left, TextSpan right) => !left.Equals(right);`
  - Summary: operator !=()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 85)
- `public static bool operator ==(TextSpan left, TextSpan right) => left.Equals(right);`
  - Summary: operator ==()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpan.cs` (line 77)

## Struct `TextSpanData<TData>`

Span and data

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.TextSpanData<TData>(span: /* TextSpan */, data: /* TData */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpanData.cs` (line 25)

### Constructors

- `public TextSpanData(TextSpan span, TData data)`
  - Summary: Constructor
  - Parameters:
    - `TextSpan span`: Span
    - `TData data`: Data
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpanData.cs` (line 41)

### Properties

- `public TData Data { get; }`
  - Summary: Gets the data
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpanData.cs` (line 34)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Data;
    ```
- `public TextSpan Span { get; }`
  - Summary: Gets the span
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextSpanData.cs` (line 29)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Span;
    ```

## Class `TextWriterDecompilerOutput`

Implements and writes the text to a

**Inherits/Implements:** `IDecompilerOutput`, `IDisposable`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.TextWriterDecompilerOutput(writer: /* TextWriter */, indenter: /* Indenter */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 28)

### Constructors

- `public TextWriterDecompilerOutput(TextWriter writer, Indenter indenter = null)`
  - Summary: Constructor
  - Parameters:
    - `TextWriter writer`: Text writer to use
    - `Indenter indenter` (default: `null`): Indenter or null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 52)

### Methods

- `public override string ToString()`
  - Summary: Returns the result from 's method
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 152)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public virtual void DecreaseIndent()`
  - Summary: Decrements the indentation level. Nothing is added to the output stream.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    instance.DecreaseIndent();
    ```
- `public virtual void IncreaseIndent()`
  - Summary: Increments the indentation level. Nothing is added to the output stream.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.IncreaseIndent();
    ```
- `public virtual void Write(string text)`
  - Summary: Writes text. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 110)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */);
    ```
- `public virtual void Write(string text, int index, int length, object color)`
  - Summary: Writes text and color. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `int index`: Index in
    - `int length`: Number of characters to write
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 126)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, index: /* int */, length: /* int */, color: /* object */);
    ```
- `public virtual void Write(string text, int index, int length, object reference, DecompilerReferenceFlags flags, object color)`
  - Summary: Writes text, color and a reference. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `int index`: Index in
    - `int length`: Number of characters to write
    - `object reference`: Reference
    - `DecompilerReferenceFlags flags`: Flags
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 146)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, index: /* int */, length: /* int */, reference: /* object */, flags: /* DecompilerReferenceFlags */, color: /* object */);
    ```
- `public virtual void Write(string text, object color)`
  - Summary: Writes text and color. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 117)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, color: /* object */);
    ```
- `public virtual void Write(string text, object reference, DecompilerReferenceFlags flags, object color)`
  - Summary: Writes text, color and a reference. The text will be indented if needed.
  - Parameters:
    - `string text`: Text
    - `object reference`: Reference
    - `DecompilerReferenceFlags flags`: Flags
    - `object color`: Color, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, reference: /* object */, flags: /* DecompilerReferenceFlags */, color: /* object */);
    ```
- `public virtual void WriteLine()`
  - Summary: Writes a new line without writing any indentation
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 72)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteLine();
    ```
- `public void Dispose()`
  - Summary: Disposes this instance and its underlying
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 157)
  - Example:
    ```csharp
    // Example invocation
    instance.Dispose();
    ```

### Properties

- `public virtual int Length => position`
  - Summary: Gets the total length of the written text
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Length;
    ```
- `public virtual int NextPosition => position + (addIndent ? indenter.String.Length : 0)`
  - Summary: This equals plus any indentation that must be written before the next text.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TextWriterDecompilerOutput.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NextPosition;
    ```

## Class `TokenReference`

Token reference

**Inherits/Implements:** `IEquatable<TokenReference>`

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.TokenReference(reference: /* IMemberRef */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/TokenReference.cs` (line 27)

### Constructors

- `public TokenReference(IMemberRef reference)`
  - Summary: Constructor
  - Parameters:
    - `IMemberRef reference`: Reference
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TokenReference.cs` (line 42)
- `public TokenReference(ModuleDef module, uint token)`
  - Summary: Constructor
  - Parameters:
    - `ModuleDef module`: Owner module
    - `uint token`: Token
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TokenReference.cs` (line 51)

### Methods

- `public bool Equals(TokenReference other)`
  - Summary: Equals()
  - Parameters:
    - `TokenReference other`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TokenReference.cs` (line 61)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(other: /* TokenReference */);
    ```
- `public override bool Equals(object obj)`
  - Summary: Equals()
  - Parameters:
    - `object obj`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TokenReference.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.Equals(obj: /* object */);
    ```
- `public override int GetHashCode()`
  - Summary: Equals()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TokenReference.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.GetHashCode();
    ```
- `public override string ToString()`
  - Summary: ToString()
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TokenReference.cs` (line 80)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```

### Properties

- `public ModuleDef ModuleDef { get; }`
  - Summary: Owner module
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TokenReference.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ModuleDef;
    ```
- `public uint Token { get; }`
  - Summary: Token
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TokenReference.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Token;
    ```

## Class `TypeDefComparer`

comparer

**Inherits/Implements:** `MemberRefComparer<TypeDef>`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.TypeDefComparer and call its members.
var instance = new dnSpy.Contracts.Decompiler.TypeDefComparer(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 50)

### Fields

- `public static readonly TypeDefComparer Instance = new TypeDefComparer()`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MemberComparer.cs` (line 54)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.TypeDefComparer.Instance;
    ```

## Class `TypesHierarchyHelpers`

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.TypesHierarchyHelpers members directly without instantiation.
dnSpy.Contracts.Decompiler.TypesHierarchyHelpers./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/TypesHierarchyHelpers.cs` (line 25)

### Methods

- `public static IEnumerable<EventDef> FindBaseEvents(EventDef eventDef)`
  - Parameters:
    - `EventDef eventDef`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TypesHierarchyHelpers.cs` (line 225)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TypesHierarchyHelpers.FindBaseEvents(eventDef: /* EventDef */);
    ```
- `public static IEnumerable<MethodDef> FindBaseMethods(MethodDef method)`
  - Summary: Finds all methods from base types overridden or hidden by the specified method.
  - Parameters:
    - `MethodDef method`: The method which overrides or hides methods from base types.
  - Returns: Methods overriden or hidden by the specified method.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TypesHierarchyHelpers.cs` (line 109)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TypesHierarchyHelpers.FindBaseMethods(method: /* MethodDef */);
    ```
- `public static IEnumerable<PropertyDef> FindBaseProperties(PropertyDef property)`
  - Summary: Finds all properties from base types overridden or hidden by the specified property.
  - Parameters:
    - `PropertyDef property`: The property which overrides or hides properties from base types.
  - Returns: Properties overriden or hidden by the specified property.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TypesHierarchyHelpers.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TypesHierarchyHelpers.FindBaseProperties(property: /* PropertyDef */);
    ```
- `public static bool IsBaseEvent(EventDef parentEvent, EventDef childEvent)`
  - Parameters:
    - `EventDef parentEvent`: Description not provided.
    - `EventDef childEvent`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TypesHierarchyHelpers.cs` (line 97)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TypesHierarchyHelpers.IsBaseEvent(parentEvent: /* EventDef */, childEvent: /* EventDef */);
    ```
- `public static bool IsBaseMethod(MethodDef parentMethod, MethodDef childMethod)`
  - Summary: Determines whether one method overrides or hides another method.
  - Parameters:
    - `MethodDef parentMethod`: The method declared in a base type.
    - `MethodDef childMethod`: The method declared in a derived type.
  - Returns: true if hides or overrides , otherwise false.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TypesHierarchyHelpers.cs` (line 54)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TypesHierarchyHelpers.IsBaseMethod(parentMethod: /* MethodDef */, childMethod: /* MethodDef */);
    ```
- `public static bool IsBaseProperty(PropertyDef parentProperty, PropertyDef childProperty)`
  - Summary: Determines whether a property overrides or hides another property.
  - Parameters:
    - `PropertyDef parentProperty`: The property declared in a base type.
    - `PropertyDef childProperty`: The property declared in a derived type.
  - Returns: true if the hides or overrides , otherwise false.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TypesHierarchyHelpers.cs` (line 79)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TypesHierarchyHelpers.IsBaseProperty(parentProperty: /* PropertyDef */, childProperty: /* PropertyDef */);
    ```
- `public static bool IsBaseType(TypeDef baseType, TypeDef derivedType, bool resolveTypeArguments)`
  - Parameters:
    - `TypeDef baseType`: Description not provided.
    - `TypeDef derivedType`: Description not provided.
    - `bool resolveTypeArguments`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TypesHierarchyHelpers.cs` (line 26)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TypesHierarchyHelpers.IsBaseType(baseType: /* TypeDef */, derivedType: /* TypeDef */, resolveTypeArguments: /* bool */);
    ```
- `public static bool IsVisibleFromDerived(IMemberDef baseMember, TypeDef derivedType)`
  - Summary: Determinates whether member of the base type is visible from a derived type.
  - Parameters:
    - `IMemberDef baseMember`: The member which visibility is checked.
    - `TypeDef derivedType`: The derived type.
  - Returns: true if the member is visible from derived type, othewise false.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TypesHierarchyHelpers.cs` (line 269)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TypesHierarchyHelpers.IsVisibleFromDerived(baseMember: /* IMemberDef */, derivedType: /* TypeDef */);
    ```
- `public static bool MatchInterfaceMethod(MethodDef candidate, MethodDef method, ITypeDefOrRef interfaceContextType)`
  - Parameters:
    - `MethodDef candidate`: Description not provided.
    - `MethodDef method`: Description not provided.
    - `ITypeDefOrRef interfaceContextType`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/TypesHierarchyHelpers.cs` (line 166)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.TypesHierarchyHelpers.MatchInterfaceMethod(candidate: /* MethodDef */, method: /* MethodDef */, interfaceContextType: /* ITypeDefOrRef */);
    ```

## Enum `VBImportScopeKind`

Visual Basic import scope kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.VBImportScopeKind and call its members.
var instance = new dnSpy.Contracts.Decompiler.VBImportScopeKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MethodDebugScope.cs` (line 118)

### Members

- `None`: Unspecified scope
- `File`: File scope
- `Project`: Project scope

## Class `VisualBasicMetadataTextColorProvider`

Visual Basic provider

**Inherits/Implements:** `MetadataTextColorProvider`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.VisualBasicMetadataTextColorProvider and call its members.
var instance = new dnSpy.Contracts.Decompiler.VisualBasicMetadataTextColorProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 286)

### Methods

- `public override object GetColor(TypeDef type)`
  - Summary: Gets a type color
  - Parameters:
    - `TypeDef type`: Type
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 299)
  - Example:
    ```csharp
    // Example invocation
    instance.GetColor(type: /* TypeDef */);
    ```

### Fields

- `public static readonly VisualBasicMetadataTextColorProvider Instance = new VisualBasicMetadataTextColorProvider()`
  - Summary: Gets the instance
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/MetadataTextColorProvider.cs` (line 290)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.Decompiler.VisualBasicMetadataTextColorProvider.Instance;
    ```

## Class `XamlOutputOptions`

XAML output options

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.XamlOutputOptions and call its members.
var instance = new dnSpy.Contracts.Decompiler.XamlOutputOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/IBamlDecompiler.cs` (line 56)

### Properties

- `public bool NewLineOnAttributes { get; set; }`
  - Summary: Add a newline after each attribute
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IBamlDecompiler.cs` (line 70)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewLineOnAttributes;
    ```
- `public string IndentChars { get; set; }`
  - Summary: Indent characters
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IBamlDecompiler.cs` (line 60)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IndentChars;
    ```
- `public string NewLineChars { get; set; }`
  - Summary: Newline characters
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/IBamlDecompiler.cs` (line 65)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NewLineChars;
    ```

