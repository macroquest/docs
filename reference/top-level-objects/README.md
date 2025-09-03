# Top-Level Objects

A "Top-Level Object" is any kind of object that you can start with when trying to find a property.

TLOs are called Top-Level Objects because nothing comes before them. A TLO is not a member of any object, it is itself an accessor to objects.

!!! Note

    A TLO provides access to _instances_ of datatypes.

    See Also: [DataType Reference](../data-types/)


The data that a TLO gives you may depend on the parameters that are provided. Most TLOs don't take any parameters (like **Me**). However, some TLOs return different data dependent on what is provided to them.
This is explained in the documentation by using the term **Forms**. A TLO with multiple **Forms** may return different datatypes depending on what is passed in.

### Examples

#### Me

**[Me](tlo-me)** is a Top Level Object that returns a [_character_](../data-types/datatype-character). **Me** has access to the members of the _character_ datatype, but **Me** is not the _character_ datatype. You will notice that the _character_ datatype inherits the _spawn_ datatype, which means the TLO **Me** will have access to both the _character_ and _spawn_ members.

#### Int

The datatype named [_int_](../data-types/datatype-int) and the Top Level Object named [**Int**](tlo-int) are not the same thing. 

The TLO is used to parse integer strings. the int datatype represents a numeric value.

## See Also

A [Beginners Guide to TLOs and MQ2DataVars](../../macros/beginners-guide-datatypes) may be useful for understanding how TLOs work.

## TLO List

