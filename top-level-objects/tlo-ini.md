## Description

Reads value(s) from an ini file located in a relative or absolute path.

## Forms

-   *[string](../data-types/datatype-string.md)* **Ini\[***filename***,**''section***,***key***,***default'**'\]**
    -   The *section*, *key*, and *default* do not need to be given. If *section* or *key* are not given, multiple
        values are read.
    -   *Section* and *key* may be set to -1 to skip them and give a new value.
    -   If the ini is located in a directory other than the root Macros directory is located, you can use a DOS-style
        filepath (relative or absolute) to locate the ini. If the macro accessing the ini is in the same non-root
        directory, you will still to provide the (relative or absolute) filepath.

## Access to Types

-   *[string](../data-types/datatype-string.md)* **string**

## Examples

If sample.ini contains:

`[KeyOne]`  
`value1=foo`  
`value2=bar`  
`[KeyTwo]`  
`Value3=foobar`

`/echo ${Ini[sample.ini,KeyOne,value1]}           foo`  
`/echo ${Ini[sample.ini,KeyOne]}                  value1|value2||`  
`/echo ${Ini[..\sample.ini]}                      KeyOne|KeyTwo||`

If sample.ini is in \\Macros\\iniTest folder:

`/echo ${Ini[sample.ini]}                         NULL`  
`/echo ${Ini[iniTest\sample.ini]}                 KeyOne|KeyTwo||`

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [string](../data-types/datatype-string.md)
-   [/ini for writing information to the ini file](../macro-commands/ini.md)


