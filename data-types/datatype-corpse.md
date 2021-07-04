## Description

Data related to a specified corpse

## Members

|                                        |                      |                                                                                        |
|----------------------------------------|----------------------|----------------------------------------------------------------------------------------|
| **Type**                               | **Member**           | **Description**                                                                        |
| *[item](datatype-item.md)*     | **Item\[**#**\]**    | #th item on the corpse                                                                 |
| *[item](datatype-item.md)*     | **Item\[**name**\]** | Finds an item by partial *name* in this corpse (use **Item\[=***name***\]** for exact) |
| *[int](datatype-int.md)*       | **Items**            | Number of items on the corpse                                                          |
| *[bool](datatype-bool.md)*     | **Open**             | Corpse open?                                                                           |
| '**'[bool](datatype-bool.md)** | **To String**        | Same as **Open**                                                                       |

## Examples

`/if (${Corpse.Open} && ${Corpse.Items}) /call LootCorpse`

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Corpse](../top-level-objects/tlo-corpse.md)


