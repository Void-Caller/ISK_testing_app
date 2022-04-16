import socket
import sys

class ISKClient():
    def __init__(self):
        pass

    def main_loop(self):
        # Create a connection to the server application on port 81
        tcp_socket = socket.create_connection(('localhost', 81))

        '''
        rozmiar zakodowanego str to 33+num_of_elements Bytów
        '''

        try:
            data = "kk"
            print(sys.getsizeof(data.encode()))
            tcp_socket.sendall(data.encode())

        finally:
            print("Closing socket")
            tcp_socket.close()

if __name__ == '__main__':
    client = ISKClient()
    client.main_loop()