"""
TODO Addresses are not finalized.
TODO Link appropriate sites and tools
TODO Upgraded versions of weapons and armor?
"""

weapons_table = {
    # Daggers
    "Dagger": 0x000186A0,
    "Parrying Dagger": 0x00018A88,
    "Bandit's Knife": 0x00019258,
    "Ghost Blade": 0x00018E70,
    "Priscilla's Dagger": 0x00019640,
    # Straight Swords
    "Shortsword": 0x00030D40,
    "Longsword": 0x00031128,
    "Broadsword": 0x00031510,
    "Balder Side Sword": 0x00031CE0,
    "Sunlight Straight Sword": 0x000324B0,
    "Darksword": 0x00033450,
    "Barbed Straight Sword": 0x00032898,
    "Crystal Straight Sword": 0x000320C8,
    "Silver Knight Straight Sword": 0x00032C80,
    "Astora's Straight Sword": 0x00033068,
    "Drake Sword": 0x00033838,
    "Broken Straight Sword": 0x000318F8,
    "Straight Sword Hilt": 0x00033C20,
    # Greatswords
    "Greatsword of Artorias (Cursed)": 123450,
    "Greatsword of Artorias": 123450,
    "Great Lord Greatsword": 123450,
    "Bastard Sword": 123450,
    "Claymore": 123450,
    "Man-Serpent Greatsword": 123450,
    "Flamberge": 123450,
    "Crystal Greatsword": 123450,
    "Black Knight Sword": 123450,
    "Stone Greatsword": 123450,
    "Moonlight Greatsword": 123450,
    # Ultra Greatswords
    "Greatsword": 0x00055B18,
    "Zweihander": 0x00055730,
    "Demon Great Machete": 0x00055F00,
    "Black Knight Greatsword": 0x00056AB8,
    "Dragon Greatsword": 0x000566D0,
    # Curved Swords
    "Scimitar": 0x00061A80,
    "Quelaag's Furysword": 0x0006331C,
    "Falchion": 0x00061E68,
    "Shotel": 0x00062250,
    "Painting Guardian Sword": 0x00062E08,
    "Jagged Ghost Blade": 0x00062638,
    # Katanas
    "Uchigatana": 0x0007A120,
    "Chaos Blade": 0x0007ADA0,
    "Iaito": 0x0007A8F0,
    "Washing Pole": 0x0007A508,
    # Curved Greatswords
    "Murakumo": 0x0006E1B8,
    "Server": 0x0006DDD0,
    "Gravelord Sword": 0x0006E988,
    # Piercing Swords
    "Mail Breaker": 0x000927C0,
    "Rapier": 0x00092BA8,
    "Estoc": 0x00092F90,
    "Ricard's Rapier": 0x00093760,
    "Velka's Rapier": 0x00093378,
    # Axes
    "Hand Axe": 0x000AAE60,
    "Battle Axe": 0x000AB248,
    "Golem Axe": 0x000ABE00,
    "Butcher Knife": 0x000ABA1C,
    "Gargoyle Tail Axe": 0x000AC1E8,
    "Crescent Axe": 0x000AB630,
    # Great Axes
    "Greataxe": 0x000B71B0,
    "Demon's Greataxe": 0x000B7598,
    "Stone Greataxe": 0x00898ED8,
    "Black Knight Greataxe": 0x000B7D68,
    "Dragon King Greataxe": 0x000B7980,
    # Hammers
    "Club": 0x000C3500,
    "Reinforced Club": 0x000C5828,
    "Blacksmith Giant Hammer": 0x000C5FF8,
    "Mace": 0x000C38E8,
    "Morning Star": 0x000C3CD0,
    "Warpick": 0x000C40B8,
    "Pickaxe": 0x000C44A0,
    "Blacksmith Hammer": 0x000C5C10,
    "Hammer of Vamos": 0x000C63E0,
    # Great Hammers
    "Smough's Hammer": 0x000D1024,
    "Large Club": 0x000D0BD8,
    "Great Club": 0x000CF850,
    "Demon's Great Hammer": 0x000D0020,
    "Grant": 0x000CFC38,
    "Dragon Tooth": 0x000D07F0,
    # Fist Weapons
    "Dragon Bone Fist": 0x000DC7BC,
    "Caestus": 0x000DBF88,
    "Claws": 0x000DC370,
    "Dark Hand": 0x000DCB40,
    # Spears
    "Spear": 0x000F4240,
    "Winged Spear": 0x000F4628,
    "Partizan": 0x000F4A10,
    "Dragonslayer Spear": 0x001009DC,
    "Moonlight Butterfly Horn": 0x00101148,
    "Pike": 0x00100590,
    "Channeler's Trident": 0x000F51E0,
    "Demon's Spear": 0x000F4DF8,
    "Silver Knight Spear": 0x000F59B0,
    # Halberds
    "Halberd": 0x0010C8E0,
    "Lifehunt Scythe": 0x00119338,
    "Lucerne": 0x0010E050,
    "Scythe": 0x0010E438,
    "Gargoyle's Halberd": 0x0010D498,
    "Giant's Halberd": 0x0010CCC8,
    "Titanite Catch Pole": 0x0010D0B0,
    "Black Knight Halberd": 0x0010DC68,
    "Great Scythe": 0x00118C30,
    # Whips
    "Whip": 0x00186A00,
    "Notched Whip": 0x00186DE8,
    # Bows
    "Short Bow": 0x00124F80,
    "Composite Bow": 0x00125F20,
    "Darkmoon Bow": 0x0012636C,
    "Longbow": 0x00125368,
    "Black Bow of Pharis": 0x00125750,
    # Greatbows
    "Dragonslayer Greatbow": 0x001E9FD8,
    # Crossbows
    "Light Crossbow": 0x001312D0,
    "Heavy Crossbow": 0x001316D8,
    "Sniper Crossbow": 0x00131E88,
    "Avelyn": 0x00131AA0,
    # Catalysts
    "Sorcerer's Catalyst": 0x0013D620,
    "Tin Darkmoon Catalyst": 0x0013E5C0,
    "Beatrice's Catalyst": 0x0013DA08,
    "Logan's Catalyst": 0x0013E1D8,
    # TODO Determine if DLC or not
    "Oolacile Ivory Catalyst": 0x0013E9A8,
    "Demon's Catalyst": 0x0013F178,
    "Izalith Catalyst": 0x0013F560,
    "Tin Banishment Catalyst": 0x0013DDF0,
    "Tin Crystallization Catalyst": 0x0013ED90,
    # Flames
    "Pyromancy Flame": 0x00145320,
    # TODO Can't determine ID, should this even be in the pool?
    "Pyromancy Flame (Upgraded)": 123450,
    # Talismans
    "Talisman": 0x0014C080,
    "Canvas Talisman": 0x0014C468,
    "Thorolund Talisman": 0x0014C850,
    "Ivory Talisman": 0x0014CC38,
    "Sunlight Talisman": 0x0014D408,
    "Darkmoon Talisman": 0x0014D7F0,
    "Velka's Talisman": 0x0014DBD8,
}

