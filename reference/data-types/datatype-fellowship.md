---
tags:
    - datatype
---
# `fellowship`

<!--dt-desc-start-->
Contains all the data about your fellowship
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | bool Campfire
TRUE if campfire is up, FALSE if not
///

/// member | ticks CampfireDuration
Time left on current campfire
///

/// member | float CampfireX
Campfire X location
///

/// member | float CampfireY
Campfire Y location
///

/// member | float CampfireZ
Campfire Z location
///

/// member | zone CampfireZone
Zone information for the zone that contains your campfire
///

/// member | bool Exists
Returns TRUE if a fellowship exists.
///

/// member | int ID
Fellowship ID
///

/// member | string Leader
Fellowship leader's name
///

/// member | fellowshipmember Member[name|#]
Member data by _name_ or _#_
///

/// member | int Members
Number of members in the fellowship
///

/// member | string MotD
Fellowship Message of the Day
///

/// member | bool Sharing[N]
Returns TRUE if exp sharing is enabled for the Nth member
///

### [string][string] `To String`

:   TRUE if currently in a fellowship, FALSE if not
<!--dt-members-end-->

## Changelog

* May 13, 2022: Added Exists
* December 3rd, 2020: Added Sharing
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[fellowshipmember]: datatype-fellowshipmember.md
[float]: datatype-float.md
[int]: datatype-int.md
[string]: datatype-string.md
[ticks]: datatype-ticks.md
[zone]: datatype-zone.md
<!--dt-linkrefs-end-->
