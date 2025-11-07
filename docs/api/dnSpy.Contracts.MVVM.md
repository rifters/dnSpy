# Namespace `dnSpy.Contracts.MVVM`

## Class `AutomationPeerMemoryLeakWorkaround`

Workaround for an memory leak. Use it on all long-lived s (eg. , , etc)

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.AutomationPeerMemoryLeakWorkaround and call its members.
var instance = new dnSpy.Contracts.MVVM.AutomationPeerMemoryLeakWorkaround(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/AutomationPeerMemoryLeakWorkaround.cs` (line 32)

### Methods

- `public static bool GetInitialize(ItemsControl element)`
  - Parameters:
    - `ItemsControl element`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/AutomationPeerMemoryLeakWorkaround.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.AutomationPeerMemoryLeakWorkaround.GetInitialize(element: /* ItemsControl */);
    ```
- `public static int GetEmptyCount(ItemsControl element)`
  - Parameters:
    - `ItemsControl element`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/AutomationPeerMemoryLeakWorkaround.cs` (line 44)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.AutomationPeerMemoryLeakWorkaround.GetEmptyCount(element: /* ItemsControl */);
    ```
- `public static void ClearAll(ItemsControl itemsControl)`
  - Parameters:
    - `ItemsControl itemsControl`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/AutomationPeerMemoryLeakWorkaround.cs` (line 58)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.AutomationPeerMemoryLeakWorkaround.ClearAll(itemsControl: /* ItemsControl */);
    ```
- `public static void SetEmptyCount(ItemsControl element, int value)`
  - Parameters:
    - `ItemsControl element`: Description not provided.
    - `int value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/AutomationPeerMemoryLeakWorkaround.cs` (line 43)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.AutomationPeerMemoryLeakWorkaround.SetEmptyCount(element: /* ItemsControl */, value: /* int */);
    ```
- `public static void SetInitialize(ItemsControl element, bool value)`
  - Parameters:
    - `ItemsControl element`: Description not provided.
    - `bool value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/AutomationPeerMemoryLeakWorkaround.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.AutomationPeerMemoryLeakWorkaround.SetInitialize(element: /* ItemsControl */, value: /* bool */);
    ```

### Fields

- `public static readonly DependencyProperty EmptyCountProperty = DependencyProperty.RegisterAttached(
			"EmptyCount", typeof(int), typeof(AutomationPeerMemoryLeakWorkaround), new UIPropertyMetadata(0))`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/AutomationPeerMemoryLeakWorkaround.cs` (line 40)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.AutomationPeerMemoryLeakWorkaround.EmptyCountProperty;
    ```
- `public static readonly DependencyProperty InitializeProperty = DependencyProperty.RegisterAttached(
			"Initialize", typeof(bool), typeof(AutomationPeerMemoryLeakWorkaround), new UIPropertyMetadata(false, InitializePropertyChangedCallback))`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/AutomationPeerMemoryLeakWorkaround.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.AutomationPeerMemoryLeakWorkaround.InitializeProperty;
    ```

## Class `BooleanListDataFieldVM`

List of s

**Inherits/Implements:** `DataFieldVM<IList<bool>>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.BooleanListDataFieldVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1265)

### Constructors

- `public BooleanListDataFieldVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1270)
- `public BooleanListDataFieldVM(IList<bool> value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `IList<bool> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1279)

### Methods

- `protected override string ConvertToValue(out IList<bool> value)`
  - Parameters:
    - `out IList<bool> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1286)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<bool> */);
    ```
- `protected override string OnNewValue(IList<bool> value)`
  - Parameters:
    - `IList<bool> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1283)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<bool> */);
    ```

## Class `BooleanVM`

**Inherits/Implements:** `DataFieldVM<bool>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.BooleanVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 732)

### Constructors

- `public BooleanVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 737)
- `public BooleanVM(bool value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `bool value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 746)

### Methods

- `protected override string ConvertToValue(out bool value)`
  - Parameters:
    - `out bool value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 753)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* bool */);
    ```
- `protected override string OnNewValue(bool value)`
  - Parameters:
    - `bool value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 750)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* bool */);
    ```

## Class `ByteListDataFieldVM`

List of s

**Inherits/Implements:** `NumberDataFieldVM<IList<byte>`, `byte>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.ByteListDataFieldVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1325)

### Constructors

- `public ByteListDataFieldVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1331)
- `public ByteListDataFieldVM(IList<byte> value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `IList<byte> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1341)

### Methods

- `protected override string ConvertToValue(out IList<byte> value)`
  - Parameters:
    - `out IList<byte> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1348)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<byte> */);
    ```
- `protected override string OnNewValue(IList<byte> value)`
  - Parameters:
    - `IList<byte> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1345)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<byte> */);
    ```

## Class `ByteVM`

**Inherits/Implements:** `NumberDataFieldVM<byte`, `byte>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.ByteVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 792)

### Constructors

- `public ByteVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 798)
- `public ByteVM(byte value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `byte value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 808)

### Methods

- `protected override string ConvertToValue(out byte value)`
  - Parameters:
    - `out byte value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 815)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* byte */);
    ```
- `protected override string OnNewValue(byte value)`
  - Parameters:
    - `byte value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 812)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* byte */);
    ```

## Class `CharListDataFieldVM`

List of s

**Inherits/Implements:** `DataFieldVM<IList<char>>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.CharListDataFieldVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1295)

### Constructors

- `public CharListDataFieldVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1300)
- `public CharListDataFieldVM(IList<char> value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `IList<char> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1309)

### Methods

- `protected override string ConvertToValue(out IList<char> value)`
  - Parameters:
    - `out IList<char> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1316)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<char> */);
    ```
- `protected override string OnNewValue(IList<char> value)`
  - Parameters:
    - `IList<char> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1313)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<char> */);
    ```

## Class `CharVM`

**Inherits/Implements:** `DataFieldVM<char>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.CharVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 762)

### Constructors

- `public CharVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 767)
- `public CharVM(char value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `char value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 776)

### Methods

- `protected override string ConvertToValue(out char value)`
  - Parameters:
    - `out char value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 783)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* char */);
    ```
- `protected override string OnNewValue(char value)`
  - Parameters:
    - `char value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 780)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* char */);
    ```

## Class `DataFieldVM`

Data field base class

**Inherits/Implements:** `ViewModelBase`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.DataFieldVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 67)

### Constructors

