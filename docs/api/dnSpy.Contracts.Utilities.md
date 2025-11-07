# Namespace `dnSpy.Contracts.Utilities`

## Struct `GacFileInfo`

GAC file info

**Example**

```csharp
// Instantiate dnSpy.Contracts.Utilities.GacFileInfo and call its members.
var instance = new dnSpy.Contracts.Utilities.GacFileInfo(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 32)

### Properties

- `public IAssembly Assembly { get; }`
  - Summary: Assembly
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Assembly;
    ```
- `public string Path { get; }`
  - Summary: Path to file
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Path;
    ```

## Class `GacInfo`

GAC

**Example**

```csharp
// Access dnSpy.Contracts.Utilities.GacInfo members directly without instantiation.
dnSpy.Contracts.Utilities.GacInfo./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 92)

### Methods

- `public static IEnumerable<GacFileInfo> GetAssemblies(int majorVersion)`
  - Summary: Gets all assemblies in the GAC
  - Parameters:
    - `int majorVersion`: CLR major version, eg. 2 or 4
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 332)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.GacInfo.GetAssemblies(majorVersion: /* int */);
    ```
- `public static bool IsGacPath(string filename)`
  - Summary: Checks whether is in the GAC
  - Parameters:
    - `string filename`: Filename
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 248)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.GacInfo.IsGacPath(filename: /* string */);
    ```
- `public static string FindInGac(IAssembly asm)`
  - Summary: Finds an assembly in the GAC
  - Parameters:
    - `IAssembly asm`: Assembly
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 278)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.GacInfo.FindInGac(asm: /* IAssembly */);
    ```
- `public static string FindInGac(IAssembly asm, int version)`
  - Summary: Finds an assembly in the GAC
  - Parameters:
    - `IAssembly asm`: Assembly
    - `int version`: 2, 4, or -1
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 286)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.GacInfo.FindInGac(asm: /* IAssembly */, version: /* int */);
    ```

### Properties

- `public static GacPathInfo[] GacPaths { get; }`
  - Summary: All GAC paths
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Utilities.GacInfo.GacPaths;
    ```
- `public static GacPathInfo[] OtherGacPaths { get; }`
  - Summary: Other GAC paths
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Utilities.GacInfo.OtherGacPaths;
    ```
- `public static bool HasGAC2 { get; }`
  - Summary: Checks if .NET 2.0-3.5 GAC exists
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Utilities.GacInfo.HasGAC2;
    ```
- `public static string[] WinmdPaths { get; }`
  - Summary: WinMD paths
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 106)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Utilities.GacInfo.WinmdPaths;
    ```

## Struct `GacPathInfo`

GAC path info

**Example**

