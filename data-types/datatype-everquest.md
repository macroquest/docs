## Description

Data types related to the current EverQuest session. This replaces the MacroQuest datatype.

## Members

|                                            |                                     |                                                                                                                                                     |
|--------------------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Type**                                   | **Member**                          | **Description**                                                                                                                                     |
| *[bool](datatype-bool.md)*         | **Background**                      | Returns TRUE if EverQuest is in Background                                                                                                          |
| *[string](datatype-string.md)*     | **BuildDate**                       | Date that MQ2Main.dll was built                                                                                                                     |
| *[int](datatype-int.md)*           | **CharSelectList**                  | Currently returns the zone ID the character is currently in                                                                                         |
| *[bool](datatype-bool.md)*         | **ChatChannel\[**channel name**\]** | Returns TRUE if *channel name* is joined                                                                                                            |
| *[string](datatype-string.md)*     | **ChatChannel\[**#**\]**            | Returns the name of chat channel #                                                                                                                  |
| *[int](datatype-int.md)*           | **ChatChannels**                    | Returns the number of channels currently joined                                                                                                     |
| *[string](datatype-string.md)*     | **CurrentUI**                       | return a string representing the currently loaded UI skin                                                                                           |
| *[string](datatype-string.md)*     | **Error**                           | Last normal error message                                                                                                                           |
| *[bool](datatype-bool.md)*         | **Foreground**                      | Returns TRUE if EverQuest is in Foreground                                                                                                          |
| *[string](datatype-string.md)*     | **GameState**                       | CHARSELECT INGAME UNKNOWN                                                                                                                           |
| *[bool](datatype-bool.md)*         | **IsDefaultUILoaded**               | returns a bool true or false if the "Default" UI skin is the one loaded                                                                             |
| *[string](datatype-string.md)*     | **LastCommand**                     | Last command entered                                                                                                                                |
| *[int](datatype-int.md)*           | **LastMouseOver.Name**              | Returns the name of the last window you moused over                                                                                                 |
| *[string](datatype-string.md)*     | **LastTell**                        | Name of last person to send you a tell                                                                                                              |
| *[bool](datatype-bool.md)*         | **LayoutCopyInProgress**            | Returns TRUE if a layoutcopy is in progress and FALSE if not.                                                                                       |
| *[bool](datatype-bool.md)*         | **LClickedObject**                  | Returns TRUE if an object has been left clicked                                                                                                     |
| *[string](datatype-string.md)*     | **LoginName**                       | Your station name                                                                                                                                   |
| *[int](datatype-int.md)*           | **MouseX**                          | Mouse's X location                                                                                                                                  |
| *[int](datatype-int.md)*           | **MouseY**                          | Mouse's Y location                                                                                                                                  |
| *[string](datatype-string.md)*     | **MQ2DataError**                    | Last MQ2Data parsing error message                                                                                                                  |
| *[int](datatype-int.md)*           | **PID**                             | Your current (Process ID)                                                                                                                           |
| *[int](datatype-int.md)*           | **Ping**                            | Your current ping                                                                                                                                   |
| *[int](datatype-int.md)*           | **Running**                         | Running time of current MQ2 session, in milliseconds                                                                                                |
| *[int](datatype-int.md)*           | **ScreenMode**                      | Returns the screenmode as an integer, 2 is Normal and 3 is No Windows                                                                               |
| *[string](datatype-string.md)*     | **Server**                          | Full name of your server                                                                                                                            |
| *[string](datatype-string.md)*     | **SyntaxError**                     | Last syntax error message                                                                                                                           |
| *[int](datatype-int.md)*           | **PPriority**                       | Returns the processor priority that Everquest is set to. Where 1 is Low 2 is below Normal 3 is Normal 4 is Above Normal 5 is High and 6 is RealTime |
| *[int](datatype-int.md)*           | **ViewportX**                       | EverQuest viewport upper left (X) position                                                                                                          |
| *[int](datatype-int.md)*           | **ViewportXCenter**                 | EverQuest viewport center (X) position                                                                                                              |
| *[int](datatype-int.md)*           | **ViewportXMax**                    | EverQuest viewport lower right (X) position                                                                                                         |
| *[int](datatype-int.md)*           | **ViewportY**                       | EverQuest viewport upper left (Y) position                                                                                                          |
| *[int](datatype-int.md)*           | **ViewportYCenter**                 | EverQuest viewport center (Y) position                                                                                                              |
| *[int](datatype-int.md)*           | **ViewportYMax**                    | EverQuest viewport lower right (Y) position                                                                                                         |
| '**'[string](datatype-string.md)** | **To String**                       | None                                                                                                                                                |

## Example

`/echo ${EverQuest.Server}`

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [Slash Commands](../commands/slash-commands.md)


