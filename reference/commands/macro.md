---
tags:
    - command
---
# /macro

## Syntax

**/macro** _filename_ **[** _param0_ **[** _param1_ **[**...**]]]**

## Description

Executes a macro file. Supports passing parameters to the macro's `Sub Main` entry point.

## Notes

* Calling a macro from another macro will immediately terminate the calling macro (no cleanup).  
* Parameters are passed as space-separated values to `Sub Main` (params with spaces must be quoted)
* File resolution:
    - Appends `.mac` extension if missing
    - Searches relative to `Macros/` directory
    - Supports absolute paths

## Examples
```text
/macro mymacro
/macro subdir/mymacro "goblin" 5
/macro "/full/path/to/macros/tradeskill.mac" "Smithing"
```