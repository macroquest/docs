---
tags:
    - command
---
# /shiftkey

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/shiftkey <command>
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Execute _command_ while telling the window manager that the shift key is pressed. Can also be used together with [/altkey](altkey.md) , [/ctrlkey](ctrlkey.md) , or both in this format:

```text
/ctrlkey /altkey /shiftkey /command
```
<!--cmd-desc-end-->
## Examples

```text
/shiftkey /itemnotify pack1 leftmouseup
```

