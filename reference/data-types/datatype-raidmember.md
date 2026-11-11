---
tags:
    - datatype
---
# `raidmember`

<!--dt-desc-start-->
Data related to the specified raid member
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | class Class
Raid member's class (works without being in zone)
///

/// member | int Group
Current group number (or 0)
///

/// member | bool GroupLeader
Returns TRUE if the member is a group leader
///

/// member | int Level
Raid member's level (works without being in zone)
///

/// member | bool Looter
Allowed to loot with current loot rules and looters?
///

/// member | string Name
Raid member's name
///

/// member | bool RaidLeader
Returns TRUE if the member is the raid leader
///

/// member | spawn Spawn
Spawn object for this player if available (must be in zone)
///

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[class]: datatype-class.md
[int]: datatype-int.md
[spawn]: datatype-spawn.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
