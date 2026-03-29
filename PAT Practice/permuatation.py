import math

key = "HACK"

def encrypt(msg):
    cipher = ""
    k_ind = 0

    msg_len = len(msg)
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    numCols = len(key)
    numRows = int(math.ceil(msg_len / numCols))

    fillNUll = (numCols * numRows) - msg_len
    msg_lst.extend('_' * fillNUll)

    matrix = [msg_lst[i:i+numCols] for i in range(0, len(msg_lst), numCols)]

    for _ in range(numCols):
        curr_ind = key.index(key_lst[k_ind])
        k_ind += 1
        cipher += ''.join(row[curr_ind] for row in matrix)
    
    return cipher

def decrypt(cipher):
    msg = ""
    k_ind = 0
    msg_ind = 0

    msg_len = len(cipher)
    msg_lst = list(cipher)
    key_lst = sorted(list(key))

    numCols = len(key)
    numRows = int(math.ceil(msg_len / numCols))

    matrix = [[None] * numCols for _ in range(numRows)]

    for _ in range(numCols):
        curr_ind = key.index(key_lst[k_ind])
        for j in range(numRows):
            matrix[j][curr_ind] = msg_lst[msg_ind]
            msg_ind += 1
        k_ind += 1

    msg = ''.join(sum(matrix, []))

    if '_' in msg:
        msg = msg[:msg.index('_')]

    return msg

msg = input("Enter msg: ")

ct = encrypt(msg)
pt = decrypt(ct)

print(msg)
print(ct)
print(pt)