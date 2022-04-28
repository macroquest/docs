# DataType:merchant

This contains information related to the active merchant.

## Members

This type inherits members from [_spawn_](datatype-spawn.md) if a merchant is active.

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
      <td style="text-align:left">&lt;em&gt;&lt;/em&gt;<a href="datatype-string.md"><em>string</em></a>&lt;em&gt;&lt;/em&gt;</td>
      <td
      style="text-align:left"><b>To String</b>
        </td>
        <td style="text-align:left">Same as <b>Open</b>
        </td>
    </tr>
  </tbody>
</table>

## Methods

| Name | Action |
| :--- | :--- |
| **Buy[\#\]** | Buys \# of whatever is selected with **Merchant.SelectItem\[xxx]** |
| **OpenWindow** | Will open the merchant closest to you, or if you have a merchant target |
| **SelectItem[xxx\]** | Select item specified or partial match that fits. Use **SelectItem\[=xxx]** for EXACT match (its not case sensitive) |
| **Sell[\#]** | Sell \# of whatever is selected with /selectitem. See examples |

## Examples

Using `${Merchant.Sell[#]}`

`/selectitem "Diamond"`

Will select a "Diamond" you can also do "=Diamond" to match EXACT name (its not case sensitive though)

Then you can use

`/invoke ${Merchant.Sell[100]}`

Sells 100 of whatever is selected with /selectitem

