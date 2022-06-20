---
tags:
    - ref
    - slash
---
# /target

## Syntax

**/target** _**option**_

## Description

Targets whatever is matched by one or more of the following _options_:

|  |  |
| :--- | :--- |
| **clear** | Clears your current target |
| **mycorpse** | Your own corpse (nearest) |
| **myself** | Target yourself |
| _Anything Else_ | Anything else is considered a [Spawn Search](../../reference/general/spawn-search.md) |

## Examples

```text
/target npc radius 100 zradius 50 alert 1
/target pc range 30 35 lfg
/target npc los radius 220
/target ${Spawn[alert 1]}
/target ${Spawn[noalert 1]}
```
