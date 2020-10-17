try:
    from collections.abc import MutableSet
except:
    from collections import MutableSet


class OrderedSet(MutableSet):
    """
    original author: Raymond Hettinger
    """
    def __init__(self, iterable=None):
        self._end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self._items = {}                # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable


    def __len__(self):
        return len(self._items)


    def __contains__(self, key):
        return key in self._items


    def add(self, key):
        if key not in self._items:
            end = self._end
            curr = end[1]
            curr[2] = end[1] = self._items[key] = [key, curr, end]


    def discard(self, key):
        if key in self._items:
            key, prev, next = self._items.pop(key)
            prev[2] = next
            next[1] = prev


    def __iter__(self):
        end = self._end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]


    def __reversed__(self):
        end = self._end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]


    def pop(self, last=True):
        if not self:
            raise KeyError("set is empty")
        key = self._end[1][0] if last else self._end[2][0]
        self.discard(key)
        return key


    def __repr__(self):
        cls = type(self)
        items = "[" + ", ".join("{i!r}".format(i) for i in self) + "]"
        return "{cls.__name__}({items})".format(**locals())


    def __str__(self):
        cls = type(self)
        items = "[" + ", ".join("{i!s}".format(i) for i in self) + "]"
        return "{cls.__name__}({items})".format(**locals())


    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)
