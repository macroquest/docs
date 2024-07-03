---
tags:
    - datatype
---
# `raid`

Contains data on the current raid

## Members

### {{ renderMember(type='float', name='AverageLevel') }} 

:   Average level of raid members (more accurate than in the window)

### {{ renderMember(type='bool', name='Invited') }} 

:   Have I been invited to the raid?

### {{ renderMember(type='raidmember', name='Leader') }} 

:   Raid leader

### {{ renderMember(type='bool', name='Locked') }} 

:   Returns TRUE if the raid is locked

### {{ renderMember(type='string', name='Looter', params='#') }} 

:   Specified looter name by number

### {{ renderMember(type='int', name='Looters') }} 

:   Number of specified looters

### {{ renderMember(type='int', name='LootType') }} 

:   <p>Loot type number:</p><ul><li>1 = Leader</li><li>2 = Leader & GroupLeader</li><li>3 = Leader & Assignments</li></ul>

### {{ renderMember(type='raidmember', name='MainAssist') }} 

:   Raid main assist

### {{ renderMember(type='raidmember', name='MarkNpc') }}

:   Raid NPC marker

### {{ renderMember(type='raidmember', name='MasterLooter') }} 

:   Raid Master Looter

### {{ renderMember(type='raidmember', name='Member', params='N') }} 

:   Raid member by number _N_

### {{ renderMember(type='raidmember', name='Member', params='name') }} 

:   Raid member by _name_.

### {{ renderMember(type='int', name='Members') }} 

:   Total number of raid members

### {{ renderMember(type='raidmember', name='Target') }} 

:   Raid target (clicked in raid window)

### {{ renderMember(type='int', name='TotalLevels') }} 

:   Sum of all raid member's levels

| [_string_](datatype-string.md) | **(To String)** | None
[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: ../data-types/datatype-spell.md
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
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[double]: datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
[raidmember]: datatype-raidmember.md
