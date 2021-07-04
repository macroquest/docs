## Introduction

This DataType performs various mathematical calculations. In the following members, *n* is any formula that consists of
valid [Operators](../documentation/operators.md).

## Members

<table>
<thead>
<tr class="header">
<th><p><strong>Type</strong></p></th>
<th><p><strong>Member</strong></p></th>
<th><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Abs[</strong><em>n</em><strong>]</strong></p></td>
<td><p>The absolute value of the result of <em>n</em></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Acos[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Arccosine of <em>n</em> (in degrees)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Asin[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Arcsine of <em>n</em> (in degrees)</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Atan[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Arctangent of <em>n</em> (in degrees)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Calc[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Performs a mathematical calculation <em>n</em></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Cos[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Cosine of <em>n</em> (in degrees)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Dec[</strong><em>hex</em><strong>]</strong></p></td>
<td><p>Decimal value of a hexidecimal string</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Distance[</strong>y,x,z<strong>:</strong>y,x,z<strong>]</strong></p></td>
<td><ul>
<li>Calculates the distance between two points on the map</li>
<li>1, 2, or 3 dimensions may be provided</li>
<li>Defaults to your character's current location</li>
</ul></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-string.md">string</a></em></p></td>
<td><p><strong>Hex[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Returns hexidecimal value of <em><a href="datatype-int.md">int</a> n</em></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Not[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Bitwise complement of <em>n</em></p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Rand[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Random integer. Rand[5] range 0 to 4. Rand[100,200] range 100 to 199</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Sin[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Sine of <em>n</em> (in degrees)</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Sqrt[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Square root of <em>n</em></p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-float.md">float</a></em></p></td>
<td><p><strong>Tan[</strong><em>n</em><strong>]</strong></p></td>
<td><p>Tangent of <em>n</em> (in degrees)</p></td>
</tr>
<tr class="odd">
<td><p>'<strong>'<a href="datatype-string.md">string</a></strong></p></td>
<td><p><strong>To String</strong></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>

## See Also

-   [Data Types](data-types.md)
-   [TLO:Math](../top-level-objects/tlo-math.md)
-   [Operators](../documentation/operators.md)


