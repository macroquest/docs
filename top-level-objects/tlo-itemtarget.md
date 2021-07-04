## Description

ItemTarget *We used to allow targeting of ground spawn but then sony started sending a packet that would be a give
away.*  
*So I added ItemTarget which is still a spawn but the ID is always 0, e.g. untargetable.*  
*- dont_know_at_all*

-   To check that you have a valid ground spawn targeted, use **${ItemTarget.Race.ID}**
-   Non-zero values indicate the DropID of the item.

## Access to Types

-   *[spawn](../data-types/datatype-spawn.md)* **spawn**

## See Also

-   [Top-Level Objects](top-level-objects.md)


