---
tags:
    - datatype
---
# `keyringitem`

This datatype deals strictly with information items on a keyring.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Index** | Where on the keyring list |
| [item](datatype-item.md) | **Item** | The item on the keyring |
| [_string_](datatype-string.md) | **Name** | name of the keyring item |

## Examples

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

