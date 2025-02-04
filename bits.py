# Part 1 goes here!
class BitList:
    def __init__(self, s):
        if not all(c in '01' for c in s):
            raise ValueError("Format is invalid and does not consist of only 0 and 1")
        self.bits = s  

    @staticmethod
    def from_ints(*ints):
        if not all(i in (0, 1) for i in ints):
            raise ValueError("Format is invalid and does not consist of only 0 and 1")
        return BitList(''.join(map(str, ints)))

    def __eq__(self, other):
        if not isinstance(other, BitList):
            return NotImplemented
        return self.bits == other.bits

    def __str__(self):
        return self.bits

    def arithmetic_shift_left(self):
        raise NotImplementedError

    def arithmetic_shift_right(self):
        raise NotImplementedError

    def bitwise_and(self, other):
        raise NotImplementedError

    def __str__(self):
        return self.bits

    def __eq__(self, other):
        if not isinstance(other, BitList):
            return NotImplemented
        return self.bits == other.bits

    def decode(self, encoding="utf-8"):
        raise NotImplementedError

    def chunk(self, size):
        raise NotImplementedError


# custom exceptions
class DecodeError(Exception):
    """raised when there's an issue attempting to decode a series of bits as a particular encoding."""
    pass

class ChunkError(Exception):
    """raised when a series of bits cannot be split into evenly sized chunks."""
    pass