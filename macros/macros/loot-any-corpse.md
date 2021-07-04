# Loot Any Corpse

This macro is UNTESTED, but should work fine. If it doesn't - hit edit and fix it.

Converted from Wait4Rez.mac to loot.mac here---&gt; [Editing Existing Macros](../../documentation/editing-existing-macros.md)

```text
 |** Loot.mac by TheNewGuy
 20 July 2005  

 Make a hotkey:
   /mac loot.mac 

 When something dies, push that hotkey as you are standing over the
 corpse.  This should loot everything.

 This code based upon Wat4rez.mac by FaNTuM.  Changed from Wait4rez.mac to
 loot.mac at the following URL:

 http://www.macroquest2.com/wiki/index.php/Editing_Existing_Macros

 **|

 | -------------- 
 | -- Main Sub -- 
 | -------------- 
 Sub Main 
    /declare t int outer 0 
    /declare loottotal int outer 
    /declare lootslot int outer 
    /declare lootleft int outer 0 
    /if (!${Defined[Param0]}) { 
    } else { 
       /varset lootleft ${Param0} 
    } 
    /tar corpse
    /loot
 | ----------------- 
 | -- Count items -- 
 | ----------------- 
    /delay 3s 
    :LootLag 
    /if (${loottotal}!=${Corpse.Items}) { 
       /varset loottotal ${Corpse.Items} 
       /delay 2s 
       /goto :LootLag 
    } 
    /if (${loottotal}<=${lootleft}) { 
       /notify LootWnd DoneButton leftmouseup 
       /return 
    } 
    /varset loottotal ${Math.Calc[${Corpse.Items}-${lootleft}]} 
 | --------------------- 
 | -- Loot the corpse -- 
 | --------------------- 
    /for lootslot 1 to ${loottotal} 
    :LootItem 
    /itemnotify loot${lootslot} rightmouseup 
    /delay 5 !${Corpse.Item[${lootslot}].ID} 
    /if (!${Corpse.Item[${lootslot}].ID}) { 
       /next lootslot 
    } else {
      /goto :LootItem 
    }
 | ----------------- 
 | -- Doublecheck -- 
 | ----------------- 
    /if (${Math.Calc[${Corpse.Items}-${lootleft}]}>0) /goto :LootLag 
    /notify LootWnd DoneButton leftmouseup 
 /return
```

