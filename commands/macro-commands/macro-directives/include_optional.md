# \#include\_optional

## Description

\#include\_optional filename

This allows you to optionally include the contents of another file \(called a "snippet"\) within your macro. It functions identically to include except that if the file does not exist, it will continue without error.

## Example

```text
#include_optional spell_routines.inc
Sub Main
  /call Cast "Complete Healing" gem1
/return
```

## See Also

* [include](include.md)
* [Pound\_Commands](/)
* [Macro\_Reference](../../../documentation/macro-reference.md)

