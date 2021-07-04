# Charinfo

## Syntax

**/charinfo**

## Description

Returns your current bind zone and location.  
**Note:** This is a normal EverQuest command that is detoured by MacroQuest2 to display additional information.

## Examples

* The EverQuest /charinfo will return your bind zone and \[secondary bind or Origin location\] in the main chat

  window.

```text
You are currently bound in: The Bazaar, The Field of Bone
```

## Inconsistency

SOE uses the _Y, X, Z_ convention for their location data instead of _X, Y, Z_ used by MQ2.  
If you would like the bind data to display _correctly \(in SOE terms\)_ you may perform the modification to MQ2Commands.cpp found here: [/charinfo thread](https://macroquest2.com/phpBB3/viewtopic.php?t=15945)

