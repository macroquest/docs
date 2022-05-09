# DataType:macroquest

Data types related to the current MacroQuest2 session.  These also inherit from the [EverQuest Type](datatype-everquest.md).

## Members

| **Type**                           | **Member**        | **Description**                                                                                                                                   |
| ---------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| [_int_](datatype-int.md)           | **Build**         | The build number for MQ2Main.dll                                                                                                                  |
| [_string_](datatype-string.md)     | **BuildDate**     | Date that MQ2Main.dll was built                                                                                                                   |
| [_string_](datatype-string.md)     | **Error**         | Last normal error message                                                                                                                         |
| [_string_](datatype-string.md)     | **InternalName**  | The internal name from MQ2Main.dll ("Next")                                                                                                       |
| [_string_](datatype-string.md)     | **MQ2DataError**  | Last MQ2Data parsing error message                                                                                                                |
| [_int_](datatype-int.md)           | **Parser**        | Which parser engine is currently active                                                                                                           |
| [_string_](datatype-string.md)     | **Path**[_Option_] | Directory that Macroquest.exe launched from.  When passed root/config/crashdumps/logs/mqini/macros/plugins/resources, returns the respective path |
| [_string_](datatype-string.md)     | **SyntaxError**   | Last syntax error message                                                                                                                         |
| [_string_](datatype-string.md)     | **Version**       | The full version of MQ2Main.dll                                                                                                                   |
| [_string_](datatype-string.md)     | **To String**     | None                                                                                                                                              |

## Example

`/echo ${MacroQuest.Path[config]}`
