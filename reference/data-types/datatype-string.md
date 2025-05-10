---
tags:
    - datatype
---
# `string`

<!--dt-desc-start-->
A string is an array of characters. In MacroQuest there is no single character datatype, so any variable or expression that contains text is considered a string.
<!--dt-desc-end-->
## Members
<!--dt-members-start-->
### {{ renderMember(type='string', name='Arg', params='#,s') }}

:   Returns the #th argument of the string separated by _s_. The separator _s_ must be a single character (defaults to space).<br />See [Difference between Arg and Token][1].

### {{ renderMember(type='int', name='Compare', params='text') }}

:   Determines how the initial string and the second string, _text_, compare to each other:<br/><ul><li>If both are the same, **Compare** will return 0.</li><li>If the string is alphabetically before text, **Compare** will return -1.</li><li>If text is alphabetically after string, **Compare** will return 1.</li></ul>**Compare** is case-insensitive

### {{ renderMember(type='int', name='CompareCS', params='text') }}

:   The same as **Compare**, except that it is case-sensitive

### {{ renderMember(type='int', name='Count', params='c') }}

:   Returns how many times a single character _c_ occurs in the string

### {{ renderMember(type='bool', name='Equal', params='text') }}

:   If the initial string and the second string _text_ are exactly the same, returns TRUE.<br/>**Equal** is case-insensitive

### {{ renderMember(type='bool', name='EqualCS', params='text') }}

:   The same as **Equal**, except that it is case-sensitive

### {{ renderMember(type='int', name='Find', params='text') }}

:   This tries to find the second string _text_ within the original string:<br/><ul><li>If it is successful, it returns the first position in the string where _text_ begins.</li><li>It returns NULL if _text_ is not found.</li></ul>**Find** is case-insensitive

### {{ renderMember(type='string', name='Left', params='#') }}

:   Returns the first # characters of the string. A negative _#_ will return the whole string except for the last # characters

### {{ renderMember(type='int', name='Length') }}

:   Returns the length of the string as an integer

### {{ renderMember(type='string', name='Lower') }}

:   Returns the string in all lower-case

### {{ renderMember(type='string', name='Mid', params='p,n') }}

:   Returns a segment of the string, starting at position _p_ and running _n_ characters.

### {{ renderMember(type='bool', name='NotEqual', params='text') }}

:   If the initial string and the second string _text_ are exactly the same, returns FALSE. **NotEqual** is case-insensitive

### {{ renderMember(type='bool', name='NotEqualCS', params='text') }}

:   The same as **NotEqual**, except that it is case-sensitive.

### {{ renderMember(type='string', name='Replace', params='ReplaceThis,WithThis') }}

:   Replaces _ReplaceThis_ with _WithThis_.

### {{ renderMember(type='string', name='Right', params='#') }}

:   Returns the last _#_ characters of the string. A negative _#_ will return the whole string except for the first _#_ characters

### {{ renderMember(type='string', name='StripLinks') }}

:   Returns the plain text version of a string, stripping out the links

### {{ renderMember(type='string', name='Token', params='#,s') }}

:   Returns the #th token of the string separated by _s_. The separator _s_ must be a single character (defaults to space).<br />See [Difference between Arg and Token][1].

### {{ renderMember(type='string', name='Upper') }}

:   Returns the string in all upper-case

### [string][string] `(To String)`

:   Returns the string
<!--dt-members-end-->

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
<!--dt-linkrefs-start-->
[1]: #difference-between-arg-and-token
[achievement]: datatype-achievement.md
[achievementcat]: datatype-achievementcat.md
[achievementobj]: datatype-achievementobj.md
[altability]: datatype-altability.md
[augtype]: datatype-augtype.md
[auratype]: datatype-auratype.md
[bandolieritem]: #bandolieritem-datatype
[body]: datatype-body.md
[bool]: datatype-bool.md
[buff]: datatype-buff.md
[cachedbuff]: datatype-cachedbuff.md
[class]: datatype-class.md
[deity]: datatype-deity.md
[double]: datatype-double.md
[dzmember]: datatype-dzmember.md
[evolving]: datatype-evolving.md
[fellowship]: datatype-fellowship.md
[fellowshipmember]: datatype-fellowshipmember.md
[float]: datatype-float.md
[ground]: datatype-ground.md
[heading]: datatype-heading.md
[inifile]: datatype-inifile.md
[inifilesection]: datatype-inifilesection.md
[inifilesectionkey]: datatype-inifilesectionkey.md
[int]: datatype-int.md
[int64]: datatype-int64.md
[invslot]: datatype-invslot.md
[item]: datatype-item.md
[itemspell]: datatype-itemspell.md
[keyringitem]: datatype-keyringitem.md
[race]: datatype-race.md
[raidmember]: datatype-raidmember.md
[spawn]: datatype-spawn.md
[spell]: datatype-spell.md
[string]: datatype-string.md
[strinrg]: datatype-string.md
[ticks]: datatype-ticks.md
[time]: datatype-time.md
[timestamp]: datatype-timestamp.md
[window]: datatype-window.md
[worldlocation]: datatype-worldlocation.md
[xtarget]: datatype-xtarget.md
[zone]: datatype-zone.md
<!--dt-linkrefs-end-->
