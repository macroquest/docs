---
tags:
    - ref
    - datatype
---
[TLO List](../top-level-objects/tlo-list.md) | [DataType List](../data-types/datatype-list.md)
# `switch`

Data related to switches (levers, buttons, etc) in the zone

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_float_](datatype-float.md) | **D** | D coordinate (Upward-positive) |
| [_heading_](datatype-heading.md) | **DefaultHeading** | Heading of "closed" switch |
| [_float_](datatype-float.md) | **DefaultN** | Y coordinate of "closed" switch (Northward-positive) |
| [_float_](datatype-float.md) | **DefaultU** | Z coordinate of "closed" switch (Upward-positive) |
| [_float_](datatype-float.md) | **DefaultW** | X coordinate of "closed" switch (Westward-positive) |
| [_float_](datatype-float.md) | **DefaultX** | X coordinate of "closed" switch |
| [_float_](datatype-float.md) | **DefaultY** | Y coordinate of "closed" switch |
| [_float_](datatype-float.md) | **DefaultZ** | Z coordinate of "closed" switch |
| [_float_](datatype-float.md) | **Distance** | Distance from player to switch in (x,y) |
| [_heading_](datatype-heading.md) | **Heading** | Switch is facing this heading |
| [_heading_](datatype-heading.md) | **HeadingTo** | Direction player must move to meet this switch |
| [_int_](datatype-int.md) | **ID** | Switch ID |
| [_bool_](datatype-bool.md) | **LineOfSight** | Returns TRUE if the switch is in LoS |
| [_float_](datatype-float.md) | **N** | Y coordinate (Northward-positive) |
| [_string_](datatype-string.md) | **Name** | Name |
| [_bool_](datatype-bool.md) | **Open** | True if the switch is in the "open" state (State == 1) |
| [_int_](datatype-int.md) | **State** | The "state" of the switch. |
| [_float_](datatype-float.md) | **W** | X coordinate (Westward-positive) |
| [_float_](datatype-float.md) | **X** | X coordinate |
| [_float_](datatype-float.md) | **Y** | Y coordinate |
| [_float_](datatype-float.md) | **Z** | Z coordinate |
| [_string_](datatype-string.md) | **ToString** | Same as **ID** |

