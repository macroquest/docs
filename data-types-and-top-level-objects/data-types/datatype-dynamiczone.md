# DataType:dynamiczone

Data for the current dynamic zone instance

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
      <td style="text-align:left"><a href="datatype-dzmember.md"><em>dzmember</em></a>
      </td>
      <td style="text-align:left"><b>Leader</b>
      </td>
      <td style="text-align:left">The leader of the dynamic zone</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>LeaderFlagged</b>
      </td>
      <td style="text-align:left">
        <p>Returns true if the dzleader can successfully enter the dz (this also
          means the dz is actually Loaded.)</p>
        <p></p>
        <p><b>Example: </b><code>${DynamicZone.LeaderFlagged}</code>
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MaxMembers</b>
      </td>
      <td style="text-align:left">Maximum number of characters that can enter this dynamic zone</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-dzmember.md"><em>dzmember</em></a>
      </td>
      <td style="text-align:left"><b>Member[</b>#<b>|</b>name<b>]</b>
      </td>
      <td style="text-align:left">The dynamic zone member <em>#</em> or <em>name</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Members</b>
      </td>
      <td style="text-align:left">Current number of characters in the dynamic zone</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Name</b>
        </td>
        <td style="text-align:left">The full name of the dynamic zone</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>MaxTimers</b>
      </td>
      <td style="text-align:left">The number of timers present in <b>Timers</b>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-dztimer.md"><em>dztimer</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>Timer[#|Name]</b>
        </td>
        <td style="text-align:left">
          <p>Access the list of current lockout timers. This is either an index from
            1 to <b>MaxTimers</b>, or a Expedition|Event combination. Event is optional,
            but if multiple Expeditions match, the timer with the earliest lockout
            expiration will be returned.</p>
          <p></p>
          <p><b>Example:<br /></b>/echo ${DynamicZone.Timer[Nagafen&apos;s Lair|Lord
            Nagafen].Timer.TimeDHM}</p>
          <p>Output: 2:10:24</p>
        </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>To String</b>
        </td>
        <td style="text-align:left">Same as <b>Name</b>
        </td>
    </tr>
  </tbody>
</table>

### Changelog

* July 9th, 2021: Added MaxTimers, Timer

