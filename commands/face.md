## Syntax

**<span style="color:red">/face</span> \[<span style="color:blue">predict</span>\]
\[<span style="color:blue">fast</span>\] \[<span style="color:blue">nolook</span>\]
\[<span style="color:blue">away</span>\] \[ <span style="color:blue">alert</span> # \|
<span style="color:blue">loc</span> y,x,z \| <span style="color:blue">heading</span> angle \|
<span style="color:blue">item</span> \| <span style="color:blue">door</span> \| <span style="color:blue">id</span> # \|
*name* \]**

## Description

Turns your character to face a target, door, item or location at comparable speeds to pressing the left, right, lookup,
and lookdown keys.  
Some of the options are listed below.  
{\| border="1" cellpadding="2" cellspacing="0" \|style="background:#000000;color:#ffffff;"\|**Option**
\|style="background:#000000;color:#ffffff;"\|**Description** \|- \|**predict** \|Returns an estimated distance/location,
unless the target is stationary \|- \|**fast** \|Faces you instantly \|- \|**nolook** \|Faces your target without
changing your vertical viewing angle (looking up/down at the target) \|- \|**away** \|Turns you the opposite direction
of your target \|- \|*name* \|Considered a [Spawn Search](../general-information/spawn-search.md) \|}  
\*Using */face* with no options will face your target. It will do nothing if you have no target.  
== Examples ==

|                    |                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------|
| **Example**        | **Description**                                                                                |
| /face              | Turns you to face and look at your selected target                                             |
| /face nolook       | Faces your target without changing your vertical view angle                                    |
| /face fast         | Immediately turns your character to face and look at your target                               |
| /face fast predict | Immediately turns your character to face and look at your target's estimated position          |
| /face fast nolook  | Immediately turns your character to face your target without changing your vertical view angle |
| /face item         | Faces and looks at the item following an /itemtarget                                           |
| /face fast item    | Immediately faces and looks at the item following an /itemtarget                               |
| /face loc y,x,z    | Faces the given loc (**note**: no spaces in 'y,x,z' portion)                                   |

  
== See Also ==

-   [/itemtarget](itemtarget.md)
-   [/doortarget](doortarget.md)
-   [Spawn Search](../general-information/spawn-search.md)

[Return to Slash Commands](slash-commands.md)


