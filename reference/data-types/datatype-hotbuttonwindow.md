---
tags:
    - datatype
---
# `hotbuttonwindow`

<!--dt-desc-start-->
Data related to hotbuttons
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | altability AltAbility
If this hotbutton activates an alternate ability, this will return the alternate
ability that is activated by pressing this button.
///

/// member | int ButtonIndex
Returns the index of the button in the hotbutton page it resides on.

e.g., if this hotbutton is the third button on the page, it will return 3.
///

/// member | int BarIndex
Returns which bar this button resides on.

e.g. If this hotbutton is on the first (main) hotbutton bar, it will return 1.
///

/// member | int IconSlot
Returns the ID of the icon that is displayed by this hotbutton, if any. Which icon
this identifies depends on the value of `IconType`.

If no icon is present, this will return -1.
///

/// member | int IconType
Returns the type of icon that is displayed by this hotbutton. Each type of icon is
read from a specific icon texture atlas.

If no icon is present, this will return -1.

| Value | Meaning | Texture Atlas |
| :---: | :---: | :---: |
| -1 | No icon | n/a |
| 0 | Item icon | A_DragItem |
| 1 | Spell Icons | A_SpellGems |
| 2 | Menu Icons | A_MenuIcons |
///

/// member | item Item
An item that is linked to the hot button
///

/// member | string ItemGuid
Unique identifier of the item associated with this hotbutton, if any.

If no item is associated with this hotbutton, this will return an empty string.
///

/// member | int ItemId
ID of the item associated with this hotbutton.

If no item is associated with this hotbutton, this will return 0.
///

/// member | string ItemName
Name of the item associated with this hotbutton.

If no item is associated with this hotbutton, this will return an empty string.
///

/// member | string Label
Display label for this hotbutton.
///

/// member | int PageIndex
Returns the index of the page of the hotbar that this button resides on.
///

/// member | int Slot
The meaning of this value depends on the type of hotbutton. The type of hotbutton can be
determined with the `Type` member.

See [HotButton Types](datatype-hotbuttonwindow.md#hotbutton-types) for the meaning of the Slot parameter.
///

/// member | social Social
Returns the social if this hotbutton is associated with a social. Otherwise returns NULL.
///

/// member | string Spell
If the hotbutton is a spell gem, this will return the associated spell.

If the hottbuton is an alternate ability, this will return the spell associated with the alternate ability.

Otherwise, returns NULL.
///

/// member | int Type
Returns the type of hotbutton. See [HotButton Types](datatype-hotbuttonwindow.md#hotbutton-types).
///

/// member | string TypeName
Returns the type name of hotbutton. See [HotButton Types](datatype-hotbuttonwindow.md#hotbutton-types).
///
<!--dt-members-end-->

## Methods


/// member | Activate
Activates the hotbutton as if it were clicked.

!!! Example

    Activate the first hotbutton on the first hotbar

    === "Lua"

        ```lua
        mq.TLO.Window("HotButtonWnd/HB_Button1").HotButton.Activate()
        ```

    === "MQScript"

        ```text
        /invoke ${Window[HotButtonWnd/HB_Button1].HotButton.Activate}
        ```
///


## HotButton Types

Each hotbutton has a type that determines what it is associated with. The type also
determines the meaning of the Slot

| Type | Type Name         | Contents | Slot |
| ---- | ----------------- | ----------- | ---- |
| 0    | None              | Empty hotbutton | _n/a_ |
| 1    | WeaponSlot        | The "Melee Attack" or "Range Attack" button | 0 = melee attack, 1 = range attack |
| 2    | CombatSkill       | _unused (deprecated)_ | _n/a_ |
| 3    | Ability           | _unused (deprecated)_ | _n/a_ |
| 4    | Social            | Social macro or an AltAbility button | 0-119 = social macro. 120+ = Alt ability (subtract 120 to get ability id) |
| 5    | InventorySlot     | An inventory slot | Invslot id |
| 6    | MenuButton        | Menu item from the EQ menu | Menu item id |
| 7    | SpellGem          | Memorized spell gem | Spell gem slot number |
| 8    | PetCommand        | Pet command from the pet window | Which pet command |
| 9    | Skill             | Skill or innate ability | 0-100 = skill by id, 101-125 = innate skill |
| 10   | MeleeAbility      | _unused (deprecated)_ | _n/a_ |
| 11   | LeadershipAbility | Leadership ability button (emu only) | First 3 bits (Slot & 7) is the button number (1, 2, 3). Shift right 3 bits to get the leader ability id. |
| 12   | ItemLink          | A specific item | Not used (uses item guid/id instead)  |
| 13   | KronoSlot         | The krono slot | _n/a_ |
| 14   | Command           | Keybind command | ID of the command |
| 15   | CombatAbility     | Combat ability | Spell ID of the combat ability |
| 16   | MountLink         | Item link from mount keyring | Not used (uses item guid/id instead) |
| 17   | IllusionLink      | Item link from illusion keyring | Not used (uses item guid/id instead) |
| 18   | FamiliarLink      | Item link from familiar keyring | Not used (uses item guid/id instead) |
| 19   | TeleportationLink | Item link from teleportation keyring | Not used (uses item guid/id instead) |


## Examples

To access a hot button, go through the Window TLO:

!!! example

    ```
    > /echo ${Window[HotButtonWnd2/HB_Button6].HotButton.Label}
    Harm Touch
    > /echo ${Window[HotButtonWnd2/HB_Button6].HotButton.Type}
    Social
    > /echo ${Window[HotButtonWnd2/HB_Button6].HotButton.AltAbility}
    6000
    > /echo ${Window[HotButtonWnd2/HB_Button6].HotButton.Spell}
    Harm Touch XXXII
    ```

The Window Inspector can be used to identify hotbars and hotbuttons.

<!--dt-linkrefs-start-->
[altability]: datatype-altability.md
[item]: datatype-item.md
[int]: datatype-int.md
[social]: datatype-social.md
[string]: datatype-string.md
<!--dt-linkrefs-end-->