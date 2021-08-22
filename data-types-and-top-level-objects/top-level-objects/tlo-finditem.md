# TLO:FindItem

## Description

A TLO used to find an item on your character, corpse, or a merchant by partial or exact name match.   _See examples below._

## Forms

|  |  |
| :--- | :--- |
| [_item_](../data-types/datatype-item.md) **FindItem\[**name**\]** | Returns item on your character, a corpse, or a merchant by partial name match |
| [_item_](../data-types/datatype-item.md) **FindItem\[**=name**\]** | Returns item on your character, a corpse, or a merchant by exact name match |

## Access to Types

* [_item_](../data-types/datatype-item.md) **item**

## Examples

Looks for the Cleric Epic \(by exact match\) and prints its ID.

{% tabs %}
{% tab title="Lua" %}
```lua
/lua parse mq.TLO.FindItem("=Water Sprinkler of Nem Ankh").ID()
```
{% endtab %}

{% tab title="MQScript" %}
`/echo ${FindItem[=Water Sprinkler of Nem Ankh].ID}`
{% endtab %}
{% endtabs %}

Looks for an item with the name swirling in it, and prints the ID.

{% tabs %}
{% tab title="Lua" %}
```lua
/lua parse mq.TLO.FindItem("swirling").ID()
```
{% endtab %}

{% tab title="MQScript" %}
`/echo ${FindItem[swirling].ID}`
{% endtab %}
{% endtabs %}



## See Also

* [Top-Level Objects](./)
* [item](../data-types/datatype-item.md)

