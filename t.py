import os
from base64 import b64encode

nonce = b64encode(os.urandom(32)).decode('utf-8')
print('nonce:', nonce)