---
tags:
    - tlo
---
# `Cursor`

Creates an object which references the item on your cursor.

## Forms

### {{ renderMember(type='item', name='Cursor') }}

:   Access the item on the cursor


## Usage

!!! Example

    If something is on your cursor, auto-inventory it.

    ```
    /if (${Cursor.ID}) /autoinventory
    ```

[item]: ../data-types/datatype-item.md
