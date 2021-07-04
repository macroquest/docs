# TLO:Plugin

## Description

Object that has access to members that provide information on a plugin.

## Forms

|  |  |
| :--- | :--- |
| [_plugin_](../data-types/datatype-plugin.md) **Plugin\[**\#**\]** | Plugin by number, starting with 1 and stopping whenever the list runs out of plugins. |
| [_plugin_](../data-types/datatype-plugin.md) **Plugin\[**name**\]** | Finds plugin by name |

## Access to Types

* [_plugin_](../data-types/datatype-plugin.md) **plugin**

## Examples

To see if a plugin is loaded:

`/if (${Plugin[MQ2MoveUtils].Name.Length}) {`  
`/echo MQ2MoveUtils plugin is loaded`  
`}`

To load a plugin if needed:

`/if ( !${Plugin[MQ2MoveUtils].Name.Length} ) {`  
`/plugin MQ2MoveUtils noauto`  
`/if ( !${Plugin[MQ2MoveUtils].Name.Length} ) {`  
`/echo To Use this macro you need to have MQ2MoveUtils Loaded`  
`/endmacro`  
`}`  
`}`

## See Also

* [Top-Level Objects](./)
* [plugin](../data-types/datatype-plugin.md)

