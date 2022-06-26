---
tags:
    - command
---
# /mouseto

## Syntax

```text
/mouseto <X or X offset> [Y or Y offset]
```

## Description

Moves the mouse to the specified location.

When an absolute location is specified (a number from 0 through 9) the mouse is moved to the absolute position.

When a relative position is specified (using - or + in front of the X or Y) the mouse is moved by that offset.

## Examples

Move the mouse to X=1 Y=1

```text
/mouseto 1 1
```

Move the mouse by 1 positive unit vertically and horizontally

```text
/mouseto +1 +1
```
