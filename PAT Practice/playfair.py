def create_playfair_square(key):
    key = key.replace('J', 'I').upper() + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = "".join(dict.fromkeys(key))
    grid = [[k for k in key[i:i+5]] for i in range(0, 25, 5)]
    return grid

def find_location(grid, char):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == char:
                return i, j

def encrypt(text, key):
    playfair_square = create_playfair_square(key)
    ct = ''

    text = "".join(filter(str.isalpha, text.upper().replace('J','I')))

    i = 0
    while i < len(text)-1:
        if text[i] == text[i+1]:
            text = text[:i+1] + 'X' + text[i+1:]
        i += 1
    
    if (len(text) % 2) == 1:
        text += 'X'
    
    for i in range(0, len(text), 2):
        digraph = text[i:i+2]
        r1, c1 = find_location(playfair_square, digraph[0])
        r2, c2 = find_location(playfair_square, digraph[1])

        if r1 == r2:
            sub1 = playfair_square[r1][(c1 + 1) % 5]
            sub2 = playfair_square[r2][(c2 + 1) % 5]
        elif c1 == c2:
            sub1 = playfair_square[(r1 + 1) % 5][c1]
            sub2 = playfair_square[(r2 + 1) % 5][c2]
        else:
            sub1 = playfair_square[r1][c2]
            sub2 = playfair_square[r2][c1]

        ct += sub1 + sub2

    return ct

def decrypt(ct, key):
    playfair_square = create_playfair_square(key)
    pt = ''

    for i in range(0, len(ct), 2):
        digraph = ct[i:i+2]

        r1, c1 = find_location(playfair_square, digraph[0]) 
        r2, c2 = find_location(playfair_square, digraph[1]) 

        if r1 == r2:
            sub1 = playfair_square[r1][(c1 - 1) % 5]
            sub2 = playfair_square[r2][(c2 - 1) % 5]
        elif c1 == c2:
            sub1 = playfair_square[(r1 - 1) % 5][c1]
            sub2 = playfair_square[(r2 - 1) % 5][c2]
        else:
            sub1 = playfair_square[r1][c2]
            sub2 = playfair_square[r2][c1]
        
        pt += sub1 + sub2
    
    i = 0
    while i < len(pt) - 2:
        if pt[i] == pt[i+2] and pt[i+1] == 'X':
            pt = pt[:i+1] + pt[i+2:]
        i += 1
    
    if pt.endswith('X'):
        pt = pt[:-1]
    
    return pt

msg = input("enter msg: ")
key = "SECRETKEY"

ct = encrypt(msg, key)
pt = decrypt(ct, key)

print(msg)
print(ct)
print(pt)