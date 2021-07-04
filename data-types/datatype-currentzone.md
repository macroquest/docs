## Description

Contains data about the current zone. Inherits [zone](datatype-zone.md).

## Members

|                                            |               |                                                                                                    |
|--------------------------------------------|---------------|----------------------------------------------------------------------------------------------------|
| **Type**                                   | **Member**    | **Description**                                                                                    |
| *[bool](datatype-bool.md)*         | **Dungeon**   | Are we in a dungeon                                                                                |
| *[float](datatype-float.md)*       | **Gravity**   | Gravity                                                                                            |
| *[int](datatype-int.md)*           | **ID**        | Zone ID                                                                                            |
| *[bool](datatype-bool.md)*         | **Indoor**    | Are we indoors?                                                                                    |
| *[float](datatype-float.md)*       | **MaxClip**   | Maximum clip plane allowed in zone                                                                 |
| *[float](datatype-float.md)*       | **MinClip**   | Minimum clip plane allowed in zone                                                                 |
| *[string](datatype-string.md)*     | **Name**      | Full zone name                                                                                     |
| *[bool](datatype-bool.md)*         | **NoBind**    | Can we bind here?                                                                                  |
| *[bool](datatype-bool.md)*         | **Outdoor**   | Are we outdoors?                                                                                   |
| *[string](datatype-string.md)*     | **ShortName** | Short zone name                                                                                    |
| *[int](datatype-int.md)*           | **SkyType**   | Sky type                                                                                           |
| *[int](datatype-int.md)*           | **Type**      | Zone type:0=Indoor Dungeon 1=Outdoor 2=Outdoor City 3=Dungeon City 4=Indoor City 5=Outdoor Dungeon |
| *[int](datatype-int.md)*           | **FOgOnOff**  | Is the fog on\|off                                                                                 |
| '**'[string](datatype-string.md)** | **To String** | Same as **Name**                                                                                   |

## Example

A check in a condition or a macro to determine if the current zone is indoors:

    ${Zone.Indoor}

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Zone](../top-level-objects/tlo-zone.md)
-   [DataType:zone](datatype-zone.md)


