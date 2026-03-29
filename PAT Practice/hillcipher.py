import numpy as np
import math

key_matrix = [[0]*3 for _ in range(3)]
message_vector = [[0] for _ in range(3)]
cipher_matrix = [[0] for _ in range(3)]

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            key_matrix[i][j] += ord(key[k]) - 65
            k += 1

def getMessageVector(msg):
    j = 0
    for i in range(3):
            message_vector[i][0] += ord(msg[j]) - 65
            j += 1

def modInverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def isInvertible():
    det = int(round(np.linalg.det(np.array(key_matrix))))
    det %= 26
    return np.gcd(det, 26) == 1

def getInvKey():
    K = np.array(key_matrix)

    det = np.linalg.det(K)
    det_mod26 = det % 26
    det_inv = modInverse(det_mod26, 26)

    K_inv = np.linalg.inv(K)
    K_adj = np.round(det * K_inv).astype(int)
    K_inv_mod26 = (det_inv * K_adj) % 26

    return K_inv_mod26

def encrypt(msg, key):
    getKeyMatrix(key)
    getMessageVector(msg)

    for i in range(3):
        for j in range(3):
            cipher_matrix[i][0] += key_matrix[i][j] * message_vector[j][0]
        cipher_matrix[i][0] %= 26
    
    ct = ''
    for i in range(3):
        ct += chr(cipher_matrix[i][0] + 65)
    
    return ct

def decrypt():
    if not isInvertible():
        print("key not invertible. cannot decrypt")
        return None
    
    plaintext_matrix = [[0] for _ in range(3)]
    
    invKey = getInvKey()

    for i in range(3):
        for j in range(3):
            plaintext_matrix[i][0] += invKey[i][j] * cipher_matrix[j][0]
        plaintext_matrix[i][0] %= 26
    
    pt = ''

    for i in range(3):
        pt += chr(plaintext_matrix[i][0] + 65)

    return pt

msg = input("Enter msg: ")
key = "GYBNQKURP"

ct = encrypt(msg, key)
pt = decrypt()

print(msg)
print(ct)
print(pt)