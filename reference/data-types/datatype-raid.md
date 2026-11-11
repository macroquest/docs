---
tags:
    - datatype
---
# `raid`

<!--dt-desc-start-->
Contains data on the current raid
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | float AverageLevel
Average level of raid members (more accurate than in the window)
///

/// member | bool Invited
Have I been invited to the raid?
///

/// member | raidmember Leader
Raid leader
///

/// member | bool Locked
Returns TRUE if the raid is locked
///

/// member | string Looter[#]
Specified looter name by number
///

/// member | int Looters
Number of specified looters
///

/// member | int LootType
Method of looter assignment

| Value | Meaning |
| :--- | :--- |
| 1 | Leader |
| 2 | Leader & Group Leader |
| 3 | Leader & Assignments |
///

/// member | raidmember MainAssist
Raid main assist
///

/// member | raidmember MarkNpc
Raid NPC marker
///

/// member | raidmember MasterLooter
Raid Master Looter
///

/// member | raidmember Member[N]
Raid member by number _N_
///

/// member | raidmember Member[name]
Raid member by _name_.
///

/// member | int Members
Total number of raid members
///

/// member | raidmember Target
Raid target (clicked in raid window)
///

/// member | int TotalLevels
Sum of all raid member's levels
///
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[float]: datatype-float.md
[int]: datatype-int.md
[raidmember]: datatype-raidmember.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
