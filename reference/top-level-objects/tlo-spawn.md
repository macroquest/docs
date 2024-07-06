---
tags:
    - tlo
---
# `Spawn`

Object used to get information on a specific spawn. Uses the filters under [Spawn Search].

## Forms

### {{ renderMember(type='spawn', name='Spawn', params='N') }}

:   Spawn matching ID _N_.

### {{ renderMember(type='spawn', name='Spawn', params='SearchString') }}

:   Any spawns matching `SearchString`. See [Spawn Search].


## Usage

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
