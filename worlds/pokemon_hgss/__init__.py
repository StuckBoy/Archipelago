class HGSSWeb(WebWorld):
	"""
	WebHost information
	"""
	theme = "ocean" # TODO update this
	game = "Pokémon HeartGold and SoulSilver"
	setup_en = Tutorial(
		"Multiworld Setup Guide",
		"A guide to playing Pokémon HeartGold/SoulSilver with Archipelago",
		"English",
		"setup_en.md",
		"setup/en",
		["StuckSouls"]
	)

	tutorials = [setup_en]
	#TODO Option Groups

class HGSSWorld(World):
	"""
	TODO Blurb on HGSS
	"""