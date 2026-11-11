---
tags:
    - datatype
---
# `itemspell` Type

<!--dt-desc-start-->
Represents a spell effect on an item.
<!--dt-desc-end-->

## Members
<!--dt-members-start-->
/// member | int CastTime
Spell cast time.
///

/// member | int EffectiveCasterLevel
Effective level that is used to cast the spell.
///

/// member | int EffectType
The type of item spell effect.
///

/// member | int MaxCharges
The maximum number of charges supported by this spell.
///

/// member | int OtherID
???
///

/// member | string OtherName
Synonym of _OverrideName_
///

/// member | string OverrideDescription
Overrides the normal spell description string, if set.
///

/// member | string OverrideName
Overrides the normal spell name string, if set.
///

/// member | int ProcRate
Combat effect proc rate.
///

/// member | int RecastType
Recast type of the spell.
///

/// member | int RequiredLevel
Level required for the spell to be usable.
///

/// member | spell Spell
The spell.
///

/// member | int SpellID
ID of the Spell.
///

/// member | int TimerID
Timer ID of the spell.
///
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[int]: ../data-types/datatype-int.md
[spell]: ../data-types/datatype-spell.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
