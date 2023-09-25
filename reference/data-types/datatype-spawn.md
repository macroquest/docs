---
tags:
    - datatype
---
# `spawn`

Represents an in-game spawn.

## Members

### [int][int] `AARank`

:   AA rank number

### `AATitle`

:   

### `ActorDef`

:   

### [bool][bool] `AFK`

:   AFK?

### [bool][bool] `Aggressive`

:   returns TRUE or FALSE if a mob is aggressive or not

### [int][int] `Animation`

:   Current animation ID. See [Animations](../../reference/general/animations.md) for a list of animations.

### [bool][bool] `Anonymous`

:   Anonymous

### [bool][bool] `Assist`

:   Current Raid or Group assist target?

### [bool][bool] `Binding`

:   Binding wounds?

### `Blind`

:   

### [body][body] `Body`

:   Body type

### `BodyWet`

:   

### `bShowHelm`

:   

### `Buff`

:   

### `BuffCount`

:   

### `BuffDuration`

:   

### `BuffsPopulated`

:   

### [bool][bool] `Buyer`

:   Is a buyer? (ie. Buyer in the bazaar)

### [cachedbuff][cachedbuff] `CachedBuff`

:   Caches buff information cast on others

### `CachedBuffCount`

:   

### [bool][bool] `CanSplashLand`

:   <p>TRUE/FALSE on if a splash spell can land...</p><p></p><p><strong>Note:</strong> This check is ONLY for line of sight to the targetindicator (red/green circle)</p>

### [spell][spell] `Casting`

:   Spell, if currently casting (only accurate on yourself, not NPCs or other group members)

### `CeilingHeightAtCurrLocation`

:   

### [class][class] `Class`

:   Class

### [string][string] `CleanName`

:   The "cleaned up" name

### `CombatSkillTicks`

:   

### [string][string] `ConColor`

:   GREY, GREEN, LIGHT BLUE, BLUE, WHITE, YELLOW, RED

### `ContractorID`

:   

### [int][int] `CurrentEndurance`

:   Current Endurance points (only updates when target/group)

### [int64][int64] `CurrentHPs`

:   Current hit points

### [int][int] `CurrentMana`

:   Current Mana points (only updates when target/group)

### [bool][bool] `Dead`

:   Dead?

### [deity][deity] `Deity`

:   Deity

### [string][string] `DisplayName`