- `protected DataFieldVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 134)

### Methods

- `protected abstract string Validate()`
  - Summary: Validates the data. Returns null or an empty string if there was no error, or an error string that can be shown to the user.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 144)
  - Example:
    ```csharp
    // Example invocation
    instance.Validate();
    ```
- `protected override string Verify(string columnName)`
  - Summary: Checks the string for errors
  - Parameters:
    - `string columnName`: Property name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 159)
  - Example:
    ```csharp
    // Example invocation
    instance.Verify(columnName: /* string */);
    ```
- `protected virtual void OnStringValueChanged()`
  - Summary: Called when gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 123)
  - Example:
    ```csharp
    // Example invocation
    instance.OnStringValueChanged();
    ```
- `protected void ForceWriteStringValue(string value)`
  - Summary: Force writing a new even if nothing changed
  - Parameters:
    - `string value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 104)
  - Example:
    ```csharp
    // Example invocation
    instance.ForceWriteStringValue(value: /* string */);
    ```
- `protected void Revalidate()`
  - Summary: Revalidates the field for errors
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 115)
  - Example:
    ```csharp
    // Example invocation
    instance.Revalidate();
    ```
- `protected void WriteStringValueFromConstructor(string value)`
  - Summary: Must only be called from the constructor
  - Parameters:
    - `string value`: Initial
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 95)
  - Example:
    ```csharp
    // Example invocation
    instance.WriteStringValueFromConstructor(value: /* string */);
    ```
- `public abstract string ConvertToObjectValue(out object value)`
  - Summary: Converts the string to the target value. Returns null or an empty string if there were no errors, else an error string that can be shown to the user.
  - Parameters:
    - `out object value`: Result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 152)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToObjectValue(value: /* object */);
    ```

### Properties

- `public abstract object ObjectValue { get; set; }`
  - Summary: Gets/sets the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 74)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ObjectValue;
    ```
- `public bool IsNull => string.IsNullOrWhiteSpace(StringValue)`
  - Summary: true if the value is null ( is empty)
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 128)
  - Example:
    ```csharp
    // Read the property
    var value = instance.IsNull;
    ```
- `public override bool HasError => cachedError.HasError`
  - Summary: true if there's at least one error
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 169)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasError;
    ```
- `public string StringValue {
			get => stringValue;
			set {
				if (value == null)
					throw new ArgumentNullException(nameof(value));
				if (stringValue != value)
					ForceWriteStringValue(value);
			}
		}`
  - Summary: Gets the string representation of the value. This could be an invalid string. Use to check whether it's valid.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 80)
  - Example:
    ```csharp
    // Read the property
    var value = instance.StringValue;
    ```

## Class `DataFieldVM<T>`

Data field base class

**Inherits/Implements:** `DataFieldVM`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.DataFieldVM<T>(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 176)

### Constructors

- `protected DataFieldVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 202)

### Methods

- `protected abstract string ConvertToValue(out T value)`
  - Summary: Converts the current string to the real value. Returns null or an empty string if there were no errors, else an error string that can be shown to the user.
  - Parameters:
    - `out T value`: Result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 231)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* T */);
    ```
- `protected abstract string OnNewValue(T value)`
  - Summary: Converts to a string
  - Parameters:
    - `T value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 223)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* T */);
    ```
- `protected override string Validate()`
  - Summary: Validates the data. Returns null or an empty string if there was no error, or an error string that can be shown to the user.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 250)
  - Example:
    ```csharp
    // Example invocation
    instance.Validate();
    ```
- `protected void SetValue(T value)`
  - Summary: Writes a new value
  - Parameters:
    - `T value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 216)
  - Example:
    ```csharp
    // Example invocation
    instance.SetValue(value: /* T */);
    ```
- `protected void SetValueFromConstructor(T value)`
  - Summary: Must only be called from the constructor
  - Parameters:
    - `T value`: Initial value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 210)
  - Example:
    ```csharp
    // Example invocation
    instance.SetValueFromConstructor(value: /* T */);
    ```
- `public override string ConvertToObjectValue(out object value)`
  - Summary: Converts the string to the target value. Returns null or an empty string if there were no errors, else an error string that can be shown to the user.
  - Parameters:
    - `out object value`: Result
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 239)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToObjectValue(value: /* object */);
    ```

### Properties

- `public T Value {
			get {
				var s = ConvertToValue(out var value);
				if (string.IsNullOrEmpty(s))
					return value;
				throw new FormatException(s);
			}
			set { SetValue(value); }
		}`
  - Summary: Gets/sets the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 188)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public override object ObjectValue {
			get => Value;
			set => Value = (T)value;
		}`
  - Summary: Gets/sets the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 180)
  - Example:
    ```csharp
    // Read the property
    var value = instance.ObjectValue;
    ```

## Class `DateTimeVM`

**Inherits/Implements:** `DataFieldVM<DateTime>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.DateTimeVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1175)

### Constructors

- `public DateTimeVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1180)
- `public DateTimeVM(DateTime value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `DateTime value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1189)

### Methods

- `protected override string ConvertToValue(out DateTime value)`
  - Parameters:
    - `out DateTime value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1196)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* DateTime */);
    ```
- `protected override string OnNewValue(DateTime value)`
  - Parameters:
    - `DateTime value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1193)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* DateTime */);
    ```

## Class `DecimalVM`

**Inherits/Implements:** `DataFieldVM<decimal>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.DecimalVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1145)

### Constructors

- `public DecimalVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1150)
- `public DecimalVM(decimal value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `decimal value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1159)

### Methods

- `protected override string ConvertToValue(out decimal value)`
  - Parameters:
    - `out decimal value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1166)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* decimal */);
    ```
- `protected override string OnNewValue(decimal value)`
  - Parameters:
    - `decimal value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1163)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* decimal */);
    ```

## Class `DefaultConverterVM<T>`

Uses the default converter to convert the type to/from a string

**Inherits/Implements:** `DataFieldVM<T>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.DefaultConverterVM<T>(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1679)

### Constructors

- `public DefaultConverterVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1693)
- `public DefaultConverterVM(T value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `T value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1702)

### Methods

- `protected override string ConvertToValue(out T value)`
  - Parameters:
    - `out T value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1709)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* T */);
    ```
- `protected override string OnNewValue(T value)`
  - Parameters:
    - `T value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1706)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* T */);
    ```

## Class `DoubleListDataFieldVM`

List of s

**Inherits/Implements:** `DataFieldVM<IList<double>>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.DoubleListDataFieldVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1611)

### Constructors

- `public DoubleListDataFieldVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1616)
- `public DoubleListDataFieldVM(IList<double> value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `IList<double> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1625)

### Methods

- `protected override string ConvertToValue(out IList<double> value)`
  - Parameters:
    - `out IList<double> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1632)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<double> */);
    ```
- `protected override string OnNewValue(IList<double> value)`
  - Parameters:
    - `IList<double> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1629)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<double> */);
    ```

## Class `DoubleVM`

**Inherits/Implements:** `DataFieldVM<double>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.DoubleVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1078)

### Constructors

- `public DoubleVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1083)
- `public DoubleVM(double value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `double value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1092)

### Methods

- `protected override string ConvertToValue(out double value)`
  - Parameters:
    - `out double value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1099)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* double */);
    ```
