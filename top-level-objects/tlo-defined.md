## Description

Determines whether a variable, array, or timer with this name exists. The variable, array or timer must not be enclosed
with ${}.

## Forms

-   *[bool](../data-types/datatype-bool.md)* **Defined\[**name**\]**

## Access to Types

-   *[bool](../data-types/datatype-bool.md)* **bool**

## Examples

`/if (${Defined[varname]}) {`  
`  /echo ${varname}`  
`}`

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [bool](../data-types/datatype-bool.md)


