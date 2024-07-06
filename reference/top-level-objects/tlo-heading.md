---
tags:
    - tlo
---
# `Heading`

Object that refers to the directional heading to of a location or direction.

## Forms

### {{ renderMember(type='heading', name='Heading', params='#') }}

:   Creates a heading object using degrees (clockwise)

### {{ renderMember(type='heading', name='Heading', params='y,x') }}

:   Creates a heading object using the heading to this y,x location

### {{ renderMember(type='heading', name='Heading', params='N,W') }}

:   Same as above, just an alternate method


## Usage

```
/echo ${Heading[15].ShortName}
```

Echos the shortname of the heading of 15 degrees.

```
/echo ${Heading[-342,700].ShortName}
```

Echos the shortname heading to the location -342,700


[heading]: ../data-types/datatype-heading.md