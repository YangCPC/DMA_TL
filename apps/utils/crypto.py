import hashlib
import os
import secrets
from base64 import b64encode

import pbkdf2
import pyaes


# CSPRNG: Cryptography Secure Pseudo-Random Number Generator
# CSPRNG guarantee that the random number coming from it is absolutely unpredictable.
def nonce_generation():
    return b64encode(os.urandom(32)).decode('utf-8')

# SHA-512 is based on "MerKle-Damgard construction".
# It is considered highly secure and collision resistance for most applications.
def H2_hash_function(temp):
    res = hashlib.sha512(temp.encode('utf-8')).hexdigest()

    return res

# Encryptor
class SymmetricEncryption(object):
    def __init__(self):
        # self.passwordSalt = os.urandom(16)
        # self.iv = secrets.randbits(256)
        self.passwordSalt = b'"k\x1asV\xac67\xd8\n\'\x8c\xa48B\xf1'
        self.iv = 61661271473775212356602068528112630478399302202911140582284521798026533363744


    def encryption(self, msg, password):
        key = pbkdf2.PBKDF2(password, self.passwordSalt).read(32)
        aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(self.iv))
        ciphertext = aes.encrypt(msg)
        return ciphertext

    def decryption(self, ciphertext, password):
        key = pbkdf2.PBKDF2(password, self.passwordSalt).read(32)
        aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(self.iv))
        message = aes.decrypt(ciphertext)
        return message


