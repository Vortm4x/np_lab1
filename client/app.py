from config import HOST, PORT
import socket
import requester
import select

def main():

    with socket.socket(
        socket.AF_INET, 
        socket.SOCK_STREAM
    ) as client_socket:
        
        client_socket.connect((HOST, PORT))

        request_data = requester.prepare()
        client_socket.sendall(request_data)

        client_socket.setblocking(False)

        readable, writable, exceptional = select.select([client_socket], [], [client_socket])

        for sock in readable:
            if sock is client_socket:

                response_data = sock.recv(1024)

                if response_data:
                    print("Received data:", response_data.decode())
                    requester.handle(response_data.decode())
                else:
                    sock.close()
        
        for sock in exceptional:
            if sock is client_socket:
                sock.close()


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(f"Error occurred: {e}")