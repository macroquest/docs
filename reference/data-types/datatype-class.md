---
tags:
    - datatype
---
# `class`

Data about a particular character class

## Members

### {{ renderMember(type='bool', name='CanCast') }} 

:   Can cast spells, including Bard

### {{ renderMember(type='bool', name='ClericType') }} 

:   True if class is a Cleric or Paladin

### {{ renderMember(type='bool', name='DruidType') }} 

:   True if class is a Druid or Ranger

### {{ renderMember(type='bool', name='HealerType') }} 

:   True if class is a Healer (Cleric, Druid or Shaman)

### {{ renderMember(type='int', name='ID') }} 

:   The class numeric ID

### {{ renderMember(type='bool', name='MercType') }} 

:   True if class is Mercenary

### {{ renderMember(type='string', name='Name') }} 

:   The full name of the class. Ex: "Ranger"

### {{ renderMember(type='bool', name='NecromancerType') }} 

:   True if class is a Necromancer or Shadow Knight

### {{ renderMember(type='bool', name='PetClass') }} 

:   True if class is a pet class (Shaman, Necromancer, Mage or Beastlord)

### {{ renderMember(type='bool', name='PureCaster') }} 

:   True if class is a pure caster (Cleric, Druid, Shaman, Necromancer, Wizard, Mage or Enchanter)

### {{ renderMember(type='bool', name='ShamanType') }} 

:   True if class is Shaman or Beastlord

### {{ renderMember(type='string', name='ShortName') }} 

:   The short name (three letter code) of the class. Ex: `RNG` for Ranger

### [string][string] `To String`

:   Same as **Name**


### Name -> ShortName list:
| **Name** | **ShortName** |
| :--- | :--- |
| Bard | BRD |
| Beastlord | BST |
| Berserker | BER |
| Cleric | CLR |
| Druid | DRU |
| Enchanter | ENC |
| Magician | MAG |
| Monk | MNK |
| Necromancer | NEC |
| Paladin | PAL |
| Ranger | RNG |
| Shadow Knight | SHD |
| Shaman | SHM |
| Warrior | WAR |
| Wizard | WIZ |
| Mercenary | MER |

[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
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
