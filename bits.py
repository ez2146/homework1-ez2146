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
        self.bits = self.bits[1:] + '0'  

    def arithmetic_shift_right(self):
        self.bits = self.bits[0] + self.bits[:-1]  

    def bitwise_and(self, other):
        if not isinstance(other, BitList):
            raise TypeError("Must be an instance of BitList")
        if len(self.bits) != len(other.bits):
            raise ValueError("Both BitLists must be the same length")
        result = ""
        for i in range(len(self.bits)):
            result += str(int(self.bits[i]) & int(other.bits[i]))
        return BitList(result)

    def __str__(self):
        return self.bits

    def __eq__(self, other):
        if not isinstance(other, BitList):
            return NotImplemented
        return self.bits == other.bits

    def decode(self, encoding="utf-8"):
        raise NotImplementedError

    def chunk(self, chunk_length):
        if len(self.bits) % chunk_length != 0:
            raise ChunkError("BitList length is not divisible by chunk size")
        chunks = []
        for i in range(0, len(self.bits), chunk_length):
            chunks.append([int(bit) for bit in self.bits[i:i + chunk_length]])
        return chunks


# custom exceptions
class DecodeError(Exception):
    """raised when there's an issue attempting to decode a series of bits as a particular encoding."""
    pass

class ChunkError(Exception):
    """raised when a series of bits cannot be split into evenly sized chunks."""
    pass