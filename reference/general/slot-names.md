---
tags:
    - ref
---
# Slot Names

## ItemSlot & ItemSlot2

These are not top level objects they are only members of [DataType:item](../data-types/datatype-item.md)

### ItemSlot Diagram

You SHOULD use .ItemSlot and .ItemSlot2 instead of .InvSlot

The reason for this is that they work without having to open the bags.

**Example:**

Picking up an item from pack 10 first slot in that pack:

```text
/itemnotify in pack${Math.Calc[${Me.Inventory[32].Item[1].ItemSlot}-22].Int} ${Math.Calc[${Me.Inventory[32].Item[1].ItemSlot2} + 1].Int} leftmouseup
```

Why not just /itemnotify in ${Me.Inventory[32\].Item\[1\].ItemSlot} ${Me.Inventory\[32\].Item\[1].ItemSlot2} you may ask...

well, we didn't have .ItemSlot and .ItemSlot2 until recently, so /itemnotify works with the old pack system that starts at slot 1 not 0

I can't change it to use real slotnumbers because then it will break a lot of old macros. So use the above calculation.

-eqmule

```text
ItemSlot Inventory
+----+----+
| 23 | 24 |
+----+----+
| 25 | 26 |
+----+----+
| 27 | 28 |
+----+----+
| 29 | 30 |
+----+----+
| 31 | 32 |
+----+----+
```

.ItemSlot2 is a "sub" slot, example if .ItemSlot is 23 (a container like a Backpack for example) and your item is inside that container this will return what slot INSIDE that container it’s in... complicated? Not really.

Picking up an item from pack 10 first slot in that pack: /itemnotify in pack${Math.Calc[${Me.Inventory\[32\].Item\[1\].ItemSlot}-22\].Int} ${Math.Calc\[${Me.Inventory\[32\].Item\[1\].ItemSlot2} + 1].Int} leftmouseup

Or say you want an Iron Ration, which is in bag 1 in slot 8 Doing /echo ${FindItem[=Iron Ration].ItemSlot} will return 23

Doing /echo ${FindItem[=Iron Ration].ItemSlot2} will return 7 (slots start at 0 so this is in fact correct)

For the above example, you would be using this:

```text
/itemnotify in pack${Math.Calc[${Me.Inventory[23].ItemSlot}-22].Int} ${Math.Calc[${Me.Inventory[23].Item[7].ItemSlot2} + 1].Int} leftmouseup
```

and programatically:

```text
/itemnotify in pack${Math.Calc[${Me.Inventory[${FindItem[=Iron Ration].ItemSlot}].ItemSlot}-22].Int}
```

