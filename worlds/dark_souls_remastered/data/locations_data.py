northern_undead_asylum_table = {
    # TODO Prepare logic to prevent immediate BK or softlock
    # "NUA: Dungeon Cell Key": 0x000007DA,  # On corpse dropped into cell
    # TODO How do these work?
    # "NUA: Shield": 0,  # Equip Tutorial
    # "NUA: Weapon/Catalyst": 0,  # Equip Tutorial
    # TODO Add setting to force this here
    # "NUA: Estus Flask": 0x000000C8,  # Oscar's 1st item
    "NUA: Undead Asylum F2 East Key": 0x000007DC,  # Oscar's 2nd item
    "NUA: Big Pilgrim's Key": 0x000007DB,  # Asylum Demon 1st item
}

northern_undead_asylum_revisit_table = {
    "NUAR: Peculiar Doll": 0x00000180,  # Only available during revisit
    "NUAR: Rusted Iron Ring": 0x0000007D  # Behind the locked F2 West door
}

firelink_shrine_table = {
    "FS: Binoculars": 0x00000173,  # Edge of graveyard
    "FS: Zweihander": 0x00055730,  # Large gravestone #2
    "FS: Morning Star": 0x000C3CD0,  # Elevator shaft chest (shared w/Talisman)
    "FS: Talisman": 0x0014C080,  # Elevator shaft chest (shared w/Morningstar)
    "FS: Winged Spear": 0x000F4628,  # Large gravestone #1
    "FS: Caduceus Round Shield": 0x001583D0,  # Lower graveyard spot
    "FS: Ring of Sacrifice": 0x0000007E,  # Next to where Domhnall of Zena sits
}

undead_burg_table = {
    "UB: Wooden Shield": 0x001560A8,  # Behind door near bonfire
    "UB: Light Crossbow": 0x001312D0,  # 2nd floor balcony near entrance
    "UB: Claymore": 0x000497C8,  # Bridge YOLO run
}

lower_undead_burg_table = {
    "LUB: Mail Breaker": 0x000927C0,  # In one of the right rooms after ambush
    "LUB: Thief Mask": 0x000493E0,  # In one of the right rooms after ambush
    "LUB: Black Leather Armor": 0x000497C8,  # In one of the right rooms after ambush
    "LUB: Black Leather Gloves": 0x00049BB0,  # In one of the right rooms after ambush
    "LUB: Black Leather Boots": 0x00049F98,  # In one of the right rooms after ambush
    "LUB: Target Shield": 0x00156C60,  # In one of the right rooms after ambush
    "LUB: Sorcerer Hat": 0x00035B60,  # Behind Residence Key door in barrel
    "LUB: Sorcerer Cloak": 0x00035F48,  # Behind Residence Key door in barrel
    "LUB: Sorcerer Gauntlets": 0x00036330,  # Behind Residence Key door in barrel
    "LUB: Sorcerer Boots": 0x00036718,  # Behind Residence Key door in barrel
    "LUB: Sorcerer's Catalyst": 0x0013D620,  # Behind Residence Key door in barrel
    "LUB: Key to Depths": 0x000007DE,  # Capra Demon reward
}

undead_parish_table = {
    "UP: Knight Shield": 0x001623F8,  # Lonely Balder Knight
    "UP: Mystery Key": 0x000007E1,  # In cellar behind boar
    "UP: Basement Key": 0x00007D1,  # Behind gate
    "UP: Halberd": 0x0010C8E0,  # Top of gate stairs before church
    "UP: Fire Keeper Soul": 0x00000189,  # Church
    "UP: Ring of Favor and Protection": 0x0000008F,  # Drops from Knight Lautrec
}

