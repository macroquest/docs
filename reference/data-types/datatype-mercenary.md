---
tags:
    - datatype
---
# `mercenary`

This is the type used for mercenaries.

## Members

This type inherits members from [_spawn_](datatype-spawn.md).

### [int][int] `AAPoints`

:   AA Points spent on mercenary abilities

### [string][string] `Stance`

:   Current stance of the mercenary

### [string][string] `State`

:   Current state of the mercenary \(returns "DEAD","SUSPENDED","ACTIVE", or "UNKNOWN"

### [int][int] `StateID`

:   Current state ID of the mercenary as a number.

### [string][string] `Index`

:   Index

### [string][string] `To String`

:   Same as **Name**


## Examples

Check on if you have an active mercenary, mercenary is a cleric, and if it's stance is NOT reactive.... then change it TO reactive.

```text
/if (${Mercenary.State.Equal[ACTIVE]} && ${Mercenary.Class.Name.Equal[Cleric]} && ${Mercenary.Stance.NotEqual[REACTIVE]}) {
    /stance reactive
}
```

[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: ../data-types/datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
[zone]: datatype-zone.md
[fellowshipmember]: datatype-fellowshipmember.md
[class]: datatype-class.md
[heading]: datatype-heading.md
[ground]: datatype-ground.md
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[double]: datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