dlc_weapons_table = {
    # Daggers
    "Dark Silver Tracer": 0x00897F38,
    # Greatswords
    # TODO Multiple IDs, how does this work?
    "Abyss Greatsword": 0x00898320,
    "Obsidian Greatsword": 0x0089A260,
    # Curved Swords
    "Gold Tracer": 0x00897B50,
    # Spears
    "Four-pronged Plow": 0x008992C0,
    # Whips
    "Guardian Tail": 0x00899E78,
    # Greatbows
    "Gough's Greatbow": 0x0089A648,
    # Catalysts
    "Manus Catalyst": 0x008996A8,
    "Oolacile Catalyst": 0x00899A90,
}

shield_table = {
    # Small
    "Warrior's Round Shield": 0x00164720,
    "Caduceus Round Shield": 0x001583D0,
    "Effigy Shield": 0x00895440,
    # TODO Are ampersand's accepted?
    "Red and White Round Shield": 0x001685A0,
    "Cracked Round Shield": 0x00157430,
    "Plank Shield": 0x00157FE8,
    "Small Leather Shield": 0x00156878,
    "Leather Shield": 0x00157C00,
    "Buckler": 0x00157048,
    "Target Shield": 0x00156C60,
    "Crystal Ring Shield": 0x001587B8,
    # Standard
    "East-West Shield": 0x00155CC0,
    "Wooden Shield": 0x001560A8,
    "Large Leather Shield": 0x00156490,
    "Heater Shield": 0x00162010,
    "Tower Kite Shield": 0x001627E0,
    "Caduceus Kite Shield": 0x00168988,
    "Hollow Soldier Shield": 0x00162FB0,
    "Knight Shield": 0x001623F8,
    "Sanctus": 0x00895828,
    "Balder Shield": 0x00163398,
    "Spider Shield": 0x00164EF0,
    "Grass Crest Shield": 0x00162BC8,
    "Bloodshield": 0x00895C10,
    "Iron Round Shield": 0x00164B08,
    "Sunlight Shield": 0x00167600,
    "Pierce Shield": 0x001681B8,
    "Spiked Shield": 0x00166E30,
    "Gargoyle's Shield": 0x00168D70,
    "Crystal Shield": 0x00167218,
    "Crest Shield": 0x00163780,
    "Dragon Crest Shield": 0x00163B68,
    "Black Knight Shield": 0x00167DD0,
    # Greatshields
    "Greatshield of Artorias": 0x0016FEB8,
    "Eagle Shield": 0x0016E360,
    "Tower Shield": 0x0016E748,
    "Black Iron Greatshield": 0x00895FF8,
    "Giant Shield": 0x0016EB30,
    "Bonewheel Shield": 0x0016FAD0,
    "Stone Greatshield": 0x0016EF18,
    "Havel's Greatshield": 0x0016F6E8,
}

