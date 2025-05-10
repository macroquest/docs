---
tags:
    - command
---
# /break

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/break
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
End a /for or /while loop immediately.
<!--cmd-desc-end-->

## Example

```text
 /for varname 1 to 5
   /if ({$varname} == 3) /break
   /echo ${varname}
 /next varname
```

Will output:

```text
 1
 2
```
