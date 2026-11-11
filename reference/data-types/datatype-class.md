---
tags:
    - datatype
---
# `class`

<!--dt-desc-start-->
Data about a particular character class
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | bool CanCast
Can cast spells, including Bard
///

/// member | bool ClericType
True if class is a Cleric or Paladin
///

/// member | bool DruidType
True if class is a Druid or Ranger
///

/// member | bool HealerType
True if class is a Healer (Cleric, Druid or Shaman)
///

/// member | int ID
The class numeric ID
///

/// member | bool MercType
True if class is Mercenary
///

/// member | string Name
The full name of the class. Ex: "Ranger"
///

/// member | bool NecromancerType
True if class is a Necromancer or Shadow Knight
///

/// member | bool PetClass
True if class is a pet class (Shaman, Necromancer, Mage or Beastlord)
///

/// member | bool PureCaster
True if class is a pure caster (Cleric, Druid, Shaman, Necromancer, Wizard, Mage or Enchanter)
///

/// member | bool ShamanType
True if class is Shaman or Beastlord
///

/// member | string ShortName
The short name (three letter code) of the class. Ex: `RNG` for Ranger
///

### [string][string] `To String`

:   Same as **Name**
<!--dt-members-end-->

<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
