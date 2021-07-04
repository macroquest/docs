## Description

Count of items in bank by partial name match. Using =name will find the exact match only.

## Forms

|                                                                     |                                              |
|---------------------------------------------------------------------|----------------------------------------------|
| *[int](../data-types/datatype-int.md)* **FindItemBankCount\[**name**\]**  | Count of items in bank by partial name match |
| *[int](../data-types/datatype-int.md)* **FindItemBankCount\[**=name**\]** | Count of items in bank by exact name match   |

## Access to Types

-   *[int](../data-types/datatype-int.md)* **int**

## Examples

`  /echo ${FindItemBankCount[=Swirling Shadows]}`

Returns how many Swirling Shadows you have in your bank

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [int](../data-types/datatype-int.md)


