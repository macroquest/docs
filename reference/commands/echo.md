---
tags:
    - ref
    - slash
---
# /echo

## Syntax

**/echo** _**text**_

## Description

Echoes the specified text (or variables) to the MQ Console window.

## Examples

**Colorized usage**

```text
/echo \amThis is a \attest\ax \n\agAll done, let's show a backslash: \ar\\
```

[MQ2] '''This is a test

All done, let's show a red backslash: \'''

**Default usage**

```text
/echo My current health percent is ${Me.PctHPs}
```

[MQ2] My current health percent is 100

## Color Codes

`\ab = black`  
`\a-b = black (dark)`

`\ag = green`  
`\a-g = green (dark)`

`\am = magenta`  
`\a-m = magenta (dark)`

`\ao = orange`  
`\a-o = orange (dark)`

`\ap = purple`  
`\a-p = purple (dark)`

`\ar = red`  
`\a-r = red (dark)`

`\at = cyan`  
`\a-t = cyan (dark)`

`\au = blue`  
`\a-u = blue (dark)`

`\aw = white`  
`\a-w = white (dark)`

`\ay = yellow`  
`\a-y = yellow (dark)`

`\ax = previous color (if no previous \a? this would be the default mq2 color)`

## Special Codes

`\n = newline`  
`\d = down? same as newline (LamahHerder knows not why)`
