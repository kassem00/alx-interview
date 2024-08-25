def validUTF8(data: list[int]) -> bool:
    """ valid UTF-8 encoding checker """
    n_bytes = 0  # Number of bytes in the current UTF-8 character
    
    for i in data:
        # Ensure the byte is valid (0-255)
        if i > 255:
            return False
        
        bin_rep = format(i, '08b')  # Convert to 8-bit binary representation
        
        if n_bytes == 0:
            # Determine how many bytes the current character uses
            if bin_rep[0] == '0':
                continue  # 1-byte character (ASCII), nothing more to do
            elif bin_rep[:3] == '110':
                n_bytes = 1  # 2-byte character
            elif bin_rep[:4] == '1110':
                n_bytes = 2  # 3-byte character
            elif bin_rep[:5] == '11110':
                n_bytes = 3  # 4-byte character
            else:
                return False  # Invalid UTF-8 start byte pattern
        else:
            # Continuation bytes should start with '10'
            if bin_rep[:2] != '10':
                return False
        
        n_bytes -= 1  # Decrement the number of expected continuation bytes

    return n_bytes == 0  # Return True only if all characters completed valid sequences
