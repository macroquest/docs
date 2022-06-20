---
tags:
   - plugin
---
# MQ2IRC

## Description

MQ2IRC is the plugin which provides the ability to connect to an IRC server from within EQ.

This is most commonly used as a method to exchange information between bots without going through the EQ servers. It's faster as well as safer.

## Commands

* [/i](commands/i.md)
* [/iconnect](commands/iconnect.md)
* [/istatus](commands/istatus.md)

## Top-Level Objects

* [_irc_](mq2irc-datatype-irc.md) [**Irc**](tlo-irc.md)

## Data Types

* [_irc_](mq2irc-datatype-irc.md) **irc**

## INI File

The MQ2IRC.ini creates a new section for every server that it connects to, and keeps your settings for future use. It also stores the last server connected to and its settings so that you may use _/iconnect_ to reconnect to that server quickly.
