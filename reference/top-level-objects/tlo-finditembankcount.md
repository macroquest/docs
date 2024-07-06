---
tags:
    - tlo
---
# `FindItemBankCount`

A TLO used to find a count of items in your bank by partial or exact name match. _See examples below._

## Forms

### {{ renderMember(type='int', name='FindItemBankCount', params='name|id') }}

:   Counts the items in your bank using the given item id, or partial name match.

    ???+ example

        Echos the number of items in your bank with the name swirling in it.

        === "MQScript"

            ```
            /echo ${FindItemBankCount[swirling]}
            ```

        === "Lua"

            ```lua
            print(mq.TLO.FindItemBankCount("swirling"))
            ```


### {{ renderMember(type='int', name='FindItemBankCount', params='=name') }}

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


[int]: ../data-types/datatype-int.md
