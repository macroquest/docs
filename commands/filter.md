## Syntax

**<span style="color:red">/filter</span> \[ <span style="color:blue">macros
all</span>\|<span style="color:blue">enhanced</span>\|<span style="color:blue">none</span> \] \[
<span style="color:blue">skills
all</span>\|<span style="color:blue">increase</span>\|<span style="color:blue">none</span> \] \[
<span style="color:blue">target</span> \| <span style="color:blue">money</span> \| <span style="color:blue">food</span>
\| <span style="color:blue">encumber</span> \| <span style="color:blue">debug</span> *on*\|*off* \] \[
<span style="color:blue">name</span> \[ <span style="color:blue">add</span>\|<span style="color:blue">remove</span>
*text* \] \] \[ <span style="color:blue">zrange</span> # \] \[ <span style="color:blue">mq</span> *on*\|*off* \]** '''

## Description

-   **Filtering of names is now improved!**

Will filter out some common messages that can be annoying to see

<table>
<tbody>
<tr class="odd">
<td><p><strong>/filter</strong></p></td>
<td><p>/filter on its own will open the chat filter section of the EQ options window</p></td>
</tr>
<tr class="even">
<td><p><strong>/filter macros</strong> <em>all enhanced none</em></p></td>
<td><p><strong>all</strong> will filter all macro messages, except for macro end<br />
<strong>enhanced</strong> is currently not in use, and does nothing<br />
<strong>none</strong> turns the filtering off</p></td>
</tr>
<tr class="odd">
<td><p><strong>/filter Skills</strong> <em>all/increase/none</em></p></td>
<td><p><strong>all</strong> will filter all skill related messages<br />
<strong>increase</strong> filters out skill increases only<br />
<strong>None</strong> turns the filtering off</p></td>
</tr>
<tr class="even">
<td><p><strong>/filter</strong> <em>target / money / food / encumber / debug on/off</em></p></td>
<td><p><strong>target</strong> filter out target lost messages<br />
<strong>money</strong> filter loot messages about money<br />
<strong>food</strong> filters hungry messages<br />
<strong>encumber</strong> filters out encumberance messages<br />
<strong>debug on/off</strong> Turns on debug filters or not</p></td>
</tr>
<tr class="odd">
<td><p><strong>/filter</strong> <em>zrange #</em></p></td>
<td><p>Related to the zrange used when using /itemtarget, this could use futher exploring and testing.</p></td>
</tr>
<tr class="even">
<td><p><strong>/filter</strong> <em>mq on/off</em></p></td>
<td><p>Filters out any plugin or macro messages, so if you want a quiet mq2 chat window this is for you</p></td>
</tr>
<tr class="odd">
<td><p><strong>/filter</strong> <em>name</em></p></td>
<td><p>Sets up custom filters, see examples below.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
</tbody>
</table>

Filters added through this, among others the custom name filters, will not appear in the EQ log when you use the EQ
command /log on\|off

Also be aware the more lose you make your filter the more messages will be filtered for example if you filter on A rat,
when conning A rat, the con message will also be filtered.

## Examples

    /filter name add Joe         This will add a filter that ignores all lines that start with "Joe"
    /filter name add *Joe        This will add a filter that ignores all lines that have "Joe" anywhere in them

[Return to Slash Commands](slash-commands.md)


