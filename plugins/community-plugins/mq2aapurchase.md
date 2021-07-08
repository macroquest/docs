# MQ2AAPurchase

## Description

by demonstar55:

Mainly I wanted to have a plugin version of the include, but I wanted to make use of some new client functions exported to MQ2 \(so requires MQ2-20151122\)

It works similar to MQ2AASpend that you can get with some precompiled MQ2 releases, but is missing the "brute" feature.

Source at [https://github.com/mackal/MQ2AAPurchase](https://github.com/mackal/MQ2AAPurchase) zip download also included in this post, but the github will always be up-to-date.

You can find the latest version of MQ2AAPurchase [here](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=19869).

## Commands

`/aapurchase help -- List commands, aka this`  
`/aapurchase now -- start buying now`  
`/aapurchase add \"AA Name\" rank -- M for max instead of a rank`  
`/aapurchase bank # -- set the amount of points to bank`  
`/aapurchase load -- Reload INI`

## INI

`[MQ2AAPurchase_Settings]`  
`BankPoints=40`  
`AutoSpend=1`  
`[MQ2AAPurchase_List]`  
`1=New Tanaan Crafting Mastery|3`  
`2=Combat Stability|M`  
`3=General Sturdiness|M`  
\`\`

This says I want to start buying once I have 40 points banked and is on. It will buy up to rank 3 of New Tanaan Crafting Mastery, and will buy max ranks of Combat Stability and General Sturdiness.

It's worth noting that in the MQ2AAPurchase\_List section the order of entries is important, not the key, so you can just write a macro to build a INI, move entries around to the order you want without having to worry about changing the keys.

It will also try to spend all your points each time it is triggered \(like the skip option in the include\) so if that's not the behavior you want, you'll have to convince me I should add it :P

## See Also

* [Plugins](../../documentation/macroquest2-plugins.md)

