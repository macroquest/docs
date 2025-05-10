---
tags:
    - command
---
# /ctrlkey

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/ctrlkey <command>
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Execute _command_ while telling the window manager that the ctrl key is pressed. Can also be used together with [/altkey](altkey.md) , [/shiftkey](shiftkey.md) , or both in this format:

/ctrlkey /altkey /shiftkey _/command_
<!--cmd-desc-end-->
## Examples

`/ctrlkey /itemnotify pack1 leftmouseup`