```csharp
var instance = new dnSpy.Contracts.Utilities.GacPathInfo(path: /* string */, version: /* GacVersion */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 67)

### Constructors

- `public GacPathInfo(string path, GacVersion version)`
  - Summary: Constructor
  - Parameters:
    - `string path`: Path
    - `GacVersion version`: Version
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 83)

### Fields

- `public readonly GacVersion Version`
  - Summary: GAC version
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 76)
  - Example:
    ```csharp
    var value = instance.Version;
    ```
- `public readonly string Path`
  - Summary: Path of dir containing assemblies
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 71)
  - Example:
    ```csharp
    var value = instance.Path;
    ```

## Enum `GacVersion`

GAC version

**Example**

```csharp
// Instantiate dnSpy.Contracts.Utilities.GacVersion and call its members.
var instance = new dnSpy.Contracts.Utilities.GacVersion(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Utilities/GacInfo.cs` (line 52)

### Members

- `V2`: .NET Framework 1.0-3.5
- `V4`: .NET Framework 4.0+

## Class `ProfileOptimizationHelper`

Helper class that calls methods

**Example**

```csharp
// Access dnSpy.Contracts.Utilities.ProfileOptimizationHelper members directly without instantiation.
dnSpy.Contracts.Utilities.ProfileOptimizationHelper./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Utilities/ProfileOptimizationHelper.cs` (line 28)

### Methods

- `public static void StartProfile(string type)`
  - Summary: Starts a profile by calling , but only if it's the first time this method has been called with the same input.
  - Parameters:
    - `string type`: Unique string that is used as a key to check whether we should start profiling the code
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Utilities/ProfileOptimizationHelper.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.ProfileOptimizationHelper.StartProfile(type: /* string */);
    ```

## Class `SimpleTypeConverter`

Converts numbers, strings and a few other types to or from strings

**Example**

```csharp
// Access dnSpy.Contracts.Utilities.SimpleTypeConverter members directly without instantiation.
dnSpy.Contracts.Utilities.SimpleTypeConverter./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 31)

### Methods

- `public static DateTime ParseDateTime(string s, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 376)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseDateTime(s: /* string */, error: /* string */);
    ```
- `public static TimeSpan ParseTimeSpan(string s, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 391)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseTimeSpan(s: /* string */, error: /* string */);
    ```
- `public static bool ParseBoolean(string s, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 406)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseBoolean(s: /* string */, error: /* string */);
    ```
- `public static bool[] ParseBooleanList(string s, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 934)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseBooleanList(s: /* string */, error: /* string */);
    ```
- `public static byte ParseByte(string s, byte min, byte max, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `byte min`: Minimum value
    - `byte max`: Maximum value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 622)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseByte(s: /* string */, min: /* byte */, max: /* byte */, error: /* string */);
    ```
- `public static byte[] ParseByteArray(string s, out string error)`
  - Summary: Parses a byte array string
  - Parameters:
    - `string s`: Input string
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseByteArray(s: /* string */, error: /* string */);
    ```
- `public static byte[] ParseByteList(string s, byte min, byte max, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `byte min`: Minimum value
    - `byte max`: Maximium value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 953)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseByteList(s: /* string */, min: /* byte */, max: /* byte */, error: /* string */);
    ```
- `public static char ParseChar(string s, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 421)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseChar(s: /* string */, error: /* string */);
    ```
- `public static char[] ParseCharList(string s, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 942)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseCharList(s: /* string */, error: /* string */);
    ```
- `public static decimal ParseDecimal(string s, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 361)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseDecimal(s: /* string */, error: /* string */);
    ```
- `public static double ParseDouble(string s, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 346)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseDouble(s: /* string */, error: /* string */);
    ```
- `public static double[] ParseDoubleList(string s, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 1039)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseDoubleList(s: /* string */, error: /* string */);
    ```
- `public static float ParseSingle(string s, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 331)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseSingle(s: /* string */, error: /* string */);
    ```
- `public static float[] ParseSingleList(string s, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 1031)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseSingleList(s: /* string */, error: /* string */);
    ```
- `public static int ParseInt32(string s, int min, int max, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `int min`: Minimum value
    - `int max`: Maximum value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 728)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseInt32(s: /* string */, min: /* int */, max: /* int */, error: /* string */);
    ```
- `public static int[] ParseInt32List(string s, int min, int max, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `int min`: Minimum value
    - `int max`: Maximium value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 1013)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseInt32List(s: /* string */, min: /* int */, max: /* int */, error: /* string */);
    ```
- `public static long ParseInt64(string s, long min, long max, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `long min`: Minimum value
    - `long max`: Maximum value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 738)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseInt64(s: /* string */, min: /* long */, max: /* long */, error: /* string */);
    ```
- `public static long[] ParseInt64List(string s, long min, long max, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `long min`: Minimum value
    - `long max`: Maximium value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 1023)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseInt64List(s: /* string */, min: /* long */, max: /* long */, error: /* string */);
    ```
- `public static sbyte ParseSByte(string s, sbyte min, sbyte max, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `sbyte min`: Minimum value
    - `sbyte max`: Maximum value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 708)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseSByte(s: /* string */, min: /* sbyte */, max: /* sbyte */, error: /* string */);
    ```
- `public static sbyte[] ParseSByteList(string s, sbyte min, sbyte max, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `sbyte min`: Minimum value
    - `sbyte max`: Maximium value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 993)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseSByteList(s: /* string */, min: /* sbyte */, max: /* sbyte */, error: /* string */);
    ```
- `public static short ParseInt16(string s, short min, short max, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `short min`: Minimum value
    - `short max`: Maximum value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 718)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseInt16(s: /* string */, min: /* short */, max: /* short */, error: /* string */);
    ```
- `public static short[] ParseInt16List(string s, short min, short max, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `short min`: Minimum value
    - `short max`: Maximium value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 1003)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseInt16List(s: /* string */, min: /* short */, max: /* short */, error: /* string */);
    ```
- `public static string ByteArrayToString(IList<byte> value, bool upper = true)`
  - Summary: Converts a array to a string
  - Parameters:
    - `IList<byte> value`: Bytes
    - `bool upper` (default: `true`): true to use upper case hex numbers
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 82)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ByteArrayToString(value: /* IList<byte> */, upper: /* bool */);
    ```
- `public static string ParseString(string s, bool canHaveNull, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `bool canHaveNull`: true if the string value "null" can be converted to a null string
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 495)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseString(s: /* string */, canHaveNull: /* bool */, error: /* string */);
    ```
- `public static string ToString(DateTime value)`
  - Summary: Converts a to a string
  - Parameters:
    - `DateTime value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 209)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* DateTime */);
    ```
- `public static string ToString(IList<bool> values)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<bool> values`: Values
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 757)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<bool> */);
    ```
