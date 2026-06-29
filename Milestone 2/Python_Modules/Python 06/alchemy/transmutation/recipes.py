import elements                        # absolute import (root elements.py)
from ..potions import strength_potion  # relative import (go up to alchemy/,)
from ..elements import create_air      # relative import (go up to alchemy/,)


def lead_to_gold():
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}'"
        f" mixed with '{elements.create_fire()}'"
    )
