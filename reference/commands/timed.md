---
tags:
    - ref
    - slash
---
# /timed

## Syntax

**/timed \#** _**command**_

## Description

Executes _command_ after a specified duration, given in deciseconds.

**Notes**

* This does not pause successive commands.
* The first argument must be a literal integer (e.g. 2)
  * It is not parsed for MQ2Data, so the following **will not work**

```text
    /timed ${Math.Calc[1+1]} /echo This does not work

-   An exception to this being the use of /docommand in combination with /timed


    /docommand /timed ${Math.Calc[1+1]} /echo This works
```

## Examples

```text
/timed 10 /echo 1 second has passed
```

