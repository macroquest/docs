---
tags:
    - tlo
---
# `Plugin`

Object that has access to members that provide information on a plugin.

## Forms

[_plugin_][plugin] **Plugin**[_name_]

:   Finds plugin by name, uses full name match, case insensitive.

[_plugin_][plugin] **Plugin**[_N_] 

:   Plugin by index, starting with 1 and stopping whenever the list runs out of plugins.


## Examples

To see if a plugin is loaded:

=== "MQScript"

    ```
    /if (${Plugin[MQ2MoveUtils].IsLoaded}) {
        /echo MQ2MoveUtils plugin is loaded!
    }
    ```

=== "Lua"

    ```lua
    if mq.TLO.Plugin('MQ2MoveUtils').IsLoaded() then
        print('MQ2MoveUtils plugin is loaded!')
    end
    ```

To load a plugin if needed:

=== "MQScript"

    ```
    /if (!${Plugin[MQ2MoveUtils].IsLoaded}) {
        /plugin MQ2MoveUtils noauto
        /if (!${Plugin[MQ2MoveUtils].IsLoaded}) {
            /echo To Use this macro you need to have MQ2MoveUtils Loaded
            /endmacro
        }
    }
    ```

[plugin]: ../data-types/datatype-plugin.md[int]: ../data-types/datatype-int.md
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
