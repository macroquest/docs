# TLO:Int

## Description

Object that creates an integer from n.

## Forms

* [_int_](../data-types/datatype-int.md) **Int[**n**]**

## Access to Types

* [_int_](../data-types/datatype-int.md) **int**

## Examples

`/echo ${Int[123].Hex}`

Echos the result of the conversion of 123 to an int in hexadecimal.

`/echo ${Int[textstringhere]}`

Echos a zero - useful if passing a string to a macro or subroutine that could be a text string or a number and you want to do different actions depending on what you recieve

`/echo ${Int[123]}`

Echos 123

## See Also

* [Top-Level Objects](./)
* [int](../data-types/datatype-int.md)

