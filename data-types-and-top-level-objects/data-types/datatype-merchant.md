# DataType:merchant

## Description

This DataType contains information related to merchants

## Members

<table>
  <thead>
    <tr>
      <th style="text-align:left"><b>Type</b>
      </th>
      <th style="text-align:left"><b>Member</b>
      </th>
      <th style="text-align:left"><b>Description</b>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Full</b>
      </td>
      <td style="text-align:left">Returns TRUE if the merchant&apos;s inventory is full</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Items</b>
      </td>
      <td style="text-align:left">Number of items on the merchant</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-item.md"><em>item</em></a>
      </td>
      <td style="text-align:left"><b>Item[</b>#<b>]</b>
      </td>
      <td style="text-align:left">Item number # on the merchant&apos;s list</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-item.md"><em>item</em></a>
      </td>
      <td style="text-align:left"><b>Item[</b>name<b>]</b>
      </td>
      <td style="text-align:left">Finds an item by partial name on the merchant (use <b>merchant.Item[</b>=name<b>]</b> for
        exact)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Markup</b>
      </td>
      <td style="text-align:left">
        <p>The number used to calculate the buy and sell value for an item (this
          is what is changed by charisma and faction). This value is capped at 1.05
          <br
          />
        </p>
        <ul>
          <li>Markup*Item Value = Amount you buy item for</li>
          <li>Item Value*(1/Markup) = Amount you sell item for</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Open</b>
      </td>
      <td style="text-align:left">Returns TRUE if merchant is open</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-item.md"><em>item</em></a>
      </td>
      <td style="text-align:left"><b>SelectedItem</b>
      </td>
      <td style="text-align:left">The currently selected item in the merchant window, and item type</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>ItemsReceived</b>
      </td>
      <td style="text-align:left">True if the merchants itemlist has been filled in.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href><em>action</em></a>
      </td>
      <td style="text-align:left"><b>OpenWindow</b>
      </td>
      <td style="text-align:left">Will open the merchant closest to you, or if you have a merchant target</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href><em>action</em></a>
      </td>
      <td style="text-align:left"><b>SelectItem[xxx]</b>
      </td>
      <td style="text-align:left">Select item specified or partial match that fits. Use SelectItem[=xxx]
        for EXACT match(its not case sensitive)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href><em>action</em></a>
      </td>
      <td style="text-align:left"><b>Buy[#]</b>
      </td>
      <td style="text-align:left">Buys # of whatever is selected with Merchant.SelectItem[xxx]</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href><em>action</em></a>
      </td>
      <td style="text-align:left"><b>Sell[#]</b>
      </td>
      <td style="text-align:left">Sell # of whatever is selected with /seletitem. See examples</td>
    </tr>
    <tr>
      <td style="text-align:left">&apos;<b>&apos;</b><a href="datatype-bool.md"><b>bool</b></a>
      </td>
      <td style="text-align:left"><b>To String</b>
      </td>
      <td style="text-align:left">Same as <b>Open</b>
      </td>
    </tr>
  </tbody>
</table>

## Examples

Using ${Merchant.Sell\[\#\]}

`/selectitem "Diamond"`

Will select a "Diamond" you can also do "=Diamond" to match EXACT name \(its not case sensitive though\)

Then you can use

`/invoke ${Merchant.Sell[100]}`

Sells 100 of whatever is selected with /selectitem

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [TLO:Merchant](../top-level-objects/tlo-merchant.md)
* [selectitem](../../commands/slash-commands/selectitem.md)

