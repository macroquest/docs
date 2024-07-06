---
tags:
    - datatype
---
# `range`

This DataType performs a simple test on _n_ using the following members.

## Members

### {{ renderMember(type='bool', name='Between', params='#1,#2:N') }}

:   True if _N_ is between the range of _#1_ and _#2_, inclusive.

    ???+ Example

        Is 50 between 33 and 66? `${Range.Between[33,66:50]}` returns TRUE

        Is 25 between 33 and 66? `${Range.Between[33,66:25]}` returns FALSE

### {{ renderMember(type='bool', name='Inside', params='#1,#2:N') }}

:   True if _N_ is within the range of _#1_ and _#2_, exclusive.

    ???+ Example

        Is 50 Inside 33 and 66? `${Range.Inside[33,66:50]}` returns TRUE

        Is 33 inside 33 and 66? `${Range.Inside[33,66:33]}` returns FALSE

[bool]: datatype-bool.md
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
