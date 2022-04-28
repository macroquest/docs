# /docommand

## Syntax

**/docommand** _**command**_

## Description

Executes _command_, parsing [MQ2Data](../../documentation/mqdata.md) first. This is useful for executing commands using MQ2Data that do not parse immediately, as well as executing a command stored in a variable.

## Examples

* A simple example that echoes "sitting" if sitting, and "not sitting" if not

```text
/docommand ${If[${Me.Sitting},/echo sitting,/echo not sitting]}
```

* A simple example that activates AA 177 if you have a target, and echoes "no target" if not.

```text
/docommand ${If[${Target.ID},/alt activate 177,/echo No Target]}
```

