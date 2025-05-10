---
tags:
    - tlo
---
# `Cursor`

<!--tlo-desc-start-->
Creates an object which references the item on your cursor.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='item', name='Cursor') }}

:   Access the item on the cursor
<!--tlo-forms-end-->

## Usage

!!! Example

    If something is on your cursor, auto-inventory it.

    ```
    /if (${Cursor.ID}) /autoinventory
    ```
<!--tlo-linkrefs-start-->
[item]: ../data-types/datatype-item.md
<!--tlo-linkrefs-end-->