- `protected override string OnNewValue(double value)`
  - Parameters:
    - `double value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1096)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* double */);
    ```

## Class `EnumListVM`

List of enum values

**Inherits/Implements:** `ListVM<EnumVM>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.EnumListVM(list: /* IList<EnumVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 100)

### Constructors

- `public EnumListVM(IEnumerable<EnumVM> list, Action<int, int> onChanged)`
  - Summary: Constructor
  - Parameters:
    - `IEnumerable<EnumVM> list`: Initial value
    - `Action<int, int> onChanged`: Called when the selected item gets changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 129)
- `public EnumListVM(IList<EnumVM> list)`
  - Summary: Constructor
  - Parameters:
    - `IList<EnumVM> list`: Initial value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 120)

### Methods

- `public bool Has(object value)`
  - Summary: Checks whether the list contains a value
  - Parameters:
    - `object value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 138)
  - Example:
    ```csharp
    // Example invocation
    instance.Has(value: /* object */);
    ```
- `public int GetIndex(object value)`
  - Summary: Gets the index of the value. If it doesn't exist, it's automatically added to the list
  - Parameters:
    - `object value`: Value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 151)
  - Example:
    ```csharp
    // Example invocation
    instance.GetIndex(value: /* object */);
    ```

### Properties

- `public new object SelectedItem {
			get {
				if (Index < 0 || Index >= list.Count)
					return null;
				return list[Index].Value;
			}
			set {
				if (!object.Equals(SelectedItem, value))
					SelectedIndex = GetIndex(value);
			}
		}`
  - Summary: Gets the selected item
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 104)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectedItem;
    ```

## Class `EnumVM`

Enum value

**Inherits/Implements:** `ViewModelBase`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.EnumVM(value: /* object */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 28)

### Constructors

- `public EnumVM(object value)`
  - Summary: Constructor
  - Parameters:
    - `object value`: Initial value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 46)
- `public EnumVM(object value, string name)`
  - Summary: Constructor
  - Parameters:
    - `object value`: Initial value
    - `string name`: Name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 56)

### Methods

- `public override string ToString()`
  - Summary: Gets the name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 94)
  - Example:
    ```csharp
    // Example invocation
    instance.ToString();
    ```
- `public static EnumVM[] Create(Type enumType, params object[] values)`
  - Summary: Creates an array of s
  - Parameters:
    - `Type enumType`: Type of enum
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 67)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.EnumVM.Create(enumType: /* Type */);
    ```
- `public static EnumVM[] Create(bool sort, Type enumType, params object[] values)`
  - Summary: Creates an array of s
  - Parameters:
    - `bool sort`: true to sort the array
    - `Type enumType`: Type of enum
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 76)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.EnumVM.Create(sort: /* bool */, enumType: /* Type */);
    ```

### Properties

- `public object Value => value`
  - Summary: Gets the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 35)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Value;
    ```
- `public string Name => name`
  - Summary: Gets the name
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/EnumVM.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Name;
    ```

## Class `GuidVM`

**Inherits/Implements:** `DataFieldVM<Guid>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.GuidVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1235)

### Constructors

- `public GuidVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1240)
- `public GuidVM(Guid value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Guid value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1249)

### Methods

- `protected override string ConvertToValue(out Guid value)`
  - Parameters:
    - `out Guid value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1256)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* Guid */);
    ```
- `protected override string OnNewValue(Guid value)`
  - Parameters:
    - `Guid value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1253)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* Guid */);
    ```

## Class `HexStringVM`

Hex string

**Inherits/Implements:** `DataFieldVM<IList<byte>>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.HexStringVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 371)

### Constructors

- `public HexStringVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 385)
- `public HexStringVM(IList<byte> value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `IList<byte> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 394)

### Methods

- `protected override string ConvertToValue(out IList<byte> value)`
  - Parameters:
    - `out IList<byte> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 401)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<byte> */);
    ```
- `protected override string OnNewValue(IList<byte> value)`
  - Parameters:
    - `IList<byte> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 398)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<byte> */);
    ```

### Properties

- `public bool UpperCaseHex {
			get => upperCaseHex;
			set => upperCaseHex = value;
		}`
  - Summary: Gets/sets whether to use upper case hex digits
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 375)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UpperCaseHex;
    ```

## Interface `IInitializeDataTemplate`

Initializes data templates

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.IInitializeDataTemplate and call its members.
var instance = new dnSpy.Contracts.MVVM.IInitializeDataTemplate(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/IInitializeDataTemplate.cs` (line 26)

### Methods

- `void Initialize(DependencyObject d)`
  - Summary: Called to initialize
  - Parameters:
    - `DependencyObject d`: Target object with the property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/IInitializeDataTemplate.cs` (line 31)
  - Example:
    ```csharp
    // Example invocation
    instance.Initialize(d: /* DependencyObject */);
    ```

## Interface `IPickDirectory`

Asks the user to pick a directory

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.IPickDirectory and call its members.
var instance = new dnSpy.Contracts.MVVM.IPickDirectory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickDirectory.cs` (line 27)

### Methods

- `string GetDirectory(string currentDir = null)`
  - Summary: Lets the user pick a directory. Returns null if user canceled.
  - Parameters:
    - `string currentDir` (default: `null`): Current directory or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickDirectory.cs` (line 33)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDirectory(currentDir: /* string */);
    ```

## Interface `IPickFilename`

