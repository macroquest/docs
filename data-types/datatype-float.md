## Description

Contains all information related to floating point numbers

-   A floating-point number is one which has a decimal component (*e.g.* **1.01**)
-   Members of this DataType generally manipulate the number's precision (*i.e.* how many decimal places)
-   They all round correctly with the exception of *int*

## Members

|                                            |                        |                                                                                       |
|--------------------------------------------|------------------------|---------------------------------------------------------------------------------------|
| **Type**                                   | **Member**             | **Description**                                                                       |
| *[string](datatype-string.md)*     | **Deci**               | The number as a string with **one** place of precision, *i.e.* ###.#                  |
| *[string](datatype-string.md)*     | **Centi**              | The number as a string with **two** places of precision, *i.e.* ###.##                |
| *[int](datatype-int.md)*           | **Int**                | Integer portion of the number truncated rather than rounded, *e.g.* 12.779 returns 12 |
| *[string](datatype-string.md)*     | **Milli**              | The number as a string with **three** places of precision, *i.e.* ###.###             |
| *[string](datatype-string.md)*     | **Precision\[**#**\]** | The number as a string with # places of precision                                     |
| '**'[string](datatype-string.md)** | **To String**          | Same as **Centi**                                                                     |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Float](../top-level-objects/tlo-float.md)
-   [DataType:math](datatype-math.md)
-   [DataType:int](datatype-int.md)


