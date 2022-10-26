from random import choices


def weighted_choice(population, weights):
    try:
        return choices(population, weights, k=1)[0]
    except IndexError:
        raise IndexError('empty population')
    except (ValueError, TypeError) as e:
        raise type(e)(e)
