# TLO:Task

## Description

Object used to return information on a current Task.

## Changes

Oct 02 2019 by Eqmule

* Made some changes to the ${Task} TLO

`It's likely some macros will break due to these changes, but`  
`I felt the upside with not having to rely on the window warrants that.`  
\`\`

New Feature: It's no longer needed to have the task window open to access the TLO. Added .Type to the TaskObjective TLO

`It returns a string that can be one of the following:`  
`Unknown,None,Deliver,Kill,Loot,Hail,Explore,Tradeskill,Fishing,`  
`Foraging,Cast,UseSkill,DZSwitch,DestroyObject,Collect,Dialogue`

Added .CurrentCount which returns the current count of the .Type needed to complete a objective.

Added .RequiredCount which returns the required count of the .Type needed to complete a objective.

Added .Optional which returns true or false if a objective is optional

Added .RequiredItem which returns a string of the required item to complete a objective.

Added .RequiredSkill which returns a string of the required skill to complete a objective.

Added .RequiredSpell which returns a string of the required spell to complete a objective.

Added .DZSwitchID which returns a int of the switch used in a objective.

`Example: /echo ${Task[The Grand Illusion].Objective[1].CurrentCount}`

Added .ID to the ${Task} TLO it returns an int of the task ID

`Example: /echo ${Task[The Grand Illusion].ID}`

Ok so fair warning, the taskwindow doesn't add items by index, unless sorted by first column, and even then, it can be "off" (because reasons) so... if you are smart don't use ${Task[1].ID} and expect it to be whatever is the first list item. ALWAYS refer to tasks by their NAME.

so like:

`${Task[The Grand Illusion].Step.Index} WILL absolutely always return the correct index`  
`as returned by the taskmanager, but it might not be the index you "see" in the window.`  
`Bottomline, we should not rely on the window anymore.`  
`It's useful to look up the name of the tasks, basically.`

## Forms

* [_task_](../data-types/datatype-task.md) **Task**

## Examples

`/echo ${Task[Task Name].Title}`

Will return Into the Hills

`/echo ${Task[Task Name].Timer}`

Will return 3521

`/echo ${Task[Task Name].Member[1].Name}`

Will return Eqmule

`/echo ${Task[Task Name].Member[eqmule].Leader}`

Will return True (if leader)

`/echo ${Task[Task Name].Member[eqmule].Index}`

Will return 1
