## Syntax

**<span style="color:red">/goto</span> *:labelname***

## Description

This moves the macro execution to the location of *:labelname* in the macro.

## Example

    :MyLabel
    /if ( ${Me.Moving} ) /goto :MyLabel
    /echo I am no longer moving!


