## Description

Data types related to the current MacroQuest2 session

## Members

|                                            |                                     |                                                      |
|--------------------------------------------|-------------------------------------|------------------------------------------------------|
| **Type**                                   | **Member**                          | **Description**                                      |
| *[string](datatype-string.md)*     | **BuildDate**                       | Date that MQ2Main.dll was built                      |
| *[bool](datatype-bool.md)*         | **ChatChannel\[**channel name**\]** | Returns TRUE if *channel name* is joined             |
| *[string](datatype-string.md)*     | **ChatChannel\[**#**\]**            | Returns the name of chat channel #                   |
| *[int](datatype-int.md)*           | **ChatChannels**                    | Returns the number of channels currently joined      |
| *[string](datatype-string.md)*     | **Error**                           | Last normal error message                            |
| *[string](datatype-string.md)*     | **GameState**                       | Returns "INGAME, CHARSELECT, PRECHARSELECT, UNKNOWN" |
| *[string](datatype-string.md)*     | **LastCommand**                     | Last command entered                                 |
| *[string](datatype-string.md)*     | **LastTell**                        | Name of last person to send you a tell               |
| *[bool](datatype-bool.md)*         | **LClickedObject**                  | Returns TRUE if an object has been left clicked      |
| *[string](datatype-string.md)*     | **LoginName**                       | Your station name                                    |
| *[int](datatype-int.md)*           | **MouseX**                          | Mouse's X location                                   |
| *[int](datatype-int.md)*           | **MouseY**                          | Mouse's Y location                                   |
| *[string](datatype-string.md)*     | **MQ2DataError**                    | Last MQ2Data parsing error message                   |
| *[string](datatype-string.md)*     | **Path**                            | Directory that Macroquest.exe launched from          |
| *[int](datatype-int.md)*           | **Ping**                            | Your current ping                                    |
| *[int](datatype-int.md)*           | **Running**                         | Running time of current MQ2 session, in milliseconds |
| *[string](datatype-string.md)*     | **Server**                          | Full name of your server                             |
| *[string](datatype-string.md)*     | **SyntaxError**                     | Last syntax error message                            |
| *[int](datatype-int.md)*           | **ViewportX**                       | EverQuest viewport upper left (X) position           |
| *[int](datatype-int.md)*           | **ViewportXCenter**                 | EverQuest viewport center (X) position               |
| *[int](datatype-int.md)*           | **ViewportXMax**                    | EverQuest viewport lower right (X) position          |
| *[int](datatype-int.md)*           | **ViewportY**                       | EverQuest viewport upper left (Y) position           |
| *[int](datatype-int.md)*           | **ViewportYCenter**                 | EverQuest viewport center (Y) position               |
| *[int](datatype-int.md)*           | **ViewportYMax**                    | EverQuest viewport lower right (Y) position          |
| '**'[string](datatype-string.md)** | **To String**                       | None                                                 |

## Example

`/echo ${MacroQuest.Server}`

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)


