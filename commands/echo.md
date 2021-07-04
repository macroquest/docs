## Syntax

**<span style="color:red">/echo</span> *text***

## Description

Echos the specified text (or variables) to the MQ2 chat window.

## Examples

**Colorized usage**

    /echo \am This is a \attest\ax \n\agAll done, let's show a backslash: \ar\\

\[MQ2\] '''<span style="color:purple">This is a</span> <span style="color:blue"> test </span>

<span style="color:green">All done, let's show a red backslash: <span style="color:red">\\'''

**Default usage**

    /echo My current health percent is ${Me.PctHPs}

\[MQ2\] My current health percent is 100

## Color Codes

`\ab  = black`  
`\a-b = black (dark)`

`\ag  = green`  
`\a-g = green (dark)`

`\am  = magenta`  
`\a-m = magenta (dark)`

`\ao  = orange`  
`\a-o = orange (dark)`

`\ap  = purple`  
`\a-p = purple (dark)`

`\ar  = red`  
`\a-r = red (dark)`

`\at  = cyan`  
`\a-t = cyan (dark)`

`\au  = blue`  
`\a-u = blue (dark)`

`\aw  = white`  
`\a-w = white (dark)`

`\ay  = yellow`  
`\a-y = yellow (dark)`

`\ax = previous color (if no previous \a? this would be the default mq2 color)`

## Special Codes

`\n = newline`  
`\d = down? same as newline (LamahHerder knows not why)`

## See Also

-   [MQ2ChatWnd](../plugins/mq2chatwnd.md)
-   [MQ2Chat](../plugins/mq2chat.md)

[Return to Slash Commands](slash-commands.md)


