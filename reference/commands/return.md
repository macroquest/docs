---
tags:
    - command
---
# /return

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/return [value|${varname}]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Returns to the line immediately following the call. Can return values or variables.
<!--cmd-desc-end-->
## Examples

```text
Sub Add(int A, int B)
  /declare Sum int local ${Math.Calc[${A}+${B}]}
/return ${Sum}
```

Return can also be used to exit out of a [subroutine](../../macros/subroutines.md) early.

```text
Sub Evade
  /if (!${Me.AbilityReady[Hide]}) {
     /echo Hide has not refreshed, so we are leaving early.
     /return
  }
  /echo Hide is ready, so we will continue processing
  /attack off
  /doability Hide
  /delay 5
  /attack on
/return
```

