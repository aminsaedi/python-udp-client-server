import socket
from time import sleep
from random import *

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind(("127.0.0.1", 1024))


while(True):
    part = randint(0, 99)
    UDPServerSocket.sendto(str.encode(str(part)), ("127.0.0.1", 20002))
    part += 1
    # print("Sent part: " + str(part))
    sleep(0.1)
