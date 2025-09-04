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
<!--dt-members-end-->

<!--dt-linkrefs-start-->
[bool]: datatype-bool.md
[int]: datatype-int.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->
