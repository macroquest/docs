---
tags:
    - command
---
# /mqlog

## Syntax

**/mqlog clear \|** _**text**_

## Description

This will log _text_ to a log file in the "Logs" directory

**Notes**

* The log filename will be _macroname.mac.log_ if run from within a macro
* The log filename will be _MacroQuest.log_ if issued normally

## Example

```text
/mqlog The number of combines completed is: ${CombineCount}
```

