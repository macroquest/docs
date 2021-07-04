## Description

Object which is the found item on your character, a corpse, or a merchant by partial name match. Using =name will only
find an exact match.

## Forms

|                                                              |                                                                               |
|--------------------------------------------------------------|-------------------------------------------------------------------------------|
| *[item](../data-types/datatype-item.md)* **FindItem\[**name**\]**  | Returns item on your character, a corpse, or a merchant by partial name match |
| *[item](../data-types/datatype-item.md)* **FindItem\[**=name**\]** | Returns item on your character, a corpse, or a merchant by exact name match   |

## Access to Types

-   *[item](../data-types/datatype-item.md)* **item**

## Examples

Picks up the cleric epic 1.0

`   /itemnotify ${FindItem[=Water Sprinkler of Nem Ankh].InvSlot} leftmouseup`

Picks up any item containing the word swirling from your current target, be it a corpse, or your inventory

`   /itemnotify ${FindItem[swirling].InvSlot} leftmouseup`

This would be the newer ItemSlot variant:

`   /itemnotify in pack${Math.Calc[${FindItem[=Dragorn Fang].ItemSlot}-22].Int} ${Math.Calc[${FindItem[=Dragorn Fang].ItemSlot2}+1].Int} leftmouseup`

The above example would find a stack of Dragorn Fangs in your inventory, locating the pack number 1-10, and which slot
in that pack (1-?) and pick up the stack

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [item](../data-types/datatype-item.md)