- `public static string ToString(IList<byte> values, byte min, byte max, bool? useDecimal)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<byte> values`: Values
    - `byte min`: Minimum value
    - `byte max`: Maximum value
    - `bool? useDecimal`: true to use decimal, false to use hex, null to use decimal if possible, hex otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 774)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<byte> */, min: /* byte */, max: /* byte */, useDecimal: /* bool? */);
    ```
- `public static string ToString(IList<char> values)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<char> values`: Values
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 764)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<char> */);
    ```
- `public static string ToString(IList<double> values)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<double> values`: Values
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 858)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<double> */);
    ```
- `public static string ToString(IList<float> values)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<float> values`: Values
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 851)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<float> */);
    ```
- `public static string ToString(IList<int> values, int min, int max, bool? useDecimal)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<int> values`: Values
    - `int min`: Minimum value
    - `int max`: Maximum value
    - `bool? useDecimal`: true to use decimal, false to use hex, null to use decimal if possible, hex otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 834)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<int> */, min: /* int */, max: /* int */, useDecimal: /* bool? */);
    ```
- `public static string ToString(IList<long> values, long min, long max, bool? useDecimal)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<long> values`: Values
    - `long min`: Minimum value
    - `long max`: Maximum value
    - `bool? useDecimal`: true to use decimal, false to use hex, null to use decimal if possible, hex otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 844)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<long> */, min: /* long */, max: /* long */, useDecimal: /* bool? */);
    ```
- `public static string ToString(IList<sbyte> values, sbyte min, sbyte max, bool? useDecimal)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<sbyte> values`: Values
    - `sbyte min`: Minimum value
    - `sbyte max`: Maximum value
    - `bool? useDecimal`: true to use decimal, false to use hex, null to use decimal if possible, hex otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 814)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<sbyte> */, min: /* sbyte */, max: /* sbyte */, useDecimal: /* bool? */);
    ```
- `public static string ToString(IList<short> values, short min, short max, bool? useDecimal)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<short> values`: Values
    - `short min`: Minimum value
    - `short max`: Maximum value
    - `bool? useDecimal`: true to use decimal, false to use hex, null to use decimal if possible, hex otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 824)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<short> */, min: /* short */, max: /* short */, useDecimal: /* bool? */);
    ```
- `public static string ToString(IList<string> values, bool canHaveNull)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<string> values`: Values
    - `bool canHaveNull`: true if null strings are converted to a string with the value "null", false if the empty string is used if the input string is null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 867)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<string> */, canHaveNull: /* bool */);
    ```
- `public static string ToString(IList<uint> values, uint min, uint max, bool? useDecimal)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<uint> values`: Values
    - `uint min`: Minimum value
    - `uint max`: Maximum value
    - `bool? useDecimal`: true to use decimal, false to use hex, null to use decimal if possible, hex otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 794)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<uint> */, min: /* uint */, max: /* uint */, useDecimal: /* bool? */);
    ```
- `public static string ToString(IList<ulong> values, ulong min, ulong max, bool? useDecimal)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<ulong> values`: Values
    - `ulong min`: Minimum value
    - `ulong max`: Maximum value
    - `bool? useDecimal`: true to use decimal, false to use hex, null to use decimal if possible, hex otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 804)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<ulong> */, min: /* ulong */, max: /* ulong */, useDecimal: /* bool? */);
    ```
- `public static string ToString(IList<ushort> values, ushort min, ushort max, bool? useDecimal)`
  - Summary: Converts a list of s to a string
  - Parameters:
    - `IList<ushort> values`: Values
    - `ushort min`: Minimum value
    - `ushort max`: Maximum value
    - `bool? useDecimal`: true to use decimal, false to use hex, null to use decimal if possible, hex otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 784)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(values: /* IList<ushort> */, min: /* ushort */, max: /* ushort */, useDecimal: /* bool? */);
    ```
- `public static string ToString(TimeSpan value)`
  - Summary: Converts a to a string
  - Parameters:
    - `TimeSpan value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 216)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* TimeSpan */);
    ```
