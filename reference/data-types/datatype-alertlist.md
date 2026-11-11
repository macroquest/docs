---
tags:
    - datatype
---
# `alertlist`

<!--dt-desc-start-->
Provides access to the properties of a spawn search associated with an alert. For a spawn to be entered into an alert it must match all the criteria specified by the alert list.

See Also: [Spawn Search](../general/spawn-search.md).
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int AlertList
Any spawn on the associated alert list
///

/// member | bool bAlert
Indicates usage of **alert** filter
///

/// member | bool bAura
Any aur.
///

/// member | bool bBanker
Any banker
///

/// member | bool bBanner
Any banner
///

/// member | bool bCampfire
Any campfire
///

/// member | bool bDps
Any player that is a DPS class
///

/// member | bool bExactName
Name match requiries an exact match
///

/// member | bool bFellowship
Any member of the fellowship
///

/// member | bool bGM
Any player flagged as a GM
///

/// member | bool bGroup
Any member of the group
///

/// member | bool bHealer
Any player that is a healer class
///

/// member | bool bKnight
Any player that is a knight
///

/// member | bool bKnownLocation
Indicates usage of a **loc** filter
///

/// member | bool bLFG
Any player that is flagged as LFG
///

/// member | bool bLight
Indicates usage of a **light** filter
///

/// member | bool bLoS
Any spawn in line of sight
///

/// member | bool bMerchant
Any merchant
///

/// member | bool bNamed
Any "named" NPC
///

/// member | bool bNearAlert
Indicates usage of **nearalert** filter
///

/// member | bool bNoAlert
Indicates usage of **noalert** filter
///

/// member | bool bNoGroup
Exclude any player that is in the group
///

/// member | bool bNoGuild
Exclude any player that is in the guild
///

/// member | bool bNoPet
Exclude any spawn that is a pet
///

/// member | bool bNotNearAlert
Indicates usage of **notnearalert** filter
///

/// member | string BodyType
Any spawn with given [body type](../general/body-types.md)
///

/// member | bool bRaid
Any member of the raid
///

/// member | bool bSlower
Any player that is a slower
///

/// member | bool bSpawnID
Indicates usage of the **id** filter
///

/// member | bool bTank
Any player that is a tank class
///

/// member | bool bTargetable
Any spawn that is targetable
///

/// member | bool bTargNext
Indicates usage of the **next** filter
///

/// member | bool bTargPrev
Indicates usage of the **prev** filter
///

/// member | bool bTrader
Any player that is a trader
///

/// member | bool bTributeMaster
Any NPC that is a tribute master
///

/// member | string Class
Any spawn that is the given class
///

/// member | double FRadius
Any spawn that is given distance from the given **loc** filter
///

/// member | int FromSpawnID
Search starts at given spawn id
///

/// member | int64 GuildID
Any member of the guild with the given id
///

/// member | string Light
Any spawn that is equipped with the given light source
///

/// member | int MaxLevel
Any spawn that is at this level or lower
///

/// member | int MinLevel
Any spawn that is at this level or greater
///

/// member | string Name
Any spawn with the given name
///

/// member | int NearAlertList
Any spawn near the given alert list
///

/// member | int NoAlertList
Excludes any spawn in the given alert list
///

/// member | int NotID
Excludes any spawn with the given id
///

/// member | int NotNearAlertList
Excludes any spawn near the given alert list
///

/// member | int PlayerState
Any spawn with the given state
///

/// member | string Race
Any spawn with the given race
///

/// member | float Radius
Excludes the spawn if any player is within this distance (**nopcnear** filter)
///

/// member | int SortBy
Indicates the sort order of the filter
///

/// member | spawn Spawn
If an ID or Name is part of the filter, attempts to return a spawn with the matching ID or Name
///

/// member | int SpawnID
Any spawn with the given Spawn ID
///

/// member | int SpawnType
Any spawn with the given type
///

/// member | float xLoc
`x` component of the **loc** filter
///

/// member | float yLoc
`y` component of the **loc** filter
///

/// member | double ZRadius
`z` distance component of the **loc** filter
///
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[double]: datatype-double.md
[float]: datatype-float.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[spawn]: datatype-spawn.md
[string]: datatype-string.md
<!--dt-linkrefs-end--> 