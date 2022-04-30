# MQ2Medley

## Description

**MQ2Medley**  
\[Created by winnower, updated by Dewey2461\]  
Song scheduler for the modern bard.  
"This plugin grew out my frustration with MQ2Twist and it being hard to change from twist to twist while still being efficient and not recasting the songs that already had signification duration left. Was hard to use aria, "A Tune Struck in My Head", and burn twists effectively"  
This is the next evolution of MQ2Twist. Features

* Set conditions for each song in the medley. Only want to cast on named? Only want to do insult if mana &gt; 10%? Only

  want to cast dots if attack is on? Only want to cast mana regen when not in combat?

* Advanced queuing support. Can specific target of queued spells for mez or cure and plugin will switch back to

  existing target with plugin reflexes. Optional interrupt when queing song.

* Adapt your song song set without missing a beat when under the effect of "A tune stuck in my head"
* Priority scheduling. Did you just mez 3 mobs? Switch back to your most important spells automatically  
* Automatically switch to maintaining 7 songs when Tune is up  
* Switch from medley to medley while still remembering the duration of current songs. Named up? just do switch to your

  burn medley to introduce new songs to the mix, while knowing what songs are already up.

You can find the latest version of MQ2Medley [here](https://macroquest.org/phpBB3/viewtopic.php?f=31&t=19781).

## Plugin Interaction

MQ2Medley has no plugin dependencies

MQ2Twist - should be able to coexist, just don't /twist and /medley at the same time  
MQ2Cast - recommend not using this on your bard. use "/medley queue" to cast items and aa with cast time. use /alt activate or /cast item to cast instant cast AA and items, can do this even while medley is active \(bards are awesome like that\)

## Commands

`/medley name - Sing the given medley`  
`/medley queue "song/item/aa name" [-targetid|spawnid] [-interrupt] - add songs to queue to cast once`  
`/medley stop/end/off - stop singing`  
`/medley - Resume the medley after using /medley stop`  
`/medley delay # - 10ths of a second, minimum of 0, default 3, how long after casting a spell to wait to cast next spell`  
`/medley reload - reload the INI file`  
`/medley quiet - Toggles songs listing for medley and queued songs`  
`/melody debug - now toggles on/off debugging information, saves its state`

Examples:  
\*/medley melee play medley defined in \[MQ2Medley-melee\] ini setion

* /medley queue "Dirge of the Sleepwalker" -interrupt

Interrupt current song and cast AA "Dirge of the Sleepwaler"

* /medley queue "Slumber of Silisia" -targetid\|${Me.XTarget\[2\].ID}

When current song ends, will mez XTarget\[2\], briefly switching target to XTraget\[2\] then switching back to current target. Target will be switched for one pulse, which is typically less than 20ms

* /medley queue "Blade of Vesagran"

Add epic click to queue

* /medley queue "Lesson of the Devoted"

Lesson of the Devoted AA will be added to the twist queue and sung when current song finished

## TLO

* Medley.Medley
* string of current medley - false \(boolean\) if no current medley
* Medley.TTQE \(time to queue empty\)
* double time in seconds until queue is empty, this is estimate only. If performating normal medley, this will be 0.0 Medley.Tune - int 1 if buffed with "A Tune Stuck in My Head", 0 otherwise
* Medley.Active
* boolean true if MQ2Medley is currently trying to cast spells

## INI Format

Can define multiply medleys in section named MQ2Medley-medleyname.  
Define up to 20 songs, song1-song20  
Each song has 3 parts separate by carrot\(^\) symbol  
\*Part 1: Song, Item or AA name  
\*Part 2: Duration the song lasts, this must be an expression like you would send to ${Math.Calc\[part2\]}. This how long you expect the buff to last. Notice use of ${Medley.Tune} in my example to increase duration if A Tune Stuck in my Head is up.  
\*Part 3: Condition for this song to cast. Also an expression for Math.Calc

## Scheduling

Songs will cast in priority order, song1 &gt; song2 &gt; ... &gt; song20  
Songs that are not read, will be skipped \(Crescendo, Items, AA, etc\)  
Songs that still have active duration will be skipped \(typically will start casting a song if less than 6 seconds left on their duration\)  
If all songs are active, then will cast the one that will expire soonest.

## INI Example

`[MQ2Medley-melee]`  
`songif=!${Me.Invis}`  
`song1=possessed dreadstone minstrel's rapier^8^${Target.Type.Equal[NPC]} && (${Target.PctHPs}<98) && !${Target.Slowed.ID}`  
`song2=Rapier of Somber Notes^60^${Spell[Symphony of Battle].Stacks}&&!${Me.Buff[Symphony of Battle].ID}`  
`song3=Selo's Sonata^60^${Spell[Selo's Sonata].Stacks}`  
`song4=Dichotomic Psalm^60^1`  
`song5=Tune Stuck In Your Head^780^1`  
`song6=War March of Jocelyn Rk. II^18+(6*${Medley.Tune})^1`  
`song7=Aria of Maetanrus Rk. II^13 + (6*${Medley.Tune})^1`  
`song8=Blade of Vesagran^120^${Target.Type.Equal[NPC]}&&${Target.PctHPs}<98&&(!${SpawnCount[group pc shaman radius 100]}||${Me.Song[Prophet's Gift of the Ruchu].ID})`  
`song9=Boastful Bellow^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`  
`song10=Bladed Song^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`  
`song11=Fierce Eye^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`  
`song12=Fundament: Third Spire of the Minstrels^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`  
`song13=Funeral Dirge^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`  
`song14=Quick Time^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`  
`song15=Song of Stone^18^${Target.Type.Equal[NPC]} && ${Target.PctHPs}<98`  
`song16=Fjilnauk's Song of Suffering Rk. II^18^1`  
`song17=Silisia's Lively Crescendo^45^1`  
`song18=Arcane Melody Rk. II^18 + (6*${Medley.Tune})^1`
