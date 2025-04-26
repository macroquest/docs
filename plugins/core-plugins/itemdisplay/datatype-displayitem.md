---
tags:
   - datatype
---
# `displayitem`

Holds members that can control and return status on item display windows. This datatype inherits all members from the **[item]** datatype.

## Members

### {{ renderMember(type='string', name='Info') }}
:   Returns details from the item. Note that this is different from the "Information" member.

### {{ renderMember(type='string', name='WindowTitle') }}
:   Returns the title of the window

### {{ renderMember(type='string', name='AdvancedLore') }}
:   Displays lore text

### {{ renderMember(type='string', name='MadeBy') }}
:   Displays the maker of the crafted item

### {{ renderMember(type='bool', name='Collected') }}

### {{ renderMember(type='bool', name='CollectedReceived') }}

### {{ renderMember(type='bool', name='Scribed') }}

### {{ renderMember(type='bool', name='ScribedReceived') }}

### {{ renderMember(type='string', name='Information') }}
:   Returns the "item information" text from the item window.

### {{ renderMember(type='int', name='DisplayIndex') }}
:   Shows the index number of the item window

### {{ renderMember(type='window', name='Window') }}
:   Gives access to the **[window]** datatype, allowing you to do things like `/invoke ${DisplayItem[5].Window.DoClose}`

### {{ renderMember(type='item', name='Item') }}
:   Gives access to the **[item]** datatype, although its members are already inherited. e.g. `/echo ${DisplayItem[2].Item.HP}`

### {{ renderMember(type='DisplayItem', name='Next') }}

[DisplayItem]: datatype-displayitem.md
[bool]: ../../../reference/data-types/datatype-bool.md
[int]: ../../../reference/data-types/datatype-int.md
[item]: ../../../reference/data-types/datatype-item.md
[string]: ../../../reference/data-types/datatype-string.md
[window]: ../../../reference/data-types/datatype-window.md