from abc import abstractmethod, ABC

from game_constants import Element, Complexity
from helper_funcs import weighted_choice


class Spell(ABC):
    def __init__(self, name, base_mp_cost, elements, description, complexity):
        self.name = name
        self.base_mp_cost = base_mp_cost
        self.elements = elements
        self.description = description
        self.complexity = complexity

    def __str__(self):
        return self.name

    def mp_cost(self, user=None, target=None, context=None):
        """Returns the actual mp cost of the spell.
        
        Override this if the mp cost is dynamic."""
        return self.base_mp_cost
    
    def drain_mp(self, user, target=None, context=None):
        user.stats.mp -= self.mp_cost(user, target, context)
        if user.stats.mp < 0:
            user.stats.mp = 0

    @abstractmethod
    def activate(self, user, target=None, context=None):
        """This is where the spell's effect is implemented.
        
        The default implementation only ensures that user and target hp gets
        set to 0 if less than 0."""
        if user.stats.hp < 0:
            user.stats.hp = 0
        if target and target.stats.hp < 0:
            target.stats.hp = 0


class Fireball(Spell):
    def __init__(self):
        super().__init__(name='Fireball', base_mp_cost=40, elements=[Element.Fire], description='Deals fire damage', complexity=Complexity.Common)
    
    def activate(self, user, target, context=None):
        self.drain_mp(user)
        target.stats.hp -= round(5 + 2 * user.stats.fire / target.stats.fire)
        super().activate(user, target)


class Waterblast(Spell):
    def __init__(self):
        super().__init__(name='Waterblast', base_mp_cost=40, elements=[Element.Water], description='Deals water damage', complexity=Complexity.Common)
    
    def activate(self, user, target, context=None):
        self.drain_mp(user)
        target.stats.hp -= round(5 + 2 * user.stats.water / target.stats.water)
        super().activate(user, target)

class Inferno(Spell):
    def __init__(self):
        super.__init__(name='Inferno', base_mp_cost=150, elements=[Element.Fire], description='A supreme display of fire mastery', complexity=Complexity.Rare)

    def activate(self, user, target, context=None):
        self.drain_mp(user)
        target.stats.hp -= round(10 + 10 * user.stats.fire / target.stats.fire)
        super().activate(user, target)

class Spellbook:
    def __init__(self, spells):
        self.spells = [*spells]
        self.weights = [spell.complexity for spell in self.spells]
    
    def draw_spells(self, n_spells=3):
        """Returns n spells from the spellbook.
        
        The probability of returning a specific spell is weighted by
        the spell's complexity, and the weight increases by the same
        complexity every time the spell is not drawn. Once a spell
        has been drawn, its weight is reset to its complexity."""

        for _ in range(n_spells):
            spell = weighted_choice(self.spells, self.weights)
            self.weights[self.spells.index(spell)] = 0
        for i, spell in enumerate(self.spells):
            self.weights[i] += spell.complexity
            