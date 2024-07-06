---
tags:
    - tlo
---
# `AdvLoot`

The AdvLoot TLO grants access to items in the Advanced Loot window.

## Members

### {{ renderMember(type='itemfilterdata', name='Filter', params='ItemID') }}

:   Inspect the loot filter for a given ItemID.

### {{ renderMember(type='bool', name='LootInProgress') }}

:   True/False if looting from AdvLoot is in progress

### {{ renderMember(type='int', name='PCount') }}

:   item count from the Personal list

### {{ renderMember(type='advlootitem', name='PList', params='Index') }}

:   Inspect the item at the specified index in the personal loot list.

### {{ renderMember(type='int', name='PWantCount') }}

:   Want count from the Personal list (AN + AG + ND + GD)

### {{ renderMember(type='int', name='SCount') }}

:   Item count from the Shared list

### {{ renderMember(type='advlootitem', name='SList', params='Index') }}

:   Inspect the item at the specified index in the shared loot list.

### {{ renderMember(type='int', name='SWantCount') }}

:   Want count from the Shared list (AN + AG + ND + GD)


## datatype `advlootitem`

Represents a discrete item being looted in an AdvLoot window.

### {{ renderMember(type='bool', name='AlwaysGreed') }}

:   The Always Greed (AG) state of the item.

### {{ renderMember(type='bool', name='AlwaysNeed') }}

:   The Always Need (AN) state of the item.

### {{ renderMember(type='bool', name='AutoRoll') }}

:   The Auto Roll state (dice icon) of the item.

### {{ renderMember(type='spawn', name='Corpse') }}

:   The spawn representing the corpse that is being looted, if available.

### {{ renderMember(type='bool', name='FreeGrab') }}

:   Indicates that the item is free grab.

### {{ renderMember(type='bool', name='Greed') }}

:   The Greed (GD) state of the item.

### {{ renderMember(type='int', name='IconID') }}

:   The ID of the icon for the item.

### {{ renderMember(type='int64', name='ID') }}

:   The ID of the item.

### {{ renderMember(type='int', name='Index') }}

:   The positional index of the item.

### {{ renderMember(type='string', name='Name') }}

:   The name of the item.

### {{ renderMember(type='bool', name='Need') }}

:   The Need (ND) state of the item.

### {{ renderMember(type='bool', name='Never') }}

:   The Never (NV) state of the item.

### {{ renderMember(type='bool', name='No') }}

:   The No state of the item.

### {{ renderMember(type='bool', name='NoDrop') }}

:   Indicates if the item is NO DROP.

### {{ renderMember(type='int', name='StackSize') }}

:   The size of the stack of items being looted.

### [string][string] `To String`

:   Same as **Name**


## datatype `itemfilterdata`

A collection of settings that together describe the loot filter for an item.

### {{ renderMember(type='bool', name='AutoRoll') }}

:   The Auto Roll state (dice icon).

### {{ renderMember(type='bool', name='Greed') }}

:   The Greed (GD) state.

### {{ renderMember(type='int', name='IconID') }}

:   The ID of the icon.

### {{ renderMember(type='int', name='ID') }}

:   The ID of the item.

### {{ renderMember(type='string', name='Name') }}

:   The Name of the item.

### {{ renderMember(type='bool', name='Need') }}

:   The Need (ND) state.

### {{ renderMember(type='bool', name='Never') }}

:   The Never (NV) state.

### {{ renderMember(type='int', name='Types') }}

:   Bit field representing all the loot filter flags for this item.

### [string][string] `To String`

:   Same as **Name**


## Usage

=== "MQScript"

    ```
    | Echo the name of the first item in the personal loot list
    /echo ${AdvLoot.PList[1].Name}

    | Echo the number of items in the personal loot list.
    /echo There are ${AdvLoot.PCount} items in the personal loot list

    | Echo the stack size of the first item in the personal loot list.
    /echo The item in index 1 has a StackSize of ${AdvLoot.PList[1].StackSize}

    | If the first item in the shared loot list is marked as Need, then echo.
    /if (${AdvLoot.SList[1].Need}==TRUE) /echo I need that item!

    | Echo the NO DROP status of the first item in the personal loot list: TRUE or FALSE.
    /echo ${AdvLoot.PList[1].NoDrop}

    | Wait 10 seconds, or until AdvLoot is no longer in the process of looting.
    /delay 10s !${AdvLoot.LootInProgress}

    | Give the first item in the shared loot list to myself.
    /if (!${AdvLoot.LootInProgress}) {
        /echo Its safe to loot!
        /if (${AdvLoot.SCount}>=1) {
            /echo I am going to give 1 ${AdvLoot.SList[1].Name} to myself
            /advloot shared 1 giveto ${Me.Name} 1
        }
    } else {
        /echo Do something else, loot is already in progress...
    }
    ```

=== "Lua"

    ```lua
    -- Print the name of the first item in the personal loot list
    print(mq.TLO.AdvLoot.PList(1).Name())

    -- Print the number of items in the personal loot list
    print('There are ', mq.TLO.AdvLoot.PCount(), ' items in the personal loot list')

    -- Print the stack size of the first item in the personal loot list.
    print('The item in index 1 has a StackSize of ', mq.TLO.AdvLoot.PList(1).StackSize()))

    -- If the first item in the shared loot list is marked as Need, then print a message.
    if mq.TLO.AdvLoot.SList(1).Need() then
        print('I need that item!')
    end

    -- Print the NO DROP status of the first item in the personal loot list.
    print(mq.TLO.AdvLoot.PList(1).NoDrop())

    -- Wait 10 seconds, or until AdvLoot is no longer in the process of looting.
    mq.delay('10s', function() return not mq.TLO.AdvLoot.LootInProgress() end)

    -- Give the first item in the shared loot list to myself.
    if not mq.TLO.AdvLoot.LootInProgress() then
        print('Its safe to loot!')
        if mq.TLO.AdvLoot.SCount() >= 1 then
            print('I am going to give 1 ', mq.TLO.AdvLoot.SList(1).Name(), ' to myself')
            mq.cmdf('/advloot shared 1 giveto %s 1', mq.TLO.Me.Name())
        end
    else
        print('Do something else, loot is already in progress...')
    end
    ```

[int]: ../data-types/datatype-int.md
[string]: ../data-types/datatype-string.md
[bool]: ../data-types/datatype-bool.md
[int64]: ../data-types/datatype-int64.md
[spawn]: ../data-types/datatype-spawn.md
[itemfilterdata]: #datatype-itemfilterdata
[advlootitem]: #datatype-advlootitem
