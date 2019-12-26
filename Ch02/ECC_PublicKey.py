import math

# Additive Operation

# Additive Operation
def add_operation(a, b, p, q, m):
    if q == (math.inf, math.inf):
        return p

    x1 = p[0]
    y1 = p[1]
    x2 = q[0]
    y2 = q[1]

    if p == q:
        # Doubling
        # slope (s) = (3 * x1 ^ 2 + a) / (2 * y1) mod m
        # 분모의 역원부터 계산.
        r = 2 * y1
        rInv = pow(r, m - 2, m)
        s = (rInv * (3 * (x1 ** 2) + a)) % m
    else:
        r = x2 - x1
        rInv = pow(r, m - 2, m) # Fermat's Little Theorem
        s = (rInv * (3 * (x1 ** 2) + a)) % m

    x3 = (s ** 2 - x1 - x2) % m
    y3 = (s * (x1 - x3) - y1) % m
    return x3, y3

# Domain parameter 정의
# y^2 = x^3 + 2 * x + 2 mod 231559
a = 2
b = 2
p = 32416189381 # prime number
G = (5, 1)

# 개인키 선택. p보다 작은 임의의 숫자를 선택
# 실제는 순환군 범위 내에서 선택. 이 부분은 지갑편에서 다룬다.
d = 1234567

# double-and-add 알고리즘으로 공개키를 생성.
bits = bin(d)
bits = bits[2:len(bits)]

# initialize. bits[0] = 1 (always)
K = G

# 두 번째 비트부터 Double-and-Add
bits = bits[1:len(bits)]
for bit in bits:
    # Double
    K = add_operation(a, b, K, K, p)

    # Multiply
    if bit == '1':
        k = add_operation(a, b, K, G, p)

priv_key = d
pub_key = K

print("\n Domain Parameters : (P, a, b, G)")
print("P = %d" % p)
print("a = %d" % a)
print("b = %d" % b)
print("G = (%d, %d)" % (G[0], G[1]))
print("EC : y^2 = x^3 + %d * x + %d mod %d" % (a, b, p))
print("\n Keys : ")
print("Private Key = ", priv_key)
print("Public Key = %d * (%d, %d) = (%d, %d)" % (d, G[0], G[1], pub_key[0], pub_key[1]))