---
tags:
    - tlo
---
# `FrameLimiter`

The FrameLimiter TLO provides access to the frame limiter feature

## Forms

[_framelimiter_](#framelimiter-type) **FrameLimiter**

:   The frame limiter object

## Associated DataTypes

### `framelimiter` Type

Represents the state of the frame limiter

[_float_][float] **BackgroundFPS**:

:   Value of the target background fps setting.

[_bool_][bool] **ClearScreen**

:   Value of the clear screen when not rendering setting.

[_float_][float] **CPU**:

:   Current CPU usage as %

[_bool_][bool] **Enabled**

:   TRUE if the frame limiter feature is currently active.

[_float_][float] **ForegroundFPS**:

:   Value of the target foreground fps setting.

[_float_][float] **MinSimulationFPS**:

:   Value of the minimum simualtion rate setting.

[_float_][float] **RenderFPS**:

:   Current graphics scene frame rate (visible fps).

[_bool_][bool] **SaveByChar**

:   TRUE if settings for the frame limiter are being saved by character.

[_float_][float] **SimulationFPS**:

:   Current simulation frame rate (game updates per second).

[_string_][string] **Status**

:   Either "Foreground" or "Background".


## Usage

Indicates that the frame limiter is enabled:

```
/echo ${FrameLimiter.Enabled}
```

[bool]: ../data-types/datatype-bool.md
[string]: ../data-types/datatype-string.md
[float]: ../data-types/datatype-float.md
[Frame Limiter]: ../../main/features/framelimiter.md
[int]: ../data-types/datatype-int.md
[string]: ../data-types/datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: ../data-types/datatype-bool.md
[time]: datatype-time.md
[achievement]: ../data-types/datatype-achievement.md
[achievementcat]: ../data-types/datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: ../data-types/datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: ../data-types/datatype-float.md
[buff]: datatype-buff.md
[spawn]: ../data-types/datatype-spawn.md
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
[double]: ../data-types/datatype-double.md
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
[achievementmgr]: #achievementmgr-type
[itemfilterdata]: #itemfilterdata-type
[advlootitem]: #advlootitem-type
[alert]: #alert-type
[alertlist]: #alertlist-type
