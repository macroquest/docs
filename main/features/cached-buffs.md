## Cached Buffs


-Previously Added: .CachedBuffCount to the spawn tlo. it returns -1 if no buffs are cached for the spawn or number of buffs cached.

-Previously Added: .CachedBuff[x] to the spawn tlo where x is a spellid if its a number and a spell name if not. It returns a MQ2CachedBuffType.

-Previously Added: .CachedBuff[\#x] to the spawn tlo where \#x is a buffslot between 1-97. It returns a MQ2CachedBuffType.

-Previously Added: .CachedBuff[\*x] to the spawn tlo where \*x is a index (buffslots are not sorted). It returns a MQ2CachedBuffType.

-Previously Added: .CachedBuff[^x] to the spawn tlo where ^x is a keyword. It returns a MQ2CachedBuffType.

`^x keywords: Slowed Rooted Mezzed Crippled Maloed Tashed Snared and Beneficial`

-Using CachedBuff to get buff info on targets, group members etc, only requires you to target the entity once. after thats done, buffs are cached. The upside is obviously that we don't have to target back and forth constantly.

### Examples

`${Group.Member[2].CachedBuff[Spirit of Wolf].Duration}`

This will show the duration of the spirit of wolf on the second member of the group.

`${Target.Clarity.Name}`

This will show you the name of the clarity spell on your target

`/cachedbuffs reset`

This will clear the cached buffs for all targets.

For more information on the `/cachedbuffs` command see [here](../../../reference/commands/cachedbuffs/).

For more information on the `cachedbuff` datatype see [here](../../../reference/data-types/datatype-cachedbuff/)
