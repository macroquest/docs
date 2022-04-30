# Spell Routines.inc

## Introduction

* Spell\_Routines.inc is an incredibly useful snippet which casts spells, clicks items and activates AAs reliably,

  deals with fizzles, and provides a wealth of return code information for use in the calling macro.

* It was originally written by ~rusty and later improved by A\_Druid\_00 (VIP version), and is probably the most-used

  inc file today. It's the de-facto standard include for any macro which requires the casting of a spell, an AA, or

  clicking of an item.

* As with many of the inc files on the forums, there are 2 versions of spell\_routines.inc:
* [Non-VIP](https://macroquest.org/phpBB3/viewtopic.php?t=7568). This is the original from ~rusty.
* [VIP](https://macroquest.org/phpBB3/viewtopic.php?t=11656). This is the updated version, maintained by A\_Druid\_00.
* The VIP version has been improved slightly and it a bit smaller (and thus faster). It also improves speed by making use of the MQ2Exchange plugin which is available in the VIP area. Both versions are interchangeable, and there are only minor differences between them. Both are fully functional.

## Usage

To make use of the Spell\_Routines.inc file, save it to your main Macros directory and then add this to the top of your macro:

`#include Spell_Routines.inc`

After this, you can use the commands/functions listed below.

## /call Cast

**/call Cast "spellname\|itemname\|AAname\|AA\#" [item\|alt\|gem\#\] \["give up time"\] \["custom subroutine name"\] \["Number of resist recasts"]**

_Note: Any of the above fields must use quotes if they are more than one word._

This will cast a spell or AA, or click an item.

**Examples:**

`/call Cast "Complete Healing" | Cast Complete Healing if it is memmed`  
`/call Cast "Arcane Rune" gem5 7s | Cast Arcane Rune, memorizing it in gem5 if not already, and keep casting for 7s in case of interrupts`  
`/call Cast "Eldritch Rune" alt | Cast Eldritch Rune`  
`/call Cast "173" alt | Cast Eldritch Rune`

The most useful part about this routine is the custom subroutine. Take the following example:

`/call Cast "Complete Healing" gem1 10s CheckHP`

The CheckHP subroutine is as follows:

`Sub CheckHP`  
`/if ( ${Target.PctHPs}>=80 ) /call Interrupt`  
`/return`

This will continuously /call the CheckHP subroutine while the spell is casting, and if the target's HPs rise above 80% (ie. they got a heal from someone else), it will interrupt the casting.

## /call SwapItem

**/call SwapItem "item name" slotname**

This will swap an item into a specific slot.

`/call SwapItem "Darkblade of the Warlord" mainhand`

This will swap your Darkblade of the Warlord into your main hand.

## /call EquipItem

**/call EquipItem "item name\|slotname"**

This will equip an item into the slot you specify. It returns "old item\|slotname", so that you can use the same function to swap the original item back.

`/call EquipItem "Sharp Ended Broken Lever" | This returns "Staff of Vindication|mainhand"`

Note the following example:

`/call EquipItem "Sharp Ended Broken Lever"`  
`/declare olditem string outer ${Macro.Return}`  
`| Do something with your new main hand...`  
`/call EquipItem "${Macro.Return}"`

## /call Interrupt

**/call Interrupt**

This will interrupt whatever spell/item/AA is currently being cast.

Essentially it dismounts if you're on a horse, and then does a /stopcast.

**Note:** if you don't want to interrupt a spell while mounted, put this at the top of your macro:

`/declare noInterrupt int outer 1`

## Return Codes

/call Cast returns the following:

|  |  |
| :--- | :--- |
| CAST\_CANCELLED | Spell was cancelled by ducking (either manually or because mob died) |
| CAST\_CANNOTSEE | You can't see your target |
| CAST\_IMMUNE | Target is immune to this spell |
| CAST\_INTERRUPTED | Casting was interrupted and exceeded the given time limit |
| CAST\_INVIS | You were invis, and **noInvis** is set to true |
| CAST\_NOTARGET | You don't have a target selected for this spell |
| CAST\_NOTMEMMED | Spell is not memmed and you gem to mem was not specified |
| CAST\_NOTREADY | AA ability or spell is not ready yet |
| CAST\_OUTOFMANA | You don't have enough mana for this spell! |
| CAST\_OUTOFRANGE | Target is out of range |
| CAST\_RESISTED | Your spell was resisted! |
| CAST\_SUCCESS | Your spell was cast successfully! (yay) |
| CAST\_UNKNOWNSPELL | Spell/Item/Ability was not found |

## Other

* If you don't want this to cast spells while you're invis, in your main macro have this at the top:

`/declare noInvis int outer 1`

This will make it return CAST\_INVIS if you're invis

* Below is a list of outer scope variables you can access in your macros:

`refreshTime | How much time is left till you're done recovering from casting`  
`castEndTime | How much time left till you're done casting the current spell... usable in custom spell Subs`  
`spellNotHold | 1 if your last spell didn't take hold, 0 otherwise`  
`spellRecastTime1-9 | How much time left until the spell is back up`

