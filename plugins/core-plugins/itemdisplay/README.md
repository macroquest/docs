---
tags:
   - plugin
---
# ItemDisplay
<!--desc-start-->
This plugin shows spell information and item data in their respective display windows. It can also show custom notes. 
<!--desc-end-->

## Commands

<a href="itemdisplay/">
{% 
  include-markdown "plugins/core-plugins/itemdisplay/itemdisplay.md" 
  start="<!--cmd-syntax-start-->" 
  end="<!--cmd-syntax-end-->" 
%}
</a>
:    {% include-markdown "plugins/core-plugins/itemdisplay/itemdisplay.md"
        start="<!--cmd-desc-start-->" 
        end="<!--cmd-desc-end-->" 
        trailing-newlines=false 
     %} {{ readMore('plugins/core-plugins/itemdisplay/itemdisplay.md') }}

<a href="inote/">
{% 
  include-markdown "plugins/core-plugins/itemdisplay/inote.md" 
  start="<!--cmd-syntax-start-->" 
  end="<!--cmd-syntax-end-->" 
%}
</a>
:    {% include-markdown "plugins/core-plugins/itemdisplay/inote.md"
        start="<!--cmd-desc-start-->" 
        end="<!--cmd-desc-end-->" 
        trailing-newlines=false 
     %} {{ readMore('plugins/core-plugins/itemdisplay/inote.md') }}

## INI File

Settings can be configured via GUI as well with the [mqsettings](../../../reference/commands/mqsettings.md) command.

```ini
[Notes]
; section for item notes
0014905=mushroom makes me feel good
; this is a note I made for the item "Mushroom" id 0014905, which will appear in the item display window. It's helpful to remember this fact! 
[Settings]
LootButton=1
; the loot button is on
LucyButton=1
; the lucy button is on, too
ShowSpellInfoOnSpells=0
; Toggle extra info on the spell window
ShowSpellsInfoOnItems=0
; Toggle extra info on item window
```

## Top-Level Objects

## [DisplayItem](tlo-displayitem.md)
{%
  include-markdown "plugins/core-plugins/itemdisplay/tlo-displayitem.md"
  start="<!--tlo-desc-start-->"
  end="<!--tlo-desc-end-->"
  trailing-newlines=false
%} {{ readMore('plugins/core-plugins/itemdisplay/tlo-displayitem.md') }}

<h2>Forms</h2>
{%
  include-markdown "plugins/core-plugins/itemdisplay/tlo-displayitem.md"
  start="<!--tlo-forms-start-->"
  end="<!--tlo-forms-end-->"
  heading-offset=0
%}
{% 
  include-markdown "plugins/core-plugins/itemdisplay/tlo-displayitem.md" 
  start="<!--tlo-linkrefs-start-->"
  end="<!--tlo-linkrefs-end-->"
%}

## Datatypes

## [displayitem](datatype-displayitem.md)
{% 
  include-markdown "plugins/core-plugins/itemdisplay/datatype-displayitem.md" 
  start="<!--dt-desc-start-->" 
  end="<!--dt-desc-end-->" 
  trailing-newlines=false
%} {{ readMore('plugins/core-plugins/itemdisplay/datatype-displayitem.md') }}

<h2>Members</h2>
{%
  include-markdown "plugins/core-plugins/itemdisplay/datatype-displayitem.md"
  start="<!--dt-members-start-->"
  end="<!--dt-members-end-->"
  heading-offset=0
%}
{%
  include-markdown "plugins/core-plugins/itemdisplay/datatype-displayitem.md"
  start="<!--dt-linkrefs-start-->"
  end="<!--dt-linkrefs-end-->"
%}
