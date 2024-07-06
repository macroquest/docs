---
tags:
    - tlo
---
# `NearestSpawn`

Object that is used in finding spawns nearest to you.

## Forms

### {{ renderMember(type='spawn', name='NearestSpawn', params='N') }}

:   The _Nth_ nearest spawn

### {{ renderMember(type='spawn', name='NearestSpawn', params='Search') }}

:   The nearest spawn matching this search string (see [Spawn Search]).

### {{ renderMember(type='spawn', name='NearestSpawn', params='N,Search') }}

:   The _Nth_ nearest spawn matching this search string (see [Spawn Search]).


## Usage

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
