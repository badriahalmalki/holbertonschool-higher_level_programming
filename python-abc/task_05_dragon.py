#!/usr/bin/env python3

class SwimMixin:
    """Mixin providing swimming ability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying ability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly thanks to mixins."""

    def roar(self):
        print("The dragon roars!")
