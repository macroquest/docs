---
tags:
    - tlo
---
# `FindItemCount`

A TLO used to find a count of items on your character, corpse, or a merchant by partial or exact name match. _See examples below._

## Forms

[_item_][item] **FindItemCount**[_name/id_]

:   Counts the items using the given item id, or partial name match. Will search character
    inventory and any items stored in key rings (illusion, mount, etc).

    ??? example

        Echos the number of items in your inventory with the name swirling in it.

        === "MQScript"

            ```
            /echo ${FindItemCount[swirling]}
            ```

        === "Lua"

            ```lua
            print(mq.TLO.FindItemCount("swirling"))
            ```


[_item_][item] **FindItemCount**[=_name_]

:   Counts the items using exact name match (case insensitive). Will search character inventory
    and any items stored in key rings (illusion, mount, etc).

    ??? example

        Echoes the number of Water Flasks you have in your inventory.

        === "MQScript"

            ```
            /echo ${FindItemCount[=Water Flask]}
            ```

        === "Lua"

            ```lua
            print(mq.TLO.FindItemCount("=Water Flask"))
            ```


[item]: ../data-types/datatype-item.md
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
