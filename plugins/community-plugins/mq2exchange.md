# MQ2Exchange

## Description

**MQ2Exchange**, by Wassup, allows you to exchange items or unequip items without having any inventory windows or bags opened.

The thread where this plugin began can be found in the VIP forums [here](https://macroquest.org/phpBB3/viewtopic.php?t=7603). The current code being maintained by pms can be found [here](https://macroquest.org/phpBB3/viewtopic.php?p=152499#p152499).

## Commands

`/exchange [itemname|itemID] [slotname|slotnumber]` - This exchanges the _itemname/itemID_ into the _slotname/slotnumber_ you define (see [Slot Names](../../reference/general/slot-names.md) for names/numbers). If there is an item in that slot already, it will be placed in the first available inventory/bag slot that is of sufficient size for the item.<br>

**Note:** Item names that contain spaces must be enclosed in quotation marks, otherwise quotations marks are not required.<br>

`/unequip [slotname|slotnumber]` - Unequips the item in the _slotname/slotnumber_.<br>
`/exchange list` - List of all equipment slot names and slot numbers.<br>
`/exchange help` - List of all commands available.<br>
## Examples

The following two examples will exchange Staff of Eternal Flames to the mainhand slot:

`/exchange "staff of eternal flames" mainhand`<br>
`/exchange 24789 13`<br>

The following two examples will unequip the item in your offhand slot:

`/unequip offhand`<br>
`/unequip 14`<br>
