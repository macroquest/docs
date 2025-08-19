---
tags:
    - command
---
# /keypress

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/keypress <name> [hold|chat]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Simulates key presses for keybinds (e.g. "jump", "forward"), virtual keyboard (e.g. "shift+b"), or direct chat window input. Does not physically press keys, making it safe for background operation.

Note: /keypress usage outside of a script is not recommended nor consistent.
<!--cmd-desc-end-->
## Parameters
| Parameter | Description |
|-----------|-------------|
| **hold**  | Maintains key in pressed state until released |
| **chat**  | Directs input to chat/UI fields instead of game world |

Note: Cannot use both together. For chat input, use simple key names ("X" not "shift+x"). "hold" works with movement/toggle commands.

### EQUI and MQ Keybinds
```text
/keypress jump         # Simulate the key mapped to JUMP
/keypress HAIL         # Simulate the key mapped to the HAIL emote
/keypress NETSTAT      # Simulate the key mapped to the NETSTAT command
```

### Keys and Key Combinations
```text
/keypress h              # Virtual h key press (will trigger HAIL by default)
/keypress shift+b        # Virtual shift+B key press
/keypress ctrl+i         # Virtual control+I key press
```

### Advanced Usage
```text
/keypress forward hold # Begin moving forward
/keypress forward      # Stop moving forward
/keypress r chat       # Type 'r' in chat input
/keypress R chat       # Type 'R' in chat input
```
## Key Reference

### Common EQUI Keybinds
| Command | Description |
|---------|-------------|
| OPEN_INV_BAGS | Toggle inventory bags |
| TOGGLE_MAPWIN | Show/hide map |
| CAST1-CAST12 | Spell gem hotkeys |
| HOT1_1-HOT1_12 | Hotbar buttons |

*Use the [/bind](bind.md) command to view your client's EQ binds `/bind eqlist` or all binds `/bind list`.*

### Virtual Keys

```text
Esc  F1-F12  ` 1 2 3 4 5 6 7 8 9 0 - = [ ] \
Tab  Q W E R T Y U I O P 
Caps_Lock A S D F G H J K L ; ' 
Shift Z X C V B N M , . / Right_Shift
Ctrl Alt Space Enter Backspace
```
For complete key names and codes, including mouse and media keys, see: [src/eqdata/dikeys.h](https://github.com/macroquest/macroquest/blob/master/src/eqdata/dikeys.h)


*See also: [/bind](bind.md), [/doability](doability.md)*
