---
tags:
    - datatype
---
# `keyring`

<!--dt-desc-start-->
This datatype represents information about a keyring (a.k.a. a collection of mounts, illusions, etc)
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='int', name='Count') }}

:   The number of items in this keyring

### {{ renderMember(type='keyringitem', name='Stat') }}

:   The keyring item assigned as the stat item
<!--dt-members-end-->

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
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[keyringitem]: datatype-keyringitem.md
<!--dt-linkrefs-end-->
