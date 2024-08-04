# MQ2Bandolier

## Description

**MQ2Bandolier**, written by Wassup, is an extension of the EQ Bandolier which allows you to swap items in any of your inventory slots.

* It requires [MQ2Exchange](mq2exchange.md) in order to perform the item swapping.

You can find the source to the plugin in the VIP forums [here](https://macroquest2.com/phpBB3/viewtopic.php?t=12793).

## Commands

`/createset  [slotname1 | slotnumber1 slotname2 | slotnumber2 ... slotname21|slotnumber22]` - Creates a set in MQ2Bandolier\_.ini using the selected equipment slots. If you use the name of an existing set, it will be over-written.<br>
`/deleteset` - Deletes the specified setname from the characters ini.<br>
`/equipset` - Equips all items in the specified set.<br>

## Examples

`/createset ThisSet chest mainhand offhand`
`/createset ThisSet 17 13 14`

Both of the above examples will create the following INI entry:

`[ThisSet]`
`17=12345`
`13=23456`
`14=34567`
