# Namespace `dnSpy.Contracts.Debugger.CallStack`

## Struct `DbgCallStackFramesInfo`

Contains the stack frames and related info

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.CallStack.DbgCallStackFramesInfo(frames: /* ReadOnlyCollection<DbgStackFrame> */, framesTruncated: /* bool */, activeFrameIndex: /* int */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 82)

### Constructors

- `public DbgCallStackFramesInfo(ReadOnlyCollection<DbgStackFrame> frames, bool framesTruncated, int activeFrameIndex)`
  - Summary: Constructor
  - Parameters:
    - `ReadOnlyCollection<DbgStackFrame> frames`: All frames
    - `bool framesTruncated`: true if there are too many frames and is a truncated list of all frames
    - `int activeFrameIndex`: Index of active thread. This could be invalid if is empty
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 109)

### Properties

- `public DbgStackFrame ActiveStackFrame => (uint)ActiveFrameIndex < (uint)Frames.Count ? Frames[ActiveFrameIndex] : null`
  - Summary: Gets the active frame or null if is empty
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 101)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveStackFrame;
    ```
- `public ReadOnlyCollection<DbgStackFrame> Frames { get; }`
  - Summary: Gets all frames
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 86)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Frames;
    ```
- `public bool FramesTruncated { get; }`
  - Summary: true if there are too many frames and is a truncated list of all frames
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 91)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FramesTruncated;
    ```
- `public int ActiveFrameIndex { get; }`
  - Summary: Index of active thread. This could be invalid if is empty
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 96)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveFrameIndex;
    ```

## Class `DbgCallStackService`

Provides all stack frames shown in the call stack window

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.CallStack.DbgCallStackService and call its members.
var instance = new dnSpy.Contracts.Debugger.CallStack.DbgCallStackService(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 27)

### Properties

- `public DbgStackFrame ActiveFrame => Frames.ActiveStackFrame`
  - Summary: Gets the active frame or null if is empty
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 41)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveFrame;
    ```
- `public abstract DbgCallStackFramesInfo Frames { get; }`
  - Summary: Gets all frames. This is a truncated list if there are too many frames
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 46)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Frames;
    ```
- `public abstract DbgThread Thread { get; }`
  - Summary: Gets the selected thread. This is identical to
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 31)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public abstract int ActiveFrameIndex { get; set; }`
  - Summary: Index of active thread. This could be invalid if is empty
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 36)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveFrameIndex;
    ```

### Events

- `public abstract event EventHandler<FramesChangedEventArgs> FramesChanged`
  - Summary: Raised when is changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 51)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.FramesChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `DbgStackFrame`

A stack frame in a debugged process

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.CallStack.DbgStackFrame and call its members.
var instance = new dnSpy.Contracts.Debugger.CallStack.DbgStackFrame(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 28)

### Methods

- `public void Close()`
  - Summary: Closes this instance
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 83)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```

### Properties

- `public DbgAppDomain AppDomain => Module?.AppDomain ?? Thread.AppDomain`
  - Summary: Gets the AppDomain or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 42)
  - Example:
    ```csharp
    // Read the property
    var value = instance.AppDomain;
    ```
- `public DbgProcess Process => Thread.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 32)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public DbgRuntime Runtime => Thread.Runtime`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 37)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract DbgCodeLocation Location { get; }`
  - Summary: Gets the location or null if none. Can be passed to or can be used to create a breakpoint if you call
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Location;
    ```
- `public abstract DbgModule Module { get; }`
  - Summary: Gets the module or null if it's unknown
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 58)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Module;
    ```
- `public abstract DbgStackFrameFlags Flags { get; }`
  - Summary: Gets the flags
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 63)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Flags;
    ```
- `public abstract DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 47)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```
- `public abstract uint FunctionOffset { get; }`
  - Summary: Gets the offset of the IP relative to the start of the function
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 68)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FunctionOffset;
    ```
- `public abstract uint FunctionToken { get; }`
  - Summary: Gets the function token or if it doesn't have a token.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 73)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FunctionToken;
    ```
- `public bool HasFunctionToken => FunctionToken != uint.MaxValue`
  - Summary: true if is valid
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 78)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasFunctionToken;
    ```

## Enum `DbgStackFrameFlags`

Stack frame flags

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.CallStack.DbgStackFrameFlags and call its members.
var instance = new dnSpy.Contracts.Debugger.CallStack.DbgStackFrameFlags(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackFrame.cs` (line 89)

### Members

- `None`: No bit is set
- `LocationIsNextStatement` = `x00000001`: Set if is the next statement to execute in this frame. It's also possible to set a BP at that location. It's false if is just an approximate location and it's not safe to set a BP at the location.

## Class `DbgStackWalker`

Walks the stack of a thread in a debugged process and creates s

**Inherits/Implements:** `DbgObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.Debugger.CallStack.DbgStackWalker and call its members.
var instance = new dnSpy.Contracts.Debugger.CallStack.DbgStackWalker(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackWalker.cs` (line 24)

### Methods

- `public abstract DbgStackFrame[] GetNextStackFrames(int maxFrames)`
  - Summary: Gets the next frames or an empty list if there are no more frames
  - Parameters:
    - `int maxFrames`: Max number of frames to return
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackWalker.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    instance.GetNextStackFrames(maxFrames: /* int */);
    ```
- `public void Close()`
  - Summary: Closes this instance. Any created s are not closed.
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackWalker.cs` (line 50)
  - Example:
    ```csharp
    // Example invocation
    instance.Close();
    ```

### Properties

- `public DbgProcess Process => Thread.Process`
  - Summary: Gets the process
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackWalker.cs` (line 28)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Process;
    ```
- `public DbgRuntime Runtime => Thread.Runtime`
  - Summary: Gets the runtime
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackWalker.cs` (line 33)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Runtime;
    ```
- `public abstract DbgThread Thread { get; }`
  - Summary: Gets the thread
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgStackWalker.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Thread;
    ```

## Struct `FramesChangedEventArgs`

Frames changed event args

**Example**

```csharp
var instance = new dnSpy.Contracts.Debugger.CallStack.FramesChangedEventArgs(framesChanged: /* bool */, activeFrameIndexChanged: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 57)

### Constructors

- `public FramesChangedEventArgs(bool framesChanged, bool activeFrameIndexChanged)`
  - Summary: Constructor
  - Parameters:
    - `bool framesChanged`: true if there are new frames available
    - `bool activeFrameIndexChanged`: true if active frame index changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 73)

### Properties

- `public bool ActiveFrameIndexChanged { get; }`
  - Summary: true if active frame index changed
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ActiveFrameIndexChanged;
    ```
- `public bool FramesChanged { get; }`
  - Summary: true if there are new frames available
  - Defined in: `dnSpy/dnSpy.Contracts.Debugger/CallStack/DbgCallStackService.cs` (line 61)
  - Example:
    ```csharp
    // Read the property
    var value = instance.FramesChanged;
    ```

