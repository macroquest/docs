---
tags:
    - datatype
---
# `keyring`

This datatype represents information about a keyring (a.k.a. a collection of mounts, illusions, etc)

## Members

### {{ renderMember(type='int', name='Count') }}

:   The number of items in this keyring

### {{ renderMember(type='keyringitem', name='Stat') }}

:   The keyring item assigned as the stat item


## Examples

!!! example

    If **Jungle Raptor Saddle** is set as your **Stat Mount**:

    ```
    /echo ${Mount.Stat}
    ```

    Outputs: Jungle Raptor Saddle

    If you have **3** items in your Mounts keyring:

    ```
    /echo ${Mount.Count}
    ```

    Outputs: 3

[int]: datatype-int.md
[keyringitem]: datatype-keyringitem.md
