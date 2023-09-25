---
tags:
    - tlo
---
# `FindItemBankCount`

A TLO used to find a count of items in your bank by partial or exact name match. _See examples below._

## Forms

[_item_][item] **FindItemBankCount**[_name/id_]

:   Counts the items in your bank using the given item id, or partial name match.

    ??? example

        Echos the number of items in your bank with the name swirling in it.

        === "MQScript"

            ```
            /echo ${FindItemBankCount[swirling]}
            ```

        === "Lua"

            ```lua
            print(mq.TLO.FindItemBankCount("swirling"))
            ```


[_item_][item] **FindItemBankCount**[=_name_]

:   Counts the items in your bank using exact name match (case insensitive).

    ??? example

        Echoes the number of Swirling Shadows you have in your bank.

        === "MQScript"

            ```
            /echo ${FindItemBankCount[=Swirling Shadows]}
            ```

        === "Lua"

            ```lua
            print(mq.TLO.FindItemBankCount("=Swirling Shadows"))
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