dlc_shields_table = {
    # Greatshields
    "Cleansing Greatshield": 0x00898AF0,
}

armor_table = {
    # Adventurer's Set
    "Helm of the Wise": 0x0001ADB0,
    "Armor of the Glorious": 0x0001B198,
    "Gauntlets of the Vanquisher": 0x0001B580,
    "Boots of the Explorer": 0x0001B968,
    # Dingy Set
    "Dingy Hood": 0x00061A80,
    "Dingy Robe": 0x00061E68,
    "Dingy Gloves": 0x00062550,
    "Blood-Stained Skirt": 0x00062638,
    # TODO Technically DLC, perhaps splitting them isn't necessary
    # Antiquated Set
    "Crown of Dusk": 0x00050910,
    "Antiquated Dress": 0x00050CF8,
    "Antiquated Gloves": 0x000510E0,
    "Antiquated Skirt": 0x000514C8,
    # Eastern Set
    "Eastern Helm": 0x000445C0,
    "Eastern Armor": 0x000449A8,
    "Eastern Gauntlets": 0x00044D90,
    "Eastern Leggings": 0x00045178,
    # Maiden Set
    "Maiden Hood": 0x00064190,
    "Maiden Robe": 0x00064578,
    "Maiden Gloves": 0x00064960,
    "Maiden Skirt": 0x00064D48,
    # Elite Knight Set
    "Elite Knight Helm": 0x00055730,
    "Elite Knight Armor": 0x00055B18,
    "Elite Knight Gauntlets": 0x00055F00,
    "Elite Knight Leggings": 0x000562E8,
    # Ornstein's Set
    "Ornstein's Helm": 0x00041EB0,
    "Ornstein's Armor": 0x00042298,
    "Ornstein's Gauntlets": 0x00042680,
    "Ornstein's Leggings": 0x0042A68,
    # Balder Set
    "Balder Helm": 0x0007C830,
    "Balder Armor": 0x0007CC18,
    "Balder Gauntlets": 0x0007D000,
    "Balder Leggings": 0x0007D3E8,
    # Favor Set
    "Helm of Favor": 0x000186A0,
    "Embraced Armor of Favor": 0x00018A88,
    "Gauntlets of Favor": 0x00018E70,
    "Leggings of Favor": 0x00019258,
    # Painting Guardian Set
    "Painting Guardian Hood": 0x0003D090,
    "Painting Guardian Robe": 0x0003D478,
    "Painting Guardian Gloves": 0x0003D860,
    "Painting Guardian Waistcloth": 0x0003DC48,
    # Bandit Set
    "Brigand Hood": 0x0000C350,
    "Brigand Armor": 0x0000C738,
    "Brigand Gauntlets": 0x0000CB20,
    "Brigand Trousers": 0x0000CF08,
    # Giant Armor Set
    "Giant Helm": 0x00081650,
    "Giant Armor": 0x00081A38,
    "Giant Gauntlets": 0x00081E20,
    "Giant Leggings": 0x00082208,
    # Paladin Set
    "Paladin Helm": 0x00004E20,
    "Paladin Armor": 0x00005208,
    "Paladin Gauntlets": 0x000055F0,
    "Paladin Leggings": 0x000059D8,
    # Big Hat's Set
    "Big Hat": 0x0005CC60,
    "Sage Robe": 0x0005D048,
    "Traveling Gloves": 0x0005D430,
    "Traveling Boots": 0x0005D818,
    # Gold-Hemmed Black Set
    "Gold-Hemmed Black Hood": 0x000704E0,
    "Gold-Hemmed Black Cloak": 0x000708C8,
    "Gold-Hemmed Black Gloves": 0x00070CB0,
    "Gold-Hemmed Black Skirt": 0x00071098,
    # Pyromancer Set
    "Tattered Cloth Hood": 0x00038270,
    "Tattered Cloth Robe": 0x00038658,
    "Tattered Cloth Manchette": 0x00038A40,
    "Heavy Boots": 0x00038E28,
    # Black Iron Set
    "Black Iron Helm": 0x00011170,
    "Black Iron Armor": 0x00011558,
    "Black Iron Gauntlets": 0x00011940,
    "Black Iron Leggings": 0x00011D28,
    # Great Lord Set
    "Crown of the Great Lord": 0x00086470,
    "Robe of the Great Lord": 0x00086858,
    "Bracelet of the Great Lord": 0x00086C40,
    "Anklet of the Great Lord": 0x00087028,
    # Thorns Set
    "Helm of Thorns": 0x00030D40,
    "Armor of Thorns": 0x00031128,
    "Gauntlets of Thorns": 0x00031510,
    "Leggings of Thorns": 0x000318F8,
    # Black Knight Set
    "Black Knight Helm": 0x0004E200,
    "Black Knight Armor": 0x0004E5E8,
    "Black Knight Gauntlets": 0x0004E9D0,
    "Black Knight Leggings": 0x0004EDB8,
    # Gough's Set
    "Gough's Helm": 0x000A6040,
    "Gough's Armor": 0x000A6428,
    "Gough's Gauntlets": 0x000A6810,
    "Gough's Leggings": 0x000A6BF8,
    # Shadow Set
    "Shadow Mask": 0x0000EA60,
    "Shadow Garb": 0x0000EE48,
    "Shadow Gauntlets": 0x0000F230,
    "Shadow Leggings": 0x0000F618,
    # Black Set
    "Mask of Velka": 0x000249F0,
    "Black Cleric Robe": 0x00024DD8,
    "Black Manchette": 0x000251C0,
    "Black Tights": 0x000255A8,
    # Guardian Set
    "Guardian Helm": 0x000A8750,
    "Guardian Armor": 0x000A8B38,
    "Guardian Gauntlets": 0x000A8F20,
    "Guardian Leggings": 0x000A9308,
    # Silver Knight Set
    "Silver Knight Helm": 0x000668A0,
    "Silver Knight Armor": 0x00066C88,
    "Sliver Gauntlets": 0x00067070,
    "Silver Knight Leggings": 0x00067458,
    # Black Sorcerer Set
    "Black Sorcerer Hat": 0x0009C400,
    "Black Sorcerer Cloak": 0x0009C7E8,
    "Black Sorcerer Gauntlets": 0x0009CBD0,
    "Black Sorcerer Boots": 0x0009CFB8,
    # Gwyndolin Moonlight Set
    "Crown of the Dark Sun": 0x00083D60,
    "Moonlight Robe": 0x00084148,
    "Moonlight Gloves": 0x00084530,
    "Moonlight Waistcloth": 0x00084918,
    # Smough's Set
    "Smough's Helm": 0x00013880,
    "Smough's Armor": 0x00013C68,
    "Smough's Gauntlets": 0x00014050,
    "Smough's Leggings": 0x00014438,
    # Brass Set
    "Brass Helm": 0x0006DDD0,
    "Brass Armor": 0x0006E1B8,
    "Brass Gauntlets": 0x0006E5A0,
    "Brass Leggings": 0x0006E988,
    # Havel's Set
    "Havel's Helm": 0x0006B6C0,
    "Havel's Armor": 0x0006BAA8,
    "Havel's Gauntlets": 0x0006BE90,
    "Havel's Leggings": 0x0006C278,
    # Sorcerer Set
    "Sorcerer Hat": 0x00035B60,
    "Sorcerer Cloak": 0x00035F48,
    "Sorcerer Gauntlets": 0x00036330,
    "Sorcerer Boots": 0x00036718,
    # Catarina Set
    "Catarina Helm": 0x00002710,
    "Catarina Armor": 0x00002AF8,
    "Catarina Gauntlets": 0x00002EE1,
    "Catarina Leggings": 0x000032C78,
    # Hollow Soldier Set
    "Hollow Soldier Helm": 0x00075300,
    "Hollow Soldier Armor": 0x000756E8,
    "Hollow Soldier Waistcloth": 0x00075EB8,
    # Steel Set
    "Steel Helm": 0x00077A10,
    "Steel Armor": 0x00077DF8,
    "Steel Gauntlets": 0x000781E0,
    "Steel Leggings": 0x00785C8,
    # Chain Set
    "Chain Helm": 0x00029810,
    "Chain Armor": 0x00029BF8,
    "Leather Gauntlets": 0x00029FE0,
    "Chain Leggings": 0x0002A3C8,
    # Hollow Thief Set
    "Hollow Thief's Hood": 0x0007A120,
    "Hollow Thief's Leather Armor": 0x0007A508,
    "Hollow Thief's Tights": 0x0007ACD8,
    # Stone Knight Set
    "Stone Helm": 0x0001D4C0,
    "Stone Armor": 0x0001D8A8,
    "Stone Gauntlets": 0x0001DC90,
    "Stone Leggings": 0x0001E078,
    # Channeler Set
    "Six-Eyed Helm of the Channelers": 0x00015F90,
    "Robe of the Channelers": 0x00016378,
    "Gauntlets of the Channelers": 0x00016760,
    "Waistcloth of the Channelers": 0x00016B48,
    # Hollow Warrior Set
    "Hollow Warrior Helm": 0x0007EF40,
    "Hollow Warrior Armor": 0x0007F328,
    "Hollow Warrior Waistcloth": 0x0007FAF8,
    # Thief Set
    "Thief Mask": 0x000493E0,
    "Black Leather Armor": 0x000497C8,
    "Black Leather Gloves": 0x00049BB0,
    "Black Leather Boots": 0x00049F98,
    # Holy Set
    "Priest's Hat": 0x0004BAF0,
    "Holy Robe": 0x0004BED8,
    "Holy Trousers": 0x0004C6A8,
    # Wanderer Set
    "Wanderer Hood": 0x00057E40,
    "Wanderer Coat": 0x00058228,
    "Wanderer Manchette": 0x00058610,
    "Wanderer Boots": 0x00589F8,
    # Cleric Set
    "Cleric Helm": 0x0002BF20,
    "Cleric Armor": 0x0002C308,
    "Cleric Gauntlets": 0x0002C6F0,
    "Cleric Leggings": 0x0002CAD8,
    # Hunter Set
    "Pharis's Hat": 0x0003A980,
    "Leather Armor": 0x0003AD68,
    "Leather Gloves": 0x0003B150,
    "Leather Boots": 0x0003B538,
    # Warrior Set
    "Standard Helm": 0x00033450,
    "Hard Leather Armor": 0x00033838,
    "Hard Leather Gauntlets": 0x00033C20,
    "Hard Leather Boots": 0x00034008,
    # Crimson Set
    "Mask of the Sealer": 0x000222E0,
    "Crimson Robe": 0x000226C8,
    "Crimson Gloves": 0x00022AB0,
    "Crimson Waistcloth": 0x00022E98,
    # Iron Golem Set
    "Golem Helm": 0x00072BF0,
    "Golem Armor": 0x00072FD8,
    "Golem Gauntlets": 0x000733C0,
    "Golem Leggings": 0x000737A8,
    # Witch Set
    "Witch Hat": 0x00053020,
    "Witch Cloak": 0x00053408,
    "Witch Gloves": 0x000537F0,
    "Witch Skirt": 0x00053BD8,
    # Crystalline Set
    "Crystalline Helm": 0x0001FBD0,
    "Crystalline Armor": 0x0001FFB8,
    "Crystalline Gauntlets": 0x000203A0,
    "Crystalline Leggings": 0x00020788,
    # Iron Set
    "Iron Helm": 0x00027100,
    "Armor of the Sun": 0x000274E8,
    "Iron Bracelet": 0x000278D0,
    "Iron Leggings": 0x00027CB8,
    # Xanthous Set
    "Xanthous Crown": 0x00046CD0,
    "Xanthous Overcoat": 0x000470B8,
    "Xanthous Gloves": 0x000474A0,
    "Xanthous Waistcloth": 0x00047888,
    # Dark Set
    "Dark Mask": 0x00009C40,
    "Dark Armor": 0x0000A028,
    "Dark Gauntlets": 0x0000A410,
    "Dark Leggings": 0x0000A7F8,
    # Knight Set
    "Knight Helm": 0x0005F370,
    "Knight Armor": 0x0005F758,
    "Knight Gauntlets": 0x0005FB40,
    "Knight Leggings": 0x0005FF28,
    # Misc.
    "Sunlight Maggot": 0x0002E630,
    "Fang Boar Helm": 0x000975E0,
    "Gargoyle Helm": 0x00099CF0,
    "Symbol of Avarice": 0x0008B290,
    "Sack": 0x00088B80,
    "Mask of the Father": 0x000900B0,
    "Mask of the Mother": 0x000927C0,
    "Mask of the Child": 0x00094ED0,
    # TODO Should the no gear IDs be added?
}

