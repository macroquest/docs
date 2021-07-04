# MQ2Timestamp

## Description

**MQ2Timestamp** Inserts a timestamp into incoming chat.

You can find the latest version of MQ2Clip [here](https://macroquest2.com/phpBB3/viewtopic.php?f=31&t=9078&hilit=mq2timestamp).

## Commands

Usage: /timestamp \[ help\| on \| off \| reload \| default \| format  \| loc \ \| maxlen  \]

`help - displays usage information`  
`on/off - enables/disables timestamps`  
`reload - reloads the ini file`  
`default - resets your format to default(only changeable via ini)`  
`format - sets your timestamp format to`  
`loc - sets timestamp location: 0-append, 1-prepend`  
`maxlen - sets the maximum length of parsed timestamp.`

Will toggle on/off with no arguments

## INI Entries

* The config section is optional.
* It lets you overwrite the hard coded defaults.

`[Config]`  
`Default=Format`  
`MaxLength=<maximum length of formatted time to be returned`  
`UseTimestamps=< greater than 0 is on, 0 or less is off >`

* Default will overwrite the hardcoded default of "\[%H:%M:%S\]" with Format.
* MaxLength will trim the timestamp to this value.
* UseTimestamps, nuff said :p
* The custom timestamps are stored in server sections by character.
* \[Server\]
* Character=Loc,Format
* Server, Character shouldn't require explanation
* Loc indicates where the timestamp will be added to chat.
* 0 appends the timestamp and 1 will prepend it.
* Format is the custom timestamp for that character.

## Sample MQ2Timestamp.ini

`[Config]`  
`Default=%I:%M:%S:%p>`  
`MaxLength=20`  
`UseTimestamps=1`  
`[Eci]`  
`Soandso=0,[%H:%M]`

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

* Format reference: Format consists of one or more codes.
* The codes are preceded by a percent sign \(%\).
* Characters that do not begin with % are copied unchanged.
* 
`%a - Abbreviated weekday name`  
`%A - Full weekday name`  
`%b - Abbreviated month name`  
`%B - Full month name`  
`%c - Date and time representation appropriate for locale`  
`%d - Day of month as decimal number (01 – 31)`  
`%H - Hour in 24-hour format (00 – 23)`  
`%I - Hour in 12-hour format (01 – 12)`  
`%j - Day of year as decimal number (001 – 366)`  
`%m - Month as decimal number (01 – 12)`  
`%M - Minute as decimal number (00 – 59)`  
`%p - Current locale's A.M./P.M. indicator for 12-hour clock`  
`%S - Second as decimal number (00 – 59)`  
`%U - Week of year as decimal number, with Sunday as first day of week (00 – 53)`  
`%w - Weekday as decimal number (0 – 6; Sunday is 0)`  
`%W - Week of year as decimal number, with Monday as first day of week (00 – 53)`  
`%x - Date representation for current locale`  
`%X - Time representation for current locale`  
`%y - Year without century, as decimal number (00 – 99)`  
`%Y - Year with century, as decimal number`  
`%z, %Z - Time-zone name or abbreviation; no characters if time zone is unknown`  
`%% - Percent sign`

`Special formating:`  
`%#c - Long date and time representation, appropriate for current locale. For example: "Tuesday, March 14, 1995, 12:41:29".`  
`%#x - Long date representation, appropriate to current locale. For example: "Tuesday, March 14, 1995".`  
`%#d, %#H, %#I, %#j, %#m, %#M, \`  
`%#S, %#U, %#w, %#W, %#y, %#Y - Remove leading zeros (if any).`

## See Also

* [Plugins](../../documentation/macroquest2-plugins.md)

