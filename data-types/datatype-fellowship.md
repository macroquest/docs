## Description

Contains all the data about your fellowship

## Members

|                                                            |                               |                                                           |
|------------------------------------------------------------|-------------------------------|-----------------------------------------------------------|
| **Type**                                                   | **Member**                    | **Description**                                           |
| *[bool](datatype-bool.md)*                         | **Campfire**                  | TRUE if campfire is up, FALSE if not                      |
| *[ticks](datatype-ticks.md)*                       | **CampfireDuration**          | Time left on current campfire                             |
| *[float](datatype-float.md)*                       | **CampfireX**                 | Campfire X location                                       |
| *[float](datatype-float.md)*                       | **CampfireY**                 | Campfire Y location                                       |
| *[float](datatype-float.md)*                       | **CampfireZ**                 | Campfire Z location                                       |
| *[zone](datatype-zone.md)*                         | **CampfireZone**              | Zone information for the zone that contains your campfire |
| *[int](datatype-int.md)*                           | **ID**                        | Fellowship ID                                             |
| *[string](datatype-string.md)*                     | **Leader**                    | Fellowship leader's name                                  |
| *[fellowshipmember](datatype-fellowshipmember.md)* | **Member\[**name**\|**#**\]** | Member data by *name* or *#*                              |
| *[int](datatype-int.md)*                           | **Members**                   | Number of members in the fellowship                       |
| *[string](datatype-string.md)*                     | **MotD**                      | Fellowship Message of the Day                             |
| '**'[string](datatype-string.md)**                 | **To String**                 | TRUE if currently in a fellowship, FALSE if not           |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [DataType:fellowshipmember](datatype-fellowshipmember.md)
-   [DataType:character](datatype-character.md)


