---
tags:
    - datatype
---
# `bandolier`

Used to access information about bandolier sets on your character.


## Members

### [bool][bool] `Active`

:   Indicates if the bandolier set is active

### [int][int] `Index`

:   Returns the index number of the bandolier set

### [bandolieritem][bandolieritem] `Item[&nbsp;Index&nbsp;]`

:   Provides information about the specified item. Returns the Nth item in the set (Primary, Secondary, Ranged, Ammo)

### [string][string] `Name`

:   Returns the name of the bandolier set



## Methods

| Name | Action |
| :--- | :--- |
| **Activate** | Activate the bandolier profile |


## Associated DataTypes

### `bandolieritem` DataType

### [int][int] `IconID`

:   Returns the icon id for the item

### [int][int] `ID`

:   Returns the item id for the item

### [string][string] `Name`

:   Returns the name of the item



## Usage Examples

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
[int]: datatype-int.md
[string]: datatype-bandolier.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
