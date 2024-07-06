---
tags:
    - datatype
---
# `spawn`

Represents an in-game spawn.

## Members

### {{ renderMember(type='int', name='AARank') }}

:   AA rank number

### {{ renderMember(type='string', name='AATitle') }}

:   Synonym for Title (deprecated)

### {{ renderMember(type='string', name='ActorDef') }}

:   ???

### {{ renderMember(type='bool', name='AFK') }}

:   AFK?

### {{ renderMember(type='bool', name='Aggressive') }}

:   returns TRUE or FALSE if a mob is aggressive or not

### {{ renderMember(type='int', name='Animation') }}

:   Current animation ID. See [Animations](../../reference/general/animations.md) for a list of animations.

### {{ renderMember(type='bool', name='Anonymous') }}

:   Anonymous

### {{ renderMember(type='bool', name='Assist') }}

:   Current Raid or Group assist target?

### {{ renderMember(type='string', name='AssistName') }}

:   ???

### {{ renderMember(type='bool', name='Binding') }}

:   Binding wounds?

### {{ renderMember(type='int', name='Blind') }}

:   ???

### {{ renderMember(type='body', name='Body') }}

:   Body type

### {{ renderMember(type='bool', name='BodyWet') }}

:   ???

### {{ renderMember(type='bool', name='bShowHelm') }}

:   ???

### {{ renderMember(type='cachedbuff', name='Buff') }}

:   ???

### {{ renderMember(type='int', name='BuffCount') }}

:   ???

### {{ renderMember(type='timestamp', name='BuffDuration') }}

:   ???

### {{ renderMember(type='bool', name='BuffsPopulated') }}

:   ???

### {{ renderMember(type='bool', name='Buyer') }}

:   Is a buyer? (ie. Buyer in the bazaar)

### {{ renderMember(type='cachedbuff', name='CachedBuff') }}

:   Caches buff information cast on others

### {{ renderMember(type='int', name='CachedBuffCount') }}

:   ???

### {{ renderMember(type='bool', name='CanSplashLand') }}

:   <p>TRUE/FALSE on if a splash spell can land...</p><p></p><p><strong>Note:</strong> This check is ONLY for line of sight to the targetindicator (red/green circle)</p>

### {{ renderMember(type='spell', name='Casting') }}

:   Spell, if currently casting (only accurate on yourself, not NPCs or other group members)

### {{ renderMember(type='float', name='CeilingHeightAtCurrLocation') }}

:   ???

### {{ renderMember(type='class', name='Class') }}

:   Class

### {{ renderMember(type='string', name='CleanName') }}

:   The "cleaned up" name

### {{ renderMember(type='int', name='CombatSkillTicks') }}

:   ???

### {{ renderMember(type='string', name='ConColor') }}

:   Returns consider color

    - GREY
    - GREEN
    - LIGHT BLUE
    - BLUE
    - WHITE
    - YELLOW
    - RED

### {{ renderMember(type='int', name='ContractorID') }}

:   ???

### {{ renderMember(type='int', name='CorpseDragCount') }}

:   Number of corpses being dragged

### {{ renderMember(type='int', name='CurrentEndurance') }}

:   Current Endurance points (only updates when target/group)

### {{ renderMember(type='int64', name='CurrentHPs') }}

:   Current hit points

### {{ renderMember(type='int', name='CurrentMana') }}

:   Current Mana points (only updates when target/group)

### {{ renderMember(type='float', name='D') }}

:   Shortcut for -Z (makes Downward positive)

### {{ renderMember(type='bool', name='Dead') }}

:   Dead?

### {{ renderMember(type='deity', name='Deity') }}

:   Deity

### {{ renderMember(type='string', name='DisplayName') }}

