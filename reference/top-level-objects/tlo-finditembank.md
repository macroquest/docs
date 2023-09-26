---
tags:
    - tlo
---
# `FindItemBank`

A TLO used to find an item in your bank by partial or exact name match. _See examples below._

Of note: The FindItemBank with ItemSlot REQUIRES that bank item containers be open to function correctly. Due to potential exploits the command will not work if the bank containers are closed. This is in contrast to FindItem functionality with character containers, where ItemSlot was designed to allow inventory management without opening containers.

## Forms

[_item_][item] **FindItemBank**[_name/id_]

:   Search for an item in your bank using the given item id, or partial name match.

    ??? example

        Looks for an item in your bank with the name swirling in it, and prints the ID.

        === "MQScript"

            ```
            /echo ${FindItemBank[swirling].ID}
            ```

        === "Lua"

            ```lua
            print(mq.TLO.FindItemBank("swirling").ID())
            ```


[_item_][item] **FindItemBank**[=_name_]

:   Search for an item in your bank using exact name match (case insensitive).

    ??? example

        Looks for the Cleric Epic (by exact match) in your bank and prints its ID.

        === "MQScript"

            ```
            /echo ${FindItemBank[=Water Sprinkler of Nem Ankh].ID}
            ```

        === "Lua"

            ```lua
            print(mq.TLO.FindItemBank("=Water Sprinkler of Nem Ankh").ID())
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
