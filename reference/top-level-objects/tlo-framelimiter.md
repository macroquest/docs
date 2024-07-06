---
tags:
    - tlo
---
# `FrameLimiter`

The FrameLimiter TLO provides access to the [frame limiter](../../main/features/framelimiter.md) feature.

## Forms

### {{ renderMember(type='framelimiter', name='FrameLimiter') }}

:   The frame limiter object


## datatype `framelimiter`

Represents the state of the frame limiter

### {{ renderMember(type='float', name='BackgroundFPS') }}

:   Value of the target background fps setting.

### {{ renderMember(type='bool', name='ClearScreen') }}

:   Value of the clear screen when not rendering setting.

### {{ renderMember(type='float', name='CPU') }}

:   Current CPU usage as %

### {{ renderMember(type='bool', name='Enabled') }}

:   TRUE if the frame limiter feature is currently active.

### {{ renderMember(type='float', name='ForegroundFPS') }}

:   Value of the target foreground fps setting.

### {{ renderMember(type='float', name='MinSimulationFPS') }}

:   Value of the minimum simualtion rate setting.

### {{ renderMember(type='float', name='RenderFPS') }}

:   Current graphics scene frame rate (visible fps).

### {{ renderMember(type='bool', name='SaveByChar') }}

:   TRUE if settings for the frame limiter are being saved by character.

### {{ renderMember(type='float', name='SimulationFPS') }}

:   Current simulation frame rate (game updates per second).

### {{ renderMember(type='string', name='Status') }}

:   Either "Foreground" or "Background".


## Usage

Indicates that the frame limiter is enabled:

```
/echo ${FrameLimiter.Enabled}
```

[bool]: ../data-types/datatype-bool.md
[string]: ../data-types/datatype-string.md
[float]: ../data-types/datatype-float.md
[framelimiter]: #datatype-framelimiter