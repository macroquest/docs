---
tags:
    - datatype
---
# `fellowship`

Contains all the data about your fellowship

## Members

### [bool][bool] `Campfire`

:   TRUE if campfire is up, FALSE if not

### [ticks][ticks] `CampfireDuration`

:   Time left on current campfire

### [float][float] `CampfireX`

:   Campfire X location

### [float][float] `CampfireY`

:   Campfire Y location

### [float][float] `CampfireZ`

:   Campfire Z location

### [zone][zone] `CampfireZone`

:   Zone information for the zone that contains your campfire

### [bool][bool] `Exists`

:   Returns TRUE if a fellowship exists.

### [int][int] `ID`

:   Fellowship ID

### [string][string] `Leader`

:   Fellowship leader's name

### [fellowshipmember][fellowshipmember] `Member[name|#]`

:   Member data by _name_ or _#_

### [int][int] `Members`

:   Number of members in the fellowship

### [string][string] `MotD`

:   Fellowship Message of the Day

### [bool][bool] `Sharing[N]`

:   Returns TRUE if exp sharing is enabled for the Nth member

### [string][string] `To String`

:   TRUE if currently in a fellowship, FALSE if not



## Changelog

* May 13, 2022: Added Exists
* December 3rd, 2020: Added Sharing
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
