#!/usr/bin/env python3
"""
This module defines the class SwimMixin
and FlyMixim
"""


class SwimMixin:
    """A class SwimMixin"""
    pass

    def swim(self):
        """Print a sentence"""
        print("The creature swims!")


class FlyMixin:
    """A class FlyMixin"""
    pass

    def fly(self):
        """Print a sentence"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """a class dragon inheretence a FlyMixin class
    and SwimMixin class
    """
    pass

    def roar(self):
        """Print a sentence"""
        print("The dragon roars!")
