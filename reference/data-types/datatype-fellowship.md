---
tags:
    - datatype
---
# `fellowship`

Contains all the data about your fellowship

## Members

### {{ renderMember(type='bool', name='Campfire') }} 

:   TRUE if campfire is up, FALSE if not

### {{ renderMember(type='ticks', name='CampfireDuration') }} 

:   Time left on current campfire

### {{ renderMember(type='float', name='CampfireX') }} 

:   Campfire X location

### {{ renderMember(type='float', name='CampfireY') }} 

:   Campfire Y location

### {{ renderMember(type='float', name='CampfireZ') }} 

:   Campfire Z location

### {{ renderMember(type='zone', name='CampfireZone') }} 

:   Zone information for the zone that contains your campfire

### {{ renderMember(type='bool', name='Exists') }} 

:   Returns TRUE if a fellowship exists.

### {{ renderMember(type='int', name='ID') }} 

:   Fellowship ID

### {{ renderMember(type='string', name='Leader') }} 

:   Fellowship leader's name

### {{ renderMember(type='fellowshipmember', name='Member', params='name|#') }} 

:   Member data by _name_ or _#_

### {{ renderMember(type='int', name='Members') }} 

:   Number of members in the fellowship

### {{ renderMember(type='string', name='MotD') }} 

:   Fellowship Message of the Day

### {{ renderMember(type='bool', name='Sharing', params='N') }} 

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
