# Updateitems

## Status

This command is currently disabled. Typing /updateitems will report: "This command is disabled since the itemdb is maintained by the devs."

## Syntax

**/updateitems**

## Description

Scans your inventory and bank and collects item IDs and names. The information is placed in ItemDB.txt which is created if it does not already exist.

### Purpose

* The original purpose was to generate item numbers for a database project like lucy. \*\*This command is now

  obsolete.\*\*

### How it Works

1. ItemDB.txt is read upon startup of MQ2 and the contents are stored in memory while it is running.
2. If you issue the /updateitems command, MQ2 scans your inventory and bank and collects item IDs and names.
3. Those IDs and names are added to the aforementioned list stored in memory.
4. The resulting list is then written to ItemDB.txt.

### Notes

* If you want a list of your current assets, delete ItemDB.txt before you start MQ2
* Don't forget to delete it and restart MQ2 each time you want to refresh that list.

[Return to Slash Commands](./)

