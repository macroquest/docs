---
tags:
    - tlo
---
# `Alert`

Provides access to spawn search filter criteria in alerts. Alerts are created using [/alert](../../reference/commands/alert.md).

## Forms

### [alert][alert] `Alert[ID]`

:   Retrieve information for the alert category by its id

| [string][string] | **Alert** | Returns pipe `|` separated list of alert ids |

## Associated DataTypes

### `alert` Type

Provides access to the values of an alert.

### [alertlist][alertlist] `List[Index]`

:   Get the item from the list at the specified index

### [int][int] `Size`

:   Get the number of alerts

### [string][string] `To String`

:   Returns **Size** as a string.


### `alertlist` Type

Provides access to the properties of a spawn search associated with an alert. For a spawn to be entered
into an alert it must match all the criteria specified by the alert list.

See Also: [Spawn Search](../general/spawn-search.md).

### [int][int] `AlertList`

:   Any spawn on the associated alert list

### [bool][bool] `bAlert`

:   Indicates usage of **alert** filter

### [bool][bool] `bAura`

:   Any aur.

### [bool][bool] `bBanker`

:   Any banker

### [bool][bool] `bBanner`

:   Any banner

### [bool][bool] `bCampfire`

:   Any campfire

### [bool][bool] `bDps`

:   Any player that is a DPS class

### [bool][bool] `bExactName`

:   Name match requiries an exact match

### [bool][bool] `bFellowship`

:   Any member of the fellowship

### [bool][bool] `bGM`

:   Any player flagged as a GM

### [bool][bool] `bGroup`

:   Any member of the group

### [bool][bool] `bHealer`

:   Any player that is a healer class

### [bool][bool] `bKnight`

:   Any player that is a knight

### [bool][bool] `bKnownLocation`

:   Indicates usage of a **loc** filter

### [bool][bool] `bLFG`

:   Any player that is flagged as LFG

### [bool][bool] `bLight`

:   Indicates usage of a **light** filter

### [bool][bool] `bLoS`

:   Any spawn in line of sight

### [bool][bool] `bMerchant`

:   Any merchant

### [bool][bool] `bNamed`

:   Any "named" NPC

### [bool][bool] `bNearAlert`

:   Indicates usage of **nearalert** filter

### [bool][bool] `bNoAlert`

:   Indicates usage of **noalert** filter

### [bool][bool] `bNoGroup`

:   Exclude any player that is in the group

### [bool][bool] `bNoGuild`

:   Exclude any player that is in the guild

### [bool][bool] `bNoPet`

:   Exclude any spawn that is a pet

### [bool][bool] `bNotNearAlert`

:   Indicates usage of **notnearalert** filter

### [string][string] `BodyType`

:   Any spawn with given body type

### [bool][bool] `bRaid`

:   Any member of the raid

### [bool][bool] `bSlower`

:   Any player that is a slower

### [bool][bool] `bSpawnID`

:   Indicates usage of the **id** filter

### [bool][bool] `bTank`

:   Any player that is a tank class

### [bool][bool] `bTargetable`

:   Any spawn that is targetable

### [bool][bool] `bTargNext`

:   Indicates usage of the **next** filter

### [bool][bool] `bTargPrev`

:   Indicates usage of the **prev** filter

### [bool][bool] `bTrader`

:   Any player that is a trader

### [bool][bool] `bTributeMaster`

:   Any NPC that is a tribute master

### [string][string] `Class`

:   Any spawn that is the given class

### [double][double] `FRadius`

:   Any spawn that is given distance from the given **loc** filter

### [int][int] `FromSpawnID`

:   Search starts at given spawn id

### [int64][int64] `GuildID`

:   Any member of the guild with the given id

### [string][string] `Light`

:   Any spawn that is equipped with the given light source

### [int][int] `MaxLevel`

:   Any spawn that is at this level or lower

### [int][int] `MinLevel`

:   Any spawn that is at this level or greater

### [string][string] `Name`

:   Any spawn with the given name

### [int][int] `NearAlertList`

:   Any spawn near the given alert list

### [int][int] `NoAlertList`

:   Excludes any spawn in the given alert list

### [int][int] `NotID`

:   Excludes any spawn with the given id

### [int][int] `NotNearAlertList`

:   Excludes any spawn near the given alert list

### [int][int] `PlayerState`

:   Any spawn with the given state

### [string][string] `Race`

:   Any spawn with the given race

### [float][float] `Radius`

:   Excludes the spawn if any player is within this distance (**nopcnear** filter)

### [int][int] `SortBy`

:   Indicates the sort order of the filter

### [spawn][spawn] `Spawn`

:   If an ID or Name is part of the filter, attempts to return a spawn with the matching ID or Name

### [int][int] `SpawnID`

:   Any spawn with the given Spawn ID

### [int][int] `SpawnType`

:   Any spawn with the given type

### [float][float] `xLoc`

:   `x` component of the **loc** filter

### [float][float] `yLoc`

:   `y` component of the **loc** filter

### [double][double] `ZRadius`

:   `z` distance component of the **loc** filter


## Usage Examples

=== "MQScript"

    ```
    | Add an alert entry for Fippy to Alert list 1
    /alert add 1 Fippy

    | Will output 'Fippy'
    /echo ${Alert[1].List[0].Name}

    | Add an alert entry using our Spawn ID
    /alert add 1 id ${Me.ID}

    | Will output your Spawn ID
    /echo ${Alert[1].List[1].SpawnID}

    | Will output the number of alerts in list 1
    /echo ${Alert[1].Size}
    ```

=== "Lua"

    ```lua
    -- Add an alert entry for Fippy to Alert list 1
    mq.cmd('/alert add 1 Fippy')

    -- Will output 'Fippy'
    print(mq.TLO.Alert(1).List(0).Name())

    -- Add an alert entry using our Spawn ID
    mq.cmdf('/alert add 1 id %d', mq.TLO.Me.ID())

    -- Will output our Spawn ID
    print(mq.TLO.Alert(1).List(1).SpawnID())

    -- Will output the number of alerts in list 1
    print(mq.TLO.Alert(1).Size())
    ```
[int]: ../data-types/datatype-int.md
[string]: ../data-types/datatype-string.md
[bool]: ../data-types/datatype-bool.md
[achievement]: ../data-types/datatype-achievement.md
[achievementcat]: ../data-types/datatype-achievementcat.md
[int64]: ../data-types/datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: ../data-types/datatype-float.md
[spawn]: ../data-types/datatype-spawn.md
[double]: ../data-types/datatype-double.md
[alert]: #alert-type
[alertlist]: #alertlist-type
