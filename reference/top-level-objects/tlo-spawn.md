---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Spawn`

## Description

Object used to get information on a specific spawn. Uses the filters under [Spawn Search].

## Forms

[_spawn_][spawn] **Spawn**[_N_]

:   Spawn matching ID _N_.

[_spawn_][spawn] **Spawn**[_search string_]

:   Any spawns matching _search string_. See [Spawn Search].

## Examples

```
/echo ${Spawn[1000]}
```

Displays the name of the spawn with id number 1000.

```
/target ${Spawn[npc radius 500 trakanon]}
```

Targets the npc with the name Trakanon only if within a radius of 500.

[spawn]: ../data-types/datatype-spawn.md
[Spawn Search]: ../../reference/general/spawn-search.md
