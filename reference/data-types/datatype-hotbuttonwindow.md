---
tags:
    - datatype
---
# `hotbuttonwindow`

Data related to hotbuttons

## Members

### {{ renderMember(type='altability', name='AltAbility') }}

:   If this hotbutton activates an alternate ability, this will return the alternate
    ability that is activated by pressing this button.

### {{ renderMember(type='int', name='ButtonIndex') }}

:   Returns the index of the button in the hotbutton page it resides on.

    e.g., if this hotbutton is the third button on the page, it will return 3.

### {{ renderMember(type='int', name='BarIndex') }}

:   Returns which bar this button resides on.

    e.g. If this hotbutton is on the first (main) hotbutton bar, it will return 1.

### {{ renderMember(type='int', name='IconSlot') }}

:   Returns the ID of the icon that is displayed by this hotbutton, if any. Which icon
    this identifies depends on the value of `IconType`.

    If no icon is present, this will return -1.

### {{ renderMember(type='int', name='IconType') }}

:   Returns the type of icon that is displayed by this hotbutton. Each type of icon is
    read from a specific icon texture atlas.

    If no icon is present, this will return -1.

    | Value | Meaning | Texture Atlas |
    | :---: | :---: | :---: |
    | -1 | No icon | n/a |
    | 0 | Item icon | A_DragItem |
    | 1 | Spell Icons | A_SpellGems |
    | 2 | Menu Icons | A_MenuIcons |

### {{ renderMember(type='item', name='Item') }}

:   An item that is linked to the hot button

### {{ renderMember(type='string', name='ItemGuid') }}

:   Unique identifier of the item associated with this hotbutton, if any.

    If no item is associated with this hotbutton, this will return an empty string.

### {{ renderMember(type='int', name='ItemId') }}

:   ID of the item associated with this hotbutton.

    If no item is associated with this hotbutton, this will return 0.

### {{ renderMember(type='string', name='ItemName') }}

:   Name of the item associated with this hotbutton.

    If no item is associated with this hotbutton, this will return an empty string.

### {{ renderMember(type='string', name='Label') }}

:   Display label for this hotbutton.

### {{ renderMember(type='int', name='PageIndex') }}

:   Returns the index of the page of the hotbar that this button resides on.

### {{ renderMember(type='int', name='Slot') }}

:   The meaning of this value depends on the type of hotbutton. The type of hotbutton can be
    determined with the `Type` member.

    See [HotButton Types](#hotbutton-types) for the meaning of the Slot parameter.

### {{ renderMember(type='social', name='Social') }}

:   Returns the social if this hotbutton is associated with a social. Otherwise returns NULL.

### {{ renderMember(type='string', name='Spell') }}

:   If the hotbutton is a spell gem, this will return the associated spell.

    If the hottbuton is an alternate ability, this will return the spell associated with the alternate ability.

    Otherwise, returns NULL.

### {{ renderMember(type='int', name='Type') }}

:   Returns the type of hotbutton. See [HotButton Types](#hotbutton-types).

### {{ renderMember(type='string', name='TypeName') }}

:   Returns the type name of hotbutton. See [HotButton Types](#hotbutton-types).


## Methods


### {{ renderMember(name='Activate') }}

:   Activates the hotbutton as if it were clicked.

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
| 11   | LeadershipAbility | Leadership ability button (emu only) | Which ability |
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


[altability]: datatype-altability.md
[item]: datatype-item.md
[int]: datatype-int.md
[social]: datatype-social.md
[string]: datatype-string.md