---
tags:
    - command
---
# /squelch

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/squelch <command>
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Executes _command_ while preventing any output from that _command_.

Basically, it does the following:

1. Turns mq filter off
2. Executes _command_
3. Turns mq filter back to the state it was in before step 1
<!--cmd-desc-end-->
## Example

```text
/squelch /attack on
```

