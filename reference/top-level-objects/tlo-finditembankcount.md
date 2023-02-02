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
