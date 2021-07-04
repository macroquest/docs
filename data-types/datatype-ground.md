## Description

Contains all data related to a ground spawn

## Members

|                                            |                 |                                                                 |
|--------------------------------------------|-----------------|-----------------------------------------------------------------|
| **Type**                                   | **Member**      | **Description**                                                 |
| *[int](datatype-int.md)*           | **ID**          | Ground item ID (not the same as item ID, this is like spawn ID) |
| *[int](datatype-int.md)*           | **Distance**    | Distance from player to ground item                             |
| *[float](datatype-float.md)*       | **X**           | X coordinate                                                    |
| *[float](datatype-float.md)*       | **Y**           | Y coordinate                                                    |
| *[float](datatype-float.md)*       | **Z**           | Z coordinate                                                    |
| *[heading](datatype-heading.md)*   | **Heading**     | Ground item is facing this heading                              |
| *[string](datatype-string.md)*     | **Name**        | Name                                                            |
| *[heading](datatype-heading.md)*   | **HeadingTo**   | Direction player must move to meet this ground item             |
| *[bool](datatype-bool.md)*         | **LineOfSight** | Returns TRUE if ground spawn is in line of sight                |
| *[int](datatype-int.md)*           | **Address**     | ???                                                             |
| *[float](datatype-float.md)*       | **DisplayName** | Displays name of the grounspawn                                 |
| *[int](datatype-int.md)*           | **Distance3D**  | Distance from player to ground item                             |
| *[int](datatype-int.md)*           | **SubID**       | ???                                                             |
| *[int](datatype-int.md)*           | **ZoneID**      | ???                                                             |
| *[action](datatype-action.md)*     | **First**       | First spawn                                                     |
| *[action](datatype-action.md)*     | **Last**        | Last spawn                                                      |
| *[action](datatype-action.md)*     | **Next**        | Next spawn                                                      |
| *[action](datatype-action.md)*     | **Prev**        | Prev spawn                                                      |
| *[action](datatype-action.md)*     | **DoFace**      | Will cause the toon to face the called for spawn if it exists   |
| *[action](datatype-action.md)*     | **DoTarget**    | Will cause the toon to target the called for spawn if it exists |
| *[action](datatype-action.md)*     | **Grab**        | Picks up the ground spawn                                       |
| *[float](datatype-float.md)*       | **W**           | X coordinate (Westward-positive)                                |
| *[float](datatype-float.md)*       | **N**           | Y coordinate (Northward-positive)                               |
| *[float](datatype-float.md)*       | **U**           | Z coordinate (Upward-positive)                                  |
| '**'[string](datatype-string.md)** | **To String**   | Same as ID                                                      |

## Examples

Extended the Ground TLO to accept searches

`/echo The closest ${Ground[brew].DisplayName} is ${Ground[brew].Distance3D} away from you.`

output: The closest Brew Barrel is 26.4 away from you.

Note that both of the search functions are case insensitive and are sorted by distance closest to you. The only
acceptable parameter in the search filter is by name or partial name.

/echo ${Ground\[egg\].Doface.Distance3D}) Will face the closest item on the ground which has the word "egg" in it. and
then echo the distance to it in the mq2 window. well if it finds an item with the word "egg" in it on the ground that
is, otherwise it will just echo NULL .DoFace does NOT target the ground item, it just faces it.

`/if (${Ground[egg].DoTarget.ID}) /echo we just targeted a ${Ground[egg]}`

Will target the closest item on the ground which has the word "egg" in it. and then echo the distance to it in the mq2
window.

`/if (${Ground[1].Doface.Distance3D}) /echo we just targeted a ${Ground[1].DisplayName}`

Will face the closest item on the ground. and then echo the distance to it in the mq2 window. well if it finds an
groundspawn, otherwise it will just echo NULL .DoFace does NOT target the ground item, it just faces it.

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Ground](../top-level-objects/tlo-ground.md)
-   [TLO:ItemTarget](../top-level-objects/tlo-itemtarget.md)
-   [TLO:GroundItemCount](../top-level-objects/tlo-grounditemcount.md)


