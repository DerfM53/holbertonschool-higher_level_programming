#!/usr/bin/python3

class VerboseList(list):
    """Extends list class with verbose messages for certain operations."""

    def append(self, item):
        """Add an item to the end of the list and print a message."""
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, iterable):
        """Extend the list with an iterable and print a message."""
        count = len(iterable)
        print(f"Extended the list with [{count}] items.")
        super().extend(iterable)

    def remove(self, item):
        """
        Remove first occurrence of item from
        the list and print a message.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index, print a message."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
