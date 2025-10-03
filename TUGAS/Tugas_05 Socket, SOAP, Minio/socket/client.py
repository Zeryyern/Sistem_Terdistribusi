import socket

# Ask user for server IP
server_ip = input("Enter Server IP (default 127.0.0.1): ").strip()
if not server_ip:
    server_ip = "127.0.0.1"  # fallback if user presses Enter

PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    try:
        client_socket.connect((server_ip, PORT))  # Connect to server
        print(f"Connected to server at {server_ip}:{PORT}")

        # Send a message
        client_socket.sendall(b"Hello from Client")
        reply = client_socket.recv(1024)  # Receive reply
        print("Server replied:", reply.decode())

    except Exception as e:
        print(f"Connection failed: {e}")