Asks the user to pick a filename

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.IPickFilename and call its members.
var instance = new dnSpy.Contracts.MVVM.IPickFilename(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilename.cs` (line 29)

### Methods

- `string GetFilename(string currentFileName, string defaultExtension, string filter = null)`
  - Summary: Lets the user pick a new filename. Returns null if the user didn't pick a new filename.
  - Parameters:
    - `string currentFileName`: Current filename or null
    - `string defaultExtension`: Default extension. It must not contain a period. Eg. valid extensions are "exe" and "dll" but not ".exe"
    - `string filter` (default: `null`): Filename filter or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilename.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFilename(currentFileName: /* string */, defaultExtension: /* string */, filter: /* string */);
    ```
- `string[] GetFilenames(string currentFileName, string defaultExtension, string filter = null)`
  - Summary: Lets the user pick filenames. Returns an empty array if the user canceled the dialog box.
  - Parameters:
    - `string currentFileName`: Current filename or null
    - `string defaultExtension`: Default extension. It must not contain a period. Eg. valid extensions are "exe" and "dll" but not ".exe"
    - `string filter` (default: `null`): Filename filter or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilename.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFilenames(currentFileName: /* string */, defaultExtension: /* string */, filter: /* string */);
    ```

## Interface `IPickSaveFilename`

Asks the user to pick a filename

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.IPickSaveFilename and call its members.
var instance = new dnSpy.Contracts.MVVM.IPickSaveFilename(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickSaveFilename.cs` (line 28)

### Methods

- `string GetFilename(string currentFileName, string defaultExtension, string filter = null)`
  - Summary: Lets the user pick a new filename. Returns null if the user didn't pick a new filename.
  - Parameters:
    - `string currentFileName`: Current filename or null
    - `string defaultExtension`: Default extension. It must not contain a period. Eg. valid extensions are "exe" and "dll" but not ".exe"
    - `string filter` (default: `null`): Filename filter or null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickSaveFilename.cs` (line 37)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFilename(currentFileName: /* string */, defaultExtension: /* string */, filter: /* string */);
    ```

## Class `InitDataTemplateAP`

Initialize data template attached property

**Inherits/Implements:** `DependencyObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.InitDataTemplateAP and call its members.
var instance = new dnSpy.Contracts.MVVM.InitDataTemplateAP(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/InitDataTemplateAP.cs` (line 29)

### Methods

- `public static bool GetInitialize(FrameworkElement element)`
  - Summary: Gets the initialize value
  - Parameters:
    - `FrameworkElement element`: Element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/InitDataTemplateAP.cs` (line 48)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.InitDataTemplateAP.GetInitialize(element: /* FrameworkElement */);
    ```
- `public static void SetInitialize(FrameworkElement element, bool value)`
  - Summary: Sets initialize value
  - Parameters:
    - `FrameworkElement element`: Element
    - `bool value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/InitDataTemplateAP.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.InitDataTemplateAP.SetInitialize(element: /* FrameworkElement */, value: /* bool */);
    ```

### Fields

- `public static readonly DependencyProperty InitializeProperty = DependencyProperty.RegisterAttached(
			"Initialize", typeof(bool), typeof(InitDataTemplateAP), new UIPropertyMetadata(false, InitializePropertyChangedCallback))`
  - Summary: Initialize property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/InitDataTemplateAP.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.InitDataTemplateAP.InitializeProperty;
    ```

## Class `Int16ListDataFieldVM`

List of s

**Inherits/Implements:** `NumberDataFieldVM<IList<short>`, `short>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.Int16ListDataFieldVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1485)

### Constructors

- `public Int16ListDataFieldVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1491)
- `public Int16ListDataFieldVM(IList<short> value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `IList<short> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1501)

### Methods

- `protected override string ConvertToValue(out IList<short> value)`
  - Parameters:
    - `out IList<short> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1508)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<short> */);
    ```
- `protected override string OnNewValue(IList<short> value)`
  - Parameters:
    - `IList<short> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1505)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<short> */);
    ```

## Class `Int16VM`

**Inherits/Implements:** `NumberDataFieldVM<short`, `short>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.Int16VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 952)

### Constructors

- `public Int16VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 958)
- `public Int16VM(short value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `short value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 968)

### Methods

- `protected override string ConvertToValue(out short value)`
  - Parameters:
    - `out short value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 975)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* short */);
    ```
- `protected override string OnNewValue(short value)`
  - Parameters:
    - `short value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 972)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* short */);
    ```

## Class `Int32ListDataFieldVM`

List of s

**Inherits/Implements:** `NumberDataFieldVM<IList<int>`, `int>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.Int32ListDataFieldVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1517)

### Constructors

- `public Int32ListDataFieldVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1523)
- `public Int32ListDataFieldVM(IList<int> value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `IList<int> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1533)

### Methods

- `protected override string ConvertToValue(out IList<int> value)`
  - Parameters:
    - `out IList<int> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1540)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<int> */);
    ```
- `protected override string OnNewValue(IList<int> value)`
  - Parameters:
    - `IList<int> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1537)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<int> */);
    ```

## Class `Int32VM`

**Inherits/Implements:** `NumberDataFieldVM<int`, `int>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.Int32VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 984)

### Constructors

- `public Int32VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 990)
- `public Int32VM(int value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `int value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1000)

### Methods

- `protected override string ConvertToValue(out int value)`
  - Parameters:
    - `out int value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1007)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* int */);
    ```
- `protected override string OnNewValue(int value)`
  - Parameters:
    - `int value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1004)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* int */);
    ```

## Class `Int64ListDataFieldVM`

List of s

**Inherits/Implements:** `NumberDataFieldVM<IList<long>`, `long>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.Int64ListDataFieldVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1549)

### Constructors

- `public Int64ListDataFieldVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1555)
- `public Int64ListDataFieldVM(IList<long> value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `IList<long> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1565)

### Methods

- `protected override string ConvertToValue(out IList<long> value)`
  - Parameters:
    - `out IList<long> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1572)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<long> */);
    ```
- `protected override string OnNewValue(IList<long> value)`
  - Parameters:
    - `IList<long> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1569)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<long> */);
    ```

## Class `Int64VM`

**Inherits/Implements:** `NumberDataFieldVM<long`, `long>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.Int64VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1016)

### Constructors

- `public Int64VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1022)
- `public Int64VM(long value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `long value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1032)

### Methods

- `protected override string ConvertToValue(out long value)`
  - Parameters:
    - `out long value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1039)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* long */);
    ```
- `protected override string OnNewValue(long value)`
  - Parameters:
    - `long value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1036)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* long */);
    ```

## Class `IsDraggableAP`

Is-draggable attached property

**Inherits/Implements:** `DependencyObject`

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.IsDraggableAP and call its members.
var instance = new dnSpy.Contracts.MVVM.IsDraggableAP(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/IsDraggableAP.cs` (line 26)

### Methods

- `public static bool GetIsDraggable(FrameworkElement element)`
  - Summary: Gets the is-draggable value
  - Parameters:
    - `FrameworkElement element`: Element
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/IsDraggableAP.cs` (line 45)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.IsDraggableAP.GetIsDraggable(element: /* FrameworkElement */);
    ```
- `public static void SetIsDraggable(FrameworkElement element, bool value)`
  - Summary: Writes a new is-draggable value
  - Parameters:
    - `FrameworkElement element`: Target
    - `bool value`: New value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/IsDraggableAP.cs` (line 38)
  - Example:
    ```csharp
    // Example invocation
    dnSpy.Contracts.MVVM.IsDraggableAP.SetIsDraggable(element: /* FrameworkElement */, value: /* bool */);
    ```

### Fields

- `public static readonly DependencyProperty IsDraggableProperty = DependencyProperty.RegisterAttached(
			"IsDraggable", typeof(bool), typeof(IsDraggableAP), new FrameworkPropertyMetadata(false, FrameworkPropertyMetadataOptions.Inherits))`
  - Summary: Is draggable property
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/IsDraggableAP.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.IsDraggableAP.IsDraggableProperty;
    ```

## Class `ListVM<T>`

List of items

**Inherits/Implements:** `INotifyPropertyChanged`, `IDataErrorInfo`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.ListVM<T>();
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 31)

