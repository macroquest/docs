**NOTE** This TLO has been changed to "KeyRing"

## Description

Used to get information about items on your Mount keyring.

The addition of this allows the item to be cast using /useitem

`  /useitem Abyssal Steed`

## Forms

|                                                              |                                            |
|--------------------------------------------------------------|--------------------------------------------|
| *[Mount](../data-types/datatype-mount.md)* **Mount\[**#**\]**      | Mount Name in slot 1 of your Mount Keyring |
| *[Mount](../data-types/datatype-mount.md)* **Mount\[**#**\].Name** | Mount Name in slot 1 of your Mount Keyring |
|                                                              |                                            |

## Access to Types

-   *[mount](../data-types/datatype-mount.md)*

## Examples

`   /echo ${Mount[1].Name} `

Outputs: \[MQ2\] Whirligig Flyer ... Displayes the first mount in your mount keyring

## See Also

-   [Top-Level Objects](top-level-objects.md)
-   [mount](../data-types/datatype-mount.md)


