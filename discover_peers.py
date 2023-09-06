import urlib.parse
import requests

def discover_peers(torrent_info, info_hash, peer_id, port=6881):

    # Extract the announce URL
    announce_url = torrent_info.get('announce', '')

    # Prepare the query parameters
    query_params = {
        'info_hash': info_hash,
        'peer_id': peer_id,
        'port': port,
        'uploaded': 0,
        'downloaded': 0,
        'left': 0,  # TODO: Calculate the bytes left to download
        'compact': 1
    }

    # Make the HTTP GET request
    full_url = f"{announce_url}?{urllib.parse.urlencode(query_params)}"
    response = requests.get(full_url)
    
    # TODO: Parse the tracker response to get the list of peers
    
    return []  # TODO: Return the list of peers