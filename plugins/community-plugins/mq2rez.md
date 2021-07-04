# MQ2Rez

## Description

Work done by Thez, Based off of dewey's [MQ2AutoRez](https://macroquest2.com/phpBB3/viewtopic.php?t=14058) This plugin is set up to auto accept rezes based on INI configuration, along with auto looting your corpse.

**MQ2Rez**

You can find the latest version of MQ2Rez [here](https://macroquest2.com/phpBB3/viewtopic.php?f=31&t=14171).

## Commands

`/rez -> displays settings`  
`/rez accept on|off -> Toggle auto-accepting rezbox`  
`/rez spawn on|off -> Toggles going to bind point after death`  
`/rez pct # -> Autoaccepts rezes only if they are higher than # percent`  
`/rez loot on|off -> Toggle looting corpse when opened and when rezzed`  
`/rez silent -> Toggle messages for looting individual items`  
`/rez command on|off -> Toggle use of a command after looting out corpse`  
`/rez setcommand "mycommand" -> Set the command that you want.`  
`/rez help`  
`/rezzme -- Immediately respawn yourself without a rez. You will *not* regain any experience.`

The "mycommand" must be formatted like this: "/memset group" or "/multiline ; /sit ; /memset group ; /mac rezbuffs" etc.

## See Also

* [Plugins](../../documentation/macroquest2-plugins.md)

