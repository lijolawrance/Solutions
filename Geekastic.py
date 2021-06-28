from collections import defaultdict


def rec_indices(col, indices):
    for element in enumerate(col):
        print(indices[element[0]])
        indices[element[0]] = element


names = ['p', 's', 'b', 'k']
indices = defaultdict(lambda: 0)

rec_indices(names, indices)

a = ''.join([1, 2, 3, 4, 5, 6, 7])

print(a)


class Mc:
    _MY_C_ = {'n': 'g'}

    def __init__(self, **kwargs):
        self._MY_C_.update(kwargs)

    def p(self):
        print(self._MY_C_)


my_cool = Mc(elo=1200)
my_s_cool = Mc(name='Myname')
