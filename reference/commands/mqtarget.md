---
tags:
    - ref
    - slash
---
# /mqtarget

## Syntax

**/mqtarget** _**option**_

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
/mqtarget npc radius 100 zradius 50 alert 1
/mqtarget pc range 30 35 lfg
/mqtarget npc los radius 220
/mqtarget ${Spawn[alert 1]}
/mqtarget ${Spawn[noalert 1]}
```
