# Namespace `dnSpy.Contracts.Disassembly`

## Interface `IGasDisassemblySettings`

GNU assembler (AT&T syntax) disassembly settings

**Inherits/Implements:** `IX86DisassemblySettings`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.IGasDisassemblySettings and call its members.
var instance = new dnSpy.Contracts.Disassembly.IGasDisassemblySettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IGasDisassemblySettings.cs` (line 24)

### Properties

- `bool NakedRegisters { get; set; }`
  - Summary: If true, the formatter doesn't add '%' to registers, eg. %eax vs eax
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IGasDisassemblySettings.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NakedRegisters;
    ```
- `bool ShowMnemonicSizeSuffix { get; set; }`
  - Summary: Shows the mnemonic size suffix, eg. 'mov %eax,%ecx' vs 'movl %eax,%ecx'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IGasDisassemblySettings.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowMnemonicSizeSuffix;
    ```
- `bool SpaceAfterMemoryOperandComma { get; set; }`
  - Summary: Add a space after the comma if it's a memory operand, eg. '(%eax,%ecx,2)' vs '(%eax, %ecx, 2)'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IGasDisassemblySettings.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SpaceAfterMemoryOperandComma;
    ```

## Interface `IMasmDisassemblySettings`

masm disassembly settings

**Inherits/Implements:** `IX86DisassemblySettings`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.IMasmDisassemblySettings and call its members.
var instance = new dnSpy.Contracts.Disassembly.IMasmDisassemblySettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IMasmDisassemblySettings.cs` (line 24)

## Interface `INasmDisassemblySettings`

nasm disassembly settings

**Inherits/Implements:** `IX86DisassemblySettings`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.INasmDisassemblySettings and call its members.
var instance = new dnSpy.Contracts.Disassembly.INasmDisassemblySettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/INasmDisassemblySettings.cs` (line 24)

### Properties

- `bool ShowSignExtendedImmediateSize { get; set; }`
  - Summary: Shows byte, word, dword or qword if it's a sign extended immediate operand value, eg. 'or rcx,-1' vs 'or rcx,byte -1'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/INasmDisassemblySettings.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowSignExtendedImmediateSize;
    ```

## Interface `ISymbolResolver`

Resolves symbols

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.ISymbolResolver and call its members.
var instance = new dnSpy.Contracts.Disassembly.ISymbolResolver(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/ISymbolResolver.cs` (line 26)

### Methods

- `void Resolve(ulong[] addresses, SymbolResolverResult[] result)`
  - Summary: Tries to get symbols
  - Parameters:
    - `ulong[] addresses`: Addresses
    - `SymbolResolverResult[] result`: Elements that were resolved get updated, the other elements aren't touched. It has the same number of elements as
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/ISymbolResolver.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve(addresses: /* ulong[] */, result: /* SymbolResolverResult[] */);
    ```

## Interface `IX86DisassemblySettings`

x86/x64 disassembly settings

**Inherits/Implements:** `INotifyPropertyChanged`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.IX86DisassemblySettings and call its members.
var instance = new dnSpy.Contracts.Disassembly.IX86DisassemblySettings(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 26)

### Properties

- `MemorySizeOptions MemorySizeOptions { get; set; }`
  - Summary: Options that control if the memory size (eg. dword ptr) is shown or not. This is ignored by the GAS (AT&T) formatter.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 224)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemorySizeOptions;
    ```
- `NumberBase NumberBase { get; set; }`
  - Summary: Number base
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 198)
  - Example:
    ```csharp
    // Read the property
    var value = instance.NumberBase;
    ```
- `bool AddLeadingZeroToHexNumbers { get; set; }`
  - Summary: Add a leading zero to numbers if there's no prefix and the number begins with hex digits A-F, eg. Ah vs 0Ah
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 193)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AddLeadingZeroToHexNumbers;
    ```
- `bool AlwaysShowScale { get; set; }`
  - Summary: Always show the scale value even if it's *1, eg. "[rax+rcx*1]" vs "[rax+rcx]"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AlwaysShowScale;
    ```
- `bool AlwaysShowSegmentRegister { get; set; }`
  - Summary: Always show the effective segment register. If the option is false, only show the segment register if there's a segment override prefix. Eg. "ds:[rax]" vs "[rax]"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AlwaysShowSegmentRegister;
    ```
- `bool RipRelativeAddresses { get; set; }`
  - Summary: true to show RIP relative addresses as '[rip+12345678h]', false to show RIP relative addresses as '[1029384756AFBECDh]'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 229)
  - Example:
    ```csharp
    // Read the property
    var value = instance.RipRelativeAddresses;
    ```
- `bool ScaleBeforeIndex { get; set; }`
  - Summary: Show memory operand scale value before the index register, eg. "[4*rax]" vs "[rax*4]"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ScaleBeforeIndex;
    ```
