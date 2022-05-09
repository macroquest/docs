# DataType:raid

Contains data on the current raid

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
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>AverageLevel</b>
      </td>
      <td style="text-align:left">Average level of raid members (more accurate than in the window)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Invited</b>
      </td>
      <td style="text-align:left">Have I been invited to the raid?</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-raidmember.md"><em>raidmember</em></a>
      </td>
      <td style="text-align:left"><b>Leader</b>
      </td>
      <td style="text-align:left">Raid leader</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Locked</b>
      </td>
      <td style="text-align:left">Returns TRUE if the raid is locked</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Looter[</b>#<b>]</b>
        </td>
        <td style="text-align:left">Specified looter name by number</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Looters</b>
      </td>
      <td style="text-align:left">Number of specified looters</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>LootType</b>
      </td>
      <td style="text-align:left">
        <p>Loot type number:</p>
        <ul>
          <li>1 = Leader</li>
          <li>2 = Leader &amp; GroupLeader</li>
          <li>3 = Leader &amp; Specified</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-raidmember.md"><em>raidmember</em></a>
      </td>
      <td style="text-align:left"><b>MainAssist</b>
      </td>
      <td style="text-align:left">Raid main assist</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-raidmember.md"><em>raidmember</em></a>
      </td>
      <td style="text-align:left"><b>MasterLooter</b>
      </td>
      <td style="text-align:left">Raid Master Looter</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-raidmember.md"><em>raidmember</em></a>
      </td>
      <td style="text-align:left"><b>Member[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Raid member by number</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-raidmember.md"><em>raidmember</em></a>
      </td>
      <td style="text-align:left"><b>Member[</b>name<b>]</b>
      </td>
      <td style="text-align:left">Raid member by <em>name</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Members</b>
      </td>
      <td style="text-align:left">Total number of raid members</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-raidmember.md"><em>raidmember</em></a>
      </td>
      <td style="text-align:left"><b>Target</b>
      </td>
      <td style="text-align:left">Raid target (clicked in raid window)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>TotalLevels</b>
      </td>
      <td style="text-align:left">Sum of all raid members&apos; levels</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>To String</b>
        </td>
        <td style="text-align:left">None</td>
    </tr>
  </tbody>
</table>

