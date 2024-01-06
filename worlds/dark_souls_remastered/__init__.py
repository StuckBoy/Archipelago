# worl/dark_souls_remastered/__init__.py
from typing import Dict

from .Items import DarkSoulsRemasteredItem
from .Locations import DarkSoulsRemasteredLocation
from .Options import dark_souls_remastered_options
from .data.items_data import weapons_upgrade_5_table, weapons_upgrade_15_table, item_dictionary, key_items_list
from .data.locations_data import location_dictionary, northern_undead_asylum_table, firelink_shrine_table, \
    undead_burg_table, lower_undead_burg_table, undead_parish_table, depths_table, blighttown_table, \
    quelaags_domain_table, the_great_hollow_table, ash_lake_table, sens_fortress_table, anor_londo_table, \
    painted_world_of_ariamis_table, darkroot_garden_table, darkroot_basin_table, new_londo_ruins_table, \
    lower_new_londo_ruins_table, the_abyss_table, the_dukes_archives_table, crystal_cave_table, demon_ruins_table, \
    lost_izalith_table, the_catacombs_table, tomb_of_giants_table, kiln_of_the_first_flame_table, \
    the_valley_of_the_drakes_table, sanctuary_garden_table, royal_wood_table, oolacile_township_table, \
    chasm_of_the_abyss_table, northern_undead_asylum_revisit_table
from ..AutoWorld import World, WebWorld
from BaseClasses import MultiWorld, Region, Item, Entrance, Tutorial, ItemClassification
from ..generic.Rules import set_rule, add_item_rule


class DarkSoulsRemasteredWeb(WebWorld):
    # TODO Set up issue tracking for game
    setup_en = Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago Dark Souls Remastered randomizer on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["StuckBoy"]
    )

    tutorials = [setup_en]


