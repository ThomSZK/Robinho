
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
    ser.write((0x0).to_bytes(1, "little"))
    try:
        while ser.read() != 1:
            print('...x')
        
        ser.write(x.to_bytes(1, "little"))

        while ser.read() != 1:
            print('...y')

        ser.write(y.to_bytes(1, "little"))
        while ser.read() != 1:
            print('...z')

        ser.write(a.to_bytes(1, "little"))
    except:
        print('error: serial to duino')


class robinho_func():
    def arduino_cmd(cmd,foo=0):
        print("send", bin(cmd))

        pose = recvPose()
        sendPose(pose)

        ser.write((cmd).to_bytes(1, "little"))

        while ser.read() != 1:
            print('POSING')
            if(ser.read()!=0):
                break
            pose = recvPose()
            sendPose(pose)
       

        print(ser.read())


if __name__ == '__main__':
    with serial.Serial('/dev/ttyUSB0', 9600, timeout=1) as ser:
        exec(code)
        #ser.write(b'00000001')
        #x = ser.read()          # read one byte
        #line = ser.readline()   # read a '\n' terminated line


