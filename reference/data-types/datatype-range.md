---
tags:
    - datatype
---
# `range`

This DataType performs a simple test on _n_ using the following members.

## Members

### {{ renderMember(type='bool', name='Between', params='#1,#2:N') }}

:   True if _N_ is between the range of _#1_ and _#2_, inclusive.

    ???+ Example

        Is 50 between 33 and 66?

        ```
        | Prints TRUE
        /echo ${Range.Between[33,66:50]}
        ```

        Is 25 between 33 and 66?
        
        ```
        | Prints FALSE
        /echo ${Range.Between[33,66:25]}
        ```

### {{ renderMember(type='bool', name='Inside', params='#1,#2:N') }}

:   True if _N_ is within the range of _#1_ and _#2_, exclusive.

    ???+ Example

        Is 50 Inside 33 and 66?
        
        ```
        | Prints TRUE
        /echo ${Range.Inside[33,66:50]}
        ```

        Is 33 inside 33 and 66?
        
        ```
        | Prints FALSE
        ${Range.Inside[33,66:33]}
        ```


[bool]: datatype-bool.md