Line above, then a space, and the following(I couldn't do a single line due to lack of linewrap):

```text
${Math.Calc[${Me.Inventory[${FindItem[=Iron Ration].ItemSlot}].Item[${FindItem[=Iron Ration].ItemSlot2}].ItemSlot2} + 1].Int} leftmouseup
```

## InvSlot

### Inventory Diagram

```text
InvSlot Inventory
+----+----+
| 24 | 25 |
+----+----+
| 26 | 27 |
+----+----+
| 28 | 29 |
+----+----+
| 30 | 31 |
+----+----+
| 32 | 33 |
+----+----+
```

### Equipment Slots

|  |  |
| :--- | :--- |
| **0** | charm |
| **1** | leftear |
| **2** | head |
| **3** | face |
| **4** | rightear |
| **5** | neck |
| **6** | shoulder |
| **7** | arms |
| **8** | back |
| **9** | leftwrist |
| **10** | rightwrist |
| **11** | ranged |
| **12** | hands |
| **13** | mainhand |
| **14** | offhand |
| **15** | leftfinger |
| **16** | rightfinger |
| **17** | chest |
| **18** | legs |
| **19** | feet |
| **20** | waist |
| **21** | powersource |
| **22** | ammo |

### Inventory Slots

|  |  |
| :--- | :--- |
| **23** | pack1 |
| **24** | pack2 |
| **25** | pack3 |
| **26** | pack4 |
| **27** | pack5 |
| **28** | pack6 |
| **29** | pack7 |
| **30** | pack8 |
| **31** | pack9 |
| **32** | pack10 |

### Bank Slots

|  |  |
| :--- | :--- |
| **2000** | bank1 |
| **2001** | bank2 |
| **2002** | bank3 |
| **2003** | bank4 |
| **2004** | bank5 |
| **2005** | bank6 |
| **2006** | bank7 |
| **2007** | bank8 |
| **2008** | bank9 |
| **2009** | bank10 |
| **2010** | bank11 |
| **2011** | bank12 |
| **2012** | bank13 |
| **2013** | bank14 |
| **2014** | bank15 |
| **2015** | bank16 |
| **2016** | bank17 |
| **2017** | bank18 |
| **2018** | bank19 |
| **2019** | bank20 |
| **2020** | bank21 |
| **2021** | bank22 |
| **2022** | bank23 |
| **2023** | bank24 |
| **2500** | sharedbank1 |
| **2501** | sharedbank2 |

### Trade Slots

|  |  |
| :--- | :--- |
| **3000** | trade1 |
| **3001** | trade2 |
| **3002** | trade3 |
| **3003** | trade4 |
| **3004** | trade5 |
| **3005** | trade6 |
| **3006** | trade7 |
| **3007** | trade8 |
| **3008** | trade9 |

### Enviroment Slots

|  |  |
| :--- | :--- |
| **4000** | enviro1 |
| **4001** | enviro2 |
| **4002** | enviro3 |
| **4003** | enviro4 |
| **4004** | enviro5 |
| **4005** | enviro6 |
| **4006** | enviro7 |
| **4007** | enviro8 |
| **4008** | enviro9 |

### Loot Slots

|  |  |
| :--- | :--- |
| **5000** | loot1 |
| **5001** | loot2 |
| **5002** | loot3 |
| **5003** | loot4 |
| **5004** | loot5 |
| **5005** | loot6 |
| **5006** | loot7 |
| **5007** | loot8 |
| **5008** | loot9 |
| **5009** | loot10 |
| **5010** | loot11 |
| **5011** | loot12 |
| **5012** | loot13 |
| **5013** | loot14 |
| **5014** | loot15 |
| **5015** | loot16 |
| **5016** | loot17 |
| **5017** | loot18 |
| **5018** | loot19 |
| **5019** | loot20 |
| **5020** | loot21 |
| **5021** | loot22 |
| **5022** | loot23 |
| **5023** | loot24 |
| **5024** | loot25 |
| **5025** | loot26 |
| **5026** | loot27 |
| **5027** | loot28 |
| **5028** | loot29 |
| **5029** | loot30 |
| **5030** | loot31 |

### Merchant Slots

|  |  |
| :--- | :--- |
| **6000** | merchant1 |
| **6001** | merchant2 |
| **6002** | merchant3 |
| **6003** | merchant4 |
| **6004** | merchant5 |
| **6005** | merchant6 |
| **6006** | merchant7 |
| **6007** | merchant8 |
| **6008** | merchant9 |
| **6009** | merchant10 |
| **6010** | merchant11 |
| **6011** | merchant12 |
| **6012** | merchant13 |
| **6013** | merchant14 |
| **6014** | merchant15 |
| **6015** | merchant16 |
| **6016** | merchant17 |
| **6017** | merchant18 |
| **6018** | merchant19 |
| **6019** | merchant20 |
| **6020** | merchant21 |
| **6021** | merchant22 |
| **6022** | merchant23 |
| **6023** | merchant24 |
| **6024** | merchant25 |
| **6025** | merchant26 |
| **6026** | merchant27 |
| **6027** | merchant28 |
| **6028** | merchant29 |
| **6029** | merchant30 |
| **6030** | merchant31 |
| **6031** | merchant32 |
| **6032** | merchant33 |
| **6033** | merchant34 |
| **6034** | merchant35 |
| **6035** | merchant36 |
| **6036** | merchant37 |
| **6037** | merchant38 |
| **6038** | merchant39 |
| **6039** | merchant40 |
| **6040** | merchant41 |
| **6041** | merchant42 |
| **6042** | merchant43 |
| **6043** | merchant44 |
| **6044** | merchant45 |
| **6045** | merchant46 |
| **6046** | merchant47 |
| **6047** | merchant48 |
| **6048** | merchant49 |
| **6049** | merchant50 |
| **6050** | merchant51 |
| **6051** | merchant52 |
| **6052** | merchant53 |
| **6053** | merchant54 |
| **6054** | merchant55 |
| **6055** | merchant56 |
| **6056** | merchant57 |
| **6057** | merchant58 |
| **6058** | merchant59 |
| **6059** | merchant60 |
| **6060** | merchant61 |
| **6061** | merchant62 |
| **6062** | merchant63 |
| **6063** | merchant64 |
| **6064** | merchant65 |
| **6065** | merchant66 |
| **6066** | merchant67 |
| **6067** | merchant68 |
| **6068** | merchant69 |
| **6069** | merchant70 |
| **6070** | merchant71 |
| **6071** | merchant72 |
| **6072** | merchant73 |
| **6073** | merchant74 |
| **6074** | merchant75 |
| **6075** | merchant76 |
| **6076** | merchant77 |
| **6077** | merchant78 |
| **6078** | merchant79 |
| **6079** | merchant80 |

### Bazaar Slots

|  |  |
| :--- | :--- |
| **7000** | bazaar1 |
| **7001** | bazaar2 |
| **7002** | bazaar3 |
| **7003** | bazaar4 |
| **7004** | bazaar5 |
| **7005** | bazaar6 |
| **7006** | bazaar7 |
| **7007** | bazaar8 |
| **7008** | bazaar9 |
| **7009** | bazaar10 |
| **7010** | bazaar11 |
| **7011** | bazaar12 |
| **7012** | bazaar13 |
| **7013** | bazaar14 |
| **7014** | bazaar15 |
| **7015** | bazaar16 |
| **7016** | bazaar17 |
| **7017** | bazaar18 |
| **7018** | bazaar19 |
| **7019** | bazaar20 |
| **7020** | bazaar21 |
| **7021** | bazaar22 |
| **7022** | bazaar23 |
| **7023** | bazaar24 |
| **7024** | bazaar25 |
| **7025** | bazaar26 |
| **7026** | bazaar27 |
| **7027** | bazaar28 |
| **7028** | bazaar29 |
| **7029** | bazaar30 |
| **7030** | bazaar31 |
| **7031** | bazaar32 |
| **7032** | bazaar33 |
| **7033** | bazaar34 |
| **7034** | bazaar35 |
| **7035** | bazaar36 |
| **7036** | bazaar37 |
| **7037** | bazaar38 |
| **7038** | bazaar39 |
| **7039** | bazaar40 |
| **7040** | bazaar41 |
| **7041** | bazaar42 |
| **7042** | bazaar43 |
| **7043** | bazaar44 |
| **7044** | bazaar45 |
| **7045** | bazaar46 |
| **7046** | bazaar47 |
| **7047** | bazaar48 |
| **7048** | bazaar49 |
| **7049** | bazaar50 |
| **7050** | bazaar51 |
| **7051** | bazaar52 |
| **7052** | bazaar53 |
| **7053** | bazaar54 |
| **7054** | bazaar55 |
| **7055** | bazaar56 |
| **7056** | bazaar57 |
| **7057** | bazaar58 |
| **7058** | bazaar59 |
| **7059** | bazaar60 |
| **7060** | bazaar61 |
| **7061** | bazaar62 |
| **7062** | bazaar63 |
| **7063** | bazaar64 |
| **7064** | bazaar65 |
| **7065** | bazaar66 |
| **7066** | bazaar67 |
| **7067** | bazaar68 |
| **7068** | bazaar69 |
| **7069** | bazaar70 |
| **7070** | bazaar71 |
| **7071** | bazaar72 |
| **7072** | bazaar73 |
| **7073** | bazaar74 |
| **7074** | bazaar75 |
| **7075** | bazaar76 |
| **7076** | bazaar77 |
| **7077** | bazaar78 |
| **7078** | bazaar79 |
| **7079** | bazaar80 |

### Inspect Slots

|  |  |
| :--- | :--- |
| **8000** | inspect1 |
| **8001** | inspect2 |
| **8002** | inspect3 |
| **8003** | inspect4 |
| **8004** | inspect5 |
| **8005** | inspect6 |
| **8006** | inspect7 |
| **8007** | inspect8 |
| **8008** | inspect9 |
| **8009** | inspect10 |
| **8010** | inspect11 |
| **8011** | inspect12 |
| **8012** | inspect13 |
| **8013** | inspect14 |
| **8014** | inspect15 |
| **8015** | inspect16 |
| **8016** | inspect17 |
| **8017** | inspect18 |
| **8018** | inspect19 |
| **8019** | inspect20 |
| **8020** | inspect21 |
| **8021** | inspect22 |
| **8022** | inspect23 |
| **8023** | inspect24 |
| **8024** | inspect25 |
| **8025** | inspect26 |
| **8026** | inspect27 |
| **8027** | inspect28 |
| **8028** | inspect29 |
| **8029** | inspect30 |
| **8030** | inspect31 |
