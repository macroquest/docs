## Description

This is the type for your current task.

## Members

<table>
<tbody>
<tr class="odd">
<td><p><strong>Type</strong></p></td>
<td><p><strong>Member</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Index</strong></p></td>
<td><p>Returns the task's place on the tasklist</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Objective[#].Instruction</strong></p></td>
<td><p>Returns a tasks's Objectives</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Objective[#].Status</strong></p></td>
<td><p>Returns the status of the objective in the format amount done Vs total IE 0/3</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Objective[#].Zone</strong></p></td>
<td><p>Returns the zone the objective is to be performed in</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>CurrentCount</strong></p></td>
<td><p>Returns the current count of the .Type needed to complete a objective</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>RequiredCount</strong></p></td>
<td><p>Returns the required count of the .Type needed to complete a objective</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Optional</strong></p></td>
<td><p>Returns true or false if a objective is optional</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>RequiredItem</strong></p></td>
<td><p>Returns a string of the required item to complete a objective.</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>RequiredSkill</strong></p></td>
<td><p>Returns a string of the required skill to complete a objective.</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>RequiredSpell</strong></p></td>
<td><p>Returns a string of the required spell to complete a objective.</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>DZSwitchID</strong></p></td>
<td><p>Returns an int of the switch used in a objective.</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>ID</strong></p></td>
<td><p>Returns an int of the task ID</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Step</strong></p></td>
<td><p>Returns description of current step in the task</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Select</strong></p></td>
<td><p>Selects the task</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Title</strong></p></td>
<td><p>Returns name of the shared task</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-ticks.md">ticks</a></em></p></td>
<td><p><strong>Timer</strong></p></td>
<td><p>Returns amount of time before task expires</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Members</strong></p></td>
<td><p>Returns number of members in task</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-taskmember.md">taskmember</a></em></p></td>
<td><p><strong>Member[</strong>#<strong>]</strong></p></td>
<td><p>Returns specified member in task by index</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-taskmember.md">taskmember</a></em></p></td>
<td><p><strong>Member[</strong>name<strong>]</strong></p></td>
<td><p>Returns specified member in task by name</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Leader</strong></p></td>
<td><p>Returns task leader's name</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>WindowIndex</strong></p></td>
<td><p>Returns the Quest Window List Index. (if the window actually has the list filled)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Type</strong></p></td>
<td><p>Returns a string that can be one of the following:</p>
<p><code> Unknown,None,Deliver,Kill,Loot,Hail,Explore,Tradeskill,Fishing,</code><br />
<code> Foraging,Cast,UseSkill,DZSwitch,DestroyObject,Collect,Dialogue</code></p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Examples

`- Task TLO can be accessed by index to make iteration possible.`  
`Example: /echo ${Task[2].Title}`  
`NOTE: THIS INDEX IS NOT THE SAME INDEX AS THE ONE YOU SEE IN THE QUEST WINDOW LIST.`  
`We are iterating through the IN MEMORY quest entries, we are NOT`  
`iterating the window list, if you want to do that, use the Window TLO.`

If you're smart don't use ${Task\[1\].ID} and expect it to be whatever is the first list item. ALWAYS refer to tasks by
their NAME.

`Example: /echo ${Task[3].WindowIndex}`  
`Example: /echo ${Task[Into The Muck].WindowIndex}`

`/echo ${Task[hatch].Type}`

Output: Shared (Can be Shared or Quest in this context)

The Task TLO also has a .Select "Method":

  
  
".Select" can select list items and combobox items.

".Select" returns TRUE if a selection was made and FALSE if not.

`/if (${Task[hatch].Select}) {`  
`    /echo I just Selected a task that has the name "hatch" in it...`  
`} else {`  
`    /echo I did not find a task that has the word "hatch" in it, so nothing was selected.`  
`}`  
` /echo The task with "hatch" in is name is called: ${Task[hatch]} `

Output: The task with "hatch" in is name is called: Hatching a Plan

` /echo ${Task[hatch]} is listed as number ${Task[hatch].Index} in the tasklist.`

Output: Hatching a Plan is listed as number 1 in the tasklist.

` /echo The ${Task[hatch]} first objective is to ${Task[hatch].Objective[1].Instruction}`

Output: The Hatching a Plan first objective is to find where the eggs are being incubated

` /echo The ${Task[hatch]} first objective status is ${Task[hatch].Objective[1].Status} `

Output: The Hatching a Plan first objective status is 0/1

` /echo The ${Task[hatch]} first objective should be completed in ${Task[hatch].Objective[1].Zone}`

Output: The Hatching a Plan first objective should be completed in Hatchery Wing

` /echo I should be working on ${Task[hatch].Step} in ${Task[hatch].Step.Zone}`

## See Also

-   [TLO:Task](../top-level-objects/tlo-task.md)
-   [DataType:taskmember](datatype-taskmember.md)


