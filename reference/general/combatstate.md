
# CombatState

**Me.CombatState**

A new Out Of Combat (OOC\) resting feature was introduced with The Serpent's Spine expansion, allowing accelerated mana and hit point regeneration. Once this state is Active and you are sitting \(or on a mount), it takes a maximum 3 mins to go from 0 to full health/mana. The waiting period to reach an active/resting state varies on the zone or mobs you are fighting. The default timer is 30 seconds but this can reach upwards of 5 mins or more in high end raid zones.

A new [DataType:character](../data-types/datatype-character.md) member was added, CombatState.

## Possible Return Values

```text
COMBAT    You are currently in a combat state and can not rest yet.
DEBUFFED  You can't rest now. You need to be cleansed before the cooldown will start
COOLDOWN  You are cooling down. OOC regen is ready when you are done cooling down
ACTIVE    You can rest now. You can use the OOC regen if you want
RESTING   You ARE resting now. the OOC regen is active
NULL      Your UI does not have the OOC regen XML additions and state can not be determined
```

NULL only occurs if your player UI file does not have the required additions to track OCC. You should replace this portion with an updated version.

## Examples

```text
/if ${Me.CombatState.Equal[ACTIVE]} /echo I can now sit and regen fast
/if ${Me.CombatState.Equal[DEBUFFED]} /echo I need cures before I can rest
```

