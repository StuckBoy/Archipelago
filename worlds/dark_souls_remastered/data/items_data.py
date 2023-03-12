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
    "Quelaag's Furysword": 123450,
    "Falchion": 0x00061E68,
    "Shotel": 0x00062250,
    "Painting Guardian Sword": 0x00062E08,
    "Jagged Ghost Blade": 0x00062638,
    # Katanas
    "Uchigatana": 0x0007A120,
    # TODO Multiple IDs, how does this work?
    "Chaos Blade": 123450,
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
    # TODO Multiple IDs, how does this work?
    "Golem Axe": 123450,
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
    "Smough's Hammer": 123450,
    "Large Club": 123450,
    "Great Club": 123450,
    "Demon's Great Hammer": 123450,
    "Grant": 123450,
    "Dragon Tooth": 123450,
    # Fist Weapons
    "Dragon Bone Fist": 123450,
    "Caestus": 123450,
    "Claws": 123450,
    "Dark Hand": 123450,
    # Spears
    "Spear": 123450,
    "Winged Spear": 123450,
    "Partizan": 123450,
    "Dragonslayer Spear": 123450,
    "Moonlight Butterfly Horn": 123450,
    "Pike": 123450,
    "Channeler's Trident": 123450,
    "Demon's Spear": 123450,
    "Silver Knight Spear": 123450,
    # Halberds
    "Halberd": 123450,
    "Lifehunt Scythe": 123450,
    "Lucerne": 123450,
    "Scythe": 123450,
    "Gargoyle's Halberd": 123450,
    "Giant's Halberd": 123450,
    "Titanite Catch Pole": 123450,
    "Black Knight Halberd": 123450,
    "Great Scythe": 123450,
    # Whips
    "Whip": 123450,
    "Notched Whip": 123450,
    # Bows
    "Short Bow": 123450,
    "Composite Bow": 123450,
    "Darkmoon Bow": 123450,
    "Longbow": 123450,
    "Black Bow of Pharis": 123450,
    # Greatbows
    "Dragonslayer Greatbow": 123450,
    # Crossbows
    "Light Crossbow": 123450,
    "Heavy Crossbow": 123450,
    "Sniper Crossbow": 123450,
    "Avelyn": 123450,
    # Catalysts
    "Sorcerer's Catalyst": 123450,
    "Tin Darkmoon Catalyst": 123450,
    "Beatrice's Catalyst": 123450,
    "Logan's Catalyst": 123450,
    # TODO Determine if DLC or not
    "Oolacile Ivory Catalyst": 123450,
    "Demon's Catalyst": 123450,
    "Izalith Catalyst": 123450,
    "Tin Banishment Catalyst": 123450,
    "Tin Crystallization Catalyst": 123450,
    # Flames
    "Pyromancy Flame": 123450,
    "Pyromancy Flame (Upgraded)": 123450,
    # Talismans
    "Talisman": 123450,
    "Canvas Talisman": 123450,
    "Thorolund Talisman": 123450,
    "Ivory Talisman": 123450,
    "Sunlight Talisman": 123450,
    "Darkmoon Talisman": 123450,
    "Velka's Talisman": 123450,
}

dlc_weapons_table = {
    # Daggers
    "Dark Silver Tracer": 0x00897F38,
    # Greatswords
    "Abyss Greatsword": 123450,
    "Obsidian Greatsword": 123450,
    # Curved Swords
    "Gold Tracer": 123450,
    # Spears
    "Four-pronged Plow": 123450,
    # Whips
    "Guardian Tail": 123450,
    # Greatbows
    "Gough's Greatbow": 123450,
    # Catalysts
    "Manus Catalyst": 123450,
    "Oolacile Catalyst": 123450,
}

