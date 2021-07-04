## Description

`This has basically the same members as the old MacroQuest TLO`  
`but I think most of them are more fitting under the EverQuest TLO.`  
`MacroQuest TLO will inherit EverQuest TLO so backward compatibility is maintained`  
`BUT new macros should use EverQuest instead.`

## Forms

-   ''[Everquest](../data-types/datatype-everquest.md)

## Examples

`Example: Place the mouse over a window and do a /echo ${EverQuest.LastMouseOver.Name}`  
`Example2: /echo ${EverQuest.LastMouseOver.Tooltip}`

`Usage: /echo Im at charsselect and ${Window[CharacterListWnd].Child[CLW_Character_List].List[1,3]} is in ${EverQuest.CharSelectList[1].ZoneID}`  
`Output: (if a char named Eqmule is the first in your charlist) Im at charselect and Eqmule is in 202`  
`/echo Im at charsselect and Eqmule is in ${EverQuest.CharSelectList[Eqmule].ZoneID}`  
`Output: same as above.`

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [DataType: EverQuest](../data-types/datatype-everquest.md)
-   [Command /Setprio](../commands/setprio.md)


