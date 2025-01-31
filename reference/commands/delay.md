---
tags:
    - command
---
# /delay

## Syntax

**/delay** _#_**[s|m]** **[** _condition_ **]**

## Description

Fully pauses the macro for the amount of time specified, or until _condition_ is met.

Time can be specified in 10ths of a second (a number by itself\) or in seconds \(number followed by an "s"\) or minutes \(number followed by "m").

## Examples

* Simple examples:

```text
/delay 7                                       Delays the macro for 7 tenths of a second
/delay 2s                                      Delays the macro for 2 seconds
/delay 3m                                      Delays the macro for 3 minutes
```

* Example using MQ2Data:

```text
/delay ${Math.Rand[10]}s                       Delays the macro for a random amount of seconds in the range of 0 to 10
/delay ${Math.Calc[${Math.Rand[10]}+5]}s       Delays the macro for a random amount of seconds in the range of 5 to 15
```

* The below example will hold down the forward key and will execute "/keypress forward" (press forward once) when

  ${Spawn[1234\].Distance} \&lt; ${Spawn\[1234].MaxMeleeTo} evaluates to TRUE or after 1 second passes.

```text
/keypress forward hold
/delay 1s ${Spawn[1234].Distance}<${Spawn[1234].MaxMeleeTo}
/keypress forward
```

