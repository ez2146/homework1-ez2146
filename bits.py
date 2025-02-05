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



    def chunk(self, chunk_length):
        if len(self.bits) % chunk_length != 0:
            raise ChunkError("BitList length is not divisible by chunk size")
        chunks = []
        for i in range(0, len(self.bits), chunk_length):
            chunks.append([int(bit) for bit in self.bits[i:i + chunk_length]])
        return chunks
    
    def decode(self, encoding="utf-8"):
        if encoding not in {"us-ascii", "utf-8"}:
            raise ValueError("Encoding not supported")

        bits = self.bits
        if encoding == "us-ascii":
            if len(bits) % 7 != 0:
                raise DecodeError("Invalid ASCII encoding: Bit length is not a multiple of 7")

            chars = []
            for i in range(0, len(bits), 7):
                segment = bits[i:i+7]  # Get 7-bit chunk
                char_code = int(segment, 2)  
                chars.append(chr(char_code))  

            return ''.join(chars)

        elif encoding == "utf-8":
            i = 0
            chars = []

            while i < len(bits):
                # Read the first byte to determine how many bytes are needed
                first_byte = bits[i:i+8]

                if first_byte.startswith("0"):  # 1-byte character 
                    num_bytes = 1
                    code_bits = first_byte[1:] 
                elif first_byte.startswith("110"):  # 2-byte character 
                    num_bytes = 2
                    code_bits = first_byte[3:] 
                elif first_byte.startswith("1110"):  # 3-byte character 
                    num_bytes = 3
                    code_bits = first_byte[4:]  
                elif first_byte.startswith("11110"):  # 4-byte character 
                    num_bytes = 4
                    code_bits = first_byte[5:]  
                else:
                    raise DecodeError("Invalid leading byte in UTF-8 encoding")

                total_bits_needed = num_bytes * 8
                if i + total_bits_needed > len(bits):
                    raise DecodeError("Incomplete UTF-8 sequence")

                # continuation bytes
                for j in range(1, num_bytes):
                    cont_byte = bits[i + j * 8:i + (j + 1) * 8]
                    if not cont_byte.startswith("10"):
                        raise DecodeError("Invalid continuation byte in UTF-8 encoding")
                    code_bits += cont_byte[2:] 
                char_code = int(code_bits, 2)
                chars.append(chr(char_code))
                i += total_bits_needed

            return ''.join(chars)

# custom exceptions
class DecodeError(Exception):
    """raised when there's an issue attempting to decode a series of bits as a particular encoding."""
    pass

class ChunkError(Exception):
    """raised when a series of bits cannot be split into evenly sized chunks."""
    pass