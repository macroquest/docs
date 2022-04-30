# TLO:Alert

Provides access to alerts. See [/alert](../../reference/commands/alert.md).

## Forms

| Type | Form | Description |
| :--- | :--- | :--- |
| [_alert_](tlo-alert.md#alert-type) | **Alert**[ _#_ ] | Alt Ability by number |
| [_string_](../data-types/datatype-string.md) | **Alert** | Returns pipe "\|" separated list of alert ids |

## Alert Type

| Type | Name | Description |
| :--- | :--- | :--- |
| [_alertlist_](../data-types/datatype-alertlisttype.md) | **List[**\#**]** | Get the #th item in the list |
| [_int_](../data-types/datatype-int.md) | **Size** | Get the number of alerts |
| [_string_](../data-types/datatype-string.md) | **To String** | Same as **Size**. |

## Usage

| **Command** | **Result** |
| :--- | :--- |
| `/alert add 1 Fippy` | Add and alert entry for Fippy to Alert List 1 |
| `/echo ${Alert[1].List[0].Name}` | Output: Fippy |
| `/alert add 1 id ${Me.ID}` | Add and alert entry using the Spawn ID. |
| `/echo ${Alert[1].List[0].SpawnID}` | Output: 12345 (or whatever your spawned is) |
| `/echo ${Alert[1].Size}` | Output: 1 (or the number of alerts in alert list 1) |

