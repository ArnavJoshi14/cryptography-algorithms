def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

def modInverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

    g, x, _ = egcd(e, phi)
    if g != 1:
        return -1
    return x % phi

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generateKeys():
    p = 101
    q = 113
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Find e
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
            
    d = modInverse(e, phi)
    return e, d, n

def encrypt(m, e, n):
    return power(m, e, n)

def decrypt(c, d, n):
    return power(c, d, n)

def encrypt_text(plaintext, e, n):
    cipher_blocks = []
    for ch in plaintext:
        m = ord(ch)
        c = encrypt(m, e, n)
        cipher_blocks.append(c)
    return cipher_blocks

def decrypt_text(cipher_blocks, d, n):
    plaintext = ""
    for c in cipher_blocks:
        m = decrypt(c, d, n)
        plaintext += chr(m)
    return plaintext

if __name__ == "__main__":
    e, d, n = generateKeys()
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")
    
    M = 123
    print(f"\nOriginal Integer Message: {M}")
    
    C = encrypt(M, e, n)
    print(f"Encrypted Integer Message: {C}")
    
    decrypted = decrypt(C, d, n)
    print(f"Decrypted Integer Message: {decrypted}")
    
    text = "hello how are you"
    print(f"\nOriginal Text Message: {text}")
    
    encrypted_text = encrypt_text(text, e, n)
    print(f"Encrypted Text (blocks): {encrypted_text}")
    
    decrypted_text = decrypt_text(encrypted_text, d, n)
    print(f"Decrypted Text: {decrypted_text}")