## Description

This is currenly not a supported datatype. This page was added as a visual representation of JacenSolo's idea for an
Event TLO and the connected datatype. In theory, the Event datatype deals with events in the current macro.

## Members

|                                                          |                                                                                        |
|----------------------------------------------------------|----------------------------------------------------------------------------------------|
| *[string](datatype-string.md)* **List**          | Returns a list of loaded Events, separated by commas                                   |
| *[int](datatype-int.md)* **Triggered**           | Returns the number of events which have been triggered but not checked by /doevents    |
| *[bool](datatype-bool.md)* **Triggered\[Name\]** | Returns TRUE if Event Name has been triggered but not checked, otherwise returns FALSE |
| **To String**                                            | Same as **List**                                                                       |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [Pound_Commands](../macro-commands/pound-commands.md)
-   [Custom_Events](../macros/custom-events.md)
-   [Macro_Reference](../documentation/macro-reference.md)
-   [Event](../macro-commands/event.md)


