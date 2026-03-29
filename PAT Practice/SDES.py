# ---------------- PERMUTATION TABLES ----------------
P10 = [3,5,2,7,4,10,1,9,8,6]
P8  = [6,3,7,4,8,5,10,9]
P4  = [2,4,3,1]

IP      = [2,6,3,1,4,8,5,7]
IP_INV  = [4,1,3,5,7,2,8,6]

EP = [4,1,2,3,2,3,4,1]

# ---------------- S-BOXES ----------------
S0 = [
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,2]
]

S1 = [
    [0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]
]

# basic functions
def permute(bits, table):
    return ''.join(bits[i-1] for i in table)

def xor(a, b):
    return ''.join('0' if i == j else '1' for i,j in zip(a,b))

def shift_left(bits, n):
    return bits[n:] + bits[:n]

# generate keys
def generate_keys(key):
    key = permute(key, P10)

    left, right = key[:5], key[5:]

    left = shift_left(left, 1)
    right = shift_left(right, 1)
    k1 = permute(left + right, P8)

    left = shift_left(left, 2)
    right = shift_left(right, 2)
    k2 = permute(left + right, P8)

    return k1, k2

# sbox lookup
def sbox_lookup(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(sbox[row][col], '02b')

# fk function
def fk(bits, key):
    left, right = bits[:4], bits[4:]

    temp = permute(right, EP)

    temp = xor(temp, key)

    left_half = temp[:4]
    right_half = temp[4:]

    s0_out = sbox_lookup(left_half, S0)
    s1_out = sbox_lookup(right_half, S1)

    temp = permute(s0_out + s1_out, P4)

    left = xor(left, temp)

    return left + right

def switch(bits):
    return bits[4:] + bits[:4]

def encrypt(bits, key):
    k1, k2 = generate_keys(key)

    pt = permute(bits, IP)

    temp = fk(pt, k1)
    temp = switch(temp)
    temp = fk(temp, k2)

    ct = permute(temp, IP_INV)

    return ct

def decrypt(bits, key):
    k1, k2 = generate_keys(key)

    ct = permute(bits, IP)

    temp = fk(ct, k2)
    temp = switch(temp)
    temp = fk(temp, k1)

    pt = permute(temp, IP_INV)

    return pt

key = input("enter 10 bit key: ")
bits = input("enter 8 bit pt: ")

ct = encrypt(bits, key)
pt = decrypt(ct, key)

print(bits)
print(ct)
print(pt)