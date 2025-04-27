import socket
import threading

def listen(client):
    try:
        while True:     
            message = client.recv(1024).decode()
            print(message)
    except:
        print("an error occurred")
        client.close()

        
def start_client():
    try:
        host = '127.0.0.1'
        port= 6969


        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host,port))
        
        print(f"Connected to server at {host}:{port}")
        
        
        receive_thread = threading.Thread(target=listen, args=(client))
        receive_thread.daemon = True
        receive_thread.start()
        
        while True:
            message = input("-> ")
            if message == "quit":
                break
            client.send(message.encode())
            
    finally:
        client.close()
        
start_client()