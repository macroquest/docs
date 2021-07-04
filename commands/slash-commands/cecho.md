# CEcho

## Deprecated

Note this command is deprecated see [Echo](echo.md)

## Syntax

**/cecho** **\au** _**text**_&lt;/span&gt;

## Description

Colorizes the specified text \(or variables\) to the MQ2 chat window.

## Commands

`b = black`  
`g = green`  
`m = magenta`  
`o = orange`  
`p = purple`  
`r = red`  
`t = cyan`  
`u = blue`  
`w = white`  
`y = yellow`  
`x = default (whatever color was active immediately prior to the last color change; no -x btw)`

So example, \au = blue, \a-u = dark blue. \aw = white, \a-w = dark white \(light gray\)

The 2 functions are the same, just one of them echoes the debug header mq2 does, i.e. \[MQ2\] before your text output, the other doesn't.

## Examples

Regular echo

```Example:/echo`` My current health is at ${Me.PctHPs}%```

This ouputs "My current health is at 100%" in the MQ2 chat window.

Colorized echo

`Example: /cecho \ar This is a \attest\ax.\n\agAll done, let's show a backslash: \am\\`

This outputs **This is a testAll done, let's show a backslash: \**

## See Also

* [MQ2ChatWnd](../../plugins/core-plugins/mq2chatwnd.md)
* [MQ2CEcho](../../plugins/community-plugins/mq2cecho.md)

[Return to Slash Commands](./)

