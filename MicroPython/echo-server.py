import socket

#Open a UDP server socket.
socketA = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socketA)
print(type(socketA))

bindAddress = ("localhost", 5070)
socketA.bind(bindAddress)

counter = 1 

while True:
    try:
        data = socketA.recv(1024).decode()  # receive response
        print("data:", data)
        x, y, angle = eval(data)
    except:
         print('no data')
    counter += 1

#Close the server socket.
socketA.close()