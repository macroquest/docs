---
tags:
    - tlo
---
# `Spawn`

<!--tlo-desc-start-->
Object used to get information on a specific spawn. Uses the filters under [Spawn Search].
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='spawn', name='Spawn', params='N') }}

:   Spawn matching ID _N_.

### {{ renderMember(type='spawn', name='Spawn', params='SearchString') }}

:   Any spawns matching `SearchString`. See [Spawn Search].
<!--tlo-forms-end-->

## Usage

```
/echo ${Spawn[1000]}
```

Displays the name of the spawn with id number 1000.

```
/target ${Spawn[npc radius 500 trakanon]}
```

Targets the npc with the name Trakanon only if within a radius of 500.
<!--tlo-linkrefs-start-->
[spawn]: ../data-types/datatype-spawn.md
[Spawn Search]: ../../reference/general/spawn-search.md
<!--tlo-linkrefs-end-->