dlc_armor_table = {
    # Lord's Blades Set
    "Porcelain Mask": 0x000A3930,
    "Lord's Blade Robe": 0x000A3D18,
    "Lord's Blade Gloves": 0x000A4100,
    "Lord's Blade Waistcloth": 0x000A44E8,
    # Artorias' Set
    "Helm of Artorias": 0x000A1220,
    "Armor of Artorias": 0x000A1608,
    "Gauntlets of Artorias": 0x000A19F0,
    "Leggings of Artorias": 0x000A1DD8,
    # TODO Determine Chester's Set IDs
    # Chester's Set
    "Snickering Top Hat": 123450,
    "Chester's Long Coat": 123450,
    "Chester's Gloves": 123450,
    "Chester's Trousers": 123450,
    # Misc.
    "Bloated Head": 0x000AD570,
    "Bloated Sorcerer Head": 0x000AFC80,
}

rings_table = {
    "Tiny Being's Ring": 0x0000006F,
    "Cloranthy Ring": 0x00000068,
    "Havel's Ring": 0x00000064,
    "Ring of Steel Protection": 0x00000078,
    "Spell Stoneplate Ring": 0x0000006B,
    "Flame Stoneplate Ring": 0x00000069,
    "Thunder Stoneplate Ring": 0x0000006A,
    "Speckled Stoneplate Ring": 0x0000006C,
    "Bloodbite Ring": 0x0000006D,
    "Poisonbite Ring": 0x0000006E,
    "Cursebite Ring": 0x00000071,
    # TODO Verify Ring ID
    "Red Tearstone Ring": 0x00000065,
    "Blue Tearstone Ring": 0x00000093,
    "Ring of Sacrifice": 0x0000007E,
    "Rare Ring of Sacrifice": 0x0000007F,
    "Bellowing Dragoncrest Ring": 0x00000073,
    "Lingering Dragoncrest Ring": 0x0000008D,
    "Slumbering Dragoncrest Ring": 0x0000007B,
    "Dusk Crown Ring": 0x00000074,
    "White Seance Ring": 0x00000072,
    "Darkmoon Seance Ring": 0x00000095,
    "Ring of the Sun's Firstborn": 0x00000094,
    "Darkmoon Blade Covenant Ring": 0x00000066,
    "Ring of the Sun Princess": 0x00000082,
    "Leo Ring": 0x00000090,
    "Wolf Ring": 0x00000092,
    "Hawk Ring": 0x00000077,
    "Hornet Ring": 0x00000075,
    "East Wood Grain Ring": 0x00000091,
    "Dark Wood Grain Ring": 0x00000080,
    "Rusted Iron Ring": 0x0000007D,
    "Covetous Gold Serpent Ring": 0x00000079,
    "Covetous Silver Serpent Ring": 0x0000007A,
    "Covenant of Artorias": 0x0000008A,
    "Orange Charred Ring": 0x0000008B,
    "Old Witch's Ring": 0x00000089,
    "Cat Covenant Ring": 0x00000067,
    "Ring of Fog": 0x0000007C,
    "Ring of Favor and Protection": 0x0000008F,
    "Ring of the Evil Eye": 0x0000008E,
}

