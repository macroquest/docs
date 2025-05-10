---
tags:
    - command
---
# /goto

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/goto :<labelname>
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
This moves the macro execution to the location of _:labelname_ in the macro.
<!--cmd-desc-end-->
## Example

```text
:MyLabel
/if ( ${Me.Moving} ) /goto :MyLabel
/echo I am no longer moving!
```

