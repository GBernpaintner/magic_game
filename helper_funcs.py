from random import choices, choice


def weighted_choice(population, weights):
    try:
        if sum(weights) == 0:
            return choice(population)
        return choices(population, weights, k=1)[0]
    except IndexError:
        raise IndexError('empty population')
    except (ValueError, TypeError) as e:
        raise type(e)(e)