depths_table = {
    "D: Large Ember": 0x00000329,  # Butcher chest
    "D: Spider Shield": 0x00164EF0,  # Above the giant rat
    "D: Greataxe": 0x000B71B0,  # Corpse surrounded by rats
    "D: Ring of the Evil Eye": 0x0000008E,  # Corpse past two basilisks
    "D: Blighttown Key": 0x000007D7,  # Gaping Dragon reward
    "D: Standard Helm": 0x00033450,  # Corpse in Gaping Dragon arena 1st item
    "D: Hard Leather Armor": 0x00033838,  # Corpse in Gaping Dragon arena 2nd item
    "D: Hard Leather Gauntlets": 0x00033C20,  # Corpse in Gaping Dragon arena 3rd item
    "D: Hard Leather Boots": 0x00034008,  # Corpse in Gaping Dragon Arena 4th item
}

blighttown_table = {
    "B: Iaito": 0x0007A8F0,  # Corpse across the gap
    "B: Shadow Mask": 0x0000EA60,  # Corpse near bonfire 1st item
    "B: Shadow Garb": 0x0000EE48,  # Corpse near bonfire 2nd item
    "B: Shadow Gauntlets": 0x0000F230,  # Corpse near bonfire 3rd item
    "B: Shadow Leggings": 0x0000F618,  # Corpse near bonfire 4th item
    "B: Eagle Shield": 0x0016E360,  # Corpse at the end of the stone walkway
    "B: Mask of the Sealer": 0x000222E0,  # Corpse past Cragspider 1st item
    "B: Crimson Robes": 0x000226C8,  # Corpse past Cragspider 2nd item
    "B: Crimson Gloves": 0x00022AB0,  # Corpse past Cragspider 3rd item
    "B: Crimson Waistcloth": 0x00022E98,  # Corpse past Cragspider 4th item
    "B: Tin Banishment Catalyst": 0x0013DDF0,  # Corpse past Cragspider 5th item
    "B: Remedy": 0x00000E1A,  # Chest next to Crimson Set corpse
    "B: Power Within": 0x00001130,  # Corpse below blowdart sniper
    "B: Whip": 0x00186A00,  # Corpse near fog gate
    "B: Wanderer Hood": 0x00057E40,  # Corpse next to blowdart sniper 1st item
    "B: Wanderer Coat": 0x00058228,  # Corpse next to blowdart sniper 2nd item
    "B: Wanderer Manchette": 0x00058610,  # Corpse next to blowdart sniper 3rd item
    "B: Wanderer Boots": 0x00589F8,  # Corpse next to blowdart sniper 4th item
    "B: Falchion": 0x00061E68,  # Corpse next to blowdart sniper 5th item
    # TODO should the following item be randomized since it's guaranteed?
    # "B: Butcher Knife": 0,  # Maneater Mildred reward (must be in human form)
    "B: Great Club": 0x000CF850,  # Guarded by two Infested Barbarians
    "B: Poison Mist": 0x00001068,  # Corpse near wall 1st item
    "B: Tattered Cloth Hood": 0x00038270,  # Corpse near wall 2nd item
    "B: Tattered Cloth Robe": 0x00038658,  # Corpse near wall 3rd item
    "B: Tattered Cloth Manchette": 0x00038A40,  # Corpse near wall 4th item
    "B: Heavy Boots": 0x00038E28,  # Corpse near wall 5th item
    "B: Server": 0x0006DDD0,  # Leech party corpse
    "B: Plank Shield": 0x00157FE8,  # Corpse in tree alcove
    "B: Key to New Londo Ruins": 0x000007D8,  # Cave chest near Valley of Drakes
}

quelaags_domain_table = {
    "QD: Soul of Quelaag": 0x000002BC,  # Quelaag reward
}

the_great_hollow_table = {
    "GH: Cloranthy Ring": 0x00000068,  # Hollow tree dive
}

ash_lake_table = {
    "Lake: Great Magic Barrier": 0x000015EA,  # Hidden log path into tree
    "Lake: Dragon Greatsword": 0x000566D0,  # Everlasting Dragon Tail
}

