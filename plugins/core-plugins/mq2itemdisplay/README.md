---
tags:
   - plugin
---
# MQ2ItemDisplay

## Description

This plugin shows spell and item data in the item display window.

\(MQ2GearScore has since been merged with MQ2itemdisplay\)

## Commands

[**/inote**](inote.md)   **"Comment"** Add/delete a note to a specific item number. This information will be displayed within the item info window, under all the other information.

### 

## Top-Level Objects

* [_item_](../../../reference/data-types/datatype-item.md) **DisplayItem**

This references the last item display window that was opened.

## INI File

All the /inote information is stored in the MQ2ItemDisplay.ini file in the following format:

```text
[Notes]
0019542=This is found on the Great Saprophyte in EC<nowiki><br></nowiki>Rarity is about 1 in 5
```

The `<br>` tag can be used to insert a line break. Sometimes it is easier to edit the file itself rather than type the whole string from within the game \(also makes copying and pasting easier\). The INI file is re-read every time the item display window is opened, so changes take effect immediately.

## Example

In the following example, the line is broken into 4 for readability, in the MQ2ItemDisplay.ini file, it would all be 1 line.

`0017910<br>Field.....Round....Large....Wood....16<br>Field.....Round....Medium.Wood...36<br>Field.....Parab.....Large....Wood...46<br>Field.....Round....Small...Wood....56<br>Field.....Round....Large...Bone.....68<br>Field.....Shield....Large...Wood....82<br>Hooked.Round....Large...Wood....102<br>Field.....Wood*...Large...Wood....122<br>Field.....Round....Large..Ceramic.135<br>Field.....Bone*....Large..Wood.....162<br>Silver....Round....Large..Wood.....182<br>Field....Ceramic*.Large..Wood.....202`

The info displayed would look like this:  
**Note:  
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

See [here](https://macroquest.org/phpBB3/viewtopic.php?t=11549) and [here](https://macroquest.org/phpBB3/viewtopic.php?t=12022) \(VIP only\) for some user-contributed ini file entries.

