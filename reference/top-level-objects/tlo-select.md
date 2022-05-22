---
tags:
    - tlo
---

# `Select`

Object used to determine if a match was made to argument in the given set of values.

## Forms

[_int_](../data-types/datatype-int.md) **Select**[_argument_,_value1_[,_value2_,...]]


!!! example
    Given:

    ```
    /declare thing string outer foo
    ```

    The following are true:

    ```
    | Outputs: 1
    /echo ${Select[${thing},foo,bar,baz]}

    | Outputs: 2
    /echo ${Select[${thing},bin,foo,baz]}

    | Outputs: 3
    /echo ${Select[${thing},bin,baz,foo]}

    | Outputs: 0
    /echo ${Select[${thing},bin,bar,baz]}
    ```

!!! example

    ```
    /if (${Select[${Target.Class.ShortName},CLR,DRU,SHM]} > 0) {
        /echo Target is a healer
    }
    ```

