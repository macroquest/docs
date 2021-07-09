# DataType:dzmember

This DataType contains information on the members of the current dynamic zone instance

## Members

| **Type** | **Member** | **Description** |
| :--- | :--- | :--- |
| [_bool_](datatype-bool.md) | **Flagged** | Returns true if the dzmember can successfully enter the dz. where x is either index or the name. |
| [_string_]() | **Name** | The name of the member |
| [_string_]() | **Status** | The status of the member - one of the following: Unknown, Online, Offline, In Dynamic Zone, Link Dead |
| \_\_[_string_]()\_\_ | **To String** | Same as **Name** |

