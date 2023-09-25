---
tags:
    - datatype
---
# `invslot`

Data related to an inventory slot.

### Members

### [int][int] `ID`

:   ID of this item slot (usable directly by [/itemnotify](../../reference/commands/itemnotify.md))

### [item][item] `Item`

:   Item data for the item in this slot

### [string][string] `Name`

:   For inventory slots not inside packs, the slot name, otherwise NULL

### [invslot][invslot] `Pack`

:   Container that must be opened to access the slot with [/itemnotify](../../reference/commands/itemnotify.md)

### [int][int] `Slot`

:   Slot number inside the pack which holds the item, otherwise NULL

### [string][string] `To String`

:   Same as **ID**


## Example

Bag is a defined variable in a for loop in this case:

```text
/if (${InvSlot[pack${Bag}].Item.Item[${Slot}].NoDrop}) {
    /echo I found a No Drop Item: \ag${InvSlot[pack${Bag}].Item.Item[${Slot}].Name}
    /return
}
```

[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
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
