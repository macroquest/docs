## Description

This datatype deals strictly with information on your "Mount" keyring.

## Members

|                                        |            |                              |
|----------------------------------------|------------|------------------------------|
| **Type**                               | **Member** | **Description**              |
| *[int](datatype-int.md)*       | **Index**  | Where on the keyring list    |
| *[string](datatype-string.md)* | **Name**   | name of the mount in XX slot |
|                                        |            |                              |

## Examples

` /echo ${Mount[1].Name}`  
` `

Outputs: \[MQ2\] Whirligig Flyer Control Device

` /echo ${Mount[2].Name}`  
` `

Outputs: \[MQ2\] Abyssal Steed

` /echo ${Mount[Abyssal Steed].Index}`

Outputs: \[MQ2\] 2

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)


