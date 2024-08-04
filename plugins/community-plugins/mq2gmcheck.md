# MQ2GMCheck

## Description

**MQ2GMCheck** Created by Bushdaka

Check to see if a GM is in the zone. This is not fool proof. It is absolutely true that a GM could be right in front of you and you'd never know it. This plugin will simply find those who are in the zone and not gm-invis, or who just came into the zone and were not gm-invised at the time. If a GM comes into the zone already gm-invised, we will not know about that.

You can find the latest version of MQ2GMCheck [here](https://macroquest2.com/phpBB3/viewtopic.php?f=50&t=11140&hilit=MQ2GMCheck).

## Commands

`/gmcheck on|off` - enable/disable scanning for GMs<br>
`/gmcheck char on|off` - toggle chat channel alert<br>
`/gmcheck chattimer X` - set frequency of chant channel alert, default=15s<br>
`/gmcheck popup on|off` - toggle popup alert<br>
`/gmcheck popuptimer X` - set frequency of popup alert, default is 30s<br>
`/gmcheck audio on|off` - toggle audio alert<br>
`/gmcheck audiotimer X` - set frequency of audio alert, default is 30s<br>
`/gmcheck list` - list all known GMs currently in zone<br>
`/gmcheck reset` - reset list of known GMs in zone<br>
`/gmcheck history` - complete history dump<br>
`/gmcheck zone` - history of GMs in this zone<br>
`/gmcheck server` - history of GMs on this server<br>
`/gmcheck servers` - history of GMs on all servers<br>
`/gmcheck timer X` - set scan delay to X seconds, default is 2s<br>
`/gmcheck help` - show the available commands<br>

## Top-Level Object: ${GMCheck}


| **Type**                                              | **Member Name**  | **Description**                                            |
| :---------------------------------------------------- | :--------------- | :--------------------------------------------------------- |
| [_string_](../../reference/data-types/datatype-string.md) | **${GMCheck}** | returns TRUE, FALSE, or DISABLED. |
| [_string_](../../reference/data-types/datatype-string.md) | **Status** | returns TRUE, FALSE, or DISABLED. |
| [_int_](../../reference/data-types/datatype-int.md) | **Count** | returns the number of GMs known in this zone. |

audio - put an entry for GMCHECK in the MQ2Sound.ini
