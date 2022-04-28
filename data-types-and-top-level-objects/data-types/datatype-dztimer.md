# DataType:dztimer

Provides information about a dynamic zone lockout timer

## Members

| Type | Name | Description |
| :--- | :--- | :--- |
| \_\_[_string_](datatype-string.md)\_\_ | **ExpeditionName** | The name of the expedition |
| \_\_[_string_](datatype-string.md)\_\_ | **EventName** | The name of the event |
| \_\_[_timestamp_](datatype-timestamp.md)\_\_ | **Timer** | The timestamp indicating when this lockout expires |
| \_\_[_int_](datatype-int.md)\_\_ | **EventID** | ID of the event. These values are only unique per Expedition. Non-event lockouts (Replay Timer) will have a -1 event id. |
| [_string_](datatype-string.md)\_\_ | **To String** | Returns the string formatted as `ExpeditionName|EventName` |

### Changelog

* July 9th, 2021: Initial version



