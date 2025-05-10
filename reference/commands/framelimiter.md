---
tags:
    - command
---
# /framelimiter

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/framelimiter [COMMAND] {OPTIONS}
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Frame limiter tool: allows adjusting internal frame limiter settings.
<!--cmd-desc-end-->
## Options
<!--cmd-options-start-->
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
<!--cmd-options-end-->
