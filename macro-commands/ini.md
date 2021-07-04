## Syntax

**<span style="color:red">/ini</span> <span style="color:blue">"filename" "keyname" "valuename" "value"</span>**

## Description

This is used to write data to an ini file. Currently there is no way to delete an ini file entry.

## Example

*Stuff.ini* contains the following data:

    [MySection]
    ; This is a comment
    Key1=123
    Key2=This is cool!
    Key3=Wheeee... 15

After running the following command:

    /ini "stuff.ini" "Section2" "ANewKey" "Some Data!"

*Stuff.ini* will contain the following:

    [MySection]
    ; This is a comment
    Key1=123
    Key2=This is cool!
    Key3=Wheeee... 15 
     
    [Section2]
    ANewKey=Some Data!

## See Also

-   [TLO:Ini](../top-level-objects/tlo-ini.md) for reading information from the ini file.

 