shield_table = {
    # Small
    "Warrior's Round Shield": 123450,
    "Caduceus Round Shield": 123450,
    "Effigy Shield": 123450,
    # TODO Are ampersand's accepted?
    "Red & White Round Shield": 123450,
    "Cracked Round Shield": 123450,
    "Plank Shield": 123450,
    "Small Leather Shield": 123450,
    "Leather Shield": 123450,
    "Buckler": 123450,
    "Target Shield": 123450,
    "Crystal Ring Shield": 123450,
    # Standard
    "East-West Shield": 123450,
    "Wooden Shield": 123450,
    "Large Leather Shield": 123450,
    "Heater Shield": 123450,
    "Tower Kite Shield": 123450,
    "Caduceus Kite Shield": 123450,
    "Hollow Soldier Shield": 123450,
    "Knight Shield": 123450,
    "Sanctus": 123450,
    "Balder Shield": 123450,
    "Spider Shield": 123450,
    "Grass Crest Shield": 123450,
    "Bloodshield": 123450,
    "Iron Round Shield": 123450,
    "Sunlight Shield": 123450,
    "Pierce Shield": 123450,
    "Spiked Shield": 123450,
    "Gargoyle's Shield": 123450,
    "Crystal Shield": 123450,
    "Crest Shield": 123450,
    "Dragon Crest Shield": 123450,
    "Black Knight Shield": 123450,
    # Greatshields
    "Greatshield of Artorias": 123450,
    "Eagle Shield": 123450,
    "Tower Shield": 123450,
    "Black Iron Greatshield": 123450,
    "Giant Shield": 123450,
    "Bonewheel Shield": 123450,
    "Stone Greatshield": 123450,
    "Havel's Greatshield": 123450,
}

dlc_shields_table = {
    # Greatshields
    "Cleansing Greatshield": 123450,
}

