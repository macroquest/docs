# TLO:Zone

## Description

Used to find information about a particular zone.

## Forms

|  |  |
| :--- | :--- |
| [_currentzone_](../data-types/datatype-currentzone.md) **Zone** | Retrieves the current zone information |
| [_zone_](../data-types/datatype-zone.md) **Zone[**\#**]** | Retrieves information about a zone by zone ID |
| [_zone_](../data-types/datatype-zone.md) **Zone[**shortname**]** | Retrieves information about a zone by short name |

## Access to Types

* [_currentzone_](../data-types/datatype-currentzone.md) **currentzone**
* [_zone_](../data-types/datatype-zone.md) **zone**

## Examples

`/echo ${Zone.Type}`

Returns an integer representing the zone you are currently in.

`/echo ${Zone.Indoor}`

Returns TRUE if you're indoors, FALSE if not.

`/echo ${Zone[zonename].ID}`

Returns the ID of _zonename_, even if you aren't in the zone.

`/echo ${Zone[zoneid].ShortName}`

Returns the short name of the zone with ID _zoneid_.
