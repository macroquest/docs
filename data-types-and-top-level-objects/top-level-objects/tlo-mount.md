# TLO:Mount

**NOTE** This TLO has been changed to "KeyRing"

## Description

Used to get information about items on your Mount keyring.

The addition of this allows the item to be cast using /useitem

`/useitem Abyssal Steed`

## Forms

|  |  |
| :--- | :--- |
| [_Mount_](../data-types/datatype-keyring.md) **Mount\[**\#**\]** | Mount Name in slot 1 of your Mount Keyring |
| [_Mount_](../data-types/datatype-keyring.md) **Mount\[**\#**\].Name** | Mount Name in slot 1 of your Mount Keyring |
|  |  |

## Access to Types

* [_mount_](../data-types/datatype-keyring.md)

## Examples

`/echo ${Mount[1].Name}`

Outputs: \[MQ2\] Whirligig Flyer ... Displayes the first mount in your mount keyring

## See Also

* [Top-Level Objects](./)
* [mount](../data-types/datatype-keyring.md)

