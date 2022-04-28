# /doevents

## Syntax

**/doevents [ flush \] \[** _**specificevent**_ **]**

## Description

Runs the first event of any type in the queue, flushes all queued events, or runs/flushes just the _specificevent_ event.

## Examples

```text
/doevents                         This will run all queued events
/doevents chat                    This will run only the chat event(s) 
/doevents flush                   Clears all events in the queue without running them
/doevents SpellFizzle             Run SpellFizzle event(s)

/doevents flush SpellFizzle       Clears SpellFizzle events in the queue
```

## See Also

* [Custom Events](../../macros/macros/custom-events.md)

[Return to Slash Commands](../slash-commands/)

