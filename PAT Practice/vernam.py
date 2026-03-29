import random

def generate_key(pt_len):
    key = ''.join(random.choice('ABCDEFGHIKLMNOPQRSTUVWXYZ') for _ in range(pt_len))
    return key

def encrypt(pt, key):
    cipher = ''.join(chr(ord(p) ^ ord(k)) for p, k  in zip(pt, key))
    return cipher

def decrypt(ct, key):
    plaintext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ct, key))
    return plaintext

msg = input("enter msg: ")

key = generate_key(len(msg))
ct = encrypt(msg, key)
pt = decrypt(ct, key)

print(msg)
print(ct)
print(pt)