from uu import encode


def decode_bencoded_value(encoded_str):

    # Decode string
    if encoded_str[0].isdigit():
        return decode_bencoded_string(encoded_str)
    
    # Decode integer
    elif encoded_str[0] == 'i':
        return decode_bencoded_integer(encoded_str)
    
    # Decode list
    elif encoded_str[0] == 'l':
        return decode_bencoded_list(encoded_str)
    
    #Decode dictionary
    elif encoded_str[0] == 'd':
        return decode_bencoded_dictionary(encoded_str)
    
    # Now let's retry decoding a bencoded dictionary
    decoded_dict, remaining = decode_bencoded_dictionary(test_encoded_str)
    decoded_dict, remaining