### Constructors

- `public ListVM()`
  - Summary: Constructor
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 119)
- `public ListVM(Action<int, int> onChanged)`
  - Summary: Constructor
  - Parameters:
    - `Action<int, int> onChanged`: Called when the selected item gets changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 127)
- `public ListVM(IEnumerable<T> list, Action<int, int> onChanged)`
  - Summary: Constructor
  - Parameters:
    - `IEnumerable<T> list`: Initial value
    - `Action<int, int> onChanged`: Called when the selected item gets changed
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 146)
- `public ListVM(IList<T> list)`
  - Summary: Constructor
  - Parameters:
    - `IList<T> list`: Initial value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 137)

### Methods

- `public void InvalidateSelected(IEnumerable<T> newValues, bool addDefault, T defaultValue)`
  - Parameters:
    - `IEnumerable<T> newValues`: Description not provided.
    - `bool addDefault`: Description not provided.
    - `T defaultValue`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 53)
  - Example:
    ```csharp
    // Example invocation
    instance.InvalidateSelected(newValues: /* IEnumerable<T> */, addDefault: /* bool */, defaultValue: /* T */);
    ```

### Properties

- `protected int Index => index`
  - Summary: Gets the index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 40)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Index;
    ```
- `public IList<T> Items => list`
  - Summary: Gets the items
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 45)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Items;
    ```
- `public T SelectedItem {
			get {
				if (index < 0 || index >= list.Count)
					return default;
				return list[index];
			}
			set {
				if (index < 0 || !object.Equals(value, SelectedItem))
					SelectedIndex = GetIndex(value);
			}
		}`
  - Summary: Gets/sets the selected item
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 104)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectedItem;
    ```
- `public int SelectedIndex {
			get => index;
			set {
				if (index != value) {
					int oldIndex = index;
					Debug.Assert(value >= 0 && value < list.Count);
					index = value;
					OnPropertyChanged(nameof(SelectedIndex));
					OnPropertyChanged(nameof(SelectedItem));
					onChanged?.Invoke(oldIndex, index);
				}
			}
		}`
  - Summary: Gets/sets the selected index
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 87)
  - Example:
    ```csharp
    // Read the property
    var value = instance.SelectedIndex;
    ```

### Fields

- `protected ObservableCollection<T> list`
  - Summary: The list
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 33)
  - Example:
    ```csharp
    var value = instance.list;
    ```
- `public Func<ListVM<T>, string> DataErrorInfoDelegate`
  - Summary: Can be set to validate the list
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 180)
  - Example:
    ```csharp
    var value = instance.DataErrorInfoDelegate;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/ListVM.cs` (line 162)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

## Class `NullableBooleanVM`

Nullable

**Inherits/Implements:** `DataFieldVM<bool?>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NullableBooleanVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 410)

### Constructors

- `public NullableBooleanVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 415)
- `public NullableBooleanVM(bool? value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `bool? value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 424)

### Methods

- `protected override string ConvertToValue(out bool? value)`
  - Parameters:
    - `out bool? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 431)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* bool? */);
    ```
- `protected override string OnNewValue(bool? value)`
  - Parameters:
    - `bool? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 428)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* bool? */);
    ```

## Class `NullableByteVM`

Nullable

**Inherits/Implements:** `NumberDataFieldVM<byte?`, `byte>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NullableByteVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 480)

### Constructors

- `public NullableByteVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 486)
- `public NullableByteVM(byte? value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `byte? value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 496)

### Methods

- `protected override string ConvertToValue(out byte? value)`
  - Parameters:
    - `out byte? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 503)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* byte? */);
    ```
- `protected override string OnNewValue(byte? value)`
  - Parameters:
    - `byte? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 500)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* byte? */);
    ```

## Class `NullableGuidVM`

Nullable

**Inherits/Implements:** `DataFieldVM<Guid?>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NullableGuidVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 327)

### Constructors

- `public NullableGuidVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 332)
- `public NullableGuidVM(Guid? value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Guid? value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 341)

### Methods

- `protected override string ConvertToValue(out Guid? value)`
  - Parameters:
    - `out Guid? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 348)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* Guid? */);
    ```
- `protected override string OnNewValue(Guid? value)`
  - Parameters:
    - `Guid? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 345)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* Guid? */);
    ```

## Class `NullableInt16VM`

Nullable

**Inherits/Implements:** `NumberDataFieldVM<short?`, `short>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NullableInt16VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 516)

### Constructors

- `public NullableInt16VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 522)
- `public NullableInt16VM(short? value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `short? value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 532)

### Methods

- `protected override string ConvertToValue(out short? value)`
  - Parameters:
    - `out short? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 539)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* short? */);
    ```
- `protected override string OnNewValue(short? value)`
  - Parameters:
    - `short? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 536)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* short? */);
    ```

## Class `NullableInt32VM`

Nullable

**Inherits/Implements:** `NumberDataFieldVM<int?`, `int>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NullableInt32VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 588)

### Constructors

- `public NullableInt32VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 594)
- `public NullableInt32VM(int? value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `int? value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 604)

### Methods

- `protected override string ConvertToValue(out int? value)`
  - Parameters:
    - `out int? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 611)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* int? */);
    ```
- `protected override string OnNewValue(int? value)`
  - Parameters:
    - `int? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 608)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* int? */);
    ```

## Class `NullableInt64VM`

Nullable

**Inherits/Implements:** `NumberDataFieldVM<long?`, `long>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NullableInt64VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 660)

### Constructors

- `public NullableInt64VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 666)
- `public NullableInt64VM(long? value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `long? value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 676)

### Methods

- `protected override string ConvertToValue(out long? value)`
  - Parameters:
    - `out long? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 683)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* long? */);
    ```
- `protected override string OnNewValue(long? value)`
  - Parameters:
    - `long? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 680)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* long? */);
    ```

## Class `NullableSByteVM`

Nullable

**Inherits/Implements:** `NumberDataFieldVM<sbyte?`, `sbyte>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NullableSByteVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 444)

### Constructors

- `public NullableSByteVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 450)
- `public NullableSByteVM(sbyte? value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `sbyte? value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 460)

### Methods

- `protected override string ConvertToValue(out sbyte? value)`
  - Parameters:
    - `out sbyte? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 467)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* sbyte? */);
    ```
- `protected override string OnNewValue(sbyte? value)`
  - Parameters:
    - `sbyte? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 464)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* sbyte? */);
    ```

## Class `NullableUInt16VM`

Nullable

**Inherits/Implements:** `NumberDataFieldVM<ushort?`, `ushort>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NullableUInt16VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 552)

### Constructors

- `public NullableUInt16VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 558)
- `public NullableUInt16VM(ushort? value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `ushort? value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 568)

### Methods

