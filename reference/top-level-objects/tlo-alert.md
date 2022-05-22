---
tags:
    - tlo
---

# `Alert`

Provides access to spawn search filter criteria in alerts. Alerts are created using [/alert](../../reference/commands/alert.md).

## Forms

| **Type** | **Form** | **Description** |
| :--- | :--- | :--- |
| [_alert_](#alert-type) | **Alert**[ _ID_ ] | Retrieve information for the alert category by its id |
| [_string_](../data-types/datatype-string.md) | **Alert** | Returns pipe `|` separated list of alert ids |

## Associated DataTypes

### `alert` Type

Provides access to the values of an alert.

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_alertlist_](#alertlist-type) | **List**[ _Index_ ] | Get the item from the list at the specified index |
| [_int_](../data-types/datatype-int.md) | **Size** | Get the number of alerts |
| [_string_](../data-types/datatype-string.md) | **To String** | Returns **Size** as a string. |

### `alertlist` Type

Provides access to the properties of a spawn search associated with an alert. For a spawn to be entered
into an alert it must match all the criteria specified by the alert list.

See Also: [Spawn Search](../general/spawn-search.md).

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](../data-types/datatype-int.md)       | **AlertList**        | Any spawn on the associated alert list |
| [_bool_](../data-types/datatype-bool.md)     | **bAlert**           | Indicates usage of **alert** filter |
| [_bool_](../data-types/datatype-bool.md)     | **bAura**            | Any aur. |
| [_bool_](../data-types/datatype-bool.md)     | **bBanker**          | Any banker |
| [_bool_](../data-types/datatype-bool.md)     | **bBanner**          | Any banner |
| [_bool_](../data-types/datatype-bool.md)     | **bCampfire**        | Any campfire |
| [_bool_](../data-types/datatype-bool.md)     | **bDps**             | Any player that is a DPS class |
| [_bool_](../data-types/datatype-bool.md)     | **bExactName**       | Name match requiries an exact match |
| [_bool_](../data-types/datatype-bool.md)     | **bFellowship**      | Any member of the fellowship |
| [_bool_](../data-types/datatype-bool.md)     | **bGM**              | Any player flagged as a GM |
| [_bool_](../data-types/datatype-bool.md)     | **bGroup**           | Any member of the group |
| [_bool_](../data-types/datatype-bool.md)     | **bHealer**          | Any player that is a healer class |
| [_bool_](../data-types/datatype-bool.md)     | **bKnight**          | Any player that is a knight |
| [_bool_](../data-types/datatype-bool.md)     | **bKnownLocation**   | Indicates usage of a **loc** filter |
| [_bool_](../data-types/datatype-bool.md)     | **bLFG**             | Any player that is flagged as LFG |
| [_bool_](../data-types/datatype-bool.md)     | **bLight**           | Indicates usage of a **light** filter |
| [_bool_](../data-types/datatype-bool.md)     | **bLoS**             | Any spawn in line of sight |
| [_bool_](../data-types/datatype-bool.md)     | **bMerchant**        | Any merchant |
| [_bool_](../data-types/datatype-bool.md)     | **bNamed**           | Any "named" NPC |
| [_bool_](../data-types/datatype-bool.md)     | **bNearAlert**       | Indicates usage of **nearalert** filter |
| [_bool_](../data-types/datatype-bool.md)     | **bNoAlert**         | Indicates usage of **noalert** filter |
| [_bool_](../data-types/datatype-bool.md)     | **bNoGroup**         | Exclude any player that is in the group |
| [_bool_](../data-types/datatype-bool.md)     | **bNoGuild**         | Exclude any player that is in the guild |
| [_bool_](../data-types/datatype-bool.md)     | **bNoPet**           | Exclude any spawn that is a pet |
| [_bool_](../data-types/datatype-bool.md)     | **bNotNearAlert**    | Indicates usage of **notnearalert** filter |
| [_string_](../data-types/datatype-string.md) | **BodyType**         | Any spawn with given body type |
| [_bool_](../data-types/datatype-bool.md)     | **bRaid**            | Any member of the raid |
| [_bool_](../data-types/datatype-bool.md)     | **bSlower**          | Any player that is a slower |
| [_bool_](../data-types/datatype-bool.md)     | **bSpawnID**         | Indicates usage of the **id** filter |
| [_bool_](../data-types/datatype-bool.md)     | **bTank**            | Any player that is a tank class |
| [_bool_](../data-types/datatype-bool.md)     | **bTargetable**      | Any spawn that is targetable |
| [_bool_](../data-types/datatype-bool.md)     | **bTargNext**        | Indicates usage of the **next** filter |
| [_bool_](../data-types/datatype-bool.md)     | **bTargPrev**        | Indicates usage of the **prev** filter |
| [_bool_](../data-types/datatype-bool.md)     | **bTrader**          | Any player that is a trader |
| [_bool_](../data-types/datatype-bool.md)     | **bTributeMaster**   | Any NPC that is a tribute master |
| [_string_](../data-types/datatype-string.md) | **Class**            | Any spawn that is the given class |
| [_double_](../data-types/datatype-double.md)  | **FRadius**          | Any spawn that is given distance from the given **loc** filter |
| [_int_](../data-types/datatype-int.md)       | **FromSpawnID**      | Search starts at given spawn id |
| [_int64_](../data-types/datatype-int64.md)   | **GuildID**          | Any member of the guild with the given id |
| [_string_](../data-types/datatype-string.md) | **Light**            | Any spawn that is equipped with the given light source |
| [_int_](../data-types/datatype-int.md)       | **MaxLevel**         | Any spawn that is at this level or lower |
| [_int_](../data-types/datatype-int.md)       | **MinLevel**         | Any spawn that is at this level or greater |
| [_string_](../data-types/datatype-string.md) | **Name**             | Any spawn with the given name |
| [_int_](../data-types/datatype-int.md)       | **NearAlertList**    | Any spawn near the given alert list |
| [_int_](../data-types/datatype-int.md)       | **NoAlertList**      | Excludes any spawn in the given alert list |
| [_int_](../data-types/datatype-int.md)       | **NotID**            | Excludes any spawn with the given id |
| [_int_](../data-types/datatype-int.md)       | **NotNearAlertList** | Excludes any spawn near the given alert list |
| [_int_](../data-types/datatype-int.md)       | **PlayerState**      | Any spawn with the given state |
| [_string_](../data-types/datatype-string.md) | **Race**             | Any spawn with the given race |
| [_float_](../data-types/datatype-float.md)   | **Radius**           | Excludes the spawn if any player is within this distance (**nopcnear** filter) |
| [_int_](../data-types/datatype-int.md)       | **SortBy**           | Indicates the sort order of the filter |
| [_spawn_](../data-types/datatype-spawn.md)   | **Spawn**            | If an ID or Name is part of the filter, attempts to return a spawn with the matching ID or Name |
| [_int_](../data-types/datatype-int.md)       | **SpawnID**          | Any spawn with the given Spawn ID |
| [_int_](../data-types/datatype-int.md)       | **SpawnType**        | Any spawn with the given type |
| [_float_](../data-types/datatype-float.md)   | **xLoc**             | `x` component of the **loc** filter |
| [_float_](../data-types/datatype-float.md)   | **yLoc**             | `y` component of the **loc** filter |
| [_double_](../data-types/datatype-double.md) | **ZRadius**          | `z` distance component of the **loc** filter |

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
