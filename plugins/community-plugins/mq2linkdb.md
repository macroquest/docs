# MQ2LinkDB

## Description

MQ2LinkDB allows you to keep your own personalised database of item links. There are two versions of the plugin:

* **v1:** The original, by Ziggy is available [here](https://macroquest.org/phpBB3/viewtopic.php?t=10375&start=0)

* **v2:** An updated version of the plugin, which includes a TLO and linkbot functionality, was created by rswiders and is available in the VIP Forums [here](https://macroquest.org/phpBB3/viewtopic.php?t=14876)

### Features

* Able to import the huge database of links from [http://eqitems.13th-floor.org/](http://eqitems.13th-floor.org/) and add them.
* Watch chat for item links and add them automatically.
* Links are returned as tells and will go into the tell window. They do not go into your log file, nor does LinkDB show up when you try and reply.

## Commands
`/link` - Display statistics

`/link /import` - Import items.txt as downloaded from [13th-Floor](http://eqitems.13th-floor.org/download.php). To import this file, do the following:

1. Download the items.zip file directly using [this link](http://eqitems.13th-floor.org/download/items.zip)<br>
2. Unzip the items.txt file to the \Release directory<br>
3. In game, type /link /import and wait a few seconds for the items to be added<br>
4. Out of game, edit the MQ2LinkDB.txt file and: 1. Remove the first line (ends in "wornlevel") 2. Search for "iksar left hand" and delete the 3 lines that end in '=\<br>
`/link /max #` - Set maximum number of results (default 10)<br>
`/link [_search-string_]` - Find items containg _search-string_<br>

### Added by v2
`/link /scan [on|off]` - Turn on and off scanning incoming chat<br>
`/link /click [on|off]` - Click on the link generated?

## Top-Level Object: ${LinkDB}

**Note:** The TLO is only available in v2.

| **Type**                                              | **Member Name**  | **Description**                                            |
| :---------------------------------------------------- | :--------------- | :--------------------------------------------------------- |
| [_string_](../../reference/data-types/datatype-string.md) | **${LinkDB[_name_]}** | Display the link found by _name_. use _=name_ for an exact match |

## Examples

`/link baby joseph sayer` - You will get a tell with a link to the Baby Joseph Sayer.

`/shout OMG I'm a dork! I have ${LinkDB[=Baby Joseph Sayer]} in my pack. Ha!` - If the item is not found, the TLO returns an empty string, so you probably don't want to be directly shouting about Baby Joseph Sayer in your backpack. If you do and misspell his name, you will end up shouting about an empty string which isn't recommended.
