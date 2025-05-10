---
tags:
    - command
---
# /timestamp

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/timestamp [on|off]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Toggles timestamps on all chat messages. It can be set in MacroQuest.ini via `TimeStampChat=1` (1=ON, 0=OFF) in the [MacroQuest] section.

`NOTE:` The timestamp is added *before* the message reaches game UI but *after* MQ's chat event processing. This should not have any adverse effects when turned on.
<!--cmd-desc-end-->
