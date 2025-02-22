---
tags:
    - command
---
# /dosocial

## Syntax

**/dosocial [ list |** _social name_ **]**

## Description

This command allows you to list all your current socials, by name and number, or activate them by name.  
It is useful in that you could activate a social by name as long as it is in your social window without having to change hotbar pages, or call a social by name from a macro.

## Examples

### list parameter

* _/dosocial list_ output for a newly-created character

```text
Socials: (page,number) name
(1, 1) Afk
1:/afk
(1, 2) Anon
1:/anon
(1, 3) Split
1: /autosplit
(1, 4) Bug
1: /bug

...and so on
```

* _/dosocial list_ for custom multi-line socials

```text
same stuff as above example

(2, 7) MyMacro
1: /macro MyMacro
2: /echo I have activated MyMacro.mac via a social button
```

### calling a social by name

```text
/dosocial "MyMacro"
```

Typing the command in this way would execute Line 1 and 2 of the above example MyMacro social button.

