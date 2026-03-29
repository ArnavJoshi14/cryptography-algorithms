import random

def generate_key(plaintext_length):
    key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(plaintext_length))
    return key

def encrypt(plaintext, key):
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return ciphertext

def decrypt(ciphertext, key):
    decrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))
    return decrypted_text

plaintext = "attack the base"
key = generate_key(len(plaintext))

print("Plain Text:", plaintext)

ciphertext = encrypt(plaintext, key)
print("Cipher Text:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)