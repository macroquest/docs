# /ini

## Syntax

**/ini "filename" "keyname" "valuename" "value"**

## Description

This is used to write data to an ini file. Currently there is no way to delete an ini file entry.

## Example

_Stuff.ini_ contains the following data:

```text
[MySection]
; This is a comment
Key1=123
Key2=This is cool!
Key3=Wheeee... 15
```

After running the following command:

```text
/ini "stuff.ini" "Section2" "ANewKey" "Some Data!"
```

_Stuff.ini_ will contain the following:

```text
[MySection]
; This is a comment
Key1=123
Key2=This is cool!
Key3=Wheeee... 15 

[Section2]
ANewKey=Some Data!
```
