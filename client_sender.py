import socket
import sys
import time

class ISKClient():
    def __init__(self, address = 'localhost', source_address = 81):
        self.address = address
        self.source_address = source_address

    def main_loop(self, iterations=10, num_of_elements = 64, wait = 0):
        # Create a connection to the server application on port 81
        tcp_socket = socket.create_connection((self.address, self.source_address))

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
    address = input("Enter address: ")
    port = int(input("Enter port: "))

    if address and port:
        client = ISKClient(address, port)
    else:
        client = ISKClient()

    iter = int(input("Enter number of messages: "))
    num = int(input("Enter message size in bytes, min 40: "))
    wait = int(input("Enter wait time between messages in miliseconds: "))


    client.main_loop(iterations=iter, num_of_elements=num, wait=wait)