---
tags:
    - command
---
# /filter

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/filter [macros {all|enhanced|none}] [skills {all|increase|none}] [target|money|food|encumber|debug {on|off}] [name {add|remove} <text> ] [zrange <#> ] [mq {on|off}]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Extends the EverQuest command to allow filtering many types of messages, such as the annoying "You are out of food and drink" alert. 

| **Command** | Description |
| :--- | :--- |
| **/filter** | /filter on its own will open the chat filter section of the EQ options window |
| **macros** _all/enhanced/none_ | **all** will filter all macro messages, except for macro end  **enhanced** is currently not in use, and does nothing  **none** turns the filtering off |
| **skills** _all/increase/none_ | **all** will filter all skill related messages  **increase** filters out skill increases only  **None** turns the filtering off |
| **target / money / food / encumber / debug** _on/off_ | **target** filter out target lost messages  **money** filter loot messages about money  **food** filters hungry and thirsty messages (food/drink alerts)  **encumber** filters out encumbrance messages  **debug on/off** Turns on debug filters or not |
| **zrange** _#_ | Sets vertical detection range for [/itemtarget](itemtarget.md) ground items
| **mq** _on/off_ | Filters out any plugin or macro messages, so if you want a quiet mq chat window this is for you |
| **name** _add/remove_ _text_ | Sets up custom filters, see examples below. |
|  |  |

### Notes

Filters added through `/filter` are excluded from EverQuest's logging (`/log`) system.

**Important:** Overly broad filters may capture unintended messages. For example, filtering out `A rat` will also hide messages containing that exact phrase, such as /con messages.
<!--cmd-desc-end-->
## Examples

```text
/filter name add Joe         This will add a filter that ignores all lines that start with "Joe"
/filter name add *Joe        This will add a filter that ignores all lines that have "Joe" anywhere in them
```