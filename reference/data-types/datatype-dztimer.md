---
tags:
    - datatype
---

# `dztimer`

Provides information about a dynamic zone lockout timer

See Also: [DataType:dynamiczone](./datatype-dynamiczone.md), [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)

## Members

| Type | Name | Description |
| :--- | :--- | :--- |
| [_string_](datatype-string.md) | **ExpeditionName** | The name of the expedition |
| [_string_](datatype-string.md) | **EventName** | The name of the event |
| [_timestamp_](datatype-timestamp.md) | **Timer** | The timestamp indicating when this lockout expires |
| [_int_](datatype-int.md) | **EventID** | ID of the event. These values are only unique per Expedition. Non-event lockouts (Replay Timer) will have a -1 event id. |
| [_string_](datatype-string.md) | **To String** | Returns the string formatted as `"ExpeditionName|EventName"` |

### Changelog

* July 9th, 2021: Initial version
