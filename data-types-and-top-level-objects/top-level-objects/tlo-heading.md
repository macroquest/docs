# TLO:Heading

## Description

Object that refers to the directional heading to of a location or direction.

## Forms

|  |  |
| :--- | :--- |
| [_heading_](../data-types/datatype-heading.md) **Heading\[**\#**\]** | Creates a heading object using degrees \(clockwise\) |
| [_heading_](../data-types/datatype-heading.md) **Heading\[**y,x**\]** | Creates a heading object using the heading to this y,x location |
| [_heading_](../data-types/datatype-heading.md) **Heading\[**N,W**\]** | Same as above, just an alternate method |

## Access to Types

* [_heading_](../data-types/datatype-heading.md) **heading**

## Examples

`/echo ${Heading[15].ShortName}`

Echos the shortname of the heading of 15 degrees.

`/echo ${Heading[-342,700].ShortName}`

Echos the shortname heading to the location -342,700

## See Also

* [Top-Level Objects](./)

