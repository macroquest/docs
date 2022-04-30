# TLO:Defined

## Description

Determines whether a variable, array, or timer with this name exists. The variable, array or timer must not be enclosed with ${}.

## Forms

* [_bool_](../data-types/datatype-bool.md) **Defined[**name**]**

## Access to Types

* [_bool_](../data-types/datatype-bool.md) **bool**

## Examples

`/if (${Defined[varname]}) {`  
`/echo ${varname}`  
`}`
