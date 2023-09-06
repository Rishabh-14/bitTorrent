import socket

def perform_handshake(peer_ip, peer_port, info_hash, peer_id):
     # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the peer
        s.connect((peer_ip, peer_port))

        # Prepare the handshake message
        pstr = "BitTorrent protocol"
        pstrlen = len(pstr)
        reserved = 8* b'\x00'
        handshake = bytes([pstrlen]) + pstr.encode() + reserved + info_hash.encode() + peer_id.encode()

        # Send the handshake message
        s.sendall(handshake)
        
        # Receive the peer's handshake message
        peer_handshake = s.recv(len(handshake))
        
        # TODO: Validate the peer's handshake (check info_hash and pstr)
        
    return True  # TODO: Return True only if the handshake is valid