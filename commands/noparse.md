## Syntax

**<span style="color:red">/noparse</span> *command***

## Description

Prevents any MQ2Data from being parsed when used in *command*.

## Example

-   Here the literal string "${stuff}" is added to the ini file, as opposed to the current value of ${stuff}.

<!-- -->

    /noparse /ini stuff.ini MySection MyVal ${stuff}

  
  
\*Here is another example. First we declare a variable

    /declare NotDisplayed string outer DISPLAYED

-   Using echo by itself, the MQ2Data is parsed and displayed in the chatwnd:

<!-- -->

    /echo ${NotDisplayed}
    [MQ2] DISPLAYED

-   Using /noparse, we do not parse the MQ2Data, and the literal string is displayed in the chatwnd

<!-- -->

    /noparse /echo ${NotDisplayed}
    [MQ2] ${NotDisplayed}

[Return to Slash Commands](slash-commands.md)


