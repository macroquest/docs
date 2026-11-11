---
tags:
    - datatype
---
# `switch`

<!--dt-desc-start-->
Data related to switches (levers, buttons, etc) in the zone
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | heading DefaultHeading
Heading of "closed" switch
///

/// member | float DefaultX
X coordinate of "closed" switch
///

/// member | float DefaultY
Y coordinate of "closed" switch
///

/// member | float DefaultZ
Z coordinate of "closed" switch
///

/// member | float Distance
Distance from player to switch in (x,y)
///

/// member | float Distance3D
Distance from player to switch in (x,y,z)
///

/// member | heading Heading
Switch is facing this heading
///

/// member | heading HeadingTo
Direction player must move to meet this switch
///

/// member | int ID
Switch ID
///

/// member | bool IsTargeted
Returns TRUE if the switch is targeted
///

/// member | bool LineOfSight
Returns TRUE if the switch is in LoS
///

/// member | string Name
Name
///

/// member | bool Open
True if the switch is in the "open" state (State == 1)
///

/// member | int State
The "state" of the switch.
///

/// member | float X
X coordinate
///

/// member | float Y
Y coordinate
///

/// member | float Z
Z coordinate
///

/// member | string ToString
Same as **ID**
///
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[float]: datatype-float.md
[heading]: datatype-heading.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
