from abc import abstractmethod, ABC
from game_constants import Element


class Spell(ABC):
    def __init__(self, name, base_mp_cost, elements):
        self.name = name
        self.base_mp_cost = base_mp_cost
        self.elements = elements

    def __str__(self):
        return self.name

    def mp_cost(self):
        """Override this if the mp cost is dynamic."""
        return self.base_mp_cost
    
    def drain_mp(self, user):
        user.stats.mp -= self.mp_cost()
        if user.stats.mp < 0:
            user.stats.mp = 0

    @abstractmethod
    def activate(self, user, target=None, context=None):
        """This is where the spell's effect is implemented."""


class Fireball(Spell):
    def __init__(self):
        super().__init__(name='Fireball', base_mp_cost=40, elements=[Element.Fire])
    
    def activate(self, user, target=None, context=None):
        self.drain_mp(user)
        target.stats.hp -= round(5 + 2 * user.stats.fire / target.stats.fire)
        if target.stats.hp < 0:
            target.stats.hp = 0
