from config import HOST, PORT
from socketserver import BaseRequestHandler, TCPServer
from responder import handle
import board
import json


game_board = board.board_create()


class TCPListener(BaseRequestHandler):
    def handle(self) -> None:
        socket = self.request

        request_data = socket.recv(1024).strip()
        
        req_dict = handle(request_data)
        
        board.board_set(game_board, req_dict['x'], req_dict['y'], req_dict['tile'])

        resp_dict = {
           'result' : board.board_check(game_board)
        }

        if resp_dict['result'] == board.TILE_X or resp_dict['result'] == board.TILE_O:
            board.board_reset(game_board)

        socket.sendall(json.dumps(resp_dict).encode())


if __name__ == '__main__':
    with TCPServer((HOST, PORT), TCPListener) as server:
        print(f"Server running on {HOST}:{PORT}")
        server.serve_forever()
    

# from selectors import DefaultSelector, SelectSelector, EVENT_READ
# from socket import socket, AF_INET, SOCK_STREAM, SOCK_NONBLOCK
# from config import HOST, PORT, REQ_QUEUE_MAX
# from queue import Queue


# def accept_connection(server_socket : socket, selector : SelectSelector):
#     client_socket, addr = server_socket.accept()

#     print(f"Accepted connection from {addr}")
#     # client_socket.setblocking(False)
#     selector.register(client_socket, EVENT_READ, data=None)


# def handle_client(client_socket : socket, selector : SelectSelector, req_queue : list):
#     data = client_socket.recv(1024)
#     if data:
#         print(f"Received data from {client_socket.getpeername()}: {data.decode()}")

#     else:
#         print(f"Connection closed by {client_socket.getpeername()}")
#         selector.unregister(client_socket)
#         client_socket.close()


# def main(server_socket : socket, selector : SelectSelector, req_queue : list):
    
    # events = selector.select()

    # for key, mask in events:
    #     if key.fileobj == server_socket:
    #         accept_connection(server_socket, selector)
    #     else:
    #         handle_client(key.fileobj, selector, req_queue)


# if __name__ == '__main__':


    # selector = DefaultSelector()
    # req_queue = list()
    
    # server_socket = socket(AF_INET, SOCK_STREAM | SOCK_NONBLOCK)
    # server_socket.bind((HOST, PORT))
    # server_socket.listen()

    # selector.register(server_socket, EVENT_READ)
    # print(f"Server at {HOST}:{PORT} is running")

    # while True: main(server_socket, selector, req_queue)