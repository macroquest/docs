## Syntax

**<span style="color:red">/call</span> *subroutine* \[<span style="color:blue">Param0</span>...
\[<span style="color:blue">Param#</span>\]\]**  
== Description == Calls *subroutine* (defined later in the macro by "Sub *subroutine*").  
  
( *See [Subroutines](subroutines.md) for detailed information*. )  
== Examples ==  
{\| border="1" cellpadding="2" cellspacing="0" \|**/call MySub** \|Executes the MySub subroutine. \|- \|**/call MySub
var1 var2 var3** \|Executes MySub subroutine and passes it parameters var1, var2 and var3 \|- \|**/call MySub ${var1}
${var2} ${var3}** \|Executes MySub subroutine and passes it variables var1, var2 and var3 as parameters \|}  

## See Also

-   [Slash Commands](../commands/slash-commands.md)
-   [MacroQuest2:Macros](../documentation/macroquest2-macros.md)
-   [Subroutines](subroutines.md)


