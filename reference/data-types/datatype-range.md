---
tags:
    - ref
    - datatype
---
[TLO List](../top-level-objects/tlo-list.md) | [DataType List](../data-types/datatype-list.md)
# `range`

This DataType performs a simple test on _n_ using the following members.

## Members

[_bool_][bool] **Between**[_#1_,_#2_:_N_]

:   True if _N_ is between the range of _#1_ and _#2_, inclusive.

    ???+ Example

        Is 50 between 33 and 66? `${Range.Between[33,66:50]}` returns TRUE

        Is 25 between 33 and 66? `${Range.Between[33,66:25]}` returns FALSE

[_bool_][bool] **Inside**[_#1_,_#2_:_N_]

:   True if _N_ is within the range of _#1_ and _#2_, exclusive.

    ???+ Example

        Is 50 Inside 33 and 66? `${Range.Inside[33,66:50]}` returns TRUE

        Is 33 inside 33 and 66? `${Range.Inside[33,66:33]}` returns FALSE

[bool]: datatype-bool.md
