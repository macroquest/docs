---
tags:
    - datatype
---
# `fellowshipmember`

Contains all the data related to fellowship members

## Members

### {{ renderMember(type='class', name='Class') }}

:   Member's class

### {{ renderMember(type='ticks', name='LastOn') }}

:   How long since member was last online

### {{ renderMember(type='int', name='Level') }}

:   Member's level

### {{ renderMember(type='string', name='Name') }}

:   Member's name

### {{ renderMember(type='bool', name='Sharing') }}

:   TRUE if member has exp sharing enabled

### {{ renderMember(type='zone', name='Zone') }}

:   Zone information for the member's zone

### [string][string] `To String`

:   player name


## Changelog

* March 7th, 2021: Added Sharing

[bool]: datatype-bool.md
[class]: datatype-class.md
[int]: datatype-int.md
[string]: datatype-string.md
[ticks]: datatype-ticks.md
[zone]: datatype-zone.md
