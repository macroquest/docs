---
tags:
    - datatype
---
# `altability`

<!--dt-desc-start-->
Contains all the data related to alternate abilities
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int AARankRequired
Rank required to train
///

/// member | bool CanTrain
Returns true/false on if the Alternative Ability can be trained
///

/// member | string Category
The name of the category that this AA belongs to.
///

/// member | int Cost
Base cost to train
///

/// member | string Description
Basic description
///

/// member | int Expansion
Expansion level for the ability.
///

/// member | int Flags
Flags value (Currently unknown?).
///

/// member | int GroupID
ID of the AA group that this AA belongs to
///

/// member | int ID
ID
///

/// member | int Index
Returns the index number of the Alternative Ability
///

/// member | int MaxRank
Max rank available in this ability
///

/// member | int MinLevel
Minimum level to train
///

/// member | int MyReuseTime
Reuse time (in seconds) that takes into account any hastened AA abilities
///

/// member | string Name
Name
///

/// member | int NextIndex
Returns the next index number of the Alternative Ability
///

/// member | bool Passive
Returns true/false on if the Alternative Ability is passive
///

/// member | int PointsSpent
Returns the amount of points spent on an AA
///

/// member | int Rank
Returns the Rank of the AA
///

/// member | altability RequiresAbility
Required ability (if any)
///

/// member | int RequiresAbilityPoints
Points required in above ability
///

/// member | int ReuseTime
Reuse time in seconds
///

/// member | string ShortName
First line of button label (if any)
///

/// member | string ShortName2
Second line of button label (if any)
///

/// member | spell Spell
Spell used by the ability (if any)
///

/// member | int Type
Type (1-6)
///

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->

## Examples

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
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
[bool]: datatype-bool.md
[spell]: datatype-spell.md
[altability]: datatype-altability.md
<!--dt-linkrefs-end-->
