from collections.abc import Sequence
from itertools import islice
from functools import reduce


class List(Sequence):
    def __init__(self, seq):
        self._d = list(seq)

    def __getitem__(self, pos):
        return self._d[pos]

    def __len__(self):
        return len(self._d)

    def __repr__(self):
        return f'List({self._d})'

    def append(self, value):
        return List(self._d + [value])

    def map(self, function: callable) -> 'List':
        return List(map(function, self._d))

    def filter(self, function: callable) -> 'List':
        return List(filter(function, self._d))

    def reduce(self, function: callable) -> 'List':
        return reduce(function, self._d)

    def take(self, n) -> 'List':
        return List(islice(self._d, n))

    def join(self, l: list) -> 'List':
        return List(self._d + l)
