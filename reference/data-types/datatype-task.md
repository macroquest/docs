---
tags:
    - datatype
---
# `task`

This is the type for your current task.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_string_](datatype-string.md) | **Index** | Returns the task&apos;s place on the tasklist |
| [_string_](datatype-string.md) | **Objective[#].Instruction** | Returns a tasks&apos;s Objectives |
| [_string_](datatype-string.md) | **Objective[#].Status** | Returns the status of the objective in the format amount done Vs total IE 0/3 |      
| [_string_](datatype-string.md) | **Objective[#].Zone** | Returns the zone the objective is to be performed in |
| [_int_](datatype-int.md) | **CurrentCount** | Returns the current count of the .Type needed to complete a objective |
| [_int_](datatype-int.md) | **RequiredCount** | Returns the required count of the .Type needed to complete a objective |
| [_bool_](datatype-bool.md) | **Optional** | Returns true or false if a objective is optional |
| [_string_](datatype-string.md) | **RequiredItem** | Returns a string of the required item to complete a objective.|
| [_string_](datatype-string.md) | **RequiredSkill** | Returns a string of the required skill to complete a objective.|
| [_string_](datatype-string.md) | **RequiredSpell** | Returns a string of the required spell to complete a objective.|
| [_int_](datatype-int.md) | **DZSwitchID** | Returns an int of the switch used in a objective.|
| [_int_](datatype-int.md) | **ID** | Returns an int of the task ID|
| [_string_](datatype-string.md) | **Step** | Returns description of current step in the task|
| [_string_](datatype-string.md) | **Select** | Selects the task|
| [_string_](datatype-string.md) | **Title** | Returns name of the shared task|
| [_timestamp_](datatype-timestamp.md) | **Timer** | Returns amount of time before task expires|
| [_int_](datatype-int.md) | **Members** | Returns number of members in task|
| [_taskmember_](datatype-task.md) | **Member[</b>#<b>]** | Returns specified member in task by index|
| [_taskmember_](datatype-task.md) | **Member[</b>name<b>]** | Returns specified member in task by name|
| [_string_](datatype-string.md) | **Leader** | Returns task leader&apos;s name|
| [_int_](datatype-int.md) | **WindowIndex** | Returns the Quest Window List Index. (if the window actually has the list filled)|
| [_string_](datatype-string.md) | **Type** | Returns a string that can be one of the following:<ul><li>Unknown</li><li>None</li><li>Deliver</li><li>Kill</li><li>Loot</li><li>Hail</li><li>Explore</li><li>Tradeskill</li><li>Fishing</li><li>Foraging</li><li>Cast</li><li>UseSkill</li><li>DZSwitch</li><li>DestroyObject</li><li>Collect</li><li>Dialogue</li></ul> |

## Methods

| Name | Action |
| :--- | :--- |
| **Select**[_name_] | Select the given task name in the UI |


## Usage

### Indexing Tasks

Task TLO can be accessed by index to make iteration possible.

Example: `/echo ${Task[2].Title}`

Don't use `${Task[1].ID}` and expect it to be whatever is the first list item. Always refer to tasks by their name.

!!! Note

    This index is not the same index as the one you see in the quest window list.

    Tasks are accessed in memory order, not in the order they are displayed in the UI. If you want the UI order, you'll need to use the [Window TLO](../top-level-objects/tlo-window.md).

Example: `/echo ${Task[3].WindowIndex}`

Example: `/echo ${Task[Into The Muck].WindowIndex}`

`/echo ${Task[hatch].Type}`

Output: Shared (Can be Shared or Quest in this context)

### Selection

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

### Examples

Output: The task with "hatch" in is name is called: Hatching a Plan

:   
    ```
    /echo ${Task[hatch]} is listed as number ${Task[hatch].Index} in the tasklist.
    ```

Output: Hatching a Plan is listed as number 1 in the tasklist.

:   
    ```
    /echo The ${Task[hatch]} first objective is to ${Task[hatch].Objective[1].Instruction}
    ```

Output: The Hatching a Plan first objective is to find where the eggs are being incubated

:   
    ```
    /echo The ${Task[hatch]} first objective status is ${Task[hatch].Objective[1].Status}
    ```

Output: The Hatching a Plan first objective status is 0/1

:   
    ```
    /echo The ${Task[hatch]} first objective should be completed in ${Task[hatch].Objective[1].Zone}
    ```

Output: The Hatching a Plan first objective should be completed in Hatchery Wing

:   
    ```
    /echo I should be working on ${Task[hatch].Step} in ${Task[hatch].Step.Zone}
    ```
