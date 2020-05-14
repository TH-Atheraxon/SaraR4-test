#Ublox Library module code combined with GeeksforGeeks Socket Code
import socket
import sys
import time
import binascii
import serial
import importlib
import ublox

#Module Creation
module = SaraR4Module(serial_port='/dev/ttyAMA0')
#Module Config
module.setup()
#Network Connect
module.connect(operator=383, roaming=True)

#Make socket
try:
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = module.create_socket(socket_type='UDP', port=1337)
    print ("Socket successfully created")
except socket.error as err:
    print ("Socket creation failed with error %s" %(err))
    
#default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    
    #this means could not resolve the host
    print ("There was an error resolving the host")
    sys.exit()
    
#connecting to the server
s.connect((host_ip, port))

print ("The socket has successfully connected to google on port == %s" %(host_ip))