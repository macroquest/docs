# TLO:Bool

## Description

Creates a bool object using text. Value is set to TRUE unless text is "NULL" "FALSE" or "0" (capitalization does not count).

## Forms

* [_bool_](../data-types/datatype-bool.md) **Bool[**text**]**

## Access to Types

* [_bool_](../data-types/datatype-bool.md) **bool**

## Examples

`/declare MyVar bool`  
`/varset MyVar ${Bool[This is true]}`  
`/echo ${MyVar}`

_This would output TRUE_

`/declare MyVar bool`  
`/varset MyVar ${Bool[NULL]}`  
`/echo ${MyVar}`

_This would output FALSE_
