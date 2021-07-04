# Target

## Syntax

**/target** _**option**_

## Description

Targets whatever is matched by one or more of the following _options_:

|  |  |
| :--- | :--- |
| **clear** | Clears your current target |
| **mycorpse** | Your own corpse \(nearest\) |
| **myself** | Target yourself |
| _**Anything Else**_ | Anything else is considered a [Spawn Search](../../general-information/spawn-search.md) |

## Examples

```text
/target npc radius 100 zradius 50 alert 1
/target pc range 30 35 lfg
/target npc los radius 220
/target ${Spawn[alert 1]}
/target ${Spawn[noalert 1]}
```

## See Also

* [TLO:Target](../../data-types-and-top-level-objects/top-level-objects/tlo-target.md)
* [Slash Commands](./)
* [Spawn Search](../../general-information/spawn-search.md)
* [/doortarget](doortarget.md)
* [/itemtarget](itemtarget.md)
* [/alert](alert.md)
* [DataType:spawn](../../data-types-and-top-level-objects/data-types/datatype-spawn.md)
* DataType:targettype