sens_fortress_table = {
    "SF: Scythe": 0x0010E438,  # Tunnel behind Titanite Demon
    "SF: Ring of Steel Protection": 0x00000078,  # Chest in room behind outside boulder staircase
    "SF: Shotel": 0x00062250,  # On the ledge next to outdoor staircase
    "SF: Covetous Gold Serpent Ring": 0x00000079,  # On windowsill corpse behind stacked boulder wall
    "SF: Lightning Spear": 0x000F4308,  # Mimic reward
    "SF: Black Sorcerer Hat": 0x0009C400,  # Corpse on Man-Serpent Mage platform 1st item
    "SF: Black Sorcerer Cloak": 0x0009C7E8,  # Corpse on Man-Serpent Mage platform 2nd item
    "SF: Black Sorcerer Gauntlets": 0x0009CBD0,  # Corpse on Man-Serpent Mage platform 3rd item
    "SF: Black Sorcerer Boots": 0x0009CFB8,  # Corpse on Man-Serpent Mage platform 4th item
    "SF: Hush": 0x00000DB6,  # Corpse on Man-Serpent Mage platform 5th item
    "SF: Slumbering Dragoncrest Ring": 0x0000007B,  # Through hole in wall on Man-Serpent Mage platform
    "SF: Flame Stoneplate Ring": 0x00000069,  # Chest behind two Balder Knights on top of the fortress
    "SF: Ricard's Rapier": 0x00093760,  # Drops from Ricard the Archer on the stairs
    "SF: Sniper Crossbow": 0x00131E88,  # Corpse near Firebomb Giant
    "SF: Cage Key": 0x000007D3,  # On a corpse below the Crestfallen Merchant
    "SF: Core of an Iron Golem": 0x000002BF,
}

anor_londo_table = {
    "AL: Crystal Halberd": 0x000002BF,  # Mimic chest near Duke's Archives
    "AL: Ring of the Sun's Firstborn": 0x00000094,  # Next to Darkmoon Tomb bonfire
    "AL: Great Magic Weapon": 0x00000C26,  # Near fallen chandelier in chapel
    "AL: Black Iron Helm": 0x00011170,  # Tarkus' corpse near painting 1st item
    "AL: Black Iron Armor": 0x00011558,  # Tarkus' corpse near painting 2nd item
    "AL: Black Iron Gauntlets": 0x00011940,  # Tarkus' corpse near painting 3rd item
    "AL: Black Iron Leggings": 0x00011D28,  # Tarkus' corpse near painting 4th item
    "AL: Greatsword": 0x00055B18,  # Tarkus' corpse near painting 5th item
    "AL: Black Iron Greatshield": 0x00895FF8,  # Tarkus' corpse near painting 6th item
    "AL: Havel's Helm": 0x0006B6C0,  # Room behind fireplace chest
    "AL: Havel's Armor": 0x0006BAA8,  # Room behind fireplace chest
    "AL: Havel's Gauntlets": 0x0006BE90,  # Room behind fireplace chest
    "AL: Havel's Leggings": 0x0006C278,  # Room behind fireplace chest
    "AL: Havel's Greatshield": 0x0016F6E8,  # Room behind fireplace chest
    "AL: Dragon Tooth": 0x000D07F0,  # Room behind fireplace chest
    "AL: Occult Club": 0x000D07F0,  # Room behind fireplace chest Mimic reward
    "AL: Silver Knight Helm": 0x000668A0,  # One of two chests in room guarded by two Silver Knights
    "AL: Silver Knight Armor": 0x00066C88,  # One of two chests in room guarded by two Silver Knights
    "AL: Silver Knight Gauntlets": 0x00067070,  # One of two chests in room guarded by two Silver Knights
    "AL: Silver Knight Leggings": 0x00067458,  # One of two chests in room guarded by two Silver Knights
    "AL: Dragonslayer Greatbow": 0x001E9FD8,  # Through the broken window
    "AL: Hawk Ring": 0x00000077,  # Chest next to Giant Blacksmith
    # TODO How to handle O&S loot? Give everything? Duplicate the check between the souls?
    # Only dropped if you kill Smough first.
    # "AL: Leo Ring": 0x00000090,
    # "AL: Soul of Ornstein": 0x000002C0,
    # Only dropped if you kill Ornstein first.
    # "AL: Soul of Smough": 0x000002C2,
    "AL: Lordvessel": 0x000009CE,  # Given by Gwynevere
}

