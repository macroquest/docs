# DataType:mount

## Description

This datatype deals strictly with information on your "Mount" keyring.

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_int_](datatype-int.md) | **Index** | Where on the keyring list |
| [_string_]() | **Name** | name of the mount in XX slot |
|  |  |  |

## Examples

`/echo ${Mount[1].Name}`  
\`\`

Outputs: \[MQ2\] Whirligig Flyer Control Device

`/echo ${Mount[2].Name}`  
\`\`

Outputs: \[MQ2\] Abyssal Steed

`/echo ${Mount[Abyssal Steed].Index}`

Outputs: \[MQ2\] 2

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)

