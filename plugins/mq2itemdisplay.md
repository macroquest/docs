## Description

This plugin shows spell and item data in the item display window.

(MQ2GearScore has since been merged with MQ2itemdisplay)

## Commands

**[/inote](../commands/inote.md) \<add\|del> \<item#\> "Comment"** Add/delete a note to a specific item number. This
information will be displayed within the item info window, under all the other information.

`GearScore Commands`

|                                    |                                                                                                                                |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **Command**                        | **Description**                                                                                                                |
| ''/iScore                          | Show the current values                                                                                                        |
| ''/iScore clear                    | reset all values to default zeros                                                                                              |
| ''/iScore click \[channel\]        | toggles auto clicking links shown in \[group\|guild\|raid\|any\]                                                               |
| ''/iScore cursor                   | evaluates the item on the cursor                                                                                               |
| ''/iScore report \[channel\]       | if set to an channel the plugin will auto report upgrades. Suggest /bc                                                         |
| ''/iScore \[Attribute\] \[Weight\] | \[Attribute\] is one of the following HP, Mana, AC , hSTR, hINT, hWIS, hAGI, hDEX, hSTA, hCHA, Heal, Nuke, Clairvoyance, Ratio |
|                                    |                                                                                                                                |

### Command Examples

Examples using GearScore

On a warrior I might use the following:

-   /iScore HP 1
-   /iScore AC 10
-   /iScore hSTA 15
-   /iScore hAGI 50
-   /iScore Ratio 1000

On a healer I might use the following:

-   /iScore HP 1
-   /iScore Mana 1
-   /iScore hWIS 15
-   /iScore hSTA 10
-   /iScore Heal 50

Example Gearscore Output: When you look at an items details there will be extra lines at the bottom that look like:

-   Base Item Score : 2222
-   Worn Item Score : 3333 (Keep Left Finger)
-   Worn Item Score : 1111 (UPGRADE Right Finger)
-   WEAR \[ uber ring \] as Right Finger = 200.0% = +10 AC +110 HP -1 hDex

When you click on an augment it will show you the value of all the slots it will fit into.

*Example: White Dragon Scale Score : 455*

-   Left Ear = Bayle's Heraldic Crest : 395 UPGRADE
-   Head = Ksathrax's Amber : 440 UPGRADE
-   WEAR \[White Dragon Scale\] as Left Ear = 12.6% = +2 AC +15 HP +1 hDex

## Top-Level Objects

-   *[item](../data-types/datatype-item.md)* **DisplayItem**

  
This references the last item display window that was opened.

### ${GearScore}

|                                        |                  |                                                        |
|----------------------------------------|------------------|--------------------------------------------------------|
| **Type**                               | **Member**       | **Description**                                        |
| *[bool](../data-types/datatype-bool.md)*     | **${GearScore}** | True if the plugin is loaded                           |
| *[string](../data-types/datatype-string.md)* | **Upgrade**      | Returns the same string as you see in the item display |
| *[string](../data-types/datatype-string.md)* | **UpgradeName**  | Returns the item name                                  |
| *[int](../data-types/datatype-int.md)*       | **UpgradeSlot**  | Returns the item slot                                  |
|                                        |                  |                                                        |

### TLO Examples

Example: looking at "Aragus Tactics" on my character I get:

-   /echo ${GearScore.Upgrade} -> WEAR \[ Aragus Tactics \] as Charm = +24.9% = AC +43 HP +733 ....
-   /echo ${GearScore.UpgradeName} -> Aragus Tactics
-   /echo ${GearScore.UpgradeSlot} -> Charm

## INI File

All the /inote information is stored in the MQ2ItemDisplay.ini file in the following format:

    [Notes]
    0019542=This is found on the Great Saprophyte in EC<nowiki><br></nowiki>Rarity is about 1 in 5

The \<br> tag can be used to insert a line break. Sometimes it is easier to edit the file itself rather than type the
whole string from within the game (also makes copying and pasting easier). The INI file is re-read every time the item
display window is opened, so changes take effect immediately.

## Example

In the following example, the line is broken into 4 for readability, in the MQ2ItemDisplay.ini file, it would all be 1
line.

`0017910=<br>Field.....Round....Large....Wood....16<br>Field.....Round....Medium.Wood...36<br>Field.....Parab.....Large....Wood...46<br>Field.....Round....Small...Wood....56<br>Field.....Round....Large...Bone.....68<br>Field.....Shield....Large...Wood....82<br>Hooked.Round....Large...Wood....102<br>Field.....Wood*...Large...Wood....122<br>Field.....Round....Large..Ceramic.135<br>Field.....Bone*....Large..Wood.....162<br>Silver....Round....Large..Wood.....182<br>Field....`  
`Ceramic*.Large..Wood.....202`

The info displayed would look like this:  
:**Note:  
Field.....Round....Large....Wood....16  
Field.....Round....Medium.Wood...36  
Field.....Parab.....Large....Wood...46  
Field.....Round....Small...Wood....56  
Field.....Round....Large...Bone.....68  
Field.....Shield....Large...Wood....82  
Hooked.Round....Large...Wood....102  
Field.....Wood\*...Large...Wood....122  
Field.....Round....Large..Ceramic.135  
Field.....Bone\*....Large..Wood.....162  
Silver....Round....Large..Wood.....182  
Field....Ceramic\*.Large..Wood.....202**

## See Also

-   [Top-Level Objects](../top-level-objects/top-level-objects.md)
-   [Plugins](../documentation/macroquest2-plugins.md)

See [here](https://macroquest2.com/phpBB3/viewtopic.php?t=11549) and
[here](https://macroquest2.com/phpBB3/viewtopic.php?t=12022) (VIP only) for some user-contributed ini
file entries.


