# -*- coding: utf-8 -*-

import rsa

def coding(message):
    (pubkey, privkey) = rsa.newkeys(1024)
    crypto = rsa.encrypt(message, pubkey)
    return privkey, crypto


def spell_out(privkey, crypto):
    message = rsa.decrypt(crypto, privkey)
    return message

