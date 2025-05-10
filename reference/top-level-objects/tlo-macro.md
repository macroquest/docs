---
tags:
    - tlo
---
# `Macro`

<!--tlo-desc-start-->
Information about the macro that's currently running. 
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='macro', name='Macro') }}

:   Returns an object related to the macro that is currently running.

    !!! example

        ```
        /echo This macro has been running for: ${Macro.RunTime} seconds
        ```
<!--tlo-forms-end-->
<!--tlo-linkrefs-start-->
[macro]: ../data-types/datatype-macro.md
<!--tlo-linkrefs-end-->