# Requires Peculiar Doll to access
painted_world_of_ariamis_table = {
    "PWA: Painting Guardian Hood": 0x0003D090,  # Chest past two Snow Rats in house
    "PWA: Painting Guardian Robe": 0x0003D478,  # Chest past two Snow Rats in house
    "PWA: Painting Guardian Gloves": 0x0003D860,  # Chest past two Snow Rats in house
    "PWA: Painting Guardian Waistcloth": 0x0003DC48,  # Chest past two Snow Rats in house
    "PWA: Velka's Rapier": 0x00093378,  # Ledge above annex
    "PWA: Acid Surge": 0x0000107C,  # Behind stairs near impaled corpses
    "PWA: Fire Surge": 0x00000FD2,  # Drops from Engorged Hollow at top of stairs
    "PWA: Annex Key": 0x000007D9,  # Drops from Bonewheel behind an illusory wall
    "PWA: Dark Ember": 0x0000032A,  # Past the Harpies after opening the annex
    "PWA: Vow of Silence": 0x000016B2,  # Past an Engorged Hollow and a couple Harpies
    "PWA: Mask of Velka": 0x000249F0,  # On a corpse up some stairs near the Vow of Silence 1st item
    "PWA: Black Cleric Robe": 0x00024DD8,  # On a corpse up some stairs near the Vow of Silence 2nd item
    "PWA: Black Manchette": 0x000251C0,  # On a corpse up some stairs near the Vow of Silence 3rd item
    "PWA: Black Tights": 0x000255A8,  # On a corpse up some stairs near the Vow of Silence 4th item
    "PWA: Soul of Priscilla": 0x000002C3,  # Reward from Crossbreed Priscilla
    # TODO Should Xanthous King Jeremiah be in the loot table? It would add 4 additional checks
}

darkroot_garden_table = {
    "DG: Wolf Ring": 0x00000092,  # On ledge past a Great Stone Knight
    "DG: Partizan": 0x000F4A10,  # In small passage next to a Tree Lizard
    "DG: Soul of the Moonlight Butterfly": 0x000002C1,  # Reward from Moonlight Butterfly
    "DG: Basement Key": 0x00007D1,  # In tower after Moonlight Butterfly
    "DG: Divine Ember": 0x00000328,  # On crouching smith after Moonlight Butterfly
    "DG: Elite Knight Helm": 0x00055730,  # On corpse surrounded by Great Stone Knights and Ents
    "DG: Elite Knight Armor": 0x00055B18,  # On corpse surrounded by Great Stone Knights and Ents
    "DG: Elite Knight Gauntlets": 0x00055F00,  # On corpse surrounded by Great Stone Knights and Ents
    "DG: Elite Knight Leggings": 0x000562E8,  # On corpse surrounded by Great Stone Knights and Ents
    "DG: Stone Helm": 0x0001D4C0,  # Chest after bridge and room with Alvina
    "DG: Stone Armor": 0x0001D8A8,  # Chest after bridge and room with Alvina
    "DG: Stone Gauntlets": 0x0001DC90,  # Chest after bridge and room with Alvina
    "DG: Stone Leggings": 0x0001E078,  # Chest after bridge and room with Alvina
    "DG: Black Bow of Pharis": 0x00125750,  # Drops from Pharis
    "DG: Pharis' Hat": 0x0003A980,  # Drops from Pharis
    "DG: Dark Wood Grain Ring": 0x00000080,  # Drops from Shiva's ninja bodyguard
    "DG: Eastern Helm": 0x000445C0,
    "DG: Eastern Armor": 0x000449A8,
    "DG: Eastern Gauntlets": 0x00044D90,
    "DG: Eastern Leggings": 0x00045178,
    "DG: Enchanted Ember": 0x00000328,  # Chest in pool of water surrounded by Large Mushroom People
    "DG: Soul of Sif": 0x000002BD,  # Reward from Sif
    "DG: Covenant of Artorias": 0x0000008A,  # Reward from Sif, needed for Four Kings
    "DG: Hornet Ring": 0x00000075,  # Behind Artorias' gravestone
}

