
import serial
import socket

#Open a UDP server socket.
socketA = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socketA)
print(type(socketA))

bindAddress = ("localhost", 5070)
socketA.bind(bindAddress)

uart = 0
ser = 0
code = open('/home/arena/Documents/GitHub/Robinho/MicroPython/sample.py').read()

def getack(ct):
    ack = ser.read(1)
    print("ack", ct , ack)
    return ack != b'1'

def recvPose():
    try:
        data = socketA.recv(1024).decode()  # receive response
        print("data:", data)
        x, y, angle = eval(data)
        return (x,y,angle)
    except:
        print('no data')
        return (0,0,0)

def sendPose(pose):
    x,y,a = pose
    ser.write(0x00.to_bytes(1, "little"))
    try:
        msg = 0
        while getack("x"):
            #msg = ser.read(1)
            #print(msg)
            print('...x')
        
        ser.write(x.to_bytes(1, "little"))

        while getack("y"):
            print('...y')

        ser.write(y.to_bytes(1, "little"))
        while getack("z"):
            print('...z')

        ser.write(a.to_bytes(1, "little"))

        while getack("p"):
            print('...pose end')
    except Exception as e:
        print('error: serial to duino', e)


class robinho_func():
    def arduino_cmd(cmd,foo=0):

        pose = recvPose()
        sendPose(pose)

        print("send", hex(cmd))
        ser.write(cmd.to_bytes(1, "little"))

        while getack("loop"):
            pose = recvPose()
            sendPose(pose)
            print("waiting after ", hex(cmd))
       

        print("end func")

import time

if __name__ == '__main__':
    with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
        time.sleep(3)
        pose = recvPose()
        sendPose(pose)
        exec(code)
        #ser.write(b'00000001')
        #x = ser.read()          # read one byte
        #line = ser.readline()   # read a '\n' terminated line


