---
tags:
    - datatype
---
# `fellowship`

Contains all the data about your fellowship

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_](datatype-bool.md) | **Campfire** | TRUE if campfire is up, FALSE if not |
| [_ticks_](datatype-ticks.md) | **CampfireDuration** | Time left on current campfire |
| [_float_](datatype-float.md) | **CampfireX** | Campfire X location |
| [_float_](datatype-float.md) | **CampfireY** | Campfire Y location |
| [_float_](datatype-float.md) | **CampfireZ** | Campfire Z location |
| [_zone_](datatype-zone.md) | **CampfireZone** | Zone information for the zone that contains your campfire |
| [_bool_](datatype-bool.md) | **Exists** | Returns TRUE if a fellowship exists. |
| [_int_](datatype-int.md) | **ID** | Fellowship ID |
| [_string_](datatype-string.md) | **Leader** | Fellowship leader's name |
| [_fellowshipmember_](datatype-fellowshipmember.md) | **Member**[ _name\|#_ ] | Member data by _name_ or _#_ |
| [_int_](datatype-int.md) | **Members** | Number of members in the fellowship |
| [_string_](datatype-string.md) | **MotD** | Fellowship Message of the Day |
| [_bool_](datatype-bool.md) | **Sharing**[ _N_ ] | Returns TRUE if exp sharing is enabled for the Nth member|
| [_string_](datatype-string.md) | **To String** | TRUE if currently in a fellowship, FALSE if not |


## Changelog

* May 13, 2022: Added Exists
* December 3rd, 2020: Added Sharing
