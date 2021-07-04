# TLO:Alert

TLO:Alert

## Members

|  |  |  |
| :--- | :--- | :--- |
| **Type** | **Member** | **Description** |
| [_AlertListType_](../data-types/datatype-alertlisttype.md) | **List\[\#\]** | Data on the Shared list |
|  |  |  |

## Sub members of TLO:Alert

|  |  |
| :--- | :--- |
| **Member** | **Description** |
| **.List\[\#\]** | Get the \#th item in List. Returns AlertListType |
| **.Size** | Returns count of alerts. |
|  |  |

## Usage

|  |  |
| :--- | :--- |
| **Command** | **Result** |
| '''Example 1: /alert add 1 Fippy | Add and alert entry for Fippy to Alert List 1 |
| '''/echo ${Alert\[1\].List\[0\].Name} | Output: \[MQ2\] Fippy |
| '''/echo ${Alert\[1\].List\[0\].Spawn.Race} | Output: \[MQ2\] Druid \(or whatever Class Fippy is\) |
| '''Example 2: /alert add 1 id ${Me.ID} | Add and alert entry using the Spawn ID. |
| '''/echo ${Alert\[1\].List\[0\].SpawnID} | Output: \[MQ2\] 12345 \(or whatever your spawned is\) |
| '''/echo ${Alert\[1\].Size} | Output: \[MQ2\] 1 \(or the number of alerts in alert list 1\) |
|  |  |

## See Also

* [Top-Level Objects](./)
* [Alert](../../commands/slash-commands/alert.md)

