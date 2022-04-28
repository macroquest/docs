# MQ2EQIM:DataType:buddy

## Members

|  |  |
| :--- | :--- |
| [_int_](datatype-int.md) **Buddies** | Size of the buddy index (will not necessarily be equal to the number of buddies, but n in Buddy[n] will never exceed this number) |
| [_string_](datatype-string.md) **Name** | Buddy's name (may be fennin.Name or just Name, depending on how you added them) |
| [_string_](datatype-string.md) **Status** | "Removed from list", "Offline", "EQIM", "EQIM (AFK\)", "Unknown Status\(4\)", "Playing", "Playing \(AFK)" |
| [_int_](datatype-int.md) **StatusID** | Numeric representation of the above (0,1,2,3,4,5,6) |
| [_time_](datatype-time.md) **LastSeen** | Last time this buddy was on/seen |
| **To String** | Same as **Name** |

## See Also

* [Data Types](./)
* [Top-Level Objects](../top-level-objects/)
* [MQ2EQIM](../../plugins/discontinued-unsupported/mq2eqim.md)

