## Description

**MQ2SpawnMaster** \[By Cr4zyb4rd\]

Those of you already familiar with the Digitalxero's SpawnAlert plugin will notice a lot of that functionality here
(though hopefully without the crashing and other oddities) though the intended use of this plugin starts where that one
leaves off.

/spawnmaster by itself will give you a short help, the commands so far are fairly simple, but will probably become
complex as development moves forward. Search strings are stored per-zone in an INI file. Two search types are currently
supported, case-sensitive exact match (the type created by calling '/spawnmaster add' with a spawn targetted) and a
case-insensitive sub-string match (created with "/spawnmaster add "search string", although prefacing the string with a
# will indicate an exact-match type). Both currently only check against the name EQ displays, although future versions
will support for exact matches against Some_Mob_00 and so on.

The plugin currently stores the mob's x/y/z location, the system and in-game time of spawn, and SpawnID#, though not all
of this information is made available in-game. When a mob dies or depops a system and in-game timestamp are also added.

Anything set in the OnSpawnCommand key in the Settings section of the INI fille will be executed as a command when the
spawn is first matched so that for example "/speak ${SpawnMaster.LastMatch} just spawned!" will give you a nice spawn
alert if using the MQ2Speech plugin.

You can find the latest version of MQ2
[here](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=9853&hilit=mq2spawnmaster).

## Commands

/spawnmaster commands

`on|off - Toggles SpawnMaster plugin on or off`  
`add \"spawn name\" - Add spawn name to watch list (or target if no name given`  
`delete \"spawn name\" - Delete spawn name from watch list (or target if no name given`  
`list - Display watch list for zone`  
`case [off|on] - Control whether to use exact case matching in any compare. Omit on or off to toggle.`  
`uplist - Display any mobs on watch list that are currently up`  
`downlist - Display any watched mobs that have died or despawned`  
`load - Load spawns from INI`  

## See Also

-   [Plugins](../documentation/macroquest2-plugins.md)


