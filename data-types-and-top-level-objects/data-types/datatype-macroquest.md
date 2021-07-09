# DataType:macroquest

Data types related to the current MacroQuest2 session

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| \_\_[_string_](datatype-string.md)\_\_ | **BuildDate** | Date that MQ2Main.dll was built |
| [_bool_](datatype-bool.md) | **ChatChannel\[**channel name**\]** | Returns TRUE if _channel name_ is joined |
| \_\_[_string_](datatype-string.md)\_\_ | **ChatChannel\[**\#**\]** | Returns the name of chat channel \# |
| [_int_](datatype-int.md) | **ChatChannels** | Returns the number of channels currently joined |
| \_\_[_string_](datatype-string.md)\_\_ | **Error** | Last normal error message |
| \_\_[_string_](datatype-string.md)\_\_ | **GameState** | Returns "INGAME, CHARSELECT, PRECHARSELECT, UNKNOWN" |
| \_\_[_string_](datatype-string.md)\_\_ | **LastCommand** | Last command entered |
| \_\_[_string_](datatype-string.md)\_\_ | **LastTell** | Name of last person to send you a tell |
| [_bool_](datatype-bool.md) | **LClickedObject** | Returns TRUE if an object has been left clicked |
| \_\_[_string_](datatype-string.md)\_\_ | **LoginName** | Your station name |
| [_int_](datatype-int.md) | **MouseX** | Mouse's X location |
| [_int_](datatype-int.md) | **MouseY** | Mouse's Y location |
| \_\_[_string_](datatype-string.md)\_\_ | **MQ2DataError** | Last MQ2Data parsing error message |
| \_\_[_string_](datatype-string.md)\_\_ | **Path** | Directory that Macroquest.exe launched from |
| [_int_](datatype-int.md) | **Ping** | Your current ping |
| [_int_](datatype-int.md) | **Running** | Running time of current MQ2 session, in milliseconds |
| \_\_[_string_](datatype-string.md)\_\_ | **Server** | Full name of your server |
| \_\_[_string_](datatype-string.md)\_\_ | **SyntaxError** | Last syntax error message |
| [_int_](datatype-int.md) | **ViewportX** | EverQuest viewport upper left \(X\) position |
| [_int_](datatype-int.md) | **ViewportXCenter** | EverQuest viewport center \(X\) position |
| [_int_](datatype-int.md) | **ViewportXMax** | EverQuest viewport lower right \(X\) position |
| [_int_](datatype-int.md) | **ViewportY** | EverQuest viewport upper left \(Y\) position |
| [_int_](datatype-int.md) | **ViewportYCenter** | EverQuest viewport center \(Y\) position |
| [_int_](datatype-int.md) | **ViewportYMax** | EverQuest viewport lower right \(Y\) position |
| \_\_[_string_](datatype-string.md)\_\_ | **To String** | None |

## Example

`/echo ${MacroQuest.Server}`

