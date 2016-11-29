#!/usr/bin/python

class Foo():
    def __init__(self, bar):
        self.bar = bar

    def bar_context(self):
        return self._context(self.bar)

    def bar_only(self):
        return self.bar

    def _context(self, bar):
        return "From bar class - this is bar: {}".format(bar)
