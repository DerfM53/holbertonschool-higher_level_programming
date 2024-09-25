#!/usr/bin/python3
"""
This module defines the CountedIterator class.

The CountedIterator extends the functionality of a built-in iterator
by keeping track of the number of items that have been iterated over.
"""


class CountedIterator:
    """
    A class that wraps an iterator and counts the number of iterations.

    This class extends the built-in iterator obtained from the iter function
    and keeps track of the number of items that have been iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.

        Args:
            iterable: An iterable object to be wrapped.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: When there are no more items to iterate over.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        Get the current count of iterated items.

        Returns:
            int: The number of items that have been iterated over.
        """
        return self.count

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            CountedIterator: The iterator object.
        """
        return self
