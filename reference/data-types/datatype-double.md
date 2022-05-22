---
tags:
    - datatype
---

# `double` Type

Represents a double precision (64-bit) floating point number.

* A floating-point number is one which has a decimal component (_e.g. 1.01_)
* Members of this DataType generally manipulate the number's precision (_i.e. how many decimal places_)
* They all round correctly with the exception of _int_

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_string_](datatype-string.md) | **Deci** | The number as a string with **one** place of precision, _i.e. ###.#_ |
| [_string_](datatype-string.md) | **Centi** | The number as a string with **two** places of precision, _i.e. ###.##_ |
| [_int_](datatype-int.md) | **Int** | Integer portion of the number truncated rather than rounded, _e.g. 12.779 returns 12_ |
| [_string_](datatype-string.md) | **Milli** | The number as a string with **three** places of precision, _i.e. ###.###_ |
| [_string_](datatype-string.md) | **Precision**[_#_] | The number as a string with # places of precision |
| [_string_](datatype-string.md) | **Prettify**[_precision_] | Pretty print the number with commas, with optional _precision_ (defaults to two decimal points). |
| [_string_](datatype-string.md) | **To String** | Same as **Centi** |
