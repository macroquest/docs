---
tags:
    - command
---
# /next

## Syntax
```eqcommand
/for <varname> <initial-value> to|downto <final-value> [step <interval>]
/next <varname>
```

## Description

This runs all commands between the /for line and the /next line, after which it increments/decrements the _varname_ number (#1) by _step_ number (#3) \(default is 1) before running through the commands again. It will keep doing this until the _varname_ number equals #2. You can end a /for loop immediately with /break or try the next iteration with /continue.

## See also
* [/for](for.md)
