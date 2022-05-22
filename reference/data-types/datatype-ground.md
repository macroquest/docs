---
tags:
    - datatype
---

# `ground`

Represents a ground item.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **ID** | Ground item ID (not the same as item ID, this is like spawn ID) |
| [_int_](datatype-int.md) | **Distance** | Distance from player to ground item |
| [_float_](datatype-float.md) | **X** | X coordinate |
| [_float_](datatype-float.md) | **Y** | Y coordinate |
| [_float_](datatype-float.md) | **Z** | Z coordinate |
| [_heading_](datatype-heading.md) | **Heading** | Ground item is facing this heading |
| [_string_](datatype-string.md) | **Name** | Name |
| [_heading_](datatype-heading.md) | **HeadingTo** | Direction player must move to meet this ground item |
| [_bool_](datatype-bool.md) | **LineOfSight** | Returns TRUE if ground spawn is in line of sight |
| [_int_](datatype-int.md) | **Address** | ??? |
| [_float_](datatype-float.md) | **DisplayName** | Displays name of the grounspawn |
| [_int_](datatype-int.md) | **Distance3D** | Distance from player to ground item |
| [_int_](datatype-int.md) | **SubID** | ??? |
| [_int_](datatype-int.md) | **ZoneID** | ??? |
| [_ground_](datatype-ground.md) | **First** | First spawn |
| [_ground_](datatype-ground.md) | **Last** | Last spawn |
| [_ground_](datatype-ground.md) | **Next** | Next spawn |
| [_ground_](datatype-ground.md) | **Prev** | Prev spawn |
| [_float_](datatype-float.md) | **W** | X coordinate (Westward-positive) |
| [_float_](datatype-float.md) | **N** | Y coordinate (Northward-positive) |
| [_float_](datatype-float.md) | **U** | Z coordinate (Upward-positive) |
| [_string_](datatype-string.md) | **To String** | Same as ID |

## Methods

| Name | Action |
| :--- | :--- |
| **DoFace** | Will cause the toon to face the called for spawn if it exists |
| **DoTarget** | Will cause the toon to target the called for spawn if it exists |
| **Grab** | Picks up the ground spawn |
| **Reset** | Clears the currently selected ground spawn |

## Examples

Extended the Ground TLO to accept searches

`/echo The closest ${Ground[brew].DisplayName} is ${Ground[brew].Distance3D} away from you.`

output: The closest Brew Barrel is 26.4 away from you.

Note that both of the search functions are case insensitive and are sorted by distance closest to you. The only acceptable parameter in the search filter is by name or partial name.

`/echo ${Ground[egg].Doface.Distance3D})` Will face the closest item on the ground which has the word "egg" in it. and then echo the distance to it in the mq2 window. well if it finds an item with the word "egg" in it on the ground that is, otherwise it will just echo NULL .DoFace does NOT target the ground item, it just faces it.

`/if (${Ground[egg].DoTarget.ID}) /echo we just targeted a ${Ground[egg]}`

Will target the closest item on the ground which has the word "egg" in it. and then echo the distance to it in the mq2 window.

`/if (${Ground[1].Doface.Distance3D}) /echo we just targeted a ${Ground[1].DisplayName}`

Will face the closest item on the ground. and then echo the distance to it in the mq2 window. well if it finds an groundspawn, otherwise it will just echo NULL .DoFace does NOT target the ground item, it just faces it.

