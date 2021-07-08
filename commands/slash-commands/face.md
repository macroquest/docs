# /face

## Syntax

**/face \[predict\] \[fast\] \[nolook\] \[away\] \[ alert \# \| loc y,x,z \| heading angle \| item \| door \| id \# \|** _**name**_ **\]**

## Description

Turns your character to face a target, door, item or location at comparable speeds to pressing the left, right, lookup, and lookdown keys.

Some of the options are listed below.

| Option | Description |
| :--- | :--- |
| **predict** | Returns an estimated distance/location, unless the target is stationary |
| **fast** | Faces you instantly |
| **nolook** | Faces your target without changing your vertical viewing angle \(looking up/date at the target\) |
| **away** | Turn you in the opposite direction of your target |
| _name_ | Considered a [Spawn Search](../../general-information/spawn-search.md) |

{% hint style="info" %}
Using **/face** without a target will do nothing.
{% endhint %}

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
| /face loc y,x,z | Faces the given loc \(**note**: no spaces in 'y,x,z' portion\) |

## See Also

* [/itemtarget](itemtarget.md)
* [/doortarget](doortarget.md)
* [Spawn Search](../../general-information/spawn-search.md)

