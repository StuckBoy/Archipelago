"""
Classes and functions related to creating a ROM patch
"""
class PokemonHGSSProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Pokemon HeartGold and SoulSilver"
    hash = "" #TODO
    patch_file_ending = ".aphgss"
    result_file_ending = ".nds"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
    	# TODO Don't forget the settings
        with open(get_settings().pokemon_hgss_settings.rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read())

        return base_rom_bytes

