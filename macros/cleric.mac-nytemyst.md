## Forum Link

-   [Cleric.mac - Nytemyst](https://macroquest2.com/phpBB3/viewtopic.php?f=49&t=186738)

## Description

This macro is mainly for high level cleric, but possible for low levels to use. It is based off of [Nils's
version](https://macroquest2.com/phpBB3/viewtopic.php?f=49&t=14508) of Afcleric which was based off of the original
[by fantum409](https://macroquest2.com/phpBB3/viewtopic.php?f=43&t=7567&hilit=afcleric), but it's been highly highly
modified. Will Heal Groups, extended targets,Pets,specific tanks, Specific PCs outside of your group.

## Plugins Used

-   [MQ2MoveUtils](https://macroquest2.com/phpBB3/viewtopic.php?t=11732)
-   [MQ2Debuffs](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=13495&hilit=mq2debuffs) Need for Curing.
-   [MQ2EQBC](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=12147) For BC curing and Buffing
-   [MQ2Netbots](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=13495) For BC curing and Buffing

## Required Include Files

General.inc - All the macros made/updated by me will use this include. Contains common features all the macros use to
ease in updating functions and features to all the macros instead of updating each macro separately.

-   [Spell_Routines.inc](https://macroquest2.com/phpBB3/viewtopic.php?t=11656)
-   [Ninjadvloot.inc](https://macroquest2.com/phpBB3/viewtopic.php?t=12578&postdays=0&postorder=asc&start=0)

If you don't want to use Ninjadvloot.inc you can comment out or delete these lines.

`#include ninjadvloot.inc `  
`/call SetupAdvLootVars`  
`/if (${DoLoot} && !${Me.Moving} && !${Me.Invis}) /call LootMobs `

-   [AAPurchase.inc](https://macroquest2.com/phpBB3/viewtopic.php?f=49&t=15824)

If you don't want to use AAPurchase.inc You can comment out or delete these lines.

`#include AAPurchase.inc `  
`/call AAInit `

Events.inc This is used for raiding to allow the bot to perform certain emotes. Whenever I get involved with a new raid
that needs the toons to react to an emote this gets updated. If you don't care to use it you can comment or delete out
this line.

`#include events.inc`

## Commands

-   /battlerez On/Off - Turn Battle rez on or off.
-   /Reverse On/Off - Changes BC Buff and Curing process order.
-   /doloot On/Off - Turns looting on or off.
-   /hammer On/Off - Turns using the Pet hammer on or off.
-   /nuke On/Off - Turns nuking on or off.
-   /GroupHeal On/Off - Turns casting a group heal on or off.
-   /Tankhot On/Off - Turns casting a HOT on the tank on or off.
-   /UseCure On/Off - Turns Spell Curing on or off.
-   /RC On/Off - Turns curing by RC on or off.
-   /Raidbuff - Turns raid buffing on or off.
-   /stopheal # - Changes the default stop heal point.
-   /startheal # - Changes the % of when to start healing.
-   /Xheal On/Off - Turns on or off healing Extended Targets.
-   /Xhealknights On/Off - Turns on or off of automatically adding Knights to xtargets.
-   /usepromise On/Off - Turns on or off using promise line on tank.
-   /promise # - Changes the % of the minimum health the tank can be for a promise heal.
-   /useepic On/Off - Turns using the epic on or off.
-   /doyaulp On/Off - Turns using spell yaulp on or off.


