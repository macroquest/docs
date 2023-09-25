---
tags:
    - datatype
---
# `altability`

Contains all the data related to alternate abilities

## Members

### [int][int] `AARankRequired`

:   Rank required to train

### [bool][bool] `CanTrain`

:   Returns true/false on if the Alternative Ability can be trained

### [string][string] `Category`

:   The name of the category that this AA belongs to.

### [int][int] `Cost`

:   Base cost to train

### [string][string] `Description`

:   Basic description

### [int][int] `Expansion`

:   Expansion level for the ability.

### [int][int] `Flags`

:   Flags value (Currently unknown?).

### [int][int] `GroupID`

:   ID of the AA group that this AA belongs to

### [int][int] `ID`

:   ID

### [int][int] `Index`

:   Returns the index number of the Alternative Ability

### [int][int] `MaxRank`

:   Max rank available in this ability

### [int][int] `MinLevel`

:   Minimum level to train

### [int][int] `MyReuseTime`

:   Reuse time (in seconds) that takes into account any hastened AA abilities

### [string][string] `Name`

:   Name

### [int][int] `NextIndex`

:   Returns the next index number of the Alternative Ability

### [int][int] `PointsSpent`

:   Returns the amount of points spent on an AA

### [bool][bool] `Passive`

:   Returns true/false on if the Alternative Ability is passive

### [int][int] `Rank`

:   Returns the Rank of the AA

### [altability][altability] `RequiresAbility`

:   Required ability (if any)

### [int][int] `RequiresAbilityPoints`

:   Points required in above ability

### [int][int] `ReuseTime`

:   Reuse time in seconds

### [string][string] `ShortName`

:   First line of button label (if any)

### [string][string] `ShortName2`

:   Second line of button label (if any)

### [spell][spell] `Spell`

:   Spell used by the ability (if any)

### [int][int] `Type`

:   Type (1-6)

### [string][string] `To String`

:   Same as **Name**


### Example:

If the AA "Companion's Aegis" can be trained, buy the next index/rank of it

=== "MQScsript"

    ```
    /if (${AltAbility[Companion's Aegis].CanTrain}) {
        /alt buy ${AltAbility[Companion's Aegis].NextIndex}
    }
    ```

=== "Lua"

    ```lua
    if mq.TLO.AltAbility("Companion's Aegis").CanTrain() then
        mq.cmd.alt('buy '..mq.TLO.AltAbility("Companion's Aegis").NextIndex())
    end
    ```
[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
