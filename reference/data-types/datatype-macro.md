# DataType:macro

The Macro DataType deals with the macro currently running, and nothing else.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_string_](datatype-string.md) | **CurCommand** | list the current line number, macro name, and code of the macro being processed |
| [_int_](datatype-int.md) | **CurLine** | The current line number of the macro being processed |
| [_string_](datatype-string.md) | **CurSub** | The current subroutine |
| [_bool_](datatype-bool.md) | **isOuterVariable** | true if the provided parameter is a defined outer variable |
| [_bool_](datatype-bool.md) | **isTLO** | true if the provided parameter an existing TLO |
| [_int_](datatype-int.md) | **MemUse** | How much memory the macro is using |
| [_string_](datatype-string.md) | **Name** | The name of the macro currently running |
| [_int_](datatype-int.md) | **Params** | The number of parameters that were passed to the current subroutine |
| [_bool_](datatype-bool.md) | **Paused** | NULL if no macro running, FALSE if mqpause is off, TRUE if mqpause is on |
| [_string_](datatype-string.md) | **Return** | The value that was returned by the last completed subroutine |
| [_int_](datatype-int.md) | **RunTime** | How long the macro has been running (in seconds) |
| [_int_](datatype-int.md) | **StackSize** | StackSize? |
| varies | **Variable** | returns the value given the name of Macro variable |

## Methods

| Method Name | Action |
| :--- | :--- |
| Undeclared | List all undeclared variables |