dlc_rings_table = {
    "Calamity Ring": 0x00000096,
}

spells_table = {
    # Sorceries
    "Soul Arrow": 0x00000BB8,
    "Great Soul Arrow": 0x00000BC2,
    "Heavy Soul Arrow": 0x00000BCC,
    "Great Heavy Soul Arrow": 0x00000BD6,
    "Homing Soulmass": 0x00000BE0,
    "Homing Crystal Soulmass": 0x00000BEA,
    "Soul Spear": 0x00000BF4,
    "Crystal Soul Spear": 0x00000BFE,
    "White Dragon Breath": 0x00000E74,
    "Magic Weapon": 0x00000C1C,
    "Great Magic Weapon": 0x00000C26,
    "Crystal Magic Weapon": 0x00000C30,
    "Magic Shield": 0x00000CE4,
    "Strong Magic Shield": 0x00000CEE,
    "Aural Decoy": 0x00000DC0,
    "Hush": 0x00000DB6,
    "Fall Control": 0x00000DD4,
    "Hidden Weapon": 0x00000D48,
    "Hidden Body": 0x00000D52,
    "Repair": 0x00000DCA,
    "Cast Light": 0x00000DAC,
    "Chameleon": 0x00000DDE,
    "Remedy": 0x00000E1A,
    "Resist Curse": 0x00000E10,
    # DLC Sorceries
    "Dark Orb": 0x00000E7E,
    "Dark Bead": 0x00000E88,
    "Dark Fog": 0x00000E92,
    "Pursuers": 0x00000E9C,
    # Pyromancies
    "Combustion": 0x00001004,
    "Great Combustion": 0x0000100E,
    "Fireball": 0x00000FA0,
    "Fire Orb": 0x00000FAA,
    "Great Fireball": 0x00000FB4,
    "Great Chaos Fireball": 0x00001194,
    "Firestorm": 0x00000FBE,
    "Chaos Storm": 0x0000119E,
    "Fire Surge": 0x00000FD2,
    "Fire Whip": 0x00000FDC,
    "Chaos Fire Whip": 0x000011A8,
    "Poison Mist": 0x00001068,
    "Toxic Mist": 0x00001072,
    "Acid Surge": 0x0000107C,
    "Flash Sweat": 0x000010D6,
    "Iron Flesh": 0x000010CC,
    "Power Within": 0x00001130,
    "Undead Rapport": 0x00001108,
    "Black Flame": 0x000011B2,
    # Miracles
    "Heal": 0x00001388,
    "Great Heal Excerpt": 0x0000139C,
    "Great Heal": 0x00001392,
    "Soothing Sunlight": 0x000013A6,
    "Replenishment": 0x000013B0,
    "Bountiful Sunlight": 0x000013BA,
    "Force": 0x000014B4,
    "Wrath of the Gods": 0x000014BE,
    "Emit Force": 0x000014C8,
    "Magic Barrier": 0x000015E0,
    "Great Magic Barrier": 0x000015EA,
    "Homeward": 0x0000145A,
    "Seek Guidance": 0x00001518,
    "Karmic Justice": 0x00001644,
    "Vow of Silence": 0x000016B2,
    "Tranquil Walk of Peace": 0x000016A8,
    "Lightning Spear": 0x0000157C,
    "Great Lightning Spear": 0x00001586,
    "Sunlight Spear": 0x00001590,
    "Sunlight Blade": 0x0000170C,
    "Darkmoon Blade": 0x00001716,
    "Gravelord Sword Dance": 0x000013EC,
    "Gravelord Greatsword Dance": 0x000013F6,
}

