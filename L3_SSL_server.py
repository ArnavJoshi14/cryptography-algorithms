import socket

SUB_BOX = [
    14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
    0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
    4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
    15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
]

def apply_sbox(bit_stream):
    cleaned_bits = bit_stream.replace(" ", "")
    output_bits = []

    for pos in range(0, len(cleaned_bits), 6):
        segment = cleaned_bits[pos:pos + 6]

        if len(segment) < 6:
            segment = segment.ljust(6, "0")

        decimal_index = int(segment, 2)
        substituted_value = SUB_BOX[decimal_index]
        output_bits.append(format(substituted_value, "04b"))

    return " ".join(output_bits)

def start_server():
    server_host = socket.gethostname()
    server_port = 1235

    srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_socket.bind((server_host, server_port))
    srv_socket.listen(1)

    print(f"Server running on {server_host}:{server_port}")

    connection, address = srv_socket.accept()
    print(f"Client connected from {address}")

    while True:
        received_data = connection.recv(1024).decode()

        if not received_data:
            break

        print(f"Received binary data: {received_data}")

        transformed_data = apply_sbox(received_data)
        connection.send(transformed_data.encode())

    connection.close()
    srv_socket.close()

if __name__ == "__main__":
    start_server()
