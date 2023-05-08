# Encryptor
import binascii
import os
import secrets
import pbkdf2
import pyaes


class SymmetricEncryption(object):
    def __init__(self):
        self.passwordSalt = os.urandom(16)
        self.iv = secrets.randbits(256)


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

encryptor = SymmetricEncryption()
c2 = encryptor.encryption('hello', '110')
m2 = encryptor.decryption(c2, '110')
print('c2: ', binascii.hexlify(c2))
print('m2: ', m2)

