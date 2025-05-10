---
tags:
    - tlo
---
# `Task`

<!--tlo-desc-start-->
Object used to return information on a current Task.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='task', name='Task') }}
<!--tlo-forms-end-->

## Usage

```
/echo ${Task[1].Title}
```

Will return the name of the first task, or the current shared task if one exists.
<!--tlo-linkrefs-start-->
[task]: ../data-types/datatype-task.md
<!--tlo-linkrefs-end-->
