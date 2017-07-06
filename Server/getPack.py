# -*- coding: utf-8 -*-

import struct
import pickle
import socket

def recvProcess(connection, n):
    buffer = b''
    
    while len(buffer) < n:
        try:
            packet = connection.recv(n - len(buffer))
        except OSError:
            continue
        if not packet:
            return None
        buffer += packet
    
    return buffer


def packetRecv(connection):
    length_data = recvProcess(connection, 4)
    
    if not length_data:
        return None
    
    data_len = struct.unpack('>I', length_data)[0]
    
    return pickle.loads(recvProcess(connection, data_len))