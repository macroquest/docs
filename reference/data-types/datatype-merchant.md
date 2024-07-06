---
tags:
    - datatype
---
# `merchant`

This contains information related to the active merchant.

## Members

This type inherits members from [_spawn_](datatype-spawn.md) if a merchant is active.

### {{ renderMember(type='bool', name='Full') }} 

:   Returns True if the merchant's inventory is full.

### {{ renderMember(type='item', name='Item', params='#') }} 

:   Item number _#_ on the merchant's list.

### {{ renderMember(type='item', name='Item', params='name') }} 

:   Find an item by partial name on the merchant's list. Prefix with "=" for an exact match.

### {{ renderMember(type='int', name='Items') }} 

:   Number of items on the merchant.

### {{ renderMember(type='bool', name='ItemsReceived') }} 

:   True if the merchant's item list has been populated.

### {{ renderMember(type='float', name='Markup') }} 

:   <p>The number used to calculate the buy and sell value for an item. (This is what is changed by charisma and faction). This value is capped at 1.05.</p><br><ul><li>Markup * Item Value = Amount you buy item for</li><li>Item Value * (1/Markup) = Amount you sell item for</li></ul>

### {{ renderMember(type='bool', name='Open') }} 

:   Returns True if the merchant window is open.

### {{ renderMember(type='item', name='SelectedItem') }} 

:   The currently selected item in the merchant window. Items can be selected by using [/selectitem](../commands/selectitem.md)

### [string][string] `(To String)`

:   Same as *Open*


## Methods

| Name | Action |
| :--- | :--- |
| **Buy**[_#_] | Buys \# of whatever is selected with **Merchant.SelectItem\[xxx]** |
| **CloseWindow** | Will close the merchant window |
| **OpenWindow** | Will open the merchant closest to you, or if you have a merchant target |
| **SelectItem**[_name_] | Select item by partial name match, case insensitive. Prefix _name_ with `=` for EXACT match |
| **Sell**[_count_] | Sell _count_ of selected item. See examples |

## Examples

Using `${Merchant.Sell[#]}`:

```
/selectitem "Diamond"
```

Will select a "Diamond" you can also do "=Diamond" to match EXACT name. Then you can the following command to sell 100 of it:

```
/invoke ${Merchant.Sell[100]}
```
[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: ../data-types/datatype-spell.md
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
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
