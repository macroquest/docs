---
tags:
    - tlo
---
# `SpawnCount`

<!--tlo-desc-start-->
Object used to count spawns based on a set of queries. Uses the filters under [Spawn Search].
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='int', name='SpawnCount') }}

:   Total number of spawns in current zone


### {{ renderMember(type='int', name='SpawnCount', params='SearchString') }}

:   Total number of spawns in current zone matching the `SearchString`. See [Spawn Search].
<!--tlo-forms-end-->

## Usage

```
/echo ${SpawnCount}
```

Displays the count of all spawns.

```
/echo ${SpawnCount[range 45 50]}
```

Displays the count of all spawns in the level range of 45 to 50.

```
/echo ${SpawnCount[npc radius 100]}
```

Displays count of all NPCs within a radius of 100.

<!--tlo-linkrefs-start-->
[int]: ../data-types/datatype-int.md
[Spawn Search]: ../../reference/general/spawn-search.md
<!--tlo-linkrefs-end-->
