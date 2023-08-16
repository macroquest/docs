---
tags:
    - command
---
# /doortarget

## Syntax

**/doortarget [id \# \| filter]**

## Description

"Targets" a door or Switch for further manipulation (eg. /face door). The targeting of doors, switches will not show up in the target window. This is because the EQ servers started monitoring for targeting that is not possible through the normal client, however current MQ will show indication of your /doortarget

## Examples

|  |  |
| :--- | :--- |
| **Example** | **Description** |
| /doortarget | Will target closest door/switch |
| /doortarget id 27 | If you are in PoK will target the portal stone to Rathemtn |
| /doortarget target | Will return the targeted switch |
| /doortarget nearest | Same as "/doortarget", returning the nearest switch |

## See Also

For scripts, targeting the door is usually unecessary.  Instead look at [_switch_](../data-types/datatype-switch.md) TLO for discovery / triggering.
