# MQ2HUDMove

## Description

MQ2HUDMove by ieatacid allows you to move HUDs or sections of HUDs easily. The plugin can be downloaded [here](https://macroquest2.com/phpBB3/viewtopic.php?t=9087).

* It requires the [MQ2HUD](../core-plugins/mq2hud/) plugin

Features:

* HUDs can be moved to the location of the cursor, or up/down/left/right by the specified number of units.
* Individual elements can be moved, or user-specified sections
* HUD colors can also be changed to a number of preset colors.

## Commands

`/hudmove list` - List all HUDs in the loaded HUD set and all sections in MQ2HUD.ini<br>
`/hudlist` - Same as above<br>
`/hudmove` - Move a single HUD<br>
`/hudmove <name> delete` - Delete a single HUD<br>
`/hudmove <name> <direction> <#>` - Move a single HUD a specified number of units in whatever direction<br>
`/hudcolor list` - List preset colors<br>
`/hudcolor <name> <color name>` - Change HUD to any of the preset colors.<br>

## Examples

If we typed "/hudmove ;section1 right 100", it would move the HUD elements "ManaRegen" and "BuffCount" 100 units to the right.

`[elements]`
`Level=3,339,649,0,255,255,${If[${Target.ID},${Target.Level} - ${Target.Class} - ${Target.Distance} - ${Target.LineOfSight},]}`
`Raid=3,1263,468,0,255,255,${If[${Raid.Members}>0,In Raid - ${Raid.Members},]}`
`TarID=3,172,337,0,255,0,ID: ${Target.ID}`
`;section1`
`ManaRegen=3,272,272,0,255,0,MR: ${Me.ManaRegen}`
`BuffCount=3,272,367,0,255,0,Buffs: ${Me.CountBuffs}`
`;section2`
`ER=3,172,342,0,255,0,ER: ${Me.AltAbilityTimer[Eldritch Rune].TimeHMS}`
`MGB=3,172,357,0,255,0,MGB: ${Me.AltAbilityTimer[Mass Group Buff].TimeHMS}`

* For now, the only requirement for defining custom sections is that it follows this format:

`;name`
