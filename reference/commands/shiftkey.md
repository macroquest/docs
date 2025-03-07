---
tags:
    - command
---
# /shiftkey

## Syntax

```eqcommand
/shiftkey <command>
```

## Description

Execute _command_ while telling the window manager that the shift key is pressed. Can also be used together with [/altkey](altkey.md) , [/ctrlkey](ctrlkey.md) , or both in this format:

```text
/ctrlkey /altkey /shiftkey /command
```

## Examples

```text
/shiftkey /itemnotify pack1 leftmouseup
```