armor_table = {
    # Adventurer's Set
    "Helm of the Wise": 123450,
    "Armor of the Glorious": 123450,
    "Gauntlets of the Vanquisher": 123450,
    "Boots of the Explorer": 123450,
    # Dingy Set
    "Dingy Hood": 123450,
    "Dingy Robe": 123450,
    "Dingy Gloves": 123450,
    "Blood-Stained Skirt": 123450,
    # TODO Technically DLC, perhaps splitting them isn't necessary
    # Antiquated Set
    "Crown of Dusk": 123450,
    "Antiquated Dress": 123450,
    "Antiquated Gloves": 123450,
    "Antiquated Skirt": 123450,
    # Eastern Set
    "Eastern Helm": 123450,
    "Eastern Armor": 123450,
    "Eastern Gauntlets": 123450,
    "Eastern Leggings": 123450,
    # Maiden Set
    "Maiden Hood": 123450,
    "Maiden Robe": 123450,
    "Maiden Gloves": 123450,
    "Maiden Skirt": 123450,
    # Elite Knight Set
    "Elite Knight Helm": 123450,
    "Elite Knight Chest": 123450,
    "Elite Knight Gauntlets": 123450,
    "Elite Knight Leggings": 123450,
    # Ornstein's Set
    "Ornstein's Helm": 123450,
    "Ornstein's Armor": 123450,
    "Ornstein's Gauntlets": 123450,
    "Ornstein's Leggings": 123450,
    # Balder Set
    "Balder Helm": 123450,
    "Balder Armor": 123450,
    "Balder Gauntlets": 123450,
    "Balder Leggings": 123450,
    # Favor Set
    "Helm of Favor": 123450,
    "Embraced Armor of Favor": 123450,
    "Gauntlets of Favor": 123450,
    "Leggings of Favor": 123450,
    # Painting Guardian Set
    "Painting Guardian Hood": 123450,
    "Painting Guardian Robe": 123450,
    "Painting Guardian Gloves": 123450,
    "Painting Guardian Waistcloth": 123450,
    # Bandit Set
    "Brigand Hood": 123450,
    "Brigand Armor": 123450,
    "Brigand Gauntlets": 123450,
    "Brigand Trousers": 123450,
    # Giant Armor Set
    "Giant Helm": 123450,
    "Giant Armor": 123450,
    "Giant Gauntlets": 123450,
    "Giant Leggings": 123450,
    # Paladin Set
    "Paladin Helm": 123450,
    "Paladin Armor": 123450,
    "Paladin Gauntlets": 123450,
    "Paladin Leggings": 123450,
    # Big Hat's Set
    "Big Hat": 123450,
    "Sage Robe": 123450,
    "Travelling Gloves": 123450,
    "Travelling Boots": 123450,
    # Gold-Hemmed Black Set
    "Gold-Hemmed Black Hood": 123450,
    "Gold-Hemmed Black Cloak": 123450,
    "Gold-Hemmed Black Gloves": 123450,
    "Gold-Hemmed Black Skirt": 123450,
    # Pyromancer Set
    "Tattered Cloth Hood": 123450,
    "Tattered Cloth Robe": 123450,
    "Tattered Cloth Manchette": 123450,
    "Heavy Boots": 123450,
    # Black Iron Set
    "Black Iron Helm": 123450,
    "Black Iron Armor": 123450,
    "Black Iron Gauntlets": 123450,
    "Black Iron Leggings": 123450,
    # Great Lord Set
    "Crown of the Great Lord": 123450,
    "Robe of the Great Lord": 123450,
    "Bracelet of the Great Lord": 123450,
    "Anklet of the Great Lord": 123450,
    # Thorns Set
    "Helm of Thorns": 123450,
    "Armor of Thorns": 123450,
    "Gauntlets of Thorns": 123450,
    "Leggings of Thorns": 123450,
    # Black Knight Set
    "Black Knight Helm": 123450,
    "Black Knight Armor": 123450,
    "Black Knight Gauntlets": 123450,
    "Black Knight Leggings": 123450,
    # Gough's Set
    "Gough's Helm": 123450,
    "Gough's Chest": 123450,
    "Gough's Gloves": 123450,
    "Gough's Leggings": 123450,
    # Shadow Set
    "Shadow Mask": 123450,
    "Shadow Garb": 123450,
    "Shadow Gauntlets": 123450,
    "Shadow Leggings": 123450,
    # Black Set
    "Mask of Velka": 123450,
    "Black Cleric Robe": 123450,
    "Black Manchette": 123450,
    "Black Tights": 123450,
    # Guardian Set
    "Guardian Helm": 123450,
    "Guardian Armor": 123450,
    "Guardian Gauntlets": 123450,
    "Guardian Leggings": 123450,
    # Silver Knight Set
    "Silver Knight Helm": 123450,
    "Silver Knight Armor": 123450,
    "Sliver Gauntlets": 123450,
    "Silver Knight Leggings": 123450,
    # Black Sorcerer Set
    "Black Sorcerer Hat": 123450,
    "Black Sorcerer Cloak": 123450,
    "Black Sorcerer Gauntlets": 123450,
    "Black Sorcerer Boots": 123450,
    # Gwyndolin Moonlight Set
    "Crown of the Dark Sun": 123450,
    "Moonlight Robe": 123450,
    "Moonlight Gloves": 123450,
    "Moonlight Waistcloth": 123450,
    # Smough's Set
    "Smough's Helm": 123450,
    "Smough's Armor": 123450,
    "Smough's Gauntlets": 123450,
    "Smough's Leggings": 123450,
    # Brass Set
    "Brass Helm": 123450,
    "Brass Armor": 123450,
    "Brass Gauntlets": 123450,
    "Brass Leggings": 123450,
    # Havel's Set
    "Havel's Helm": 123450,
    "Havel's Armor": 123450,
    "Havel's Gauntlets": 123450,
    "Havel's Leggings": 123450,
    # Sorcerer Set
    "Sorcerer Hat": 123450,
    "Sorcerer Cloak": 123450,
    "Sorcerer Gauntlets": 123450,
    "Sorcerer Boots": 123450,
    # Catarina Set
    "Catarina Helm": 123450,
    "Catarina Armor": 123450,
    "Catarina Gauntlets": 123450,
    "Catarina Leggings": 123450,
    # Hollow Soldier Set
    "Hollow Soldier Helm": 123450,
    "Hollow Soldier Armor": 123450,
    "Hollow Soldier Waistcloth": 123450,
    # Steel Set
    "Steel Helm": 123450,
    "Steel Armor": 123450,
    "Steel Gauntlets": 123450,
    "Steel Leggings": 123450,
    # Chain Set
    "Chain Helm": 123450,
    "Chain Armor": 123450,
    "Leather Gauntlets": 123450,
    "Chain Leggings": 123450,
    # Hollow Thief Set
    "Hollow Thief's Hood": 123450,
    "Hollow Thief's Leather Armor": 123450,
    "Hollow Thief's Tights": 123450,
    # Stone Knight Set
    "Stone Helm": 123450,
    "Stone Armor": 123450,
    "Stone Gauntlets": 123450,
    "Stone Leggings": 123450,
    # Channeler Set
    "Six-Eyed Helm of the Channelers": 123450,
    "Robe of the Channelers": 123450,
    "Gauntlets of the Channelers": 123450,
    "Waistcloth of the Channelers": 123450,
    # Hollow Warrior Set
    "Hollow Warrior Helm": 123450,
    "Hollow Warrior Armor": 123450,
    "Hollow Warrior Waistcloth": 123450,
    # Thief Set
    "Thief Mask": 123450,
    "Black Leather Armor": 123450,
    "Black Leather Gloves": 123450,
    "Black Leather Boots": 123450,
    # Holy Set
    "Priest's Hat": 123450,
    "Holy Robe": 123450,
    "Holy Trousers": 123450,
    # Wanderer Set
    "Wanderer Hood": 123450,
    "Wanderer Coat": 123450,
    "Wanderer Manchette": 123450,
    "Wanderer Boots": 123450,
    # Cleric Set
    "Cleric Helm": 123450,
    "Cleric Armor": 123450,
    "Cleric Gauntlets": 123450,
    "Cleric Leggings": 123450,
    # Hunter Set
    "Pharis's Hat": 123450,
    "Leather Armor": 123450,
    "Leather Gloves": 123450,
    "Leather Boots": 123450,
    # Warrior Set
    "Standard Helm": 123450,
    "Hard Leather Armor": 123450,
    "Hard Leather Gauntlets": 123450,
    "Hard Leather Boots": 123450,
    # Crimson Set
    "Mask of the Sealer": 123450,
    "Crimson Robe": 123450,
    "Crimson Gloves": 123450,
    "Crimson Waistcloth": 123450,
    # Iron Golem Set
    "Golem Helm": 123450,
    "Golem Armor": 123450,
    "Golem Gauntlets": 123450,
    "Golem Leggings": 123450,
    # Witch Set
    "Witch Hat": 123450,
    "Witch Cloak": 123450,
    "Witch Gloves": 123450,
    "Witch Skirt": 123450,
    # Crystalline Set
    "Crystalline Helm": 123450,
    "Crystalline Armor": 123450,
    "Crystalline Gauntlets": 123450,
    "Crystalline Leggings": 123450,
    # Iron Set
    "Iron Helm": 123450,
    "Armor of the Sun": 123450,
    "Iron Bracelet": 123450,
    "Iron Leggings": 123450,
    # Xanthous Set
    "Xanthous Crown": 123450,
    "Xanthous Overcoat": 123450,
    "Xanthous Gloves": 123450,
    "Xanthous Waistcloth": 123450,
    # Dark Set
    "Dark Mash": 123450,
    "Dark Armor": 123450,
    "Dark Gauntlets": 123450,
    "Dark Leggings": 123450,
    # Knight Set
    "Knight Helm": 123450,
    "Knight Armor": 123450,
    "Knight Gauntlets": 123450,
    "Knight Leggings": 123450,
}

