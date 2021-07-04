## Description

Contains data on the current raid

## Members

<table>
<tbody>
<tr class="odd">
<td><p><strong>Type</strong></p></td>
<td><p><strong>Member</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>AverageLevel</strong></p></td>
<td><p>Average level of raid members (more accurate than in the window)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Invited</strong></p></td>
<td><p>Have I been invited to the raid?</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-raidmember.md">raidmember</a></em></p></td>
<td><p><strong>Leader</strong></p></td>
<td><p>Raid leader</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Locked</strong></p></td>
<td><p>Returns TRUE if the raid is locked</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Looter[</strong>#<strong>]</strong></p></td>
<td><p>Specified looter name by number</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Looters</strong></p></td>
<td><p>Number of specified looters</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>LootType</strong></p></td>
<td><p>Loot type number:<br />
1 Leader<br />
2 Leader &amp; GroupLeader<br />
3 Leader &amp; Specified</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-raidmember.md">raidmember</a></em></p></td>
<td><p><strong>MainAssist</strong></p></td>
<td><p>Raid main assist</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-raidmember.md">raidmember</a></em></p></td>
<td><p><strong>MasterLooter</strong></p></td>
<td><p>Raid Master Looter</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-raidmember.md">raidmember</a></em></p></td>
<td><p><strong>Member[</strong>#<strong>]</strong></p></td>
<td><p>Raid member by number</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-raidmember.md">raidmember</a></em></p></td>
<td><p><strong>Member[</strong>name<strong>]</strong></p></td>
<td><p>Raid member by <em>name</em></p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Members</strong></p></td>
<td><p>Total number of raid members</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-raidmember.md">raidmember</a></em></p></td>
<td><p><strong>Target</strong></p></td>
<td><p>Raid target (clicked in raid window)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>TotalLevels</strong></p></td>
<td><p>Sum of all raid members' levels</p></td>
</tr>
<tr class="even">
<td><p>'<strong>'<a href="datatype-string.md">string</a></strong></p></td>
<td><p><strong>To String</strong></p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Raid](../top-level-objects/tlo-raid.md)
-   [DataType:raidmember](datatype-raidmember.md)


