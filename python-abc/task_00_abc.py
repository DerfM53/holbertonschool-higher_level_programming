#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite représentant un animal."""

    @abstractmethod
    def sound(self):
        """Méthode abstraite pour produire le son de l'animal."""
        pass


class Dog(Animal):
    """Classe représentant un chien."""

    def sound(self):
        """Produit le son caractéristique d'un chien."""
        return ("Bark")


class Cat(Animal):
    """Classe représentant un chat"""

    def sound(self):
        """Produit le son caracteristique du chat"""
        return ("Meow")
