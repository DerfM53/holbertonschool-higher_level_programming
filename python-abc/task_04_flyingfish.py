#!/usr/bin/env python3
"""
This module defines the class Fish and Bird
"""


class Fish:
    """A class Fish"""
    pass

    def swim(self):
        """Print a sentence"""
        print("The fish is swimming")

    def habitat(self):
        """Print a sentence"""
        print("The fish lives in water")


class Bird:
    """A class Bird"""
    pass

    def fly(self):
        """Print a sentence"""
        print("The bird is flying")

    def habitat(self):
        """Print a sentence"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """This class inheritence class of Fish and Bird"""
    pass

    def fly(self):
        """Print a sentence"""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a sentence"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print a sentence"""
        print("The flying fish lives both in water and the sky!")
