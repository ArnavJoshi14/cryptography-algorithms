p, q, x, g, H, k = map(int, input().split())

# key generation
y = pow(g, x, p)

# signature generation - (r, s)
r = pow(g, k, p) % q
k_inv = pow(k, -1, q)
s = (k_inv * (H + x*r)) % q

# signature verification
w = pow(s, -1, q)
u1 = (H * w) % q
u2 = (r * w) % q

v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

print("Valid" if v == r else "Invalid")

# def mod_exp(base, exp, mod):
#     result = 1
#     base = base % mod

#     print("\nPerforming Modular Exponentiation:")

#     while exp > 0:
#         if exp % 2 == 1:
#             result = (result * base) % mod
#             print(f"result = ({result//base} * {base}) mod {mod} = {result}")

#         base = (base * base) % mod
#         exp = exp // 2

#     return result


# def mod_inverse(a, m):
#     print(f"\nFinding Modular Inverse of {a} mod {m}")

#     for i in range(1, m):
#         if (a * i) % m == 1:
#             print(f"Inverse found: {i}")
#             return i

#     return -1


# p = int(input("Enter prime p: "))
# q = int(input("Enter prime q (divisor of p-1): "))
# g = int(input("Enter generator g: "))
# x = int(input("Enter private key x: "))
# message = int(input("Enter message hash H(m): "))
# k = int(input("Enter random number k: "))

# print("\n----- KEY GENERATION -----")

# y = mod_exp(g, x, p)

# print("\nPublic key y = g^x mod p")
# print(f"y = {g}^{x} mod {p} = {y}")

# print("\n----- SIGNATURE GENERATION -----")

# r = mod_exp(g, k, p) % q

# print("\nr = (g^k mod p) mod q")
# print(f"r = ({g}^{k} mod {p}) mod {q} = {r}")

# k_inv = mod_inverse(k, q)

# s = (k_inv * (message + x * r)) % q

# print("\ns = k^-1(H(m) + x*r) mod q")
# print(f"s = {k_inv}({message} + {x}*{r}) mod {q}")
# print(f"s = {s}")

# print(f"\nSignature (r,s) = ({r}, {s})")

# print("\n----- SIGNATURE VERIFICATION -----")

# w = mod_inverse(s, q)

# print(f"\nw = s^-1 mod q = {w}")

# u1 = (message * w) % q
# u2 = (r * w) % q

# print(f"\nu1 = H(m)*w mod q = {u1}")
# print(f"u2 = r*w mod q = {u2}")

# v = ((mod_exp(g, u1, p) * mod_exp(y, u2, p)) % p) % q

# print(f"\nv = ((g^u1 * y^u2) mod p) mod q = {v}")

# print("\n----- FINAL RESULT -----")

# if v == r:
#     print("Signature Verified (Valid)")
# else:
#     print("Signature Invalid")