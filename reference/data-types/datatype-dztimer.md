---
tags:
    - datatype
---
# `dztimer`

<!--dt-desc-start-->
Provides information about a dynamic zone lockout timer

See Also: [DataType:dynamiczone](./datatype-dynamiczone.md), [TLO:DynamicZone](../top-level-objects/tlo-dynamiczone.md)
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | string ExpeditionName
The name of the expedition
///

/// member | string EventName
The name of the event
///

/// member | timestamp Timer
The timestamp indicating when this lockout expires
///

/// member | int EventID
ID of the event. These values are only unique per Expedition. Non-event lockouts (Replay Timer) will have a -1 event id.
///

### [string][string] `To String`

:   Returns the string formatted as `"ExpeditionName|EventName"` |
<!--dt-members-end-->
### Changelog

* July 9th, 2021: Initial version
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
[timestamp]: datatype-timestamp.md
<!--dt-linkrefs-end-->
