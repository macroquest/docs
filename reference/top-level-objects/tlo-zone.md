---
tags:
    - tlo
---

# `Zone`

Used to find information about a particular zone.

## Forms

[_currentzone_][currentzone] **Zone**

:   Retrieves the current zone information

[_zone_][zone] **Zone**[_N_]

:   Retrieves information about a zone by zone ID. If this zone is the current zone, then
    this will return [currentzone].

[_zone_][zone] **Zone**[_shortname_]

:   Retrieves information about a zone by short name. If this zone is the current zone, then
    this will return [currentzone].

## Examples

```
/echo ${Zone.Type}
```

Returns an integer representing the zone you are currently in.

```
/echo ${Zone.Indoor}
```

Returns TRUE if you're indoors, FALSE if not.

```
/echo ${Zone[zonename].ID}
```

Returns the ID of _zonename_, even if you aren't in the zone.

```
/echo ${Zone[zoneid].ShortName}
```

Returns the short name of the zone with ID _zoneid_.


[zone]: ../data-types/datatype-zone.md
[currentzone]: ../data-types/datatype-currentzone.md