- `public static string ToString(bool value)`
  - Summary: Converts a to a string
  - Parameters:
    - `bool value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 223)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* bool */);
    ```
- `public static string ToString(char value)`
  - Summary: Converts a to a C# char string in single quotes
  - Parameters:
    - `char value`: Character
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 230)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* char */);
    ```
- `public static string ToString(decimal value)`
  - Summary: Converts a to a string
  - Parameters:
    - `decimal value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 202)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* decimal */);
    ```
- `public static string ToString(double value)`
  - Summary: Converts a to a string
  - Parameters:
    - `double value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 195)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* double */);
    ```
- `public static string ToString(float value)`
  - Summary: Converts a to a string
  - Parameters:
    - `float value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* float */);
    ```
- `public static string ToString(long value)`
  - Summary: Converts a to a string
  - Parameters:
    - `long value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 174)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* long */);
    ```
- `public static string ToString(long value, long min, long max, bool? useDecimal)`
  - Summary: Converts a signed integer to a string
  - Parameters:
    - `long value`: Value
    - `long min`: Minimum value
    - `long max`: Maximium value
    - `bool? useDecimal`: true to use decimal, false to use hex, null to use decimal if possible, hex otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 155)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* long */, min: /* long */, max: /* long */, useDecimal: /* bool? */);
    ```
- `public static string ToString(string s, bool canHaveNull)`
  - Summary: Converts a to a C# string in double quotes
  - Parameters:
    - `string s`: String, may be null
    - `bool canHaveNull`: true if the return value will be the string "null" without the quotes if is null, otherwise an empty string is returned if the input string is null
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 263)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(s: /* string */, canHaveNull: /* bool */);
    ```
- `public static string ToString(ulong value)`
  - Summary: Converts a to a string
  - Parameters:
    - `ulong value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 181)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* ulong */);
    ```
- `public static string ToString(ulong value, ulong min, ulong max, bool? useDecimal)`
  - Summary: Converts an unsigned integer to a string
  - Parameters:
    - `ulong value`: Value
    - `ulong min`: Minimum value
    - `ulong max`: Maximium value
    - `bool? useDecimal`: true to use decimal, false to use hex, null to use decimal if possible, hex otherwise
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 135)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ToString(value: /* ulong */, min: /* ulong */, max: /* ulong */, useDecimal: /* bool? */);
    ```
- `public static string[] ParseStringList(string s, bool canHaveNull, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `bool canHaveNull`: true if the string value "null" can be converted to a null string
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 1048)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseStringList(s: /* string */, canHaveNull: /* bool */, error: /* string */);
    ```
- `public static uint ParseUInt32(string s, uint min, uint max, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `uint min`: Minimum value
    - `uint max`: Maximum value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 642)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseUInt32(s: /* string */, min: /* uint */, max: /* uint */, error: /* string */);
    ```
- `public static uint[] ParseUInt32List(string s, uint min, uint max, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `uint min`: Minimum value
    - `uint max`: Maximium value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 973)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseUInt32List(s: /* string */, min: /* uint */, max: /* uint */, error: /* string */);
    ```
- `public static ulong ParseUInt64(string s, ulong min, ulong max, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `ulong min`: Minimum value
    - `ulong max`: Maximum value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 652)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseUInt64(s: /* string */, min: /* ulong */, max: /* ulong */, error: /* string */);
    ```
- `public static ulong[] ParseUInt64List(string s, ulong min, ulong max, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `ulong min`: Minimum value
    - `ulong max`: Maximium value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 983)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseUInt64List(s: /* string */, min: /* ulong */, max: /* ulong */, error: /* string */);
    ```
- `public static ushort ParseUInt16(string s, ushort min, ushort max, out string error)`
  - Summary: Converts a string to a
  - Parameters:
    - `string s`: String
    - `ushort min`: Minimum value
    - `ushort max`: Maximum value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 632)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseUInt16(s: /* string */, min: /* ushort */, max: /* ushort */, error: /* string */);
    ```
- `public static ushort[] ParseUInt16List(string s, ushort min, ushort max, out string error)`
  - Summary: Converts a string containing a list of s to an array
  - Parameters:
    - `string s`: Input string
    - `ushort min`: Minimum value
    - `ushort max`: Maximium value
    - `out string error`: Updated with error string or null if no error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Utilities/SimpleTypeConverter.cs` (line 963)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Utilities.SimpleTypeConverter.ParseUInt16List(s: /* string */, min: /* ushort */, max: /* ushort */, error: /* string */);
    ```

