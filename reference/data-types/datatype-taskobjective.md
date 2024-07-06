---
tags:
    - datatype
---
# `taskobjective`

This is the type for your current task objective.

## Members

### {{ renderMember(type='int', name='CurrentCount') }}

:   Returns the current count of the .Type needed to complete a objective

### {{ renderMember(type='int', name='DZSwitchID') }}

:   Returns an int of the switch used in a objective.

### {{ renderMember(type='string', name='Index') }}

:   Returns the objective's place on the objectivelist

### {{ renderMember(type='string', name='Instruction') }}

:   Returns a tasks' Objectives

### {{ renderMember(type='bool', name='Optional') }}

:   Returns true or false if a objective is optional

### {{ renderMember(type='int', name='RequiredCount') }}

:   Returns the required count of the .Type needed to complete a objective

### {{ renderMember(type='string', name='RequiredItem') }}

:   Returns a string of the required item to complete a objective.

### {{ renderMember(type='string', name='RequiredSkill') }}

:   Returns a string of the required skill to complete a objective.

### {{ renderMember(type='string', name='RequiredSpell') }}

:   Returns a string of the required spell to complete a objective.

### {{ renderMember(type='string', name='Status') }}

:   Returns the status of the objective in the format amount done Vs total IE 0/3

### {{ renderMember(type='string', name='Type') }}

:   Returns a string that can be one of the following:<

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

### {{ renderMember(type='string', name='Zone') }}

:   Returns the zone the objective is to be performed in

[int]: datatype-int.md
[string]: datatype-string.md
[bool]: datatype-bool.md
