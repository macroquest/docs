---
tags:
    - tlo
---
# `AdvLoot`

The AdvLoot TLO grants access to items in the Advanced Loot window.

## Members

### [itemfilterdata][itemfilterdata] `Filter[ItemID]`

:   Inspect the loot filter for a given ItemID.

### [bool][bool] `LootInProgress`

:   True/False if looting from AdvLoot is in progress

### [int][int] `PCount`

:   item count from the Personal list

### [advlootitem][advlootitem] `PList[Index]`

:   Inspect the item at the specified index in the personal loot list.

### [int][int] `PWantCount`

:   Want count from the Personal list (AN + AG + ND + GD)

### [int][int] `SCount`

:   Item count from the Shared list

### [advlootitem][advlootitem] `SList[Index]`

:   Inspect the item at the specified index in the shared loot list.

### [int][int] `SWantCount`

:   Want count from the Shared list (AN + AG + ND + GD)


## Associated DataTypes

### `advlootitem` Type

Represents a discrete item being looted in an AdvLoot window.

### [bool][bool] `AlwaysGreed`

:   The Always Greed (AG) state of the item.

### [bool][bool] `AlwaysNeed`

:   The Always Need (AN) state of the item.

### [bool][bool] `AutoRoll`

:   The Auto Roll state (dice icon) of the item.

### [spawn][spawn] `Corpse`

:   The spawn representing the corpse that is being looted, if available.

### [bool][bool] `FreeGrab`

:   Indicates that the item is free grab.

### [bool][bool] `Greed`

:   The Greed (GD) state of the item.

### [int][int] `IconID`

:   The ID of the icon for the item.

### [int64][int64] `ID`

:   The ID of the item.

### [int][int] `Index`

:   The positional index of the item.

### [string][string] `Name`

:   The name of the item.

### [bool][bool] `Need`

:   The Need (ND) state of the item.

### [bool][bool] `Never`

:   The Never (NV) state of the item.

### [bool][bool] `No`

:   The No state of the item.

### [bool][bool] `NoDrop`

:   Indicates if the item is NO DROP.

### [int][int] `StackSize`

:   The size of the stack of items being looted.

### [string][string] `To String`

:   Same as **Name**



### `itemfilterdata` Type

A collection of settings that together describe the loot filter for an item.

### [bool][bool] `AutoRoll`

:   The Auto Roll state (dice icon).

### [bool][bool] `Greed`

:   The Greed (GD) state.

### [int][int] `IconID`

:   The ID of the icon.

### [int][int] `ID`

:   The ID of the item.

### [string][string] `Name`

:   The Name of the item.

### [bool][bool] `Need`

:   The Need (ND) state.

### [bool][bool] `Never`

:   The Never (NV) state.

### [int][int] `Types`

:   Bit field representing all the loot filter flags for this item.

### [string][string] `To String`

:   Same as **Name**


## Usage Examples

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
[float]: datatype-float.md
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
[double]: datatype-double.md
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
