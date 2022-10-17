from spells import Spell, Fireball, Waterblast


class Stats:
    def __init__(self, hp=0, mp=0, fire=0, water=0, air=0, earth=0):
        self.hp = hp
        self.mp = mp
        self.fire = fire
        self.water = water
        self.air = air
        self.earth = earth

    def copy(self):
        return Stats(hp=self.hp, mp=self.mp, fire=self.fire, water=self.water, air=self.air, earth=self.earth)


class Wizard:
    def __init__(self, name, base_stats: Stats):
        self.name = name
        self.base_stats = base_stats
        self.stats: Stats
        self.reset_stats()
    
    def __str__(self) -> str:
        return self.name
    
    def reset_stats(self):
        self.stats = self.base_stats.copy()

    def can_cast(self, spell: Spell, target=None, context=None):
        return self.stats.mp > spell.mp_cost(self, target, context)


def print_simple_battle_status(wizard1: Wizard, wizard2: Wizard):
    print(f'{wizard1} has {wizard1.stats.hp} hp and {wizard1.stats.mp} mp. {wizard2} has {wizard2.stats.hp} hp and {wizard2.stats.mp} mp.')


def simple_battle_activation(user: Wizard, target: Wizard, spell: Spell, print_reversed=False):
    spell.activate(user, target)
    print(f'{user} activates {spell}.')
    if print_reversed:
        print_simple_battle_status(target, user)
    else:
        print_simple_battle_status(user, target)
    print()


def print_simple_battle_introduction(wizard1: Wizard, wizard2: Wizard, spell: Spell):
    print(f'\n\n{"-"*100}\n\nStarting simple battle between {wizard1} and {wizard2} activating the {spell} spell.')
    print_simple_battle_status(wizard1, wizard2)
    print(f'\n{"-"*100}\n\n')


def simple_battle(wizard1: Wizard, wizard2: Wizard, spell: Spell):
    """Makes two wizards cast the same spell at each other until one dies.
    
    Useful for testing new wizards and spells."""
    print_simple_battle_introduction(wizard1, wizard2, spell)
    while True:
        simple_battle_activation(wizard1, wizard2, spell)
        if wizard2.stats.hp == 0:
            break
        simple_battle_activation(wizard2, wizard1, spell, print_reversed=True)
        if wizard1.stats.hp ==0:
            break


def main():
    stats_fb = Stats(hp=100, mp=500, fire=20, water=10)
    stats_wg = Stats(hp=100, mp=500, fire=10, water=15)
    fireboy = Wizard('Fire Boy', stats_fb)
    watergirl = Wizard('Water Girl', stats_wg)
    fireball = Fireball()
    waterblast = Waterblast()
    simple_battle(fireboy, watergirl, waterblast)


if __name__ == '__main__':
    main()
    