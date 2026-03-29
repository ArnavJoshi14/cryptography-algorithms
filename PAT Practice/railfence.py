def encrypt(msg, key):
    rails = ['' for _ in range(key)]

    row, step = 0, 1

    for ch in msg:
        rails[row] += ch

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        
        row += step
    
    cipher = ''.join(rails)

    return cipher

def decrypt(cipher, key):
    n = len(cipher)

    pattern = [[False] * n for _ in range(key)]
    row, step = 0, 1

    for col in range(n):
        pattern[row][col] = True

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        
        row += step
    
    rails = [[''] * n for _ in range(key)]

    index = 0
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
    
    plaintext = ''.join(result)
    return plaintext

msg = input("Enter msg: ")
key = 2

ct =  encrypt(msg, key)
pt = decrypt(ct, key)        

print(msg)
print(ct)
print(pt)