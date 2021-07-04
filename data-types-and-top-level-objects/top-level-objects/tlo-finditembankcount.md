# TLO:FindItemBankCount

## Description

Count of items in bank by partial name match. Using =name will find the exact match only.

## Forms

|  |  |
| :--- | :--- |
| [_int_](../data-types/datatype-int.md) **FindItemBankCount\[**name**\]** | Count of items in bank by partial name match |
| [_int_](../data-types/datatype-int.md) **FindItemBankCount\[**=name**\]** | Count of items in bank by exact name match |

## Access to Types

* [_int_](../data-types/datatype-int.md) **int**

## Examples

`/echo ${FindItemBankCount[=Swirling Shadows]}`

Returns how many Swirling Shadows you have in your bank

## See Also

* [Top-Level Objects](./)
* [int](../data-types/datatype-int.md)

