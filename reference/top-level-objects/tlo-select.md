# TLO:Select

## Description

Object used to determine if a match was made to argument in the given set of values.

## Forms

* [_int_](../data-types/datatype-int.md) **Select[\***argument_,\_value1_\[,_value2_,...\]\*]\_

## Access to Types

* [_int_](../data-types/datatype-int.md) **int**

## Examples

`/declare thing string outer foo`  
`/echo ${Select[${thing},foo,bar,baz]} | output: 1`  
`/echo ${Select[${thing},bin,foo,baz]} | output: 2`  
`/echo ${Select[${thing},bin,baz,foo]} | output: 3`  
`/echo ${Select[${thing},bin,bar,baz]} | output: 0`

`/if (${Select[${Target.Class.ShortName},CLR,DRU,SHM]} > 0) /echo Target is a healer`
