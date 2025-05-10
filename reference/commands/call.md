---
tags:
    - command
---
# /call

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/call <subroutine> [Param0... [Param#]]
```
<!--cmd-syntax-end-->
## Description
<!--cmd-desc-start-->
Calls _subroutine_ (defined later in the macro by "Sub _subroutine_").
<!--cmd-desc-end-->
(_See_ [_Subroutines_](../../macros/subroutines.md) _for detailed information_)

## Examples

| \*\*\*\* |  |
| :--- | :--- |
| **/call MySub** | Executes the MySub subroutine |
| **/call MySub var1 var2 var3** | Executes the MySub and passes it parameters var1, var, var3 |
| **/call MySub ${var1} ${var2}** | Executes the MySub subroutine and passes it variables var1, var2 as parameters |
