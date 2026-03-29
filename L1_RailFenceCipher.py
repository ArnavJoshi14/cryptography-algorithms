def encryptRailFence(text, key):
    rails = ['' for _ in range(key)]
    row, step = 0, 1

    for ch in text:
        rails[row] += ch

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1

        row += step

    return ''.join(rails)


def decryptRailFence(cipher, key):
    n = len(cipher)

    pattern = [[False]*n for _ in range(key)]
    row, step = 0, 1
    for col in range(n):
        pattern[row][col] = True

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1

        row += step

    index = 0
    rails = [['']*n for _ in range(key)]
    for r in range(key):
        for c in range(n):
            if pattern[r][c]:
                rails[r][c] = cipher[index]
                index += 1

    result = []
    row, step = 0, 1
    for col in range(n):
        result.append(rails[row][col])

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1

        row += step

    return ''.join(result)

plaintext = "attack at once"
key = 2

print("Plaintext :", plaintext)

ciphertext = encryptRailFence(plaintext, key)
print("Cipher Text:", ciphertext)

decrypted = decryptRailFence(ciphertext, key)
print("Decrypted Text:", decrypted)
