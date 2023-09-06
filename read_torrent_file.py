def read_torrent_file_from_disk(file_path):
    with open(file_path, 'rb') as f:
        file_content = f.read()
    torrent_info, _ = decode_bencoded_dictionary(file_content.decode('utf-8'))
    return torrent_info