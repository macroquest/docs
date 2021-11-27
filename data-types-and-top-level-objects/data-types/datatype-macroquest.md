# DataType:macroquest

Data types related to the current MacroQuest2 session.  These also inherit from the EverQuest Type.

## Members

| **Type**                           | **Member**        | **Description**                                                                                                                                   |
| ---------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| [_int_](datatype-int.md)           | **Build**         | The build number for MQ2Main.dll                                                                                                                  |
| __[_string_](datatype-string.md)__ | **BuildDate**     | Date that MQ2Main.dll was built                                                                                                                   |
| __[_string_](datatype-string.md)__ | **Error**         | Last normal error message                                                                                                                         |
| [_string_](datatype-string.md)__   | **InternalName**  | The internal name from MQ2Main.dll ("Next")                                                                                                       |
| [_string_](datatype-string.md)__   | **MQ2DataError**  | Last MQ2Data parsing error message                                                                                                                |
| [_int_](datatype-int.md)           | **Parser**        | Which parser engine is currently active                                                                                                           |
| __[_string_](datatype-string.md)__ | **Path\[Option]** | Directory that Macroquest.exe launched from.  When passed root/config/crashdumps/logs/mqini/macros/plugins/resources, returns the respective path |
| __[_string_](datatype-string.md)__ | **SyntaxError**   | Last syntax error message                                                                                                                         |
| [_string_](datatype-string.md)__   | **Version**       | The full version of MQ2Main.dll                                                                                                                   |
| __[_string_](datatype-string.md)__ | **To String**     | None                                                                                                                                              |

## Example

`/echo ${MacroQuest.Path[config]}`