misc_items_table = {
    "Skull Lantern": 0x00154D20,
    "Binoculars": 0x00000173,
    "Darksign": 0x00000075,
    "Dragon Head Stone": 0x00000179,
    "Dragon Torso Stone": 0x0000017A,
    "Black Eye Orb": 0x00000073,
}

dlc_misc_items_table = {
    "Silver Pendant": 0x000000DC,
}

}

firekeeper_souls_table = {
    "Soul of the Ash Maiden": 0x00000186,
    "Soul of the Darkmoon Knightess": 0x00000187,
    "Soul of a Daughter of Chaos": 0x00000188,
    "Firekeeper Soul #1": 0x00000189,
    "Firekeeper Soul #2": 0x0000018A,
    "Firekeeper Soul #3": 0x0000018B,
    "Firekeeper Soul #4": 0x0000018C,
}

misc_souls_table = {
    "Soul of a Lost Undead": 0x00000190,
    "Large Soul of a Lost Undead": 0x00000191,
    "Soul of a Nameless Soldier": 0x00000192,
    "Large Soul of a Nameless Soldier": 0x00000193,
    "Soul of a Proud Knight": 0x00000194,
    "Large Soul of a Proud Knight": 0x00000195,
    "Soul of a Brave Warrior": 0x00000196,
    "Large Soul of a Brave Warrior": 0x00000197,
    "Soul of a Hero": 0x00000198,
    "Soul of a Great Hero": 0x00000199,
}

