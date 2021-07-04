# DataType:EverQuest

## Description

Data types related to the current EverQuest session. This replaces the MacroQuest datatype.

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_bool_](datatype-bool.md) | **Background** | Returns TRUE if EverQuest is in Background |
| [_string_](datatype-string.md) | **BuildDate** | Date that MQ2Main.dll was built |
| [_int_](datatype-int.md) | **CharSelectList** | Currently returns the zone ID the character is currently in |
| [_bool_](datatype-bool.md) | **ChatChannel\[**channel name**\]** | Returns TRUE if _channel name_ is joined |
| [_string_](datatype-string.md) | **ChatChannel\[**\#**\]** | Returns the name of chat channel \# |
| [_int_](datatype-int.md) | **ChatChannels** | Returns the number of channels currently joined |
| [_string_](datatype-string.md) | **CurrentUI** | return a string representing the currently loaded UI skin |
| [_string_](datatype-string.md) | **Error** | Last normal error message |
| [_bool_](datatype-bool.md) | **Foreground** | Returns TRUE if EverQuest is in Foreground |
| [_string_](datatype-string.md) | **GameState** | CHARSELECT INGAME UNKNOWN |
| [_bool_](datatype-bool.md) | **IsDefaultUILoaded** | returns a bool true or false if the "Default" UI skin is the one loaded |
| [_string_](datatype-string.md) | **LastCommand** | Last command entered |
| [_int_](datatype-int.md) | **LastMouseOver.Name** | Returns the name of the last window you moused over |
| [_string_](datatype-string.md) | **LastTell** | Name of last person to send you a tell |
| [_bool_](datatype-bool.md) | **LayoutCopyInProgress** | Returns TRUE if a layoutcopy is in progress and FALSE if not. |
| [_bool_](datatype-bool.md) | **LClickedObject** | Returns TRUE if an object has been left clicked |
| [_string_](datatype-string.md) | **LoginName** | Your station name |
| [_int_](datatype-int.md) | **MouseX** | Mouse's X location |
| [_int_](datatype-int.md) | **MouseY** | Mouse's Y location |
| [_string_](datatype-string.md) | **MQ2DataError** | Last MQ2Data parsing error message |
| [_int_](datatype-int.md) | **PID** | Your current \(Process ID\) |
| [_int_](datatype-int.md) | **Ping** | Your current ping |
| [_int_](datatype-int.md) | **Running** | Running time of current MQ2 session, in milliseconds |
| [_int_](datatype-int.md) | **ScreenMode** | Returns the screenmode as an integer, 2 is Normal and 3 is No Windows |
| [_string_](datatype-string.md) | **Server** | Full name of your server |
| [_string_](datatype-string.md) | **SyntaxError** | Last syntax error message |
| [_int_](datatype-int.md) | **PPriority** | Returns the processor priority that Everquest is set to. Where 1 is Low 2 is below Normal 3 is Normal 4 is Above Normal 5 is High and 6 is RealTime |
| [_int_](datatype-int.md) | **ViewportX** | EverQuest viewport upper left \(X\) position |
| [_int_](datatype-int.md) | **ViewportXCenter** | EverQuest viewport center \(X\) position |
| [_int_](datatype-int.md) | **ViewportXMax** | EverQuest viewport lower right \(X\) position |
| [_int_](datatype-int.md) | **ViewportY** | EverQuest viewport upper left \(Y\) position |
| [_int_](datatype-int.md) | **ViewportYCenter** | EverQuest viewport center \(Y\) position |
| [_int_](datatype-int.md) | **ViewportYMax** | EverQuest viewport lower right \(Y\) position |
| '**'**[**string**](datatype-string.md) | **To String** | None |

## Example

`/echo ${EverQuest.Server}`

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [Slash Commands](../../commands/slash-commands/)

