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