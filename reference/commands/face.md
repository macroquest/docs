---
tags:
    - command
---
# /face

## Syntax
<!--cmd-syntax-start-->
```eqcommand
/face [predict] [fast] [nolook] [away] [ loc <y,x[,z]> | heading <angle> | item | door|switch | id <#> | <Spawn Search> ]
```
<!--cmd-syntax-end-->

## Description
<!--cmd-desc-start-->
Turns your character in the specified direction.
<!--cmd-desc-end-->
## Options

| Option | Description |
| :--- | :--- |
| **predict** | Returns an estimated distance/location, unless the target is stationary |
| **fast** | Faces you instantly |
| **nolook** | Faces your target without changing your vertical viewing angle (looking up/date at the target) |
| **away** | Turn you in the opposite direction of your target |
| **loc** _y,x[,z]_ | Face specific coordinates (y,x,z format, z optional) |
| **heading** _angle_ | Face specific compass direction (0-360 degrees, accepts decimal values and automatically wraps beyond 360°) |
| **item** | Face currently [/itemtarget](itemtarget.md)-ed ground item |
| **door** or **switch** | Face currently [/doortarget](doortarget.md)-ed door |
| **id** _#_ | Face specific spawn ID |
| _name_/**Spawn Search** | Face a target by its name, or any other [Spawn Search](../../reference/general/spawn-search.md) parameter|

## Examples

| **Example** | **Description** |
| :--- | :--- |
| /face | Turns you to face and look at your selected target |
| /face nolook | Faces your target without changing your vertical view angle |
| /face fast | Immediately turns your character to face and look at your target |
| /face fast predict | Immediately turns your character to face and look at your target's estimated position |
| /face fast nolook | Immediately turns your character to face your target without changing your vertical view angle |
| /face item | Faces and looks at the item following an /itemtarget |
| /face fast item | Immediately faces and looks at the item following an /itemtarget |
| /face loc 100,100,100 | Faces the given loc (**note**: no spaces in 'y,x,z' portion) |