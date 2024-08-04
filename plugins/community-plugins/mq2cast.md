# MQ2Cast

## Introduction

[MQ2Cast](https://macroquest2.com/phpBB3/viewtopic.php?t=12758) by s0rCieR and A\_Enchanter\_00 is a plugin to handle most things related to spell casting, item clicking and activating of AAs.

The official forum thread for MQ2Cast is [here](https://macroquest2.com/phpBB3/viewtopic.php?t=12758) (VIP Only).

## Features

* Reliably casts spells (auto-recasts on fizzles or gate collapses). Will attempt to immobilize you before casting. Will cast immediately a spell is available, before the gem is even fully ready.<br>
* Intelligently and reliably memorizes spells and allows saving and loading of custom spell sets. Will attempt to immobilize you before memorizing.<br>
* Clicks items and activates AAs. Will equip items in bags before clicking, and then return them once clicked.
* Utilizes MQ2Bandolier to swap in sets of items before casting (ie. Focus items).
* Auto-pause Stick and/or Advpath if detected and resume when complete.
* Custom interrupt function, to interrupt spells during casting (includes dismounting).
* Returns control to the macro immediately after it has started (ie. while the spell is casting), to allow the macro to perform other checks. Eg. while casting a heal spell, you could get the macro to check if the target has already been healed and then interrupt your spell if his HPs are above a certain amount.<br>

## Requirements

[MQ2Bandolier](https://macroquest2.com/phpBB3/viewtopic.php?t=12793) _For swapping in sets of items before casting (ie. focus items)_

[MQ2Exchange](mq2exchange.md) _For equipping clickies before using them_

## Commands

### /casting

**Syntax:**

`/casting "Name" [type] [options]`

_Although the [type] is optional, it's always recommended to specify if you're casting a spell (specify the gem or number), clicking an item (specify "item" or the slot name/slot number) or activating an AA (specify "alt"), since there are AAs which have the same name as spells and spells and items can have the same IDs._

The /casting command requires only 1 argument, the name of the spell you wish to cast. If the spell is not memmed, it will try and mem it in gem5 (this is the default if no gem is specified). If the spell has more than one word, make sure to surround it with quotes. For example:

`/casting "Minor Shielding"`

_This will cast the Minor Shielding spell if it is already memmed, or if not, will attempt to memorize it in gem5 before casting._

You can also include the gem number (or just the number) after the name of the spell, to indicate which gem it should be memmed into. For example:

`/casting "Minor Shielding" 1`
`/casting "Minor Shielding" gem1`

_These will both cast Minor Shielding if memmed, or memorize it in gem1 before casting._

The gem number can also be appended to the end of the spell name, separated by a pipe command, like so:

`/casting "Minor Shielding|gem1"`
`/casting "Minor Shielding|1"`

You can also use the ID of the spell you wish to mem/cast. The following 4 examples all do the same thing:

`/casting 288|gem1`
`/casting 288|1`
`/casting 288 gem1`
`/casting 288 1`

_All of the above will cast "Minor Shielding" (ID 288) and mem it in gem1 if not already memmed._

When clicking items you use the same syntax, except the "name" of the spell is the name of the item or the item's ID. It's always recommended to specify the type as "item" or specify the slot name/slot ID if you are clicking an item. For example:

`/casting "Fabled Journeyman's Boots" item`
`/casting 68239|item`
`/casting "Shrunken Goblin Skull Earring" leftear`

**Options:**
The following optional parameters can be added to the /casting line:

-bandolier|&lt;#&gt;
Equip the bandolier with before casting. Useful for focus effects.

-invis
With this parameter, it will not cast if you are invisible.

-kill
Keep casting this spell until the target dies.

-maxtries|&lt;#&gt;
Cast the spell this many times until successful.

-recast|&lt;#&gt;
Recast the spell this many times.

-setin
Same as bandolier (left here for backwards-compatibility purposes).

-targetid|&lt;#&gt;
Target this ID before casting.

**Examples:**

`/casting "Wunshi's Focusing" gem4 -invis`<br>
`/casting "Complete Heal|gem1" -kill -targetid|1234`<br>
`/casting "Fizzle a Lot|gem4" -maxtries|5`<br>
`/casting "uber nuke|9" -kill`<br>
`/casting "cannibalize" gem3 -recast|5`<br>

### /interrupt

This will just interrupt the current spell/item/AA that is casting. It's the same as doing /stopcast, or /dismount then /stopcast if you're mounted at the time.

### /memorize

**Syntax:**

`/memorize "name" [gem]`

As with the /casting command above, the /memorize command can take spell names or IDs, and can use gem# or just the numbers themselves. The gem# or number can also be appended to the end of the name.

See the following examples:

`/memorize "Minor Shielding"`<br>
`/memorize "Minor Shielding" 1`<br>
`/memorize 288|gem1`<br>

Multiple spells can be memorized with the same line, such as the following example:

`/memorize "1234|1" "gate|2" "cannibalize|gem4"`<br>

As with /casting, the plugin will attempt to immobilize you before memorizing the spell.

### /sss

**''Spell Set Save**'' - This will save your any number of your currently memmed spells into a spell set.
**Syntax:**

`/sss "name" [gems]`

Name is what you want your spell set to be called. If no gems are specified, all your gems are saved (ie. 123456789ABC). You can specify a smaller subset if needed.

`/sss dps 1238`<br>
`/sss dps 12ABC`<br>
`/sss wunshi 5`<br>

### /ssm

_**Spell Set Memorize**_ - This will memorize a previously saved spell set.

`/ssm dps`

### /ssl

_**Spell Set List**_ - This will list all spell sets that have been saved.

`/ssl`

### /ssd

_**Spell Set Delete**_ - This will delete a spell set from the ini file.

`/ssd wunshi`

## Top Level Object: ${Cast}

| **Type** | **Member Name** | **Description** |
| :--- | :--- | :--- |
| [_bool_](../../reference/data-types/datatype-bool.md) | **${Cast}** | Same as ${Cast.Active} (see below). |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Active** | Return TRUE if plugin is loaded and you are in-game. |
| [_spell_](../../reference/data-types/datatype-spell.md) | **Effect** | Returns the name of the spell being casted, or a NULL string if not casting. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Ready** | Return TRUE if ready to cast a spell, item or AA. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Ready[M]** | Return TRUE if ready to memorize a spell. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Ready[#]** | Return TRUE if gem # is ready to cast. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Ready[X]** | Return TRUE if spell, item, gem, ID, AA, etc is ready to cast. (See examples below) |
| [_string_](../../reference/data-types/datatype-string.md) | **Result** | Returns a string containing the result of the /casting command. (See possible results below) |
| [_string_](../../reference/data-types/datatype-string.md) | **Return** | Returns the result of the casting/memorize/interrupt request. |
| [_string_](../../reference/data-types/datatype-string.md) | **Status** | Returns a string containing all the pending events. This string often contains multiple events (See possible events below) |
| [_spell_](../../reference/data-types/datatype-spell.md) | **Stored** | Returns the last spell that was cast, or NULL if no spell has been cast. |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Taken** | Return TRUE if last spell cast didn't take hold on target. |
| [_int_](../../reference/data-types/datatype-int.md) | **Timing** | Returns the estimated number of miliseconds remaining until the spell finished casting. |

## ${Cast.Ready} Examples

`${Cast.Ready[spellname or spellid]}`<br>
`${Cast.Ready[aaname or aaid]}`<br>
`${Cast.Ready[itemname or itemid]}`<br>
`${Cast.Ready[1460]}`<br>
`${Cast.Ready[Death Peace]}`<br>
`${Cast.Ready[Death Peace|alt]}`<br>
`${Cast.Ready[Death Peace|gem]}`<br>
`${Cast.Ready[Death Peace|gem3]}`<br>

## ${Cast.Result} Results

  * **CAST\_ABORTED**: Casting Aborted (/interrupt)
  * **CAST\_CANCELLED**: Casting was aborted
  * **CAST\_CANNOTSEE**: Cannot see target
  * **CAST\_COLLAPSE**: Your Gate collapsed
  * **CAST\_COMPONENTS**: Missing Component
  * **CAST\_DISTRACTED**: You were distracted
  * **CAST\_FIZZLE**: Your cast fizzled
  * **CAST\_IMMUNE**: Target is immune the spell's effect
  * **CAST\_INTERRUPTED**: Casting was interupted
  * **CAST\_INVISIBLE**: You are invisible
  * **CAST\_NOTARGET**: No target
  * **CAST\_NOTREADY**: Not ready to cast
  * **CAST\_OUTOFMANA**: Not enough mana to cast spell
  * **CAST\_OUTOFRANGE**: Target is out of range
  * **CAST\_OUTDOORS**: Spell not working here (on mount ect..)
  * **CAST\_PENDING**: Casting is in progress
  * **CAST\_RECOVER**: Spell is not ready
  * **CAST\_RESIST**: Cast was resisted
  * **CAST\_STANDING**: Not standing
  * **CAST\_STUNNED**: You are stunned
  * **CAST\_SUCCESS**: The cast was a success
  * **CAST\_TAKEHOLD**: The spell did not take hold
  * **CAST\_UNKNOWN**: Unknown Spell

## ${Cast.Status} Results

  * **I**: idle and waiting for you
  * **A**: advpath pause
  * **F**: stick pause
  * **S**: immobilize in progress
  * **M**: memorize in progress
  * **E**: item swapped
  * **D**: ducking casting
  * **T**: targeting
  * **C**: spell casting in progress

## MQ2CastTimer

MQ2CastTimer is a plugin which allows you to check timers on active spells, and adds a Timer Window that can be used to monitor spells you have cast on others.

### Commands

#### /timer

**Syntax:**

`/timer [on|off]`

_Turns timer Window on / off_

`/timer clear [all|target|pc|npc|pet]`

_Clear Spell timers_

`/timer autorecast [#]`

_Set Number of seconds left on spell before recasting Default:20_

### Top Level Object: ${SpellTimer}

| **Type** | **Member Name** | **Description** |
| :--- | :--- | :--- |
| [_int_](../../reference/data-types/datatype-int.md) | **${SpellTimer[SpawnID,Caster,Spell Name]}** | Returns time (in seconds) left on the spell. Caster can be **me**(default), **other**, or **any**. (See examples below) |

**Examples:**

`${SpellTimer[${Target.ID},Euphoria]}`<br>
`${SpellTimer[${Target.ID},me,Euphoria]}`<br>

_This will give the time remaining on the Euphoria spell that **you** cast on your current target (both examples do the same thing)._

`${SpellTimer[${Target.ID},other,Euphoria]}`

_This will give the time remaining on Euphoria on your current target, only if **someone else** cast it._

`${SpellTimer[${Target.ID},any,Euphoria]} OR ${SpellTimer[${Target.ID},All,Euphoria]}`

_This will give the time remaining on Euphoria on your current target, no matter who cast the spell._

`/if (${SpellTimer[${Target.ID},Euphoria]} < 15) {`<br>
`/call mq2cast Euphoria gem1 20s`<br>
`}`<br>

_Cast Euphoria on target if you originally cast the spell, and it has less than 15 sec left._

`${SpellTimer[${Target.ID},any,"Sha's Legacy","Forlorn Deeds","Desolate Deeds","Turgur's Insects","Balance of Discord"]}`

_If you want to check if a target is slowed you may use somthing like this. **NOTE: this is just an example**_

### Timer Window

An example of what the Timer Window looks like is (NOTE: Links removed as they are both dead.) (DarkDevil)

The Timer Window shows the following information:

* **Time Left**

  The amount of time left on the spell, in HH:MM:SS format. Eg. 00:15:32.

* **Tags**

  Some information on the target.

  * **T**: This is your current target.
  * **N**: Spell did not take hold on this target.
  * **I**: Target is immune to this spell.
  * **E**: Event (Show that the timer is an Event)
  * **GA**: This target is the Group Assist.
  * **G1-3**: This target is group marked 1-3.
  * **RA**: This target is the Raid Assist.
  * **R1-3**: This target is raid marked 1-3.

* **Spell Name**

  The name of the spell.

* **Spawn Name**

  The unique name of the spawn.

The buttons/comboboxes at the bottom of the window do the following:

* **Button**

  Pauses and unpauses the Timer Window.

* **Combobox 1**

  Select what you want to do when left-clicking the line in the window:

  * Target
  * TargetNAB (Target nearest spawn without this spell)
  * Recast spell (if memmed)
  * Clear (removes timer). _You cannot remove an event._

* **Combobox 2**

  Select what you want to do when right-clicking the line. Same choices as above.

The Timer Settings Tab:

* **Target (Current Target)**

  Show Target Timers

* **NPC**

  Show Npc and Npc Pet Timers

* **PC**

  Show Pc Timers

* **PET**

  Show Pc Pet Timers

* **Events (All Events)**

  Show Events

* **My Spells (Show Your Spells)**

  Show My Spells

* **Other's Spells (Show Other Spells)**

  Show Other Spells

An example INI entry created by the MQ2CastTimer Window is below. This contains the location, size and colors of the window.

`[Settings..]`<br>
`ChatTop=58`<br>
`ChatBottom=233`<br>
`ChatLeft=58`<br>
`ChatRight=580`<br>
`Locked=0`<br>
`WindowTitle=Timers`<br>
`Fades=1`<br>
`Delay=0`<br>
`Duration=500`<br>
`Alpha=255`<br>
`FadeToAlpha=255`<br>
`BGType=1`<br>
`BGTint.red=93`<br>
`BGTint.green=83`<br>
`BGTint.blue=93`<br>
`ActorModeLeft=0`<br>
`ActorModeRight=2`<br>
`DefaultGem=gem8`<br>
`ShowTarget=0`<br>
`ShowNpc=1`<br>
`ShowPC=0`<br>
`ShowPet=0`<br>
`ShowEvent=1`<br>
`ShowMySpells=1`<br>
`ShowOtherSpells=0`<br>

### Custom Events

You can add Custom Events to the INI file in the following format:

`[Name of Event]`<br>
`duration=<#>`<br>
`event=<" event text">`<br>
`spawntype=<1=pc|2=npc>`<br>

The duration is in seconds. The event is the text that you see on the screen when you want the event to occur. An example is below:

`[NPC Gating]`<br>
`duration=5`<br>
`event="#SpawnName# begins to cast the gate spell."`<br>
`spawntype=2`<br>

`[NPC Complete Healing]`<br>
`duration=10`<br>
`event="#SpawnName# begins to cast a spell."`<br>
`spawntype=2`<br>

`[PC Complete Healing]`<br>
`duration=10`<br>
`event="#SpawnName# begins to cast a spell."`<br>
`spawntype=1`<br>

`[Redfang Despawn]`<br>
`duration=240`<br>
`event="An ear-piercing screech reverberates throughout the surreal cavernous Demi-Plane of Blood, announcing the arrival of Redfang."`<br>
