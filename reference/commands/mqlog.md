---
tags:
    - command
---
# /mqlog

## Syntax

```eqcommand
/mqlog clear | <text>
```

## Description

This will log _text_ to a log file in the "Logs" directory. Clear will delete everything in the log file.

**Notes**

* The log filename will be _macroname.mac.log_ if run from within a macro
* The log filename will be _MacroQuest.log_ if issued normally

## Example

```text
/mqlog The number of combines completed is: ${CombineCount}
```
