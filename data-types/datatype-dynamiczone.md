## Description

Data for the current dynamic zone instance

## Members

|                                            |                               |                                                                                                                                               |
|--------------------------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Type**                                   | **Member**                    | **Description**                                                                                                                               |
| *[dzmember](datatype-dzmember.md)* | **Leader**                    | The leader of the dynamic zone                                                                                                                |
| *[bool](datatype-bool.md)*         | **LeaderFlagged**             | Returns true if the dzleader can successfully enter the dz (this also means the dz is actually Loaded.) Example: ${DynamicZone.LeaderFlagged} |
| *[int](datatype-int.md)*           | **MaxMembers**                | Maximum number of characters that can enter this dynamic zone                                                                                 |
| *[dzmember](datatype-dzmember.md)* | **Member\[**#**\|**name**\]** | The dynamic zone member *#* or *name*                                                                                                         |
| *[int](datatype-int.md)*           | **Members**                   | Current number of characters in the dynamic zone                                                                                              |
| *[string](datatype-string.md)*     | **Name**                      | The full name of the dynamic zone                                                                                                             |
| '**'[string](datatype-string.md)** | **To String**                 | Same as **Name**                                                                                                                              |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)
-   [DataType:dzmember](datatype-dzmember.md)