darkroot_basin_table = {
    "DB: Leather Armor": 0x0003AD68,  # Corpse halfway down 1st item
    "DB: Leather Gloves": 0x0003B150,  # Corpse halfway down 2nd item
    "DB: Leather Boots": 0x0003B538,  # Corpse halfway down 3rd item
    "DB: Longbow": 0x00125368,  # Corpse halfway down 4th item
    "DB: Grass Crest Shield": 0x00162BC8,  # Guarded by Black Knight near bottom
    "DB: Havel's Ring": 0x00000064,  # Dropped by Havel the Rock
    "DB: Dusk Crown Ring": 0x00000074,  # Dropped by Hydra
    "DB: Knight Helm": 0x0005F370,  # Near shoreline of Hydra fight
    "DB: Knight Armor": 0x0005F758,  # Near shoreline of Hydra fight
    "DB: Knight Gauntlets": 0x0005FB40,  # Near shoreline of Hydra fight
    "DB: Knight Leggings": 0x0005FF28,  # Near shoreline of Hydra fight
    "DB: Crown of Dusk": 0x00050910,  # In cave after beating the Golden Crystal Golem
    "DB: Antiquated Dress": 0x00050CF,  # In cave after beating the Golden Crystal Golem8,
    "DB: Antiquated Gloves": 0x000510E0,  # In cave after beating the Golden Crystal Golem
    "DB: Antiquated Skirt": 0x000514C8,  # In cave after beating the Golden Crystal Golem
}

new_londo_ruins_table = {
    "NLR: Estoc": 0x00092F90,  # Pot Corpse
    "NLR: Fire Keeper Soul": 0x0000018A,  # Ghost YOLO run
    "NLR: Parrying Dagger": 0x00018A88,  # Corpse down a spiral staircase
    "NLR: Key to the Seal": 0x000007DD,  # Given/Dropped by Ingward
    "NLR: Composite Bow": 0x00125F20,  # Corpse up the spiral staircase near Ingward
}

# Requires Key to the Seal to access
lower_new_londo_ruins_table = {
    "LNLR: Very Large Ember": 0x00000321,  # In a chest up the right doorway staircase
}

# Requires Covenant of Artorias to access
the_abyss_table = {
    "TA: Soul of the Four Kings": 0x000009C6,  # TODO Determine which Bequeathed Lord Soul this is.
}

# Requires Lordvessel to access
the_dukes_archives_table = {
    "DA: Broken Pendant": 0x000009D8,  # Dropped by Crystal Golem to right of doorway after rescuing Dusk
    "DA: Crystal Knight Shield": 0x000009D8,  # Mimic chest guarded by two Crystal Soldiers
    "DA: Large Magic Ember": 0x00000326,  # Chest in the first Seath arena after defeating him
    # TODO Figure out the logic so a majority of runs don't softlock or BK here.
    "DA: Archive Tower Cell Key": 0x000007D4,  # Drops from the Serpent Soldier guarding your cell
    "DA: Archive Prison Extra Key": 0x000007E4,  # Dropped by one of the caged Crystal Soldiers
    "DA: Maiden Hood": 0x00064190,  # Inside a cell accessed through a hole
    "DA: Maiden Robe": 0x00064578,  # Inside a cell accessed through a hole
    "DA: Maiden Gloves": 0x00064960,  # Inside a cell accessed through a hole
    "DA: Maiden Skirt": 0x00064D48,  # Inside a cell accessed through a hole
    "DA: White Seance Ring": 0x00000072,  # Inside a cell accessed through a hole
    # TODO Figure out the logic so a majority of runs don't *also* softlock or BK here.
    "DA: Archive Tower Giant Door Key": 0x000007D5,  # Retrieved from a chest on a balcony
    "DA: Soothing Sunlight": 0x000013A6,  # Drops from a non-aggressive Pisaca
    "DA: Bountiful Sunlight": 0x000013BA,  # Drops from a non-aggressive Pisaca
    "DA: Avelyn": 0x00131AA0,  # In a chest atop a tall bookcase
    "DA: Enchanted Falchion": 0x00006205C,  # Reward from Mimic
    "DA: Crystalline Helm": 0x0001FBD0,
    "DA: Crystalline Armor": 0x0001FFB8,
    "DA: Crystalline Gauntlets": 0x000203A0,
    "DA: Crystalline Leggings": 0x00020788,
}