- `bool ShortBranchNumbers { get; set; }`
  - Summary: Don't add leading zeroes to branch offsets, eg. 'je 123h' vs 'je 00000123h'. Used by call near, call far, jmp near, jmp far, jcc, loop, loopcc, xbegin
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 203)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShortBranchNumbers;
    ```
- `bool ShortNumbers { get; set; }`
  - Summary: Use shortest possible hexadecimal/octal/binary numbers, eg. 0xA/0Ah instead of eg. 0x0000000A/0000000Ah. This option has no effect on branch targets, use .
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 178)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShortNumbers;
    ```
- `bool ShowBranchSize { get; set; }`
  - Summary: Shows near, short, etc if it's a branch instruction, eg. 'je short 1234h' vs 'je 1234h'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 234)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowBranchSize;
    ```
- `bool ShowSymbolAddress { get; set; }`
  - Summary: Show the original value after the symbol name, eg. 'mov eax,[myfield (12345678)]' vs 'mov eax,[myfield]'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 244)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowSymbolAddress;
    ```
- `bool ShowZeroDisplacements { get; set; }`
  - Summary: Show zero displacements, eg. '[rcx*2+0]' vs '[rcx*2]'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 107)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ShowZeroDisplacements;
    ```
- `bool SignExtendMemoryDisplacements { get; set; }`
  - Summary: Sign extend memory displacements to the address size (16-bit, 32-bit, 64-bit), eg. 'mov al,[eax+12h]' vs 'mov al,[eax+00000012h]'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 218)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SignExtendMemoryDisplacements;
    ```
- `bool SignedImmediateOperands { get; set; }`
  - Summary: Show immediate operands as signed numbers, eg. 'mov eax,FFFFFFFF' vs 'mov eax,-1'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 208)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SignedImmediateOperands;
    ```
- `bool SignedMemoryDisplacements { get; set; }`
  - Summary: Displacements are signed numbers, eg. 'mov al,[eax-2000h]' vs 'mov al,[eax+0FFFFE000h]'
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 213)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SignedMemoryDisplacements;
    ```
- `bool SmallHexNumbersInDecimal { get; set; }`
  - Summary: Small hex numbers (-9 .. 9) are shown in decimal
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 188)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SmallHexNumbersInDecimal;
    ```
- `bool SpaceAfterMemoryBracket { get; set; }`
  - Summary: Add a space between the memory expression and the brackets, eg. "[ rax ]" vs "[rax]"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 76)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SpaceAfterMemoryBracket;
    ```
- `bool SpaceAfterOperandSeparator { get; set; }`
  - Summary: Add a space after the operand separator, eg. "rax, rcx" vs "rax,rcx"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 71)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SpaceAfterOperandSeparator;
    ```
- `bool SpaceBetweenMemoryAddOperators { get; set; }`
  - Summary: Add spaces between memory operand "+" and "-" operators, eg. "[rax + rcx]" vs "[rax+rcx]"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 81)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SpaceBetweenMemoryAddOperators;
    ```
- `bool SpaceBetweenMemoryMulOperators { get; set; }`
  - Summary: Add spaces between memory operand "*" operator, eg. "[rax * 4]" vs "[rax*4]"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SpaceBetweenMemoryMulOperators;
    ```
- `bool UpperCaseAll { get; set; }`
  - Summary: Everything is upper cased, except numbers and their prefixes/suffixes
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UpperCaseAll;
    ```
- `bool UpperCaseHex { get; set; }`
  - Summary: Use upper case hex digits
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 183)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UpperCaseHex;
    ```
- `bool UpperCaseKeywords { get; set; }`
  - Summary: Keywords are upper cased (eg. BYTE PTR, SHORT)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UpperCaseKeywords;
    ```
- `bool UpperCaseMnemonics { get; set; }`
  - Summary: Mnemonics are upper cased
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UpperCaseMnemonics;
    ```
- `bool UpperCaseOther { get; set; }`
  - Summary: Upper case other stuff, eg. {z}, {sae}, {rd-sae}
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UpperCaseOther;
    ```
