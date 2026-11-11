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
/// member | itemfilterdata Filter[ItemID]
Inspect the loot filter for a given ItemID.
///

/// member | bool LootInProgress
True/False if looting from AdvLoot is in progress
///

/// member | int PCount
item count from the Personal list
///

/// member | advlootitem PList[Index]
Inspect the item at the specified index in the personal loot list.
///

/// member | int PWantCount
Want count from the Personal list (AN + AG + ND + GD)
///

/// member | int SCount
Item count from the Shared list
///

/// member | advlootitem SList[Index]
Inspect the item at the specified index in the shared loot list.
///

/// member | int SWantCount
Want count from the Shared list (AN + AG + ND + GD)
///
<!--dt-members-end-->
<!--dt-linkrefs-start-->
[advlootitem]: datatype-advlootitem.md
[bool]: datatype-bool.md
[int]: datatype-int.md
[itemfilterdata]: datatype-itemfilterdata.md
<!--dt-linkrefs-end--> 