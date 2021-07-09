# TLO:Mount

Used to get information about items on your Mount keyring.

## Forms

|  |  |  |
| :--- | :--- | :--- |
| \_\_[_keyring_](../data-types/datatype-keyring.md) | **Mount\[**N**\]** | Retrieves the item in your mount keyring by index |
| [_keyring_](../data-types/datatype-keyring.md) | **Mount\[**name**\]** | Retrieve the item in your mount keyring by name. A `=` can be prepended for an exact match. |

## Examples

`/echo ${Mount[1].Name}`

Outputs: Whirligig Flyer

Displays the first mount in your mount keyring



