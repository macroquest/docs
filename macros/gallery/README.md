---
tags:
   - macro
---
# Examples

## Chat-Sub

This is an example of a cleric bot with both loop based decision and instanced based dissision.

Created for and freely shared by Belgarion

\|Cleric Automation \|Set target name /Varset Toon "Character Name"

1. turbo
2. Chat Tell
3. Event Root "\#\*\#Root\#\*\#"
4. Event HPBuff "\#\*\#HPBuff\#\*\#"
5. Event Heal "\#\*\#Heal\#\*\#"

Sub Main

/declare Toon string Global /declare HPlower /declare HPhigher /declare CharID /declare MyID /declare Range /declare ManaWarn

/varset HPlower 30 /Varset HPhigher 55 /Varset ManaWarn 50 /varset Range 50 /varset Toon "Character Name"

/Target ${Toon} /Delay 10 /varset ToonID ${Target.ID}

/Target myself /Delay 10 /Varset MyID ${Target.ID}

body

/if (${Me.Casting.ID}\) /goto :body /target ${Toon} /If \(${Me.PctMana}\&lt;${ManaWarn}\) /Tell ${Toon} LOM !!! ${Me.PctMana} /If \(${Me.Pet.ID}==${NULL}\) /goto :Attack /if \(${Me.PctHPs}\&lt;80\) /goto :heal3 /if \(${Target.PctHPs}\&lt;${HPlower}\) /goto :heal1 /if \(${Target.PctHPs}\&lt;${HPhigher}) /goto :heal2 /goto :body

heal1

`/face`  
`/Tell ${Toon} Quick Heal Incomming 8)`  
`/cast 2`  
`/if (${Me.Standing} && !${Me.Mount.ID}) /sit`

/goto :body

heal2

`/face`  
`/tell ${Toon} Healing you up 8)`  
`/cast 9`  
`/if (${Me.Standing} && !${Me.Mount.ID}) /sit`

/goto :body

heal3

`/target myself`  
`/cast 4`  
`/if (${Me.Standing} && !${Me.Mount.ID}) /sit`

/goto :body

Attack

`/If (${Me.PctMana}<${ManaWarn}) /Tell ${Toon} LOM !!! ${Me.PctMana}`  
`|/Doevents`  
`/delay 20`  
`/assist ${Toon}`  
`/IF (${Target.ID}==${CharID}) /goto :Attack`  
`/If (${Target.ID}==${MyID}) /goto :Attack`  
`/If (${Target.Distance}>${Range}) /goto :Attack`  
`/keypress 9`  
`/delay 60`  
`/cast 7`

/goto :body

/Return

Sub Event\_Root

`/Tell ${Toon} Root Incomming`  
`/delay 10`  
`/assist ${Toon}`  
`/delay 10`  
`/Cast 6`

/Return

Sub Event\_HPBuff

`/Tell ${Toon} HP Buff Incomming`  
`/delay 10`  
`/Target ${Toon}`  
`/delay 10`  
`/Cast 5`

/Return

Sub Event\_Heal

`/Tell ${Toon} Heal on demand Incomming`  
`/delay 10`  
`/Target ${Toon}`  
`/delay 10`  
`/Cast 9`

/Return

The Problem is in the return to Sub main from the Sub Event on the /doevents call. To remedy replace /Return with /Return Main or /goto :body.

## Macro Errors

With the recent changes for ${String\[ an attempt was made to fix an existing statement.

```text
:CounterLoop 
   /if (${String[${Ini[${FileName},${SectionName},${ArrayType}${nValues}]}].Equal[null]}) { 
      /varcalc nValues ${nValues}-1 
      /goto :MakeArray 
   } 
   /varcalc nValues ${nValues}+1 
   /goto :CounterLoop
```

Error:

```text
Unparsable in calculation 'E'
adv_fishing.mac@145(ReadINI(FileName,SectionName,ArrayType)):/if ($Ini{$FileName},${SectionName},${ArrayType}${nValues}]}.Equal[null]}){adv_Fishing.mac@41(Main): /call ReadINI FishingLoot.ini "$Zone.Name}" Loot
Failed to parse /if condition (NULL.Equal}), non-numeric encountered.
```

Attempted fixes: assumption - remove string syntax and clear check for null value,

```text
/if (${Ini[${FileName},${SectionName},${ArrayType}${nValues}] > 0)
```

this resulted in script working but all loot was dropped, the array was not populated from ini file.

Solution:

```text
:CounterLoop 
   /if (${Ini[${FileName},${SectionName},${ArrayType}${nValues},NULL].Equal[NULL]}) { 
     /varcalc nValues ${nValues}-1 
     /goto :MakeArray 
  } 
  /varcalc nValues ${nValues}+1 
  /goto :CounterLoop
```

This was able to make the macro work. I doubt this was the only solution but after some suggestions by others this block of code worked.
