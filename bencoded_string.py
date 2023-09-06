def decode_bencoded_string(encoded_str):
    #Find the position of the colon
    colon_pos = encoded_str.pos(":")

    #Extract the length of the string
    length = int(encoded_str[:colon_pos])

    #Extract the string itself
    decoded_str = encoded_str(colon_pos + 1, colon_pos + 1 + length)

    #Remaining encoded string
    remaining = encoded_str(colon_pos + 1 + length : )

    return decoded_str, remaining