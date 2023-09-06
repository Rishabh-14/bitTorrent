# Stage 1: Decode bencoded strings
def decode_bencoded_string(encoded_str):
    colon_pos = encoded_str.index(":")
    length = int(encoded_str[:colon_pos])
    decoded_str = encoded_str[colon_pos + 1 : colon_pos + 1 + length]
    remaining = encoded_str[colon_pos + 1 + length :]
    return decoded_str, remaining

# Stage 2: Decode bencoded integers
def decode_bencoded_integer(encoded_str):
    if encoded_str[0] != 'i':
        return None, encoded_str
    e_pos = encoded_str.index('e')
    integer_value = int(encoded_str[1:e_pos])
    remaining = encoded_str[e_pos + 1:]
    return integer_value, remaining

# General function to decode either a string or integer
def decode_bencoded_value(encoded_str):
    if encoded_str[0].isdigit():
        return decode_bencoded_string(encoded_str)
    elif encoded_str[0] == 'i':
        return decode_bencoded_integer(encoded_str)
    else:
        return None, encoded_str

# Stage 3: Decode bencoded lists
def decode_bencoded_list(encoded_str):
    if encoded_str[0] != 'l':
        return None, encoded_str
    encoded_str = encoded_str[1:]
    decoded_list = []
    while encoded_str[0] != 'e':
        decoded_value, encoded_str = decode_bencoded_value(encoded_str)
        decoded_list.append(decoded_value)
    encoded_str = encoded_str[1:]
    return decoded_list, encoded_str
