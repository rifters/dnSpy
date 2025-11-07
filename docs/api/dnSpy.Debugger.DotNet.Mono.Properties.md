# Namespace `dnSpy.Debugger.DotNet.Mono.Properties`

## Class `dnSpy_Debugger_DotNet_Mono_Resources`

**Example**

```csharp
// Instantiate dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources and call its members.
var instance = new dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 22)

### Properties

- `public static global::System.Globalization.CultureInfo Culture {
            get {
                return resourceCulture;
            }
            set {
                resourceCulture = value;
            }
        }`
  - Summary: Overrides the current thread's CurrentUICulture property for all resource lookups using this strongly typed resource class.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Culture;
    ```
- `public static global::System.Resources.ResourceManager ResourceManager {
            get {
                if (object.ReferenceEquals(resourceMan, null)) {
                    global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("dnSpy.Debugger.DotNet.Mono.Properties.dnSpy.Debugger.DotNet.Mono.Resources", typeof(dnSpy_Debugger_DotNet_Mono_Resources).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }`
  - Summary: Returns the cached ResourceManager instance used by this class.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.ResourceManager;
    ```
- `public static string AttachToProcessXCommand {
            get {
                return ResourceManager.GetString("AttachToProcessXCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Attach to Process ({0})....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.AttachToProcessXCommand;
    ```
- `public static string AttachToUnityProcess_DebugBuildsOnlyMessage {
            get {
                return ResourceManager.GetString("AttachToUnityProcess_DebugBuildsOnlyMessage", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to This is for Unity Debug builds only.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.AttachToUnityProcess_DebugBuildsOnlyMessage;
    ```
- `public static string CanNotSetABreakpointWhenProcessIsPaused {
            get {
                return ResourceManager.GetString("CanNotSetABreakpointWhenProcessIsPaused", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Can't set a breakpoint when the process is paused..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.CanNotSetABreakpointWhenProcessIsPaused;
    ```
- `public static string ConnectToUnity_UseAttachToUnityProcessDlgBoxMessage {
            get {
                return ResourceManager.GetString("ConnectToUnity_UseAttachToUnityProcessDlgBoxMessage", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Use the Attach to Process (Unity) dialog box to attach to debug builds.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.ConnectToUnity_UseAttachToUnityProcessDlgBoxMessage;
    ```
- `public static string CouldNotConnectToUnityGame_MakeSureMonoDllFileIsPatched {
            get {
                return ResourceManager.GetString("CouldNotConnectToUnityGame_MakeSureMonoDllFileIsPatched", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Make sure you have patched the game's mono.dll file.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.CouldNotConnectToUnityGame_MakeSureMonoDllFileIsPatched;
    ```
- `public static string DbgAsm_Args {
            get {
                return ResourceManager.GetString("DbgAsm_Args", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to A_rguments.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgAsm_Args;
    ```
- `public static string DbgAsm_Assembly {
            get {
                return ResourceManager.GetString("DbgAsm_Assembly", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Assembly.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 120)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgAsm_Assembly;
    ```
- `public static string DbgAsm_BreakAt {
            get {
                return ResourceManager.GetString("DbgAsm_BreakAt", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Break at.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgAsm_BreakAt;
    ```
- `public static string DbgAsm_Connect_To_Process {
            get {
                return ResourceManager.GetString("DbgAsm_Connect_To_Process", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Connect.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 138)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgAsm_Connect_To_Process;
    ```
- `public static string DbgAsm_ConnectionPort {
            get {
                return ResourceManager.GetString("DbgAsm_ConnectionPort", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Port.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 147)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgAsm_ConnectionPort;
    ```
- `public static string DbgAsm_ConnectionTimeoutInSeconds {
            get {
                return ResourceManager.GetString("DbgAsm_ConnectionTimeoutInSeconds", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Timeout (s).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 156)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgAsm_ConnectionTimeoutInSeconds;
    ```
- `public static string DbgAsm_Executable {
            get {
                return ResourceManager.GetString("DbgAsm_Executable", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to E_xecutable.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 165)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgAsm_Executable;
    ```
- `public static string DbgAsm_IP_Address {
            get {
                return ResourceManager.GetString("DbgAsm_IP_Address", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to IP Address.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 174)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgAsm_IP_Address;
    ```
- `public static string DbgAsm_ProcessIsSuspended {
            get {
                return ResourceManager.GetString("DbgAsm_ProcessIsSuspended", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Process is paused and _waiting for the debugger.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 183)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgAsm_ProcessIsSuspended;
    ```
- `public static string DbgAsm_WorkingDir {
            get {
                return ResourceManager.GetString("DbgAsm_WorkingDir", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Working Directory.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 192)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgAsm_WorkingDir;
    ```
- `public static string DbgBreak_CreateProcessEvent {
            get {
                return ResourceManager.GetString("DbgBreak_CreateProcessEvent", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to CreateProcess.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 201)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgBreak_CreateProcessEvent;
    ```
- `public static string DbgBreak_Dont {
            get {
                return ResourceManager.GetString("DbgBreak_Dont", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Don't Break.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 210)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgBreak_Dont;
    ```
- `public static string DbgBreak_EntryPoint {
            get {
                return ResourceManager.GetString("DbgBreak_EntryPoint", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Entry Point.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 219)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DbgBreak_EntryPoint;
    ```
- `public static string DebuggingUnityGamesText {
            get {
                return ResourceManager.GetString("DebuggingUnityGamesText", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debugging Unity Games.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 228)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.DebuggingUnityGamesText;
    ```
- `public static string Error_CanNotWriteToThisArgument {
            get {
                return ResourceManager.GetString("Error_CanNotWriteToThisArgument", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to It's not possible to write to 'this'.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 246)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_CanNotWriteToThisArgument;
    ```
- `public static string Error_CannotAccessMemberRuntimeLimitations {
            get {
                return ResourceManager.GetString("Error_CannotAccessMemberRuntimeLimitations", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Member can't be accessed due to runtime limitations.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 237)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_CannotAccessMemberRuntimeLimitations;
    ```
- `public static string Error_ConnectionWasUnexpectedlyClosed {
            get {
                return ResourceManager.GetString("Error_ConnectionWasUnexpectedlyClosed", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The connection to the debugged process was unexpectedly closed.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 255)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_ConnectionWasUnexpectedlyClosed;
    ```
- `public static string Error_CouldNotConnectToProcess {
            get {
                return ResourceManager.GetString("Error_CouldNotConnectToProcess", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Couldn't connect to the debugged process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 264)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_CouldNotConnectToProcess;
    ```
- `public static string Error_CouldNotFindDebuggedProcess {
            get {
                return ResourceManager.GetString("Error_CouldNotFindDebuggedProcess", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Could not find the debugged process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 273)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_CouldNotFindDebuggedProcess;
    ```
- `public static string Error_CouldNotFindFile {
            get {
                return ResourceManager.GetString("Error_CouldNotFindFile", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Could not find {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 282)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_CouldNotFindFile;
    ```
- `public static string Error_CouldNotSetNextStatement {
            get {
                return ResourceManager.GetString("Error_CouldNotSetNextStatement", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Could not set the next statement..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 291)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_CouldNotSetNextStatement;
    ```
- `public static string Error_FileDoesNotExist {
            get {
                return ResourceManager.GetString("Error_FileDoesNotExist", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The file doesn't exist.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 300)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_FileDoesNotExist;
    ```
- `public static string Error_MissingFilename {
            get {
                return ResourceManager.GetString("Error_MissingFilename", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Missing filename.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 309)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_MissingFilename;
    ```
- `public static string Error_RuntimeDoesNotSupportCallingGenericMethods {
            get {
                return ResourceManager.GetString("Error_RuntimeDoesNotSupportCallingGenericMethods", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to This runtime doesn't support calling generic methods.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 318)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_RuntimeDoesNotSupportCallingGenericMethods;
    ```
- `public static string Error_RuntimeDoesNotSupportSettingNewStatement {
            get {
                return ResourceManager.GetString("Error_RuntimeDoesNotSupportSettingNewStatement", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The runtime doesn't support setting a new statement.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 327)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Error_RuntimeDoesNotSupportSettingNewStatement;
    ```
- `public static string ExceptionMessageIsNull {
            get {
                return ResourceManager.GetString("ExceptionMessageIsNull", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to "<no exception message>".
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 336)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.ExceptionMessageIsNull;
    ```
- `public static string Plugin_ShortDescription {
            get {
                return ResourceManager.GetString("Plugin_ShortDescription", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debugger ({0}).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 345)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Plugin_ShortDescription;
    ```
- `public static string StackFrame_FunctionEvaluation {
            get {
                return ResourceManager.GetString("StackFrame_FunctionEvaluation", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Function Evaluation.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 354)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.StackFrame_FunctionEvaluation;
    ```
- `public static string StackFrame_NativeTransition {
            get {
                return ResourceManager.GetString("StackFrame_NativeTransition", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Native Transition.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 363)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.StackFrame_NativeTransition;
    ```
- `public static string Thread_UserState_AbortRequested {
            get {
                return ResourceManager.GetString("Thread_UserState_AbortRequested", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to AbortRequested.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 381)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Thread_UserState_AbortRequested;
    ```
- `public static string Thread_UserState_Aborted {
            get {
                return ResourceManager.GetString("Thread_UserState_Aborted", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Aborted.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 372)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Thread_UserState_Aborted;
    ```
- `public static string Thread_UserState_Background {
            get {
                return ResourceManager.GetString("Thread_UserState_Background", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Background.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 390)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Thread_UserState_Background;
    ```
- `public static string Thread_UserState_StopRequested {
            get {
                return ResourceManager.GetString("Thread_UserState_StopRequested", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to StopRequested.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 408)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Thread_UserState_StopRequested;
    ```
- `public static string Thread_UserState_Stopped {
            get {
                return ResourceManager.GetString("Thread_UserState_Stopped", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Stopped.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 399)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Thread_UserState_Stopped;
    ```
- `public static string Thread_UserState_SuspendRequested {
            get {
                return ResourceManager.GetString("Thread_UserState_SuspendRequested", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to SuspendRequested.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 426)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Thread_UserState_SuspendRequested;
    ```
- `public static string Thread_UserState_Suspended {
            get {
                return ResourceManager.GetString("Thread_UserState_Suspended", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Suspended.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 417)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Thread_UserState_Suspended;
    ```
- `public static string Thread_UserState_Unstarted {
            get {
                return ResourceManager.GetString("Thread_UserState_Unstarted", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Unstarted.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 435)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Thread_UserState_Unstarted;
    ```
- `public static string Thread_UserState_WaitSleepJoin {
            get {
                return ResourceManager.GetString("Thread_UserState_WaitSleepJoin", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to WaitSleepJoin.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 444)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.Thread_UserState_WaitSleepJoin;
    ```
- `public static string UnityEditor {
            get {
                return ResourceManager.GetString("UnityEditor", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Editor.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger.DotNet.Mono/Properties/dnSpy.Debugger.DotNet.Mono.Resources.Designer.cs` (line 453)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.DotNet.Mono.Properties.dnSpy_Debugger_DotNet_Mono_Resources.UnityEditor;
    ```

