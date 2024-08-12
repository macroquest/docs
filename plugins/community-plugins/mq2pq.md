# MQ2PQ

## Description

**MQ2PQ** \(by dewey2461\)

Provide a general purpose spell priority queue.

You can find the latest version of MQ2PQ [here](https://macroquest2.com/phpBB3/viewtopic.php?f=31&t=20060&sid=53b793f1fc32e16a60783466e13c7345).

## Requirements

Plugin:MQ2Cast for... you know... casting!

## Goals

`- Replace MQ2Twist / MQ2Medley / MQ2Melee shits.`
`- Automatically figure out Rk.II & Rk. III versions.`
`- Make it easy to write conditionals for individual spells and/or sets of spells.`
`- Make it easy to see what is going on by providing a window with a list all your 'spells', and showing the status of the conditions.`

How? Define the spells \( AA/Disc/Items \) you want used in the order of importance. Each pulse the plugin find the most important 'spell' that is ready and casts it.
1. Download source and compile plugin.
2. Download UI and save in your EQ\uifiles\default folder.
3. In game type /plugin MQ2PQ
4. In game reload your UI.
5. Click the save button and go edit your servername\_characerter.ini file.
6. In game click Load & On

## Commands

`Help - Show information`
`load - Loads the saved configuration`
`save - Saves the current state`
`show - Shows the priority list window`
`hide - Hides the priority list window`
`on - Start casting spells.`
`off - Stop casting spells.`
`clear - Clears the priority list`
`addset - Add a set to the priority list`
`lag - How long after the "casttime" to consider the spell complete?`
`BARDS ONLY - After "casttime"+lag , the plugin will send a /stopcast.`

## Example

Bard profile converted from MQ2Medley \( WORKING \)

`[MQ2PQ]`
`Set=|melee`
`ON=1`
`SHOW=1`
`CastLag=200`
`Silent=0`
`AutoSelect=1`

`[MQ2PQ-melee]`
`CastIF=!${Me.Invis}`
`Priority=0`

`Spell1_Name=possessed dreadstone minstrel's rapier`
`Spell1_Recast=8000`
`Spell1_CastIF=${Target.Type.Equal[NPC]} && (${Target.PctHPs}<98) && !${Target.Slowed.ID}`

`Spell2_Name=Rapier of Somber Notes`
`Spell2_Recast=10000`
`Spell2_CastIF=${Spell[Symphony of Battle].Stacks}&&!${Me.Buff[Symphony of Battle].ID}`

`Spell3_Name=Selo's Sonata`
`Spell3_Recast=60000`
`Spell3_CastIF=${Spell[Selo's Sonata].Stacks}`

`Spell4_Name=Dichotomic Psalm`
`Spell5_Name=Tune Stuck In Your Head`
`Spell6_Name=War March of Jocelyn Rk. II`

`Spell7_Name=Aria of Maetanrus Rk. II`
`Spell8_Name=Blade of Vesagran`
`Spell8_CastIF=${Target.Type.Equal[NPC]}&&${Target.PctHPs}<98&&(!${SpawnCount[group pc shaman radius 100]}||${Me.Song[Prophet's Gift of the Ruchu].ID})`

`Spell9_Name=Boastful Bellow`
`Spell9_CastIF=${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`

`Spell10_Name=Bladed Song`
`Spell10_CastIF=${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`

`Spell11_Name=Fierce Eye`
`Spell11_CastIF=${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`

`Spell12_Name=Fundament: Third Spire of the Minstrels`
`Spell12_CastIF=${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`

`Spell13_Name=Funeral Dirge`
`Spell13_CastIF=${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`

`Spell14_Name=Quick Time`
`Spell14_CastIF=${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`

`Spell15_Name=Song of Stone`
`Spell15_CastIF=${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`

`Spell16_Name=Fjilnauk's Song of Suffering`
`Spell17_Name=Silisia's Lively Crescendo`
`Spell18_Name=Arcane Melody`