- `bool UpperCasePrefixes { get; set; }`
  - Summary: Prefixes are upper cased
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UpperCasePrefixes;
    ```
- `bool UpperCaseRegisters { get; set; }`
  - Summary: Registers are upper cased
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UpperCaseRegisters;
    ```
- `bool UsePseudoOps { get; set; }`
  - Summary: Use pseudo instructions, eg. vcmpngesd vs vcmpsd+imm8
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 239)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UsePseudoOps;
    ```
- `int BinaryDigitGroupSize { get; set; }`
  - Summary: Size of a digit group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 167)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BinaryDigitGroupSize;
    ```
- `int DecimalDigitGroupSize { get; set; }`
  - Summary: Size of a digit group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 137)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DecimalDigitGroupSize;
    ```
- `int FirstOperandCharIndex { get; set; }`
  - Summary: Character index (0-based) where the first operand is formatted. Can be set to 0 to format it immediately after the mnemonic. At least one space or tab is always added betewen the mnemonic and the first operand.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FirstOperandCharIndex;
    ```
- `int HexDigitGroupSize { get; set; }`
  - Summary: Size of a digit group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 122)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexDigitGroupSize;
    ```
- `int OctalDigitGroupSize { get; set; }`
  - Summary: Size of a digit group
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 152)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OctalDigitGroupSize;
    ```
- `int TabSize { get; set; }`
  - Summary: Size of a tab character or <= 0 to use spaces
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.TabSize;
    ```
- `string BinaryPrefix { get; set; }`
  - Summary: Binary number prefix or null/empty string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 157)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BinaryPrefix;
    ```
- `string BinarySuffix { get; set; }`
  - Summary: Binary number suffix or null/empty string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 162)
  - Example:
    ```csharp
    // Read the property
    var value = instance.BinarySuffix;
    ```
- `string DecimalPrefix { get; set; }`
  - Summary: Decimal number prefix or null/empty string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 127)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DecimalPrefix;
    ```
- `string DecimalSuffix { get; set; }`
  - Summary: Decimal number suffix or null/empty string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 132)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DecimalSuffix;
    ```
- `string DigitSeparator { get; set; }`
  - Summary: Digit separator or null/empty string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 172)
  - Example:
    ```csharp
    // Read the property
    var value = instance.DigitSeparator;
    ```
- `string HexPrefix { get; set; }`
  - Summary: Hex number prefix or null/empty string, eg. "0x"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 112)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexPrefix;
    ```
- `string HexSuffix { get; set; }`
  - Summary: Hex number suffix or null/empty string, eg. "h"
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 117)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HexSuffix;
    ```
- `string OctalPrefix { get; set; }`
  - Summary: Octal number prefix or null/empty string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 142)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OctalPrefix;
    ```
- `string OctalSuffix { get; set; }`
  - Summary: Octal number suffix or null/empty string
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/IX86DisassemblySettings.cs` (line 147)
  - Example:
    ```csharp
    // Read the property
    var value = instance.OctalSuffix;
    ```

## Enum `MemorySizeOptions`

