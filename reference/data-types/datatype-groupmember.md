---
tags:
    - datatype
---
# `groupmember`

Contains data on a specific group member

## Members

this type inherits members from [_spawn_ ](datatype-spawn.md)if the member is in the current zone.

### [int][int] `Index`

:   Which number in the group the member is

### [bool][bool] `Leader`

:   TRUE if the member is the group's leader, FALSE otherwise

### [int][int] `Level`

:   The member's level

### [bool][bool] `MainAssist`

:   TRUE if the member is designated as the group's Main Assist, FALSE otherwise

### [bool][bool] `MainTank`

:   TRUE if the member is designated as the group's Main Tank, FALSE otherwise

### [bool][bool] `Mercenary`

:   TRUE if the member is a mercenary, FALSE otherwise

### [string][string] `Name`

:   The name of the group member. This works even if they are not in the same zone as you.

### [bool][bool] `Offline`

:   TRUE if the member is offline and FALSE if online

### [bool][bool] `OtherZone`

:   TRUE if the member is online but in another zone and FALSE if online and in same zone as you.

### [bool][bool] `Present`

:   TRUE if the member is online and in same zone and FALSE if online and not in same zone as you.

### [bool][bool] `Puller`

:   TRUE if the member is designated as the group's Puller, FALSE otherwise

### [spawn][spawn] `Spawn`

:   Accesses the group member's spawn. Not all members will have a spawn (if they are out of the zone).

### [string][string] `To String`

:   Same as **Name**


## Examples

`/echo ${Group.Member[0].Leader}`

Echo TRUE if you are Group Leader.

`/echo ${Group.Member[3].Puller}`

Echo TRUE if Group Member 3 is marked as Role Puller

[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
[zone]: datatype-zone.md
[fellowshipmember]: datatype-fellowshipmember.md
[class]: datatype-class.md
[heading]: datatype-heading.md
[ground]: datatype-ground.md
