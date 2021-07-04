## Description

Contains data related to time

## Members

|                                            |                          |                                                                            |
|--------------------------------------------|--------------------------|----------------------------------------------------------------------------|
| **Type**                                   | **Member**               | **Description**                                                            |
| *[string](datatype-string.md)*     | **Date**                 | Date in the format MM/DD/YYYY                                              |
| *[int](datatype-int.md)*           | **Day**                  | Day of the month                                                           |
| *[int](datatype-int.md)*           | **DayOfWeek**            | Day of the week (1=sunday to 7=saturday)                                   |
| *[int](datatype-int.md)*           | **Hour**                 | Hour (0-23)                                                                |
| *[int](datatype-int.md)*           | **Minute**               | Minute (0-59)                                                              |
| *[int](datatype-int.md)*           | **Month**                | Month of the year (1-12)                                                   |
| *[bool](datatype-bool.md)*         | **Night**                | Gives true if the current hour is considered "night" in EQ (7:00pm-6:59am) |
| *[int](datatype-int.md)*           | **Second**               | Second (0-59)                                                              |
| *[int](datatype-int.md)*           | **SecondsSinceMidnight** | Number of seconds since midnight                                           |
| *[string](datatype-string.md)*     | **Time12**               | Time in 12-hour format (HH:MM:SS)                                          |
| *[string](datatype-string.md)*     | **Time24**               | Time in 24-hour format (HH:MM:SS)                                          |
| *[int](datatype-int.md)*           | **Year**                 | Year                                                                       |
| '**'[string](datatype-string.md)** | **To String**            | Same as **Time24**                                                         |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Time](../top-level-objects/tlo-time.md)
-   [TLO:GameTime](../top-level-objects/tlo-gametime.md)


