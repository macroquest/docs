---
tags:
    - command
---
# /invoke

## Syntax

```eqcommand
/invoke ${TLO.[XXX].Action}
```

## Description

This will invoke the action portion of some of the new TLO additions. This has the potential to shorten macros and make them more powerful.

The current methods that are available for use and testing are:

For the Task TLO:

`.Select`

For the Spawn[]. TLO:

`.DoTarget`  
`.DoFace`  
`.DoAssist`  
`.LeftClick`  
`.RightClick`

For the Me. TLO:

`.Stand`  
`.Sit`  
`.Dismount`  
`.StopCast`

For the Me.Buff TLO Member:

`.Remove`

For the Switch TLO:

`.Toggle`

For the Ground TLO:

`.Grab`

For the Window TLO:

`.LeftMouseDown`  
`.LeftMouseUp`  
`.LeftMouseHeld`  
`.LeftMouseHeldUp`  
`.RightMouseDown`  
`.RightMouseUp`  
`.RightMouseHeld`  
`.RightMouseHeldUp`  
`.Select`

## Examples

`/invoke ${Spawn[eqmule].DoTarget}`

if spawn "eqmule" is found, will target

`/invoke ${Me.Buff[Cred].Remove}`

If a buff with the partial name "Cred" is found it will remove it
