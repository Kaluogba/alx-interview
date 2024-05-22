#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    # Masks to check the leading bits
    mask1 = 1 << 7
    mask2 = 1 << 6
    for num in data:
        # Get the binary representation of the byte
        bin_rep = num & 0xFF  # Mask to get the last 8 bits
        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            mask = 1 << 7
            while mask & bin_rep:
                num_bytes += 1
                mask >>= 1
                # 1-byte character
            if num_bytes == 0:
                continue
            # UTF-8 characters can only be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (bin_rep & mask1 and not (bin_rep & mask2)):
                return False
            # Decrement the number of bytes remaining in the current UTF-8
        num_bytes -= 1
    return num_bytes == 0
