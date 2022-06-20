---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `SelectedItem`

Used to return information on the object that is selected in your own inventory while using a merchant.

## Forms

[_item_](../data-types/datatype-item.md) **SelectedItem**

:   !!! example

        === "MQScript"

            ```
            /if (!${SelectedItem.ID}) {
                /echo Nothing in your inventory is selected
            } else {
                /echo Size of the item: ${SelectedItem.Size}

                /if (${SelectedItem.Charges} < 1) {
                    /echo the selected item is out of charges
                }

                /if (${SelectedItem.Name.Equal[rusty dagger]}) {
                    /echo the selected item is a rusty dagger
                }
            }
            ```
        
        === "Lua"

            ```lua
            if mq.TLO.SelectedItem() == nil then
                print('Nothing in your inventory is selected')
            else
                print('Size of the item: ', mq.TLO.SelectedItem.Size())

                if mq.TLO.SelectedItem.Charges() < 1 then
                    print('The selected item is out of charges')
                end

                if mq.TLO.SelectedItem.Name.Equal('rusty dagger')() then
                    print('The selected item is a rusty dagger')
                end
            end
            ```