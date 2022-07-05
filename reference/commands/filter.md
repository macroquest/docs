---
tags:
    - command
---
# /filter

## Syntax

**/filter [ macros all\|enhanced\|none \] \[ skills all\|increase\|none \] \[ target \| money \| food \| encumber \| debug** _**on**_**\|**_**off**_ **\] \[ name \[ add\|remove** _**text**_ **\] \] \[ zrange \# \] \[ mq** _**on**_**\|**_**off**_ **]** '''

## Description

* **Filtering of names is now improved!**

Will filter out some common messages that can be annoying to see

| **Command** | Description |
| :--- | :--- |
| **/filter** | /filter on its own will open the chat filter section of the EQ options window |
| **/filter macros** _all enhanced none_ | **all** will filter all macro messages, except for macro end  **enhanced** is currently not in use, and does nothing  **none** turns the filtering off |
| **/filter Skills** _all/increase/none_ | **all** will filter all skill related messages  **increase** filters out skill increases only  **None** turns the filtering off |
| **/filter** _target / money / food / encumber / debug on/off_ | **target** filter out target lost messages  **money** filter loot messages about money  **food** filters hungry messages  **encumber** filters out encumberance messages  **debug on/off** Turns on debug filters or not |
| **/filter** _zrange \#_ | Related to the zrange used when using /itemtarget, this could use futher exploring and testing. |
| **/filter** _mq on/off_ | Filters out any plugin or macro messages, so if you want a quiet mq2 chat window this is for you |
| **/filter** _name_ | Sets up custom filters, see examples below. |
|  |  |

Filters added through this, among others the custom name filters, will not appear in the EQ log when you use the EQ command /log on\|off

Also be aware the more lose you make your filter the more messages will be filtered for example if you filter on A rat, when conning A rat, the con message will also be filtered.

## Examples

```text
/filter name add Joe         This will add a filter that ignores all lines that start with "Joe"
/filter name add *Joe        This will add a filter that ignores all lines that have "Joe" anywhere in them
```

