---
tags:
    - tlo
---
# `LastSpawn`

<!--tlo-desc-start-->
Information about the spawns that have occurred since you entered the zone. When you enter a zone you dont know the spawn order of anything already there, just anything that spawns while you are in the zone.

The useful thing about `${LastSpawn[-1]}` is just being able to get the first spawn in the list which you might use in conjunction with other spawn members to go through the entire spawn list in a loop.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='spawn', name='LastSpawn', params='N') }}

:   The nth latest spawn (chronological order)

### {{ renderMember(type='spawn', name='LastSpawn', params='-N') }}

:   The nth oldest spawn (chronological order)
<!--tlo-forms-end-->

## Usage

```
/echo ${LastSpawn[10].ID}
```

Echos the spawnID of the 10th mob to spawn in the zone

```
/echo ${LastSpawn[-10]}
```

Echos the name of the 10th to last spawn in the zone
<!--tlo-linkrefs-start-->
[spawn]: ../data-types/datatype-spawn.md
<!--tlo-linkrefs-end-->
