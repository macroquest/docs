---
tags:
    - command
---
# /usercamera

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/usercamera [ <0-7> |on|off|save [ <charname> ]|load [ <charname> ]]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Switch to a specified camera view or manage the User Camera 1 position settings.
<!--cmd-desc-end-->
## Options

### Camera Numbers (0-7)
Switches to the specified camera view:

- **0:** First Person Camera
- **1:** Overhead Camera
- **2:** Chase Camera
- **3:** User Camera 1
- **4:** User Camera 2
- **5:** Tether Camera
- **6:** Zoom Camera
- **7:** Internal Camera (used for character customization and similar features)

### Display Controls
- `on` - Enable Window Selector Display for current camera
- `off` - Disable Window Selector Display for current camera

### Position Management
- `save [charname]` - Save the current User Camera 1 position, optionally for a specific character
- `load [charname]` - Load a saved User Camera 1 position, optionally for a specific character