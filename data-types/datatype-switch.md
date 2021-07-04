## Description

Data related to switches (levers, buttons, etc) in the zone

## Members

|                                            |                    |                                                      |
|--------------------------------------------|--------------------|------------------------------------------------------|
| **Type**                                   | **Member**         | **Description**                                      |
| *[heading](datatype-heading.md)*   | **DefaultHeading** | Heading of "closed" switch                           |
| *[float](datatype-float.md)*       | **Distance**       | Distance from player to switch in (x,y)              |
| *[heading](datatype-heading.md)*   | **Heading**        | Switch is facing this heading                        |
| *[heading](datatype-heading.md)*   | **HeadingTo**      | Direction player must move to meet this switch       |
| *[int](datatype-int.md)*           | **ID**             | Switch ID                                            |
| *[bool](datatype-bool.md)*         | **LineOfSight**    | Returns TRUE if the switch is in LoS                 |
| *[string](datatype-string.md)*     | **Name**           | Name                                                 |
| *[bool](datatype-bool.md)*         | **Open**           | Open?                                                |
| *[float](datatype-float.md)*       | **X**              | X coordinate                                         |
| *[float](datatype-float.md)*       | **Y**              | Y coordinate                                         |
| *[float](datatype-float.md)*       | **Z**              | Z coordinate                                         |
| *[float](datatype-float.md)*       | **W**              | X coordinate (Westward-positive)                     |
| *[float](datatype-float.md)*       | **N**              | Y coordinate (Northward-positive)                    |
| *[float](datatype-float.md)*       | **D**              | D coordinate (Upward-positive)                       |
| *[float](datatype-float.md)*       | **DefaultX**       | X coordinate of "closed" switch                      |
| *[float](datatype-float.md)*       | **DefaultY**       | Y coordinate of "closed" switch                      |
| *[float](datatype-float.md)*       | **DefaultZ**       | Z coordinate of "closed" switch                      |
| *[float](datatype-float.md)*       | **DefaultW**       | X coordinate of "closed" switch (Westward-positive)  |
| *[float](datatype-float.md)*       | **DefaultN**       | Y coordinate of "closed" switch (Northward-positive) |
| *[float](datatype-float.md)*       | **DefaultU**       | Z coordinate of "closed" switch (Upward-positive)    |
| '**'[string](datatype-string.md)** | **To String**      | Same as **ID**                                       |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Switch](../top-level-objects/tlo-switch.md)
-   [DataType:heading](datatype-heading.md)


