TLO:AdvLoot

## Members

|                                          |                       |                                                   |
|------------------------------------------|-----------------------|---------------------------------------------------|
| **Type**                                 | **Member**            | **Description**                                   |
| *Advloot* | **LootingInProgress** | True/False if looting from ADVLoot is in progress |
| *Advloot* | **SList**             | Data on the Shared list                           |
| *Advloot* | **PList**             | Data on the Personal list                         |
| *Advloot* | **SCount**            | Item count from the Shared list                   |
| *Advloot* | **PCount**            | item count from the Personal list                 |
| *Advloot* | **SWantCount**        | Want count from the Shared list                   |
| *Advloot* | **PWantCount**        | Want count from the Personal list                 |
|                                          |                       |                                                   |

## Sub members of TLO:AdvLoot

|                  |                                                               |
|------------------|---------------------------------------------------------------|
| **Member**       | **Description**                                               |
| **.AlwaysGreed** | TRUE/FALSE if the "AG" option is on                           |
| **.AlwaysNeed**  | TRUE/FALSE if the "AN" option is on                           |
| **.AutoRoll**    | TRUE/FALSE if the "Always Roll" (IE Dice symbol) option is on |
| **.Greed**       | TRUE/FALSE if the "GD" option is on                           |
| **.IconID**      | returns an int - cred randyleo                                |
| **.Need**        | TRUE/FALSE if the "ND" option is on                           |
| **.Never**       | TRUE/FALSE if the "NV" option is on                           |
| **.No**          | TRUE/FALSE if the "NO" option is on                           |
| **.NoDrop**      | TRUE if the item is No Drop... FALSE if not                   |
| **.StackSize**   | Integer - list the amount of items in the stack               |
|                  |                                                               |

## Usage

|                                                                                 |                                                                                    |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| **Command**                                                                     | **Result**                                                                         |
| '''/echo ${AdvLoot.PList\[1\].Name}                                             | Output: \[MQ2\] Bone Chips                                                         |
| '''/echo there are ${AdvLoot.PCount} items in the personal loot list            | Output: \[MQ2\] there are 3 items in the personal lootlist                         |
| '''/echo the item in index 1 has a StackSize of ${AdvLoot.PList\[1\].StackSize} | Output: \[MQ2\] the item in index 1 has a StackSize of 2                           |
| '''/if (${AdvLoot.SList\[1\].Need}==TRUE) /command                              | if item 1 in the shared list has Need checked, do command                          |
| '''/echo ${AdvLoot.PList\[1\].NoDrop}                                           | Output: \[MQ2\]TRUE/FALSE                                                          |
| '''/echo the item in index 1 has a StackSize of ${AdvLoot.PList\[1\].StackSize} | Output: \[MQ2\] the item in index 1 has a StackSize of 2                           |
| '''/delay 10s !${ADVLoot.InProgress}                                            | will wait either 10 second or until ADVLoot is no longer in the process of looting |
|                                                                                 |                                                                                    |

` /if (!${AdvLoot.LootInProgress}) { `  
`  /echo its safe to loot`  
`  /if (${AdvLoot.SCount}>=1) {`  
`    /echo im going to give 1 ${AdvLoot.SList[1].Name} to myself`  
`    /advloot shared 1 giveto ${Me.Name} 1`  
`    }`  
`  } else {`  
`    /echo do something else, loot is in progress...`  
`  }`

## See Also

-   [Top-Level Objects](top-level-objects.md)


