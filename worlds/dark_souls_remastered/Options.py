import typing
from Options import DeathLink, Option

# TODO Implement additional options for game

dark_souls_remastered_options: typing.Dict[str, type(Option)] = {
    "death_link": DeathLink,
}