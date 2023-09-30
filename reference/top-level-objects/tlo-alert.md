---
tags:
    - tlo
---
# `Alert`

Provides access to spawn search filter criteria in alerts. Alerts are created using [/alert](../../reference/commands/alert.md).

## Forms

### {{ renderMember(type='alert', name='Alert', params='ID') }} 

:   Retrieve information for the alert category by its id

| [string][string] | **Alert** | Returns pipe `|` separated list of alert ids |

## Associated DataTypes

### {{ renderMember(name='alert') }} 

Provides access to the values of an alert.

### {{ renderMember(type='alertlist', name='List', params='Index') }} 

:   Get the item from the list at the specified index

### {{ renderMember(type='int', name='Size') }} 

:   Get the number of alerts

### [string][string] `To String`

:   Returns **Size** as a string.


### {{ renderMember(name='alertlist') }} 

Provides access to the properties of a spawn search associated with an alert. For a spawn to be entered
into an alert it must match all the criteria specified by the alert list.

See Also: [Spawn Search](../general/spawn-search.md).

### {{ renderMember(type='int', name='AlertList') }} 

:   Any spawn on the associated alert list

### {{ renderMember(type='bool', name='bAlert') }} 

:   Indicates usage of **alert** filter

### {{ renderMember(type='bool', name='bAura') }} 

:   Any aur.

### {{ renderMember(type='bool', name='bBanker') }} 

:   Any banker

### {{ renderMember(type='bool', name='bBanner') }} 

:   Any banner

### {{ renderMember(type='bool', name='bCampfire') }} 

:   Any campfire

### {{ renderMember(type='bool', name='bDps') }} 

:   Any player that is a DPS class

### {{ renderMember(type='bool', name='bExactName') }} 

:   Name match requiries an exact match

### {{ renderMember(type='bool', name='bFellowship') }} 

:   Any member of the fellowship

### {{ renderMember(type='bool', name='bGM') }} 

:   Any player flagged as a GM

### {{ renderMember(type='bool', name='bGroup') }} 

:   Any member of the group

### {{ renderMember(type='bool', name='bHealer') }} 

:   Any player that is a healer class

### {{ renderMember(type='bool', name='bKnight') }} 

:   Any player that is a knight

### {{ renderMember(type='bool', name='bKnownLocation') }} 

:   Indicates usage of a **loc** filter

### {{ renderMember(type='bool', name='bLFG') }} 

:   Any player that is flagged as LFG

### {{ renderMember(type='bool', name='bLight') }} 

:   Indicates usage of a **light** filter

### {{ renderMember(type='bool', name='bLoS') }} 

:   Any spawn in line of sight

### {{ renderMember(type='bool', name='bMerchant') }} 

:   Any merchant

### {{ renderMember(type='bool', name='bNamed') }} 

:   Any "named" NPC

### {{ renderMember(type='bool', name='bNearAlert') }} 

:   Indicates usage of **nearalert** filter

### {{ renderMember(type='bool', name='bNoAlert') }} 

:   Indicates usage of **noalert** filter

### {{ renderMember(type='bool', name='bNoGroup') }} 

:   Exclude any player that is in the group

### {{ renderMember(type='bool', name='bNoGuild') }} 

:   Exclude any player that is in the guild

### {{ renderMember(type='bool', name='bNoPet') }} 

:   Exclude any spawn that is a pet

### {{ renderMember(type='bool', name='bNotNearAlert') }} 

:   Indicates usage of **notnearalert** filter

### {{ renderMember(type='string', name='BodyType') }} 

:   Any spawn with given body type

### {{ renderMember(type='bool', name='bRaid') }} 

:   Any member of the raid

### {{ renderMember(type='bool', name='bSlower') }} 

:   Any player that is a slower

### {{ renderMember(type='bool', name='bSpawnID') }} 

:   Indicates usage of the **id** filter

### {{ renderMember(type='bool', name='bTank') }} 

:   Any player that is a tank class

### {{ renderMember(type='bool', name='bTargetable') }} 

:   Any spawn that is targetable

### {{ renderMember(type='bool', name='bTargNext') }} 

:   Indicates usage of the **next** filter

### {{ renderMember(type='bool', name='bTargPrev') }} 

:   Indicates usage of the **prev** filter

### {{ renderMember(type='bool', name='bTrader') }} 

:   Any player that is a trader

### {{ renderMember(type='bool', name='bTributeMaster') }} 

:   Any NPC that is a tribute master

### {{ renderMember(type='string', name='Class') }} 

:   Any spawn that is the given class

### {{ renderMember(type='double', name='FRadius') }} 

:   Any spawn that is given distance from the given **loc** filter

### {{ renderMember(type='int', name='FromSpawnID') }} 

:   Search starts at given spawn id

### {{ renderMember(type='int64', name='GuildID') }} 

:   Any member of the guild with the given id

### {{ renderMember(type='string', name='Light') }} 

:   Any spawn that is equipped with the given light source

### {{ renderMember(type='int', name='MaxLevel') }} 

:   Any spawn that is at this level or lower

### {{ renderMember(type='int', name='MinLevel') }} 

:   Any spawn that is at this level or greater

### {{ renderMember(type='string', name='Name') }} 

:   Any spawn with the given name

### {{ renderMember(type='int', name='NearAlertList') }} 

:   Any spawn near the given alert list

### {{ renderMember(type='int', name='NoAlertList') }} 

:   Excludes any spawn in the given alert list

### {{ renderMember(type='int', name='NotID') }} 

:   Excludes any spawn with the given id

### {{ renderMember(type='int', name='NotNearAlertList') }} 

:   Excludes any spawn near the given alert list

### {{ renderMember(type='int', name='PlayerState') }} 

:   Any spawn with the given state

### {{ renderMember(type='string', name='Race') }} 

:   Any spawn with the given race

### {{ renderMember(type='float', name='Radius') }} 

:   Excludes the spawn if any player is within this distance (**nopcnear** filter)

### {{ renderMember(type='int', name='SortBy') }} 

:   Indicates the sort order of the filter

### {{ renderMember(type='spawn', name='Spawn') }} 

:   If an ID or Name is part of the filter, attempts to return a spawn with the matching ID or Name

### {{ renderMember(type='int', name='SpawnID') }} 

:   Any spawn with the given Spawn ID

### {{ renderMember(type='int', name='SpawnType') }} 

:   Any spawn with the given type

### {{ renderMember(type='float', name='xLoc') }} 

:   `x` component of the **loc** filter

### {{ renderMember(type='float', name='yLoc') }} 

:   `y` component of the **loc** filter

### {{ renderMember(type='double', name='ZRadius') }} 

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
