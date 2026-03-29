def CaesarCipherEncrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result


def CaesarCipherDecrypt(cipher, key):
    result = ""
    for char in cipher:
        if char.isupper():
            result += chr((ord(char) - 65 - key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            result += char
    return result


text = "Attack postponed until two am"
k = 4

encrypted = CaesarCipherEncrypt(text, k)
decrypted = CaesarCipherDecrypt(encrypted, k)

print("Text:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)