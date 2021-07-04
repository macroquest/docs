## Syntax

**<span style="color:red">/itemnotify</span>
<span style="color:blue">slotname</span>\|<span style="color:blue">#</span>\|\|<span style="color:blue">itemname</span>
''notification**''  
**<span style="color:red">/itemnotify</span> <span style="color:blue">in</span> *bagslot*
<span style="color:blue">slot#</span> *notification***

## Description

Similar to the /click function, but does not involve the use of the mouse.

-   *Slotname* can be any one of the equipment [Slot Names](../general-information/slot-names.md).
-   *Bagslot* can be pack1-pack8 or bank1-bank16. **Sharedbank1, sharedbank2 and trade1-trade8 are not yet implemented
    in /itemnotify.**

*Notification* can be any one of the following:

|                    |                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **leftmouseup**    | Puts the item on the cursor, or returns it to *slotname* if its already on the cursor (same as left clicking an inventory item). |
| **leftmouseheld**  | Clicks and holds *slotname*. Used for making hotkeys.                                                                            |
| **rightmouseup**   | Casts the item, or opens the container. This is the same as right clicking an inventory slot.                                    |
| **rightmouseheld** | Opens up the item display window.                                                                                                |

## Examples

Exchange the item in slot1 of pack8 with the item in your main hand:

     /itemnotify in pack8 1 leftmouseup
     /itemnotify mainhand leftmouseup
     /itemnotify in pack8 1 leftmouseup

Right-click your Shrunken Goblin Skull Earring:

     /itemnotify "Shrunken Goblin Skull Earring" rightmouseup

## See Also

-   [/click](click.md)
-   [Slot_Names](../general-information/slot-names.md)

[Return to Slash Commands](slash-commands.md)


