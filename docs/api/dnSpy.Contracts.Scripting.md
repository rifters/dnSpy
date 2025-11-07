# Namespace `dnSpy.Contracts.Scripting`

## Interface `IOutputWritable`

Implemented by classes that can write itself using a

**Example**

```csharp
// Instantiate dnSpy.Contracts.Scripting.IOutputWritable and call its members.
var instance = new dnSpy.Contracts.Scripting.IOutputWritable(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IOutputWritable.cs` (line 27)

### Methods

- `void WriteTo(IOutputWriter output)`
  - Summary: Writes itself to
  - Parameters:
    - `IOutputWriter output`: Output
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IOutputWritable.cs` (line 32)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteTo(output: /* IOutputWriter */);
    ```

## Interface `IOutputWriter`

Writes text

**Example**

```csharp
// Instantiate dnSpy.Contracts.Scripting.IOutputWriter and call its members.
var instance = new dnSpy.Contracts.Scripting.IOutputWriter(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IOutputWriter.cs` (line 27)

### Methods

- `void Write(string text, TextColor color = TextColor.ReplScriptOutputText)`
  - Summary: Writes text
  - Parameters:
    - `string text`: Text to write
    - `TextColor color` (default: `TextColor.ReplScriptOutputText`): Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IOutputWriter.cs` (line 40)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, color: /* TextColor */);
    ```
- `void Write(string text, object color = null)`
  - Summary: Writes text
  - Parameters:
    - `string text`: Text to write
    - `object color` (default: `null`): Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IOutputWriter.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.Write(text: /* string */, color: /* object */);
    ```

## Interface `IServiceLocator`

Service locator

**Example**

```csharp
// Instantiate dnSpy.Contracts.Scripting.IServiceLocator and call its members.
var instance = new dnSpy.Contracts.Scripting.IServiceLocator(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IServiceLocator.cs` (line 24)

### Methods

- `T Resolve<T>()`
  - Summary: Resolves a service, and throws if it wasn't found
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IServiceLocator.cs` (line 30)
  - Example:
    ```csharp
    // Example invocation
    instance.Resolve();
    ```
- `T TryResolve<T>()`
  - Summary: Resolves a service or returns null if not found
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IServiceLocator.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.TryResolve();
    ```

## Class `OutputWritableExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Scripting.OutputWritableExtensions members directly without instantiation.
dnSpy.Contracts.Scripting.OutputWritableExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IOutputWritable.cs` (line 38)

### Methods

- `public static void WriteLineTo(this IOutputWritable obj, IOutputWriter output)`
  - Summary: Writes text followed by a newline
  - Parameters:
    - `this IOutputWritable obj`: Object
    - `IOutputWriter output`: Output
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IOutputWritable.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Scripting.OutputWritableExtensions.WriteLineTo(obj: /* IOutputWritable */, output: /* IOutputWriter */);
    ```

## Class `OutputWriterExtensions`

Extension methods

**Example**

```csharp
// Access dnSpy.Contracts.Scripting.OutputWriterExtensions members directly without instantiation.
dnSpy.Contracts.Scripting.OutputWriterExtensions./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IOutputWriter.cs` (line 46)

### Methods

- `public static void WriteLine(this IOutputWriter writer, string text, TextColor color = TextColor.ReplScriptOutputText)`
  - Summary: Writes text followed by a newline
  - Parameters:
    - `this IOutputWriter writer`: Writer
    - `string text`: Text to write
    - `TextColor color` (default: `TextColor.ReplScriptOutputText`): Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IOutputWriter.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Scripting.OutputWriterExtensions.WriteLine(writer: /* IOutputWriter */, text: /* string */, color: /* TextColor */);
    ```
- `public static void WriteLine(this IOutputWriter writer, string text, object color)`
  - Summary: Writes text followed by a newline
  - Parameters:
    - `this IOutputWriter writer`: Writer
    - `string text`: Text to write
    - `object color`: Color
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/IOutputWriter.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Scripting.OutputWriterExtensions.WriteLine(writer: /* IOutputWriter */, text: /* string */, color: /* object */);
    ```

## Class `ScriptException`

Base class of script-related exceptions

**Inherits/Implements:** `Exception`

**Example**

```csharp
var instance = new dnSpy.Contracts.Scripting.ScriptException();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/ScriptException.cs` (line 26)

### Constructors

- `public ScriptException()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/ScriptException.cs` (line 31)
- `public ScriptException(string message)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/ScriptException.cs` (line 38)
- `public ScriptException(string message, Exception innerException)`
  - Summary: Constructor
  - Parameters:
    - `string message`: Message
    - `Exception innerException`: Inner exception or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/ScriptException.cs` (line 47)

## Class `UIUtils`

Executes code on the UI thread

**Example**

```csharp
// Access dnSpy.Contracts.Scripting.UIUtils members directly without instantiation.
dnSpy.Contracts.Scripting.UIUtils./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/Scripting/UIUtils.cs` (line 29)

### Methods

- `public static IEnumerable<T> UIIter<T>(this Dispatcher dispatcher, Func<IEnumerable<T>> getIter)`
  - Summary: Returns the result of an . is only called on the UI thread.
  - Parameters:
    - `this Dispatcher dispatcher`: UI dispatcher
    - `Func<IEnumerable<T>> getIter`: Called on the UI thread to return the result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/UIUtils.cs` (line 93)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Scripting.UIUtils.UIIter(dispatcher: /* Dispatcher */, getIter: /* Func<IEnumerable<T>> */);
    ```
- `public static T UI<T>(this Dispatcher dispatcher, Func<T> f)`
  - Summary: Executes in the UI thread and returns the result
  - Parameters:
    - `this Dispatcher dispatcher`: UI dispatcher
    - `Func<T> f`: Func
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/UIUtils.cs` (line 64)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Scripting.UIUtils.UI(dispatcher: /* Dispatcher */, f: /* Func<T> */);
    ```
- `public static void UI(this Dispatcher dispatcher, Action a)`
  - Summary: Executes in the UI thread and then returns
  - Parameters:
    - `this Dispatcher dispatcher`: UI dispatcher
    - `Action a`: Action
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/Scripting/UIUtils.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.Scripting.UIUtils.UI(dispatcher: /* Dispatcher */, a: /* Action */);
    ```

