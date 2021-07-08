# /break

## Syntax

**/break**

## **Description**

End a /for or /while loop immediately.

## Example

```text
 /for varname 1 to 5
   /if ({$varname} == 3) /break
   /echo ${varname}
 /next varname
```

Will output:

```text
 1
 2
```

## See also

* [/for](for.md)

