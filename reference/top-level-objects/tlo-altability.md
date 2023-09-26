---
tags:
    - tlo
---
# `AltAbility`

!!! danger
    The AltAbility TLO should not be used except for when experimenting  with data. If you've already purchased the AA, use `Me.AltAbility`, which is tailored to your character and is much faster.

## Forms

| [_altability_](../data-types/datatype-altability.md) **AltAbility**[ _Number_ ] | Look up an AltAbility by its altability id |
| [_altability_](../data-types/datatype-altability.md) **AltAbility**[ _Name_ ] | Look up an AltAbility by its name |


## Example Usage

=== "MQScript"

    ```
    | Prints the pre-requisite AA ability needed to train Combat Stability
    /echo ${AltAbility[Combat Stability].RequiresAbility}
    ```

=== "Lua"

    ```lua
    -- Prints the pre-requisite AA ability needed to train Combat Stability
    print(mq.TLO.AltAbility('Combat Stability').RequiresAbility())
    ```
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