## [Achievement](tlo-achievement.md)
{% include-markdown "reference/top-level-objects/tlo-achievement.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-achievement.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-achievement.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-achievement.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [AdvLoot](tlo-advloot.md)
{% include-markdown "reference/top-level-objects/tlo-advloot.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-advloot.md') }}

## [Alert](tlo-alert.md)
{% include-markdown "reference/top-level-objects/tlo-alert.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-alert.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-alert.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-alert.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Alias](tlo-alias.md)
{% include-markdown "reference/top-level-objects/tlo-alias.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-alias.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-alias.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-alias.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [AltAbility](tlo-altability.md)
{% include-markdown "reference/top-level-objects/tlo-altability.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-altability.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-altability.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-altability.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Bool](tlo-bool.md)
{% include-markdown "reference/top-level-objects/tlo-bool.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-bool.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-bool.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-bool.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Corpse](tlo-corpse.md)
{% include-markdown "reference/top-level-objects/tlo-corpse.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-corpse.md') }}

## [Cursor](tlo-cursor.md)
{% include-markdown "reference/top-level-objects/tlo-cursor.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-cursor.md') }}

## [Defined](tlo-defined.md)
{% include-markdown "reference/top-level-objects/tlo-defined.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-defined.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-defined.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-defined.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [DisplayItem](tlo-displayitem.md)
{% include-markdown "reference/top-level-objects/tlo-displayitem.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-displayitem.md') }}

## [DoorTarget](tlo-doortarget.md)
{% include-markdown "reference/top-level-objects/tlo-doortarget.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-doortarget.md') }}

## [DynamicZone](tlo-dynamiczone.md)
{% include-markdown "reference/top-level-objects/tlo-dynamiczone.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-dynamiczone.md') }}

## [EverQuest](tlo-everquest.md)
{% include-markdown "reference/top-level-objects/tlo-everquest.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-everquest.md') }}

## [Familiar](tlo-familiar.md)
{% include-markdown "reference/top-level-objects/tlo-familiar.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-familiar.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-familiar.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-familiar.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [FindItem](tlo-finditem.md)
{% include-markdown "reference/top-level-objects/tlo-finditem.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-finditem.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-finditem.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-finditem.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [FindItemBank](tlo-finditembank.md)
{% include-markdown "reference/top-level-objects/tlo-finditembank.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-finditembank.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-finditembank.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-finditembank.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [FindItemBankCount](tlo-finditembankcount.md)
{% include-markdown "reference/top-level-objects/tlo-finditembankcount.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-finditembankcount.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-finditembankcount.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-finditembankcount.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [FindItemCount](tlo-finditemcount.md)
{% include-markdown "reference/top-level-objects/tlo-finditemcount.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-finditemcount.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-finditemcount.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-finditemcount.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Float](tlo-float.md)
{% include-markdown "reference/top-level-objects/tlo-float.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-float.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-float.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-float.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [FrameLimiter](tlo-framelimiter.md)
{% include-markdown "reference/top-level-objects/tlo-framelimiter.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-framelimiter.md') }}

## [Friends](tlo-friends.md)
{% include-markdown "reference/top-level-objects/tlo-friends.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-friends.md') }}

## [GameTime](tlo-gametime.md)
{% include-markdown "reference/top-level-objects/tlo-gametime.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-gametime.md') }}

## [Ground](tlo-ground.md)
{% include-markdown "reference/top-level-objects/tlo-ground.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-ground.md') }}

## [GroundItemCount](tlo-grounditemcount.md)
{% include-markdown "reference/top-level-objects/tlo-grounditemcount.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-grounditemcount.md') }}

## [Group](tlo-group.md)
{% include-markdown "reference/top-level-objects/tlo-group.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-group.md') }}

## [Heading](tlo-heading.md)
{% include-markdown "reference/top-level-objects/tlo-heading.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-heading.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-heading.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-heading.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [If](tlo-if.md)
{% include-markdown "reference/top-level-objects/tlo-if.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-if.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-if.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-if.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Illusion](tlo-illusion.md)
{% include-markdown "reference/top-level-objects/tlo-illusion.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-illusion.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-illusion.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-illusion.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Ini](tlo-ini.md)
{% include-markdown "reference/top-level-objects/tlo-ini.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-ini.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-ini.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-ini.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Int](tlo-int.md)
{% include-markdown "reference/top-level-objects/tlo-int.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-int.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-int.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-int.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [InvSlot](tlo-invslot.md)
{% include-markdown "reference/top-level-objects/tlo-invslot.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-invslot.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-invslot.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-invslot.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Inventory](tlo-inventory.md)
{% include-markdown "reference/top-level-objects/tlo-inventory.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-inventory.md') }}

## [ItemTarget](tlo-itemtarget.md)
{% include-markdown "reference/top-level-objects/tlo-itemtarget.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-itemtarget.md') }}

## [LastSpawn](tlo-lastspawn.md)
{% include-markdown "reference/top-level-objects/tlo-lastspawn.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-lastspawn.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-lastspawn.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-lastspawn.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [LineOfSight](tlo-lineofsight.md)
{% include-markdown "reference/top-level-objects/tlo-lineofsight.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-lineofsight.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-lineofsight.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-lineofsight.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Macro](tlo-macro.md)
{% include-markdown "reference/top-level-objects/tlo-macro.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-macro.md') }}

## [MacroQuest](tlo-macroquest.md)
{% include-markdown "reference/top-level-objects/tlo-macroquest.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-macroquest.md') }}

## [Math](tlo-math.md)
{% include-markdown "reference/top-level-objects/tlo-math.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-math.md') }}

## [Me](tlo-me.md)
{% include-markdown "reference/top-level-objects/tlo-me.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-me.md') }}

## [Menu](tlo-menu.md)
{% include-markdown "reference/top-level-objects/tlo-menu.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-menu.md') }}

## [Mercenary](tlo-mercenary.md)
{% include-markdown "reference/top-level-objects/tlo-mercenary.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-mercenary.md') }}

## [Merchant](tlo-merchant.md)
{% include-markdown "reference/top-level-objects/tlo-merchant.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-merchant.md') }}

## [Mount](tlo-mount.md)
{% include-markdown "reference/top-level-objects/tlo-mount.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-mount.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-mount.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-mount.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [NearestSpawn](tlo-nearestspawn.md)
{% include-markdown "reference/top-level-objects/tlo-nearestspawn.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-nearestspawn.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-nearestspawn.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-nearestspawn.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Pet](tlo-pet.md)
{% include-markdown "reference/top-level-objects/tlo-pet.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-pet.md') }}

## [Plugin](tlo-plugin.md)
{% include-markdown "reference/top-level-objects/tlo-plugin.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-plugin.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-plugin.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-plugin.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [PointMerchant](tlo-pointmerchant.md)
{% include-markdown "reference/top-level-objects/tlo-pointmerchant.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-pointmerchant.md') }}

## [Raid](tlo-raid.md)
{% include-markdown "reference/top-level-objects/tlo-raid.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-raid.md') }}

## [Range](tlo-range.md)
{% include-markdown "reference/top-level-objects/tlo-range.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-range.md') }}

## [Select](tlo-select.md)
{% include-markdown "reference/top-level-objects/tlo-select.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-select.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-select.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-select.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [SelectedItem](tlo-selecteditem.md)
{% include-markdown "reference/top-level-objects/tlo-selecteditem.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-selecteditem.md') }}
## [Skill](tlo-skill.md)
{% include-markdown "reference/top-level-objects/tlo-skill.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-skill.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-skill.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-skill.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Social](tlo-social.md)
{% include-markdown "reference/top-level-objects/tlo-social.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-social.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-social.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-social.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Spawn](tlo-spawn.md)
{% include-markdown "reference/top-level-objects/tlo-spawn.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-spawn.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-spawn.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-spawn.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [SpawnCount](tlo-spawncount.md)
{% include-markdown "reference/top-level-objects/tlo-spawncount.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-spawncount.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-spawncount.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-spawncount.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Spell](tlo-spell.md)
{% include-markdown "reference/top-level-objects/tlo-spell.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-spell.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-spell.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-spell.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [String](tlo-string.md)
{% include-markdown "reference/top-level-objects/tlo-string.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-string.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-string.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-string.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [SubDefined](tlo-subdefined.md)
{% include-markdown "reference/top-level-objects/tlo-subdefined.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-subdefined.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-subdefined.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-subdefined.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Switch](tlo-switch.md)
{% include-markdown "reference/top-level-objects/tlo-switch.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-switch.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-switch.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-switch.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [SwitchTarget](tlo-switchtarget.md)
{% include-markdown "reference/top-level-objects/tlo-switchtarget.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-switchtarget.md') }}

## [Target](tlo-target.md)
{% include-markdown "reference/top-level-objects/tlo-target.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-target.md') }}

## [Task](tlo-task.md)
{% include-markdown "reference/top-level-objects/tlo-task.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-task.md') }}

## [TeleportationItem](tlo-teleportationitem.md)
{% include-markdown "reference/top-level-objects/tlo-teleportationitem.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-teleportationitem.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-teleportationitem.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-teleportationitem.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Time](tlo-time.md)
{% include-markdown "reference/top-level-objects/tlo-time.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-time.md') }}

## [TradeskillDepot](tlo-tradeskilldepot.md)
{% include-markdown "reference/top-level-objects/tlo-tradeskilldepot.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-tradeskilldepot.md') }}

## [Type](tlo-type.md)
{% include-markdown "reference/top-level-objects/tlo-type.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-type.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-type.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-type.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Window](tlo-window.md)
{% include-markdown "reference/top-level-objects/tlo-window.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-window.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-window.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-window.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}

## [Zone](tlo-zone.md)
{% include-markdown "reference/top-level-objects/tlo-zone.md" start="<!--tlo-desc-start-->" end="<!--tlo-desc-end-->" trailing-newlines=false %} {{ readMore('reference/top-level-objects/tlo-zone.md') }}
:    <h3>Forms</h3>
    {% include-markdown "reference/top-level-objects/tlo-zone.md" start="<!--tlo-forms-start-->" end="<!--tlo-forms-end-->" %}
    {% include-markdown "reference/top-level-objects/tlo-zone.md" start="<!--tlo-linkrefs-start-->" end="<!--tlo-linkrefs-end-->" %}
