# TLO:If

## Description

Performs Math.Calc on _conditions_, gives _whentrue_ if non-zero, gives _whenfalse_ if zero

## Forms

* [_string_]() **If[\***conditions,whentrue,whenfalse**\*]**

## Access to Types

* [_string_]() **string**

## Examples

`/docommand ${If[${Me.Sitting},/stand,/echo I am not sitting down]}`

If I am sitting, stand up, Otherwise echo "I am not sitting down".

`/docommand ${If[${Me.CurrentHP}<50,/cast "Gate",/goto :Continue]}`

If my hp percent is below 50 cast the Gate spell, otherwise goto the :Continue label.

## See Also

* [Top-Level Objects](./)
* [string]()

