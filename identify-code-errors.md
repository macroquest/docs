Finding errors in a perticular part of a macro can be a challenge but never impossible. After an unsuccessfull attempt
to get the macro to run an eror message was generated. "Due to complete misuse of the String Top-Level Object, it has
been removed."

Here we look at two pieces from the Cleric Bot macro.

/varset Classes ${String\[${SpellBuff\[${i},2\]}\].Count\[,\]}

` /if (${Spawn[${sID}].Class.Name.Equal[${String[${SpellBuff[${i},2]}].Arg[${h},,]}]}) { `

Since ${String\[ is no longer valid attempt to remove and re-run the macro. With $String\[ removed the error is gone,
but now a new error is present.

No such 'bool' member 'Arg' ClericBot.mac@2031 (singlebuffs): /if
(${Spawn\[${sID}\].Class.Name.Equal\[${String\[${SpellBuff\[${i},2\]}\].Arg\[${h},,\]}\]}) { ClericBot.mac@789 (Main):
/if (${Me.PctMana}>40 /if........./call SingleBuffs Unparsable in Calculation

Following the code the macro is testing predetermined conditions then calling the single buff routine. Once that routine
is called the new error is generated.
