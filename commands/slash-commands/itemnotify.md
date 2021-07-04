# Itemnotify

## Syntax

**/itemnotify slotname\|\#\|\|itemname ''notification**''  
**/itemnotify in** _**bagslot**_ **slot\#** _**notification**_

## Description

Similar to the /click function, but does not involve the use of the mouse.

* _Slotname_ can be any one of the equipment [Slot Names](../../general-information/slot-names.md).
* _Bagslot_ can be pack1-pack8 or bank1-bank16. \*\*Sharedbank1, sharedbank2 and trade1-trade8 are not yet implemented

  in /itemnotify.\*\*

_Notification_ can be any one of the following:

|  |  |
| :--- | :--- |
| **leftmouseup** | Puts the item on the cursor, or returns it to _slotname_ if its already on the cursor \(same as left clicking an inventory item\). |
| **leftmouseheld** | Clicks and holds _slotname_. Used for making hotkeys. |
| **rightmouseup** | Casts the item, or opens the container. This is the same as right clicking an inventory slot. |
| **rightmouseheld** | Opens up the item display window. |

## Examples

Exchange the item in slot1 of pack8 with the item in your main hand:

```text
 /itemnotify in pack8 1 leftmouseup
 /itemnotify mainhand leftmouseup
 /itemnotify in pack8 1 leftmouseup
```

Right-click your Shrunken Goblin Skull Earring:

```text
 /itemnotify "Shrunken Goblin Skull Earring" rightmouseup
```

## See Also

* [/click](click.md)
* [Slot\_Names](../../general-information/slot-names.md)

[Return to Slash Commands](./)

