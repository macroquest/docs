---
tags:
    - datatype
---
# `timer`

<!--dt-desc-start-->
A timer data type is set in tenths of one second and counts down to zero; starting immediately after being set.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='int', name='OriginalValue') }}

:   Original value of the timer

### {{ renderMember(type='int', name='Value') }}

:   Current value of the timer

### [string][string] `To String`

:   Same as **Value**
<!--dt-members-end-->

## Methods

| Name | Action |
| :--- | :--- |
| **Expire** | Set the timer to 0
| **Reset** | Reset the timer to the original value
| **Set**[_value_] | Set the timer to the given value

## Usage

Consider the following timer:

```
/declare BuffTimer timer local
/varset BuffTimer 360
```

BuffTimer will be equal to 0 in:

* 360 tenths of 1 second
* 36 seconds
* 6 ticks (a tick is 6 seconds)

Timers may also be set with an "s" (seconds) or an "m" (minutes) appended to the value. For example:

```
/varset BuffTimer 360s
```

This would set the timer to 3600 (360 * 10) tenths of 1 second

```
/varset BuffTimer 360m
```

This would set the timer to 216000 (360 * 60 * 10) tenths of 1 second

```text
sub main
    /declare myTimer timer local 100
    /while ( ${myTimer} ) {
        /echo ${myTimer}
        /delay 10
    }
/return
```

This would loop while myTimer is above 0
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
[zone]: datatype-zone.md
[fellowshipmember]: datatype-fellowshipmember.md
[class]: datatype-class.md
[heading]: datatype-heading.md
[ground]: datatype-ground.md
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[double]: datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
[raidmember]: datatype-raidmember.md
[body]: datatype-body.md
[cachedbuff]: datatype-cachedbuff.md
[deity]: datatype-deity.md
[race]: datatype-race.md
[taskmember]: datatype-task.md
<!--dt-linkrefs-end-->
