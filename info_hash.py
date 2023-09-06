import hashlib

def calculate_info_hash(torrent_info):

    # Extract the 'info' dictionary and bencode it
    info_dict = torrent_info.get('info', {})
    bencoded_info = bencode_dictionary(info_dict)

    # Calculate the SHA-1 hash
    sha1 = hashlib.sha1()
    sha1.update(bencoded_info.encode('utf-8'))

    # Return the hash as hexadecimal string
    return sha1.hexdigits()