dlc_armor_table = {
    # Lord's Blades Set
    "Porcelain Mask": 123450,
    "Lord's Blade Robe": 123450,
    "Lord's Blade Gloves": 123450,
    "Lord's Blade Waistcloth": 123450,
    # Artorias' Set
    "Helm of Artorias": 123450,
    "Armor of Artorias": 123450,
    "Gauntlets of Artorias": 123450,
    "Leggings of Artorias": 123450,
    # Chester's Set
    "Snickering Top Hat": 123450,
    "Chester's Long Coat": 123450,
    "Chester's Gloves": 123450,
    "Chester's Trousers": 123450,
}

rings_table = {
    "Tiny Being's Ring": 123450,
    "Cloranthy Ring": 123450,
    "Havel's Ring": 123450,
    "Ring of Steel Protection": 123450,
    "Spell Stoneplate Ring": 123450,
    "Flame Stoneplate Ring": 123450,
    "Thunder Stoneplate Ring": 123450,
    "Speckled Stoneplate Ring": 123450,
    "Bloodbite Ring": 123450,
    "Poisonbite Ring": 123450,
    "Cursebite Ring": 123450,
    "Red Tearstone Ring": 123450,
    "Blue Tearstone Ring": 123450,
    "Ring of Sacrifice": 123450,
    "Rare Ring of Sacrifice": 123450,
    "Bellowing Dragoncrest Ring": 123450,
    "Lingering Dragoncrest Ring": 123450,
    "Slumbering Dragoncrest Ring": 123450,
    "Dusk Crown Ring": 123450,
    "White Seance Ring": 123450,
    "Darkmoon Seance Ring": 123450,
    "Ring of the Sun's Firstborn": 123450,
    "Darkmoon Blade Covenant Ring": 123450,
    "Ring of the Sun Princess": 123450,
    "Leo Ring": 123450,
    "Wolf Ring": 123450,
    "Hawk Ring": 123450,
    "Hornet Ring": 123450,
    "East Wood Grain Ring": 123450,
    "Dark Wood Grain Ring": 123450,
    "Rusted Iron Ring": 123450,
    "Covetous Gold Serpent Ring": 123450,
    "Covetous Silver Serpent Ring": 123450,
    "Covenant of Artorias": 123450,
    "Orange Charred Ring": 123450,
    "Old Witch's Ring": 123450,
    "Cat Covenant Ring": 123450,
    "Ring of Fog": 123450,
    "Ring of Favor and Protection": 123450,
    "Ring of the Evil Eye": 123450,
}

