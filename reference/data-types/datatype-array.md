---
tags:
    - datatype
---
# `array`

Data related to arrays.

!!! Note

    Array indexing starts at 1.


## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_int_](datatype-int.md) | **Dimensions** | Number of dimensions in the array |
| [_int_](datatype-int.md) | **Size** | Total number of elements in the array |
| [_int_](datatype-int.md) | **Size**[ _N_ ] | Total number of elements stored in the _N_ th dimension of the array |

## Usage

To create an array, attach square brackets to the end of the variable name and place in it the number of elements per dimension.

!!! tip

    This array syntax only applies to MQScript. For lua, use tables instead.


### Array Examples

This creates a single-dimension local array of int with 10 elements (1-10) all 0:

```text
/declare MyArray[10] int
```

This creates a 2-dimensional 10x10 elements(1-10,1-10) int array of scope outer with all values of 5:

```text
/declare MyArray[10,10] int outer 5
```

This creates a 3-dimensional array with 4x5x6 elements (1-4,1-5, 1-6) with UNDEFINED-ARRAY-ELEMENT in each location:

```text
/declare MyArray[4,5,6] string outer UNDEFINED-ARRAY-ELEMENT
```

There is no limit to the number of dimensions or the number of elements in each dimension, but use your own good judgement.

**Note:** You cannot make an array of timers.

### Example Snippets

!!! example

    ```text title="ArrayExample.mac"
    sub main
        /declare myArray[9] int local 0
        /declare myCounter int local

        /echo =============[Put Data]=================
        /for myCounter 1 to ${myArray.Size}
            /varset myArray[${myCounter}] ${Math.Rand[999]}
            /echo Put a random number in Index ${myCounter} of myArray
        /next myCounter

        /echo =============[Get Data]=================
        /for myCounter 1 to ${myArray.Size}
            /echo Index ${myCounter} in myArray is ${myArray[${myCounter}]}
        /next myCounter
    /return
    ```

