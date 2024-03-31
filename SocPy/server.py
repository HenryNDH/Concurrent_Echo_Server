import socket
import threading

def handle_client(conn, addr):
    print(f'Connected by {addr}')

    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received from client {addr}: {message}")
        conn.sendall(data)
        if message.strip().lower() == "quit":
            break

    print(f"Connection with {addr} closed.")
    conn.close()

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f'Server started, listening on {host}:{port}')
        s.listen()

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
