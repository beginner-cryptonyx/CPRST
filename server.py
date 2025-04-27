import socket
import threading


# Handling client requests
def handle_client(client, address):
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(message)
        except Exception as e:
            print(f'Error -> {e}')
        finally:
            client.close()
            break

# Listening Function    
def start_server():
    host = '127.0.0.1'
    port= 6969

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host,port))
    
    server.listen(5)
    print(f"server listening on {host}:{port}")
    
    try:
        while True:
            client, address = server.accept()
            print(f'connection from {address}')
            

            handling_thread = threading.Thread(target=handle_client, args=(client, address))
            handling_thread.daemon = True
            handling_thread.start()
            
            if input("command: ") == "quit":
                break
            
    except KeyboardInterrupt:
        print("shutdown")
    finally:
        server.close()

start_server()