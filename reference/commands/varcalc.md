---
tags:
    - command
---
# /varcalc

## Syntax

```eqcommand
/varcalc varname <formula>
```

## Description

* Sets a variable directly to the numeric result of a calculation (_formula_)
* Keep in mind that the type of the variable may itself reject this value depending on what you give it
* **This will not work on strings!**

## Examples

```text
/varcalc MyInt 1+2*2+1
/varcalc MyInt 1+(2*2)+1

/varcalc MyInt ${MyInt}+6
```
