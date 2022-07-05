---
tags:
    - command
---
# /while

## Syntax

**/while (condition) {**

`...`

**}**

## Description

Executes the commands between { and } while the expression condition evaluates to true. Note that } must be on a line by its own. You can end a /while loop immediately with /break or try the next iteration with /continue.

## Examples

```text
/declare varname int 0
/while (${varname) < 5) {
  /varcalc varname ${varname}+1
  /echo ${varname}
}
```

Will output:

```text
 1
 2
 3
 4
 5

/declare varname int 0
/while (${varname) < 5) {
  /varcalc varname ${varname}+1
  /if ({$varname} == 3) /continue
  /echo ${varname}
}
```

Will output:

```text
 1
 2
 4
 5

/declare varname int 0
/while (${varname) < 5) {
  /varcalc varname ${varname}+1
  /if ({$varname} == 3) /break
  /echo ${varname}
}
```

Will output:

```text
 1
 2
```
