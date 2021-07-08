# /call

## Syntax

**/call** _**subroutine**_ **\[Param0... \[Param\#\]\]**

### Description

Calls _subroutine_ \(defined later in the macro by "Sub _subroutine_"\).

\(_See_ [_Subroutines_](../../documentation/subroutines.md) _for detailed information_\)

### Examples

| \*\*\*\* |  |
| :--- | :--- |
| **/call MySub** | Executes the MySub subroutine |
| **/call MySub var1 var2 var3** | Executes the MySub and passes it parameters var1, var, var3 |
| **/call MySub ${var1} ${var2}** | Executes the MySub subroutine and passes it variables var1, var2 as parameters |

## See Also

* [Slash Commands](../slash-commands/)
* [MacroQuest2:Macros](../../documentation/macroquest2-macros.md)
* [Subroutines](../../documentation/subroutines.md)

