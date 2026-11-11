---
tags:
    - datatype
---
# `bandolier`

<!--dt-desc-start-->
Used to access information about bandolier sets on your character.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
/// member | bool Active
Indicates if the bandolier set is active
///

/// member | int Index
Returns the index number of the bandolier set
///

/// member | bandolieritem Item[Index]
Provides information about the specified item. Returns the Nth item in the set (Primary, Secondary, Ranged, Ammo)
///

/// member | string Name
Returns the name of the bandolier set
///
<!--dt-members-end-->

## Methods

| Name | Action |
| :--- | :--- |
| **Activate** | Activate the bandolier profile |


## Associated DataTypes

## `bandolieritem`

/// member | int IconID
Returns the icon id for the item
///

/// member | int ID
Returns the item id for the item
///

/// member | string Name
    label: Name (bandolieritem)
Returns the name of the item
///



## Examples

!!! example

    === "MQScript"

        ```
        | Activate the bandolier set named "1HB"
        /if (!${Me.Bandolier[1HB].Active}) {
            /echo Player want us to activate Bandolier: 1HB.
            /invoke ${Me.Bandolier[1HB].Activate}
        }

        | Print the weapon in the primary bandolier slot
        /echo I have a ${Me.Bandolier[1HB].Item[1].Name} in my primary bandolier slot
        ```

    === "Lua"

        ```lua
        -- Activate the bandolier set named "1HB"
        if not mq.TLO.Me.Bandolier('1HB').Active() then
            print('Player wants us to activate Bandodlier: 1HB')
            mq.TLO.Me.Bandolier('1HB').Activate()
        end

        -- Print the weapon in the primary bandolier slot
        print('I have a ', mq.TLO.Me.Bandolier('1HB').Item(1).Name(), ' in my primary bandolier slot')
        ```
<!--dt-linkrefs-start-->
[int]: datatype-int.md
[string]: datatype-bandolier.md
[bool]: datatype-bool.md
[bandolieritem]: datatype-bandolier.md#bandolieritem
<!--dt-linkrefs-end-->