# Requires Lordvessel to access
crystal_cave_table = {
    # "CC: Moonlight Greatsword": 0,  # Drops when Seath's tail is cut off
    "CC: Soul of Seath the Scaleless": 0x000009C7,  # TODO Determine which Bequeathed Lord Soul this is.
}

demon_ruins_table = {
    "DR: Gold-Hemmed Black Hood": 0x000704E0,  # On the altar next to Ceaseless Discharge
    "DR: Gold-Hemmed Black Cloak": 0x000708C8,  # On the altar next to Ceaseless Discharge
    "DR: Gold-Hemmed Black Gloves": 0x00070CB0,  # On the altar next to Ceaseless Discharge
    "DR: Gold-Hemmed Black Skirt": 0x00071098,  # On the altar next to Ceaseless Discharge
    "DR: Large Flame Ember": 0x0000032C,  # Chest guarded by several Rockworms
    "DR: Demon's Catalyst": 0x0013F178,  # Drops from Demon Firesage
    "DR: Orange Charred Ring": 0x0000008B,  # Drop from Centipede Demon
}

# Requires Lordvessel to access
lost_izalith_table = {
    "LI: Sunlight Maggot": 0x0002E630,  # Dropped by either Solaire or the red-eyed Chaos Bug
    "LI: Soul of Bed of Chaos": 0x000009C5,
}

the_catacombs_table = {
    "TC: Great Scythe": 0x00118C30,  # On a platform near lever
    "TC: Darkmoon Seance Ring": 0x00000095,  # Behind a fragile wall after Vamos
    "TC: Rite of Kindling": 0x00000A2F,  # Reward from Pinwheel
    "TC: Mace": 0x000C38E8,  # On a shortcut ledge
    "TC: Priest's Hat": 0x0004BAF0,  # On a shortcut ledge
    "TC: Holy Robe": 0x0004BED8,  # On a shortcut ledge
    "TC: Holy Trousers": 0x0004C6A8,  # On a shortcut ledge
    # TODO Should each of these be mapped to the same item? It's not required.
    # "TC: Mask of the Father": 0,
    # "TC: Mask of the Mother": 0,
    # "TC: Mask of the Child": 0,
}

tomb_of_giants_table = {
    "TG: Skull Lantern": 0x00154D20,  # On a corpse in the pit below Patches
    "TG: Large Divine Ember": 0x00000329,  # On a blacksmith corpse on the left path past the illusory wall
    "TG: Effigy Shield": 0x00895440,  # At the end of the right path past the fog gate
    "TG: Covetous Silver Serpent Ring": 0x0000007A,  # On a corpse after a jump
    "TG: Soul of Gravelord Nito": 0x000009C4,
}

# Requires the Lordvessel and every lord soul
kiln_of_the_first_flame_table = {
    "KFF: Black Knight Helm": 0x0004E200,
    "KFF: Black Knight Armor": 0x0004E5E8,
    "KFF: Black Knight Gauntlets": 0x0004E9D0,
    "KFF: Black Knight Leggings": 0x0004EDB8,
}

the_valley_of_the_drakes_table = {
    "VD: Astora's Straight Sword": 0x00033068,  # Guarded by the Undead Dragon
    "VD: Dragon Crest Shield": 0x00163B68,  # Guarded by the Undead Dragon
    "VD: Brigand Hood": 0x0000C350,  # On a corpse past the Drake on the bridge
    "VD: Brigand Armor": 0x0000C738,  # On a corpse past the Drake on the bridge
    "VD: Brigand Gauntlets": 0x0000CB20,  # On a corpse past the Drake on the bridge
    "VD: Brigand Trousers": 0x0000CF08,  # On a corpse past the Drake on the bridge
    "VD: Spider Shield": 0x00164EF0,  # On a corpse past the Drake on the bridge
    "VD: Red Tearstone Ring": 0x00000065,  # On top of the tower with the ladder
    "VD: Beatrice's Catalyst": 0x0013DA08,  # At the edge of a cliff after beating Four Kings
    "VD: Witch Hat": 0x00053020,  # At the edge of a cliff after beating Four Kings
    "VD: Witch Cloak": 0x00053408,  # At the edge of a cliff after beating Four Kings
    "VD: Witch Gloves": 0x000537F0,  # At the edge of a cliff after beating Four Kings
    "VD: Witch Skirt": 0x00053BD8,  # At the edge of a cliff after beating Four Kings
}

