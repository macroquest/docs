## Introduction

This DataType performs a simple test on *n* using the following members.

## Members

| **Type**                           | **Member**                   | **Description**                                                     |
|------------------------------------|------------------------------|---------------------------------------------------------------------|
| *[Bool](datatype-bool.md)* | **Between\[***#1,#2:*'n*\]*' | is ***n*** Between the range of *#1* and *#2* both numbers included |
| *[Bool](datatype-bool.md)* | **Inside\[***#1,#2:*'n*\]*'  | is ***n*** Inside the range of *#1* and *#2* both numbers excluded  |
|                                    |                              |                                                                     |

## Examples

### .Between

/echo Is 50 between 33 and 66?: ${Range.Between\[33,66:50\]}

`Is 50 between 33 and 66?: TRUE`

/echo Is 25 between 33 and 66?: ${Range.Between\[33,66:25\]}

`Is 25 between 33 and 66?: FALSE`

### .Inside

/echo Is 50 Inside 33 and 66?: ${Range.Inside\[33,66:50\]}

`Is 50 Inside 33 and 66?: TRUE`

/echo Is 33 inside 33 and 66?: ${Range.Inside\[33,66:33\]}

`Is 33 between 33 and 66?: FALSE`

## See Also

-   [Data Types](data-types.md)
-   [TLO:Range](../top-level-objects/tlo-range.md)


