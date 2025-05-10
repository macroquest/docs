---
tags:
    - command
---
# /varcalc

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/varcalc varname <formula>
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
* Sets a variable directly to the numeric result of a calculation (_formula_)
* Keep in mind that the type of the variable may itself reject this value depending on what you give it
* **This will not work on strings!**
<!--cmd-desc-end-->
## Examples

```text
/varcalc MyInt 1+2*2+1
/varcalc MyInt 1+(2*2)+1

/varcalc MyInt ${MyInt}+6
```
