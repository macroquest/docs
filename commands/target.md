## Syntax

**<span style="color:red">/target</span> *option***

## Description

Targets whatever is matched by one or more of the following *options*:

|                     |                                                                       |
|---------------------|-----------------------------------------------------------------------|
| **clear**           | Clears your current target                                            |
| **mycorpse**        | Your own corpse (nearest)                                             |
| **myself**          | Target yourself                                                       |
| ***Anything Else*** | Anything else is considered a [Spawn Search](../general-information/spawn-search.md) |

## Examples

    /target npc radius 100 zradius 50 alert 1
    /target pc range 30 35 lfg
    /target npc los radius 220
    /target ${Spawn[alert 1]}
    /target ${Spawn[noalert 1]}

## See Also

-   [TLO:Target](../top-level-objects/tlo-target.md)
-   [Slash Commands](slash-commands.md)
-   [Spawn Search](../general-information/spawn-search.md)
-   [/doortarget](doortarget.md)
-   [/itemtarget](itemtarget.md)
-   [/alert](alert.md)
-   [DataType:spawn](../data-types/datatype-spawn.md)
-   DataType:targettype


