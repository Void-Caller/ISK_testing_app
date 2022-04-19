import socket
import sys



class ISKServer():
    def __init__(self, size=64, address = 'localhost', source_address = 81):
        self.size = size
        self.address = address
        self.source_adress = source_address

    def main_loop(self):
        # Set up a TCP/IP server
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to server address and port 81
        server_address = (self.address, self.source_adress)
        tcp_socket.bind(server_address)

        # Listen on port 81
        tcp_socket.listen(1)

        while True:
            print("Waiting for connection")
            connection, client = tcp_socket.accept()

            try:
                print("Connected to client IP: {}".format(client))

                # Receive and print data 32 bytes at a time, as long as the client is sending something
                while True:
                    data = connection.recv(self.size).decode()
                    print("Data: "+data)

                    if not data:
                        break

            finally:
                connection.close()

if __name__ == '__main__':
    server = ISKServer()
    server.main_loop()