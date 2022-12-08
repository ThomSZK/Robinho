#!/usr/bin/env python3

import socket
import cv2
import numpy as np


rxSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
rxSocket.bind(("192.168.101.2",5000))

print("Listening")
try:
    while True:
        data,addr = rxSocket.recvfrom(1000000)
        arr = np.asarray(bytearray(data), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        print("-------")
        print(addr)

        cv2.imwrite('/home/arena/Documents/GitHub/Robinho/Robinho_Webapp/images/pov_feed.png', img)
finally:
    rxSocket.close()
