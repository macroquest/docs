---
tags:
    - command
---
# /click

## Syntax

```eqcommand
/click [ left | right ] [ target | item | door | switch | center | <x> <y> ]
```

## Description

Executes a left or right mouse button click on targets or specific screen location.  

### Click targets

- **target**: Clicks your current target (PC, NPC)
- **item**: Clicks the currently "[/itemtarget](itemtarget.md)"-ed ground item or container  
- **door** or **switch**: Clicks the currently "[/doortarget](doortarget.md)"-ed door or switch  
- **center**: Clicks the center of the viewport  
- _x_ _y_: Clicks anywhere on the screen by specifying coordinates (absolute or relative, e.g. "100 200" or "+10 -20").

If no target argument is specified then the mouse button is clicked at the current mouse position.

Certain commands (e.g., "[/shiftkey](shiftkey.md) /click right target") can be chained to combine keystroke modifiers with clicking actions.

## Examples

| Example                       | Description                                                                |
| ---------------------------- | -------------------------------------------------------------------------- |
| /click left                  | Left-clicks at the current mouse position                                  |
| /click right target          | Right-clicks your currently selected target                                |
| /click left item             | Left-clicks a ground item. Requires setting a ground item first via /itemtarget |
| /click left door             | Left-clicks a door or switch. Requires setting a door via /doortarget       |
| /click right center          | Right-clicks the center of the viewport                                    |
| /click left +10 +10          | Moves the mouse 10 px right/down from the current position and left-clicks |
| /click right 100 200         | Moves the mouse to coordinates (100,200) and right-clicks                  |