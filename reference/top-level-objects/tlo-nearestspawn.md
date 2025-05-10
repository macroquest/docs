---
tags:
    - tlo
---
# `NearestSpawn`

<!--tlo-desc-start-->
Object that is used in finding spawns nearest to you.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='spawn', name='NearestSpawn', params='N') }}

:   The _Nth_ nearest spawn

### {{ renderMember(type='spawn', name='NearestSpawn', params='Search') }}

:   The nearest spawn matching this search string (see [Spawn Search]).

### {{ renderMember(type='spawn', name='NearestSpawn', params='N,Search') }}

:   The _Nth_ nearest spawn matching this search string (see [Spawn Search]).
<!--tlo-forms-end-->

## Usage

```
/echo ${NearestSpawn[npc radius 100 "orc pawn"]}
```

Finds the npc containing orc pawn in its name that is within 100 of you.

```
/echo ${NearestSpawn[2]}
```

Finds the closest spawn to you (`${NearestSpawn[1]}` will always match yourself).

<!--tlo-linkrefs-start-->
[spawn]: ../data-types/datatype-spawn.md
[Spawn Search]: ../general/spawn-search.md
<!--tlo-linkrefs-end-->
