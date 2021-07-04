## Description

Creates a bool object using text. Value is set to TRUE unless text is "NULL" "FALSE" or "0" (capitalization does not
count).

## Forms

-   *[bool](../data-types/datatype-bool.md)* **Bool\[**text**\]**

## Access to Types

-   *[bool](../data-types/datatype-bool.md)* **bool**

## Examples

`/declare MyVar bool`  
`/varset MyVar ${Bool[This is true]}`  
`/echo ${MyVar}`

*This would output TRUE*

`/declare MyVar bool`  
`/varset MyVar ${Bool[NULL]}`  
`/echo ${MyVar}`

*This would output FALSE*

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [bool](../data-types/datatype-bool.md)


