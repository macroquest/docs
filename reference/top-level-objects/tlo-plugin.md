---
tags:
    - tlo
---
# `Plugin`

<!--tlo-desc-start-->
Object that has access to members that provide information on a plugin.
<!--tlo-desc-end-->
## Forms
<!--tlo-forms-start-->
### {{ renderMember(type='plugin', name='Plugin', params='Name') }}

:   Finds plugin by name, uses full name match, case insensitive.

### {{ renderMember(type='plugin', name='Plugin', params='N') }}

:   Plugin by index, starting with 1 and stopping whenever the list runs out of plugins.
<!--tlo-forms-end-->

## Associated DataTypes

## [plugin](../data-types/datatype-plugin.md)
{%
  include-markdown "reference/data-types/datatype-plugin.md"
  start="<!--dt-desc-start-->"
  end="<!--dt-desc-end-->"
  trailing-newlines=false
%} {{ readMore('reference/data-types/datatype-plugin.md') }}

<h2>Members</h2>
{%
  include-markdown "reference/data-types/datatype-plugin.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "reference/data-types/datatype-plugin.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}

## Usage

To see if a plugin is loaded:

=== "MQScript"

    ```
    /if (${Plugin[MQ2MoveUtils].IsLoaded}) {
        /echo MQ2MoveUtils plugin is loaded!
    }
    ```

=== "Lua"

    ```lua
    if mq.TLO.Plugin('MQ2MoveUtils').IsLoaded() then
        print('MQ2MoveUtils plugin is loaded!')
    end
    ```

To load a plugin if needed:

=== "MQScript"

    ```
    /if (!${Plugin[MQ2MoveUtils].IsLoaded}) {
        /plugin MQ2MoveUtils noauto
        /if (!${Plugin[MQ2MoveUtils].IsLoaded}) {
            /echo To Use this macro you need to have MQ2MoveUtils Loaded
            /endmacro
        }
    }
    ```
<!--tlo-linkrefs-start-->
[plugin]: ../data-types/datatype-plugin.md
<!--tlo-linkrefs-end-->