- `protected override string ConvertToValue(out ushort? value)`
  - Parameters:
    - `out ushort? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 575)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* ushort? */);
    ```
- `protected override string OnNewValue(ushort? value)`
  - Parameters:
    - `ushort? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 572)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* ushort? */);
    ```

## Class `NullableUInt32VM`

Nullable

**Inherits/Implements:** `NumberDataFieldVM<uint?`, `uint>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NullableUInt32VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 624)

### Constructors

- `public NullableUInt32VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 630)
- `public NullableUInt32VM(uint? value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `uint? value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 640)

### Methods

- `protected override string ConvertToValue(out uint? value)`
  - Parameters:
    - `out uint? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 647)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* uint? */);
    ```
- `protected override string OnNewValue(uint? value)`
  - Parameters:
    - `uint? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 644)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* uint? */);
    ```

## Class `NullableUInt64VM`

Nullable

**Inherits/Implements:** `NumberDataFieldVM<ulong?`, `ulong>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NullableUInt64VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 696)

### Constructors

- `public NullableUInt64VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 702)
- `public NullableUInt64VM(ulong? value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `ulong? value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 712)

### Methods

- `protected override string ConvertToValue(out ulong? value)`
  - Parameters:
    - `out ulong? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 719)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* ulong? */);
    ```
- `protected override string OnNewValue(ulong? value)`
  - Parameters:
    - `ulong? value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 716)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* ulong? */);
    ```

## Class `NumberDataFieldVM<T, U>`

Number base class

**Inherits/Implements:** `DataFieldVM<T>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.NumberDataFieldVM<T, U>(onUpdated: /* Action<DataFieldVM> */, min: /* U */, max: /* U */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 268)

### Constructors

- `protected NumberDataFieldVM(Action<DataFieldVM> onUpdated, U min, U max, bool? useDecimal)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `U min`: Minimum value
    - `U max`: Maximum value
    - `bool? useDecimal`: true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 316)

### Properties

- `public U Max {
			get => max;
			set {
				max = value;
				Revalidate();
			}
		}`
  - Summary: Gets/sets the maximum value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 300)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Max;
    ```
- `public U Min {
			get => min;
			set {
				min = value;
				Revalidate();
			}
		}`
  - Summary: Gets/sets the minimum value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 288)
  - Example:
    ```csharp
    // Read the property
    var value = instance.Min;
    ```
- `public bool? UseDecimal {
			get => useDecimal;
			set {
				if (useDecimal != value) {
					useDecimal = value;
					if (!HasError)
						ForceWriteStringValue(OnNewValue(Value));
				}
			}
		}`
  - Summary: true to always use decimal, false to never use decimal (except if it's just one digit), and null to use decimal or hex depending on what number it is.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 273)
  - Example:
    ```csharp
    // Read the property
    var value = instance.UseDecimal;
    ```

## Class `PickDirectory`

Implements

**Inherits/Implements:** `IPickDirectory`

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.PickDirectory and call its members.
var instance = new dnSpy.Contracts.MVVM.PickDirectory(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickDirectory.cs` (line 39)

### Methods

- `public string GetDirectory(string currentDir)`
  - Parameters:
    - `string currentDir`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickDirectory.cs` (line 42)
  - Example:
    ```csharp
    // Example invocation
    instance.GetDirectory(currentDir: /* string */);
    ```

## Class `PickFilename`

Implements

**Inherits/Implements:** `IPickFilename`

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.PickFilename and call its members.
var instance = new dnSpy.Contracts.MVVM.PickFilename(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilename.cs` (line 54)

### Methods

- `public string GetFilename(string currentFileName, string defaultExtension, string filter)`
  - Parameters:
    - `string currentFileName`: Description not provided.
    - `string defaultExtension`: Description not provided.
    - `string filter`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilename.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFilename(currentFileName: /* string */, defaultExtension: /* string */, filter: /* string */);
    ```
- `public string[] GetFilenames(string currentFileName, string defaultExtension, string filter = null)`
  - Parameters:
    - `string currentFileName`: Description not provided.
    - `string defaultExtension`: Description not provided.
    - `string filter` (default: `null`): Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilename.cs` (line 74)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFilenames(currentFileName: /* string */, defaultExtension: /* string */, filter: /* string */);
    ```

## Class `PickFilenameConstants`

Pick filename constants

**Example**

```csharp
// Access dnSpy.Contracts.MVVM.PickFilenameConstants members directly without instantiation.
dnSpy.Contracts.MVVM.PickFilenameConstants./* member */
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilenameConstants.cs` (line 26)

### Fields

- `public static readonly string AnyFilenameFilter = $"{dnSpy_Contracts_DnSpy_Resources.AllFiles} (*.*)|*.*"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilenameConstants.cs` (line 30)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.PickFilenameConstants.AnyFilenameFilter;
    ```
- `public static readonly string DotNetAssemblyOrModuleFilter = $"{dnSpy_Contracts_DnSpy_Resources.Files_DotNetExecutables} (*.exe, *.dll, *.netmodule, *.winmd)|*.exe;*.dll;*.netmodule;*.winmd|{dnSpy_Contracts_DnSpy_Resources.AllFiles} (*.*)|*.*"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilenameConstants.cs` (line 32)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.PickFilenameConstants.DotNetAssemblyOrModuleFilter;
    ```
- `public static readonly string DotNetExecutableFilter = $"{dnSpy_Contracts_DnSpy_Resources.Files_DotNetExecutables} (*.exe)|*.exe|{dnSpy_Contracts_DnSpy_Resources.AllFiles} (*.*)|*.*"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilenameConstants.cs` (line 31)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.PickFilenameConstants.DotNetExecutableFilter;
    ```
- `public static readonly string ExecutableFilter = $"{dnSpy_Contracts_DnSpy_Resources.Files_Executables} (*.exe)|*.exe|{dnSpy_Contracts_DnSpy_Resources.AllFiles} (*.*)|*.*"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilenameConstants.cs` (line 34)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.PickFilenameConstants.ExecutableFilter;
    ```
- `public static readonly string ImagesFilter = $"{dnSpy_Contracts_DnSpy_Resources.Files_Images}|*.png;*.gif;*.bmp;*.dib;*.jpg;*.jpeg;*.jpe;*.jif;*.jfif;*.jfi;*.ico;*.cur|{dnSpy_Contracts_DnSpy_Resources.AllFiles} (*.*)|*.*"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilenameConstants.cs` (line 28)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.PickFilenameConstants.ImagesFilter;
    ```
