# DataType:range

This DataType performs a simple test on _n_ using the following members.

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_](datatype-bool.md) | **Between\[**\#1,\#2:_n_\] | is _**n**_ Between the range of _\#1_ and _\#2_ both numbers included |
| [_bool_](datatype-bool.md) | **Inside\[**\#1,\#2:_n_\] | is _**n**_ Inside the range of _\#1_ and _\#2_ both numbers excluded |

## Examples

### .Between

/echo Is 50 between 33 and 66?: ${Range.Between\[33,66:50\]}

`Is 50 between 33 and 66?: TRUE`

/echo Is 25 between 33 and 66?: ${Range.Between\[33,66:25\]}

`Is 25 between 33 and 66?: FALSE`

### .Inside

/echo Is 50 Inside 33 and 66?: ${Range.Inside\[33,66:50\]}

`Is 50 Inside 33 and 66?: TRUE`

/echo Is 33 inside 33 and 66?: ${Range.Inside\[33,66:33\]}

`Is 33 between 33 and 66?: FALSE`

