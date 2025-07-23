import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
	from worlds._bizhawk.context import BizHawkClientContext

game_version = "v0.0.1"

class HGSSClient(BizHawkClient):
	game = "Pokemon HeartGold and SoulSilver"
	system = "NDS"
	patch_suffix = ".aphgss"

	"""
	TODO MASSIVE PLACEHOLDERS
	 Everything beyond here is: 1) Untested, 2) Guesswork
	 Fake it 'till you make it! :D
	"""
    local_checked_locations: Set[int]
    goal_flag: int
    rom_slot_name: Optional[str]
    eUsed: List[int]
    room: int
    local_events: List[int]
    player_name: Optional[str]
    checked_dungeon_flags: Dict[int, list] = {}
    checked_general_flags: Dict[int, list] = {}
    ram_mem_domain = "Main RAM"
    goal_complete = False
    bag_given = False
    macguffins_collected = 0
    macguffin_unlock_amount = 0
    instruments_collected = 0
    required_instruments = 0
    spinda_events = 0
    spinda_drinks = 0
    skypeaks_open = 0
    aegis_seals = 0
    dialga_complete = False
    random: Random = Random()
    outside_deathlink = 0
    deathlink_sender = ""
    deathlink_message: str = ""
    item_box_count = 0
    hint_loc = []
    hints_hinted: List[int] = []
    client_version = game_version
    hint_issue = False

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.local_set_events = {}
        self.local_found_key_items = {}
        self.rom_slot_name = None
        self.seed_verify = False
        self.eUsed = []
        self.room = 0
        self.local_events = []