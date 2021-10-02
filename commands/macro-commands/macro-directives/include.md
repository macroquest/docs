# \#include

## Description

\#include filename

This allows you to include the contents of another file \(called a "snippet"\) within your macro, as though the contents were part of the calling macro. You can access the [Subroutines](../../../documentation/subroutines.md) of the included file using /call, just as though they were a part of the original macro.

## Use

Traditionally the filename extension .inc is used to indicate that it is an include file, but you may use any extension name that you like. When you are including a file, you must make sure you type the name correctly. Include files are case-insensitive \(eg. spells.inc = spellS.inc\).

## Example

```text
#include spell_routines.inc
Sub Main
  /call Cast "Complete Healing" gem1
/return
```

## See Also

* [Pound\_Commands](./)
* [Macro\_Reference](../../../documentation/macro-reference.md)

