import math

key = "HACK"

def encryptMessage(msg):
    cipher = ""
    k_indx = 0

    msg_len = len(msg)
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    col = len(key)
    row = int(math.ceil(msg_len / col))

    fill_null = (row * col) - msg_len
    msg_lst.extend('_' * fill_null)

    matrix = [msg_lst[i:i+col] for i in range(0, len(msg_lst), col)]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join(row[curr_idx] for row in matrix)
        k_indx += 1

    return cipher


def decryptMessage(cipher):
    msg = ""
    k_indx = 0
    msg_indx = 0

    msg_len = len(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))

    key_lst = sorted(list(key))
    msg_lst = list(cipher)

    matrix = [[None]*col for _ in range(row)]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            matrix[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    msg = ''.join(sum(matrix, []))

    if '_' in msg:
        msg = msg[:msg.index('_')]

    return msg


plaintext = "attack the base"
print("Plain Text:", plaintext)

ciphertext = encryptMessage(plaintext)
print("Cipher Text:", ciphertext)

decrypted = decryptMessage(ciphertext)
print("Decrypted Text:", decrypted)
