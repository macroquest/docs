# MQ2GMCheck

## Description

**MQ2GMCheck** Created by Bushdaka

Check to see if a GM is in the zone. This is not fool proof. It is absolutely true that a GM could be right in front of you and you'd never know it. This plugin will simply find those who are in the zone and not gm-invis, or who just came into the zone and were not gm-invised at the time. If a GM comes into the zone already gm-invised, we will not know about that.

You can find the latest version of MQ2GMCheck [here](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=11140&hilit=MQ2GMCheck).

## Commands

`/gmcheck on|off - enable/disable scanning for GMs`  
`/gmcheck char on|off - toggle chat channel alert`  
`/gmcheck chattimer X - set frequency of chant channel alert, default=15s`  
`/gmcheck popup on|off - toggle popup alert`  
`/gmcheck popuptimer X - set frequency of popup alert, default is 30s`  
`/gmcheck audio on|off - toggle audio alert`  
`/gmcheck audiotimer X - set frequency of audio alert, default is 30s`  
`/gmcheck list - list all known GMs currently in zone`  
`/gmcheck reset - reset list of known GMs in zone`  
`/gmcheck history - complete history dump`  
`/gmcheck zone - history of GMs in this zone`  
`/gmcheck server - history of GMs on this server`  
`/gmcheck servers - history of GMs on all servers`  
`/gmcheck timer X - set scan delay to X seconds, default is 2s`  
`/gmcheck help - show the available commands`

## Datatype

`${GMCheck} returns TRUE, FALSE, or DISABLED.`  
`${GMCheck.Status} returns TRUE, FALSE, or DISABLED.`  
`${GMCheck.Count} returns the number of GMs known in this zone.`

audio - put an entry for GMCHECK in the MQ2Sound.ini

## See Also

* [Plugins](../../documentation/macroquest2-plugins.md)

