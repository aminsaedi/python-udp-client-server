import socket


msgFromClient       = "Hello UDP Server"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024


# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.bind(("127.0.0.1", 20002))

# list with length 100
parts = [0] * 100

while True:
    # print(parts)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = msgFromServer[0].decode("utf-8")

    parts[int(msg)] = 1

    # total count of parts received
    count = 0
    for i in parts:
        count += i
    
    print(F"Dowloaded {count}%")

    # if all parts received
    if count == 100:
        print("All parts received")
        break
