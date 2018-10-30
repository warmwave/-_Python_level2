import unittest
import threading
import client
import server
import socket
from config import *

def create_client():
    s = socket.socket()
    s.connect((ADDRESS, PORT))
    #
    # s.send(b"Hello")
    while True:
        pass

class TestMain(unittest.TestCase):

    def test_send_data(self):
        t = threading.Thread(target=create_client, daemon=True)

        t.start()

        s = socket.socket()
        s.bind((ADDRESS, PORT))
        s.listen(10)
        s.settimeout(3)

        print("Server started")

        try:

            client, addr = s.accept()
            data = client.recv(1024)

            self.assertEqual(data, b"Hello")


            client.close()
            s.close()
        except socket.timeout as err:

            self.fail("Accept failed")






if __name__ == '__main__':
    unittest.main()
