---
tags:
    - tlo
---

# `Task`

Object used to return information on a current Task.

## Forms

[_task_](../data-types/datatype-task.md) **Task**

## Examples

```
/echo ${Task[1].Title}
```

Will return the name of the first task, or the current shared task if one exists.

