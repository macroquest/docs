---
tags:
    - tlo
---
# `Zone`

Used to find information about a particular zone.

## Forms

[_currentzone_][currentzone] **Zone**

:   Retrieves the current zone information

[_zone_][zone] **Zone**[_N_]

:   Retrieves information about a zone by zone ID. If this zone is the current zone, then
    this will return [currentzone].

[_zone_][zone] **Zone**[_shortname_]

:   Retrieves information about a zone by short name. If this zone is the current zone, then
    this will return [currentzone].

## Examples

```
/echo ${Zone.Type}
```

Returns an integer representing the zone you are currently in.

```
/echo ${Zone.Indoor}
```

Returns TRUE if you're indoors, FALSE if not.

```
/echo ${Zone[zonename].ID}
```

Returns the ID of _zonename_, even if you aren't in the zone.

```
/echo ${Zone[zoneid].ShortName}
```

Returns the short name of the zone with ID _zoneid_.


[zone]: ../data-types/datatype-zone.md
[currentzone]: ../data-types/datatype-currentzone.md
[int]: ../data-types/datatype-int.md
[string]: ../data-types/datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: ../data-types/datatype-bool.md
[time]: datatype-time.md
[achievement]: ../data-types/datatype-achievement.md
[achievementcat]: ../data-types/datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: ../data-types/datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: ../data-types/datatype-float.md
[buff]: datatype-buff.md
[spawn]: ../data-types/datatype-spawn.md
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
[double]: ../data-types/datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
[raidmember]: datatype-raidmember.md
[body]: datatype-body.md
[cachedbuff]: datatype-cachedbuff.md
[deity]: datatype-deity.md
[race]: datatype-race.md
[taskmember]: datatype-task.md
[achievementmgr]: #achievementmgr-type
[itemfilterdata]: #itemfilterdata-type
[advlootitem]: #advlootitem-type
[alert]: #alert-type
[alertlist]: #alertlist-type
[friends]: #friends-type
