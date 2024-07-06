---
tags:
    - tlo
---
# `Task`

Object used to return information on a current Task.

## Forms

### {{ renderMember(type='task', name='Task') }}


## Usage

```
/echo ${Task[1].Title}
```

Will return the name of the first task, or the current shared task if one exists.

[task]: ../data-types/datatype-task.md
