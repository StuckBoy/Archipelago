import sys

from BaseClasses import Item
from worlds.dark_souls_remastered.data.items_data import item_tables


class DarkSoulsRemasteredItem(Item):
    game: str = "Dark Souls Remastered"

    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 100000  # TODO Is this the base we want?
        table_offset = 100  # TODO What should this be set to?

        output = {}
        for i, table in enumerate(item_tables):
            if len(table) > table_offset:
                raise Exception("An item table has {} entries, that is more than {} entries (table #{})".
                                format(len(table), table_offset, i))
            output.update({name: id for id, name in enumerate(table, base_id + (table_offset * i))})
        return output
