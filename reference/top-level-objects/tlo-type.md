---
tags:
    - tlo
---
# `Type`

Used to get information on data types.

## Forms

### {{ renderMember(type='type', name='Type', params='Name') }}

:   Retrieve metadata about the type with given `Name`


## Usage

Determines if a member of a type exists:

```
/echo ${Type[spawn].Member[ID]}
```

Enumerate members of a type using a loop:

```
/for n 1 to 100
    /echo ${Type[spawn].Member[${n}]}
/next n
```

[type]: ../data-types/datatype-type.md
