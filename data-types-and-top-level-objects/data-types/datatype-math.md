# DataType:math

## Introduction

This DataType performs various mathematical calculations. In the following members, _n_ is any formula that consists of valid [Operators](../../documentation/operators.md).

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
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Abs[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">The absolute value of the result of <em>n</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Acos[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Arccosine of <em>n</em> (in degrees)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Asin[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Arcsine of <em>n</em> (in degrees)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Atan[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Arctangent of <em>n</em> (in degrees)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Calc[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Performs a mathematical calculation <em>n</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Cos[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Cosine of <em>n</em> (in degrees)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Dec[</b><em>hex</em><b>]</b>
      </td>
      <td style="text-align:left">Decimal value of a hexidecimal string</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Distance[</b>y,x,z<b>:</b>y,x,z<b>]</b>
      </td>
      <td style="text-align:left">
        <ul>
          <li>Calculates the distance between two points on the map</li>
          <li>1, 2, or 3 dimensions may be provided</li>
          <li>Defaults to your character&apos;s current location</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a>
      </td>
      <td style="text-align:left"><b>Hex[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Returns hexidecimal value of <a href="datatype-int.md"><em>int</em></a><em> n</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Not[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Bitwise complement of <em>n</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Rand[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Random integer. Rand[5] range 0 to 4. Rand[100,200] range 100 to 199</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Sin[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Sine of <em>n</em> (in degrees)</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Sqrt[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Square root of <em>n</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-float.md"><em>float</em></a>
      </td>
      <td style="text-align:left"><b>Tan[</b><em>n</em><b>]</b>
      </td>
      <td style="text-align:left">Tangent of <em>n</em> (in degrees)</td>
    </tr>
    <tr>
      <td style="text-align:left">&apos;<b>&apos;</b><a href="datatype-string.md"><b>string</b></a>
      </td>
      <td style="text-align:left"><b>To String</b>
      </td>
      <td style="text-align:left">NULL</td>
    </tr>
  </tbody>
</table>

## See Also

* [Data Types](./)
* [TLO:Math](../top-level-objects/tlo-math.md)
* [Operators](../../documentation/operators.md)

