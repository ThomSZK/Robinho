import machine
import socket
import time
import camera
import robinho_func
from machine import Pin
from machine import UART

flash = Pin(4, Pin.OUT)
uart = machine.UART(1, 9600, rx=12, tx=13)
uart.init(9600, bits=8, parity=None, stop=1)
uart.read()


while 1:
  robinho_func.blink(0.1, flash)
  time.sleep(2)
  robinho_func.blink(0.1, flash)
  time.sleep(5)


##############CODIGO DO ALUNO#################
#robinho_func.arduino_cmd(0b00011110, uart, client_socket)
#if (robinho_func.read_floor_color(uart, client_socket) == '#FF0000'):
#  for i in range (3):
#    robinho_func.arduino_cmd(0b00011100, uart, client_socket)
#  robinho_func.arduino_cmd(0b00011110, uart, client_socket)
#  robinho_func.arduino_cmd(0b00011110, uart, client_socket)
#else:
#  robinho_func.arduino_cmd(0b00011010, uart, client_socket);
#  robinho_func.arduino_cmd(0b10011000, uart, client_socket)
#  robinho_func.arduino_cmd(0b00011011, uart, client_socket);
##############################################
    
client_socket.close()