Memory size options used by the formatters

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.MemorySizeOptions and call its members.
var instance = new dnSpy.Contracts.Disassembly.MemorySizeOptions(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/MemorySizeOptions.cs` (line 24)

### Members

- `Default`: Show memory size if the assembler requires it, else don't show any
- `Always`: Always show the memory size, even if the assembler doesn't need it
- `Minimum`: Show memory size if a human can't figure out the size of the operand
- `Never`: Never show memory size

## Struct `NativeCode`

Contains the code that will be disassembled

**Example**

```csharp
var instance = new dnSpy.Contracts.Disassembly.NativeCode(kind: /* NativeCodeKind */, optimization: /* NativeCodeOptimization */, blocks: /* NativeCodeBlock[] */, codeInfo: /* NativeCodeInfo */, variableInfo: /* NativeVariableInfo[] */, methodName: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCode.cs` (line 26)

### Constructors

- `public NativeCode(NativeCodeKind kind, NativeCodeOptimization optimization, NativeCodeBlock[] blocks, NativeCodeInfo codeInfo, NativeVariableInfo[] variableInfo, string methodName)`
  - Summary: Constructor
  - Parameters:
    - `NativeCodeKind kind`: Code kind
    - `NativeCodeOptimization optimization`: Optimization kind
    - `NativeCodeBlock[] blocks`: All blocks to disassemble
    - `NativeCodeInfo codeInfo`: Extra code info or null
    - `NativeVariableInfo[] variableInfo`: Variable info or null
    - `string methodName`: Method name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCode.cs` (line 66)

### Properties

- `public NativeCodeBlock[] Blocks { get; }`
  - Summary: All blocks to disassemble
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCode.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Blocks;
    ```
- `public NativeCodeInfo CodeInfo { get; }`
  - Summary: Extra optional info, or null if none
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCode.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.CodeInfo;
    ```
- `public NativeCodeKind Kind { get; }`
  - Summary: Gets the code kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCode.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public NativeCodeOptimization Optimization { get; }`
  - Summary: Gets the optimization kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCode.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Optimization;
    ```
- `public NativeVariableInfo[] VariableInfo { get; }`
  - Summary: Variable info or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCode.cs` (line 50)
  - Example:
    ```csharp
    // Read the property
    var value = instance.VariableInfo;
    ```
- `public string MethodName { get; }`
  - Summary: Method name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCode.cs` (line 55)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MethodName;
    ```

## Struct `NativeCodeBlock`

A block of native code

**Example**

```csharp
var instance = new dnSpy.Contracts.Disassembly.NativeCodeBlock(kind: /* NativeCodeBlockKind */, address: /* ulong */, code: /* ArraySegment<byte> */, comment: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCodeBlock.cs` (line 26)

### Constructors

- `public NativeCodeBlock(NativeCodeBlockKind kind, ulong address, ArraySegment<byte> code, string comment)`
  - Summary: Constructor
  - Parameters:
    - `NativeCodeBlockKind kind`: Code kind
    - `ulong address`: Address of block
    - `ArraySegment<byte> code`: Raw code
    - `string comment`: Block comment or null. It can contain multiple lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCodeBlock.cs` (line 54)

### Properties

- `public ArraySegment<byte> Code { get; }`
  - Summary: Gets the raw code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCodeBlock.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Code;
    ```
- `public NativeCodeBlockKind Kind { get; }`
  - Summary: Gets the kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCodeBlock.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public string Comment { get; }`
  - Summary: Block comment or null. It can contain multiple lines
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCodeBlock.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Comment;
    ```
- `public ulong Address { get; }`
  - Summary: Gets the address of the code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCodeBlock.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```

## Enum `NativeCodeBlockKind`

Code block kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.NativeCodeBlockKind and call its members.
var instance = new dnSpy.Contracts.Disassembly.NativeCodeBlockKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCodeBlockKind.cs` (line 24)

### Members

- `Unknown`: Unknown code kind
- `Prolog`: It's the prolog
- `Epilog`: It's the epilog
- `Code`: Normal code (not prolog/epilog)

## Class `NativeCodeInfo`

Base class of extra info a disassembler can use

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.NativeCodeInfo and call its members.
var instance = new dnSpy.Contracts.Disassembly.NativeCodeInfo(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCode.cs` (line 79)

## Enum `NativeCodeKind`

Code kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.NativeCodeKind and call its members.
var instance = new dnSpy.Contracts.Disassembly.NativeCodeKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCodeKind.cs` (line 24)

### Members

- `X86_16`: 16-bit x86 code
- `X86_32`: 32-bit x86 code
- `X86_64`: 64-bit x86 code
- `Arm`: 32-bit ARM
- `Arm64`: 64-bit ARM

## Enum `NativeCodeOptimization`

Code optimization

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.NativeCodeOptimization and call its members.
var instance = new dnSpy.Contracts.Disassembly.NativeCodeOptimization(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeCodeOptimization.cs` (line 24)

### Members

- `Unknown`: It's not known whether the code is optimized or not
- `Unoptimized`: The code wasn't optimized, eg. it's a debug build
- `Optimized`: Optimized code

## Struct `NativeVariableInfo`

Variable info

**Example**

```csharp
var instance = new dnSpy.Contracts.Disassembly.NativeVariableInfo(isLocal: /* bool */, index: /* int */, name: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeVariableInfo.cs` (line 26)

### Constructors

- `public NativeVariableInfo(bool isLocal, int index, string name)`
  - Summary: Constructor
  - Parameters:
    - `bool isLocal`: true if it's a local, false if it's an argument
    - `int index`: Local/argument index
    - `string name`: Name of local/argument
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeVariableInfo.cs` (line 48)

### Properties

- `public bool IsLocal { get; }`
  - Summary: true if it's a local, false if it's an argument
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeVariableInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsLocal;
    ```
- `public int Index { get; }`
  - Summary: Local/argument index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeVariableInfo.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Index;
    ```
- `public string Name { get; }`
  - Summary: Name of local/argument
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NativeVariableInfo.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Enum `NumberBase`

Number base

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.NumberBase and call its members.
var instance = new dnSpy.Contracts.Disassembly.NumberBase(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/NumberBase.cs` (line 24)

### Members

- `Hexadecimal`: Hex numbers (base 16)
- `Decimal`: Decimal numbers (base 10)
- `Octal`: Octal numbers (base 8)
- `Binary`: Binary numbers (base 2)

## Enum `SymbolKind`

Symbol kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.SymbolKind and call its members.
var instance = new dnSpy.Contracts.Disassembly.SymbolKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/ISymbolResolver.cs` (line 39)

### Members

- `Unknown`: Unknown kind
- `Label`: Code label
- `Function`: Function
- `Data`: Data

## Struct `SymbolResolverResult`

Symbol resolver result

**Example**

```csharp
var instance = new dnSpy.Contracts.Disassembly.SymbolResolverResult(kind: /* SymbolKind */, symbol: /* string */, address: /* ulong */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/ISymbolResolver.cs` (line 64)

### Constructors

- `public SymbolResolverResult(SymbolKind kind, string symbol, ulong address)`
  - Summary: Constructor
  - Parameters:
    - `SymbolKind kind`: Symbol kind
    - `string symbol`: Symbol name
    - `ulong address`: Address of symbol, usually the same as the address passed to
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/ISymbolResolver.cs` (line 91)

### Properties

- `public SymbolKind Kind { get; }`
  - Summary: Symbol kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/ISymbolResolver.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Kind;
    ```
- `public bool IsDefault => Symbol == null`
  - Summary: Checks if this is the default instance
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/ISymbolResolver.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsDefault;
    ```
- `public string Symbol { get; }`
  - Summary: Symbol name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/ISymbolResolver.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Symbol;
    ```
- `public ulong Address { get; }`
  - Summary: Address of the symbol, usually identical to the address passed to
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/ISymbolResolver.cs` (line 83)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Address;
    ```

## Class `X86NativeCodeInfo`

Extra x86 (16/32/64-bit) info that can be used by a disassembler to show more info to the user

**Inherits/Implements:** `NativeCodeInfo`

**Example**

```csharp
var instance = new dnSpy.Contracts.Disassembly.X86NativeCodeInfo(variables: /* X86Variable[] */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86NativeCodeInfo.cs` (line 26)

### Constructors

- `public X86NativeCodeInfo(X86Variable[] variables)`
  - Summary: Constructor
  - Parameters:
    - `X86Variable[] variables`: Variables or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86NativeCodeInfo.cs` (line 36)

### Properties

- `public X86Variable[] Variables { get; }`
  - Summary: All known variables. Can be empty.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86NativeCodeInfo.cs` (line 30)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Variables;
    ```

## Enum `X86Register`

x86 register

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.X86Register and call its members.
var instance = new dnSpy.Contracts.Disassembly.X86Register(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Register.cs` (line 24)

### Members

- `None`
- `AL`
- `CL`
- `DL`
- `BL`
- `AH`
- `CH`
- `DH`
- `BH`
- `SPL`
- `BPL`
- `SIL`
- `DIL`
- `R8L`
- `R9L`
- `R10L`
- `R11L`
- `R12L`
- `R13L`
- `R14L`
- `R15L`
- `AX`
- `CX`
- `DX`
- `BX`
- `SP`
- `BP`
- `SI`
- `DI`
- `R8W`
- `R9W`
- `R10W`
- `R11W`
- `R12W`
- `R13W`
- `R14W`
- `R15W`
- `EAX`
- `ECX`
- `EDX`
- `EBX`
- `ESP`
- `EBP`
- `ESI`
- `EDI`
- `R8D`
- `R9D`
- `R10D`
- `R11D`
- `R12D`
- `R13D`
- `R14D`
- `R15D`
- `RAX`
- `RCX`
- `RDX`
- `RBX`
- `RSP`
- `RBP`
- `RSI`
- `RDI`
- `R8`
- `R9`
- `R10`
- `R11`
- `R12`
- `R13`
- `R14`
- `R15`
- `EIP`
- `RIP`
- `ST0`
- `ST1`
- `ST2`
- `ST3`
- `ST4`
- `ST5`
- `ST6`
- `ST7`
- `MM0`
- `MM1`
- `MM2`
- `MM3`
- `MM4`
- `MM5`
- `MM6`
- `MM7`
- `XMM0`
- `XMM1`
- `XMM2`
- `XMM3`
- `XMM4`
- `XMM5`
- `XMM6`
- `XMM7`
- `XMM8`
- `XMM9`
- `XMM10`
- `XMM11`
- `XMM12`
- `XMM13`
- `XMM14`
- `XMM15`
- `XMM16`
- `XMM17`
- `XMM18`
- `XMM19`
- `XMM20`
- `XMM21`
- `XMM22`
- `XMM23`
- `XMM24`
- `XMM25`
- `XMM26`
- `XMM27`
- `XMM28`
- `XMM29`
- `XMM30`
- `XMM31`
- `YMM0`
- `YMM1`
- `YMM2`
- `YMM3`
- `YMM4`
- `YMM5`
- `YMM6`
- `YMM7`
- `YMM8`
- `YMM9`
- `YMM10`
- `YMM11`
- `YMM12`
- `YMM13`
- `YMM14`
- `YMM15`
- `YMM16`
- `YMM17`
- `YMM18`
- `YMM19`
- `YMM20`
- `YMM21`
- `YMM22`
- `YMM23`
- `YMM24`
- `YMM25`
- `YMM26`
- `YMM27`
- `YMM28`
- `YMM29`
- `YMM30`
- `YMM31`
- `ZMM0`
- `ZMM1`
- `ZMM2`
- `ZMM3`
- `ZMM4`
- `ZMM5`
- `ZMM6`
- `ZMM7`
- `ZMM8`
- `ZMM9`
- `ZMM10`
- `ZMM11`
- `ZMM12`
- `ZMM13`
- `ZMM14`
- `ZMM15`
- `ZMM16`
- `ZMM17`
- `ZMM18`
- `ZMM19`
- `ZMM20`
- `ZMM21`
- `ZMM22`
- `ZMM23`
- `ZMM24`
- `ZMM25`
- `ZMM26`
- `ZMM27`
- `ZMM28`
- `ZMM29`
- `ZMM30`
- `ZMM31`

## Struct `X86Variable`

A variable (argument or local) in a function

**Example**

```csharp
var instance = new dnSpy.Contracts.Disassembly.X86Variable(name: /* string */, index: /* int */, isLocal: /* bool */, liveAddress: /* ulong */, liveLength: /* uint */, locationKind: /* X86VariableLocationKind */, register: /* X86Register */, memoryOffset: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 24)

### Constructors

- `public X86Variable(string name, int index, bool isLocal, ulong liveAddress, uint liveLength, X86VariableLocationKind locationKind, X86Register register, int memoryOffset)`
  - Summary: Constructor
  - Parameters:
    - `string name`: Name or null
    - `int index`: Argument/local index or < 0
    - `bool isLocal`: true if it's a local, false if it's an argument
    - `ulong liveAddress`: Start address in the code where this variable is live
    - `uint liveLength`: Length of the live range
    - `X86VariableLocationKind locationKind`: Variable kind
    - `X86Register register`: Register or memory base register
    - `int memoryOffset`: Offset relative to if it's a memory location ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 81)

### Properties

- `public X86Register Register { get; }`
  - Summary: Register or memory base register
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Register;
    ```
- `public X86VariableLocationKind LocationKind { get; }`
  - Summary: Variable location kind
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LocationKind;
    ```
- `public bool IsArgument => !IsLocal`
  - Summary: true if it's an argument
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 43)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsArgument;
    ```
- `public bool IsLocal { get; }`
  - Summary: true if it's a local variable
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsLocal;
    ```
- `public int Index { get; }`
  - Summary: Argument/local index or < 0
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Index;
    ```
- `public int MemoryOffset { get; }`
  - Summary: Offset relative to if it's a memory location ()
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.MemoryOffset;
    ```
- `public string Name { get; }`
  - Summary: Name or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```
- `public uint LiveLength { get; }`
  - Summary: Length of the live range
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LiveLength;
    ```
- `public ulong LiveAddress { get; }`
  - Summary: Start address in the code where this variable is live
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 48)
  - Example:
    ```csharp
    // Read the property
    var value = instance.LiveAddress;
    ```

## Enum `X86VariableLocationKind`

Variable location kind

**Example**

```csharp
// Instantiate dnSpy.Contracts.Disassembly.X86VariableLocationKind and call its members.
var instance = new dnSpy.Contracts.Disassembly.X86VariableLocationKind(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Disassembly/X86Variable.cs` (line 96)

### Members

- `Other`: The variable is stored somewhere else
- `Register`: The variable is stored in a register
- `Memory`: The variable is stored in a memory location (register + offset)