:   Name displayed in game (same as EQ's %T)

### {{ renderMember(type='float', name='Distance') }}

:   Distance from player in (x,y)

### {{ renderMember(type='float', name='Distance3D') }}

:   Distance from player in (x,y,z) in 3D

### {{ renderMember(type='float', name='DistanceN') }}

:   Distance from player in Y plane (North/South)

### {{ renderMember(type='float', name='DistancePredict') }}

:   Estimated distance in (x,y), taking into account the spawn's movement speed but not the player's

### {{ renderMember(type='float', name='DistanceU') }}

:   Distance from player in Z plane (Up/Down)

### {{ renderMember(type='float', name='DistanceW') }}

:   Distance from player in X plane (East/West)

### {{ renderMember(type='float', name='DistanceX') }}

:   Distance from player in X plane

### {{ renderMember(type='float', name='DistanceY') }}

:   Distance from player in Y plane

### {{ renderMember(type='float', name='DistanceZ') }}

:   Distance from player in Z plane

### {{ renderMember(type='bool', name='Ducking') }}

:   Ducking?

### {{ renderMember(type='float', name='E') }}

:   Shortcut for -X (makes Eastward positive)

### {{ renderMember(type='string', name='EQLoc') }}

:   Location using EQ format

### {{ renderMember(type='int', name='Equipment') }}

:   returns a inttype, it takes numbers 0-8 or names: head chest arms wrists hands legs feet primary offhand

### {{ renderMember(type='bool', name='FeetWet') }}

:   Feet wet/swimming?

### {{ renderMember(type='bool', name='Feigning') }}

:   Feigning?

### {{ renderMember(type='cachedbuff', name='FindBuff') }}

:   ???

### {{ renderMember(type='bool', name='Fleeing') }}

:   Is your target moving away from you?

### {{ renderMember(type='float', name='FloorZ') }}

:   ???

### {{ renderMember(type='spawn', name='Following') }}

:   The spawn a player is following using /follow on - also returns your pet's target via ${Me.Pet.Following}

### {{ renderMember(type='string', name='Gender') }}

:   Gender

### {{ renderMember(type='bool', name='GM') }}

:   GM or Guide?

### {{ renderMember(type='int', name='GMRank') }}

:   ???

### {{ renderMember(type='bool', name='GroupLeader') }}

:   Group leader?

### {{ renderMember(type='string', name='Guild') }}

:   Guild name

### {{ renderMember(type='string', name='GuildStatus') }}

:   Guild status (Leader, Officer, Member) **NOTE** GuildStatus is no longer present in BETA/TEST/LIVE versions and only available in UF and ROF EMU builds.

### {{ renderMember(type='heading', name='Heading') }}

:   Heading in this direction

### {{ renderMember(type='heading', name='HeadingTo') }}

:   Heading player must travel in to reach this spawn

### {{ renderMember(type='heading', name='HeadingToLoc', params='y, x') }}

:   Heading to the coordinates y,x from the spawn

### {{ renderMember(type='bool', name='HeadWet') }}

:   ???

### {{ renderMember(type='float', name='Height') }}

:   Height

### {{ renderMember(type='bool', name='Holding') }}

:   Is the spawn holding an item?

### {{ renderMember(type='int', name='HoldingAnimation') }}

:   ???

### {{ renderMember(type='bool', name='Hovering') }}

:   Hovering?

### {{ renderMember(type='int', name='ID') }}

:   Spawn ID

### {{ renderMember(type='int', name='InPvPArea') }}

:   ???

### {{ renderMember(type='bool', name='Invis', params='ANY|0') }}

:   Returns whether invis is in effect against specific types of creatures.

    Options are:

    - ANY or 0 - ${Me.Invis[ANY]} or ${Me.Invis[0]} or ${Me.Invis}
    - NORMAL or 1 - ${Me.Invis[NORMAL]} or just ${Me.Invis[1]}
    - UNDEAD or 2 - ${Me.Invis[UNDEAD]} or just ${Me.Invis[2]}
    - ANIMAL or 3 - ${Me.Invis[ANIMAL]} or just ${Me.Invis[3]}
    - SOS or 4 - ${Me.Invis[SOS]} or just ${Me.Invis[4]} returns true IF you are a ROG AND in fact hidden AND have a skill of at least 100 in HIDE AND have the AA for SoS</li></ul>

### {{ renderMember(type='bool', name='IsSummoned') }}

:   Is this a summoned being?

### {{ renderMember(type='bool', name='IsTouchingSwitch') }}

:   ???

### {{ renderMember(type='int', name='Level') }}

:   Level

### {{ renderMember(type='bool', name='Levitating') }}

:   Levitating?

### {{ renderMember(type='bool', name='LFG') }}

:   LFG?

### {{ renderMember(type='string', name='Light') }}

:   Name of the light class this spawn has

### {{ renderMember(type='bool', name='LineOfSight') }}

:   Returns TRUE if spawn is in LoS

### {{ renderMember(type='bool', name='Linkdead') }}

:   Linkdead?

### {{ renderMember(type='string', name='Loc') }}

:   Loc of the spawn

### {{ renderMember(type='string', name='LocYX') }}

:   LocYX of the spawn

### {{ renderMember(type='string', name='LocYXZ') }}

:   ???

### {{ renderMember(type='float', name='Look') }}

:   Looking this angle

### {{ renderMember(type='int', name='Mark') }}

:   Current Raid or Group marked npc mark number (raid first)

### {{ renderMember(type='spawn', name='Master') }}

:   Master, if it is charmed or a pet

### {{ renderMember(type='int', name='MaxEndurance') }}

:   Maximum Endurance points (only updates when target/group)

### {{ renderMember(type='int64', name='MaxHPs') }}

:   Maximum hit points

### {{ renderMember(type='int', name='MaxMana') }}

:   Maximum Mana points (only updates when target/group)

### {{ renderMember(type='float', name='MaxRange') }}

:   The max distance from this spawn for it to hit you

### {{ renderMember(type='float', name='MaxRangeTo') }}

:   The Max distance from this spawn for you to hit it

### {{ renderMember(type='int', name='MercID') }}

:   ???

### {{ renderMember(type='spawn', name='Mount') }}

:   Mount

### {{ renderMember(type='bool', name='Moving') }}

:   Moving?

### {{ renderMember(type='string', name='MQLoc') }}

:   Location using MQ format

### {{ renderMember(type='cachedbuff', name='MyBuff') }}

:   ???

### {{ renderMember(type='int', name='MyBuffCount') }}

:   ???

### {{ renderMember(type='timestamp', name='MyBuffDuration') }}

:   ???
### {{ renderMember(type='float', name='N') }}

:   Synonym for Y

### {{ renderMember(type='string', name='Name') }}

:   Name

### {{ renderMember(type='bool', name='Named') }}

:   Is this a "named" spawn (ie. does it's name not start with an "a" or an "an")

### {{ renderMember(type='spawn', name='NearestSpawn', params='search') }}

:   Find the nearest spawn matching this [Spawn Search](../../reference/general/spawn-search.md), to this spawn (most efficient on yourself)

### {{ renderMember(type='spawn', name='NearestSpawn', params='#, search') }}

:   Find the #th nearest spawn matching this [Spawn Search](../../reference/general/spawn-search.md), to this spawn (most efficient on yourself)

### {{ renderMember(type='spawn', name='Next') }}

:   Next spawn in the list

### {{ renderMember(type='spawn', name='Owner') }}

:   Owner, if mercenary

### {{ renderMember(type='int', name='PctEndurance') }}

: Current endurance as a percent

### {{ renderMember(type='int64', name='PctHPs') }}

:   Current hitpoins as a percent

### {{ renderMember(type='int', name='PctMana') }}

:   Current mana as a percent

### {{ renderMember(type='spawn', name='Pet') }}

:   Returns this spawn's pet, if one exists.

### {{ renderMember(type='int', name='PlayerState') }}

:   returns a mask as an int of which each bit has the following meaning:

    | Value | Meaning |
    | --- | --- |
    | 0 | Idle |
    | 1 | Open |
    | 2 | WeaponSheathed |
    | 4 | Aggressive |
    | 8 | ForcedAggressive |
    | 16 | InstrumentEquipped |
    | 32 | Stunned |
    | 64 | PrimaryWeaponEquipped |
    | 128 | SecondaryWeaponEquipped |

### {{ renderMember(type='spawn', name='Prev') }}

:   Previous spawn in the list

### {{ renderMember(type='int', name='Primary') }}

:   Item ID of anything that may be in the Primary slot

### {{ renderMember(type='race', name='Race') }}

:   Race

### {{ renderMember(type='bool', name='Roleplaying') }}

:   Roleplaying?

### {{ renderMember(type='float', name='S') }}

:   Shortcut for -Y (makes Southward positive)

### {{ renderMember(type='int', name='Secondary') }}

:   Item ID of anything that may be in the Secondary slot

### {{ renderMember(type='int', name='SeeInvis') }}

:   ???

### {{ renderMember(type='bool', name='Sitting') }}

:   Sitting?

### {{ renderMember(type='bool', name='Sneaking') }}

:   Sneaking?

### {{ renderMember(type='int', name='SpawnStatus') }}

:   ???

### {{ renderMember(type='float', name='Speed') }}

:   Speed moving

### {{ renderMember(type='bool', name='Standing') }}

:   Standing?

### {{ renderMember(type='int', name='StandState') }}

:   StandState

### {{ renderMember(type='string', name='State') }}

:   Return current animation state:

    - "STAND"
    - "SIT"
    - "DUCK"
    - "BIND"
    - "FEIGN"
    - "DEAD"
    - "STUN"
    - "HOVER"
    - "MOUNT"
    - "UNKNOWN"

### {{ renderMember(type='bool', name='Stuck') }}

:   Stuck?

### {{ renderMember(type='bool', name='Stunned') }}

:   Stunned?

### {{ renderMember(type='string', name='Suffix') }}

:   Suffix attached to name, eg. of

### {{ renderMember(type='string', name='Surname') }}

:   Last name

### {{ renderMember(type='bool', name='Targetable') }}

:   ???

### {{ renderMember(type='spawn', name='TargetOfTarget') }}

:   ???

### {{ renderMember(type='bool', name='TemporaryPet') }}

:   ???

### {{ renderMember(type='timestamp', name='TimeBeenDead') }}

:   ???

### {{ renderMember(type='string', name='Title') }}

:   Prefix/Title before name

### {{ renderMember(type='bool', name='Trader') }}

:   Trader?

### {{ renderMember(type='string', name='Type') }}

:   The Type of Spawn.

    - "PC"
    - "NPC"
    - "Untargetable"
    - "Mount"
    - "Pet"
    - "Corpse"
    - "Chest"
    - "Trigger"
    - "Trap"
    - "Timer"
    - "Item"
    - "Mercenary"
    - "Aura"
    - "Object"
    - "Banner"
    - "Campfire"
    - "Flyer"

### {{ renderMember(type='float', name='U') }}

:   Synonym for Z

### {{ renderMember(type='bool', name='Underwater') }}

:   Underwater?

### {{ renderMember(type='float', name='W') }}

:   Synonym for X

### {{ renderMember(type='float', name='X') }}

:   X coordinate

### {{ renderMember(type='float', name='Y') }}

:   Y coordinate

### {{ renderMember(type='float', name='Z') }}

:   Z coordinate

### {{ renderMember(type='float', name='N') }}

:   X, the Northward-positive coordinate

### {{ renderMember(type='float', name='W') }}

:   Y, the Westward-positive coordinate

### {{ renderMember(type='float', name='U') }}

:   Z, the Upward-positive coordinate

### {{ renderMember(type='float', name='E') }}

:   Shortcut for -X (makes Eastward positive)

### {{ renderMember(type='float', name='S') }}

:   Shortcut for -Y (makes Southward positive)

### {{ renderMember(type='float', name='D') }}

:   Shortcut for -Z (makes Downward positive)

### [string][string] `To String`

:   Same as **Name**


## Methods

| Name           | Action                 |
| -------------- | ---------------------- |
| **DoAssist**   | assists the spawn      |
| **DoFace**     | Faces target           |
| **DoTarget**   | Targets the spawn      |
| **LeftClick**  | left clicks the spawn  |
| **RightClick** | Right clicks the spawn |

## Examples

| Example | Output |
| --- | --- |
| `${Pet.Equipment[primary].ID}` | ID number of the pet's primary weapon |
| `${Group.Member[mymagesname].Pet.Equipment[primary].ID}` | ID number of the group member's pet's primary weapon |

[body]: datatype-body.md
[bool]: datatype-bool.md
[buff]: datatype-buff.md
[cachedbuff]: datatype-cachedbuff.md
[class]: datatype-class.md
[deity]: datatype-deity.md
[float]: datatype-float.md
[heading]: datatype-heading.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[race]: datatype-race.md
[spawn]: datatype-spawn.md
[spell]: datatype-spell.md
[string]: datatype-string.md
[timestamp]: datatype-timestamp.md
