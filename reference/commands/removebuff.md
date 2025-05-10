---
tags:
    - command
---
# /removebuff

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/removebuff [-pet|-both] <Name Of Buff>
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Will remove a buff or song by the name of the buff.  It can be used to remove buffs from the player, the pet, or both.  By default it does a partial match, but you can force an exact compare with the equals sign.
<!--cmd-desc-end-->
## Example

```text
 /removebuff Resolution
 /removebuff -pet Resolution
 /removebuff -both Resolution
 
 /removebuff Illusion: Dark Elf
 /removebuff =Some Overlapping Buffname
```

