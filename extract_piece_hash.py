def extract_piece_hashes(torrent_info):
    
    # Extract the 'pieces' field (a bytes-like object)
    pieces = torrent_info.get('pieces', b'')
    
    # Split the pieces into 20-byte chunks
    piece_hashes = [pieces[i:i+20] for i in range(0, len(pieces), 20)]
    
    return piece_hashes
