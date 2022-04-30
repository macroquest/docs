# DataType:float

Contains all information related to floating point numbers

* A floating-point number is one which has a decimal component (_e.g._ **1.01**)
* Members of this DataType generally manipulate the number's precision (_i.e._ how many decimal places)
* They all round correctly with the exception of _int_

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_string_](datatype-string.md) | **Deci** | The number as a string with **one** place of precision, _i.e._ \#\#\#.\# |
| [_string_](datatype-string.md) | **Centi** | The number as a string with **two** places of precision, _i.e._ \#\#\#.\#\# |
| [_int_](datatype-int.md) | **Int** | Integer portion of the number truncated rather than rounded, _e.g._ 12.779 returns 12 |
| [_string_](datatype-string.md) | **Milli** | The number as a string with **three** places of precision, _i.e._ \#\#\#.\#\#\# |
| [_string_](datatype-string.md) | **Precision[**\#**]** | The number as a string with \# places of precision |
| [_string_](datatype-string.md) | **To String** | Same as **Centi** |

