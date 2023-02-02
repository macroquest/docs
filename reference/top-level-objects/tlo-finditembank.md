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

:   Search for an item in your bank using exact name match (case insensntive).

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
