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
### {{ renderMember(type='int', name='AARankRequired') }}

:   Rank required to train

### {{ renderMember(type='bool', name='CanTrain') }}

:   Returns true/false on if the Alternative Ability can be trained

### {{ renderMember(type='string', name='Category') }}

:   The name of the category that this AA belongs to.

### {{ renderMember(type='int', name='Cost') }}

:   Base cost to train

### {{ renderMember(type='string', name='Description') }}

:   Basic description

### {{ renderMember(type='int', name='Expansion') }}

:   Expansion level for the ability.

### {{ renderMember(type='int', name='Flags') }}

:   Flags value (Currently unknown?).

### {{ renderMember(type='int', name='GroupID') }}

:   ID of the AA group that this AA belongs to

### {{ renderMember(type='int', name='ID') }}

:   ID

### {{ renderMember(type='int', name='Index') }}

:   Returns the index number of the Alternative Ability

### {{ renderMember(type='int', name='MaxRank') }}

:   Max rank available in this ability

### {{ renderMember(type='int', name='MinLevel') }}

:   Minimum level to train

### {{ renderMember(type='int', name='MyReuseTime') }}

:   Reuse time (in seconds) that takes into account any hastened AA abilities

### {{ renderMember(type='string', name='Name') }}

:   Name

### {{ renderMember(type='int', name='NextIndex') }}

:   Returns the next index number of the Alternative Ability

### {{ renderMember(type='bool', name='Passive') }}

:   Returns true/false on if the Alternative Ability is passive

### {{ renderMember(type='int', name='PointsSpent') }}

:   Returns the amount of points spent on an AA

### {{ renderMember(type='int', name='Rank') }}

:   Returns the Rank of the AA

### {{ renderMember(type='altability', name='RequiresAbility') }}

:   Required ability (if any)

### {{ renderMember(type='int', name='RequiresAbilityPoints') }}

:   Points required in above ability

### {{ renderMember(type='int', name='ReuseTime') }}

:   Reuse time in seconds

### {{ renderMember(type='string', name='ShortName') }}

:   First line of button label (if any)

### {{ renderMember(type='string', name='ShortName2') }}

:   Second line of button label (if any)

### {{ renderMember(type='spell', name='Spell') }}

:   Spell used by the ability (if any)

### {{ renderMember(type='int', name='Type') }}

:   Type (1-6)

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
