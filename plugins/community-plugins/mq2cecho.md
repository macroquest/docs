# MQ2CEcho

## Description

Plugin to help colorize text in the MQ2 Window. Thank you for sharing htw!

* This plugin is included in the main source download.
* Link to the latest stable source: [1](https://macroquest.org/phpBB3/viewtopic.php?f=47&p=152508#p152508)

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

example: /cecho \arThis is a \attest\ax.\n\agAll done, let's show a backslash: \am\
