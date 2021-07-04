## Description

Performs Math.Calc on *conditions*, gives *whentrue* if non-zero, gives *whenfalse* if zero

## Forms

-   *[string](../data-types/datatype-string.md)* **If\[***conditions,whentrue,whenfalse***\]**

## Access to Types

-   *[string](../data-types/datatype-string.md)* **string**

## Examples

`   /docommand ${If[${Me.Sitting},/stand,/echo I am not sitting down]}`

If I am sitting, stand up, Otherwise echo "I am not sitting down".

`   /docommand ${If[${Me.CurrentHP}<50,/cast "Gate",/goto :Continue]}`

If my hp percent is below 50 cast the Gate spell, otherwise goto the :Continue label.

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [string](../data-types/datatype-string.md)


