---
tags:
    - datatype
---
# `ground`

Represents a ground item.

## Members

### {{ renderMember(type='float', name='DisplayName') }} 

:   Displays name of the grounspawn

### {{ renderMember(type='int', name='Distance') }} 

:   Distance from player to ground item

### {{ renderMember(type='int', name='Distance3D') }} 

:   Distance from player to ground item

### {{ renderMember(type='heading', name='Heading') }} 

:   Ground item is facing this heading

### {{ renderMember(type='heading', name='HeadingTo') }} 

:   Direction player must move to meet this ground item

### {{ renderMember(type='int', name='ID') }} 

:   Ground item ID (not the same as item ID, this is like spawn ID)

### {{ renderMember(type='bool', name='LineOfSight') }} 

:   Returns TRUE if ground spawn is in line of sight

### {{ renderMember(type='string', name='Name') }} 

:   Name

### {{ renderMember(type='int', name='SubID') }} 

:   ???

### {{ renderMember(type='int', name='ZoneID') }} 

:   ???

### {{ renderMember(type='float', name='X') }} 

:   X coordinate

### {{ renderMember(type='float', name='Y') }} 

:   Y coordinate

### {{ renderMember(type='float', name='Z') }} 

:   Z coordinate

### {{ renderMember(type='float', name='W') }} 

:   X coordinate (Westward-positive)

### {{ renderMember(type='float', name='N') }} 

:   Y coordinate (Northward-positive)

### {{ renderMember(type='float', name='U') }} 

:   Z coordinate (Upward-positive)

### {{ renderMember(type='ground', name='First') }} 

:   First spawn

### {{ renderMember(type='ground', name='Last') }} 

:   Last spawn

### {{ renderMember(type='ground', name='Next') }} 

:   Next spawn

### {{ renderMember(type='ground', name='Prev') }} 

:   Prev spawn

### [string][string] `To String`

:   Same as ID


## Methods

| Name | Action |
| :--- | :--- |
| **DoFace** | Will cause the toon to face the called for spawn if it exists |
| **DoTarget** | Will cause the toon to target the called for spawn if it exists |
| **Grab** | Picks up the ground spawn |
| **Reset** | Clears the currently selected ground spawn |

## Examples

Extended the Ground TLO to accept searches

`/echo The closest ${Ground[brew].DisplayName} is ${Ground[brew].Distance3D} away from you.`

output: The closest Brew Barrel is 26.4 away from you.

Note that both of the search functions are case insensitive and are sorted by distance closest to you. The only acceptable parameter in the search filter is by name or partial name.

`/echo ${Ground[egg].Doface.Distance3D})` Will face the closest item on the ground which has the word "egg" in it. and then echo the distance to it in the mq2 window. well if it finds an item with the word "egg" in it on the ground that is, otherwise it will just echo NULL .DoFace does NOT target the ground item, it just faces it.

`/if (${Ground[egg].DoTarget.ID}) /echo we just targeted a ${Ground[egg]}`

Will target the closest item on the ground which has the word "egg" in it. and then echo the distance to it in the mq2 window.

`/if (${Ground[1].Doface.Distance3D}) /echo we just targeted a ${Ground[1].DisplayName}`

Will face the closest item on the ground. and then echo the distance to it in the mq2 window. well if it finds an groundspawn, otherwise it will just echo NULL .DoFace does NOT target the ground item, it just faces it.

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
