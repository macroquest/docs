---
tags:
    - command
---
# /multiline

## Syntax

```eqcommand
/multiline <delimiter> <command> [ <delimiter> <command> [...] ]
```

## Description

Executes multiple commands using a single line separated by the delimiter.

**Notes**

* This is useful for keybinds
* There **must** be a space before and after the defined delimiter. e.g. **/multiline ; command**
* You do not need to put a space before and after the delimiter separating the individual commands
*   The delimiter is 1 parameter, and the list of commands is 1 parameter, ergo you need a space separating the

    delimiter from the list of commands. The delimiter may be anything of your choosing e.g ; | word @ # !&#x20;
* /call, /return and /delay are line based and their use on a /multiline line is unpredictable.

## Examples

```
; using one multline
/if ( ${Target.ID} && ${Target.Type.Equal[NPC]} && !${Me.Combat} ) {
       /multiline ; /echo Attacking ${Target.DisplayName}; /attack on
}

; use more than one multiline
/multiline ; /target clear; /mqp on; /timed 200 /multiline | mqp off | /beep
```
