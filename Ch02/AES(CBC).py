# AES Algorithms labs
# CBC 모드로 암화화.

from Crypto.Cipher import AES
from Crypto import Random
import numpy as np

# Create Symmetry key, Symmetry key - 128bit, 192bit, 256bit 사용.
secret_key128 = b'0123456701234567'
secret_key192 = b'012345670123456701234567'
secret_key256 = b'01234567012345670123456701234567'

# Use 128bit
secret_key = secret_key128
plain_text = "This is Plain Text. It will be encrypted using AES with CBC mode"
print("\n\n")
print("원문 :")
print(plain_text)


# CBC 모드에서는 plain text 가 128-bit(16byte)의 배수가 돼야 하므로 padding이 필요함.
# padding 으로 NULL 문자를 삽입. 수신자는 별도로 padding 을 제거할 필요는 없음.
n = len(plain_text)
if (n % 16) != 0:
    n = n + 16 - (n % 16)
    plain_text = plain_text.ljust(n, '\0')

# initialization vector. iv 도 수신자에게 보내야 함.
iv = Random.new().read(AES.block_size)
ivcopy = np.copy(iv) # 수신자에게 보낼 복사본.

# 송신자는 secret_key 와 iv로 plain_text 를 암호문으로 변환.
iv = Random.new().read(AES.block_size)
ivcopy = np.copy(iv)
aes = AES.new(secret_key, AES.MODE_CBC, iv)
cipher_text = aes.encrypt(plain_text)
print("\n\n\n")
print("암호문 :")
print(cipher_text.hex())

# 암호문, secret_key, ivcopy 를 수신자에게 보내면 수신자는 암호문을 해독할 수 있음.
aes = AES.new(secret_key, AES.MODE_CBC, ivcopy)
plain_text2 = aes.decrypt(cipher_text)
plain_text2 = plain_text2.decode()
print("\n\n\n")
print("해독문 :")
print(plain_text2)