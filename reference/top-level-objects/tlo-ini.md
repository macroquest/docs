---
tags:
    - ref
    - tlo
---
[TLO Page](../top-level-objects/tlo-list.md) | [DataType Page](../data-types/datatype-list.md)
# `Ini`

Reads value(s) from an ini file located in a relative or absolute path.

## Forms

[_string_](../data-types/datatype-string.md) **Ini**[_filename_,_section_,_key_,_default_]

:   The _section_, _key_, and _default_ do not need to be given. If _section_ or _key_ are not given, multiple values are read.

    _Section_ and _key_ may be set to -1 to skip them and give a new value.

    If the ini is located in a directory other than the root Macros directory is located, you can use
    a DOS-style filepath (relative or absolute) to locate the ini. If the macro accessing the ini
    is in the same non-root directory, you will still to provide the (relative or absolute) filepath.


## Examples

If sample.ini contains:

```
[KeyOne]
value1=foo
value2=bar
[KeyTwo]
Value3=foobar
```

```
/echo ${Ini[sample.ini,KeyOne,value1]}
```

foo

```
/echo ${Ini[sample.ini,KeyOne]}
```

value1|value2||

```
/echo ${Ini[..\sample.ini]}
```

KeyOne|KeyTwo||

If sample.ini is in \Macros\iniTest folder:

```
/echo ${Ini[sample.ini]}
```

NULL

```
/echo ${Ini[iniTest\sample.ini]}
```

KeyOne|KeyTwo||
