# DataType:corpse

Data related to a specified corpse

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_item_](datatype-item.md) | **Item[**\#**]** | \#th item on the corpse |
| [_item_](datatype-item.md) | **Item[**name**\]** | Finds an item by partial _name_ in this corpse (use **Item\[=\***name**\*]** for exact) |
| [_int_](datatype-int.md) | **Items** | Number of items on the corpse |
| [_bool_](datatype-bool.md) | **Open** | Corpse open? |
| \_\_[_string_](datatype-string.md)\_\_ | **To String** | Same as **Open** |

## Examples

`/if (${Corpse.Open} && ${Corpse.Items}) /call LootCorpse`

