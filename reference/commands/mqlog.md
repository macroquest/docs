---
tags:
    - command
---
# /mqlog

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/mqlog clear | <text>
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
This will log _text_ to a log file in the "Logs" directory. Clear will delete everything in the log file.
<!--cmd-desc-end-->

## Notes

* The log filename will be _macroname.mac.log_ if run from within a macro
* The log filename will be _MacroQuest.log_ if issued normally

## Example

```text
/mqlog The number of combines completed is: ${CombineCount}
```
