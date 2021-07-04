## Syntax

**<span style="color:red">/return</span>
\[<span style="color:blue">value</span>\|<span style="color:blue">${varname}</span>\]**

## Description

Returns to the line immediately following the call. Can return values or variables.

## Examples

    Sub Add(int A, int B)
      /declare Sum int local ${Math.Calc[${A}+${B}]}
    /return ${Sum}

Return can also be used to exit out of a [subroutine](subroutines.md) early.

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