embers_table = {
    "Large Ember": 0x00000329,
    "Very Large Ember": 0x00000321,
    "Divine Ember": 0x00000328,
    "Large Divine Ember": 0x00000329,
    "Dark Ember": 0x0000032A,
    "Large Magic Ember": 0x00000326,
    "Enchanted Ember": 0x0000327,
    "Crystal Ember": 0x00000322,
    "Large Flame Ember": 0x0000032C,
    "Chaos Flame Ember": 0x0000032D,
}

key_items_table = {
    "Lordvessel": 0x000009CE,
    # TODO Seath and FK are both Bequeathed Lord Souls, which is which?
    "Soul of the Four Kings": 0x000009C6,
    "Soul of Seath the Scaleless": 0x000009C7,
    # TODO Nito and BoC are both Lord Souls, which is which?
    "Soul of Gravelord Nito": 0x000009C4,
    "Soul of Bed of Chaos": 0x000009C5,
}

boss_souls_table = {
    "Soul of the Moonlight Butterfly": 0x000002C1,
    "Soul of Quelaag": 0x000002BC,
    "Core of an Iron Golem": 0x000002BF,
    "Soul of Gwyndolin": 0x000002C4,
    "Soul of Ornstein": 0x000002C0,
    "Soul of Smough": 0x000002C2,
    "Soul of Sif": 0x000002BD,
    "Soul of Priscilla": 0x000002C3,
    "Soul of Gwyn, Lord of Cinder": 0x000002BE,
}

