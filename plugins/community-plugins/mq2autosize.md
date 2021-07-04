# MQ2AutoSize

## Description

`This plugin will automatically shrink everyone within range down to minimum`  
`allowed size. They will automatically resize back to normal when they move`  
`out of range. (Current range is set at 50' - adjust with Range settings in INI)`  
`NOTE: These effects are CLIENT SIDE ONLY!`

`You can find the latest version of MQ2AutoSize`[`here`](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=12808&hilit=MQ2AutoSize)`.`

## Commands

`/autosize - Toggles AutoSizing on/off`  
`/autosizeall - Toggles AutoSizing for whole zone`  
`/autosize [pc | npc | pets | mercs | mounts | corpse | target | everything | self ]`  
`/autosize dist - Toggles distance based AutoSize on/off`  
`/autosize range ### - Sets range for distance checking`  
`/autosize [ size | sizepc | sizenpc | sizepets | sizemercs | sizemounts | sizecorpse | sizetarget | sizeself ] ### (1-250)`  
`/autosize [help | status | autosave | save | load }`

## INI Entries

`[Config]`  
`AutoSave=off`  
`ResizePC=on`  
`ResizeNPC=off`  
`ResizePets=off`  
`ResizeMercs=off`  
`ResizeAll=off`  
`ResizeMounts=off`  
`ResizeCorpse=off`  
`ResizeSelf=off`  
`SizeByRange=off`  
`Range=50`  
`SizeDefault=1`  
`SizePC=1`  
`SizeNPC=1`  
`SizePets=1`  
`SizeMercs=1`  
`SizeTarget=1`  
`SizeMounts=1`  
`SizeCorpse=1`  
`SizeSelf=1`

## See Also

* [Plugins](../../documentation/macroquest2-plugins.md)

