# Namespace `dnSpy.Contracts.Decompiler.XmlDoc`

## Interface `IXmlDocOutput`

XML doc output

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.XmlDoc.IXmlDocOutput and call its members.
var instance = new dnSpy.Contracts.Decompiler.XmlDoc.IXmlDocOutput(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 29)

### Methods

- `void Write(string s, object data)`
  - Summary: Writes text
  - Parameters:
    - `string s`: Text
    - `object data`: Data
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(s: /* string */, data: /* object */);
    ```
- `void WriteNewLine()`
  - Summary: Writes a new line
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteNewLine();
    ```
- `void WriteSpace()`
  - Summary: Writes a space character
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteSpace();
    ```

## Class `XmlDocKeyProvider`

Provides XML documentation tags.

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.XmlDoc.XmlDocKeyProvider and call its members.
var instance = new dnSpy.Contracts.Decompiler.XmlDoc.XmlDocKeyProvider(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocKeyProvider.cs` (line 29)

### Methods

- `public static IMemberRef FindMemberByKey(ModuleDef module, string key)`
  - Summary: Finds a member by key
  - Parameters:
    - `ModuleDef module`: Module to search
    - `string key`: Key
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocKeyProvider.cs` (line 229)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.XmlDoc.XmlDocKeyProvider.FindMemberByKey(module: /* ModuleDef */, key: /* string */);
    ```
- `public static StringBuilder GetKey(IMemberRef member, StringBuilder b)`
  - Summary: Gets an XML doc key
  - Parameters:
    - `IMemberRef member`: Member
    - `StringBuilder b`: String builder
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocKeyProvider.cs` (line 36)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.XmlDoc.XmlDocKeyProvider.GetKey(member: /* IMemberRef */, b: /* StringBuilder */);
    ```
- `public static string SplitTypeParameterCountFromReflectionName(string reflectionName, out int typeParameterCount)`
  - Summary: Removes the ` with type parameter count from the reflection name.
  - Parameters:
    - `string reflectionName`: Description not provided.
    - `out int typeParameterCount`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocKeyProvider.cs` (line 208)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.XmlDoc.XmlDocKeyProvider.SplitTypeParameterCountFromReflectionName(reflectionName: /* string */, typeParameterCount: /* int */);
    ```

## Class `XmlDocLoader`

Helps finding and loading .xml documentation.

**Example**

```csharp
// Access dnSpy.Contracts.Decompiler.XmlDoc.XmlDocLoader members directly without instantiation.
dnSpy.Contracts.Decompiler.XmlDoc.XmlDocLoader./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocLoader.cs` (line 32)

### Methods

- `public static XmlDocumentationProvider LoadDocumentation(ModuleDef module)`
  - Summary: Loads XML documentation
  - Parameters:
    - `ModuleDef module`: Module
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocLoader.cs` (line 56)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.XmlDoc.XmlDocLoader.LoadDocumentation(module: /* ModuleDef */);
    ```
- `public static XmlDocumentationProvider LoadDocumentation(object key, string assemblyFilename, string runtimeVersion = null)`
  - Summary: Loads XML documentation
  - Parameters:
    - `object key`: Key used to lookup cached documentation, eg. the instance
    - `string assemblyFilename`: Filename of the assembly or module
    - `string runtimeVersion` (default: `null`): Optional runtime version, eg.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocLoader.cs` (line 69)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.XmlDoc.XmlDocLoader.LoadDocumentation(key: /* object */, assemblyFilename: /* string */, runtimeVersion: /* string */);
    ```

### Properties

- `public static XmlDocumentationProvider MscorlibDocumentation => mscorlibDocumentation.Value`
  - Summary: mscorlib documentation
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocLoader.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Decompiler.XmlDoc.XmlDocLoader.MscorlibDocumentation;
    ```

## Class `XmlDocRenderer`

Renders XML documentation

**Inherits/Implements:** `IXmlDocOutput`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Decompiler.XmlDoc.XmlDocRenderer and call its members.
var instance = new dnSpy.Contracts.Decompiler.XmlDoc.XmlDocRenderer(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 51)

