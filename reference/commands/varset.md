---
tags:
    - ref
    - slash
---
# /varset

## Syntax

**/varset varname [** _**newvalue**_ **]**

## Description

Sets a variable directly to a new value.

* Keep in mind that the type of the variable may itself reject this value depending on what you give it.
* To clear the value of the variable, you may omit the new value.

## Examples

```text
 /varset MyString ${MyString}stuff             Concatenate a string variable
 /varset MyString stuff${MyString}             Inserts stuff at the front of ${MyString}
 /varset MyInt 123                             Sets MyInt to 123
 /varset MyTimer 123s                          Sets MyTimer to 123 seconds
 /varset MyFloat 1.23                          Sets MyFloat to 1.23
 /varset MyIntArray[n] 123                     Sets array element n to 123
```