- `public static readonly string NetModuleFilter = $"{dnSpy_Contracts_DnSpy_Resources.Files_DotNetNetModules} (*.netmodule)|*.netmodule|{dnSpy_Contracts_DnSpy_Resources.AllFiles} (*.*)|*.*"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilenameConstants.cs` (line 33)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.PickFilenameConstants.NetModuleFilter;
    ```
- `public static readonly string StrongNameKeyFilter = $"{dnSpy_Contracts_DnSpy_Resources.Files_StrongNameKeyFiles} (*.snk)|*.snk|{dnSpy_Contracts_DnSpy_Resources.AllFiles} (*.*)|*.*"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilenameConstants.cs` (line 29)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.PickFilenameConstants.StrongNameKeyFilter;
    ```
- `public static readonly string XmlFilenameFilter = $"{dnSpy_Contracts_DnSpy_Resources.Files_XmlFiles} (*.xml)|*.xml|{dnSpy_Contracts_DnSpy_Resources.AllFiles} (*.*)|*.*"`
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickFilenameConstants.cs` (line 35)
  - Example:
    ```csharp
    var value = dnSpy.Contracts.MVVM.PickFilenameConstants.XmlFilenameFilter;
    ```

## Class `PickSaveFilename`

Implements

**Inherits/Implements:** `IPickSaveFilename`

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.PickSaveFilename and call its members.
var instance = new dnSpy.Contracts.MVVM.PickSaveFilename(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickSaveFilename.cs` (line 43)

### Methods

- `public string GetFilename(string currentFileName, string extension, string filter)`
  - Parameters:
    - `string currentFileName`: Description not provided.
    - `string extension`: Description not provided.
    - `string filter`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/PickSaveFilename.cs` (line 46)
  - Example:
    ```csharp
    // Example invocation
    instance.GetFilename(currentFileName: /* string */, extension: /* string */, filter: /* string */);
    ```

## Class `RelayCommand`

Implements the interface

**Inherits/Implements:** `ICommand`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.RelayCommand(exec: /* Action<object> */, canExec: /* Predicate<object> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/RelayCommand.cs` (line 27)

### Constructors

- `public RelayCommand(Action<object> exec, Predicate<object> canExec = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<object> exec`: Called when the command gets executed
    - `Predicate<object> canExec` (default: `null`): Gets called to check whether can execute, may be null
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/RelayCommand.cs` (line 37)

## Class `SByteListDataFieldVM`

List of s

**Inherits/Implements:** `NumberDataFieldVM<IList<sbyte>`, `sbyte>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.SByteListDataFieldVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1453)

### Constructors

- `public SByteListDataFieldVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1459)
- `public SByteListDataFieldVM(IList<sbyte> value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `IList<sbyte> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1469)

### Methods

- `protected override string ConvertToValue(out IList<sbyte> value)`
  - Parameters:
    - `out IList<sbyte> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1476)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<sbyte> */);
    ```
- `protected override string OnNewValue(IList<sbyte> value)`
  - Parameters:
    - `IList<sbyte> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1473)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<sbyte> */);
    ```

## Class `SByteVM`

**Inherits/Implements:** `NumberDataFieldVM<sbyte`, `sbyte>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.SByteVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 920)

### Constructors

- `public SByteVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 926)
- `public SByteVM(sbyte value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `sbyte value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 936)

### Methods

- `protected override string ConvertToValue(out sbyte value)`
  - Parameters:
    - `out sbyte value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 943)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* sbyte */);
    ```
- `protected override string OnNewValue(sbyte value)`
  - Parameters:
    - `sbyte value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 940)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* sbyte */);
    ```

## Class `SingleListDataFieldVM`

List of s

**Inherits/Implements:** `DataFieldVM<IList<float>>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.SingleListDataFieldVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1581)

### Constructors

- `public SingleListDataFieldVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1586)
- `public SingleListDataFieldVM(IList<float> value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `IList<float> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1595)

### Methods

- `protected override string ConvertToValue(out IList<float> value)`
  - Parameters:
    - `out IList<float> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1602)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<float> */);
    ```
- `protected override string OnNewValue(IList<float> value)`
  - Parameters:
    - `IList<float> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1599)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<float> */);
    ```

## Class `SingleVM`

**Inherits/Implements:** `DataFieldVM<float>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.SingleVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1048)

### Constructors

- `public SingleVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1053)
- `public SingleVM(float value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `float value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1062)

### Methods

- `protected override string ConvertToValue(out float value)`
  - Parameters:
    - `out float value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1069)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* float */);
    ```
- `protected override string OnNewValue(float value)`
  - Parameters:
    - `float value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1066)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* float */);
    ```

## Class `StringListDataFieldVM`

List of s

**Inherits/Implements:** `DataFieldVM<IList<string>>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.StringListDataFieldVM(onUpdated: /* Action<DataFieldVM> */, allowNullString: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1641)

### Constructors

- `public StringListDataFieldVM(Action<DataFieldVM> onUpdated, bool allowNullString = true)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool allowNullString` (default: `true`): true to allow null strings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1649)
- `public StringListDataFieldVM(IList<string> value, Action<DataFieldVM> onUpdated, bool allowNullString = true)`
  - Summary: Constructor
  - Parameters:
    - `IList<string> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool allowNullString` (default: `true`): true to allow null strings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1659)

### Methods

- `protected override string ConvertToValue(out IList<string> value)`
  - Parameters:
    - `out IList<string> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1669)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<string> */);
    ```
- `protected override string OnNewValue(IList<string> value)`
  - Parameters:
    - `IList<string> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1666)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<string> */);
    ```

## Class `StringVM`

**Inherits/Implements:** `DataFieldVM<string>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.StringVM(onUpdated: /* Action<DataFieldVM> */, allowNullString: /* bool */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1108)

### Constructors

- `public StringVM(Action<DataFieldVM> onUpdated, bool allowNullString = false)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool allowNullString` (default: `false`): true to allow null strings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1116)
- `public StringVM(string value, Action<DataFieldVM> onUpdated, bool allowNullString = false)`
  - Summary: Constructor
  - Parameters:
    - `string value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool allowNullString` (default: `false`): true to allow null strings
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1126)

### Methods

- `protected override string ConvertToValue(out string value)`
  - Parameters:
    - `out string value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1136)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* string */);
    ```
- `protected override string OnNewValue(string value)`
  - Parameters:
    - `string value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1133)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* string */);
    ```

## Class `TimeSpanVM`

**Inherits/Implements:** `DataFieldVM<TimeSpan>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.TimeSpanVM(onUpdated: /* Action<DataFieldVM> */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1205)

### Constructors

- `public TimeSpanVM(Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1210)
- `public TimeSpanVM(TimeSpan value, Action<DataFieldVM> onUpdated)`
  - Summary: Constructor
  - Parameters:
    - `TimeSpan value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1219)

### Methods

- `protected override string ConvertToValue(out TimeSpan value)`
  - Parameters:
    - `out TimeSpan value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1226)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* TimeSpan */);
    ```
- `protected override string OnNewValue(TimeSpan value)`
  - Parameters:
    - `TimeSpan value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1223)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* TimeSpan */);
    ```