# DLC
sanctuary_garden_table = {
    "SG: Guardian Soul": 0x000002C5,
}

# DLC
royal_wood_table = {
    "RW: Guardian Helm": 0x000A8750,  # Across a gap
    "RW: Guardian Armor": 0x000A8B38,  # On a corpse hanging from a cliff near bushes
    "RW: Guardian Gauntlets": 0x000A8F20,  # Inside the stone tower
    "RW: Guardian Leggings": 0x000A9308,  # On a corpse near a flower bed
    "RW: Soul of Artorias": 0x000002C6,  # Reward from Artorias the Abysswalker o7
    "RW: Calamity Ring": 0x00000096,  # Reward from Black Dragon Kalameet
}

# DLC
oolacile_township_table = {
    "OT: Silver Pendant": 0x000000DC,  # Behind a special illusory wall that requires light
    "OT: Dark Orb": 0x00000E7E,  # In the chest down the stairs
    "OT: Crest Key": 0x000007E6,  # Reward from Mimic
    "OT: Dark Fog": 0x00000E92,  # On a corpse next to a Corrupted Sorcerer
    # TODO Chained Prisoner Drops?
    # TODO Carvings?
}

# DLC
chasm_of_the_abyss_table = {
    "CA: Dark Bead": 0x00000E88,  # Guarded by several Oolacile Residents and a Sorceress
    "CA: Cleansing Greatshield": 0x00898AF0,  # Reward from saving Sif (best doggo)
    "CA: Black Flame": 0x000011B2,  # Guarded by several Giant Humanities
    "CA: Soul of Manus": 0x000002C7,  # Reward from Manus, Father of the Abyss
}

location_tables = [northern_undead_asylum_table, northern_undead_asylum_revisit_table, firelink_shrine_table,
                   undead_burg_table, lower_undead_burg_table, undead_parish_table, depths_table, blighttown_table,
                   quelaags_domain_table, the_great_hollow_table, ash_lake_table, sens_fortress_table, anor_londo_table,
                   painted_world_of_ariamis_table, darkroot_garden_table, darkroot_basin_table, new_londo_ruins_table,
                   lower_new_londo_ruins_table, the_abyss_table, the_dukes_archives_table, crystal_cave_table,
                   demon_ruins_table, lost_izalith_table, the_catacombs_table, tomb_of_giants_table,
                   kiln_of_the_first_flame_table, the_valley_of_the_drakes_table, sanctuary_garden_table,
                   royal_wood_table, oolacile_township_table, chasm_of_the_abyss_table]

location_dictionary = {**northern_undead_asylum_table, **northern_undead_asylum_revisit_table, **firelink_shrine_table,
                       **undead_burg_table, **lower_undead_burg_table, **undead_parish_table, **depths_table,
                       **blighttown_table, **quelaags_domain_table, **the_great_hollow_table, **ash_lake_table,
                       **sens_fortress_table, **anor_londo_table, **painted_world_of_ariamis_table,
                       **darkroot_garden_table, **darkroot_basin_table, **new_londo_ruins_table,
                       **lower_new_londo_ruins_table, **the_abyss_table, **the_dukes_archives_table,
                       **crystal_cave_table, **demon_ruins_table, **lost_izalith_table, **the_catacombs_table,
                       **tomb_of_giants_table, **kiln_of_the_first_flame_table, **the_valley_of_the_drakes_table,
                       **sanctuary_garden_table, **royal_wood_table, **oolacile_township_table,
                       **chasm_of_the_abyss_table}
