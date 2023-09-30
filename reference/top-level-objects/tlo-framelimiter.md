---
tags:
    - tlo
---
# `FrameLimiter`

The FrameLimiter TLO provides access to the frame limiter feature

## Forms

[framelimiter](#framelimiter-type) **FrameLimiter**

:   The frame limiter object

## Associated DataTypes

### {{ renderMember(name='framelimiter') }} 

Represents the state of the frame limiter

[float][float] **BackgroundFPS**:

:   Value of the target background fps setting.

[bool][bool] **ClearScreen**

:   Value of the clear screen when not rendering setting.

[float][float] **CPU**:

:   Current CPU usage as %

[bool][bool] **Enabled**

:   TRUE if the frame limiter feature is currently active.

[float][float] **ForegroundFPS**:

:   Value of the target foreground fps setting.

[float][float] **MinSimulationFPS**:

:   Value of the minimum simualtion rate setting.

[float][float] **RenderFPS**:

:   Current graphics scene frame rate (visible fps).

[bool][bool] **SaveByChar**

:   TRUE if settings for the frame limiter are being saved by character.

[float][float] **SimulationFPS**:

:   Current simulation frame rate (game updates per second).

[string][string] **Status**

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

