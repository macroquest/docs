## Description

Used to find information about a particular zone.

## Forms

|                                                              |                                                  |
|--------------------------------------------------------------|--------------------------------------------------|
| *[currentzone](../data-types/datatype-currentzone.md)* **Zone**    | Retrieves the current zone information           |
| *[zone](../data-types/datatype-zone.md)* **Zone\[**#**\]**         | Retrieves information about a zone by zone ID    |
| *[zone](../data-types/datatype-zone.md)* **Zone\[**shortname**\]** | Retrieves information about a zone by short name |

## Access to Types

-   *[currentzone](../data-types/datatype-currentzone.md)* **currentzone**
-   *[zone](../data-types/datatype-zone.md)* **zone**

## Examples

`  /echo ${Zone.Type}`

Returns an integer representing the zone you are currently in.

`  /echo ${Zone.Indoor}`

Returns TRUE if you're indoors, FALSE if not.

`  /echo ${Zone[zonename].ID}`

Returns the ID of *zonename*, even if you aren't in the zone.

`  /echo ${Zone[zoneid].ShortName}`

Returns the short name of the zone with ID *zoneid*.

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [currentzone](../data-types/datatype-currentzone.md)
-   [zone](../data-types/datatype-zone.md)


