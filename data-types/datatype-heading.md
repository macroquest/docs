## Description

Data related to a specific spawn heading

## Members

|                                            |                |                                                                               |
|--------------------------------------------|----------------|-------------------------------------------------------------------------------|
| **Type**                                   | **Member**     | **Description**                                                               |
| *[int](datatype-int.md)*           | **Clock**      | The nearest clock direction, e.g. 1-12                                        |
| *[float](datatype-float.md)*       | **Degrees**    | Heading in degrees (same as casting to float)                                 |
| *[float](datatype-float.md)*       | **DegreesCCW** | Heading in degrees counter-clockwise (the way the rest of MQ2 and EQ uses it) |
| *[string](datatype-string.md)*     | **Name**       | The long compass direction, eg. "south", "south by southeast"                 |
| *[string](datatype-string.md)*     | **ShortName**  | The short compass direction, eg. "S", "SSE"                                   |
| '**'[string](datatype-string.md)** | **To String**  | Same as **ShortName**                                                         |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Heading](../top-level-objects/tlo-heading.md)
-   [DataType:spawn](datatype-spawn.md)
-   [DataType:ground](datatype-ground.md)
-   [DataType:switch](datatype-switch.md)


