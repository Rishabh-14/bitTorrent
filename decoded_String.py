def decode_bencoded_string(encoded_str):
    
    # Check for initial character i
    if encoded_str[0] != 'i':
        return None, encoded_str
    
    #Find the position of e character
    e_pos = encoded_str.index('e')

    #Extract the integer value
    integer_value = int(encoded_str(1: e_pos))

    #Remaining string
    remaining = encoded_str(e_pos + 1)

    return integer_value, remaining