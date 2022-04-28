# TLO:InvSlot

.invslot .InvSlot .InvSlot2 are all deprecated

Use [ItemSlot]()

### Historic Info

Access to inventory and pack slots, as well as other similar types of slots within windows such as corpse, trade, bazaar, inspect, etc. See [Slot Names](../../general-information/slot-names.md) for a list of slot names and numbers.

## Forms

|  |  |
| :--- | :--- |
| [_invslot_](../data-types/datatype-invslot.md) **InvSlot[**name**]** | Inventory slot by name |
| [_invslot_](../data-types/datatype-invslot.md) **InvSlot[**\#**]** | Inventory slot by number |

## Access to Types

* [_invslot_](../data-types/datatype-invslot.md) **invslot**

## Examples

`/if (!${Window[pack${bag}].Open}) /itemnotify pack${bag} rightmouseup`

If the container in slot pack${bag} isn't opened, open it.

`/if (${InvSlot[bank${index}].Item.Container}) /call CheckPack bank${index}`

Is the item in bank${index} a container? If so /call CheckPack and pass the parameter bank${index}.

## See Also

* [Top-Level Objects](./)
* [invslot](../data-types/datatype-invslot.md)
* [Slot Names](../../general-information/slot-names.md)

