---
tags:
    - tlo
---
# `NearestSpawn`

Object that is used in finding spawns nearest to you.

## Forms

[_spawn_][spawn] **NearestSpawn**[_N_]

:   The _Nth_ nearest spawn

[_spawn_][spawn] **NearestSpawn**[_search_]

:   The nearest spawn matching this search string (see [Spawn Search]).

[_spawn_][spawn] **NearestSpawn**[_N_,_search_]

:   The _Nth_ nearest spawn matching this search string (see [Spawn Search]).

## Examples

```
/echo ${NearestSpawn[npc radius 100 "orc pawn"]}
```

Finds the npc containing orc pawn in its name that is within 100 of you.

```
/echo ${NearestSpawn[2]}
```

Finds the closest spawn to you (`${NearestSpawn[1]}` will always match yourself).


[spawn]: ../data-types/datatype-spawn.md
[Spawn Search]: ../general/spawn-search.md
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