dlc_rings_table = {
    "Calamity Ring": 123450,
}

spells_table = {
    "Soul Arrow": 123450,
    "Great Soul Arrow": 123450,
    "Heavy Soul Arrow": 123450,
    "Great Heavy Soul Arrow": 123450,
    "Homing Soulmass": 123450,
    "Homing Crystal Soulmass": 123450,
    "Soul Spear": 123450,
    "Crystal Soul Spear": 123450,
    "White Dragon Breath": 123450,
    "Magic Weapon": 123450,
    "Great Magic Weapon": 123450,
    "Crystal Magic Weapon": 123450,
    "Magic Shield": 123450,
    "Strong Magic Shield": 123450,
    "Aural Decoy": 123450,
    "Hush": 123450,
    "Fall Control": 123450,
    "Hidden Weapon": 123450,
    "Hidden Body": 123450,
    "Repair": 123450,
    "Cast Light": 123450,
    "Chameleon": 123450,
    "Remedy": 123450,
    "Resist Curse": 123450,
}

dlc_spells_table = {
    "Dark Orb": 123450,
    "Dark Bead": 123450,
    "Dark Fog": 123450,
    "Pursuers": 123450,
}

misc_items_table = {

}

dlc_misc_items_table = {

}

embers_table = {
    "Large Ember": 123450,
    "Very Large Ember": 123450,
    "Divine Ember": 123450,
    "Large Divine Ember": 123450,
    "Dark Ember": 123450,
    "Large Magic Ember": 123450,
    "Enchanted Ember": 123450,
    "Crystal Ember": 123450,
    "Large Flame Ember": 123450,
    "Chaos Flame Ember": 123450,
}

key_items_table = {
    "Lordvessel": 123450,
    "Soul of Four Kings": 123450,
    "Soul of Seath the Scaleless": 123450,
    "Soul of Gravelord Nito": 123450,
    "Soul of Bed of Chaos": 123450,
}

boss_souls_table = {
    "Soul of the Moonlight Butterfly": 123450,
    "Soul of Quelaag": 123450,
    "Core of an Iron Golem": 123450,
    "Soul of Gwyndolin": 123450,
    "Soul of Ornstein": 123450,
    "Soul of Smough": 123450,
    "Soul of Sif": 123450,
    "Soul of Priscilla": 123450,
    "Soul of Gwyn, Lord of Cinder": 123450,
}

dlc_boss_souls_table = {
    "Guardian Soul": 123450,
    "Soul of Artorias": 123450,
    "Soul of Manus": 123450,
}

keys_table = {
    "Master Key": 123450,
    "Dungeon Cell Key": 123450,
    "Undead Asylum F2 East Key": 123450,
    "Undead Asylum F2 West Key": 123450,
    "Big Pilgrim's Key": 123450,
    "Residence Key": 123450,
    "Mystery Key": 123450,
    "Basement Key": 123450,
    "Key to Depths": 123450,
    "Sewer Chamber Key": 123450,
    "Blighttown Key": 123450,
    "Watchtower Basement Key": 123450,
    "Key to New Londo Ruins": 123450,
    "Key to the Seal": 123450,
    "Cage Key": 123450,
    "Archive Tower Cell Key": 123450,
    "Archive Prison Extra Key": 123450,
    "Archive Tower Giant Door Key": 123450,
    "Archive Tower Giant Cell Key": 123450,
    "Annex Key": 123450,
    "Crest of Artorias": 123450,
    "Peculiar Doll": 123450,
}

dlc_keys_table = {
    "Broken Pendant": 123450,
    "Crest Key": 123450,
}