---
tags:
    - datatype
---
# `ground`

<!--dt-desc-start-->
Represents a ground item.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | float DisplayName
Displays name of the grounspawn
///

/// member | int Distance
Distance from player to ground item
///

/// member | int Distance3D
Distance from player to ground item
///

/// member | heading Heading
Ground item is facing this heading
///

/// member | heading HeadingTo
Direction player must move to meet this ground item
///

/// member | int ID
Ground item ID (not the same as item ID, this is like spawn ID)
///

/// member | bool LineOfSight
Returns TRUE if ground spawn is in line of sight
///

/// member | string Name
Name
///

/// member | int SubID
???
///

/// member | int ZoneID
???
///

/// member | float X
X coordinate
///

/// member | float Y
Y coordinate
///

/// member | float Z
Z coordinate
///

/// member | float W
X coordinate (Westward-positive)
///

/// member | float N
Y coordinate (Northward-positive)
///

/// member | float U
Z coordinate (Upward-positive)
///

/// member | ground First
First spawn
///

/// member | ground Last
Last spawn
///

/// member | ground Next
Next spawn
///

/// member | ground Prev
Prev spawn
///

### [string][string] `To String`

:   Same as ID
<!--dt-members-end-->

## Methods

| Name | Action |
| :--- | :--- |
| **DoFace** | Will cause the toon to face the called for spawn if it exists |
| **DoTarget** | Will cause the toon to target the called for spawn if it exists |
| **Grab** | Picks up the ground spawn |
| **Reset** | Clears the currently selected ground spawn |

## Examples


Extended the Ground TLO to accept searches

```
/echo The closest ${Ground[brew].DisplayName} is ${Ground[brew].Distance3D} away from you.
```

Output:
```
The closest Brew Barrel is 26.4 away from you.
```

Note that both of the search functions are case insensitive and are sorted by distance closest to you. The only acceptable parameter in the search filter is by name or partial name.

```
/echo ${Ground[egg].Doface.Distance3D}
```

Will face the closest item on the ground which has the word "egg" in it. and then echo the distance to it in the mq2 window. well if it finds an item with the word "egg" in it on the ground that is, otherwise it will just echo NULL .DoFace does NOT target the ground item, it just faces it.

```
/if (${Ground[egg].DoTarget.ID}) /echo we just targeted a ${Ground[egg]}
```

Will target the closest item on the ground which has the word "egg" in it. and then echo the distance to it in the mq2 window.

```
/if (${Ground[1].Doface.Distance3D}) /echo we just targeted a ${Ground[1].DisplayName}
```

Will face the closest item on the ground. and then echo the distance to it in the mq2 window. well if it finds an groundspawn, otherwise it will just echo NULL .DoFace does NOT target the ground item, it just faces it.
<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[float]: datatype-float.md
[ground]: datatype-ground.md
[heading]: datatype-heading.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
