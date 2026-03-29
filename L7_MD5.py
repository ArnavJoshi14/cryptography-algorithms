import math

rotation_amounts = [
    7,12,17,22, 7,12,17,22, 7,12,17,22, 7,12,17,22,
    5,9,14,20, 5,9,14,20, 5,9,14,20, 5,9,14,20,
    4,11,16,23, 4,11,16,23, 4,11,16,23, 4,11,16,23,
    6,10,15,21, 6,10,15,21, 6,10,15,21, 6,10,15,21
]

md5_constants = [
    int(abs(math.sin(i + 1)) * (2**32)) & 0xFFFFFFFF
    for i in range(64)
]

initial_state = [
    0x67452301,
    0xefcdab89,
    0x98badcfe,
    0x10325476
]

def rotate_left_32bit(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def apply_padding(message_bytes):
    original_bit_length = (8 * len(message_bytes)) & 0xffffffffffffffff
    
    message_bytes.append(0x80)
    
    while len(message_bytes) % 64 != 56:
        message_bytes.append(0)
    
    message_bytes += original_bit_length.to_bytes(8, byteorder='little')
    return message_bytes

def process_blocks(padded_message):
    A, B, C, D = initial_state
    hash_buffers = [A, B, C, D]

    for block_start in range(0, len(padded_message), 64):
        a, b, c, d = hash_buffers
        block = padded_message[block_start:block_start + 64]

        for round_index in range(64):
            
            if round_index < 16:
                function_result = (b & c) | (~b & d)
                word_index = round_index

            elif round_index < 32:
                function_result = (d & b) | (~d & c)
                word_index = (5 * round_index + 1) % 16

            elif round_index < 48:
                function_result = b ^ c ^ d
                word_index = (3 * round_index + 5) % 16

            else:
                function_result = c ^ (b | ~d)
                word_index = (7 * round_index) % 16

            word = int.from_bytes(
                block[4 * word_index: 4 * word_index + 4],
                byteorder='little'
            )

            temp_value = (a + function_result + md5_constants[round_index] + word) & 0xFFFFFFFF
            updated_b = (b + rotate_left_32bit(temp_value, rotation_amounts[round_index])) & 0xFFFFFFFF

            a, b, c, d = d, updated_b, b, c

        hash_buffers[0] = (hash_buffers[0] + a) & 0xFFFFFFFF
        hash_buffers[1] = (hash_buffers[1] + b) & 0xFFFFFFFF
        hash_buffers[2] = (hash_buffers[2] + c) & 0xFFFFFFFF
        hash_buffers[3] = (hash_buffers[3] + d) & 0xFFFFFFFF

    final_digest = sum(hash_buffers[i] << (32 * i) for i in range(4))
    return final_digest

def convert_to_hex_string(digest_value):
    raw_bytes = digest_value.to_bytes(16, byteorder='little')
    return format(int.from_bytes(raw_bytes, byteorder='big'), '032x')

def compute_md5(input_text):
    message_bytes = bytearray(input_text, 'ascii')
    padded_message = apply_padding(message_bytes)
    digest = process_blocks(padded_message)
    return convert_to_hex_string(digest)

if __name__ == "__main__":
    user_input = input("Enter message: ")
    print("MD5 Hash:", compute_md5(user_input))