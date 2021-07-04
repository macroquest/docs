## Description

The Macro DataType deals with the macro currently running, and nothing else.

## Members

|                                        |                     |                                                                                |
|----------------------------------------|---------------------|--------------------------------------------------------------------------------|
| **DataType**                           | **Member Name**     | **Description**                                                                |
| *[string](datatype-string.md)* | **CurCommand**      | list the current line number, macro name and code of the macro being processed |
| *[int](datatype-int.md)*       | **CurLine**         | The current line number of the macro being processed                           |
| *[string](datatype-string.md)* | **CurSub**          | The current sub routine                                                        |
| *[bool](datatype-bool.md)*     | **isOuterVariable** | true if the provided parameter is a defined outer variable                     |
| *[bool](datatype-bool.md)*     | **isTLO**           | true if the provided parameter an existing TLO                                 |
| *[int](datatype-int.md)*       | **MemUse**          | How much memory the macro is using                                             |
| *[string](datatype-string.md)* | **Name**            | The name of the macro currently running                                        |
| *[int](datatype-int.md)*       | **Params**          | The number of parameters that were passed to the current subroutine            |
| *[bool](datatype-bool.md)*     | **Paused**          | NULL if no macro running, FALSE if mqpause is off, TRUE if mqpause is on       |
| *[string](datatype-string.md)* | **Return**          | The value that was returned by the last completed subroutine                   |
| *[int](datatype-int.md)*       | **RunTime**         | How long the macro has been running (in seconds)                               |
| *[int](datatype-int.md)*       | **StackSize**       | StackSize?                                                                     |
| *[Invoke](../macro-commands/invoke.md)*          | **Undeclared**      | will list all undeclared variables                                             |
|                                        |                     |                                                                                |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Macro](../top-level-objects/tlo-macro.md)


