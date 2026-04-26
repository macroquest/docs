---
tags:
    - command
---
# /mqoverlay

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/mqoverlay [reload | resume | stop | start | cursor [on|off] | perchar [on|off] | copy {[server] <character> | default} | debug [mouse|graphics|fonts|cursor]]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Simple controls for the imgui overlay in MacroQuest. If imgui crashes, it can be resumed with this command.
<!--cmd-desc-end-->
## Parameters

- **reload** - Reload the overlay by shutting it down and starting it back up again.
- **resume** - Resumes the overlay in the event that an error has occurred.
- **stop** - Turns off the overlay. This state does not persist between MQ sessions.
- **start** - Turns on the overlay.
- **cursor [on|off]** - Turn cursor attachment emulation on/off (no param will toggle).
- **perchar [on|off]** - Turn per character overlay INI file on/off (no param will toggle).
- **copy** - Copy an overlay INI configuration to the currently logged in character.
    - `copy [server] character` - From the specified server+character (defaults to current server).
    - `copy default` - From the default overlay INI file.
- **debug** - overlay debug info
