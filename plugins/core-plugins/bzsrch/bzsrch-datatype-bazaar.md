---
tags:
   - datatype
---
# `bazaar`

Datatype providing access to bazaar search results and status information.Datatype providing access to bazaar search results and status information.

## Members

### {{ renderMember(type='int', name='Count') }}
:   Number of search results available

### {{ renderMember(type='bool', name='Done') }}
:   True if search operation has completed

### {{ renderMember(type='bazaaritem', name='Item', params='#') }}
:   Returns the name of the item at the specified index

### {{ renderMember(type='bazaaritem', name='SortedItem', params='#') }}
:   Returns the name of the item at the specified index from a sorted list, as you'd see it in the GUI.

[bazaaritem]: bzsrch-datatype-bazaaritem.md
[bool]: ../../../reference/data-types/datatype-bool.md
[int]: ../../../reference/data-types/datatype-int.md