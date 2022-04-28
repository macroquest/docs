# TLO:Alert

Provides access to alerts. See also: [/alert](../../commands/slash-commands/alert.md).

## Forms

| Type | Form | Description |
| :--- | :--- | :--- |
| \_\_[_alert_](tlo-alert.md#alert-type)\_\_ | **Alert[**\#**]** | Alt Ability by number |
| \_\_[_string_](../data-types/datatype-string.md)\_\_ | **Alert** | Returns pipe "\|" separated list of alert ids |

## Alert Type

| Type | Name | Description |
| :--- | :--- | :--- |
| \_\_[_alertlist_](../data-types/datatype-alertlisttype.md)\_\_ | **List[**\#**]** | Get the \#th item in the list |
| \_\_[_int_](../data-types/datatype-int.md)\_\_ | **Size** | Get the number of alerts |
| \_\_[_string_](../data-types/datatype-string.md)\_\_ | **To String** | Same as **Size**. |

## Usage

| **Command** | **Result** |
| :--- | :--- |
| `/alert add 1 Fippy` | Add and alert entry for Fippy to Alert List 1 |
| `/echo ${Alert[1].List[0].Name}` | Output: Fippy |
| `/alert add 1 id ${Me.ID}` | Add and alert entry using the Spawn ID. |
| `/echo ${Alert[1].List[0].SpawnID}` | Output: 12345 (or whatever your spawned is) |
| `/echo ${Alert[1].Size}` | Output: 1 (or the number of alerts in alert list 1) |

