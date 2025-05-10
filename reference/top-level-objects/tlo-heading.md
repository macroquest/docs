---
tags:
    - tlo
---
# `Heading`

<!--tlo-desc-start-->
Object that refers to the directional heading to of a location or direction.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='heading', name='Heading', params='#') }}

:   Creates a heading object using degrees (clockwise)

### {{ renderMember(type='heading', name='Heading', params='y,x') }}

:   Creates a heading object using the heading to this y,x location

### {{ renderMember(type='heading', name='Heading', params='N,W') }}

:   Same as above, just an alternate method
<!--tlo-forms-end-->

## Usage

```
/echo ${Heading[15].ShortName}
```

Echos the shortname of the heading of 15 degrees.

```
/echo ${Heading[-342,700].ShortName}
```

Echos the shortname heading to the location -342,700
<!--tlo-linkrefs-start-->
[heading]: ../data-types/datatype-heading.md
<!--tlo-linkrefs-end-->