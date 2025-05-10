---
tags:
    - command
---
# /continue

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/continue
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
When in a /for or /while loop try the next iteration.
<!--cmd-desc-end-->
## Example

```text
/for varname 1 to 5
  /if ({$varname} == 3) /continue
  /echo ${varname}
/next varname

/declare varname int 0
/while (${varname} < 5) {
  /varcalc varname ${varname}+1
  /if ({$varname} == 3) /continue
  /echo ${varname} 
}
```

Each loop will output:

```text
 1
 2
 4
 5
```
