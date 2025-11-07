# Namespace `dnSpy.Debugger.Properties`

## Class `dnSpy_Debugger_Resources`

**Example**

```csharp
// Instantiate dnSpy.Debugger.Properties.dnSpy_Debugger_Resources and call its members.
var instance = new dnSpy.Debugger.Properties.dnSpy_Debugger_Resources(/* arguments */);
```

*Defined in* `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 22)

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
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 53)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Culture;
    ```
- `public static global::System.Resources.ResourceManager ResourceManager {
            get {
                if (object.ReferenceEquals(resourceMan, null)) {
                    global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("dnSpy.Debugger.Properties.dnSpy.Debugger.Resources", typeof(dnSpy_Debugger_Resources).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }`
  - Summary: Returns the cached ResourceManager instance used by this class.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 38)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ResourceManager;
    ```
- `public static string AddBreakpointCommand {
            get {
                return ResourceManager.GetString("AddBreakpointCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Add Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 66)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AddBreakpointCommand;
    ```
- `public static string AddExceptionButton {
            get {
                return ResourceManager.GetString("AddExceptionButton", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Add.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 75)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AddExceptionButton;
    ```
- `public static string AddExceptionCommand {
            get {
                return ResourceManager.GetString("AddExceptionCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Add E_xception.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 84)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AddExceptionCommand;
    ```
- `public static string AllRemainingExceptionsNotInList {
            get {
                return ResourceManager.GetString("AllRemainingExceptionsNotInList", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to <All {0} not in this list>.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 93)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AllRemainingExceptionsNotInList;
    ```
- `public static string AppDomainNotAvailable {
            get {
                return ResourceManager.GetString("AppDomainNotAvailable", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to <not available>.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 102)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AppDomainNotAvailable;
    ```
- `public static string AppMenu_Debug {
            get {
                return ResourceManager.GetString("AppMenu_Debug", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Debug.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 111)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AppMenu_Debug;
    ```
- `public static string AppTitle_Debugging {
            get {
                return ResourceManager.GetString("AppTitle_Debugging", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debugging.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 120)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AppTitle_Debugging;
    ```
- `public static string AskAppWindowClosingStopDebugging {
            get {
                return ResourceManager.GetString("AskAppWindowClosingStopDebugging", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Do you want to stop debugging?.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 129)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AskAppWindowClosingStopDebugging;
    ```
- `public static string AskDeleteAllBreakpoints {
            get {
                return ResourceManager.GetString("AskDeleteAllBreakpoints", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Do you want to delete all breakpoints?.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 138)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AskDeleteAllBreakpoints;
    ```
- `public static string AttachToProcessCommand {
            get {
                return ResourceManager.GetString("AttachToProcessCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Attach to _Process....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 192)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AttachToProcessCommand;
    ```
- `public static string AttachToProcess_MakingAnImageEasierToDebug {
            get {
                return ResourceManager.GetString("AttachToProcess_MakingAnImageEasierToDebug", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Making an Image Easier to Debug.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 174)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AttachToProcess_MakingAnImageEasierToDebug;
    ```
- `public static string AttachToProcess_Search_ToolTip {
            get {
                return ResourceManager.GetString("AttachToProcess_Search_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Search for a process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 183)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AttachToProcess_Search_ToolTip;
    ```
- `public static string Attach_AttachToProcess {
            get {
                return ResourceManager.GetString("Attach_AttachToProcess", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Attach to Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 147)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Attach_AttachToProcess;
    ```
- `public static string Attach_UseDnSpy32 {
            get {
                return ResourceManager.GetString("Attach_UseDnSpy32", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Use dnSpy.exe to attach to 64-bit processes.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 156)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Attach_UseDnSpy32;
    ```
- `public static string Attach_UseDnSpy64 {
            get {
                return ResourceManager.GetString("Attach_UseDnSpy64", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Use dnSpy-x86.exe to attach to 32-bit processes.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 165)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Attach_UseDnSpy64;
    ```
- `public static string AutosCommand {
            get {
                return ResourceManager.GetString("AutosCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Autos.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 201)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.AutosCommand;
    ```
- `public static string BgImgDisplayName_DebuggerMemory {
            get {
                return ResourceManager.GetString("BgImgDisplayName_DebuggerMemory", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Hex Editor (Memory Window).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 210)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.BgImgDisplayName_DebuggerMemory;
    ```
- `public static string BreakCommand {
            get {
                return ResourceManager.GetString("BreakCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Brea_k All.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 219)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.BreakCommand;
    ```
- `public static string BreakProcessCommand {
            get {
                return ResourceManager.GetString("BreakProcessCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Break Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 633)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.BreakProcessCommand;
    ```
- `public static string BreakpointExpressionMustBeABooleanExpression {
            get {
                return ResourceManager.GetString("BreakpointExpressionMustBeABooleanExpression", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The breakpoint expression must be a boolean expression.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 435)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.BreakpointExpressionMustBeABooleanExpression;
    ```
- `public static string BreakpointMessage_CouldNotCreateBreakpoint {
            get {
                return ResourceManager.GetString("BreakpointMessage_CouldNotCreateBreakpoint", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Could not create the breakpoint..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 444)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.BreakpointMessage_CouldNotCreateBreakpoint;
    ```
- `public static string BreakpointMessage_TheFunctionCanNotBeFound {
            get {
                return ResourceManager.GetString("BreakpointMessage_TheFunctionCanNotBeFound", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The function cannot be found: {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 453)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.BreakpointMessage_TheFunctionCanNotBeFound;
    ```
- `public static string Breakpoint_Condition_ConditionalExpression {
            get {
                return ResourceManager.GetString("Breakpoint_Condition_ConditionalExpression", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Conditional expression:.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 228)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Condition_ConditionalExpression;
    ```
- `public static string Breakpoint_Condition_IsTrue {
            get {
                return ResourceManager.GetString("Breakpoint_Condition_IsTrue", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Is true.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 237)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Condition_IsTrue;
    ```
- `public static string Breakpoint_Condition_NoCondition {
            get {
                return ResourceManager.GetString("Breakpoint_Condition_NoCondition", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to (no condition).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 246)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Condition_NoCondition;
    ```
- `public static string Breakpoint_Condition_WhenChanged {
            get {
                return ResourceManager.GetString("Breakpoint_Condition_WhenChanged", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to When changed.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 255)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Condition_WhenChanged;
    ```
- `public static string Breakpoint_Condition_WhenConditionHasChanged {
            get {
                return ResourceManager.GetString("Breakpoint_Condition_WhenConditionHasChanged", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to when '{0}' has changed.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 264)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Condition_WhenConditionHasChanged;
    ```
- `public static string Breakpoint_Condition_WhenConditionHasChanged2 {
            get {
                return ResourceManager.GetString("Breakpoint_Condition_WhenConditionHasChanged2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to '{0}' has changed.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 273)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Condition_WhenConditionHasChanged2;
    ```
- `public static string Breakpoint_Condition_WhenConditionIsTrue {
            get {
                return ResourceManager.GetString("Breakpoint_Condition_WhenConditionIsTrue", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to when '{0}' is true.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 282)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Condition_WhenConditionIsTrue;
    ```
- `public static string Breakpoint_Condition_WhenConditionIsTrue2 {
            get {
                return ResourceManager.GetString("Breakpoint_Condition_WhenConditionIsTrue2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to '{0}' is true.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 291)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Condition_WhenConditionIsTrue2;
    ```
- `public static string Breakpoint_Filter_Filter {
            get {
                return ResourceManager.GetString("Breakpoint_Filter_Filter", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Filter: '{0}'.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 300)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Filter_Filter;
    ```
- `public static string Breakpoint_Filter_NoFilter {
            get {
                return ResourceManager.GetString("Breakpoint_Filter_NoFilter", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to (none).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 309)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Filter_NoFilter;
    ```
- `public static string Breakpoint_HitCount_CurrentHitCountValue {
            get {
                return ResourceManager.GetString("Breakpoint_HitCount_CurrentHitCountValue", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to currently {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 318)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_HitCount_CurrentHitCountValue;
    ```
- `public static string Breakpoint_HitCount_HitCountIsAMultipleOf {
            get {
                return ResourceManager.GetString("Breakpoint_HitCount_HitCountIsAMultipleOf", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to when hit count is a multiple of {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 327)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_HitCount_HitCountIsAMultipleOf;
    ```
- `public static string Breakpoint_HitCount_HitCountIsAMultipleOf2 {
            get {
                return ResourceManager.GetString("Breakpoint_HitCount_HitCountIsAMultipleOf2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Hit count is a multiple of {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 336)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_HitCount_HitCountIsAMultipleOf2;
    ```
- `public static string Breakpoint_HitCount_HitCountIsEqualTo {
            get {
                return ResourceManager.GetString("Breakpoint_HitCount_HitCountIsEqualTo", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to when hit count is equal to {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 345)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_HitCount_HitCountIsEqualTo;
    ```
- `public static string Breakpoint_HitCount_HitCountIsEqualTo2 {
            get {
                return ResourceManager.GetString("Breakpoint_HitCount_HitCountIsEqualTo2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Hit count is equal to {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 354)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_HitCount_HitCountIsEqualTo2;
    ```
- `public static string Breakpoint_HitCount_HitCountIsGreaterThanOrEqualTo {
            get {
                return ResourceManager.GetString("Breakpoint_HitCount_HitCountIsGreaterThanOrEqualTo", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to when hit count is greater than or equal to {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 363)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_HitCount_HitCountIsGreaterThanOrEqualTo;
    ```
- `public static string Breakpoint_HitCount_HitCountIsGreaterThanOrEqualTo2 {
            get {
                return ResourceManager.GetString("Breakpoint_HitCount_HitCountIsGreaterThanOrEqualTo2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Hit count is greater than or equal to {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 372)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_HitCount_HitCountIsGreaterThanOrEqualTo2;
    ```
- `public static string Breakpoint_HitCount_IsAMultipleOf {
            get {
                return ResourceManager.GetString("Breakpoint_HitCount_IsAMultipleOf", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Is a multiple of.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 381)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_HitCount_IsAMultipleOf;
    ```
- `public static string Breakpoint_HitCount_NoHitCount {
            get {
                return ResourceManager.GetString("Breakpoint_HitCount_NoHitCount", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to break always.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 390)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_HitCount_NoHitCount;
    ```
- `public static string Breakpoint_Tracepoint_BreakPrintMessage {
            get {
                return ResourceManager.GetString("Breakpoint_Tracepoint_BreakPrintMessage", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Break and print message '{0}'.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 399)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Tracepoint_BreakPrintMessage;
    ```
- `public static string Breakpoint_Tracepoint_NoTraceMessage {
            get {
                return ResourceManager.GetString("Breakpoint_Tracepoint_NoTraceMessage", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Break.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 408)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Tracepoint_NoTraceMessage;
    ```
- `public static string Breakpoint_Tracepoint_PrintMessage {
            get {
                return ResourceManager.GetString("Breakpoint_Tracepoint_PrintMessage", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Print message '{0}'.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 417)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Tracepoint_PrintMessage;
    ```
- `public static string Breakpoint_Tracepoint_PrintMessage2 {
            get {
                return ResourceManager.GetString("Breakpoint_Tracepoint_PrintMessage2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Log message '{0}', to Output window.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 426)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoint_Tracepoint_PrintMessage2;
    ```
- `public static string BreakpointsCommand {
            get {
                return ResourceManager.GetString("BreakpointsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Breakpoints.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 624)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.BreakpointsCommand;
    ```
- `public static string Breakpoints_AddBreakpoint_ToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_AddBreakpoint_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Add breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 462)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_AddBreakpoint_ToolTip;
    ```
- `public static string Breakpoints_BreakpointWillNotBeHit {
            get {
                return ResourceManager.GetString("Breakpoints_BreakpointWillNotBeHit", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The breakpoint will not currently be hit. {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 471)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_BreakpointWillNotBeHit;
    ```
- `public static string Breakpoints_ExportMatchingBreakpoints_ToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_ExportMatchingBreakpoints_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Export all breakpoints matching the current search criteria.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 480)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_ExportMatchingBreakpoints_ToolTip;
    ```
- `public static string Breakpoints_GlyphMargin_BreakWhenBreakpointHit {
            get {
                return ResourceManager.GetString("Breakpoints_GlyphMargin_BreakWhenBreakpointHit", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Break.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 489)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_GlyphMargin_BreakWhenBreakpointHit;
    ```
- `public static string Breakpoints_GlyphMargin_DisableBreakpoint {
            get {
                return ResourceManager.GetString("Breakpoints_GlyphMargin_DisableBreakpoint", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Disable breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 498)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_GlyphMargin_DisableBreakpoint;
    ```
- `public static string Breakpoints_GlyphMargin_EnableBreakpoint {
            get {
                return ResourceManager.GetString("Breakpoints_GlyphMargin_EnableBreakpoint", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Enable breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 507)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_GlyphMargin_EnableBreakpoint;
    ```
- `public static string Breakpoints_GlyphMargin_ShowSettingsToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_GlyphMargin_ShowSettingsToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Settings....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 516)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_GlyphMargin_ShowSettingsToolTip;
    ```
- `public static string Breakpoints_GoToDisassembly_ToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_GoToDisassembly_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Go To Disassembly.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 525)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_GoToDisassembly_ToolTip;
    ```
- `public static string Breakpoints_GoToSourceCode_ToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_GoToSourceCode_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Go To Source Code.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 534)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_GoToSourceCode_ToolTip;
    ```
- `public static string Breakpoints_ImportBreakpoints_ToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_ImportBreakpoints_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Import breakpoints from a file.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 543)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_ImportBreakpoints_ToolTip;
    ```
- `public static string Breakpoints_ModuleNotLoaded {
            get {
                return ResourceManager.GetString("Breakpoints_ModuleNotLoaded", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The module hasn't been loaded or no symbols have been loaded for this module..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 552)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_ModuleNotLoaded;
    ```
- `public static string Breakpoints_NoMatch {
            get {
                return ResourceManager.GetString("Breakpoints_NoMatch", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to No breakpoints match your search filter..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 561)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_NoMatch;
    ```
- `public static string Breakpoints_RemoveBreakpoint_ToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_RemoveBreakpoint_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Remove breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 570)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_RemoveBreakpoint_ToolTip;
    ```
- `public static string Breakpoints_RemoveMatchingBreakpoints_ToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_RemoveMatchingBreakpoints_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Remove all breakpoints matching the current search criteria.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 579)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_RemoveMatchingBreakpoints_ToolTip;
    ```
- `public static string Breakpoints_ResetSearchSettings_ToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_ResetSearchSettings_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Reset all search criteria so that all breakpoints are shown.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 588)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_ResetSearchSettings_ToolTip;
    ```
- `public static string Breakpoints_Search {
            get {
                return ResourceManager.GetString("Breakpoints_Search", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Search.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 597)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_Search;
    ```
- `public static string Breakpoints_Search_ToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_Search_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Search for a breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 606)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_Search_ToolTip;
    ```
- `public static string Breakpoints_ToggleMatchingBreakpoints_ToolTip {
            get {
                return ResourceManager.GetString("Breakpoints_ToggleMatchingBreakpoints_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Enable or disable all breakpoints matching the current search criteria.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 615)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Breakpoints_ToggleMatchingBreakpoints_ToolTip;
    ```
- `public static string Button_AddCondition {
            get {
                return ResourceManager.GetString("Button_AddCondition", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Add Condition.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 642)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Button_AddCondition;
    ```
- `public static string Button_Attach {
            get {
                return ResourceManager.GetString("Button_Attach", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Attach.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 651)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Button_Attach;
    ```
- `public static string Button_Cancel {
            get {
                return ResourceManager.GetString("Button_Cancel", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Cancel.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 660)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Button_Cancel;
    ```
- `public static string Button_OK {
            get {
                return ResourceManager.GetString("Button_OK", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _OK.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 669)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Button_OK;
    ```
- `public static string Button_Refresh {
            get {
                return ResourceManager.GetString("Button_Refresh", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Refresh.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 678)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Button_Refresh;
    ```
- `public static string CallStackBreakpointCommand {
            get {
                return ResourceManager.GetString("CallStackBreakpointCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 696)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.CallStackBreakpointCommand;
    ```
- `public static string CallStackCommand {
            get {
                return ResourceManager.GetString("CallStackCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Call Stack.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 705)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.CallStackCommand;
    ```
- `public static string CallStack_MaxFramesExceeded {
            get {
                return ResourceManager.GetString("CallStack_MaxFramesExceeded", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The maximum number of stack frames supported by dnSpy has been exceeded..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 687)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.CallStack_MaxFramesExceeded;
    ```
- `public static string CannotReadLocalOrArgumentMaybeOptimizedAway {
            get {
                return ResourceManager.GetString("CannotReadLocalOrArgumentMaybeOptimizedAway", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Cannot obtain value of the local variable or argument because it is not available at this instruction pointer, possibly because it has been optimized away..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 714)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.CannotReadLocalOrArgumentMaybeOptimizedAway;
    ```
- `public static string ClearAllCommand {
            get {
                return ResourceManager.GetString("ClearAllCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Clear All.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 723)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ClearAllCommand;
    ```
- `public static string Column_Address {
            get {
                return ResourceManager.GetString("Column_Address", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Address.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 732)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Address;
    ```
- `public static string Column_AppDomain {
            get {
                return ResourceManager.GetString("Column_AppDomain", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to AppDomain.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 741)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_AppDomain;
    ```
- `public static string Column_BreakWhenThrown {
            get {
                return ResourceManager.GetString("Column_BreakWhenThrown", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Break When Thrown.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 750)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_BreakWhenThrown;
    ```
- `public static string Column_Category {
            get {
                return ResourceManager.GetString("Column_Category", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Category.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 759)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Category;
    ```
- `public static string Column_Condition {
            get {
                return ResourceManager.GetString("Column_Condition", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Condition.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 768)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Condition;
    ```
- `public static string Column_Conditions {
            get {
                return ResourceManager.GetString("Column_Conditions", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Conditions.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 777)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Conditions;
    ```
- `public static string Column_Debugging {
            get {
                return ResourceManager.GetString("Column_Debugging", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debugging.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 786)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Debugging;
    ```
- `public static string Column_DynamicModule {
            get {
                return ResourceManager.GetString("Column_DynamicModule", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Dynamic.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 795)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_DynamicModule;
    ```
- `public static string Column_Filter {
            get {
                return ResourceManager.GetString("Column_Filter", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Filter.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 804)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Filter;
    ```
- `public static string Column_HitCount {
            get {
                return ResourceManager.GetString("Column_HitCount", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Hit Count.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 813)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_HitCount;
    ```
- `public static string Column_ID {
            get {
                return ResourceManager.GetString("Column_ID", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to ID.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 822)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ID;
    ```
- `public static string Column_InMemoryModule {
            get {
                return ResourceManager.GetString("Column_InMemoryModule", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to InMemory.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 831)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_InMemoryModule;
    ```
- `public static string Column_Labels {
            get {
                return ResourceManager.GetString("Column_Labels", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Labels.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 840)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Labels;
    ```
- `public static string Column_Module {
            get {
                return ResourceManager.GetString("Column_Module", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Module.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 849)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Module;
    ```
- `public static string Column_Name {
            get {
                return ResourceManager.GetString("Column_Name", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Name.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 858)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Name;
    ```
- `public static string Column_OptimizedModule {
            get {
                return ResourceManager.GetString("Column_OptimizedModule", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Optimized.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 867)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_OptimizedModule;
    ```
- `public static string Column_Order {
            get {
                return ResourceManager.GetString("Column_Order", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Order.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 876)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Order;
    ```
- `public static string Column_Path {
            get {
                return ResourceManager.GetString("Column_Path", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Path.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 885)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Path;
    ```
- `public static string Column_Process {
            get {
                return ResourceManager.GetString("Column_Process", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 894)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Process;
    ```
- `public static string Column_ProcessArchitecture {
            get {
                return ResourceManager.GetString("Column_ProcessArchitecture", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Architecture.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 903)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ProcessArchitecture;
    ```
- `public static string Column_ProcessCommandLine {
            get {
                return ResourceManager.GetString("Column_ProcessCommandLine", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Command Line.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 912)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ProcessCommandLine;
    ```
- `public static string Column_ProcessFilename {
            get {
                return ResourceManager.GetString("Column_ProcessFilename", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Filename.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 921)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ProcessFilename;
    ```
- `public static string Column_ProcessID {
            get {
                return ResourceManager.GetString("Column_ProcessID", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to ID.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 930)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ProcessID;
    ```
- `public static string Column_ProcessName {
            get {
                return ResourceManager.GetString("Column_ProcessName", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Process Name.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 939)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ProcessName;
    ```
- `public static string Column_ProcessTitle {
            get {
                return ResourceManager.GetString("Column_ProcessTitle", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Title.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 948)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ProcessTitle;
    ```
- `public static string Column_ProcessType {
            get {
                return ResourceManager.GetString("Column_ProcessType", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Type.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 957)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ProcessType;
    ```
- `public static string Column_State {
            get {
                return ResourceManager.GetString("Column_State", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to State.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 966)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_State;
    ```
- `public static string Column_ThreadAffinityMask {
            get {
                return ResourceManager.GetString("Column_ThreadAffinityMask", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Affinity Mask.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 975)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ThreadAffinityMask;
    ```
- `public static string Column_ThreadCategory {
            get {
                return ResourceManager.GetString("Column_ThreadCategory", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Category.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 984)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ThreadCategory;
    ```
- `public static string Column_ThreadID {
            get {
                return ResourceManager.GetString("Column_ThreadID", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to ID.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 993)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ThreadID;
    ```
- `public static string Column_ThreadLocation {
            get {
                return ResourceManager.GetString("Column_ThreadLocation", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Location.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1002)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ThreadLocation;
    ```
- `public static string Column_ThreadManagedId {
            get {
                return ResourceManager.GetString("Column_ThreadManagedId", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Managed ID.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1011)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ThreadManagedId;
    ```
- `public static string Column_ThreadPriority {
            get {
                return ResourceManager.GetString("Column_ThreadPriority", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Priority.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1020)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ThreadPriority;
    ```
- `public static string Column_ThreadState {
            get {
                return ResourceManager.GetString("Column_ThreadState", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to State.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1029)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ThreadState;
    ```
- `public static string Column_ThreadSuspendedCount {
            get {
                return ResourceManager.GetString("Column_ThreadSuspendedCount", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Suspended Count.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1038)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_ThreadSuspendedCount;
    ```
- `public static string Column_Timestamp {
            get {
                return ResourceManager.GetString("Column_Timestamp", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Timestamp.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1047)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Timestamp;
    ```
- `public static string Column_Title {
            get {
                return ResourceManager.GetString("Column_Title", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Title.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1056)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Title;
    ```
- `public static string Column_Type {
            get {
                return ResourceManager.GetString("Column_Type", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Type.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1065)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Type;
    ```
- `public static string Column_Value {
            get {
                return ResourceManager.GetString("Column_Value", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Value.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1074)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Value;
    ```
- `public static string Column_Version {
            get {
                return ResourceManager.GetString("Column_Version", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Version.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1083)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_Version;
    ```
- `public static string Column_WhenHit {
            get {
                return ResourceManager.GetString("Column_WhenHit", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to When Hit.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1092)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Column_WhenHit;
    ```
- `public static string ContinueDebuggingCommand {
            get {
                return ResourceManager.GetString("ContinueDebuggingCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Continue.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1101)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ContinueDebuggingCommand;
    ```
- `public static string ContinueProcessCommand {
            get {
                return ResourceManager.GetString("ContinueProcessCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Continue Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1110)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ContinueProcessCommand;
    ```
- `public static string CopyCommand {
            get {
                return ResourceManager.GetString("CopyCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Cop_y.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1119)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.CopyCommand;
    ```
- `public static string CopyExpressionCommand {
            get {
                return ResourceManager.GetString("CopyExpressionCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Copy E_xpression.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1128)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.CopyExpressionCommand;
    ```
- `public static string DbgAsm_DebugEngine {
            get {
                return ResourceManager.GetString("DbgAsm_DebugEngine", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Debug engine.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1137)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgAsm_DebugEngine;
    ```
- `public static string DbgAsm_Title {
            get {
                return ResourceManager.GetString("DbgAsm_Title", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debug Program.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1146)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgAsm_Title;
    ```
- `public static string DbgSettings_AsyncDebugging {
            get {
                return ResourceManager.GetString("DbgSettings_AsyncDebugging", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Enable async debugging.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1155)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_AsyncDebugging;
    ```
- `public static string DbgSettings_AutoOpenLocalsWindow {
            get {
                return ResourceManager.GetString("DbgSettings_AutoOpenLocalsWindow", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show the Locals window when the debugger starts.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1164)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_AutoOpenLocalsWindow;
    ```
- `public static string DbgSettings_BreakAllProcesses {
            get {
                return ResourceManager.GetString("DbgSettings_BreakAllProcesses", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Break all processes when one process breaks.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1173)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_BreakAllProcesses;
    ```
- `public static string DbgSettings_DebugEngine {
            get {
                return ResourceManager.GetString("DbgSettings_DebugEngine", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debug Engine.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1182)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_DebugEngine;
    ```
- `public static string DbgSettings_DisableDebuggerDetection {
            get {
                return ResourceManager.GetString("DbgSettings_DisableDebuggerDetection", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Prevent code from detecting the debugger.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1191)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_DisableDebuggerDetection;
    ```
- `public static string DbgSettings_EnableManagedDebuggingAssistants {
            get {
                return ResourceManager.GetString("DbgSettings_EnableManagedDebuggingAssistants", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Enable Managed Debugging Assistants (MDA).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1200)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_EnableManagedDebuggingAssistants;
    ```
- `public static string DbgSettings_FocusActiveProcess {
            get {
                return ResourceManager.GetString("DbgSettings_FocusActiveProcess", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Give focus to debugged process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1209)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_FocusActiveProcess;
    ```
- `public static string DbgSettings_GroupParametersAndLocalsTogether {
            get {
                return ResourceManager.GetString("DbgSettings_GroupParametersAndLocalsTogether", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Group parameters and locals together.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1218)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_GroupParametersAndLocalsTogether;
    ```
- `public static string DbgSettings_HideCompilerGeneratedMembers {
            get {
                return ResourceManager.GetString("DbgSettings_HideCompilerGeneratedMembers", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Hide compiler generated members.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1227)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_HideCompilerGeneratedMembers;
    ```
- `public static string DbgSettings_HideDeprecatedError {
            get {
                return ResourceManager.GetString("DbgSettings_HideDeprecatedError", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Hide deprecated members in variables windows.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1236)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_HideDeprecatedError;
    ```
- `public static string DbgSettings_HighlightChangedVariables {
            get {
                return ResourceManager.GetString("DbgSettings_HighlightChangedVariables", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Highlight changed variables in variables windows.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1245)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_HighlightChangedVariables;
    ```
- `public static string DbgSettings_IgnoreBreakInstructions {
            get {
                return ResourceManager.GetString("DbgSettings_IgnoreBreakInstructions", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ignore Debugger.Break() and break instructions.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1254)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_IgnoreBreakInstructions;
    ```
- `public static string DbgSettings_Language {
            get {
                return ResourceManager.GetString("DbgSettings_Language", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Language.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1263)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_Language;
    ```
- `public static string DbgSettings_PropertyEvalAndFunctionCalls {
            get {
                return ResourceManager.GetString("DbgSettings_PropertyEvalAndFunctionCalls", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Enable property evaluation and other implicit function calls.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1272)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_PropertyEvalAndFunctionCalls;
    ```
- `public static string DbgSettings_RedirectGuiConsoleOutput {
            get {
                return ResourceManager.GetString("DbgSettings_RedirectGuiConsoleOutput", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Redirect GUI applications' console output to the Output window.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1281)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_RedirectGuiConsoleOutput;
    ```
- `public static string DbgSettings_RespectHideMemberAttributes {
            get {
                return ResourceManager.GetString("DbgSettings_RespectHideMemberAttributes", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Respect attributes that hide members.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1290)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_RespectHideMemberAttributes;
    ```
- `public static string DbgSettings_ShowCompilerGeneratedVariables {
            get {
                return ResourceManager.GetString("DbgSettings_ShowCompilerGeneratedVariables", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show compiler generated variables.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1299)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_ShowCompilerGeneratedVariables;
    ```
- `public static string DbgSettings_ShowDecompilerGeneratedVariables {
            get {
                return ResourceManager.GetString("DbgSettings_ShowDecompilerGeneratedVariables", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show decompiler generated variables.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1308)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_ShowDecompilerGeneratedVariables;
    ```
- `public static string DbgSettings_ShowRawLocals {
            get {
                return ResourceManager.GetString("DbgSettings_ShowRawLocals", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show raw locals.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1317)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_ShowRawLocals;
    ```
- `public static string DbgSettings_ShowRawStructureOfObjects {
            get {
                return ResourceManager.GetString("DbgSettings_ShowRawStructureOfObjects", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show raw structure of objects in variables windows.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1326)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_ShowRawStructureOfObjects;
    ```
- `public static string DbgSettings_ShowReturnValues {
            get {
                return ResourceManager.GetString("DbgSettings_ShowReturnValues", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show return values.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1335)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_ShowReturnValues;
    ```
- `public static string DbgSettings_SortLocals {
            get {
                return ResourceManager.GetString("DbgSettings_SortLocals", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Sort locals.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1344)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_SortLocals;
    ```
- `public static string DbgSettings_SortParameters {
            get {
                return ResourceManager.GetString("DbgSettings_SortParameters", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Sort parameters.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1353)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_SortParameters;
    ```
- `public static string DbgSettings_StepOverPropertiesAndOperators {
            get {
                return ResourceManager.GetString("DbgSettings_StepOverPropertiesAndOperators", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step over properties and operators.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1362)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_StepOverPropertiesAndOperators;
    ```
- `public static string DbgSettings_SuppressJITOptimization {
            get {
                return ResourceManager.GetString("DbgSettings_SuppressJITOptimization", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Suppress JIT optimization on module load.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1371)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_SuppressJITOptimization;
    ```
- `public static string DbgSettings_SuppressJITOptimization_ProgramModules {
            get {
                return ResourceManager.GetString("DbgSettings_SuppressJITOptimization_ProgramModules", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Program modules.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1380)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_SuppressJITOptimization_ProgramModules;
    ```
- `public static string DbgSettings_SuppressJITOptimization_SystemModules {
            get {
                return ResourceManager.GetString("DbgSettings_SuppressJITOptimization_SystemModules", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to System modules.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1389)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_SuppressJITOptimization_SystemModules;
    ```
- `public static string DbgSettings_SyntaxHighlight {
            get {
                return ResourceManager.GetString("DbgSettings_SyntaxHighlight", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Syntax highlight.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1398)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_SyntaxHighlight;
    ```
- `public static string DbgSettings_UseMemoryModules {
            get {
                return ResourceManager.GetString("DbgSettings_UseMemoryModules", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debug files loaded from the process' memory (uncheck to use disk files).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1407)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_UseMemoryModules;
    ```
- `public static string DbgSettings_UseStringConversionFunction {
            get {
                return ResourceManager.GetString("DbgSettings_UseStringConversionFunction", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Call string-conversion function on objects in variables windows.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1416)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DbgSettings_UseStringConversionFunction;
    ```
- `public static string DebugLogAdditionalInformation {
            get {
                return ResourceManager.GetString("DebugLogAdditionalInformation", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Additional information: {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1470)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugLogAdditionalInformation;
    ```
- `public static string DebugLogExceptionHandled {
            get {
                return ResourceManager.GetString("DebugLogExceptionHandled", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Exception thrown: '{0}' in {1}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1479)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugLogExceptionHandled;
    ```
- `public static string DebugLogExceptionUnhandled {
            get {
                return ResourceManager.GetString("DebugLogExceptionUnhandled", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to An unhandled exception of type '{0}' occurred in {1}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1488)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugLogExceptionUnhandled;
    ```
- `public static string DebugLogExitProcess {
            get {
                return ResourceManager.GetString("DebugLogExitProcess", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The program '{0}' has exited with code {1} (0x{1:x})..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1497)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugLogExitProcess;
    ```
- `public static string DebugLogExitThread {
            get {
                return ResourceManager.GetString("DebugLogExitThread", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The thread 0x{0:x} has exited with code {1} (0x{1:x})..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1506)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugLogExitThread;
    ```
- `public static string DebugLogLoadModule {
            get {
                return ResourceManager.GetString("DebugLogLoadModule", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Loaded '{0}'..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1524)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugLogLoadModule;
    ```
- `public static string DebugLogMDA {
            get {
                return ResourceManager.GetString("DebugLogMDA", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Managed Debugging Assistant '{0}' has detected a problem in '{1}'..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1533)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugLogMDA;
    ```
- `public static string DebugLogUnloadModule {
            get {
                return ResourceManager.GetString("DebugLogUnloadModule", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Unloaded '{0}'..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1542)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugLogUnloadModule;
    ```
- `public static string DebugLoggerName {
            get {
                return ResourceManager.GetString("DebugLoggerName", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debug.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1515)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugLoggerName;
    ```
- `public static string DebugProgramX {
            get {
                return ResourceManager.GetString("DebugProgramX", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Debug {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1551)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugProgramX;
    ```
- `public static string DebugStepProcessError {
            get {
                return ResourceManager.GetString("DebugStepProcessError", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Could not step: {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1560)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugStepProcessError;
    ```
- `public static string DebugWindows {
            get {
                return ResourceManager.GetString("DebugWindows", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Windows.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1569)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebugWindows;
    ```
- `public static string Debug_EventDescription_Exception {
            get {
                return ResourceManager.GetString("Debug_EventDescription_Exception", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Exception.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1425)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Debug_EventDescription_Exception;
    ```
- `public static string Debug_EventDescription_LoadModule1 {
            get {
                return ResourceManager.GetString("Debug_EventDescription_LoadModule1", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to LoadModule DYN={0} MEM={1} {2:X8} {3:X8} {4}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1434)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Debug_EventDescription_LoadModule1;
    ```
- `public static string Debug_EventDescription_LoadModule2 {
            get {
                return ResourceManager.GetString("Debug_EventDescription_LoadModule2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to LoadModule A={0:X8} S={1:X8} {2}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1443)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Debug_EventDescription_LoadModule2;
    ```
- `public static string Debug_EventDescription_UnhandledException {
            get {
                return ResourceManager.GetString("Debug_EventDescription_UnhandledException", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Unhandled Exception.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1452)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Debug_EventDescription_UnhandledException;
    ```
- `public static string DebuggerOptDlgTab {
            get {
                return ResourceManager.GetString("DebuggerOptDlgTab", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debugger.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1461)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DebuggerOptDlgTab;
    ```
- `public static string DeleteAllBreakpointsCommand {
            get {
                return ResourceManager.GetString("DeleteAllBreakpointsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Delete _All Breakpoints.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1578)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DeleteAllBreakpointsCommand;
    ```
- `public static string DeleteBreakpointCommand {
            get {
                return ResourceManager.GetString("DeleteBreakpointCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to D_elete Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1587)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DeleteBreakpointCommand;
    ```
- `public static string DeleteObjectIdCommand {
            get {
                return ResourceManager.GetString("DeleteObjectIdCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Delete Object ID.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1596)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DeleteObjectIdCommand;
    ```
- `public static string DeleteWatchCommand {
            get {
                return ResourceManager.GetString("DeleteWatchCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Delete Watch.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1605)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DeleteWatchCommand;
    ```
- `public static string DetachAllCommand {
            get {
                return ResourceManager.GetString("DetachAllCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Detach A_ll.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1614)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DetachAllCommand;
    ```
- `public static string DetachProcessCommand {
            get {
                return ResourceManager.GetString("DetachProcessCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Detach Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1623)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DetachProcessCommand;
    ```
- `public static string DetachWhenDebuggingStoppedCommand {
            get {
                return ResourceManager.GetString("DetachWhenDebuggingStoppedCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Detach _When Debugging Stopped.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1632)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DetachWhenDebuggingStoppedCommand;
    ```
- `public static string DigitSeparatorsCommand {
            get {
                return ResourceManager.GetString("DigitSeparatorsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Digit Separators.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1641)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DigitSeparatorsCommand;
    ```
- `public static string DisableAllBreakpointsCommand {
            get {
                return ResourceManager.GetString("DisableAllBreakpointsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Disable All Breakpoi_nts.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1650)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DisableAllBreakpointsCommand;
    ```
- `public static string DisableBreakpointCommand2 {
            get {
                return ResourceManager.GetString("DisableBreakpointCommand2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Disable Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1659)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DisableBreakpointCommand2;
    ```
- `public static string DisableBreakpointCommand3 {
            get {
                return ResourceManager.GetString("DisableBreakpointCommand3", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Disable Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1668)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DisableBreakpointCommand3;
    ```
- `public static string DisassemblyCommand {
            get {
                return ResourceManager.GetString("DisassemblyCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Disassembly.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1677)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.DisassemblyCommand;
    ```
- `public static string EditAppDomainNameCommand {
            get {
                return ResourceManager.GetString("EditAppDomainNameCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Edit AppDomain Name.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1686)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditAppDomainNameCommand;
    ```
- `public static string EditBreakpointSettings_ConditionalExpression {
            get {
                return ResourceManager.GetString("EditBreakpointSettings_ConditionalExpression", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Conditional _Expression.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1695)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditBreakpointSettings_ConditionalExpression;
    ```
- `public static string EditBreakpointSettings_Filter {
            get {
                return ResourceManager.GetString("EditBreakpointSettings_Filter", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Filter.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1704)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditBreakpointSettings_Filter;
    ```
- `public static string EditBreakpointSettings_HitCount {
            get {
                return ResourceManager.GetString("EditBreakpointSettings_HitCount", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Hit Count.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1713)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditBreakpointSettings_HitCount;
    ```
- `public static string EditBreakpointSettings_Title {
            get {
                return ResourceManager.GetString("EditBreakpointSettings_Title", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Breakpoint Settings.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1722)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditBreakpointSettings_Title;
    ```
- `public static string EditBreakpointSettings_Trace {
            get {
                return ResourceManager.GetString("EditBreakpointSettings_Trace", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Log Message.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1731)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditBreakpointSettings_Trace;
    ```
- `public static string EditBreakpointSettings_TraceContinue {
            get {
                return ResourceManager.GetString("EditBreakpointSettings_TraceContinue", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Continue execution.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1740)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditBreakpointSettings_TraceContinue;
    ```
- `public static string EditConditionsCommand {
            get {
                return ResourceManager.GetString("EditConditionsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Edit Conditions....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1758)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditConditionsCommand;
    ```
- `public static string EditConditions_Title {
            get {
                return ResourceManager.GetString("EditConditions_Title", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Edit Conditions.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1749)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditConditions_Title;
    ```
- `public static string EditLabelsCommand {
            get {
                return ResourceManager.GetString("EditLabelsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Edit Labels.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1767)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditLabelsCommand;
    ```
- `public static string EditLabelsMsgBoxLabel {
            get {
                return ResourceManager.GetString("EditLabelsMsgBoxLabel", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Labels.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1776)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditLabelsMsgBoxLabel;
    ```
- `public static string EditLabelsTitle {
            get {
                return ResourceManager.GetString("EditLabelsTitle", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Edit Labels.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1785)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditLabelsTitle;
    ```
- `public static string EditModuleNameCommand {
            get {
                return ResourceManager.GetString("EditModuleNameCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Edit Module Name.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1794)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditModuleNameCommand;
    ```
- `public static string EditOrderCommand {
            get {
                return ResourceManager.GetString("EditOrderCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Edit Module Load Order.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1803)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditOrderCommand;
    ```
- `public static string EditProcessNameCommand {
            get {
                return ResourceManager.GetString("EditProcessNameCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Edit Process Name.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1812)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EditProcessNameCommand;
    ```
- `public static string EnableAllBreakpointsCommand {
            get {
                return ResourceManager.GetString("EnableAllBreakpointsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Enable All Breakpoi_nts.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1821)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EnableAllBreakpointsCommand;
    ```
- `public static string EnableBreakpointCommand {
            get {
                return ResourceManager.GetString("EnableBreakpointCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Enable Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1830)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EnableBreakpointCommand;
    ```
- `public static string EnableBreakpointCommand2 {
            get {
                return ResourceManager.GetString("EnableBreakpointCommand2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Enab_le Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1839)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EnableBreakpointCommand2;
    ```
- `public static string EnableBreakpointCommand3 {
            get {
                return ResourceManager.GetString("EnableBreakpointCommand3", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Enable Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1848)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.EnableBreakpointCommand3;
    ```
- `public static string ErrorEvaluatingExpression {
            get {
                return ResourceManager.GetString("ErrorEvaluatingExpression", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Couldn't evaluate the expression.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1894)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ErrorEvaluatingExpression;
    ```
- `public static string ErrorOccurredX {
            get {
                return ResourceManager.GetString("ErrorOccurredX", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to An error occurred: {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1905)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ErrorOccurredX;
    ```
- `public static string Error_CantEvalUnlessDebuggerStopped {
            get {
                return ResourceManager.GetString("Error_CantEvalUnlessDebuggerStopped", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Can't evaluate unless debugger is stopped.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1857)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Error_CantEvalUnlessDebuggerStopped;
    ```
- `public static string Error_CantEvalWhenUnhandledExceptionHasOccurred {
            get {
                return ResourceManager.GetString("Error_CantEvalWhenUnhandledExceptionHasOccurred", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Can't evaluate when an unhandled exception has occurred.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1866)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Error_CantEvalWhenUnhandledExceptionHasOccurred;
    ```
- `public static string Error_CouldNotShowDisassembly {
            get {
                return ResourceManager.GetString("Error_CouldNotShowDisassembly", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Could not find the method's code. Make sure that the process is paused and that the method has been jitted..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1875)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Error_CouldNotShowDisassembly;
    ```
- `public static string Error_StartWithoutDebuggingCouldNotStart {
            get {
                return ResourceManager.GetString("Error_StartWithoutDebuggingCouldNotStart", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Could not start '{0}' ERROR: {1}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1885)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Error_StartWithoutDebuggingCouldNotStart;
    ```
- `public static string ExceptionDescription {
            get {
                return ResourceManager.GetString("ExceptionDescription", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Exception description.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1950)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ExceptionDescription;
    ```
- `public static string ExceptionMessage {
            get {
                return ResourceManager.GetString("ExceptionMessage", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Message: {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1959)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ExceptionMessage;
    ```
- `public static string ExceptionMessageIsNull {
            get {
                return ResourceManager.GetString("ExceptionMessageIsNull", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to "<no exception message>".
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1968)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ExceptionMessageIsNull;
    ```
- `public static string ExceptionName {
            get {
                return ResourceManager.GetString("ExceptionName", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Exception: {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1977)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ExceptionName;
    ```
- `public static string ExceptionSettingsCommand {
            get {
                return ResourceManager.GetString("ExceptionSettingsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to E_xception Settings.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2094)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ExceptionSettingsCommand;
    ```
- `public static string Exception_Conditions_And {
            get {
                return ResourceManager.GetString("Exception_Conditions_And", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to And.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1914)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exception_Conditions_And;
    ```
- `public static string Exception_Conditions_ModuleNameEquals {
            get {
                return ResourceManager.GetString("Exception_Conditions_ModuleNameEquals", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Module name equals.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1923)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exception_Conditions_ModuleNameEquals;
    ```
- `public static string Exception_Conditions_ModuleNameNotEquals {
            get {
                return ResourceManager.GetString("Exception_Conditions_ModuleNameNotEquals", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Module name not equals.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1932)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exception_Conditions_ModuleNameNotEquals;
    ```
- `public static string Exception_Error_NameCanNotBeEmpty {
            get {
                return ResourceManager.GetString("Exception_Error_NameCanNotBeEmpty", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Name can't be empty.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1941)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exception_Error_NameCanNotBeEmpty;
    ```
- `public static string ExceptionsCommand {
            get {
                return ResourceManager.GetString("ExceptionsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Exceptions.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2085)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ExceptionsCommand;
    ```
- `public static string Exceptions_Add_ToolTip {
            get {
                return ResourceManager.GetString("Exceptions_Add_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Add an exception to the list.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1986)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_Add_ToolTip;
    ```
- `public static string Exceptions_AllCategories {
            get {
                return ResourceManager.GetString("Exceptions_AllCategories", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to All.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 1995)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_AllCategories;
    ```
- `public static string Exceptions_EditConditions_ToolTip {
            get {
                return ResourceManager.GetString("Exceptions_EditConditions_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Edit conditions.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2004)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_EditConditions_ToolTip;
    ```
- `public static string Exceptions_NoMatch {
            get {
                return ResourceManager.GetString("Exceptions_NoMatch", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to No exception types match your search filter..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2013)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_NoMatch;
    ```
- `public static string Exceptions_Remove_ToolTip {
            get {
                return ResourceManager.GetString("Exceptions_Remove_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Remove an exception from the list.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2022)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_Remove_ToolTip;
    ```
- `public static string Exceptions_ResetSearchSettings_ToolTip {
            get {
                return ResourceManager.GetString("Exceptions_ResetSearchSettings_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Reset all search criteria so that all exceptions are shown.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2031)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_ResetSearchSettings_ToolTip;
    ```
- `public static string Exceptions_RestoreSettings_ToolTip {
            get {
                return ResourceManager.GetString("Exceptions_RestoreSettings_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Restore the list to the default settings.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2040)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_RestoreSettings_ToolTip;
    ```
- `public static string Exceptions_Search {
            get {
                return ResourceManager.GetString("Exceptions_Search", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Search.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2049)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_Search;
    ```
- `public static string Exceptions_Search_ToolTip {
            get {
                return ResourceManager.GetString("Exceptions_Search_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Search for an exception.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2058)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_Search_ToolTip;
    ```
- `public static string Exceptions_ShowOnlyEnabledExceptions_ToolTip {
            get {
                return ResourceManager.GetString("Exceptions_ShowOnlyEnabledExceptions_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show only enabled exceptions.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2067)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_ShowOnlyEnabledExceptions_ToolTip;
    ```
- `public static string Exceptions_ToggleMatchingExceptions_ToolTip {
            get {
                return ResourceManager.GetString("Exceptions_ToggleMatchingExceptions_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Enable or disable all exceptions matching the current search criteria.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2076)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Exceptions_ToggleMatchingExceptions_ToolTip;
    ```
- `public static string ExportCommand {
            get {
                return ResourceManager.GetString("ExportCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to E_xport....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2103)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ExportCommand;
    ```
- `public static string ExportSelectedCommand {
            get {
                return ResourceManager.GetString("ExportSelectedCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Export Selected....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2112)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ExportSelectedCommand;
    ```
- `public static string ExpressionCausesSideEffectsNoEval {
            get {
                return ResourceManager.GetString("ExpressionCausesSideEffectsNoEval", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to This expression causes side effects and will not be evaluated.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2121)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ExpressionCausesSideEffectsNoEval;
    ```
- `public static string FilterExpression_AllVariables {
            get {
                return ResourceManager.GetString("FilterExpression_AllVariables", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Variables that can be used:.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2130)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.FilterExpression_AllVariables;
    ```
- `public static string FilterExpression_Example {
            get {
                return ResourceManager.GetString("FilterExpression_Example", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Example: {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2139)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.FilterExpression_Example;
    ```
- `public static string FindCommand {
            get {
                return ResourceManager.GetString("FindCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Find.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2148)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.FindCommand;
    ```
- `public static string FreezeThreadCommand {
            get {
                return ResourceManager.GetString("FreezeThreadCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Freeze.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2157)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.FreezeThreadCommand;
    ```
- `public static string FuncEvalRequiresAllThreadsToRun {
            get {
                return ResourceManager.GetString("FuncEvalRequiresAllThreadsToRun", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The function evaluation requires all threads to run..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2166)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.FuncEvalRequiresAllThreadsToRun;
    ```
- `public static string FunctionEvaluationDisabled {
            get {
                return ResourceManager.GetString("FunctionEvaluationDisabled", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Implicit function evaluation is turned off by the user.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2175)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.FunctionEvaluationDisabled;
    ```
- `public static string GlyphMargin_CurrentStatementToolTip {
            get {
                return ResourceManager.GetString("GlyphMargin_CurrentStatementToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to This is the next statement that will be executed..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2184)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.GlyphMargin_CurrentStatementToolTip;
    ```
- `public static string GlyphMargin_ReturnStatementToolTip {
            get {
                return ResourceManager.GetString("GlyphMargin_ReturnStatementToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to This is the next statement to execute when this thread returns from the current function..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2193)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.GlyphMargin_ReturnStatementToolTip;
    ```
- `public static string GlyphToolTip_Actions {
            get {
                return ResourceManager.GetString("GlyphToolTip_Actions", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Actions:.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2202)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.GlyphToolTip_Actions;
    ```
- `public static string GlyphToolTip_Conditions {
            get {
                return ResourceManager.GetString("GlyphToolTip_Conditions", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Conditions:.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2211)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.GlyphToolTip_Conditions;
    ```
- `public static string GlyphToolTip_Location {
            get {
                return ResourceManager.GetString("GlyphToolTip_Location", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Location.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2220)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.GlyphToolTip_Location;
    ```
- `public static string GoToDisassemblyCommand2 {
            get {
                return ResourceManager.GetString("GoToDisassemblyCommand2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Go To _Disassembly.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2229)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.GoToDisassemblyCommand2;
    ```
- `public static string GoToModuleCommand {
            get {
                return ResourceManager.GetString("GoToModuleCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Go To Module.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2238)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.GoToModuleCommand;
    ```
- `public static string GoToSourceCodeCommand {
            get {
                return ResourceManager.GetString("GoToSourceCodeCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Go To Source Code.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2247)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.GoToSourceCodeCommand;
    ```
- `public static string HelpToolTip {
            get {
                return ResourceManager.GetString("HelpToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Help.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2256)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.HelpToolTip;
    ```
- `public static string HexDisplayCommand {
            get {
                return ResourceManager.GetString("HexDisplayCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Hexadecimal Display.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2265)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.HexDisplayCommand;
    ```
- `public static string HexEditorGroup_DebuggerMemory {
            get {
                return ResourceManager.GetString("HexEditorGroup_DebuggerMemory", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Memory Window.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2274)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.HexEditorGroup_DebuggerMemory;
    ```
- `public static string InsertBreakpointCommand {
            get {
                return ResourceManager.GetString("InsertBreakpointCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Insert B_reakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2283)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.InsertBreakpointCommand;
    ```
- `public static string InsertTracepointCommand {
            get {
                return ResourceManager.GetString("InsertTracepointCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Insert _Tracepoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2292)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.InsertTracepointCommand;
    ```
- `public static string InternalDebuggerError {
            get {
                return ResourceManager.GetString("InternalDebuggerError", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Internal debugger error.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2301)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.InternalDebuggerError;
    ```
- `public static string LanguageCommand {
            get {
                return ResourceManager.GetString("LanguageCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Language.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2310)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LanguageCommand;
    ```
- `public static string LoadAllModulesCommand {
            get {
                return ResourceManager.GetString("LoadAllModulesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Open All Modules.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2319)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LoadAllModulesCommand;
    ```
- `public static string LoadModulesCommand {
            get {
                return ResourceManager.GetString("LoadModulesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Open Modules.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2328)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LoadModulesCommand;
    ```
- `public static string LoadXModulesCommand {
            get {
                return ResourceManager.GetString("LoadXModulesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Open {0} Modules.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2337)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LoadXModulesCommand;
    ```
- `public static string LocalsAddWatchCommand {
            get {
                return ResourceManager.GetString("LocalsAddWatchCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Add _Watch.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2393)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LocalsAddWatchCommand;
    ```
- `public static string LocalsCollapseChildrenNodesCommand {
            get {
                return ResourceManager.GetString("LocalsCollapseChildrenNodesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Collapse Children.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2402)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LocalsCollapseChildrenNodesCommand;
    ```
- `public static string LocalsCollapseParentNodeCommand {
            get {
                return ResourceManager.GetString("LocalsCollapseParentNodeCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to C_ollapse Parent.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2411)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LocalsCollapseParentNodeCommand;
    ```
- `public static string LocalsCommand {
            get {
                return ResourceManager.GetString("LocalsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Locals.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2420)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LocalsCommand;
    ```
- `public static string LocalsCopyValueCommand {
            get {
                return ResourceManager.GetString("LocalsCopyValueCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Copy Va_lue.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2429)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LocalsCopyValueCommand;
    ```
- `public static string LocalsEditValueCommand {
            get {
                return ResourceManager.GetString("LocalsEditValueCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Edit Value.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2438)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LocalsEditValueCommand;
    ```
- `public static string LocalsExpandChildrenNodesCommand {
            get {
                return ResourceManager.GetString("LocalsExpandChildrenNodesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to E_xpand Children.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2447)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LocalsExpandChildrenNodesCommand;
    ```
- `public static string LocalsSaveCommand {
            get {
                return ResourceManager.GetString("LocalsSaveCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Save....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2466)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LocalsSaveCommand;
    ```
- `public static string LocalsSave_Error_CouldNotSaveDataToFilename {
            get {
                return ResourceManager.GetString("LocalsSave_Error_CouldNotSaveDataToFilename", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Error saving data to '{0}' ERROR: {1}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2457)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.LocalsSave_Error_CouldNotSaveDataToFilename;
    ```
- `public static string Locals_Ask_TooManyItems {
            get {
                return ResourceManager.GetString("Locals_Ask_TooManyItems", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to This item contains more than {0} child items and will be limited to displaying that number of items when expanded. Are you sure you want to expand it?.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2348)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Locals_Ask_TooManyItems;
    ```
- `public static string Locals_Error_CantEvaluateWhenThreadIsAtUnsafePoint {
            get {
                return ResourceManager.GetString("Locals_Error_CantEvaluateWhenThreadIsAtUnsafePoint", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Can't evaluate when the thread is at an unsafe point. Step once or run until a breakpoint hits..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2357)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Locals_Error_CantEvaluateWhenThreadIsAtUnsafePoint;
    ```
- `public static string Locals_Error_EvalDisabledCantCallPropsAndMethods {
            get {
                return ResourceManager.GetString("Locals_Error_EvalDisabledCantCallPropsAndMethods", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to It's currently not possible to call properties and methods.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2366)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Locals_Error_EvalDisabledCantCallPropsAndMethods;
    ```
- `public static string Locals_Error_EvalTimedOutIsDisabled {
            get {
                return ResourceManager.GetString("Locals_Error_EvalTimedOutIsDisabled", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Evaluation timed out and has been disabled until you continue the debugged program..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2375)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Locals_Error_EvalTimedOutIsDisabled;
    ```
- `public static string Locals_Error_EvaluationTimedOut {
            get {
                return ResourceManager.GetString("Locals_Error_EvaluationTimedOut", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Evaluation timed out.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2384)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Locals_Error_EvaluationTimedOut;
    ```
- `public static string MakeObjectIdCommand {
            get {
                return ResourceManager.GetString("MakeObjectIdCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Make Object ID.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2475)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.MakeObjectIdCommand;
    ```
- `public static string MemoryWindowCommand {
            get {
                return ResourceManager.GetString("MemoryWindowCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Memory.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2484)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.MemoryWindowCommand;
    ```
- `public static string ModuleBreakpointsCommand {
            get {
                return ResourceManager.GetString("ModuleBreakpointsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Mod_ule Breakpoints.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2502)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ModuleBreakpointsCommand;
    ```
- `public static string ModuleCopyFilenameCommand {
            get {
                return ResourceManager.GetString("ModuleCopyFilenameCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Copy Filename.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2511)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ModuleCopyFilenameCommand;
    ```
- `public static string ModuleSaveModuleTitle {
            get {
                return ResourceManager.GetString("ModuleSaveModuleTitle", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Save Module.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2583)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ModuleSaveModuleTitle;
    ```
- `public static string ModuleSaveModulesTitle {
            get {
                return ResourceManager.GetString("ModuleSaveModulesTitle", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Save Modules.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2574)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ModuleSaveModulesTitle;
    ```
- `public static string Module_NoAddress {
            get {
                return ResourceManager.GetString("Module_NoAddress", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to <no address>.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2493)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Module_NoAddress;
    ```
- `public static string ModulesCommand {
            get {
                return ResourceManager.GetString("ModulesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to M_odules.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2592)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ModulesCommand;
    ```
- `public static string Modules_AllProcesses {
            get {
                return ResourceManager.GetString("Modules_AllProcesses", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to All.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2520)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Modules_AllProcesses;
    ```
- `public static string Modules_NoMatch {
            get {
                return ResourceManager.GetString("Modules_NoMatch", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to No modules match your search filter..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2529)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Modules_NoMatch;
    ```
- `public static string Modules_Process {
            get {
                return ResourceManager.GetString("Modules_Process", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2538)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Modules_Process;
    ```
- `public static string Modules_ResetSearchSettings_ToolTip {
            get {
                return ResourceManager.GetString("Modules_ResetSearchSettings_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Reset all search criteria so that all modules are shown.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2547)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Modules_ResetSearchSettings_ToolTip;
    ```
- `public static string Modules_Search {
            get {
                return ResourceManager.GetString("Modules_Search", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Search.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2556)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Modules_Search;
    ```
- `public static string Modules_Search_ToolTip {
            get {
                return ResourceManager.GetString("Modules_Search_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Search for a module.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2565)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Modules_Search_ToolTip;
    ```
- `public static string OpenContainingFolderCommand {
            get {
                return ResourceManager.GetString("OpenContainingFolderCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Open Containing Folder.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2601)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.OpenContainingFolderCommand;
    ```
- `public static string OpenModuleFromMemoryCommand {
            get {
                return ResourceManager.GetString("OpenModuleFromMemoryCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Open Module from Memory.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2610)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.OpenModuleFromMemoryCommand;
    ```
- `public static string Options {
            get {
                return ResourceManager.GetString("Options", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Options....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2619)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Options;
    ```
- `public static string OutputCommand {
            get {
                return ResourceManager.GetString("OutputCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Output.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2628)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.OutputCommand;
    ```
- `public static string PasteCommand {
            get {
                return ResourceManager.GetString("PasteCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Paste.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2637)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.PasteCommand;
    ```
- `public static string Plugin_ShortDescription {
            get {
                return ResourceManager.GetString("Plugin_ShortDescription", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debugger.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2646)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Plugin_ShortDescription;
    ```
- `public static string ProcessCommand {
            get {
                return ResourceManager.GetString("ProcessCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2673)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ProcessCommand;
    ```
- `public static string ProcessIsNotPaused {
            get {
                return ResourceManager.GetString("ProcessIsNotPaused", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Process is not paused.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2763)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ProcessIsNotPaused;
    ```
- `public static string Process_Paused {
            get {
                return ResourceManager.GetString("Process_Paused", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Break.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2655)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Process_Paused;
    ```
- `public static string Process_Running {
            get {
                return ResourceManager.GetString("Process_Running", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Running.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2664)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Process_Running;
    ```
- `public static string ProcessesCommand {
            get {
                return ResourceManager.GetString("ProcessesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Processes.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2754)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ProcessesCommand;
    ```
- `public static string Processes_AttachToProcessToolTip {
            get {
                return ResourceManager.GetString("Processes_AttachToProcessToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Attach to Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2682)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Processes_AttachToProcessToolTip;
    ```
- `public static string Processes_BreakProcessToolTip {
            get {
                return ResourceManager.GetString("Processes_BreakProcessToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Break Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2691)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Processes_BreakProcessToolTip;
    ```
- `public static string Processes_ContinueProcessToolTip {
            get {
                return ResourceManager.GetString("Processes_ContinueProcessToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Continue Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2700)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Processes_ContinueProcessToolTip;
    ```
- `public static string Processes_DetachToolTip {
            get {
                return ResourceManager.GetString("Processes_DetachToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Detach Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2709)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Processes_DetachToolTip;
    ```
- `public static string Processes_StepIntoProcessToolTip {
            get {
                return ResourceManager.GetString("Processes_StepIntoProcessToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step Into.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2718)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Processes_StepIntoProcessToolTip;
    ```
- `public static string Processes_StepOutProcessToolTip {
            get {
                return ResourceManager.GetString("Processes_StepOutProcessToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step Out.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2727)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Processes_StepOutProcessToolTip;
    ```
- `public static string Processes_StepOverProcessToolTip {
            get {
                return ResourceManager.GetString("Processes_StepOverProcessToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step Over.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2736)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Processes_StepOverProcessToolTip;
    ```
- `public static string Processes_TerminateToolTip {
            get {
                return ResourceManager.GetString("Processes_TerminateToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Terminate Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2745)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Processes_TerminateToolTip;
    ```
- `public static string Refresh {
            get {
                return ResourceManager.GetString("Refresh", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Refresh.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2772)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Refresh;
    ```
- `public static string RefreshExpressionButtonToolTip {
            get {
                return ResourceManager.GetString("RefreshExpressionButtonToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Click this button to evaluate now..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2781)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.RefreshExpressionButtonToolTip;
    ```
- `public static string RemoveAllBreakpointsCommand {
            get {
                return ResourceManager.GetString("RemoveAllBreakpointsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Remove All Breakpoints.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2790)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.RemoveAllBreakpointsCommand;
    ```
- `public static string RemoveBreakpointCommand {
            get {
                return ResourceManager.GetString("RemoveBreakpointCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Remove Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2799)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.RemoveBreakpointCommand;
    ```
- `public static string RemoveExceptionCommand {
            get {
                return ResourceManager.GetString("RemoveExceptionCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Remove.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2808)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.RemoveExceptionCommand;
    ```
- `public static string RenameThreadCommand {
            get {
                return ResourceManager.GetString("RenameThreadCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Rename.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2817)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.RenameThreadCommand;
    ```
- `public static string ResetBreakpointHitCountCommand {
            get {
                return ResourceManager.GetString("ResetBreakpointHitCountCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Reset Hit Count.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2826)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ResetBreakpointHitCountCommand;
    ```
- `public static string RestartCommand {
            get {
                return ResourceManager.GetString("RestartCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Restart.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2835)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.RestartCommand;
    ```
- `public static string RestoreDefaultExceptionSettingsCommand {
            get {
                return ResourceManager.GetString("RestoreDefaultExceptionSettingsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Restore Defaults.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2844)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.RestoreDefaultExceptionSettingsCommand;
    ```
- `public static string RunToCursorCommand {
            get {
                return ResourceManager.GetString("RunToCursorCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ru_n To Cursor.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2862)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.RunToCursorCommand;
    ```
- `public static string RuntimeIsUnableToEvaluateExpression {
            get {
                return ResourceManager.GetString("RuntimeIsUnableToEvaluateExpression", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The runtime is unable to evaluate this expression..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2853)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.RuntimeIsUnableToEvaluateExpression;
    ```
- `public static string SaveModuleCommand {
            get {
                return ResourceManager.GetString("SaveModuleCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Save Module....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2871)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.SaveModuleCommand;
    ```
- `public static string SaveModulesCommand {
            get {
                return ResourceManager.GetString("SaveModulesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Save {0} Modules....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2880)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.SaveModulesCommand;
    ```
- `public static string SearchHelp_ToolTip {
            get {
                return ResourceManager.GetString("SearchHelp_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Help.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2889)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.SearchHelp_ToolTip;
    ```
- `public static string SelectAllCommand {
            get {
                return ResourceManager.GetString("SelectAllCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Select _All.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2898)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.SelectAllCommand;
    ```
- `public static string SetNextStatementCommand {
            get {
                return ResourceManager.GetString("SetNextStatementCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Set Ne_xt Statement.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2907)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.SetNextStatementCommand;
    ```
- `public static string SettingsCommand {
            get {
                return ResourceManager.GetString("SettingsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Settings.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2916)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.SettingsCommand;
    ```
- `public static string SettingsCommand2 {
            get {
                return ResourceManager.GetString("SettingsCommand2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Settings....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2925)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.SettingsCommand2;
    ```
- `public static string ShortCutAltAsterisk {
            get {
                return ResourceManager.GetString("ShortCutAltAsterisk", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Alt+Num *.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2934)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutAltAsterisk;
    ```
- `public static string ShortCutKeyAlt4 {
            get {
                return ResourceManager.GetString("ShortCutKeyAlt4", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Alt+4.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2943)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyAlt4;
    ```
- `public static string ShortCutKeyAlt6 {
            get {
                return ResourceManager.GetString("ShortCutKeyAlt6", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Alt+6.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2952)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyAlt6;
    ```
- `public static string ShortCutKeyAlt8 {
            get {
                return ResourceManager.GetString("ShortCutKeyAlt8", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Alt+8.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2961)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyAlt8;
    ```
- `public static string ShortCutKeyAltEnter {
            get {
                return ResourceManager.GetString("ShortCutKeyAltEnter", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Alt+Enter.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2970)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyAltEnter;
    ```
- `public static string ShortCutKeyCtrlA {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlA", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+A.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2988)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlA;
    ```
- `public static string ShortCutKeyCtrlAltB {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltB", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+B.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2997)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltB;
    ```
- `public static string ShortCutKeyCtrlAltBreak {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltBreak", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+Break.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3006)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltBreak;
    ```
- `public static string ShortCutKeyCtrlAltC {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltC", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+C.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3015)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltC;
    ```
- `public static string ShortCutKeyCtrlAltE {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltE", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+E.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3024)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltE;
    ```
- `public static string ShortCutKeyCtrlAltF10 {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltF10", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+F10.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3033)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltF10;
    ```
- `public static string ShortCutKeyCtrlAltF11 {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltF11", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+F11.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3042)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltF11;
    ```
- `public static string ShortCutKeyCtrlAltH {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltH", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+H.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3051)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltH;
    ```
- `public static string ShortCutKeyCtrlAltP {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltP", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+P.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3060)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltP;
    ```
- `public static string ShortCutKeyCtrlAltU {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltU", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+U.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3069)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltU;
    ```
- `public static string ShortCutKeyCtrlAltV_A {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltV_A", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+V, A.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3078)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltV_A;
    ```
- `public static string ShortCutKeyCtrlAltW_DIGIT {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltW_DIGIT", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+W, {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3087)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltW_DIGIT;
    ```
- `public static string ShortCutKeyCtrlAltZ {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlAltZ", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Alt+Z.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3096)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlAltZ;
    ```
- `public static string ShortCutKeyCtrlC {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlC", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+C.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3105)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlC;
    ```
- `public static string ShortCutKeyCtrlF {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlF", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+F.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3114)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlF;
    ```
- `public static string ShortCutKeyCtrlF10 {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlF10", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+F10.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3123)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlF10;
    ```
- `public static string ShortCutKeyCtrlF5 {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlF5", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+F5.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3132)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlF5;
    ```
- `public static string ShortCutKeyCtrlF9 {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlF9", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+F9.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3141)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlF9;
    ```
- `public static string ShortCutKeyCtrlShiftAltF11 {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlShiftAltF11", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Shift+Alt+F11.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3159)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlShiftAltF11;
    ```
- `public static string ShortCutKeyCtrlShiftC {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlShiftC", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Shift+C.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3168)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlShiftC;
    ```
- `public static string ShortCutKeyCtrlShiftF10 {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlShiftF10", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Shift+F10.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3177)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlShiftF10;
    ```
- `public static string ShortCutKeyCtrlShiftF5 {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlShiftF5", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Shift+F5.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3186)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlShiftF5;
    ```
- `public static string ShortCutKeyCtrlShiftF9 {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlShiftF9", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Shift+F9.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3195)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlShiftF9;
    ```
- `public static string ShortCutKeyCtrlShift_DIGIT {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlShift_DIGIT", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+Shift+{0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3150)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlShift_DIGIT;
    ```
- `public static string ShortCutKeyCtrlV {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrlV", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+V.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3204)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrlV;
    ```
- `public static string ShortCutKeyCtrl_DIGIT {
            get {
                return ResourceManager.GetString("ShortCutKeyCtrl_DIGIT", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ctrl+{0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 2979)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyCtrl_DIGIT;
    ```
- `public static string ShortCutKeyDelete {
            get {
                return ResourceManager.GetString("ShortCutKeyDelete", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Del.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3213)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyDelete;
    ```
- `public static string ShortCutKeyEnter {
            get {
                return ResourceManager.GetString("ShortCutKeyEnter", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Enter.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3222)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyEnter;
    ```
- `public static string ShortCutKeyF10 {
            get {
                return ResourceManager.GetString("ShortCutKeyF10", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to F10.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3231)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyF10;
    ```
- `public static string ShortCutKeyF11 {
            get {
                return ResourceManager.GetString("ShortCutKeyF11", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to F11.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3240)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyF11;
    ```
- `public static string ShortCutKeyF2 {
            get {
                return ResourceManager.GetString("ShortCutKeyF2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to F2.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3249)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyF2;
    ```
- `public static string ShortCutKeyF5 {
            get {
                return ResourceManager.GetString("ShortCutKeyF5", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to F5.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3258)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyF5;
    ```
- `public static string ShortCutKeyF9 {
            get {
                return ResourceManager.GetString("ShortCutKeyF9", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to F9.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3267)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyF9;
    ```
- `public static string ShortCutKeyInsert {
            get {
                return ResourceManager.GetString("ShortCutKeyInsert", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ins.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3276)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyInsert;
    ```
- `public static string ShortCutKeyShiftF11 {
            get {
                return ResourceManager.GetString("ShortCutKeyShiftF11", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Shift+F11.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3285)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyShiftF11;
    ```
- `public static string ShortCutKeyShiftF5 {
            get {
                return ResourceManager.GetString("ShortCutKeyShiftF5", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Shift+F5.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3294)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShortCutKeyShiftF5;
    ```
- `public static string ShowDeclaringTypesCommand {
            get {
                return ResourceManager.GetString("ShowDeclaringTypesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show Declaring Types.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3303)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowDeclaringTypesCommand;
    ```
- `public static string ShowExceptionMessages {
            get {
                return ResourceManager.GetString("ShowExceptionMessages", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Exception Messages.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3312)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowExceptionMessages;
    ```
- `public static string ShowInMemoryWindowCommand {
            get {
                return ResourceManager.GetString("ShowInMemoryWindowCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show in Memory Window.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3321)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowInMemoryWindowCommand;
    ```
- `public static string ShowInstructionPointerCommand {
            get {
                return ResourceManager.GetString("ShowInstructionPointerCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show IP.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3330)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowInstructionPointerCommand;
    ```
- `public static string ShowIntrinsicTypeKeywordsCommand {
            get {
                return ResourceManager.GetString("ShowIntrinsicTypeKeywordsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show Intrinsic Type Keywords.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3339)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowIntrinsicTypeKeywordsCommand;
    ```
- `public static string ShowMDAMessages {
            get {
                return ResourceManager.GetString("ShowMDAMessages", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to MDA Messages.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3348)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowMDAMessages;
    ```
- `public static string ShowModuleLoadMessages {
            get {
                return ResourceManager.GetString("ShowModuleLoadMessages", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Module _Load Messages.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3357)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowModuleLoadMessages;
    ```
- `public static string ShowModuleNamesCommand {
            get {
                return ResourceManager.GetString("ShowModuleNamesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show _Module Names.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3366)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowModuleNamesCommand;
    ```
- `public static string ShowModuleUnloadMessages {
            get {
                return ResourceManager.GetString("ShowModuleUnloadMessages", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Module _Unload Messages.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3375)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowModuleUnloadMessages;
    ```
- `public static string ShowNamespacesCommand {
            get {
                return ResourceManager.GetString("ShowNamespacesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show Namespaces.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3384)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowNamespacesCommand;
    ```
- `public static string ShowNextStatementCommand {
            get {
                return ResourceManager.GetString("ShowNextStatementCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to S_how Next Statement.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3393)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowNextStatementCommand;
    ```
- `public static string ShowOnlyPublicMembersCommand {
            get {
                return ResourceManager.GetString("ShowOnlyPublicMembersCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Public Members.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3402)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowOnlyPublicMembersCommand;
    ```
- `public static string ShowParameterNamesCommand {
            get {
                return ResourceManager.GetString("ShowParameterNamesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show _Parameter Names.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3411)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowParameterNamesCommand;
    ```
- `public static string ShowParameterTypesCommand {
            get {
                return ResourceManager.GetString("ShowParameterTypesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show Parameter _Types.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3420)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowParameterTypesCommand;
    ```
- `public static string ShowParameterTypesCommand2 {
            get {
                return ResourceManager.GetString("ShowParameterTypesCommand2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show Parameter Types.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3429)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowParameterTypesCommand2;
    ```
- `public static string ShowParameterValuesCommand {
            get {
                return ResourceManager.GetString("ShowParameterValuesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show Parameter _Values.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3438)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowParameterValuesCommand;
    ```
- `public static string ShowProcessExitMessages {
            get {
                return ResourceManager.GetString("ShowProcessExitMessages", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Process Exit Messages.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3447)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowProcessExitMessages;
    ```
- `public static string ShowProgramOutputMessages {
            get {
                return ResourceManager.GetString("ShowProgramOutputMessages", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Program _Output.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3456)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowProgramOutputMessages;
    ```
- `public static string ShowReturnTypesCommand {
            get {
                return ResourceManager.GetString("ShowReturnTypesCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show Return Types.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3465)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowReturnTypesCommand;
    ```
- `public static string ShowStepFilteringMessages {
            get {
                return ResourceManager.GetString("ShowStepFilteringMessages", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Step Filtering Messages.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3474)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowStepFilteringMessages;
    ```
- `public static string ShowThreadExitMessages {
            get {
                return ResourceManager.GetString("ShowThreadExitMessages", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Thread Exit Messages.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3483)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowThreadExitMessages;
    ```
- `public static string ShowTokensCommand {
            get {
                return ResourceManager.GetString("ShowTokensCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show Tokens.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3492)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ShowTokensCommand;
    ```
- `public static string StartDebugging2 {
            get {
                return ResourceManager.GetString("StartDebugging2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Start Debugging....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3501)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StartDebugging2;
    ```
- `public static string StartDebuggingCommand {
            get {
                return ResourceManager.GetString("StartDebuggingCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Start Debugging.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3510)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StartDebuggingCommand;
    ```
- `public static string StartWithoutDebuggingCommand {
            get {
                return ResourceManager.GetString("StartWithoutDebuggingCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Start Wit_hout Debugging.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3519)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StartWithoutDebuggingCommand;
    ```
- `public static string StatusBar_BreakpointHit {
            get {
                return ResourceManager.GetString("StatusBar_BreakpointHit", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3528)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StatusBar_BreakpointHit;
    ```
- `public static string StatusBar_Ready {
            get {
                return ResourceManager.GetString("StatusBar_Ready", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ready.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3537)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StatusBar_Ready;
    ```
- `public static string StatusBar_Running {
            get {
                return ResourceManager.GetString("StatusBar_Running", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Running....
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3546)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StatusBar_Running;
    ```
- `public static string StepIntoCommand {
            get {
                return ResourceManager.GetString("StepIntoCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step _Into.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3555)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StepIntoCommand;
    ```
- `public static string StepIntoCurrentProcessCommand {
            get {
                return ResourceManager.GetString("StepIntoCurrentProcessCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step Into (Current Process).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3564)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StepIntoCurrentProcessCommand;
    ```
- `public static string StepOutCommand {
            get {
                return ResourceManager.GetString("StepOutCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step Ou_t.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3573)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StepOutCommand;
    ```
- `public static string StepOutCurrentProcessCommand {
            get {
                return ResourceManager.GetString("StepOutCurrentProcessCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step Out (Current Process).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3582)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StepOutCurrentProcessCommand;
    ```
- `public static string StepOverCommand {
            get {
                return ResourceManager.GetString("StepOverCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step _Over.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3591)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StepOverCommand;
    ```
- `public static string StepOverCurrentProcessCommand {
            get {
                return ResourceManager.GetString("StepOverCurrentProcessCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step Over (Current Process).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3600)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StepOverCurrentProcessCommand;
    ```
- `public static string StepsOnlyTheCurrentProcess {
            get {
                return ResourceManager.GetString("StepsOnlyTheCurrentProcess", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Steps only the current process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3609)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StepsOnlyTheCurrentProcess;
    ```
- `public static string StopDebuggingCommand {
            get {
                return ResourceManager.GetString("StopDebuggingCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Stop D_ebugging.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3618)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.StopDebuggingCommand;
    ```
- `public static string SwitchToFrameCommand {
            get {
                return ResourceManager.GetString("SwitchToFrameCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Switch To Frame.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3627)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.SwitchToFrameCommand;
    ```
- `public static string SwitchToThreadCommand {
            get {
                return ResourceManager.GetString("SwitchToThreadCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Switch To Thread.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3636)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.SwitchToThreadCommand;
    ```
- `public static string TerminateAllCommand {
            get {
                return ResourceManager.GetString("TerminateAllCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ter_minate All.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3645)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.TerminateAllCommand;
    ```
- `public static string TerminateProcessCommand {
            get {
                return ResourceManager.GetString("TerminateProcessCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Ter_minate Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3654)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.TerminateProcessCommand;
    ```
- `public static string ThawThreadCommand {
            get {
                return ResourceManager.GetString("ThawThreadCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Thaw.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3663)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ThawThreadCommand;
    ```
- `public static string ThreadType_Main {
            get {
                return ResourceManager.GetString("ThreadType_Main", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Main Thread.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3816)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ThreadType_Main;
    ```
- `public static string ThreadType_Terminated {
            get {
                return ResourceManager.GetString("ThreadType_Terminated", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Terminated Thread.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3825)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ThreadType_Terminated;
    ```
- `public static string ThreadType_ThreadPool {
            get {
                return ResourceManager.GetString("ThreadType_ThreadPool", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Thread Pool.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3834)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ThreadType_ThreadPool;
    ```
- `public static string ThreadType_Unknown {
            get {
                return ResourceManager.GetString("ThreadType_Unknown", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Unknown Thread.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3843)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ThreadType_Unknown;
    ```
- `public static string ThreadType_Worker {
            get {
                return ResourceManager.GetString("ThreadType_Worker", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Worker Thread.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3852)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ThreadType_Worker;
    ```
- `public static string Thread_LocationNotAvailable {
            get {
                return ResourceManager.GetString("Thread_LocationNotAvailable", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to <not available>.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3672)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Thread_LocationNotAvailable;
    ```
- `public static string Thread_NoName {
            get {
                return ResourceManager.GetString("Thread_NoName", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to <No Name>.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3681)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Thread_NoName;
    ```
- `public static string Thread_Priority_AboveNormal {
            get {
                return ResourceManager.GetString("Thread_Priority_AboveNormal", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Above Normal.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3690)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Thread_Priority_AboveNormal;
    ```
- `public static string Thread_Priority_BelowNormal {
            get {
                return ResourceManager.GetString("Thread_Priority_BelowNormal", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Below Normal.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3699)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Thread_Priority_BelowNormal;
    ```
- `public static string Thread_Priority_Highest {
            get {
                return ResourceManager.GetString("Thread_Priority_Highest", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Highest.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3708)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Thread_Priority_Highest;
    ```
- `public static string Thread_Priority_Lowest {
            get {
                return ResourceManager.GetString("Thread_Priority_Lowest", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Lowest.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3717)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Thread_Priority_Lowest;
    ```
- `public static string Thread_Priority_Normal {
            get {
                return ResourceManager.GetString("Thread_Priority_Normal", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Normal.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3726)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Thread_Priority_Normal;
    ```
- `public static string ThreadsCommand {
            get {
                return ResourceManager.GetString("ThreadsCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to T_hreads.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3807)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ThreadsCommand;
    ```
- `public static string Threads_AllProcesses {
            get {
                return ResourceManager.GetString("Threads_AllProcesses", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to All.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3735)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Threads_AllProcesses;
    ```
- `public static string Threads_FreezeThreads_ToolTip {
            get {
                return ResourceManager.GetString("Threads_FreezeThreads_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Freeze Threads.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3744)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Threads_FreezeThreads_ToolTip;
    ```
- `public static string Threads_NoMatch {
            get {
                return ResourceManager.GetString("Threads_NoMatch", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to No threads match your search filter..
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3753)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Threads_NoMatch;
    ```
- `public static string Threads_Process {
            get {
                return ResourceManager.GetString("Threads_Process", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Process.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3762)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Threads_Process;
    ```
- `public static string Threads_ResetSearchSettings_ToolTip {
            get {
                return ResourceManager.GetString("Threads_ResetSearchSettings_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Reset all search criteria so that all threads are shown.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3771)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Threads_ResetSearchSettings_ToolTip;
    ```
- `public static string Threads_Search {
            get {
                return ResourceManager.GetString("Threads_Search", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Search.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3780)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Threads_Search;
    ```
- `public static string Threads_Search_ToolTip {
            get {
                return ResourceManager.GetString("Threads_Search_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Search for a thread.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3789)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Threads_Search_ToolTip;
    ```
- `public static string Threads_ThawThreads_ToolTip {
            get {
                return ResourceManager.GetString("Threads_ThawThreads_ToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Thaw Threads.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3798)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Threads_ThawThreads_ToolTip;
    ```
- `public static string ToggleBreakpointCommand {
            get {
                return ResourceManager.GetString("ToggleBreakpointCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to To_ggle Breakpoint.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3861)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToggleBreakpointCommand;
    ```
- `public static string ToolBarBreakAllToolTip {
            get {
                return ResourceManager.GetString("ToolBarBreakAllToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Break All.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3870)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarBreakAllToolTip;
    ```
- `public static string ToolBarContinueDebuggingButton {
            get {
                return ResourceManager.GetString("ToolBarContinueDebuggingButton", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Continue.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3879)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarContinueDebuggingButton;
    ```
- `public static string ToolBarContinueDebuggingToolTip {
            get {
                return ResourceManager.GetString("ToolBarContinueDebuggingToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Continue.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3888)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarContinueDebuggingToolTip;
    ```
- `public static string ToolBarDebugAssemblyToolTip {
            get {
                return ResourceManager.GetString("ToolBarDebugAssemblyToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Debug a Program.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3897)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarDebugAssemblyToolTip;
    ```
- `public static string ToolBarRestartToolTip {
            get {
                return ResourceManager.GetString("ToolBarRestartToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Restart.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3906)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarRestartToolTip;
    ```
- `public static string ToolBarShowNextStatementToolTip {
            get {
                return ResourceManager.GetString("ToolBarShowNextStatementToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Show Next Statement.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3915)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarShowNextStatementToolTip;
    ```
- `public static string ToolBarStartDebuggingButton {
            get {
                return ResourceManager.GetString("ToolBarStartDebuggingButton", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Start.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3924)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarStartDebuggingButton;
    ```
- `public static string ToolBarStepIntoToolTip {
            get {
                return ResourceManager.GetString("ToolBarStepIntoToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step Into.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3933)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarStepIntoToolTip;
    ```
- `public static string ToolBarStepOutToolTip {
            get {
                return ResourceManager.GetString("ToolBarStepOutToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step Out.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3942)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarStepOutToolTip;
    ```
- `public static string ToolBarStepOverToolTip {
            get {
                return ResourceManager.GetString("ToolBarStepOverToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Step Over.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3951)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarStepOverToolTip;
    ```
- `public static string ToolBarStopDebuggingToolTip {
            get {
                return ResourceManager.GetString("ToolBarStopDebuggingToolTip", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Stop Debugging.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3960)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.ToolBarStopDebuggingToolTip;
    ```
- `public static string TracepointMessage_EscapeSequences {
            get {
                return ResourceManager.GetString("TracepointMessage_EscapeSequences", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Escape sequences: {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3969)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.TracepointMessage_EscapeSequences;
    ```
- `public static string TracepointMessage_EvaluateMessage {
            get {
                return ResourceManager.GetString("TracepointMessage_EvaluateMessage", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Use {xxx} to evaluate expression xxx.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3978)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.TracepointMessage_EvaluateMessage;
    ```
- `public static string TracepointMessage_Example {
            get {
                return ResourceManager.GetString("TracepointMessage_Example", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Example: {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3987)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.TracepointMessage_Example;
    ```
- `public static string TracepointMessage_ValidKeywords {
            get {
                return ResourceManager.GetString("TracepointMessage_ValidKeywords", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to The following keywords can be used:.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 3996)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.TracepointMessage_ValidKeywords;
    ```
- `public static string UnhandledExceptionMessage_ProcessName_ProcessId {
            get {
                return ResourceManager.GetString("UnhandledExceptionMessage_ProcessName_ProcessId", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to An unhandled exception occurred in {0} ({1}).
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4005)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.UnhandledExceptionMessage_ProcessName_ProcessId;
    ```
- `public static string UnknownValue {
            get {
                return ResourceManager.GetString("UnknownValue", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to <Unknown>.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4014)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.UnknownValue;
    ```
- `public static string UnwindToThisFrameCommand {
            get {
                return ResourceManager.GetString("UnwindToThisFrameCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Unwind To This Frame.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4023)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.UnwindToThisFrameCommand;
    ```
- `public static string WatchCommand {
            get {
                return ResourceManager.GetString("WatchCommand", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to _Watch.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4032)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.WatchCommand;
    ```
- `public static string Window_Autos {
            get {
                return ResourceManager.GetString("Window_Autos", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Autos.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4041)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Autos;
    ```
- `public static string Window_Breakpoints {
            get {
                return ResourceManager.GetString("Window_Breakpoints", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Breakpoints.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4050)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Breakpoints;
    ```
- `public static string Window_CallStack {
            get {
                return ResourceManager.GetString("Window_CallStack", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Call Stack.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4059)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_CallStack;
    ```
- `public static string Window_ExceptionSettings {
            get {
                return ResourceManager.GetString("Window_ExceptionSettings", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Exception Settings.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4068)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_ExceptionSettings;
    ```
- `public static string Window_Locals {
            get {
                return ResourceManager.GetString("Window_Locals", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Locals.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4077)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Locals;
    ```
- `public static string Window_Memory_10_MenuItem {
            get {
                return ResourceManager.GetString("Window_Memory_10_MenuItem", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Memory 1_0.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4086)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Memory_10_MenuItem;
    ```
- `public static string Window_Memory_N {
            get {
                return ResourceManager.GetString("Window_Memory_N", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Memory {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4095)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Memory_N;
    ```
- `public static string Window_Memory_N_MenuItem {
            get {
                return ResourceManager.GetString("Window_Memory_N_MenuItem", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Memory _{0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4104)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Memory_N_MenuItem;
    ```
- `public static string Window_Memory_N_MenuItem2 {
            get {
                return ResourceManager.GetString("Window_Memory_N_MenuItem2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Memory {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4113)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Memory_N_MenuItem2;
    ```
- `public static string Window_ModuleBreakpoints {
            get {
                return ResourceManager.GetString("Window_ModuleBreakpoints", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Module Breakpoints.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4122)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_ModuleBreakpoints;
    ```
- `public static string Window_Modules {
            get {
                return ResourceManager.GetString("Window_Modules", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Modules.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4131)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Modules;
    ```
- `public static string Window_Processes {
            get {
                return ResourceManager.GetString("Window_Processes", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Processes.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4140)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Processes;
    ```
- `public static string Window_Threads {
            get {
                return ResourceManager.GetString("Window_Threads", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Threads.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4149)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Threads;
    ```
- `public static string Window_Watch_10_MenuItem {
            get {
                return ResourceManager.GetString("Window_Watch_10_MenuItem", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Watch 1_0.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4158)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Watch_10_MenuItem;
    ```
- `public static string Window_Watch_N {
            get {
                return ResourceManager.GetString("Window_Watch_N", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Watch {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4167)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Watch_N;
    ```
- `public static string Window_Watch_N_MenuItem {
            get {
                return ResourceManager.GetString("Window_Watch_N_MenuItem", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Watch _{0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4176)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Watch_N_MenuItem;
    ```
- `public static string Window_Watch_N_MenuItem2 {
            get {
                return ResourceManager.GetString("Window_Watch_N_MenuItem2", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Watch {0}.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4185)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.Window_Watch_N_MenuItem2;
    ```
- `public static string YesNo_No {
            get {
                return ResourceManager.GetString("YesNo_No", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to No.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4194)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.YesNo_No;
    ```
- `public static string YesNo_Yes {
            get {
                return ResourceManager.GetString("YesNo_Yes", resourceCulture);
            }
        }`
  - Summary: Looks up a localized string similar to Yes.
  - Defined in: `Extensions/dnSpy.Debugger/dnSpy.Debugger/Properties/dnSpy.Debugger.Resources.Designer.cs` (line 4203)
  - Example:
    ```csharp
    // Read the property
    var value = dnSpy.Debugger.Properties.dnSpy_Debugger_Resources.YesNo_Yes;
    ```

