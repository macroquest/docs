# Macro Error

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

