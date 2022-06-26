---
tags:
    - command
---
# /vardata

## Syntax

**/vardata varname** _**newMQ2Datavalue**_

## Description

Sets a variable directly to the end result of a MQ2Data string.  
\*To use this, **do not** put ${} around the outer data to parse.

* This is more efficient than using _/varset_ as it skips a step
  * _/varset_ first converts the MQ2Data to text, and then back to MQ2Data
  * _/vardata_ converts directly through MQ2Data

## Examples

```text
/vardata MyFloat Math.Calc[${Me.X}+${Me.Y}]

/vardata M_Assist Param0

| using /vardata with non-basic data types

/declare x int local
/declare xSpawn spawn local
/for x 1 to ${SpawnCount[pc]}
   /vardata xSpawn NearestSpawn[${x},pc]
   /echo ID:${xSpawn.ID} NAME:${xSpawn.Name}
/next x
```
