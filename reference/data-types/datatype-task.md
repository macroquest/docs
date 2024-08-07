---
tags:
    - datatype
---
# `task`

This is the type for your current task.

## Members

### {{ renderMember(type='int', name='ID') }}

:   Returns an int of the task ID

### {{ renderMember(type='string', name='Index') }}

:   Returns the tasks' place on the tasklist

### {{ renderMember(type='string', name='Leader') }}

:   Returns task leader's name

### {{ renderMember(type='taskmember', name='Member', params='#') }}

:   Returns specified member in task by index

### {{ renderMember(type='taskmember', name='Member', params='name') }}

:   Returns specified member in task by name

### {{ renderMember(type='int', name='Members') }}

:   Returns number of members in task

### {{ renderMember(type='taskobjective', name='Objective', params='#') }}

:   Returns the specified objective

### {{ renderMember(type='string', name='Step') }}

:   Returns description of current step in the task

### {{ renderMember(type='timestamp', name='Timer') }}

:   Returns amount of time before task expires

### {{ renderMember(type='string', name='Title') }}

:   Returns name of the shared task

### {{ renderMember(type='string', name='Type') }}

:   Returns a string that can be one of the following:

    - Unknown
    - None
    - Deliver
    - Kill
    - Loot
    - Hail
    - Explore
    - Tradeskill
    - Fishing
    - Foraging
    - Cast
    - UseSkill
    - DZSwitch
    - DestroyObject
    - Collect
    - Dialogue

### {{ renderMember(type='int', name='WindowIndex') }}

:   Returns the Quest Window List Index. (if the window actually has the list filled)


## Methods

| Name | Action |
| :--- | :--- |
| **Select**[_name_] | Select the given task name in the UI |


## Usage

### Indexing Tasks

Task TLO can be accessed by index to make iteration possible.

```
/echo ${Task[2].Title}
```

Don't use `${Task[1].ID}` and expect it to be whatever is the first list item. Always refer to tasks by their name.

!!! Note

    This index is not the same index as the one you see in the quest window list.

    Tasks are accessed in memory order, not in the order they are displayed in the UI. If you want the UI order, you'll need to use the [Window TLO](../top-level-objects/tlo-window.md).

```
/echo ${Task[3].WindowIndex}
```

```
/echo ${Task[Into The Muck].WindowIndex}
```

```
/echo ${Task[hatch].Type}
```

Output: Shared (Can be Shared or Quest in this context)

## Selection

The Task TLO also has a `Select` Method:

`Select` can select list items and combobox items. It returns TRUE if a selection was made and FALSE if not.

```
/if (${Task[hatch].Select}) {
    /echo I just Selected a task that has the name "hatch" in it...
} else {
    /echo I did not find a task that has the word "hatch" in it, so nothing was selected.
}

/echo The task with "hatch" in is name is called: ${Task[hatch]}
```

## Examples

!!! Example

    Output: The task with "hatch" in is name is called: Hatching a Plan

    ```
    /echo ${Task[hatch]} is listed as number ${Task[hatch].Index} in the tasklist.
    ```

!!! Example

     Output: Hatching a Plan is listed as number 1 in the tasklist.

    ```
    /echo The ${Task[hatch]} first objective is to ${Task[hatch].Objective[1].Instruction}
    ```

!!! Example

    Output: The Hatching a Plan first objective is to find where the eggs are being incubated

    ```
    /echo The ${Task[hatch]} first objective status is ${Task[hatch].Objective[1].Status}
    ```

!!! Example

    Output: The Hatching a Plan first objective status is 0/1

    ```
    /echo The ${Task[hatch]} first objective should be completed in ${Task[hatch].Objective[1].Zone}
    ```

!!! Example

    Output: The Hatching a Plan first objective should be completed in Hatchery Wing

    ```
    /echo I should be working on ${Task[hatch].Step} in ${Task[hatch].Step.Zone}
    ```

[int]: datatype-int.md
[string]: datatype-string.md
[taskmember]: datatype-task.md
[taskobjective]: datatype-taskobjective.md
[timestamp]: datatype-timestamp.md
