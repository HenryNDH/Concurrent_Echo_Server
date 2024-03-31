import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to the server.")

        while True:
            message = input("Enter message to send (type 'quit' to exit): ")
            s.sendall(message.encode())
            if message.lower().strip() == "quit":
                break

            data = s.recv(1024)
            print('Received from server:', data.decode())

        print("Closing connection.")
        s.close()

if __name__ == "__main__":
    start_client()
