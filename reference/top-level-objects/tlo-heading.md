---
tags:
    - tlo
---
# `Heading`

Object that refers to the directional heading to of a location or direction.

## Forms

|  |  |
| :--- | :--- |
| [heading][heading] **Heading[**\#**]** | Creates a heading object using degrees (clockwise) |
| [heading][heading] **Heading[**y,x**]** | Creates a heading object using the heading to this y,x location |
| [heading][heading] **Heading[**N,W**]** | Same as above, just an alternate method |

## Examples

`/echo ${Heading[15].ShortName}`

Echos the shortname of the heading of 15 degrees.

`/echo ${Heading[-342,700].ShortName}`

Echos the shortname heading to the location -342,700

[heading]: ../data-types/datatype-heading.md