# /continue

## Syntax

**/continue**

## Description

When in a /for or /while loop try the next iteration.

## Example

```text
/for varname 1 to 5
  /if ({$varname} == 3) /continue
  /echo ${varname}
/next varname

/declare varname int 0
/while (${varname} < 5) {
  /varcalc varname ${varname}+1
  /if ({$varname} == 3) /continue
  /echo ${varname} 
}
```

Each loop will output:

```text
 1
 2
 4
 5
```

## See also

* [/for](for.md)
* [/while](while.md)

