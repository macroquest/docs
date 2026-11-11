---
tags:
    - datatype
---
# `spawn`

<!--dt-desc-start-->
Represents an in-game spawn.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int AARank
AA rank number
///

/// member | string AATitle
Synonym for Title (deprecated)
///

/// member | string ActorDef
???
///

/// member | bool AFK
AFK?
///

/// member | bool Aggressive
returns TRUE or FALSE if a mob is aggressive or not
///

/// member | int Animation
Current animation ID. See [Animations](../../reference/general/animations.md) for a list of animations.
///

/// member | bool Anonymous
Anonymous
///

/// member | bool Assist
Current Raid or Group assist target?
///

/// member | string AssistName
???
///

/// member | bool Binding
Binding wounds?
///

/// member | int Blind
???
///

/// member | body Body
Body type (see [body types](../general/body-types.md))
///

/// member | bool BodyWet
???
///

/// member | bool bShowHelm
???
///

/// member | cachedbuff Buff
???
///

/// member | int BuffCount
???
///

/// member | timestamp BuffDuration
???
///

/// member | bool BuffsPopulated
???
///

/// member | bool Buyer
Is a buyer? (ie. Buyer in the bazaar)
///

/// member | cachedbuff CachedBuff
Caches buff information cast on others
///

/// member | int CachedBuffCount
???
///

/// member | bool CanEngage
TRUE if you are allowed to engage this spawn under encounter locking (FTE), i.e. **EncounterLockStatus** is "Unlocked" or "Mine". FALSE only when the spawn is locked to someone outside your group or raid.

On clients without encounter locking, this is always TRUE.
///

/// member | bool CanSplashLand
<p>TRUE/FALSE on if a splash spell can land...</p><p></p><p><strong>Note:</strong> This check is ONLY for line of sight to the targetindicator (red/green circle)</p>
///

/// member | spell Casting
Spell, if currently casting (only accurate on yourself, not NPCs or other group members)
///

/// member | float CeilingHeightAtCurrLocation
???
///

/// member | class Class
Class
///

/// member | string CleanName
The "cleaned up" name
///

/// member | int CombatSkillTicks
???
///

/// member | string ConColor
Returns consider color

- GREY
- GREEN
- LIGHT BLUE
- BLUE
- WHITE
- YELLOW
- RED
///

/// member | int ContractorID
???
///

/// member | int CorpseDragCount
Number of corpses being dragged
///

/// member | int CurrentEndurance
Current Endurance points (only updates when target/group)
///

/// member | int64 CurrentHPs
Current hit points
///

/// member | int CurrentMana
Current Mana points (only updates when target/group)
///

/// member | float D
Shortcut for -Z (makes Downward positive)
///

/// member | bool Dead
Dead?
///

/// member | deity Deity
Deity
///

