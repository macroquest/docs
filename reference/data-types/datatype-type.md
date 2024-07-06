---
tags:
    - datatype
---
# `type`

Contains information about data types

## Members

### {{ renderMember(type='int', name='InheritedType') }}

:   Type of inherited type, if applicable.

    Ex: character inherits from spawn, so its inherited type will be spawn.

### {{ renderMember(type='string', name='Name') }}

:   Type name

### {{ renderMember(type='string', name='Member', params='N') }}

:   Member name based on an internal ID number (based on 1 through _N_, not all values will be used)

### {{ renderMember(type='int', name='Member', params='name') }}

:   Member internal ID number based on _name_ (will be a number from 1 to N)

### [string][string] `(To String)`

:   Same as **Name**


[int]: datatype-int.md
[string]: datatype-string.md
