from Crypto.Hash import MD5, RIPEMD, SHA, SHA256

# msg = "이 문서의 Hash Value를 계산한다."
msg = "이 문서의 Hash Value를 계산한다?"
print("\nMessgae : ", msg)

msg = msg.encode()

# MD5
h = MD5.new()
h.update(msg)
hv = h.hexdigest()
print("\nMD5 (%d bit) : %s" % (len(hv) * 4, hv))


# RIPEMD160
h = RIPEMD.new()
h.update(msg)
hv = h.hexdigest()
print("RIPEMD (%d bit) : %s" % (len(hv) * 4, hv))


# SHA
h = SHA.new()
h.update(msg)
hv = h.hexdigest()
print("SHA (%d bit) : %s" % (len(hv) * 4, hv))


# SHA-256
h = SHA256.new()
h.update(msg)
hv = h.hexdigest()
print("SHA256 (%d bit) : %s" % (len(hv) * 4, hv))


# Double-SHA256
h1 = SHA256.new()  # 1st SHA256
h1.update(msg)

h2 = SHA256.new()
h1.update((h1.hexdigest()).encode())  # 2nd SHA256
hv = h2.hexdigest()
print("Double-SHA256 (%d bit) : %s" % (len(hv) * 4, hv))