/// member | string DisplayName
Name displayed in game (same as EQ's %T)
///

/// member | float Distance
Distance from player in (x,y)
///

/// member | float Distance3D
Distance from player in (x,y,z) in 3D
///

/// member | float DistanceN
Distance from player in Y plane (North/South)
///

/// member | float DistancePredict
Estimated distance in (x,y), taking into account the spawn's movement speed but not the player's
///

/// member | float DistanceU
Distance from player in Z plane (Up/Down)
///

/// member | float DistanceW
Distance from player in X plane (East/West)
///

/// member | float DistanceX
Distance from player in X plane
///

/// member | float DistanceY
Distance from player in Y plane
///

/// member | float DistanceZ
Distance from player in Z plane
///

/// member | bool Ducking
Ducking?
///

/// member | float E
Shortcut for -X (makes Eastward positive)
///

/// member | spawn EncounterLockOwner
The spawn that currently holds the encounter lock (FTE) on this spawn, or NULL if there is no lock owner. Use sub-members for more detail, e.g. `${Target.EncounterLockOwner.CleanName}` or `${Target.EncounterLockOwner.ID}`.
///

/// member | string EncounterLockStatus
Encounter lock (FTE) status of the spawn, relative to you:

- "Unlocked" - not locked, or opened up with /yell. Anyone can engage.
- "Mine" - locked to you, a member of your group, or a member of your raid.
- "Other" - locked to someone you are not grouped or raided with (also returned if the lock owner can't be resolved).

On clients without encounter locking, this is always "Unlocked".
///

/// member | string EQLoc
Location using EQ format
///

/// member | int Equipment
returns a inttype, it takes numbers 0-8 or names: head chest arms wrists hands legs feet primary offhand
///

/// member | bool FeetWet
Feet wet/swimming?
///

/// member | bool Feigning
Feigning?
///

/// member | cachedbuff FindBuff
???
///

/// member | bool Fleeing
Is your target moving away from you?
///

/// member | float FloorZ
???
///

/// member | spawn Following
The spawn a player is following using /follow on - also returns your pet's target via ${Me.Pet.Following}
///

/// member | string Gender
Gender
///

/// member | bool GM
GM or Guide?
///

/// member | int GMRank
???
///

/// member | bool GroupLeader
Group leader?
///

/// member | string Guild
Guild name
///

/// member | string GuildStatus
Guild status (Leader, Officer, Member) **NOTE** GuildStatus is no longer present in BETA/TEST/LIVE versions and only available in UF and ROF EMU builds.
///

/// member | heading Heading
Heading in this direction
///

/// member | heading HeadingTo
Heading player must travel in to reach this spawn
///

/// member | heading HeadingToLoc[y, x]
Heading to the coordinates y,x from the spawn
///

/// member | bool HeadWet
???
///

/// member | float Height
Height
///

/// member | bool Holding
Is the spawn holding an item?
///

/// member | int HoldingAnimation
???
///

/// member | bool Hovering
Hovering?
///

/// member | int ID
Spawn ID
///

/// member | int InPvPArea
???
///

/// member | bool Invis[ANY|0]
Returns whether invis is in effect against specific types of creatures.

Options are:

- ANY or 0 - ${Me.Invis[ANY]} or ${Me.Invis[0]} or ${Me.Invis}
- NORMAL or 1 - ${Me.Invis[NORMAL]} or just ${Me.Invis[1]}
- UNDEAD or 2 - ${Me.Invis[UNDEAD]} or just ${Me.Invis[2]}
- ANIMAL or 3 - ${Me.Invis[ANIMAL]} or just ${Me.Invis[3]}
- SOS or 4 - ${Me.Invis[SOS]} or just ${Me.Invis[4]} returns true IF you are a ROG AND in fact hidden AND have a skill of at least 100 in HIDE AND have the AA for SoS</li></ul>
///

/// member | bool IsSummoned
Is this a summoned being?
///

/// member | bool IsTouchingSwitch
???
///

/// member | int Level
Level
///

/// member | bool Levitating
Levitating?
///

/// member | bool LFG
LFG?
///

/// member | string Light
Name of the light class this spawn has
///

/// member | bool LineOfSight
Returns TRUE if spawn is in LoS
///

/// member | bool Linkdead
Linkdead?
///

/// member | string Loc
Loc of the spawn
///

/// member | string LocYX
LocYX of the spawn
///

/// member | string LocYXZ
???
///

/// member | float Look
Looking this angle
///

/// member | int Mark
Current Raid or Group marked npc mark number (raid first)
///

/// member | spawn Master
Master, if it is charmed or a pet
///

/// member | int MaxEndurance
Maximum Endurance points (only updates when target/group)
///

/// member | int64 MaxHPs
Maximum hit points
///

/// member | int MaxMana
Maximum Mana points (only updates when target/group)
///

/// member | float MaxRange
The max distance from this spawn for it to hit you
///

/// member | float MaxRangeTo
The Max distance from this spawn for you to hit it
///

/// member | int MercID
???
///

/// member | spawn Mount
Mount
///

/// member | bool Moving
Moving?
///

/// member | string MQLoc
Location using MQ format
///

/// member | cachedbuff MyBuff
???
///

/// member | int MyBuffCount
???
///

/// member | timestamp MyBuffDuration
???
///
/// member | float N
Synonym for Y
///

/// member | string Name
Name
///

/// member | bool Named
Is this a "named" spawn (ie. does it's name not start with an "a" or an "an")
///

/// member | spawn NearestSpawn[search]
Find the nearest spawn matching this [Spawn Search](../../reference/general/spawn-search.md), to this spawn (most efficient on yourself)
///

/// member | spawn NearestSpawn[#, search]
Find the #th nearest spawn matching this [Spawn Search](../../reference/general/spawn-search.md), to this spawn (most efficient on yourself)
///

/// member | spawn Next
Next spawn in the list
///

/// member | spawn Owner
Owner, if mercenary
///

/// member | int PctEndurance
Current endurance as a percent
///

/// member | int64 PctHPs
Current hitpoins as a percent
///

/// member | int PctMana
Current mana as a percent
///

/// member | spawn Pet
Returns this spawn's pet, if one exists.
///

/// member | int PlayerState
returns a mask as an int of which each bit has the following meaning:

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
///

/// member | spawn Prev
Previous spawn in the list
///

/// member | int Primary
Item ID of anything that may be in the Primary slot
///

/// member | race Race
Race
///

/// member | bool Roleplaying
Roleplaying?
///

/// member | float S
Shortcut for -Y (makes Southward positive)
///

/// member | int Secondary
Item ID of anything that may be in the Secondary slot
///

/// member | int SeeInvis
???
///

/// member | bool Sitting
Sitting?
///

/// member | bool Sneaking
Sneaking?
///

/// member | int SpawnStatus
???
///

/// member | float Speed
Speed moving
///

/// member | bool Standing
Standing?
///

/// member | int StandState
StandState
///

/// member | string State
Return current animation state:

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
///

/// member | bool Stuck
Stuck?
///

/// member | bool Stunned
Stunned?
///

/// member | string Suffix
Suffix attached to name, eg. of
///

/// member | string Surname
Last name
///

/// member | bool Targetable
???
///

/// member | spawn TargetOfTarget
???
///

/// member | bool TemporaryPet
???
///

/// member | timestamp TimeBeenDead
???
///

/// member | string Title
Prefix/Title before name
///

/// member | bool Trader
Trader?
///

/// member | string Type
The Type of Spawn.

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
///

/// member | float U
Synonym for Z
///

/// member | bool Underwater
Underwater?
///

/// member | float W
Synonym for X
///

/// member | float X
X coordinate
///

/// member | float Y
Y coordinate
///

/// member | float Z
Z coordinate
///

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->

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
| `${Target.CanEngage}` | TRUE if your target isn't encounter locked to someone outside your group/raid |
| `${Target.EncounterLockStatus}` | "Unlocked", "Mine", or "Other" |
| `${Target.EncounterLockOwner.CleanName}` | Name of the player holding the encounter lock on your target |
| `/if (!${Target.CanEngage}) /squelch /target clear` | Drop a target that's locked to another player |
<!--dt-linkrefs-start-->
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
<!--dt-linkrefs-end-->
