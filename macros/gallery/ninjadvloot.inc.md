---
tags:
   - macro
---
# Ninjadvloot.inc

## Description

Ninjadvloot.inc is an include file writen by A\_Druid\_00 available [here](https://macroquest2.com/phpBB3/viewtopic.php?t=12578).

## Usage

Ninjadvloot.inc uses an ini(Loot.ini) which it will populate with items looted by the loot section of Autobot. Below is a start of some docummentation for the various possible INI file entries.

## INI File Entries

**[Settings]**
**LootMobs=TRUE** _Whether or not to do looting_
**CorpseRadius=100** _Radius in which to check for corpses to loot_
**MobsTooClose=50** _Radius in which to check for live NPCs so as to avoid looting while mobs are too close_
**CorpseRotTime=440s** _The amount of time you want to wait before trying to loot a corpse that was previously unlootable due to the corpse timer_
**ReportLoot=TRUE** _Whether or not to report items looted to $LootChannel?_
**LootChannel=i say** _Channel into which to report looting issues_
**[B]** _Start of section for items starting with "b"_
**Blue Diamond=Keep** ''Name of item and action to take. Possible actions are **Keep**, **Ignore** and **Destroy**. Ninjadvloot automatically adds droppable items as Keep and No Drop items as Ignore by default. It will not automatically set any items to Destroy. It reads the ini each time a loot decision is made, so you do not need to restart your macro in order to update the ini settings for any given item when you make a change. Just save the ini and the next time it encounters that item, it will use the new Keep/Ignore/Destroy setting.

