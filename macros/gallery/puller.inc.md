---
tags:
   - macro
---
# Puller.inc

## Link

[Click Here to go to the MQ2 forum thread](https://macroquest2.com/phpBB3/viewtopic.php?t=11693&highlight=)

## Features

* Per toon customization logged in PULLER.INI which will be created by the include. Uses AdvPath for pre-pathed and nearest matching mob pulling.
* Pathed pulling you record a path to pull along then play that path back.
* Unpathed pulling will just target the nearest matching mob and go to it. If obsticles are hit it will use MoveStuck.inc to try and get around them. The entire time it's recording your path so when you do have a mob it will play the file back to get back to camp.
* Camp can be a location (where you enter the routine if not previously defined)
* Camp can be another Spawn (player or NPC) - Untested
* Camp can be changed via commands
* Bandoliear can be used with mele and ranged pulling
* Pull methods currently supported are spell (using spell\_routines)
* Ranged
* Melee
* Pet - Untested
* Target aquired and tracked without targeting until the mob is tagged.
* If you get a target (you got hit) before you reach the perferred target you return with your add
* Targeting is based on alerts so new target types can be easily managed
* ie. /alert add 1 orc
* just look up /alert in TFM

-Alert 2 is used to hold target's you DO NOT want to target. Let's say you want to kill any orc so /alert add 1 orc but you don't want to kill the wood elf named orcflayer so do /alert add 2 orcflayer to exclude him from potential targets

## REQUIRED Include's

`#include spell_routines.inc`
`#include advpath.inc`
`#include system_events.inc`
`#include outlander.inc`

## Initialization Calls

`/call InitAPFVars 1 15 20`
`/call SysEventInit`
`/call PullerInit`
`/call MoveStuckInit`

## To Do:

* **Split Routine(s)**
* **Mob Avoidance (for both pulling and returning from pull)**

Stubbed in and partially coded.

* **Auto Add to oE\_BadTargetList if we just can't get to a mob in X amount of time and we are within Y distance.**

