---
tags:
    - command
---
# /for

### Syntax

**/for** _**varname** initial-value_ **to\|downto** final-value **[step** _interval_**]**

**/next** _**varname**_

## Description

This runs all commands between the /for line and the /next line, after which it increments/decrements the _varname_ number (\#1\) by _step_ number \(\#3\) \(default is 1) before running through the commands again. It will keep doing this until the _varname_ number equals \#2. You can end a /for loop immediately with /break or try the next iteration with /continue.

### Examples

**Simplest**

```text
/declare varname int local
/for varname 1 to 5
    /echo ${varname}
/next varname


| Will output:
|  1
|  2
|  3
|  4
|  5
```

**Using /continue**

```text
/declare varname int local
/for varname 1 to 5
   /if ({$varname} == 3) /continue
   /echo ${varname}
/next varname


| Will output:
|  1
|  2
|  4
|  5
```

**Using /break**

```text
/declare varname int local
/for varname 1 to 5
    /if (${varname} == 3) /break
    /echo ${varname}
/next varname


| Will output:
|  1
|  2
```

**With a pre-defined ending variable**

```text
/declare foo int local 5

/declare varname int local
/for varname 1 ${foo}
  /echo ${varname}
/next varname

| Will output:
|  1
|  2
|  3
|  4
|  5
```