### Methods

- `public override string ToString()`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 201)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static bool WriteXmlDoc(IXmlDocOutput output, string xmlDocumentation)`
  - Summary: Writes XML documentation
  - Parameters:
    - `IXmlDocOutput output`: Output
    - `string xmlDocumentation`: XML documentation
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.XmlDoc.XmlDocRenderer.WriteXmlDoc(output: /* IXmlDocOutput */, xmlDocumentation: /* string */);
    ```
- `public static string GetCref(string cref)`
  - Summary: Gets a cref
  - Parameters:
    - `string cref`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 188)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.XmlDoc.XmlDocRenderer.GetCref(cref: /* string */);
    ```
- `public void AddXmlDocumentation(string xmlDocumentation)`
  - Summary: Adds xml documentation
  - Parameters:
    - `string xmlDocumentation`: XML documentation
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 68)
  - Example:
    ```csharp
    // Example invocation
    instance.AddXmlDocumentation(xmlDocumentation: /* string */);
    ```
- `public void AppendText(string text)`
  - Summary: Appends text
  - Parameters:
    - `string text`: Text
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.AppendText(text: /* string */);
    ```

### Properties

- `public static Regex WhitespaceRegex => whitespace`
  - Summary: Whitespace regex
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocRenderer.cs` (line 92)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Contracts.Decompiler.XmlDoc.XmlDocRenderer.WhitespaceRegex;
    ```

## Class `XmlDocumentationProvider`

Provides documentation from an .xml file (as generated by the Microsoft C# compiler).

**Inherits/Implements:** `IDeserializationCallback`

This class first creates an in-memory index of the .xml file, and then uses that to read only the requested members. This way, we avoid keeping all the documentation in memory. The .xml file is only opened when necessary, the file handle is not kept open all the time. If the .xml file is changed, the index will automatically be recreated.

**Example**

```csharp
var instance = new dnSpy.Contracts.Decompiler.XmlDoc.XmlDocumentationProvider(fileName: /* string */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocumentationProvider.cs` (line 37)

### Constructors

- `public XmlDocumentationProvider(string fileName)`
  - Summary: Creates a new XmlDocumentationProvider.
  - Parameters:
    - `string fileName`: Name of the .xml file.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocumentationProvider.cs` (line 136)

### Methods

- `public static XmlDocumentationProvider Create(string fileName)`
  - Summary: Creates a new XmlDocumentationProvider. Can return null if we couldn't read the file.
  - Parameters:
    - `string fileName`: Name of the .xml file.
  - Returns: null if we couldn't create it
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocumentationProvider.cs` (line 108)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.XmlDoc.XmlDocumentationProvider.Create(fileName: /* string */);
    ```
- `public static string LookupLocalizedXmlDoc(string fileName)`
  - Summary: Given the assembly file name, looks up the XML documentation file name. Returns null if no XML documentation file is found.
  - Parameters:
    - `string fileName`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocumentationProvider.cs` (line 199)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Decompiler.XmlDoc.XmlDocumentationProvider.LookupLocalizedXmlDoc(fileName: /* string */);
    ```
- `public string GetDocumentation(StringBuilder key)`
  - Summary: Get the documentation for the member with the specified documentation key.
  - Parameters:
    - `StringBuilder key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocumentationProvider.cs` (line 345)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDocumentation(key: /* StringBuilder */);
    ```
- `public string GetDocumentation(string key)`
  - Summary: Get the documentation for the member with the specified documentation key.
  - Parameters:
    - `string key`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocumentationProvider.cs` (line 335)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDocumentation(key: /* string */);
    ```
- `public virtual void OnDeserialization(object sender)`
  - Parameters:
    - `object sender`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/Decompiler/XmlDoc/XmlDocumentationProvider.cs` (line 438)
  - Example:
    ```csharp
    // Example invocation
    instance.OnDeserialization(sender: /* object */);
    ```

