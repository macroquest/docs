# RDCommon.ini

RDCommon.ini is a bot-independent .ini file for [AutoBot.mac](https://macroquest2.com/phpBB3/viewtopic.php?t=12712)\(AutoBot documentation [here](https://macroquest2.com/wiki/index.php/AutoBot.mac)\). It will mostly handle itself. But it can be very useful to add your own settings here for spells not to cast ina given zone \(mez in PoK or the Guild Lobby/Hall, for example\).

## Possible settings

**\[ImmuneList\]** _This section describes immunities on a per spellID basis._  
**5520Immune=\|Gelidran Icekeeper\|** _5520 is the spellID for Euphoria. the Gelidran Icekeeper is immune to it. Autobot won't ever cast Euphoria at that mob. Also useful for excluding certain spells from certain mobs. Autobot will automatically add mobs here that give an immune message to any given spell._  
**\[RestrictedList\]** _This section describes things not to do in a given zone._  
**GukTop=\|3185\|NoMount\|** _In Upper Guk, don't cast Flight of Eagles and don't use a mount. It is possible that you CAN'T use a mount and or cast FoE in Upper Guk, this section simply says AUtoBot Won't do that. This is also updated automagically based on in-game messages._  
**\[Settings\]**  
**Version=4.5** _Current AutoBot version. To force a rebuild of AB Aliases, set this value to 0._

