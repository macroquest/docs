# MQ2AutoSize

## Description

`This plugin will automatically shrink everyone within range down to minimum`<br>
`allowed size. They will automatically resize back to normal when they move`<br>
`out of range. (Current range is set at 50' - adjust with Range settings in INI)`<br>
`NOTE: These effects are CLIENT SIDE ONLY!`<br>

`You can find the latest version of MQ2AutoSize`[`here`](https://github.com/RedGuides/MQ2AutoSize)`.`

## Commands

`/autosize [on | off] - Toggles AutoSize functionality on/off`<br>
`/autosize [pc | npc | pets | mercs | mounts | corpse | everything | self ] [on | off] - Toggles   AutoSizing on/off for the specified type`<br>
`/autosize dist - Toggles distance-based vs Zonewide`<br>
`/autosize range ### - Sets range for distance checking`<br>
`/autosize [ sizepc | sizenpc | sizepets | sizemercs | sizemounts | sizecorpse | sizetarget | sizeself ]  ### (1-250)`<br>
`/autosize [help | status | autosave | save | load ]`<br>

## INI Entries

`[Config]`<br>
`AutoSave=off`<br>
`ResizePC=on`<br>
`ResizeNPC=off`<br>
`ResizePets=off`<br>
`ResizeMercs=off`<br>
`ResizeMounts=off`<br>
`ResizeCorpse=off`<br>
`ResizeSelf=off`<br>
`Range=50`<br>
`SizeDefault=1`<br>
`SizePC=1`<br>
`SizeNPC=1`<br>
`SizePets=1`<br>
`SizeMercs=1`<br>
`SizeMounts=1`<br>
`SizeCorpse=1`<br>
`SizeSelf=1`<br>

## Top-Level Object: ${AutoSize}

| **Type**                                              | **Member Name**  | **Description**                                            |
| :---------------------------------------------------- | :--------------- | :--------------------------------------------------------- |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Active**       | Whether the plugin is actively resizing something or not   |
| [_bool_](../../reference/data-types/datatype-bool.md) | **AutoSave**     | Whether the plugin should autosave or not                  |
| [_bool_](../../reference/data-types/datatype-bool.md) | **Enabled**      | Whether the plugin is enabled or not                       |
| [_int_](../../reference/data-types/datatype-int.md)   | **Range**        | Distance within which the plugin will resize enabled types |
| [_bool_](../../reference/data-types/datatype-bool.md) | **ResizeCorpse** | Whether the plugin should resize corpses or not            |
| [_bool_](../../reference/data-types/datatype-bool.md) | **ResizeMercs**  | Whether the plugin should resize mercanaries or not        |
| [_bool_](../../reference/data-types/datatype-bool.md) | **ResizeMounts** | Whether the plugin should resize mounts or not             |
| [_bool_](../../reference/data-types/datatype-bool.md) | **ResizeNPC**    | Whether the plugin should resize NPCs or not               |
| [_bool_](../../reference/data-types/datatype-bool.md) | **ResizePC**     | Whether the plugin should resize PCs or not                |
| [_bool_](../../reference/data-types/datatype-bool.md) | **ResizePets**   | Whether the plugin should resize pets or not               |
| [_bool_](../../reference/data-types/datatype-bool.md) | **ResizeSelf**   | Whether the plugin should resize self or not               |
| [_int_](../../reference/data-types/datatype-int.md)   | **SizeCorpse**   | Size of corpses                                            |
| [_int_](../../reference/data-types/datatype-int.md)   | **SizeMercs**    | Size of mercanaries                                        |
| [_int_](../../reference/data-types/datatype-int.md)   | **SizeMounts**   | Size of mounts                                             |
| [_int_](../../reference/data-types/datatype-int.md)   | **SizeNPC**      | Size of NPCs                                               |
| [_int_](../../reference/data-types/datatype-int.md)   | **SizePC**       | Size of PCs                                                |
| [_int_](../../reference/data-types/datatype-int.md)   | **SizePets**     | Size of pets                                               |
| [_int_](../../reference/data-types/datatype-int.md)   | **SizeSelf**     | Size of self                                               |
