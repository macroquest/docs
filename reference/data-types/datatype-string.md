---
tags:
    - datatype
---
# `string`

A string is an array of characters. In MQ2 there is no single character datatype, so any variable or expression that contains text is considered a string.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_string_](datatype-string.md) | **Arg**[_#_,_s_] | Returns the #th argument of the string separated by _s_. The separator _s_ must be a single character (defaults to space).<br />See [Difference between Arg and Token][1].
| [_int_](datatype-int.md) | **Compare**[_text_] | Determines how the initial string and the second string, _text_, compare to each other:<br/><ul><li>If both are the same, **Compare** will return 0.</li><li>If the string is alphabetically before text, **Compare** will return -1.</li><li>If text is alphabetically after string, **Compare** will return 1.</li></ul>**Compare** is case-insensitive |
| [_int_](datatype-int.md) | **CompareCS**[_text_] | The same as **Compare**, except that it is case-sensitive |
| [_int_](datatype-int.md) | **Count**[_c_] | Returns how many times a single character _c_ occurs in the string |
| [_bool_](datatype-bool.md) | **Equal**[_text_] | If the initial string and the second string _text_ are exactly the same, returns TRUE.<br/>**Equal** is case-insensitive |
| [_bool_](datatype-bool.md) | **EqualCS**[_text_] | The same as **Equal**, except that it is case-sensitive |
| [_int_](datatype-int.md) | **Find**[_text_] | This tries to find the second string _text_ within the original string:<br/><ul><li>If it is successful, it returns the first position in the string where _text_ begins.</li><li>It returns NULL if _text_ is not found.</li></ul>**Find** is case-insensitive |
| [_string_](datatype-string.md) | **Left**[_#_] | Returns the first # characters of the string. A negative _#_ will return the whole string except for the last # characters |
| [_int_](datatype-int.md) | **Length** | Returns the length of the string as an integer |
| [_string_](datatype-string.md) | **Lower** | Returns the string in all lower-case |
| [_string_](datatype-string.md) | **Mid**[_p_,_n_] | Returns a segment of the string, starting at position _p_ and running _n_ characters. |
| [_bool_](datatype-bool.md) | **NotEqual**[_text_] | If the initial string and the second string _text_ are exactly the same, returns FALSE. **NotEqual** is case-insensitive |
| [_bool_](datatype-bool.md) | **NotEqualCS**[_text_] | The same as **NotEqual**, except that it is case-sensitive. |
| [_string_](datatype-string.md) | **Replace**[_ReplaceThis_,_WithThis_] | Replaces _ReplaceThis_ with _WithThis_. |
| [_string_](datatype-string.md) | **Right**[_#_] | Returns the last _#_ characters of the string. A negative _#_ will return the whole string except for the first _#_ characters |
| [_string_](datatype-string.md) | **StripLinks** | Returns the plain text version of a string, stripping out the links |
| [_string_](datatype-string.md) | **Token**[_#_,_s_] | Returns the #th token of the string separated by _s_. The separator _s_ must be a single character (defaults to space).<br />See [Difference between Arg and Token][1]. |
| [_string_](datatype-string.md) | **Upper** | Returns the string in all upper-case |
| [_string_](datatype-string.md) | **(To String)** | Returns the string |

## Usage

### Simple Examples

```text
/declare TestString abcdebc
/echo ${TestString.Find[bc]}         | Will return 2
/echo ${TestString.Left[2]}          | Will return "ab"
/echo ${TestString.Left[-2]}         | Will return "abcde"
/echo ${TestString.Mid[2,3]}         | Will return "bcd"
/echo ${TestString.Right[2]}         | Will return "bc"
/echo ${TestString.Right[-2]}        | Will return "cdebc"
```

### Difference between Arg and Token

**Arg**[_#_,_s_] and **Token**[_#_,_s_] are very similar. The only difference between them is **Token** will include null values, while **Arg** will skip them. For example:

```text
/declare TestString ABC,,DEF

| Will return "DEF" because it is the second non-null string separated by a comma:
/echo ${TestString.Arg[2,,]}

| Will return "NULL" because the second token, the null string, is not ignored:
/echo ${TestString.Token[2,,]}
```

### Compare strings to strings

!!! Warning

    There is a temptation by some novice macro writers to put the string inside quotes within brackets. Don't!

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

[1]: #difference-between-arg-and-token