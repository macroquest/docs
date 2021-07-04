## Description

**MQ2Exchange**, by Wassup, allows you to exchange items or unequip items without having any
inventory windows or bags opened.

The thread where this plugin began can be found in the VIP forums
[here](https://macroquest2.com/phpBB3/viewtopic.php?t=7603). The current code being maintained by pms can be found
[here](https://macroquest2.com/phpBB3/viewtopic.php?p=152499#p152499).

## Commands

-   **/exchange \[itemname\|itemID\] \[slotname\|slotnumber\]**

  
This exchanges the *itemname/itemID* into the *slotname/slotnumber* you define (see [Slot Names](../general-information/slot-names.md)
for names/numbers). If there is an item in that slot already, it will be placed in the first available inventory/bag
slot that is of sufficient size for the item.

**Note:** Item names that contain spaces must be enclosed in quotation marks, otherwise quotations marks are not
required.

-   **/unequip \[slotname\|slotnumber\]**

  
Unequips the item at *slotname/slotnumber*.

## Examples

The following two examples will exchange Staff of Eternal Flames to the mainhand slot:

`/exchange "staff of eternal flames" mainhand`  
`/exchange 24789 13`

The following two examples will unequip the item in your offhand slot:

`/unequip offhand`  
`/unequip 14 `

-   **/exchange list** gives a list of the equipment slot names and slot numbers.
-   **/exchange help** gives a list of the commands available.

## See Also

-   [Plugins](../documentation/macroquest2-plugins.md)


