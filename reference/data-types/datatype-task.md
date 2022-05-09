# DataType:task

This is the type for your current task.

## Members

<table>
  <thead>
    <tr>
      <th style="text-align:left"><b>Type</b>
      </th>
      <th style="text-align:left"><b>Member</b>
      </th>
      <th style="text-align:left"><b>Description</b>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Index</b>
        </td>
        <td style="text-align:left">Returns the task&apos;s place on the tasklist</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Objective[#].Instruction</b>
        </td>
        <td style="text-align:left">Returns a tasks&apos;s Objectives</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Objective[#].Status</b>
        </td>
        <td style="text-align:left">Returns the status of the objective in the format amount done Vs total
          IE 0/3</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Objective[#].Zone</b>
        </td>
        <td style="text-align:left">Returns the zone the objective is to be performed in</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CurrentCount</b>
      </td>
      <td style="text-align:left">Returns the current count of the .Type needed to complete a objective</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>RequiredCount</b>
      </td>
      <td style="text-align:left">Returns the required count of the .Type needed to complete a objective</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Optional</b>
      </td>
      <td style="text-align:left">Returns true or false if a objective is optional</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>RequiredItem</b>
        </td>
        <td style="text-align:left">Returns a string of the required item to complete a objective.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>RequiredSkill</b>
        </td>
        <td style="text-align:left">Returns a string of the required skill to complete a objective.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>RequiredSpell</b>
        </td>
        <td style="text-align:left">Returns a string of the required spell to complete a objective.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>DZSwitchID</b>
      </td>
      <td style="text-align:left">Returns an int of the switch used in a objective.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>ID</b>
      </td>
      <td style="text-align:left">Returns an int of the task ID</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Step</b>
        </td>
        <td style="text-align:left">Returns description of current step in the task</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Select</b>
        </td>
        <td style="text-align:left">Selects the task</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Title</b>
        </td>
        <td style="text-align:left">Returns name of the shared task</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-timestamp.md"><em>timestamp</em></a></td>
      <td
      style="text-align:left"><b>Timer</b>
        </td>
        <td style="text-align:left">Returns amount of time before task expires</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Members</b>
      </td>
      <td style="text-align:left">Returns number of members in task</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-task.md"><em>taskmember</em></a>
      </td>
      <td style="text-align:left"><b>Member[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Returns specified member in task by index</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-task.md"><em>taskmember</em></a>
      </td>
      <td style="text-align:left"><b>Member[</b>name<b>]</b>
      </td>
      <td style="text-align:left">Returns specified member in task by name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Leader</b>
        </td>
        <td style="text-align:left">Returns task leader&apos;s name</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>WindowIndex</b>
      </td>
      <td style="text-align:left">Returns the Quest Window List Index. (if the window actually has the list
        filled)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Type</b>
        </td>
        <td style="text-align:left">
          <p>Returns a string that can be one of the following:</p>
          <ul>
            <li>Unknown</li>
            <li>None</li>
            <li>Deliver</li>
            <li>Kill</li>
            <li>Loot</li>
            <li>Hail</li>
            <li>Explore</li>
            <li>Tradeskill</li>
            <li>Fishing</li>
            <li>Foraging</li>
            <li>Cast</li>
            <li>UseSkill</li>
            <li>DZSwitch</li>
            <li>DestroyObject</li>
            <li>Collect</li>
            <li>Dialogue</li>
          </ul>
        </td>
    </tr>
  </tbody>
</table>

## Examples

`- Task TLO can be accessed by index to make iteration possible.`  
`Example: /echo ${Task[2].Title}`  
`NOTE: THIS INDEX IS NOT THE SAME INDEX AS THE ONE YOU SEE IN THE QUEST WINDOW LIST.`  
`We are iterating through the IN MEMORY quest entries, we are NOT`  
`iterating the window list, if you want to do that, use the Window TLO.`

If you're smart don't use ${Task[1].ID} and expect it to be whatever is the first list item. ALWAYS refer to tasks by their NAME.

`Example: /echo ${Task[3].WindowIndex}`  
`Example: /echo ${Task[Into The Muck].WindowIndex}`

`/echo ${Task[hatch].Type}`

Output: Shared (Can be Shared or Quest in this context)

The Task TLO also has a .Select "Method":

".Select" can select list items and combobox items.

".Select" returns TRUE if a selection was made and FALSE if not.

`/if (${Task[hatch].Select}) {`  
`/echo I just Selected a task that has the name "hatch" in it...`  
`} else {`  
`/echo I did not find a task that has the word "hatch" in it, so nothing was selected.`  
`}`  
`/echo The task with "hatch" in is name is called: ${Task[hatch]}`

Output: The task with "hatch" in is name is called: Hatching a Plan

`/echo ${Task[hatch]} is listed as number ${Task[hatch].Index} in the tasklist.`

Output: Hatching a Plan is listed as number 1 in the tasklist.

`/echo The ${Task[hatch]} first objective is to ${Task[hatch].Objective[1].Instruction}`

Output: The Hatching a Plan first objective is to find where the eggs are being incubated

`/echo The ${Task[hatch]} first objective status is ${Task[hatch].Objective[1].Status}`

Output: The Hatching a Plan first objective status is 0/1

`/echo The ${Task[hatch]} first objective should be completed in ${Task[hatch].Objective[1].Zone}`

Output: The Hatching a Plan first objective should be completed in Hatchery Wing

`/echo I should be working on ${Task[hatch].Step} in ${Task[hatch].Step.Zone}`

