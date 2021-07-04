## Description

A string is an array of characters. In MQ2 there is no single character datatype, so any variable or expression that
contains text is considered a string.

## Members

<table>
<tbody>
<tr class="odd">
<td><p><strong>Type</strong></p></td>
<td><p><strong>Member</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td><p><em>string</em></p></td>
<td><p><strong>Arg[</strong>#<strong>,</strong>s<strong>]</strong></p></td>
<td><p>Returns the #th argument of the string separated by <em>s</em>. The separator <em>s</em> must be a single character (defaults to space).<br />
See below for difference between <strong>Token</strong> and <strong>Arg</strong></p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Compare[</strong>text<strong>]</strong></p></td>
<td><p>Determines how the initial string and the second string, <em>text</em>, compare to each other:</p>
<ul>
<li>If both are the same, <strong>Compare</strong> will return 0.</li>
<li>If the string is alphabetically before text, <strong>Compare</strong> will return -1.</li>
<li>If text is alphabetically after string, <strong>Compare</strong> will return 1.</li>
</ul>
<p><strong>Compare</strong> is case-insensitive</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>CompareCS[</strong>text<strong>]</strong></p></td>
<td><p>CompareCS is exactly the same as <strong>Compare</strong>, except that it is case-sensitive</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Count[</strong>c<strong>]</strong></p></td>
<td><p>Returns how many times a single character <em>c</em> occurs in the string</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>Equal[</strong>text<strong>]</strong></p></td>
<td><p>If the initial string and the second string <em>text</em> are exactly the same, returns TRUE. <strong>Equal</strong> is case-insensitive</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>EqualCS[</strong>text<strong>]</strong></p></td>
<td><p><strong>EqualCS</strong> is exactly the same as <strong>Equal</strong>, except that it is case-sensitive</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Find[</strong>text<strong>]</strong></p></td>
<td><p>This tries to find the second string <em>text</em> within the original string:</p>
<ul>
<li>If it is successful, it returns the first position in the string where <em>text</em> begins.</li>
<li>It returns NULL if <em>text</em> is not found.</li>
</ul>
<p><strong>Find</strong> is case-insensitive</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-int.md">int</a></em></p></td>
<td><p><strong>Length</strong></p></td>
<td><p>Returns the length of the string as an integer</p></td>
</tr>
<tr class="even">
<td><p><em>string</em></p></td>
<td><p><strong>Left[</strong>#<strong>]</strong></p></td>
<td><p>Returns the first # characters of the string. A negative # will return the whole string except for the last # characters</p></td>
</tr>
<tr class="odd">
<td><p><em>string</em></p></td>
<td><p><strong>Lower</strong></p></td>
<td><p>Returns the string in all lower-case</p></td>
</tr>
<tr class="even">
<td><p><em>string</em></p></td>
<td><p><strong>Mid[</strong>p<strong>,</strong>n<strong>]</strong></p></td>
<td><p>Returns a segment of the string, starting at position <strong>p</strong> and running <strong>n</strong> characters</p></td>
</tr>
<tr class="odd">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>NotEqual[</strong>text<strong>]</strong></p></td>
<td><p>If the initial string and the second string <em>text</em> are exactly the same, returns FALSE. <strong>NotEqual</strong> is case-insensitive</p></td>
</tr>
<tr class="even">
<td><p><em><a href="datatype-bool.md">bool</a></em></p></td>
<td><p><strong>NotEqualCS[</strong>text<strong>]</strong></p></td>
<td><p><strong>NotEqualCS</strong> is exactly the same as <strong>NotEqual</strong>, except that it is case-sensitive</p></td>
</tr>
<tr class="odd">
<td><p><em>string</em></p></td>
<td><p><strong>Replace[</strong>ReplaceThis<strong>,</strong>WithThis<strong>]</strong></p></td>
<td><p>Replaces <em>ReplaceThis</em> with <em>WithThis</em></p></td>
</tr>
<tr class="even">
<td><p><em>string</em></p></td>
<td><p><strong>Right[</strong>#<strong>]</strong></p></td>
<td><p>Returns the last # characters of the string. A negative # will return the whole string except for the first # characters</p></td>
</tr>
<tr class="odd">
<td><p><em>string</em></p></td>
<td><p><strong>Token[</strong>#<strong>,</strong>s<strong>]</strong></p></td>
<td><p>Returns the #th token of the string separated by <em>s</em>. The separator <em>s</em> must be a single character (defaults to space).<br />
See below for difference between <strong>Arg</strong> and <strong>Token</strong></p></td>
</tr>
<tr class="even">
<td><p><em>string</em></p></td>
<td><p><strong>Upper</strong></p></td>
<td><p>Returns the string in all upper-case</p></td>
</tr>
<tr class="odd">
<td><p>'<strong>'<a href="datatype-string.md">string</a></strong></p></td>
<td><p><strong>To String</strong></p></td>
<td><p>This is a string!</p></td>
</tr>
</tbody>
</table>

  
== Examples ==

### Simple Examples

    /declare TestString abcdebc
    /echo ${TestString.Find[bc]}          Will return 2
    /echo ${TestString.Left[2]}           Will return "ab"
    /echo ${TestString.Left[-2]}          Will return "abcde"
    /echo ${TestString.Mid[2,3]}          Will return "bcd"
    /echo ${TestString.Right[2]}          Will return "bc"
    /echo ${TestString.Right[-2]}         Will return "cdebc"

### Difference between Arg and Token

**Arg\[**#**,**s**\]** and **Token\[**#**,**s**\]** are very similar. The only difference between them is **Token** will
include null values, while **Arg** will skip them. For example:

    /declare TestString ABC,,DEF
    /echo ${TestString.Arg[2,,]}          Will return "DEF" because it is the second non-null string separated by a comma
    /echo ${TestString.Token[2,,]}        Will return "NULL" because the second token, the null string, is not ignored

### Compare strings to strings

-   **There is a temptation by some novice MQ2 macro writers to put the string inside quotes within brackets. Don't!**

<!-- -->

    #Event SpellWornOff  "Your #1# spell has worn off of #2#."

    Sub Event_SpellWornOff(string Line, string SpellName, string OnWho) 
       | You can put all kinds of logic here, on what to do when certain buffs or debuffs wear off.
       | In this example, we'll just check to see if the spell that wore off is a particular spell
       | multiple words seperated by spaces. Note: No quotes inside the brackets, and pay attention
       | to where the curly brackets are in the /if compare statement.
       /echo SpellWornOff: ${SpellName} wore off ${OnWho}
       /if (${SpellName.Equal[Enveloping Roots]}) /echo Yikes, Root wore off ... run!
    /return

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)


