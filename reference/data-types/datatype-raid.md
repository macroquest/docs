---
tags:
    - datatype
---
# `raid`

Contains data on the current raid

## Members

### {{ renderMember(type='float', name='AverageLevel') }}

:   Average level of raid members (more accurate than in the window)

### {{ renderMember(type='bool', name='Invited') }}

:   Have I been invited to the raid?

### {{ renderMember(type='raidmember', name='Leader') }}

:   Raid leader

### {{ renderMember(type='bool', name='Locked') }}

:   Returns TRUE if the raid is locked

### {{ renderMember(type='string', name='Looter', params='#') }}

:   Specified looter name by number

### {{ renderMember(type='int', name='Looters') }}

:   Number of specified looters

### {{ renderMember(type='int', name='LootType') }}

:   Method of looter assignment

    | Value | Meaning |
    | :--- | :--- |
    | 1 | Leader |
    | 2 | Leader & Group Leader |
    | 3 | Leader & Assignments |

### {{ renderMember(type='raidmember', name='MainAssist') }}

:   Raid main assist

### {{ renderMember(type='raidmember', name='MarkNpc') }}

:   Raid NPC marker

### {{ renderMember(type='raidmember', name='MasterLooter') }}

:   Raid Master Looter

### {{ renderMember(type='raidmember', name='Member', params='N') }}

:   Raid member by number _N_

### {{ renderMember(type='raidmember', name='Member', params='name') }}

:   Raid member by _name_.

### {{ renderMember(type='int', name='Members') }}

:   Total number of raid members

### {{ renderMember(type='raidmember', name='Target') }}

:   Raid target (clicked in raid window)

### {{ renderMember(type='int', name='TotalLevels') }}

:   Sum of all raid member's levels


[bool]: datatype-bool.md
[float]: datatype-float.md
[int]: datatype-int.md
[raidmember]: datatype-raidmember.md
[string]: datatype-string.md
