import numpy as np
import math

keyMatrix = [[0]*3 for _ in range(3)]
messageVector = [[0] for _ in range(3)]
cipherMatrix = [[0] for _ in range(3)]

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) - 65
            k += 1

def encrypt():
    for i in range(3):
        cipherMatrix[i][0] = 0
        for x in range(3):
            cipherMatrix[i][0] += keyMatrix[i][x] * messageVector[x][0]
        cipherMatrix[i][0] %= 26

def modInverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def isInvertible():
    det = int(round(np.linalg.det(np.array(keyMatrix))))
    det %= 26
    return math.gcd(det, 26) == 1

def inverseKeyMatrix():
    K = np.array(keyMatrix)
    det = int(round(np.linalg.det(K)))
    det_mod = det % 26
    det_inv = modInverse(det_mod, 26)

    K_inv = np.linalg.inv(K)
    K_adj = np.round(det * K_inv).astype(int)
    K_inv_mod26 = (det_inv * K_adj) % 26

    return K_inv_mod26

def decrypt(invKey):
    plainMatrix = [[0] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            plainMatrix[i][0] += invKey[i][j] * cipherMatrix[j][0]
        plainMatrix[i][0] %= 26

    plaintext = ""
    for i in range(3):
        plaintext += chr(plainMatrix[i][0] + 65)

    return plaintext

def HillCipher(message, key):
    getKeyMatrix(key)
    print("Plain Text:", message)

    if not isInvertible():
        print("Key matrix is NOT invertible modulo 26")
        return

    for i in range(3):
        messageVector[i][0] = ord(message[i]) - 65

    encrypt()

    cipher = ""
    for i in range(3):
        cipher += chr(cipherMatrix[i][0] + 65)
    print("Cipher Text:", cipher)

    invKey = inverseKeyMatrix()
    plaintext = decrypt(invKey)
    print("Decrypted Text:", plaintext)

def main():
    message = "DOG"
    key = "GYBNQKURP"
    HillCipher(message, key)

if __name__ == "__main__":
    main()
