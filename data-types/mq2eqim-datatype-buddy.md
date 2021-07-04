## Members

|                                                   |                                                                                                                                     |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| *[int](datatype-int.md)* **Buddies**      | Size of the buddy index (will not necessarily be equal to the number of buddies, but n in Buddy\[n\] will never exceed this number) |
| *[string](datatype-string.md)* **Name**   | Buddy's name (may be fennin.Name or just Name, depending on how you added them)                                                     |
| *[string](datatype-string.md)* **Status** | "Removed from list", "Offline", "EQIM", "EQIM (AFK)", "Unknown Status(4)", "Playing", "Playing (AFK)"                               |
| *[int](datatype-int.md)* **StatusID**     | Numeric representation of the above (0,1,2,3,4,5,6)                                                                                 |
| *[time](datatype-time.md)* **LastSeen**   | Last time this buddy was on/seen                                                                                                    |
| **To String**                                     | Same as **Name**                                                                                                                    |

## See Also

-   [Data Types](data-types.md)
-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [MQ2EQIM](../plugins/mq2eqim.md)


