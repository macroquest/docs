## Syntax

**<span style="color:red">/docommand</span> *command***

## Description

Executes *command*, parsing [MQ2Data](../documentation/mq2data.md) first. This is useful for executing commands using MQ2Data
that do not parse immediately, as well as executing a command stored in a variable.

## Examples

-   A simple example that echoes "sitting" if sitting, and "not sitting" if not

<!-- -->

    /docommand ${If[${Me.Sitting},/echo sitting,/echo not sitting]}

-   A simple example that activates AA 177 if you have a target, and echoes "no target" if not.

<!-- -->

    /docommand ${If[${Target.ID},/alt activate 177,/echo No Target]}

[Return to Slash Commands](slash-commands.md)


