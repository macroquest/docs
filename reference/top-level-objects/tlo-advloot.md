---
tags:
    - tlo
---
# `AdvLoot`

<!--tlo-desc-start-->
The AdvLoot TLO grants access to items in the Advanced Loot window.
<!--tlo-desc-end-->

## Associated DataTypes

## [advloot](../data-types/datatype-advloot.md)
{%
  include-markdown "reference/data-types/datatype-advloot.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-advloot.md') }}
:    <h2>Members</h2>
    {%
      include-markdown "reference/data-types/datatype-advloot.md"
      start="<!--dt-members-start-->"
      end="<!--dt-members-end-->"
      heading-offset=0
    %}
    {%
      include-markdown "reference/data-types/datatype-advloot.md"
      start="<!--dt-linkrefs-start-->"
      end="<!--dt-linkrefs-end-->"
    %}

## [advlootitem](../data-types/datatype-advlootitem.md)
{%
  include-markdown "reference/data-types/datatype-advlootitem.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-advlootitem.md') }}
:    <h2>Members</h2>
    {%
      include-markdown "reference/data-types/datatype-advlootitem.md"
      start="<!--dt-members-start-->"
      end="<!--dt-members-end-->"
      heading-offset=0
    %}
    {%
      include-markdown "reference/data-types/datatype-advlootitem.md"
      start="<!--dt-linkrefs-start-->"
      end="<!--dt-linkrefs-end-->"
    %}

## [itemfilterdata](../data-types/datatype-itemfilterdata.md)
{%
  include-markdown "reference/data-types/datatype-itemfilterdata.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-itemfilterdata.md') }}
:    <h2>Members</h2>
    {%
      include-markdown "reference/data-types/datatype-itemfilterdata.md"
      start="<!--dt-members-start-->"
      end="<!--dt-members-end-->"
      heading-offset=0
    %}
    {%
      include-markdown "reference/data-types/datatype-itemfilterdata.md"
      start="<!--dt-linkrefs-start-->"
      end="<!--dt-linkrefs-end-->"
    %}


## Usage

=== "Lua"

    ```lua
    -- Print the name of the first item in the personal loot list
    print(mq.TLO.AdvLoot.PList(1).Name())

    -- Print the number of items in the personal loot list
    print('There are ', mq.TLO.AdvLoot.PCount(), ' items in the personal loot list')

    -- Print the stack size of the first item in the personal loot list.
    print('The item in index 1 has a StackSize of ', mq.TLO.AdvLoot.PList(1).StackSize()))

    -- If the first item in the shared loot list is marked as Need, then print a message.
    if mq.TLO.AdvLoot.SList(1).Need() then
        print('I need that item!')
    end

    -- Print the NO DROP status of the first item in the personal loot list.
    print(mq.TLO.AdvLoot.PList(1).NoDrop())

    -- Wait 10 seconds, or until AdvLoot is no longer in the process of looting.
    mq.delay('10s', function() return not mq.TLO.AdvLoot.LootInProgress() end)

    -- Give the first item in the shared loot list to myself.
    if not mq.TLO.AdvLoot.LootInProgress() then
        print('Its safe to loot!')
        if mq.TLO.AdvLoot.SCount() >= 1 then
            print('I am going to give 1 ', mq.TLO.AdvLoot.SList(1).Name(), ' to myself')
            mq.cmdf('/advloot shared 1 giveto %s 1', mq.TLO.Me.Name())
        end
    else
        print('Do something else, loot is already in progress...')
    end
    ```

=== "MQScript"

    ```
    | Echo the name of the first item in the personal loot list
    /echo ${AdvLoot.PList[1].Name}

    | Echo the number of items in the personal loot list.
    /echo There are ${AdvLoot.PCount} items in the personal loot list

    | Echo the stack size of the first item in the personal loot list.
    /echo The item in index 1 has a StackSize of ${AdvLoot.PList[1].StackSize}

    | If the first item in the shared loot list is marked as Need, then echo.
    /if (${AdvLoot.SList[1].Need}==TRUE) /echo I need that item!

    | Echo the NO DROP status of the first item in the personal loot list: TRUE or FALSE.
    /echo ${AdvLoot.PList[1].NoDrop}

    | Wait 10 seconds, or until AdvLoot is no longer in the process of looting.
    /delay 10s !${AdvLoot.LootInProgress}

    | Give the first item in the shared loot list to myself.
    /if (!${AdvLoot.LootInProgress}) {
        /echo Its safe to loot!
        /if (${AdvLoot.SCount}>=1) {
            /echo I am going to give 1 ${AdvLoot.SList[1].Name} to myself
            /advloot shared 1 giveto ${Me.Name} 1
        }
    } else {
        /echo Do something else, loot is already in progress...
    }
    ```

<!--tlo-linkrefs-start-->
[advloot]: ../data-types/datatype-advloot.md
[advlootitem]: ../data-types/datatype-advlootitem.md
[bool]: ../data-types/datatype-bool.md
[int]: ../data-types/datatype-int.md
[int64]: ../data-types/datatype-int64.md
[itemfilterdata]: ../data-types/datatype-itemfilterdata.md
[spawn]: ../data-types/datatype-spawn.md
[string]: ../data-types/datatype-string.md
<!--tlo-linkrefs-end-->
