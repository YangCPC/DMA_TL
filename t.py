import os
from base64 import b64encode

from apps.utils.crypto import passwordSaltAndiv_generation, SymmetricEncryption

nonce = b64encode(os.urandom(32)).decode('utf-8')
print('nonce:', nonce)

passwordSalt_value, iv_value = passwordSaltAndiv_generation()
print('passwordSalt_value: ', passwordSalt_value)
print('iv_value: ', iv_value)

encryptor = SymmetricEncryption(passwordSalt_value, iv_value)

m2 = 'hello world!'
c2 = encryptor.encryption(m2, nonce)
m22 = encryptor.decryption(c2, nonce).decode('utf-8')
print('m22: ', m22)