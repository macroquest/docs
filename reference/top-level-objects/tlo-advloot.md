# TLO:AdvLoot

The AdvLoot TLO grants access to items in the Advanced Loot window.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_itemfilterdata_](#itemfilterdata-type) | **Filter**[ _ItemID_ ] | Inspect the loot filter for a given ItemID. |
| [_bool_](../data-types/datatype-bool.md) | **LootInProgress** | True/False if looting from AdvLoot is in progress |
| [_int_](../data-types/datatype-int.md) | **PCount** | item count from the Personal list |
| [_advlootitem_](#advlootitem-type) | **PList**[ _Index_ ] | Inspect the item at the specified index in the personal loot list. |
| [_int_](../data-types/datatype-int.md) | **PWantCount** | Want count from the Personal list (AN + AG + ND + GD) |
| [_int_](../data-types/datatype-int.md) | **SCount** | Item count from the Shared list |
| [_advlootitem_](#advlootitem-type) | **SList**[ _Index_ ] | Inspect the item at the specified index in the shared loot list. |
| [_int_](../data-types/datatype-int.md) | **SWantCount** | Want count from the Shared list (AN + AG + ND + GD) |

## Associated  DataTypes

### `advlootitem` Type

Represents a discrete item being looted in an AdvLoot window.

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_](../data-types/datatype-bool.md) | **AlwaysGreed** | The Always Greed (AG) state of the item. |
| [_bool_](../data-types/datatype-bool.md) | **AlwaysNeed** | The Always Need (AN) state of the item. |
| [_bool_](../data-types/datatype-bool.md) | **AutoRoll** | The Auto Roll state (dice icon) of the item. |
| [_spawn_](../data-types/datatype-spawn.md) | **Corpse** | The spawn representing the corpse that is being looted, if available. |
| [_bool_](../data-types/datatype-bool.md) | **Greed** | The Greed (GD) state of the item. |
| [_int_](../data-types/datatype-int.md) | **IconID** | The ID of the icon for the item. |
| [_int_](../data-types/datatype-int.md) | **ID** | The ID of the item. |
| [_int_](../data-types/datatype-int.md) | **Index** | The positional index of the item. |
| [_string_](../data-types/datatype-string.md) | **Name** | The name of the item. |
| [_bool_](../data-types/datatype-bool.md) | **Need** | The Need (ND) state of the item. |
| [_bool_](../data-types/datatype-bool.md) | **Never** | The Never (NV) state of the item. |
| [_bool_](../data-types/datatype-bool.md) | **No** | The No state of the item. |
| [_bool_](../data-types/datatype-bool.md) | **NoDrop** | Indicates if the item is NO DROP. |
| [_int_](../data-types/datatype-int.md) | **StackSize** | The size of the stack of items being looted. |
| [_string_](../data-types/datatype-string.md) | **To String** | Same as **Name** |


### `itemfilterdata` Type

A collection of settings that together describe the loot filter for an item.

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_](../data-types/datatype-bool.md) | **AutoRoll** | The Auto Roll state (dice icon). |
| [_bool_](../data-types/datatype-bool.md) | **Greed** | The Greed (GD) state.|
| [_int_](../data-types/datatype-int.md) | **IconID** | The ID of the icon. |
| [_int_](../data-types/datatype-int.md) | **ID** | The ID of the item. |
| [_string_](../data-types/datatype-string.md) | **Name** | The Name of the item. |
| [_bool_](../data-types/datatype-bool.md) | **Need** | The Need (ND) state. |
| [_bool_](../data-types/datatype-bool.md) | **Never** | The Never (NV) state. |
| [_int_](../data-types/datatype-int.md) | **Types** | Bit field representing all the loot filter flags for this item. |
| [_string_](../data-types/datatype-string.md) | **To String** | Same as **Name** |

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
