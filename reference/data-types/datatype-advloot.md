---
tags:
    - datatype
---
# `advloot`

<!--dt-desc-start-->
The AdvLoot TLO grants access to items in the Advanced Loot window.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='itemfilterdata', name='Filter', params='ItemID') }}

:   Inspect the loot filter for a given ItemID.

### {{ renderMember(type='bool', name='LootInProgress') }}

:   True/False if looting from AdvLoot is in progress

### {{ renderMember(type='int', name='PCount') }}

:   item count from the Personal list

### {{ renderMember(type='advlootitem', name='PList', params='Index') }}

:   Inspect the item at the specified index in the personal loot list.

### {{ renderMember(type='int', name='PWantCount') }}

:   Want count from the Personal list (AN + AG + ND + GD)

### {{ renderMember(type='int', name='SCount') }}

:   Item count from the Shared list

### {{ renderMember(type='advlootitem', name='SList', params='Index') }}

:   Inspect the item at the specified index in the shared loot list.

### {{ renderMember(type='int', name='SWantCount') }}

:   Want count from the Shared list (AN + AG + ND + GD)
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[advlootitem]: datatype-advlootitem.md
[bool]: datatype-bool.md
[int]: datatype-int.md
[itemfilterdata]: datatype-itemfilterdata.md
<!--dt-linkrefs-end--> 