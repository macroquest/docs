---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
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
