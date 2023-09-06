def decode_bencoded_disctionary(encoded_str):
    if encoded_str[0] != 'd':
        return None, encoded_str
    encoded_str = encoded_str[1:]
    decoded_dict = {}
    while encoded_str[0] != 'e':
        key, encoded_str = decode_bencoded_str(encoded_str)
        value, encoded_str = decode_bencoded_value(encoded_str)
        decoded_dict[key] = value

    encoded_str = encoded_str[1:]
    return decoded_dict, encoded_str