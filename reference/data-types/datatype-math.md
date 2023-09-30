---
tags:
    - datatype
---
# `math`

This DataType performs various mathematical calculations. In the following members, _n_ is any formula that consists of valid [Operators](../../macros/operators.md).

## Members

### {{ renderMember(type='float', name='Abs', params='n') }} 

:   The absolute value of the result of _n_

### {{ renderMember(type='float', name='Acos', params='n') }} 

:   Arccosine of _n_ (in degrees)

### {{ renderMember(type='float', name='Asin', params='n') }} 

:   Arcsine of _n_ (in degrees)

### {{ renderMember(type='float', name='Atan', params='n') }} 

:   Arctangent of _n_ (in degrees)

### {{ renderMember(type='float', name='Calc', params='n') }} 

:   Performs a mathematical calculation _n_

### {{ renderMember(type='int', name='Clamp', params='n, min, max') }} 

:   Clamps the value _n_ such that _min _<= _n_ <= _max_

### {{ renderMember(type='float', name='Cos', params='n') }} 

:   Cosine of _n_ (in degrees)

### {{ renderMember(type='int', name='Dec', params='hex') }} 

:   Decimal value of a hexidecimal string

### {{ renderMember(type='float', name='Distance', params='y,x,z:y,x,z') }} 

:   <ul><li>Calculates the distance between two points on the map</li><li>1, 2, or 3 dimensions may be provided</li><li>Defaults to your character's current location</li></ul>

### {{ renderMember(type='string', name='Hex', params='n') }} 

:   Returns hexidecimal value of [_int_](datatype-int.md) _n_

### {{ renderMember(type='int', name='Not', params='n') }} 

:   Bitwise complement of _n_

### {{ renderMember(type='int', name='Rand', params='n') }} 

:   Random integer. Rand\[5] range 0 to 4. Rand\[100,200] range 100 to 199

### {{ renderMember(type='float', name='Sin', params='n') }} 

:   Sine of _n_ (in degrees)

### {{ renderMember(type='float', name='Sqrt', params='n') }} 

:   Square root of _n_

### {{ renderMember(type='float', name='Tan', params='n') }} 

:   Tangent of _n_ (in degrees)

### [string][string] `To String`

:   NULL

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
