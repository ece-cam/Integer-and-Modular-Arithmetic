class radixConversion:
    """
    A class to represent arbitrarily large integers using Base 10,000 blocks.
    Limits all intermediate arithmetic to 32-bit bounds.
    """
    BASE = 10000

    def __init__(self, blocks=None, is_negative=False):
        # Store the number as an array of blocks (little-endian: lowest values at index 0)
        self.blocks = blocks if blocks is not None else [0]
        self.is_negative = is_negative

    @classmethod
    def from_string(cls, val_str: str, radix: int):
        """Converts an input string of a given radix to a Base 10,000 BigInt."""
        is_negative = False
        if val_str.startswith("-"):
            is_negative = True
            val_str = val_str[1:]
        
        blocks = [0]
        
        for char in val_str:
            # Manually map character to integer without using the built in function int(val, base)
            if '0' <= char <= '9':
                digit = ord(char) - ord('0')
            elif 'A' <= char.upper() <= 'F':
                digit = ord(char.upper()) - ord('A') + 10
            else:
                digit = 0
            
            # Multiply array by radix and add the new digit
            carry = digit
            for i in range(len(blocks)):
                temp = blocks[i] * radix + carry
                blocks[i] = temp % cls.BASE
                carry = temp // cls.BASE
            
            # If there's still carry left over, append it as a new block
            while carry > 0:
                blocks.append(carry % cls.BASE)
                carry //= cls.BASE
                
        # Remove any excess leading zero blocks
        while len(blocks) > 1 and blocks[-1] == 0:
            blocks.pop()
            
        # Handle the edge case of negative zero
        if len(blocks) == 1 and blocks[0] == 0:
            is_negative = False
            
        return cls(blocks, is_negative)

    def to_string(self, radix: int) -> str:
        """Converts the internal Base 10,000 array to a string of the target radix."""
        if len(self.blocks) == 1 and self.blocks[0] == 0:
            return "0"
        
        # Copy blocks so we don't destroy the original number during division
        temp_blocks = self.blocks[:]
        result_chars = []
        char_map = "0123456789ABCDEF"
        
        # Repeatedly divide the array by the radix until it hits zero
        while not (len(temp_blocks) == 1 and temp_blocks[0] == 0):
            remainder = 0
            
            # Divide from highest block down to lowest
            for i in range(len(temp_blocks) - 1, -1, -1):
                current = remainder * self.BASE + temp_blocks[i]
                temp_blocks[i] = current // radix
                remainder = current % radix
            
            # The final remainder is our next right-most character
            result_chars.append(char_map[remainder])
            
            # Trim trailing zero blocks to speed up the next division loop
            while len(temp_blocks) > 1 and temp_blocks[-1] == 0:
                temp_blocks.pop()
        
        # We collected characters from right to left, so reverse them
        result_chars.reverse()
        result_str = "".join(result_chars)
        
        if self.is_negative:
            result_str = "-" + result_str
            
        return result_str