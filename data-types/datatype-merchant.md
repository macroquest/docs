## Description

This DataType contains information related to merchants

## Members

<table>
<tbody>
<tr class="odd">
<td><p><strong>Type</strong></p></td>
<td><p><strong>Member</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Full</strong></p></td>
<td><p>Returns TRUE if the merchant's inventory is full</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Items</strong></p></td>
<td><p>Number of items on the merchant</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-item.md">item</a></em></p></td>
<td><p><strong>Item[</strong>#<strong>]</strong></p></td>
<td><p>Item number # on the merchant's list</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-item.md">item</a></em></p></td>
<td><p><strong>Item[</strong>name<strong>]</strong></p></td>
<td><p>Finds an item by partial name on the merchant (use <strong>merchant.Item[</strong>=name<strong>]</strong> for exact)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Markup</strong></p></td>
<td><p>The number used to calculate the buy and sell value for an item (this is what is changed by charisma and faction). This value is capped at 1.05<br />
</p>
<ul>
<li>Markup*Item Value = Amount you buy item for</li>
<li>Item Value*(1/Markup) = Amount you sell item for</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Open</strong></p></td>
<td><p>Returns TRUE if merchant is open</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-item.md">item</a></em></p></td>
<td><p><strong>SelectedItem</strong></p></td>
<td><p>The currently selected item in the merchant window, and item type</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>ItemsReceived</strong></p></td>
<td><p>True if the merchants itemlist has been filled in.</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-action.md">action</a></em></p></td>
<td><p><strong>OpenWindow</strong></p></td>
<td><p>Will open the merchant closest to you, or if you have a merchant target</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-action.md">action</a></em></p></td>
<td><p><strong>SelectItem[xxx]</strong></p></td>
<td><p>Select item specified or partial match that fits. Use SelectItem[=xxx] for EXACT match(its not case sensitive)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-action.md">action</a></em></p></td>
<td><p><strong>Buy[#]</strong></p></td>
<td><p>Buys # of whatever is selected with Merchant.SelectItem[xxx]</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-action.md">action</a></em></p></td>
<td><p><strong>Sell[#]</strong></p></td>
<td><p>Sell # of whatever is selected with /seletitem. See examples</p></td>
</tr>
<tr class="even">
<td><p>'<strong>'<a href="datatype-bool.md">bool</a></strong></p></td>
<td><p><strong>To String</strong></p></td>
<td><p>Same as <strong>Open</strong></p></td>
</tr>
</tbody>
</table>

## Examples

Using ${Merchant.Sell\[#\]}

`/selectitem "Diamond" `

Will select a "Diamond" you can also do "=Diamond" to match EXACT name (its not case sensitive though)

Then you can use

`/invoke ${Merchant.Sell[100]}`

Sells 100 of whatever is selected with /selectitem

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [TLO:Merchant](../top-level-objects/tlo-merchant.md)
-   [selectitem](../commands/selectitem.md)


