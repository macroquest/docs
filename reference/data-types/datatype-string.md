# DataType:string

A string is an array of characters. In MQ2 there is no single character datatype, so any variable or expression that contains text is considered a string.

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
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Arg[</b>#<b>,</b>s<b>]</b>
        </td>
        <td style="text-align:left">Returns the #th argument of the string separated by <em>s</em>. The separator <em>s</em> must
          be a single character (defaults to space).
          <br />See below for difference between <b>Token</b> and <b>Arg</b>
        </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Compare[</b>text<b>]</b>
      </td>
      <td style="text-align:left">
        <p>Determines how the initial string and the second string, <em>text</em>,
          compare to each other:</p>
        <ul>
          <li>If both are the same, <b>Compare</b> will return 0.</li>
          <li>If the string is alphabetically before text, <b>Compare</b> will return
            -1.</li>
          <li>If text is alphabetically after string, <b>Compare</b> will return 1.</li>
        </ul>
        <p><b>Compare</b> is case-insensitive</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>CompareCS[</b>text<b>]</b>
      </td>
      <td style="text-align:left">CompareCS is exactly the same as <b>Compare</b>, except that it is case-sensitive</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Count[</b>c<b>]</b>
      </td>
      <td style="text-align:left">Returns how many times a single character <em>c</em> occurs in the string</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>Equal[</b>text<b>]</b>
      </td>
      <td style="text-align:left">If the initial string and the second string <em>text</em> are exactly the
        same, returns TRUE. <b>Equal</b> is case-insensitive</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>EqualCS[</b>text<b>]</b>
      </td>
      <td style="text-align:left"><b>EqualCS</b> is exactly the same as <b>Equal</b>, except that it is case-sensitive</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Find[</b>text<b>]</b>
      </td>
      <td style="text-align:left">
        <p>This tries to find the second string <em>text</em> within the original string:</p>
        <ul>
          <li>If it is successful, it returns the first position in the string where <em>text</em> begins.</li>
          <li>It returns NULL if <em>text</em> is not found.</li>
        </ul>
        <p><b>Find</b> is case-insensitive</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-int.md"><em>int</em></a>
      </td>
      <td style="text-align:left"><b>Length</b>
      </td>
      <td style="text-align:left">Returns the length of the string as an integer</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Left[</b>#<b>]</b>
        </td>
        <td style="text-align:left">Returns the first # characters of the string. A negative # will return
          the whole string except for the last # characters</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Lower</b>
        </td>
        <td style="text-align:left">Returns the string in all lower-case</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Mid[</b>p<b>,</b>n<b>]</b>
        </td>
        <td style="text-align:left">Returns a segment of the string, starting at position <b>p</b> and running <b>n</b> characters</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>NotEqual[</b>text<b>]</b>
      </td>
      <td style="text-align:left">If the initial string and the second string <em>text</em> are exactly the
        same, returns FALSE. <b>NotEqual</b> is case-insensitive</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-bool.md"><em>bool</em></a>
      </td>
      <td style="text-align:left"><b>NotEqualCS[</b>text<b>]</b>
      </td>
      <td style="text-align:left"><b>NotEqualCS</b> is exactly the same as <b>NotEqual</b>, except that it
        is case-sensitive</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Replace[</b>ReplaceThis<b>,</b>WithThis<b>]</b>
        </td>
        <td style="text-align:left">Replaces <em>ReplaceThis</em> with <em>WithThis</em>
        </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Right[</b>#<b>]</b>
        </td>
        <td style="text-align:left">Returns the last # characters of the string. A negative # will return
          the whole string except for the first # characters</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Token[</b>#<b>,</b>s<b>]</b>
        </td>
        <td style="text-align:left">Returns the #th token of the string separated by <em>s</em>. The separator <em>s</em> must
          be a single character (defaults to space).
          <br />See below for difference between <b>Arg</b> and <b>Token</b>
        </td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>Upper</b>
        </td>
        <td style="text-align:left">Returns the string in all upper-case</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="datatype-string.md"><em>string</em></a></td>
      <td
      style="text-align:left"><b>To String</b>
        </td>
        <td style="text-align:left">This is a string!</td>
    </tr>
  </tbody>
</table>

## Examples

### Simple Examples

```text
/declare TestString abcdebc
/echo ${TestString.Find[bc]}          Will return 2
/echo ${TestString.Left[2]}           Will return "ab"
/echo ${TestString.Left[-2]}          Will return "abcde"
/echo ${TestString.Mid[2,3]}          Will return "bcd"
/echo ${TestString.Right[2]}          Will return "bc"
/echo ${TestString.Right[-2]}         Will return "cdebc"
```

### Difference between Arg and Token

**Arg[**\#**,**s**\]** and **Token\[**\#**,**s**]** are very similar. The only difference between them is **Token** will include null values, while **Arg** will skip them. For example:

```text
/declare TestString ABC,,DEF
/echo ${TestString.Arg[2,,]}          Will return "DEF" because it is the second non-null string separated by a comma
/echo ${TestString.Token[2,,]}        Will return "NULL" because the second token, the null string, is not ignored
```

### Compare strings to strings

* **There is a temptation by some novice MQ2 macro writers to put the string inside quotes within brackets. Don't!**

```text
#Event SpellWornOff  "Your #1# spell has worn off of #2#."

Sub Event_SpellWornOff(string Line, string SpellName, string OnWho) 
   | You can put all kinds of logic here, on what to do when certain 
   | buffs or debuffs wear off.
   | In this example, we'll just check to see if the spell that wore
   | off is a particular spell multiple words seperated by spaces.
   |
   | Note: No quotes inside the brackets, and pay attention
   | to where the curly brackets are in the /if compare statement.
   /echo SpellWornOff: ${SpellName} wore off ${OnWho}
   /if (${SpellName.Equal[Enveloping Roots]}) /echo Yikes, Root wore off ... run!
/return
```

