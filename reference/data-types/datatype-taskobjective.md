---
tags:
    - datatype
---
# `taskobjective`

<!--dt-desc-start-->
This is the type for your current task objective.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | int CurrentCount
Returns the current count of the .Type needed to complete a objective
///

/// member | int DZSwitchID
Returns an int of the switch used in a objective.
///

/// member | string Index
Returns the objective's place on the objectivelist
///

/// member | string Instruction
Returns a tasks' Objectives
///

/// member | bool Optional
Returns true or false if a objective is optional
///

/// member | int RequiredCount
Returns the required count of the .Type needed to complete a objective
///

/// member | string RequiredItem
Returns a string of the required item to complete a objective.
///

/// member | string RequiredSkill
Returns a string of the required skill to complete a objective.
///

/// member | string RequiredSpell
Returns a string of the required spell to complete a objective.
///

/// member | string Status
Returns the status of the objective in the format amount done Vs total IE 0/3
///

/// member | string Type
Returns a string that can be one of the following:

- Unknown
- None
- Deliver
- Kill
- Loot
- Hail
- Explore
- Tradeskill
- Fishing
- Foraging
- Cast
- UseSkill
- DZSwitch
- DestroyObject
- Collect
- Dialogue
///

/// member | string Zone
Returns the zone the objective is to be performed in
///
<!--dt-members-end-->

<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
[bool]: datatype-bool.md
<!--dt-linkrefs-end-->
