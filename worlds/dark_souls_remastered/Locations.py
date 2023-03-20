from BaseClasses import Location
from worlds.dark_souls_remastered.data.locations_data import location_tables


class DarkSoulsRemasteredLocation(Location):
    game: str = "Dark Souls Remastered"

    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 100000  # TODO Is this the number we want?
        table_offset = 100  # TODO Is this the number we want?

        output = {}
        for i, table in enumerate(location_tables):
            if len(table) > table_offset:
                raise Exception("A location table has {} entries, that is more than {} entries (table #{})".format(len(table), table_offset, i))
            output.update({name: id for id, name in enumerate(table, base_id + (table_offset * i))})

        return output
