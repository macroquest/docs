---
tags:
    - datatype
---
# `string`

A string is an array of characters. In MQ2 there is no single character datatype, so any variable or expression that contains text is considered a string.

## Members

| [_string_](datatype-string.md) | **Arg**[_#_,_s_] | Returns the #th argument of the string separated by _s_. The separator _s_ must be a single character (defaults to space).<br />See [Difference between Arg and Token][1].
### [int][int] `Compare[text]`

:   Determines how the initial string and the second string, _text_, compare to each other:<br/><ul><li>If both are the same, **Compare** will return 0.</li><li>If the string is alphabetically before text, **Compare** will return -1.</li><li>If text is alphabetically after string, **Compare** will return 1.</li></ul>**Compare** is case-insensitive

### [int][int] `CompareCS[text]`

:   The same as **Compare**, except that it is case-sensitive

### [int][int] `Count[c]`

:   Returns how many times a single character _c_ occurs in the string

### [bool][bool] `Equal[text]`

:   If the initial string and the second string _text_ are exactly the same, returns TRUE.<br/>**Equal** is case-insensitive

### [bool][bool] `EqualCS[text]`

:   The same as **Equal**, except that it is case-sensitive

### [int][int] `Find[text]`

:   This tries to find the second string _text_ within the original string:<br/><ul><li>If it is successful, it returns the first position in the string where _text_ begins.</li><li>It returns NULL if _text_ is not found.</li></ul>**Find** is case-insensitive

### [string][string] `Left[#]`

:   Returns the first # characters of the string. A negative _#_ will return the whole string except for the last # characters

### [int][int] `Length`

:   Returns the length of the string as an integer

### [string][string] `Lower`

:   Returns the string in all lower-case

### [string][string] `Mid[p,n]`

:   Returns a segment of the string, starting at position _p_ and running _n_ characters.

### [bool][bool] `NotEqual[text]`

:   If the initial string and the second string _text_ are exactly the same, returns FALSE. **NotEqual** is case-insensitive

### [bool][bool] `NotEqualCS[text]`

:   The same as **NotEqual**, except that it is case-sensitive.

### [string][string] `Replace[ReplaceThis,WithThis]`

:   Replaces _ReplaceThis_ with _WithThis_.

### [string][string] `Right[#]`

:   Returns the last _#_ characters of the string. A negative _#_ will return the whole string except for the first _#_ characters

### [string][string] `StripLinks`

:   Returns the plain text version of a string, stripping out the links

### [string][string] `Token[#,s]`

:   Returns the #th token of the string separated by _s_. The separator _s_ must be a single character (defaults to space).<br />See [Difference between Arg and Token][1].

### [string][string] `Upper`

:   Returns the string in all upper-case

### [string][string] `(To String)`

:   Returns the string


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

[1]: #difference-between-arg-and-token[int]: datatype-int.md
[string]: datatype-string.md
[achievementobj]: datatype-achievementobj.md
[bool]: datatype-bool.md
[time]: datatype-time.md
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[altability]: datatype-altability.md
[spell]: datatype-spell.md
[bandolieritem]: #bandolieritem-datatype
[int64]: datatype-int64.md
[timestamp]: datatype-timestamp.md
[float]: datatype-float.md
[buff]: datatype-buff.md
[spawn]: datatype-spawn.md
[auratype]: datatype-auratype.md
[item]: datatype-item.md
[worldlocation]: datatype-worldlocation.md
[ticks]: datatype-ticks.md
[fellowship]: datatype-fellowship.md
[strinrg]: datatype-string.md
[xtarget]: datatype-xtarget.md
[dzmember]: datatype-dzmember.md
[window]: datatype-window.md
[zone]: datatype-zone.md
[fellowshipmember]: datatype-fellowshipmember.md
[class]: datatype-class.md
[heading]: datatype-heading.md
[ground]: datatype-ground.md
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[double]: datatype-double.md
[invslot]: datatype-invslot.md
[augtype]: datatype-augtype.md
[itemspell]: datatype-itemspell.md
[evolving]: datatype-evolving.md
[keyringitem]: datatype-keyringitem.md
[raidmember]: datatype-raidmember.md
[body]: datatype-body.md
[cachedbuff]: datatype-cachedbuff.md
[deity]: datatype-deity.md
[race]: datatype-race.md
