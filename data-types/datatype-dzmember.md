## Description

This DataType contains information on the members of the current dynamic zone instance

## Members

|                                            |               |                                                                                                                                                   |
|--------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Type**                                   | **Member**    | **Description**                                                                                                                                   |
| *[bool](datatype-bool.md)*         | **Flagged**   | Returns true if the dzmember can successfully enter the dz. <Example:$%7BDynamicZone.Member%5Bx%5D.Flagged>} where x is either index or the name. |
| *[string](datatype-string.md)*     | **Name**      | The name of the member                                                                                                                            |
| *[string](datatype-string.md)*     | **Status**    | The status of the member - one of the following: Unknown, Online, Offline, In Dynamic Zone, Link Dead                                             |
| '**'[string](datatype-string.md)** | **To String** | Same as **Name**                                                                                                                                  |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)
-   [DataType:dynamiczone](datatype-dynamiczone.md)