dlc_boss_souls_table = {
    "Guardian Soul": 0x000002C5,
    "Soul of Artorias": 0x000002C6,
    "Soul of Manus": 0x000002C7,
}

keys_table = {
    "Master Key": 0x00000834,
    "Dungeon Cell Key": 0x000007DA,
    "Undead Asylum F2 East Key": 0x000007DC,
    "Undead Asylum F2 West Key": 0x000007E0,
    "Big Pilgrim's Key": 0x000007DB,
    "Residence Key": 0x000007E5,
    "Mystery Key": 0x000007E1,
    "Basement Key": 0x00007D1,
    "Key to Depths": 0x000007DE,
    "Sewer Chamber Key": 0x000007E2,
    "Blighttown Key": 0x000007D7,
    "Watchtower Basement Key": 0x000007E3,
    "Key to New Londo Ruins": 0x000007D8,
    "Key to the Seal": 0x000007DD,
    "Cage Key": 0x000007D3,
    "Archive Tower Cell Key": 0x000007D4,
    "Archive Prison Extra Key": 0x000007E4,
    "Archive Tower Giant Door Key": 0x000007D5,
    "Archive Tower Giant Cell Key": 0x000007D6,
    "Annex Key": 0x000007D9,
    "Crest of Artorias": 0x000007D2,
    "Peculiar Doll": 0x00000180,
}

dlc_keys_table = {
    "Broken Pendant": 0x000009D8,
    "Crest Key": 0x000007E6,
}