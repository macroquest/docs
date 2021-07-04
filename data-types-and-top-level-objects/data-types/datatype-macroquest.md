# DataType:macroquest

## Description

Data types related to the current MacroQuest2 session

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_string_](datatype-string.md) | **BuildDate** | Date that MQ2Main.dll was built |
| [_bool_](datatype-bool.md) | **ChatChannel\[**channel name**\]** | Returns TRUE if _channel name_ is joined |
| [_string_](datatype-string.md) | **ChatChannel\[**\#**\]** | Returns the name of chat channel \# |
| [_int_](datatype-int.md) | **ChatChannels** | Returns the number of channels currently joined |
| [_string_](datatype-string.md) | **Error** | Last normal error message |
| [_string_](datatype-string.md) | **GameState** | Returns "INGAME, CHARSELECT, PRECHARSELECT, UNKNOWN" |
| [_string_](datatype-string.md) | **LastCommand** | Last command entered |
| [_string_](datatype-string.md) | **LastTell** | Name of last person to send you a tell |
| [_bool_](datatype-bool.md) | **LClickedObject** | Returns TRUE if an object has been left clicked |
| [_string_](datatype-string.md) | **LoginName** | Your station name |
| [_int_](datatype-int.md) | **MouseX** | Mouse's X location |
| [_int_](datatype-int.md) | **MouseY** | Mouse's Y location |
| [_string_](datatype-string.md) | **MQ2DataError** | Last MQ2Data parsing error message |
| [_string_](datatype-string.md) | **Path** | Directory that Macroquest.exe launched from |
| [_int_](datatype-int.md) | **Ping** | Your current ping |
| [_int_](datatype-int.md) | **Running** | Running time of current MQ2 session, in milliseconds |
| [_string_](datatype-string.md) | **Server** | Full name of your server |
| [_string_](datatype-string.md) | **SyntaxError** | Last syntax error message |
| [_int_](datatype-int.md) | **ViewportX** | EverQuest viewport upper left \(X\) position |
| [_int_](datatype-int.md) | **ViewportXCenter** | EverQuest viewport center \(X\) position |
| [_int_](datatype-int.md) | **ViewportXMax** | EverQuest viewport lower right \(X\) position |
| [_int_](datatype-int.md) | **ViewportY** | EverQuest viewport upper left \(Y\) position |
| [_int_](datatype-int.md) | **ViewportYCenter** | EverQuest viewport center \(Y\) position |
| [_int_](datatype-int.md) | **ViewportYMax** | EverQuest viewport lower right \(Y\) position |
| '**'**[**string**](datatype-string.md) | **To String** | None |

## Example

`/echo ${MacroQuest.Server}`

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)

