---
tags:
    - datatype
---
# `keyringitem`

This datatype deals strictly with information items on a keyring.

## Members

### {{ renderMember(type='int', name='Index') }}

:   Where on the keyring list

### {{ renderMember(type='item', name='Item') }}

:   The item on the keyring

### {{ renderMember(type='string', name='Name') }}

:   name of the keyring item


## Examples

!!! examples

    ```
    /echo ${Mount[1].Name}
    ```

    Outputs: Whirligig Flyer Control Device

    ```
    /echo ${Mount[2].Name}
    ```

    Outputs: Abyssal Steed

    ```
    /echo ${Mount[Abyssal Steed].Index}
    ```

    Outputs: 2

[int]: datatype-int.md
[string]: datatype-string.md
[item]: datatype-item.md
