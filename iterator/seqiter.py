class SequenceIterator(object):
    """An Iterator for python sequence Type"""

    def __init__(self, sequence):
        self._counter = -1
        self._sequence = sequence

    def __next__(self):
        self._counter += 1 # next index starting from 0th index
        if len(self._sequence) > self._counter:
            return self._sequence[self._counter]
        else:
            raise StopIteration("No more Elements")

    def __iter__(self):
        return self # By convention, an iterator must return itself as an iterator.
