import RPi.GPIO as GPIO
import time
import socket

GPIO.setmode(GPIO.BCM)
button_pin = 21  
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ip = "192.168.125.110"  
port = 6454

UDP_MESSAGE_LED_ON = bytearray([0x41, 0x72, 0x74, 0x2d, 0x4e, 0x65, 0x74, 0x00, 0x00, 0x50, 0x00, 0x0e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x20, 0xfa, 0xfa, 0xfa, 0xfa, 0xfa, 0xfa, 0xfa, 0xfa, 0xfa, 0xfa, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

UDP_MESSAGE_LED_OFF = bytearray([0x41, 0x72, 0x74, 0x2d, 0x4e, 0x65, 0x74, 0x00, 0x00, 0x50, 0x00, 0x0e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

button_presses = 0

def button_callback(channel):
    global button_presses
    button_presses += 1
    
    if button_presses % 2 == 1:
        print("Switching on")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(UDP_MESSAGE_LED_ON, (ip, port))
        time.sleep(1)
    else:
        print("Switching off")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(UDP_MESSAGE_LED_OFF, (ip, port))
        time.sleep(1)

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
