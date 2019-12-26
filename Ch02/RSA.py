# public key (RSA) 알고리즘 실습
from Crypto.PublicKey import RSA

# private key 와 public key 쌍을 생성.
# priavte 는 소유자가 보관하고, public key 는 공개
key_pair = RSA.generate(2048)
priv_key = key_pair.exportKey()
pub_key = key_pair.publickey()

# key_pair 의 p,q,e,d 확인
key_obj = RSA.importKey(priv_key)
print("p = ", key_obj.p)
print("q = ", key_obj.q)
print("e = ", key_obj.e)
print("d = ", key_obj.d)

# 암호화할 원문
plain_text = "This is Plain Text. It will be encrypted using RSA"
print()
print("원문 :")
print(plain_text)

# 공개키로 원문을 암호화.
cipher_text = pub_key.encrypt(plain_text.encode(), 10)
print("\n")
print("암호문 :")
print(cipher_text[0].hex())

# private key 를 소유한 수신자는 자신의 private key 로 암호문을 해독
# pub_key 와 쌍을 이루는 priv_key 만이 이 암호문을 해독 가능.
key = RSA.importKey(priv_key)
plain_text2 = key.decrypt(cipher_text)
plain_text2 = plain_text2.decode()
print("\n")
print("해독문 :")
print(plain_text2)