# MQ2FeedMe

## Description

**MQ2Feedme**, by s0rCieR, is a plugin which will eat/drink items that you specify, in order to keep your hunger/thirst above a certain level (and thus not eat your stat food).

* It can be found [here](https://macroquest2.com/phpBB3/viewtopic.php?t=11490). \*\*An updated version of the plugin, with a few changes, can be found in [this](https://macroquest2.com/phpBB3/viewtopic.php?t=11490&start=107) post by jaq.\*\*

## Commands

`/autodrink` - Force manual drinking.<br>
`/autodrink 0` - Turn off autodrinking.<br>
`/autodrink #` - Set thirst level. When ${Me.Thirst} is below this, the plugin will drink for you.<br>
`/autofeed` - Force manual feeding.<br>
`/autofeed 0` - Turn off autofeeding.<br>
`/autofeed #` - Set hunger level, below which the plugin will automatically eat for you.<br>

## INI File

This plugin stores its information in the file MQ2FeedMe.ini. This INI file contains a list of all the food/drink that should be consumed (see the sample INI in the first page of the plugin post).
