## Syntax

**<span style="color:red">/squelch</span> *command***

## Description

Executes *command* while preventing any output from that *command*.

Basically, it does the following:

1.  Turns mq filter off
2.  Executes *command*
3.  Turns mq filter back to the state it was in before step 1

## Example

    /squelch /attack on

[Return to Slash Commands](slash-commands.md)


