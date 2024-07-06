---
tags:
    - datatype
---
# `invslot`

Data related to an inventory slot.

### Members

### {{ renderMember(type='int', name='ID') }}

:   ID of this item slot (usable directly by [/itemnotify](../../reference/commands/itemnotify.md))

### {{ renderMember(type='item', name='Item') }}

:   Item data for the item in this slot

### {{ renderMember(type='string', name='Name') }}

:   For inventory slots not inside packs, the slot name, otherwise NULL

### {{ renderMember(type='invslot', name='Pack') }}

:   Container that must be opened to access the slot with [/itemnotify](../../reference/commands/itemnotify.md)

### {{ renderMember(type='int', name='Slot') }}

:   Slot number inside the pack which holds the item, otherwise NULL

### [string][string] `To String`

:   Same as **ID**


## Example

!!! example
    Bag is a defined variable in a for loop in this case:

    === "MQScript"

        ```text
        /if (${InvSlot[pack${Bag}].Item.Item[${Slot}].NoDrop}) {
            /echo I found a No Drop Item: \ag${InvSlot[pack${Bag}].Item.Item[${Slot}].Name}
            /return
        }
        ```

    === "Lua"

        ```lua
        local item = mq.TLO.InvSlot("pack" .. Bag).Item.Item(Slot)
        if item.NoDrop() then
            printf("I found a No Drop Item: \ag%s\ax", item.Name())
            return
        end
        ```


[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[achievementobj]: datatype-achievementobj.md
[altability]: datatype-altability.md
[auratype]: datatype-auratype.md
[bandolieritem]: #bandolieritem-datatype
[bool]: datatype-bool.md
[buff]: datatype-buff.md
[class]: datatype-class.md
[double]: datatype-double.md
[dzmember]: datatype-dzmember.md
[fellowship]: datatype-fellowship.md
[fellowshipmember]: datatype-fellowshipmember.md
[float]: datatype-float.md
[ground]: datatype-ground.md
[heading]: datatype-heading.md
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[invslot]: datatype-invslot.md
[item]: datatype-item.md
[spawn]: datatype-spawn.md
[spell]: datatype-spell.md
[string]: datatype-string.md
[strinrg]: datatype-string.md
[ticks]: datatype-ticks.md
[time]: datatype-time.md
[timestamp]: datatype-timestamp.md
[window]: datatype-window.md
[worldlocation]: datatype-worldlocation.md
[xtarget]: datatype-xtarget.md
[zone]: datatype-zone.md