class DarkSoulsRemasteredWorld(World):
    """
    Dark Souls Remastered is an Action role-playing game and is part of the Souls series developed by FromSoftware.
    Played from a third-person perspective, players have access to various weapons, armour, magic, and consumables that
    they can use to fight their enemies.
    """

    game: str = "Dark Souls Remastered"
    option_definitions = dark_souls_remastered_options
    topology_present: bool = True
    web = DarkSoulsRemasteredWeb()
    data_version = 1  # TODO Is this right?
    base_id = 110000
    required_client_version = (0, 3, 8)  # TODO Match current version on master
    item_name_to_id = DarkSoulsRemasteredItem.get_name_to_id()
    location_name_to_id = DarkSoulsRemasteredLocation.get_name_to_id()

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.locked_items = []
        self.locked_locations = []
        self.main_path_locations = []

    def generate_early(self):
        pass

    def create_items(self):
        for name, address in self.item_name_to_id.items():
            self.multiworld.itempool += [self.create_item(name)]

    def create_item(self, name: str) -> Item:
        data = self.item_name_to_id[name]

        if name in key_items_list:
            item_classification = ItemClassification.progression
        elif name in weapons_upgrade_15_table or name in weapons_upgrade_5_table:
            item_classification = ItemClassification.useful
        else:
            item_classification = ItemClassification.filler

        return DarkSoulsRemasteredItem(name, item_classification, data, self.player)

    def create_regions(self):
        # TODO Implement progressive items (souls, resins, firebombs, etc.)
        menu_region = self.create_region("Menu", None)

        # Vanilla Regions
        northern_undead_asylum_region = self.create_region("Northern Undead Asylum", northern_undead_asylum_table)
        northern_undead_asylum_revisit_region = self.create_region("Northern Undead Asylum Revisit",
                                                                   northern_undead_asylum_revisit_table)
        firelink_shrine_region = self.create_region("Firelink Shrine", firelink_shrine_table)
        undead_burg_region = self.create_region("Undead Burg", undead_burg_table)
        lower_undead_burg_region = self.create_region("Lower Undead Burg", lower_undead_burg_table)
        undead_parish_region = self.create_region("Undead Parish", undead_parish_table)
        depths_region = self.create_region("Depths", depths_table)
        blighttown_region = self.create_region("Blighttown", blighttown_table)
        quelaags_domain_region = self.create_region("Quelaag's Domain", quelaags_domain_table)
        the_great_hollow_region = self.create_region("The Great Hollow", the_great_hollow_table)
        ash_lake_region = self.create_region("Ash Lake", ash_lake_table)
        sens_fortress_region = self.create_region("Sen's Fortress", sens_fortress_table)
        anor_londo_region = self.create_region("Anor Londo", anor_londo_table)
        painted_world_of_ariamis_region = self.create_region("Painted World of Ariamis", painted_world_of_ariamis_table)
        darkroot_garden_region = self.create_region("Darkroot Garden", darkroot_garden_table)
        darkroot_basin_region = self.create_region("Darkroot Basin", darkroot_basin_table)
        new_londo_ruins_region = self.create_region("New Londo Ruins", new_londo_ruins_table)
        lower_new_londo_ruins_region = self.create_region("Lower New Londo Ruins", lower_new_londo_ruins_table)
        the_abyss_region = self.create_region("The Abyss", the_abyss_table)
        the_dukes_archives_region = self.create_region("The Duke's Archives", the_dukes_archives_table)
        crystal_cave_region = self.create_region("Crystal Cave", crystal_cave_table)
        demon_ruins_region = self.create_region("Demon Ruins", demon_ruins_table)
        lost_izalith_region = self.create_region("Lost Izalith", lost_izalith_table)
        the_catacombs_region = self.create_region("The Catacombs", the_catacombs_table)
        tomb_of_giants_region = self.create_region("Tomb of Giants", tomb_of_giants_table)
        kiln_of_the_first_flame_region = self.create_region("Kiln of the First Flame", kiln_of_the_first_flame_table)
        the_valley_of_the_drakes_region = self.create_region("Valley of Drakes", the_valley_of_the_drakes_table)
        # DLC Regions
        sanctuary_garden_region = self.create_region("Sanctuary Garden", sanctuary_garden_table)
        royal_wood_region = self.create_region("Royal Wood", royal_wood_table)
        oolacile_township_region = self.create_region("Oolacile Township", oolacile_township_table)
        chasm_of_the_abyss_region = self.create_region("Chasm of the Abyss", chasm_of_the_abyss_table)

        # Entrances
        # TODO Should the entrances be strictly the default progression path?
        menu_region.exits.append(Entrance(self.player, "New Game", menu_region))
        self.multiworld.get_entrance("New Game", self.player).connect(northern_undead_asylum_region)
        # Northern Undead Asylum
        northern_undead_asylum_region.exits.append(Entrance(self.player, "Goto Firelink Shrine",
                                                            northern_undead_asylum_region))
        # Firelink Shrine
        self.multiworld.get_entrance("Goto Firelink Shrine", self.player).connect(firelink_shrine_region)
        firelink_shrine_region.exits.append(Entrance(self.player, "Goto Undead Burg", firelink_shrine_region))
        firelink_shrine_region.exits.append(Entrance(self.player, "Goto New Londo Ruins", firelink_shrine_region))
        firelink_shrine_region.exits.append(Entrance(self.player, "Goto The Catacombs", firelink_shrine_region))
        firelink_shrine_region.exits.append(Entrance(self.player, "Goto Northern Undead Asylum Revisit",
                                                     firelink_shrine_region))
        firelink_shrine_region.exits.append(Entrance(self.player, "Goto Kiln of the First Flame",
                                                     firelink_shrine_region))

        # Northern Undead Asylum Revisit
        self.multiworld.get_entrance("Goto Northern Undead Asylum Revisit", self.player) \
            .connect(northern_undead_asylum_revisit_region)

        # Kiln of the First Flame
        self.multiworld.get_entrance("Goto Kiln of the First Flame", self.player). \
            connect(kiln_of_the_first_flame_region)

        # The Catacombs
        self.multiworld.get_entrance("Goto The Catacombs", self.player).connect(the_catacombs_region)
        the_catacombs_region.exits.append(Entrance(self.player, "Goto Tomb of Giants", the_catacombs_region))

        # Tomb of Giants
        self.multiworld.get_entrance("Goto Tomb of Giants", self.player).connect(tomb_of_giants_region)

        # New Londo Ruins
        self.multiworld.get_entrance("Goto New Londo Ruins", self.player).connect(new_londo_ruins_region)
        new_londo_ruins_region.exits.append(Entrance(self.player, "Goto Lower New Londo Ruins",
                                                     new_londo_ruins_region))
        # TODO Move ownership to VoD
        new_londo_ruins_region.exits.append(Entrance(self.player, "Upper shortcut to Valley of Drakes",
                                                     new_londo_ruins_region))

        # Lower New Londo Ruins
        self.multiworld.get_entrance("Goto Lower New Londo Ruins", self.player).connect(lower_new_londo_ruins_region)
        lower_new_londo_ruins_region.exits.append(Entrance(self.player, "Goto The Abyss", the_abyss_region))

        # Not possible until you have the Key to the Seal
        lower_new_londo_ruins_region.exits.append(Entrance(self.player, "Lower shortcut to Valley of Drakes",
                                                           lower_new_londo_ruins_region))

        # The Abyss
        self.multiworld.get_entrance("Goto The Abyss", self.player).connect(the_abyss_region)

        # Undead Burg
        self.multiworld.get_entrance("Goto Undead Burg", self.player).connect(undead_burg_region)
        undead_burg_region.exits.append(Entrance(self.player, "Goto Undead Parish", undead_burg_region))
        undead_burg_region.exits.append(Entrance(self.player, "Goto Lower Undead Burg", undead_burg_region))

        undead_burg_region.exits.append(Entrance(self.player, "Shortcut to Darkroot Basin", undead_burg_region))

        # Undead Parish
        self.multiworld.get_entrance("Goto Undead Parish", self.player).connect(undead_parish_region)
        undead_parish_region.exits.append(Entrance(self.player, "Elevator to Firelink Shrine", undead_parish_region))
        self.multiworld.get_entrance("Elevator to Firelink Shrine", self.player).connect(firelink_shrine_region)
        undead_parish_region.exits.append(Entrance(self.player, "Goto Darkroot Garden", undead_parish_region))
        undead_parish_region.exits.append(Entrance(self.player, "Goto Sen's Fortress", undead_parish_region))

        # Darkroot Garden
        self.multiworld.get_entrance("Goto Darkroot Garden", self.player).connect(darkroot_garden_region)
        darkroot_garden_region.exits.append(Entrance(self.player, "Goto Darkroot Basin", darkroot_garden_region))

        # Darkroot Basin
        self.multiworld.get_entrance("Goto Darkroot Basin", self.player).connect(darkroot_basin_region)
        self.multiworld.get_entrance("Shortcut to Darkroot Basin", self.player).connect(darkroot_basin_region)
        # TODO Should DLC be a toggle?
        darkroot_basin_region.exits.append(Entrance(self.player, "Goto Sanctuary Garden", darkroot_basin_region))
        darkroot_basin_region.exits.append(Entrance(self.player, "Goto Valley of Drakes", darkroot_basin_region))

        # Valley of Drakes
        self.multiworld.get_entrance("Goto Valley of Drakes", self.player).connect(the_valley_of_the_drakes_region)
        self.multiworld.get_entrance("Upper shortcut to Valley of Drakes", self.player) \
            .connect(the_valley_of_the_drakes_region)
        self.multiworld.get_entrance("Lower shortcut to Valley of Drakes", self.player) \
            .connect(the_valley_of_the_drakes_region)
        the_valley_of_the_drakes_region.exits.append(Entrance(self.player, "Valley entrance to Blighttown",
                                                              the_valley_of_the_drakes_region))

        # Lower Undead Burg
        self.multiworld.get_entrance("Goto Lower Undead Burg", self.player).connect(lower_undead_burg_region)
        lower_undead_burg_region.exits.append(Entrance(self.player, "Goto Depths", lower_undead_burg_region))

        # Depths
        self.multiworld.get_entrance("Goto Depths", self.player).connect(depths_region)
        depths_region.exits.append(Entrance(self.player, "Goto Blighttown", depths_region))

        # Blighttown
        self.multiworld.get_entrance("Goto Blighttown", self.player).connect(blighttown_region)
        self.multiworld.get_entrance("Valley entrance to Blighttown", self.player).connect(blighttown_region)
        blighttown_region.exits.append(Entrance(self.player, "Goto Quelaag's Domain", blighttown_region))
        blighttown_region.exits.append(Entrance(self.player, "Goto The Great Hollow", blighttown_region))

        # Quelaag's Domain
        self.multiworld.get_entrance("Goto Quelaag's Domain", self.player).connect(quelaags_domain_region)
        quelaags_domain_region.exits.append(Entrance(self.player, "Goto Demon Ruins", quelaags_domain_region))

        # Demon Ruins
        self.multiworld.get_entrance("Goto Demon Ruins", self.player).connect(demon_ruins_region)
        demon_ruins_region.exits.append(Entrance(self.player, "Goto Lost Izalith", demon_ruins_region))

        # Lost Izalith
        self.multiworld.get_entrance("Goto Lost Izalith", self.player).connect(lost_izalith_region)

        # Sen's Fortress
        self.multiworld.get_entrance("Goto Sen's Fortress", self.player).connect(sens_fortress_region)
        sens_fortress_region.exits.append(Entrance(self.player, "Goto Anor Londo", sens_fortress_region))

        # Anor Londo
        self.multiworld.get_entrance("Goto Anor Londo", self.player).connect(anor_londo_region)
        anor_londo_region.exits.append(Entrance(self.player, "Goto Painted World of Ariamis", anor_londo_region))
        anor_londo_region.exits.append(Entrance(self.player, "Goto Duke's Archives", anor_londo_region))

        # Painted World
        self.multiworld.get_entrance("Goto Painted World of Ariamis", self.player) \
            .connect(painted_world_of_ariamis_region)

        # Duke's Archives
        self.multiworld.get_entrance("Goto Duke's Archives", self.player).connect(the_dukes_archives_region)
        the_dukes_archives_region.exits.append(Entrance(self.player, "Goto Crystal Cave", the_dukes_archives_region))

        # Crystal Cave
        self.multiworld.get_entrance("Goto Crystal Cave", self.player).connect(crystal_cave_region)

        # The Great Hollow
        self.multiworld.get_entrance("Goto The Great Hollow", self.player).connect(the_great_hollow_region)
        the_great_hollow_region.exits.append(Entrance(self.player, "Goto Ash Lake", the_great_hollow_region))

        # Ash Lake
        self.multiworld.get_entrance("Goto Ash Lake", self.player).connect(ash_lake_region)

        # Sanctuary Garden
        self.multiworld.get_entrance("Goto Sanctuary Garden", self.player).connect(sanctuary_garden_region)
        sanctuary_garden_region.exits.append(Entrance(self.player, "Goto Royal Wood", sanctuary_garden_region))

        # Royal Wood
        self.multiworld.get_entrance("Goto Royal Wood", self.player).connect(royal_wood_region)
        royal_wood_region.exits.append(Entrance(self.player, "Goto Oolacile Township", royal_wood_region))

        # Oolacile Township
        self.multiworld.get_entrance("Goto Oolacile Township", self.player).connect(oolacile_township_region)
        oolacile_township_region.exits.append(Entrance(self.player, "Goto Chasm of the Abyss",
                                                       oolacile_township_region))

        # Chasm of the Abyss
        self.multiworld.get_entrance("Goto Chasm of the Abyss", self.player).connect(chasm_of_the_abyss_region)

    def create_region(self, region_name, location_table) -> Region:
        new_region = Region(region_name, self.player, self.multiworld)
        if location_table:
            for name, address in location_table.items():
                location = DarkSoulsRemasteredLocation(self.player, name, self.location_name_to_id[name], new_region)
                if region_name == "Menu":
                    add_item_rule(location, lambda item: not item.advancement)
                new_region.locations.append(location)
        self.multiworld.regions.append(new_region)
        return new_region

    def fill_slot_data(self) -> Dict[str, object]:
        item_dictionary_copy = item_dictionary.copy()

        items_id = []
        items_address = []
        locations_id = []
        locations_address = []
        locations_target = []
        for location in self.multiworld.get_filled_locations():
            if location.item.player == self.player:
                items_id.append(location.item.code)
                items_address.append(item_dictionary_copy[location.item.name])

            if location.player == self.player:
                locations_address.append(location_dictionary[location.name])
                locations_id.append(location.address)
                if location.item.player == self.player:
                    locations_target.append(item_dictionary_copy[location.item.name])
                else:
                    locations_target.append(0)

        slot_data: Dict[str, object] = {
            "options": {
                "death_link": self.multiworld.death_link[self.player].value
            },
            "seed": self.multiworld.seed_name,  # To verify the server's multiworld
            "slot": self.multiworld.player_name[self.player],  # To connect to the server
            "base_id": self.base_id,  # To merge locations and items
            "locationsId": locations_id,
            "locationsAddress": locations_address,  # TODO are these the in-game locations?
            "locationsTarget": locations_target,  # TODO  are these the hex IDs to be given at the locations?
            "itemsId": items_id,
            "itemsAddress": items_address
        }

        return slot_data

    def set_rules(self) -> None:
        # TODO How to prevent access to Sen's Fortress before both bells are rung?
        # Quelaag has a unique soul, but the Bell Gargoyles do not.
        set_rule(self.multiworld.get_entrance("Goto Firelink Shrine", self.player),
                 lambda state: state.has("Big Pilgrim's Key", self.player) and
                               state.has("Undead Asylum F2 East Key", self.player))
        set_rule(self.multiworld.get_entrance("Goto Kiln of the First Flame", self.player),
                 lambda state: state.has("Soul of the Four Kings", self.player) and
                               state.has("Soul of Gravelord Nito", self.player) and
                               state.has("Soul of Bed of Chaos", self.player) and
                               state.has("Soul of Seath the Scaleless", self.player) and
                               state.has("Lordvessel", self.player))
        set_rule(self.multiworld.get_entrance("Goto Lower Undead Burg", self.player),
                 lambda state: state.has("Basement Key", self.player))
        set_rule(self.multiworld.get_entrance("Shortcut to Darkroot Basin", self.player),
                 lambda state: state.has("Watchtower Basement Key", self.player) or
                               state.has("Master Key", self.player))
        set_rule(self.multiworld.get_entrance("Upper shortcut to Valley of Drakes", self.player),
                 lambda state: state.has("Key to New Londo Ruins", self.player) or
                               state.has("Master Key", self.player))
        set_rule(self.multiworld.get_entrance("Goto Depths", self.player),
                 lambda state: state.has("Key to Depths", self.player))
        set_rule(self.multiworld.get_entrance("Goto Blighttown", self.player),
                 lambda state: state.has("Blighttown Key", self.player))
        set_rule(self.multiworld.get_entrance("Goto Painted World of Ariamis", self.player),
                 lambda state: state.has("Peculiar Doll", self.player))
        set_rule(self.multiworld.get_entrance("Goto Duke's Archives", self.player),
                 lambda state: state.has("Lordvessel", self.player))
        set_rule(self.multiworld.get_entrance("Goto Lost Izalith", self.player),
                 lambda state: state.has("Lordvessel", self.player))
        set_rule(self.multiworld.get_entrance("Goto Lower New Londo Ruins", self.player),
                 lambda state: state.has("Key to the Seal", self.player))
        set_rule(self.multiworld.get_entrance("Goto The Abyss", self.player),
                 lambda state: state.has("Covenant of Artorias", self.player))
        set_rule(self.multiworld.get_entrance("Goto Sanctuary Garden", self.player),
                 lambda state: state.has("Broken Pendant", self.player) and state.has("Lordvessel", self.player))

        # TODO How to set rule about placement of Cell Key to prevent softlock?
        # set_rule(self.multiworld.get_location("NUA: Estus Flask", self.player),
        #          lambda state: state.has("Dungeon Cell Key", self.player))
        # TODO Does this and the following rule prevent softlocks in Duke's Archives?
        set_rule(self.multiworld.get_location("DA: Archive Tower Cell Key", self.player),
                 lambda state: state.has("Archive Tower Cell Key", self.player))
        set_rule(self.multiworld.get_location("DA: Archive Tower Giant Door Key", self.player),
                 lambda state: state.has("Archive Tower Giant Door Key", self.player))
        # TODO Does this prevent hell runs in Lost Izalith?
        set_rule(self.multiworld.get_location("DR: Orange Charred Ring", self.player),
                 lambda state: state.has("Orange Charred Ring", self.player))
        set_rule(self.multiworld.get_location("TG: Soul of Gravelord Nito", self.player),
                 lambda state: state.has("Lordvessel", self.player))

        self.multiworld.completion_condition[self.player] = lambda state: \
            state.has("Soul of the Four Kings", self.player) and \
            state.has("Soul of Gravelord Nito", self.player) and \
            state.has("Soul of Seath the Scaleless", self.player) and \
            state.has("Soul of Bed of Chaos", self.player) and \
            state.has("Lordvessel", self.player)
