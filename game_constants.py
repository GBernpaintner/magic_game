from enum import Enum


class Element(Enum):
    Fire = 'fire'
    Water = 'water'
    Wind = 'wind'
    Earth = 'earth'


class Complexity(Enum):
    """The complexity of a spell is the same thing as its weight in spellbooks."""
    Common = 5
    Uncommon = 3
    Rare = 2