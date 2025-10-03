import socket

# Server will listen on all network interfaces
HOST = ''
PORT = 5000  # Port number

# Create TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))   # Bind to host and port
    server_socket.listen()             # Start listening
    print(f"Server listening on port {PORT}...")

    # Accept client connection
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)   # Receive data from client
            if not data:
                break                # Exit if client disconnects
            print("Received from client:", data.decode())
            conn.sendall(b"Echo: " + data)  # Send back response
