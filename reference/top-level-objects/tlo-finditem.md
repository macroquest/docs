---
tags:
    - tlo
---
# `FindItem`

A TLO used to find an item on your character, corpse, or a merchant by partial or exact name match. _See examples below._

## Forms

[_item_][item] **FindItem**[_name/id_]

:   Search for an item using the given item id, or partial name match. Will search character
    inventory and any items stored in key rings (illusion, mount, etc).

    ??? example

        Looks for an item with the name swirling in it, and prints the ID.

        === "MQScript"

            ```
            /echo ${FindItem[swirling].ID}
            ```

        === "Lua"

            ```lua
            print(mq.TLO.FindItem("swirling").ID())
            ```


[_item_][item] **FindItem**[=_name_]

:   Search for an item using exact name match (case insensntive). Will search character inventory
    and any items stored in key rings (illusion, mount, etc).

    ??? example

        Looks for the Cleric Epic (by exact match) and prints its ID.

        === "MQScript"

            ```
            /echo ${FindItem[=Water Sprinkler of Nem Ankh].ID}
            ```

        === "Lua"

            ```lua
            print(mq.TLO.FindItem("=Water Sprinkler of Nem Ankh").ID())
            ```


[item]: ../data-types/datatype-item.md
