# Frame Limiter

Frame limiter is a built-in feature of MacroQuest that helps control the resource usage of EverQuest by
limiting how often the game renders frames.

## Configuration

Frame lmiter settings can be modified in the MacroQuest Settings window.

![MQSettings Frame Limiter](../../images/framelimiter.png)

## Commands

`/framelimiter [COMMAND] {OPTIONS}`

Frame limiter tool: allows adjusting internal frame limiter settings.

```text
enable -- turn the framelimiter on (background)
on -- turn the framelimiter on (background)
disable -- turn the rendering client off
off -- turn the rendering client off
toggle -- set/toggle the framelimiter functionality
enablefg -- turn the framelimiter on (foreground)
onfg -- turn the framelimiter on (foreground)
disablefg -- turn the framelimiter off (foreground)
offfg -- turn the framelimiter off (foreground)
togglefg -- set/toggle the framelimiter (foreground)
savebychar -- set/toggle saving settings by character
bgrender -- set/toggle rendering when client is in background
imguirender -- set/toggle rendering ImGui when rendering is otherwise disabled
uirender -- set/toggle rendering the UI when rendering is otherwise disabled
clearscreen -- set/toggle clearing (blanking) the screen when rendering is disabled
bgfps -- set the FPS rate for the background process
fgfps -- set the FPS rate for the foreground process
simfps -- sets the minimum FPS the simulation will run
reloadsettings -- reload settings from ini
-h, -?, help -- displays this help text
```

## Top-Level Objects

### [FrameLimiter](reference\top-level-objects\tlo-framelimiter.md)

## Members

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

[bool]: datatype-bool.md
[float]: datatype-float.md
[string]: datatype-string.md
