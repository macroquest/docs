## Syntax

**<span style="color:red">/doevents</span> \[ <span style="color:blue">flush</span> \] \[ *specificevent* \]**

## Description

Runs the first event of any type in the queue, flushes all queued events, or runs/flushes just the *specificevent*
event.

## Examples

    /doevents                         This will run all queued events
    /doevents chat                    This will run only the chat event(s) 
    /doevents flush                   Clears all events in the queue without running them
    /doevents SpellFizzle             Run SpellFizzle event(s)

    /doevents flush SpellFizzle       Clears SpellFizzle events in the queue 

## See Also

-   [Custom Events](../macros/custom-events.md)

[Return to Slash Commands](../commands/slash-commands.md)


