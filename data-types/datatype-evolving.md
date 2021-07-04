## Description

A DataType that deals with evolving items.

## Members

|                                            |               |                                                      |
|--------------------------------------------|---------------|------------------------------------------------------|
| **Type**                                   | **Member**    | **Description**                                      |
| *[float](datatype-float.md)*       | **ExpPct**    | Percentage of experience that the item has gained    |
| *[bool](datatype-bool.md)*         | **ExpOn**     | Is evolving item experience turned on for this item? |
| *[int](datatype-int.md)*           | **Level**     | The level of the evolving item.                      |
| *[int](datatype-int.md)*           | **MaxLevel**  | The maximum level of the evolving item               |
| '**'[string](datatype-string.md)** | **To String** | Same as **ExpOn**                                    |

## Examples

`/echo ${FindItem[Blade of the Eclipse].Evolving.ExpPct}`

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [DataType:item](datatype-item.md)


