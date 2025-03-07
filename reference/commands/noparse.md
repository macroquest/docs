---
tags:
    - command
---
# /noparse

## Syntax

```eqcommand
/noparse <command>
```

## Description

Prevents any MQ2Data from being parsed when used in _command_.

## Example

* Here the literal string "${stuff}" is added to the ini file, as opposed to the current value of ${stuff}.

```text
/noparse /ini stuff.ini MySection MyVal ${stuff}
```

\*Here is another example. First we declare a variable

```text
/declare NotDisplayed string outer DISPLAYED
```

* Using echo by itself, the MQ2Data is parsed and displayed in the chatwnd:

```text
/echo ${NotDisplayed}
[MQ2] DISPLAYED
```

* Using /noparse, we do not parse the MQ2Data, and the literal string is displayed in the chatwnd

```text
/noparse /echo ${NotDisplayed}
[MQ2] ${NotDisplayed}
```

