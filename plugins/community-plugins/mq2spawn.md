# MQ2Spawn

## Description

**MQ2Spawn** \[By pms\]

The intention behind this plugin was to have the ability to announce all OnAddSpawn and OnRemoveSpawn to a dedicated window without the need of attaching a debugger. There are several great spawn tracking plugins on these forums such as MQ2Targets and MQ2Pop that offer named mob announcements, custom spawn search arguments, and many more features. This is not intended to be any sort of replacement for their great utility - just real-time tracking of desired spawn types. I borrowed ideas from MQ2ChatWnd, MQ2EQBC, MQ2TimeStamp, MQ2Paranoid, and others.

You can find the latest version of MQ2 [here](https://macroquest.org/phpBB3/viewtopic.php?p=143610#p143610).

## Commands

`/spawn - toggle announcements on/off`  
`/spawn on - turns announcements on`  
`/spawn off - turns announcements off`  
`/spawn loc - toggles spawn location suffix in output`  
`/spawn spawnid - toggles display of mob spawnid suffix in output`  
`/spawn timestamp - toggles timestamp prefix in output`  
`/spawn autosave - toggles autosaving of INI file upon setting change`  
`/spawn delay - Sets zone time delay`

`/spawn log on - Turns logging on`  
`/spawn log off - Turns logging off`  
`/spawn log auto - Enables automatic logging`  
`/spawn log setpath- Set path to store log files`

`/spawn save - save configuration to INI (also saves UI settings)`  
`/spawn load - load configuration from INI (also reloads UI settings)`  
`/spawn savebychar - toggle saving UI window settings to [i]server.charname[/i] INI section`  
`/spawn status - outputs current plugin settings`  
`/spawn help - outputs valid command parameters`

`/spawn clear - clears UI text (like /mqclear)`  
`/spawn min - minimizes UI window (like /mqmin)`  
`/spawn font # - sets UI font size`

`/spawn exclude name - adds a spawn name to the exclude list, if using multiple words use quotes e.g.:`  
`/spawn exclude guard`  
`/spawn exclude "chuckles the great"`

`// Valid spawn type announcement toggles`  
`// e.g. /spwn all`  
`// e.g. /spwn pc`  
`// e.g. /dspwn npc`  
`// e.g. /dspwn all`  
`//`  
`// Note: 'all' will override settings and display all types when on`  
`// this does not reset your other toggles, so if you toggle 'all' off`  
`// it will announce only the types that are on, retaining old settings`

`all - pc - npc - mount - pet - merc - flyer - campfire - banner - aura - object - untargetable - chest - trap - timer - trigger - corpse - item - unknown`

`// you may also use the following commands, where you substitute [i]toggletype[/i] with any of those types listed above:`

`/spwn [i]toggletype[/i] - toggles output of this type spawning`  
`/dspwn [i]toggletype[/i] - toggles output of this type despawning`

`/spawn [i]toggletype[/i] spawn - toggles output of this type spawning`  
`/spawn [i]toggletype[/i] despawn - toggles output of this type despawning`  
`/spawn [i]toggletype[/i] minlevel # - sets minimum level a spawn of this type must be to display output (valid 1 to 99)`  
`/spawn [i]toggletype[/i] maxlevel # - sets maximum level a spawn of this type must be to display output (valid 1 to 99)`  
`/spawn [i]toggletype[/i] color FF00FF - sets the output text color for this spawn type to the supplied hexadecimal RGB color value. do NOT prefix this value with 0x, #, nor use the integer value.`
