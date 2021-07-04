# Squelch

## Syntax

**/squelch** _**command**_

## Description

Executes _command_ while preventing any output from that _command_.

Basically, it does the following:

1. Turns mq filter off
2. Executes _command_
3. Turns mq filter back to the state it was in before step 1

## Example

```text
/squelch /attack on
```

[Return to Slash Commands](./)