:   Name displayed in game (same as EQ's %T)

### [float][float] `Distance`

:   Distance from player in (x,y)

### [float][float] `Distance3D`

:   Distance from player in (x,y,z) in 3D

### [float][float] `DistanceN`

:   Distance from player in Y plane (North/South)

### [float][float] `DistancePredict`

:   Estimated distance in (x,y), taking into account the spawn's movement speed but not the player's

### [float][float] `DistanceU`

:   Distance from player in Z plane (Up/Down)

### [float][float] `DistanceW`

:   Distance from player in X plane (East/West)

### [float][float] `DistanceX`

:   Distance from player in X plane

### [float][float] `DistanceY`

:   Distance from player in Y plane

### [float][float] `DistanceZ`

:   Distance from player in Z plane

### [bool][bool] `Ducking`

:   Ducking?

### [float][float] `EQLoc`

:   Location using EQ format

### [int][int] `Equipment`

:   returns a inttype, it takes numbers 0-8 or names: head chest arms wrists hands legs feet primary offhand

### [bool][bool] `FeetWet`

:   Feet wet/swimming?

### [bool][bool] `Feigning`

:   Feigning?

### `FindBuff`

:   

### [bool][bool] `Fleeing`

:   Is your target moving away from you?

### `FloorZ`

:   

### [spawn][spawn] `Following`

:   The spawn a player is following using /follow on - also returns your pet's target via ${Me.Pet.Following}

### [string][string] `Gender`

:   Gender

### [bool][bool] `GM`

:   GM or Guide?

### `GMRank`

:   

### [bool][bool] `GroupLeader`

:   Group leader?

### [string][string] `Guild`

:   Guild name

### [string][string] `GuildStatus`

:   Guild status (Leader, Officer, Member) **NOTE** GuildStatus is no longer present in BETA/TEST/LIVE versions and only available in UF and ROF EMU builds.

### [heading][heading] `Heading`

:   Heading in this direction

### [heading][heading] `HeadingTo`

:   Heading player must travel in to reach this spawn

### [heading][heading] `HeadingToLoc[y, x]`

:   Heading to the coordinates y,x from the spawn

### `HeadWet`

:   

### [float][float] `Height`

:   Height

### [bool][bool] `Holding`

:   Is the spawn holding an item?

### `HoldingAnimation`

:   

### [bool][bool] `Hovering`

:   Hovering?

### [int][int] `ID`

:   Spawn ID

### `InPvPArea`

:   

### [bool][bool] `Invis[ANY|0]`

:   <p>Gives TRUE/FALSE returns. Options are:</p><ul><li>ANY or 0 - ${Me.Invis[ANY]} or ${Me.Invis[0]} or ${Me.Invis}</li><li>NORMAL or 1 - ${Me.Invis[NORMAL]} or just ${Me.Invis[1]}</li><li>UNDEAD or 2 - ${Me.Invis[UNDEAD]} or just ${Me.Invis[2]}</li><li>ANIMAL or 3 - ${Me.Invis[ANIMAL]} or just ${Me.Invis[3]}</li><li>SOS or 4 - ${Me.Invis[SOS]} or just ${Me.Invis[4]} returns true IF you are a ROG AND in fact hidden AND have a skill of at least 100 in HIDE AND have the AA for SoS</li></ul>

### `IsSummoned`

:   

### `IsTouchingSwitch`

:   

### [int][int] `Level`

:   Level

### [bool][bool] `Levitating`

:   Levitating?

### [bool][bool] `LFG`

:   LFG?

### [string][string] `Light`

:   Name of the light class this spawn has

### [bool][bool] `LineOfSight`

:   Returns TRUE if spawn is in LoS

### [bool][bool] `Linkdead`

:   Linkdead?

### [string][string] `Loc`

:   Loc of the spawn

### [string][string] `LocYX`

:   LocYX of the spawn

### `LocYXZ`

:   

### [float][float] `Look`

:   Looking this angle

### [int][int] `Mark`

:   Current Raid or Group marked npc mark number (raid first)

### [spawn][spawn] `Master`

:   Master, if it is charmed or a pet

### [int][int] `MaxEndurance`

:   Maximum Endurance points (only updates when target/group)

### [int64][int64] `MaxHPs`

:   Maximum hit points

### [int][int] `MaxMana`

:   Maximum Mana points (only updates when target/group)

### [float][float] `MaxRange`

:   The max distance from this spawn for it to hit you

### [float][float] `MaxRangeTo`

:   The Max distance from this spawn for you to hit it

### `MercID`

:   

### [spawn][spawn] `Mount`

:   Mount

### [bool][bool] `Moving`

:   Moving?

### [float][float] `MQLoc`

:   Location using MQ format

### `MyBuff`

:   

### `MyBuffCount`

:   

### `MyBuffDuration`

:   

### [string][string] `Name`

:   Name

### [bool][bool] `Named`

:   Is this a "named" spawn (ie. does it's name not start with an "a" or an "an")

### [spawn][spawn] `NearestSpawn[search]`

:   Find the nearest spawn matching this [Spawn Search](../../reference/general/spawn-search.md), to this spawn (most efficient on yourself)

### [spawn][spawn] `NearestSpawn[#, search]`

:   Find the #th nearest spawn matching this [Spawn Search](../../reference/general/spawn-search.md), to this spawn (most efficient on yourself)

### [spawn][spawn] `Next`

:   Next spawn in the list

### [spawn][spawn] `Owner`

:   Owner, if mercenary

### [int64][int64] `PctHPs`

:   Percent hit points

### `PctMana`

:   

### [spawn][spawn] `Pet`

:   Pet

### [int][int] `PlayerState`

:   returns a mask as an inttype which has the following meaning: 0=Idle 1=Open 2=WeaponSheathed 4=Aggressive 8=ForcedAggressive 0x10=InstrumentEquipped 0x20=Stunned 0x40=PrimaryWeaponEquipped 0x80=SecondaryWeaponEquipped

### [spawn][spawn] `Prev`

:   Previous spawn in the list

### [int][int] `Primary`

:   Item ID of anything that may be in the Primary slot

### [race][race] `Race`

:   Race

### [bool][bool] `Roleplaying`

:   Roleplaying?

### [int][int] `Secondary`

:   Item ID of anything that may be in the Secondary slot

### `SeeInvis`

:   

### [bool][bool] `Sitting`

:   Sitting?

### [bool][bool] `Sneaking`

:   Sneaking?

### `SpawnStatus`

:   

### [float][float] `Speed`

:   Speed moving

### [bool][bool] `Standing`

:   Standing?

### [int][int] `StandState`

:   StandState

### [string][string] `State`

:   STAND, SIT, DUCK, BIND, FEIGN, DEAD, STUN, HOVER, MOUNT, UNKNOWN

### [bool][bool] `Stuck`

:   Stuck?

### [bool][bool] `Stunned`

:   Stunned?

### [string][string] `Suffix`

:   Suffix attached to name, eg. of

### [string][string] `Surname`

:   Last name

### `Targetable`

:   

### `TargetOfTarget`

:   

### `TemporaryPet`

:   

### `TimeBeenDead`

:   

### [string][string] `Title`

:   Prefix/Title before name

### [bool][bool] `Trader`

:   Trader?

### [string][string] `Type`

:   PC, NPC, Untargetable, Mount, Pet, Corpse, Chest, Trigger, Trap, Timer, Item, Mercenary, Aura, Object, Banner, Campfire, Flyer

### [bool][bool] `Underwater`

:   Underwater?

### [float][float] `X`

:   X coordinate

### [float][float] `Y`

:   Y coordinate

### [float][float] `Z`

:   Z coordinate

### [float][float] `N`

:   X, the Northward-positive coordinate

### [float][float] `W`

:   Y, the Westward-positive coordinate

### [float][float] `U`

:   Z, the Upward-positive coordinate

### [float][float] `E`

:   Shortcut for -X (makes Eastward positive)

### [float][float] `S`

:   Shortcut for -Y (makes Southward positive)

### [float][float] `D`

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

| **Example**                                              | **Output**                                           |
| -------------------------------------------------------- | ---------------------------------------------------- |
| `${Pet.Equipment[primary].ID}`                           | ID number of the pet's primary weapon                |
| `${Group.Member[mymagesname].Pet.Equipment[primary].ID}` | ID number of the group member's pet's primary weapon |

[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
[zone]: datatype-zone.md
[fellowshipmember]: datatype-fellowshipmember.md
[class]: datatype-class.md
[heading]: datatype-heading.md
[ground]: datatype-ground.md
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[double]: datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
[raidmember]: datatype-raidmember.md
[body]: datatype-body.md
[cachedbuff]: datatype-cachedbuff.md
[deity]: datatype-deity.md
[race]: datatype-race.md
