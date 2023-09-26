---
tags:
    - tlo
---
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
            ```[int]: ../data-types/datatype-int.md
[string]: ../data-types/datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: ../data-types/datatype-bool.md
[time]: datatype-time.md
[achievement]: ../data-types/datatype-achievement.md
[achievementcat]: ../data-types/datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: ../data-types/datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: ../data-types/datatype-float.md
[buff]: datatype-buff.md
[spawn]: ../data-types/datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
[zone]: datatype-zone.md
[fellowshipmember]: datatype-fellowshipmember.md
[class]: datatype-class.md
[heading]: datatype-heading.md
[ground]: datatype-ground.md
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[double]: ../data-types/datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
[raidmember]: datatype-raidmember.md
[body]: datatype-body.md
[cachedbuff]: datatype-cachedbuff.md
[deity]: datatype-deity.md
[race]: datatype-race.md
[taskmember]: datatype-task.md
[achievementmgr]: #achievementmgr-type
[itemfilterdata]: #itemfilterdata-type
[advlootitem]: #advlootitem-type
[alert]: #alert-type
[alertlist]: #alertlist-type
[friends]: #friends-type
