import socket

def text_to_binary(message):
    binary_output = []

    for character in message:
        ascii_code = ord(character)
        binary_output.append(bin(ascii_code)[2:])

    return " ".join(binary_output)

def start_client():
    server_host = socket.gethostname()
    server_port = 1235

    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_socket.connect((server_host, server_port))

    user_message = input("Enter message: ")

    binary_message = text_to_binary(user_message)
    cli_socket.send(binary_message.encode())

    response = cli_socket.recv(1024).decode()
    print(f"Received transformed data: {response}")

    cli_socket.close()

if __name__ == "__main__":
    start_client()
