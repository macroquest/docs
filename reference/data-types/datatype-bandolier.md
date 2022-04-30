# DataType:bandolier

Used to access information about bandolier sets on your character.


## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_](../data-types/datatype-bool.md) | **Active** | Indicates if the bandolier set is active |
| [_int_](../data-types/datatype-int.md) | **Index** | Returns the index number of the bandolier set |
| [_bandolieritem_](#bandolieritem-datatype) | **Item**[&nbsp;_Index_&nbsp;] | Provides information about the specified item. Returns the Nth item in the set (Primary, Secondary, Ranged, Ammo) |
| [_string_](../data-types/datatype-bandolier.md) | **Name** | Returns the name of the bandolier set |


## Methods

| Name | Action |
| :--- | :--- |
| **Activate** | Activate the bandolier profile |


## Associated DataTypes

### `bandolieritem` DataType

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](../data-types/datatype-int.md)          | **IconID** | Returns the icon id for the item |
| [_int_](../data-types/datatype-int.md)          | **ID** | Returns the item id for the item |
| [_string_](../data-types/datatype-bandolier.md) | **Name** | Returns the name of the item |


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
