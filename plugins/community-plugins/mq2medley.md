# MQ2Medley

## Description

**MQ2Medley**
[Created by winnower, updated by Dewey2461]
Song scheduler for the modern bard.<br>
"This plugin grew out my frustration with MQ2Twist and it being hard to change from twist to twist while still being efficient and not recasting the songs that already had signification duration left. Was hard to use aria, "A Tune Struck in My Head", and burn twists effectively"

This is the next evolution of MQ2Twist.

## Features

* Set conditions for each song in the medley. Only want to cast on named? Only want to do insult if mana &gt; 10%? Only want to cast dots if attack is on? Only want to cast mana regen when not in combat?<br>
* Advanced queuing support. Can specific target of queued spells for mez or cure and plugin will switch back to existing target with plugin reflexes. Optional interrupt when queing song.<br>
* Adapt your song song set without missing a beat when under the effect of "A tune stuck in my head"<br>
* Priority scheduling. Did you just mez 3 mobs? Switch back to your most important spells automatically<br>
* Automatically switch to maintaining 7 songs when Tune is up<br>
* Switch from medley to medley while still remembering the duration of current songs. Named up? just do switch to your burn medley to introduce new songs to the mix, while knowing what songs are already up.<br>

You can find the latest version of MQ2Medley [here](https://macroquest2.com/phpBB3/viewtopic.php?f=31&t=19781).

## Plugin Interaction

MQ2Medley has no plugin dependencies

MQ2Twist - should be able to coexist, just don't /twist and /medley at the same time<br>
MQ2Cast - recommend not using this on your bard. use "/medley queue" to cast items and aa with cast time. use /alt activate or /cast item to cast instant cast AA and items, can do this even while medley is active (bards are awesome like that)<br>

## Commands

`/medley name` - Sing the given medley<br>
`/medley queue "song/item/aa name" [-targetid|spawnid] [-interrupt]` - add songs to queue to cast once<br>
`/medley stop/end/off` - stop singing<br>
`/medley` - Resume the medley after using /medley stop<br>
`/medley delay #` - 10ths of a second, minimum of 0, default 3, how long after casting a spell to wait to cast next spell<br>
`/medley reload` - reload the INI file
`/medley quiet` - Toggles songs listing for medley and queued songs
`/melody debug` - now toggles on/off debugging information, saves its state

## Examples
`/medley melee` - play medley defined in [MQ2Medley-melee] ini setion
`/medley queue "Dirge of the Sleepwalker" -interrupt` - Interrupt current song and cast AA "Dirge of the Sleepwaler"<br>
`/medley queue "Slumber of Silisia" -targetid|${Me.XTarget[2].ID}` - When current song ends, will mez XTarget[2], briefly switching target to XTraget[2] then switching back to current target. Target will be switched for one pulse, which is typically less than 20ms<br>
`/medley queue "Blade of Vesagran"` - Add epic click to queue<br>
`/medley queue "Lesson of the Devoted"` - Lesson of the Devoted AA will be added to the twist queue and sung when current song finished<br>

## Top-Level Object: ${Medley}

| **Type**                                              | **Member Name**  | **Description**                                            |
| :---------------------------------------------------- | :--------------- | :--------------------------------------------------------- |
| [_string_](../../reference/data-types/datatype-string.md) | **Medley** | String of current medley - false (bool) if no current medley |
| [_double_](../../reference/data-types/datatype-double.md) | **TTQE** | Time in seconds until queue is empty, this is estimate only. If performating normal medley, this will be 0.0 |
| [_boolean_](../../reference/data-types/datatype-boolean.md) | **Active** | true if MQ2Medley is currently trying to cast spells |
| [_int_](../../reference/data-types/datatype-int.md) | **Tune** | Deprecated - always 0. "Tune Stuck in Head" was changed to passive AA |

## INI Format

Can define multiply medleys in section named MQ2Medley-medleyname.<br>
Define up to 20 songs, song1-song20<br>
Each song has 3 parts separated by carrot(^) symbol<br>
* Part 1: Song, Item or AA name<br>
* Part 2: Duration the song lasts, this must be an expression like you would send to ${Math.Calc[part2]}. This how long you expect the buff to last. Notice use of ${Medley.Tune} in my example to increase duration if A Tune Stuck in my Head is up.<br>
* Part 3: Condition for this song to cast. Also an expression for Math.Calc<br>

## Scheduling

Songs will cast in priority order, song1 > song2 > ... > song20<br>
Songs that are not read, will be skipped (Crescendo, Items, AA, etc)<br>
Songs that still have active duration will be skipped (typically will start casting a song if less than 6 seconds left on their duration)<br>
If all songs are active, then will cast the one that will expire soonest.<br>

## INI Example

`[MQ2Medley-melee]`<br>
`songif=!${Me.Invis}`<br>
`song1=possessed dreadstone minstrel's rapier^8^${Target.Type.Equal[NPC]} && (${Target.PctHPs}<98) && !${Target.Slowed.ID}`<br>
`song2=Rapier of Somber Notes^60^${Spell[Symphony of Battle].Stacks}&&!${Me.Buff[Symphony of Battle].ID}`<br>
`song3=Selo's Sonata^60^${Spell[Selo's Sonata].Stacks}`<br>
`song4=Dichotomic Psalm^60^1`<br>
`song5=Tune Stuck In Your Head^780^1`<br>
`song6=War March of Jocelyn Rk. II^18+(6*${Medley.Tune})^1`<br>
`song7=Aria of Maetanrus Rk. II^13 + (6*${Medley.Tune})^1`<br>
`song8=Blade of Vesagran^120^${Target.Type.Equal[NPC]}&&${Target.PctHPs}<98&&(!${SpawnCount[group pc shaman radius 100]}||${Me.Song[Prophet's Gift of the Ruchu].ID})`<br>
`song9=Boastful Bellow^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`<br>
`song10=Bladed Song^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`<br>
`song11=Fierce Eye^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`<br>
`song12=Fundament: Third Spire of the Minstrels^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`<br>
`song13=Funeral Dirge^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`<br>
`song14=Quick Time^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`<br>
`song15=Song of Stone^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`<br>
`song16=Fjilnauk's Song of Suffering Rk. II^18^1`<br>
`song17=Silisia's Lively Crescendo^45^1`<br>
`song18=Arcane Melody Rk. II^18 + (6*${Medley.Tune})^1`<br>
