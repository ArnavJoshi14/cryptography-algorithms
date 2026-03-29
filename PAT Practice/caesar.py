def encrypt(text, key):
    result = ''
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result

def decrypt(cipher, key):
    result = ''
    for char in cipher:
        if char.isupper():
            result += chr((ord(char) - 65 - key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            result += char
    return result

msg = input("enter message")
key = 4

ct = encrypt(msg, key)
pt = decrypt(ct, key)
print("message:", msg)
print("encrtypted:", ct)
print("decrypted:", pt)