## Class `UInt16ListDataFieldVM`

List of s

**Inherits/Implements:** `NumberDataFieldVM<IList<ushort>`, `ushort>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.UInt16ListDataFieldVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1357)

### Constructors

- `public UInt16ListDataFieldVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1363)
- `public UInt16ListDataFieldVM(IList<ushort> value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `IList<ushort> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1373)

### Methods

- `protected override string ConvertToValue(out IList<ushort> value)`
  - Parameters:
    - `out IList<ushort> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1380)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<ushort> */);
    ```
- `protected override string OnNewValue(IList<ushort> value)`
  - Parameters:
    - `IList<ushort> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1377)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<ushort> */);
    ```

## Class `UInt16VM`

**Inherits/Implements:** `NumberDataFieldVM<ushort`, `ushort>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.UInt16VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 824)

### Constructors

- `public UInt16VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 830)
- `public UInt16VM(ushort value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `ushort value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 840)

### Methods

- `protected override string ConvertToValue(out ushort value)`
  - Parameters:
    - `out ushort value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 847)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* ushort */);
    ```
- `protected override string OnNewValue(ushort value)`
  - Parameters:
    - `ushort value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 844)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* ushort */);
    ```

## Class `UInt32ListDataFieldVM`

List of s

**Inherits/Implements:** `NumberDataFieldVM<IList<uint>`, `uint>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.UInt32ListDataFieldVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1389)

### Constructors

- `public UInt32ListDataFieldVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1395)
- `public UInt32ListDataFieldVM(IList<uint> value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `IList<uint> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1405)

### Methods

- `protected override string ConvertToValue(out IList<uint> value)`
  - Parameters:
    - `out IList<uint> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1412)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<uint> */);
    ```
- `protected override string OnNewValue(IList<uint> value)`
  - Parameters:
    - `IList<uint> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1409)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<uint> */);
    ```

## Class `UInt32VM`

**Inherits/Implements:** `NumberDataFieldVM<uint`, `uint>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.UInt32VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 856)

### Constructors

- `public UInt32VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 862)
- `public UInt32VM(uint value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `uint value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 872)

### Methods

- `protected override string ConvertToValue(out uint value)`
  - Parameters:
    - `out uint value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 879)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* uint */);
    ```
- `protected override string OnNewValue(uint value)`
  - Parameters:
    - `uint value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 876)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* uint */);
    ```

## Class `UInt64ListDataFieldVM`

List of s

**Inherits/Implements:** `NumberDataFieldVM<IList<ulong>`, `ulong>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.UInt64ListDataFieldVM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1421)

### Constructors

- `public UInt64ListDataFieldVM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1427)
- `public UInt64ListDataFieldVM(IList<ulong> value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `IList<ulong> value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1437)

### Methods

- `protected override string ConvertToValue(out IList<ulong> value)`
  - Parameters:
    - `out IList<ulong> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1444)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* IList<ulong> */);
    ```
- `protected override string OnNewValue(IList<ulong> value)`
  - Parameters:
    - `IList<ulong> value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 1441)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* IList<ulong> */);
    ```

## Class `UInt64VM`

**Inherits/Implements:** `NumberDataFieldVM<ulong`, `ulong>`

**Example**

```csharp
var instance = new dnSpy.Contracts.MVVM.UInt64VM(onUpdated: /* Action<DataFieldVM> */, useDecimal: /* bool? */);
```

*Defined in* `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 888)

### Constructors

- `public UInt64VM(Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 894)
- `public UInt64VM(ulong value, Action<DataFieldVM> onUpdated, bool? useDecimal = null)`
  - Summary: Constructor
  - Parameters:
    - `ulong value`: Initial value
    - `Action<DataFieldVM> onUpdated`: Called when value gets updated
    - `bool? useDecimal` (default: `null`): true to use decimal, false to use hex, or null if it depends on the value
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 904)

### Methods

- `protected override string ConvertToValue(out ulong value)`
  - Parameters:
    - `out ulong value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 911)
  - Example:
    ```csharp
    // Example invocation
    instance.ConvertToValue(value: /* ulong */);
    ```
- `protected override string OnNewValue(ulong value)`
  - Parameters:
    - `ulong value`: Description not provided.
  - Defined in: `dnSpy/dnSpy.Contracts.DnSpy/MVVM/DataFieldVM.cs` (line 908)
  - Example:
    ```csharp
    // Example invocation
    instance.OnNewValue(value: /* ulong */);
    ```

## Class `ViewModelBase`

Base class of view models

**Inherits/Implements:** `INotifyPropertyChanged`, `IDataErrorInfo`

**Example**

```csharp
// Instantiate dnSpy.Contracts.MVVM.ViewModelBase and call its members.
var instance = new dnSpy.Contracts.MVVM.ViewModelBase(/* arguments */);
```

*Defined in* `dnSpy/dnSpy.Contracts.Logic/MVVM/ViewModelBase.cs` (line 27)

### Methods

- `protected virtual string Verify(string columnName)`
  - Summary: Called to check if a property is valid. Returns null or an empty string if there's no error, else an error string that can be shown to the user
  - Parameters:
    - `string columnName`: Name of property
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/MVVM/ViewModelBase.cs` (line 57)
  - Example:
    ```csharp
    // Example invocation
    instance.Verify(columnName: /* string */);
    ```
- `protected void HasErrorUpdated()`
  - Summary: Call this method if some property's error state changed
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/MVVM/ViewModelBase.cs` (line 62)
  - Example:
    ```csharp
    // Example invocation
    instance.HasErrorUpdated();
    ```
- `protected void OnPropertyChanged(PropertyChangedEventArgs e)`
  - Summary: Raises
  - Parameters:
    - `PropertyChangedEventArgs e`: Changed event args
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/MVVM/ViewModelBase.cs` (line 41)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(e: /* PropertyChangedEventArgs */);
    ```
- `protected void OnPropertyChanged(string propName)`
  - Summary: Raises
  - Parameters:
    - `string propName`: Name of property that got changed
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/MVVM/ViewModelBase.cs` (line 35)
  - Example:
    ```csharp
    // Example invocation
    instance.OnPropertyChanged(propName: /* string */);
    ```

### Properties

- `public virtual bool HasError => false`
  - Summary: true if there's an error
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/MVVM/ViewModelBase.cs` (line 49)
  - Example:
    ```csharp
    // Read the property
    var value = instance.HasError;
    ```

### Events

- `public event PropertyChangedEventHandler PropertyChanged`
  - Defined in: `dnSpy/dnSpy.Contracts.Logic/MVVM/ViewModelBase.cs` (line 29)
  - Example:
    ```csharp
    // Subscribe to the event
    instance.PropertyChanged += (sender, args) =>
    {
        // TODO: handler logic
    };
    ```

