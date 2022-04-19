import socket
import sys
import time

class ISKClient():
    def __init__(self, address = 'localhost', source_address = 81):
        self.address = address
        self.source_adress = source_address

    def main_loop(self, iterations=10, num_of_elements = 64, wait = 0):
        # Create a connection to the server application on port 81
        tcp_socket = socket.create_connection((self.address, self.source_adress))

        '''
        rozmiar zakodowanego str to 33+num_of_elements Bytów
        '''

        data = ""
        for i in range(num_of_elements-34):
            data += "k"
        data+="e"

        print(sys.getsizeof(data.encode()))

        try:
            for i in range(iterations):
                tcp_socket.sendall(data.encode())
                if wait:
                    time.sleep(wait/1000)
        finally:
            print("Closing socket")
            tcp_socket.close()

if __name__ == '__main__':
    client = ISKClient()
    client.main_loop(wait=10)