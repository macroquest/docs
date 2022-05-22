---
tags:
    - tlo
    - datatype
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
