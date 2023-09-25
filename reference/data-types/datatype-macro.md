---
tags:
    - datatype
---
# `macro`

The Macro DataType deals with the macro currently running, and nothing else.

## Members

### [string][string] `CurCommand`

:   list the current line number, macro name, and code of the macro being processed

### [int][int] `CurLine`

:   The current line number of the macro being processed

### [string][string] `CurSub`

:   The current subroutine

### [bool][bool] `isOuterVariable`

:   true if the provided parameter is a defined outer variable

### [bool][bool] `isTLO`

:   true if the provided parameter an existing TLO

### [int][int] `MemUse`

:   How much memory the macro is using

### [string][string] `Name`

:   The name of the macro currently running

### [int][int] `Params`

:   The number of parameters that were passed to the current subroutine

### [bool][bool] `Paused`

:   NULL if no macro running, FALSE if mqpause is off, TRUE if mqpause is on

### [string][string] `Return`

:   The value that was returned by the last completed subroutine

### [int64][int64] `RunTime`

:   How long the macro has been running (in seconds)

### [int][int] `StackSize`

:   StackSize?

### [varies][varies] `Variable`

:   returns the value given the name of Macro variable


## Methods

| Method Name | Action |
| :--- | :--- |
| Undeclared | List all undeclared variables |

[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: ../data-types/datatype-spell.md
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
