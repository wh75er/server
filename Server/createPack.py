# -*- coding: utf-8 -*-

import pickle
import struct

def create(req_type, er_name, er_pass, ee_name, data):
    packet = pickle.dumps(dict(REQUEST_TYPE = req_type,
                  ADRESSER_NAME = er_name,
                  ADRESSER_PASSWORD = er_pass,
                  ADRESSEE_NAME = ee_name,
                  DATA = data), 2)
    
    return struct.pack('>I', len(packet)) + packet