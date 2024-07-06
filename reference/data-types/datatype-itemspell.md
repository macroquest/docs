---
tags:
    - datatype
---
# `itemspell` Type

Represents a spell effect on an item.

## Members

### {{ renderMember(type='int', name='CastTime') }}

:   Spell cast time.

### {{ renderMember(type='int', name='EffectiveCasterLevel') }}

:   Effective level that is used to cast the spell.

### {{ renderMember(type='int', name='EffectType') }}

:   The type of item spell effect.

### {{ renderMember(type='int', name='MaxCharges') }}

:   The maximum number of charges supported by this spell.

### {{ renderMember(type='int', name='OtherID') }}

:   ???

### {{ renderMember(type='string', name='OtherName') }}

:   Synonym of _OverrideName_

### {{ renderMember(type='string', name='OverrideDescription') }}

: Overrides the normal spell description string, if set.

### {{ renderMember(type='string', name='OverrideName') }}

: Overrides the normal spell name string, if set.

### {{ renderMember(type='int', name='ProcRate') }}

:   Combat effect proc rate.

### {{ renderMember(type='int', name='RecastType') }}

:   Recast type of the spell.

### {{ renderMember(type='int', name='RequiredLevel') }}

:   Level required for the spell to be usable.

### {{ renderMember(type='spell', name='Spell') }}

:   The spell.

### {{ renderMember(type='int', name='SpellID') }}

:   ID of the Spell.

### {{ renderMember(type='int', name='TimerID') }}

:   Timer ID of the spell.


[int]: ../data-types/datatype-int.md
[spell]: ../data-types/datatype-spell.md
[string]: datatype-string.md
