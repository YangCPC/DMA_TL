import binascii
import os
import random
import secrets
from base64 import b64encode
from datetime import datetime

import pbkdf2
import pyaes
from Crypto.PublicKey import RSA

from apps.utils.crypto import H2_hash_function

r1 = random.random()
print('r1:', r1)

t2 = datetime.now()
print('t2', t2)
print('type of t2', type(t2))
print('new type of t2', type(str(t2)))

DMi = 111

t2_str = t2.strftime("%Y-%m-%d %H:%M:%S")
print("t2_str: ", t2_str)
print("type of t2_str", type(t2_str))

temp = str(r1) + str(t2) + str(DMi)

H2 = H2_hash_function(temp)
print('H2', H2)
print('type of H2', type(H2)) #str
m2 = str(r1) + ' ' + str() + ' ' + H2

print('-----------------AES--------------')

# Derive a 256-bit AES encryption key from the password
password = "s3cr3t*c0d3"
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key:', binascii.hexlify(key))

# Encryption
iv = secrets.randbits(256)
plaintext = "Text for encryption"
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print('Encrypted:', binascii.hexlify(ciphertext))
print('passwordSalt: ', passwordSalt)
print('type of Encrypted: ', type(binascii.hexlify(ciphertext))) # <class 'bytes'>


# Decryption
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)
print('Decrypted:', decrypted)


nounce = b64encode(os.urandom(32)).decode('utf-8')
print('nounce: ', nounce)
print('type of nounce: ',  type(nounce)) #str


