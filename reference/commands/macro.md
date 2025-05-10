---
tags:
    - command
---
# /macro

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/macro <filename> [ <param0> [ <param1> [...]]]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Executes a macro file. Supports passing parameters to the macro's `Sub Main` entry point.
<!--cmd-desc-end-->
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