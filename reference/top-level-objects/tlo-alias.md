---
tags:
    - tlo
---
# `Alias`

<!--tlo-desc-start-->
Provides a way to query whether a given alias exists. See [/alias](../commands/alias.md).
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='bool', name='Alias', params='Name') }}

:   Returns bool indicating if named aliase exists
<!--tlo-forms-end-->

## Usage

=== "MQScript"

    ```
    | prints TRUE if the /yes alias exists
    /echo ${Alias[/yes]}
    ```

=== "Lua"

    ```lua
    -- prints true if the /yes alias exists
    print(mq.TLO.Alias('/yes')())
    ```
<!--tlo-linkrefs-start-->
[bool]: ../data-types/datatype-bool.md
<!--tlo-linkrefs-end-->